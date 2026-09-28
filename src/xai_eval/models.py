"""Compact model and prediction helpers for the benchmark."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


def make_models(*, random_state: int = 42):
    """Build deterministic linear, tree-ensemble, and neural classifiers."""
    return {
        "LogisticRegression": LogisticRegression(max_iter=2000, random_state=random_state),
        "RandomForest": RandomForestClassifier(
            n_estimators=80,
            min_samples_leaf=2,
            random_state=random_state,
            n_jobs=1,
        ),
        "MLP": MLPClassifier(
            hidden_layer_sizes=(32,),
            max_iter=500,
            early_stopping=True,
            random_state=random_state,
        ),
    }


def positive_probability(model, x):
    """Return the probability of the classifier's class 1 for one instance."""
    return float(model.predict_proba(x.reshape(1, -1))[0, 1])