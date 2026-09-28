"""Teaching utilities for quantitative XAI evaluation."""

from .metrics import (
    aopc,
    comprehensiveness,
    deletion_auc,
    deletion_curve,
    entropy_complexity,
    faithfulness_correlation,
    gini_sparsity,
    max_sensitivity,
    random_attribution,
    sufficiency,
)

__all__ = [
    "aopc",
    "comprehensiveness",
    "deletion_auc",
    "deletion_curve",
    "entropy_complexity",
    "faithfulness_correlation",
    "gini_sparsity",
    "max_sensitivity",
    "random_attribution",
    "sufficiency",
]
