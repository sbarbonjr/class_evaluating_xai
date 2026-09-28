import numpy as np

from xai_eval.metrics import random_attribution


def test_random_attribution_is_reproducible():
    first = random_attribution(5, random_state=12)
    second = random_attribution(5, random_state=12)
    np.testing.assert_array_equal(first, second)