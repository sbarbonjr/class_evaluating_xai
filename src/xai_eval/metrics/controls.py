"""Negative-control attributions for evaluation protocols."""

import numpy as np


def random_attribution(n_features: int, *, random_state: int = 0) -> np.ndarray:
    """Generate a reproducible non-negative random attribution vector."""
    if n_features < 1:
        raise ValueError("n_features must be at least 1.")
    return np.random.default_rng(random_state).uniform(size=n_features)
