"""Perturbation-based faithfulness metrics for feature attributions."""

from collections.abc import Callable

import numpy as np

from ._utils import ScoreFunction, as_baseline, as_instance, score


def deletion_curve(
    model: ScoreFunction,
    x: np.ndarray,
    attribution: np.ndarray,
    *,
    baseline: float | np.ndarray,
    steps: int = 20,
) -> tuple[np.ndarray, np.ndarray]:
    """Return removed-feature fractions and model scores in most-important-first order."""
    instance = as_instance(x)
    values = np.asarray(attribution, dtype=float)
    if values.shape != instance.shape:
        raise ValueError("Attribution shape must match the instance shape.")
    if steps < 1:
        raise ValueError("steps must be at least 1.")

    replacement = as_baseline(baseline, instance)
    order = np.argsort(-np.abs(values), kind="stable")
    removed_counts = np.unique(np.rint(np.linspace(0, instance.size, min(steps, instance.size) + 1)).astype(int))
    fractions = removed_counts / instance.size
    scores = np.empty(removed_counts.size, dtype=float)
    for index, count in enumerate(removed_counts):
        perturbed = instance.copy()
        perturbed[order[:count]] = replacement[order[:count]]
        scores[index] = score(model, perturbed)
    return fractions, scores


def deletion_auc(
    model: ScoreFunction,
    x: np.ndarray,
    attribution: np.ndarray,
    *,
    baseline: float | np.ndarray,
    steps: int = 20,
) -> float:
    """Return normalized area under the deletion curve; lower is generally better."""
    fractions, scores = deletion_curve(model, x, attribution, baseline=baseline, steps=steps)
    widths = np.diff(fractions)
    return float(np.sum((scores[:-1] + scores[1:]) * widths / 2))


def aopc(
    model: ScoreFunction,
    x: np.ndarray,
    attribution: np.ndarray,
    *,
    baseline: float | np.ndarray,
    steps: int = 20,
) -> float:
    """Return average output drop along deletion; higher is generally better."""
    _, scores = deletion_curve(model, x, attribution, baseline=baseline, steps=steps)
    if scores.size == 1:
        return 0.0
    return float(np.mean(scores[0] - scores[1:]))


def faithfulness_correlation(
    model: ScoreFunction,
    x: np.ndarray,
    attribution: np.ndarray,
    *,
    baseline: float | np.ndarray,
    n_subsets: int = 100,
    subset_fraction: float = 0.2,
    random_state: int = 0,
) -> float:
    """Correlate subset attribution sums with output changes after replacement."""
    instance = as_instance(x)
    values = np.asarray(attribution, dtype=float)
    if values.shape != instance.shape:
        raise ValueError("Attribution shape must match the instance shape.")
    if n_subsets < 2:
        raise ValueError("n_subsets must be at least 2.")
    if not 0 < subset_fraction <= 1:
        raise ValueError("subset_fraction must be in (0, 1].")

    replacement = as_baseline(baseline, instance)
    subset_size = max(1, int(round(instance.size * subset_fraction)))
    original_score = score(model, instance)
    rng = np.random.default_rng(random_state)
    attribution_sums = np.empty(n_subsets)
    output_changes = np.empty(n_subsets)
    for index in range(n_subsets):
        selected = rng.choice(instance.size, size=subset_size, replace=False)
        perturbed = instance.copy()
        perturbed[selected] = replacement[selected]
        attribution_sums[index] = values[selected].sum()
        output_changes[index] = original_score - score(model, perturbed)

    if np.std(attribution_sums) == 0 or np.std(output_changes) == 0:
        return 0.0
    return float(np.corrcoef(attribution_sums, output_changes)[0, 1])
