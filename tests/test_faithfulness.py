import numpy as np

from xai_eval.metrics import aopc, deletion_auc, deletion_curve, faithfulness_correlation


def linear_score(x):
    return float(np.dot(np.array([1.0, 2.0, 0.0]), x))


def test_deletion_ranks_important_features_first():
    fractions, scores = deletion_curve(
        linear_score,
        np.array([1.0, 1.0, 9.0]),
        np.array([1.0, 2.0, 0.0]),
        baseline=0.0,
        steps=3,
    )

    np.testing.assert_allclose(fractions, [0, 1 / 3, 2 / 3, 1])
    np.testing.assert_allclose(scores, [3.0, 1.0, 0.0, 0.0])


def test_deletion_metric_directions_are_consistent():
    x = np.array([1.0, 1.0, 9.0])
    good = np.array([1.0, 2.0, 0.0])
    random = np.array([0.0, 0.0, 1.0])

    assert deletion_auc(linear_score, x, good, baseline=0.0, steps=3) < deletion_auc(
        linear_score, x, random, baseline=0.0, steps=3
    )
    assert aopc(linear_score, x, good, baseline=0.0, steps=3) > aopc(
        linear_score, x, random, baseline=0.0, steps=3
    )


def test_faithfulness_correlation_is_reproducible():
    result = faithfulness_correlation(
        linear_score,
        np.array([1.0, 1.0, 9.0]),
        np.array([1.0, 2.0, 0.0]),
        baseline=0.0,
        n_subsets=30,
        subset_fraction=1 / 3,
        random_state=7,
    )
    assert -1.0 <= result <= 1.0
    assert result == faithfulness_correlation(
        linear_score,
        np.array([1.0, 1.0, 9.0]),
        np.array([1.0, 2.0, 0.0]),
        baseline=0.0,
        n_subsets=30,
        subset_fraction=1 / 3,
        random_state=7,
    )
