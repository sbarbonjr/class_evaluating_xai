"""Small, download-free datasets for the teaching benchmark."""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def breast_cancer_split(*, random_state: int = 42):
    """Return standardized train/test data and original feature names."""
    dataset = load_breast_cancer(as_frame=True)
    x_train, x_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.25,
        random_state=random_state,
        stratify=dataset.target,
    )
    scaler = StandardScaler().fit(x_train)
    return (
        scaler.transform(x_train),
        scaler.transform(x_test),
        y_train.to_numpy(),
        y_test.to_numpy(),
        dataset.feature_names.tolist(),
    )