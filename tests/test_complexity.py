import numpy as np

from xai_eval.metrics import entropy_complexity, gini_sparsity


def test_concentrated_attribution_has_lower_entropy_and_higher_sparsity():
    concentrated = np.array([1.0, 0.0, 0.0])
    diffuse = np.array([1.0, 1.0, 1.0])

    assert entropy_complexity(concentrated) < entropy_complexity(diffuse)
    assert gini_sparsity(concentrated) == 1.0
    assert gini_sparsity(diffuse) == 0.0
