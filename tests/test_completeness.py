import numpy as np

from xai_eval.metrics import comprehensiveness, sufficiency


def test_comprehensiveness_and_sufficiency_on_linear_model():
    model = lambda x: float(x[0] + 2 * x[1])
    x = np.array([3.0, 4.0])

    assert comprehensiveness(model, x, [1], baseline=0.0) == 8.0
    assert sufficiency(model, x, [1], baseline=0.0) == 3.0


def test_boolean_feature_mask_is_supported():
    model = lambda x: float(x.sum())
    assert comprehensiveness(model, np.array([2.0, 5.0]), np.array([False, True]), baseline=0.0) == 5.0
