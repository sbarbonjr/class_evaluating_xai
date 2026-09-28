"""Local explanation sensitivity under an explicit perturbation set."""

from collections.abc import Callable

import numpy as np


def max_sensitivity(
    explain: Callable[[np.ndarray], np.ndarray],
    x: np.ndarray,
    perturbations: np.ndarray,
    *,
    radius: float,
    input_norm: int | float = 2,
    explanation_norm: int | float = 2,
) -> float:
    """Return the largest attribution distance inside a specified input neighborhood."""
    instance = np.asarray(x, dtype=float)
    candidates = np.asarray(perturbations, dtype=float)
    if instance.ndim != 1 or candidates.ndim != 2 or candidates.shape[1:] != instance.shape:
        raise ValueError("Expected x shaped (features,) and perturbations shaped (samples, features).")
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    if candidates.shape[0] == 0:
        raise ValueError("At least one perturbation is required.")

    distances = np.linalg.norm(candidates - instance, ord=input_norm, axis=1)
    if np.any(distances > radius + 1e-12):
        raise ValueError("Every perturbation must lie within radius of x.")
    reference = np.asarray(explain(instance), dtype=float)
    if reference.ndim != 1:
        raise ValueError("Explanation function must return a one-dimensional vector.")

    changes = []
    for candidate in candidates:
        explanation = np.asarray(explain(candidate), dtype=float)
        if explanation.shape != reference.shape:
            raise ValueError("Explanation shape changed across perturbations.")
        changes.append(np.linalg.norm(explanation - reference, ord=explanation_norm))
    return float(max(changes))
