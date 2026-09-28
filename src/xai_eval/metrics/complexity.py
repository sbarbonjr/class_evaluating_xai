"""Attribution concentration measures used as compactness proxies."""

import numpy as np


def _nonnegative_weights(attribution: np.ndarray) -> np.ndarray:
    values = np.abs(np.asarray(attribution, dtype=float)).reshape(-1)
    if values.size == 0:
        raise ValueError("Attribution must contain at least one value.")
    if not np.all(np.isfinite(values)):
        raise ValueError("Attribution values must be finite.")
    return values


def entropy_complexity(attribution: np.ndarray) -> float:
    """Return Shannon entropy of normalized absolute attributions; lower is more concentrated."""
    values = _nonnegative_weights(attribution)
    total = values.sum()
    if total == 0:
        return 0.0
    probabilities = values[values > 0] / total
    return float(-np.sum(probabilities * np.log(probabilities)))


def gini_sparsity(attribution: np.ndarray) -> float:
    """Return finite-sample-corrected Gini concentration in [0, 1]; higher is sparser."""
    values = np.sort(_nonnegative_weights(attribution))
    n_features = values.size
    total = values.sum()
    if total == 0 or n_features == 1:
        return 0.0
    ranks = np.arange(1, n_features + 1)
    raw_gini = np.sum((2 * ranks - n_features - 1) * values) / (n_features * total)
    return float(raw_gini * n_features / (n_features - 1))
