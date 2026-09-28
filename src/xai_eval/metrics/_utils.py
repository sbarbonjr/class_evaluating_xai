"""Shared validation and model-output helpers for the metric examples."""

from collections.abc import Callable

import numpy as np

ScoreFunction = Callable[[np.ndarray], float]


def as_instance(values: np.ndarray) -> np.ndarray:
    """Return a validated one-dimensional numeric instance."""
    instance = np.asarray(values, dtype=float)
    if instance.ndim != 1:
        raise ValueError("Expected a one-dimensional instance.")
    return instance


def as_baseline(baseline: float | np.ndarray, instance: np.ndarray) -> np.ndarray:
    """Broadcast a scalar or feature-wise baseline to the instance shape."""
    try:
        return np.broadcast_to(np.asarray(baseline, dtype=float), instance.shape)
    except ValueError as error:
        raise ValueError("Baseline must be scalar or match the instance shape.") from error


def score(model: ScoreFunction, instance: np.ndarray) -> float:
    """Evaluate a scalar-output model and reject non-scalar results."""
    value = np.asarray(model(instance), dtype=float)
    if value.size != 1:
        raise ValueError("Model must return one scalar score per instance.")
    return float(value.reshape(-1)[0])
