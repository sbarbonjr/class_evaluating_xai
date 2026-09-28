"""Simple attribution methods used in the reproducible default benchmark."""

import numpy as np

from .metrics._utils import as_baseline
from .models import positive_probability


def local_perturbation_attribution(model, x: np.ndarray, *, baseline: np.ndarray) -> np.ndarray:
    """Estimate local feature effects by replacing one feature at a time."""
    instance = np.asarray(x, dtype=float)
    replacement = as_baseline(baseline, instance)
    original = positive_probability(model, instance)
    attribution = np.empty_like(instance)
    for feature_index in range(instance.size):
        perturbed = instance.copy()
        perturbed[feature_index] = replacement[feature_index]
        attribution[feature_index] = original - positive_probability(model, perturbed)
    return attribution


def model_specific_attribution(model, x: np.ndarray) -> np.ndarray:
    """Return linear-model contributions for one instance."""
    if hasattr(model, "coef_"):
        return np.asarray(model.coef_[0], dtype=float) * np.asarray(x, dtype=float)
    raise TypeError(f"No local model-specific attribution available for {type(model).__name__}.")