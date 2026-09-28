"""Explicit, small implementations of representative XAI metrics."""

from .completeness import comprehensiveness, sufficiency
from .complexity import entropy_complexity, gini_sparsity
from .controls import random_attribution
from .faithfulness import aopc, deletion_auc, deletion_curve, faithfulness_correlation
from .robustness import max_sensitivity

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
