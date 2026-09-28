"""Comprehensiveness and sufficiency for a selected set of features."""

import numpy as np

from ._utils import ScoreFunction, as_baseline, as_instance, score


def _selected_indices(selected: np.ndarray, n_features: int) -> np.ndarray:
    indices = np.asarray(selected)
    if indices.dtype == bool:
        if indices.shape != (n_features,):
            raise ValueError("Boolean feature mask must match the instance shape.")
        indices = np.flatnonzero(indices)
    else:
        indices = indices.astype(int, copy=False).reshape(-1)
    if indices.size == 0 or np.any(indices < 0) or np.any(indices >= n_features):
        raise ValueError("selected must contain valid feature indices.")
    return np.unique(indices)


def comprehensiveness(
    model: ScoreFunction,
    x: np.ndarray,
    selected: np.ndarray,
    *,
    baseline: float | np.ndarray,
) -> float:
    """Return original score minus score after removing selected features; higher is better."""
    instance = as_instance(x)
    indices = _selected_indices(selected, instance.size)
    perturbed = instance.copy()
    perturbed[indices] = as_baseline(baseline, instance)[indices]
    return score(model, instance) - score(model, perturbed)


def sufficiency(
    model: ScoreFunction,
    x: np.ndarray,
    selected: np.ndarray,
    *,
    baseline: float | np.ndarray,
) -> float:
    """Return absolute score change when only selected features are retained; lower is better."""
    instance = as_instance(x)
    indices = _selected_indices(selected, instance.size)
    retained = as_baseline(baseline, instance).copy()
    retained[indices] = instance[indices]
    return abs(score(model, instance) - score(model, retained))
