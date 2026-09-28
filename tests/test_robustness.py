import numpy as np
import pytest

from xai_eval.metrics import max_sensitivity


def test_max_sensitivity_measures_largest_explanation_change():
    explain = lambda x: np.array([x[0], 2 * x[1]])
    result = max_sensitivity(
        explain,
        np.array([0.0, 0.0]),
        np.array([[0.1, 0.0], [0.0, 0.2]]),
        radius=0.2,
    )
    assert result == pytest.approx(0.4)


def test_max_sensitivity_rejects_perturbations_outside_radius():
    with pytest.raises(ValueError, match="within radius"):
        max_sensitivity(
            lambda x: x,
            np.array([0.0]),
            np.array([[0.2]]),
            radius=0.1,
        )
