"""Compare measured deletion curves under distinct baseline conventions."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from xai_eval.explainers import local_perturbation_attribution
from xai_eval.metrics import deletion_curve

dataset = load_breast_cancer()
x_train, x_test, y_train, _ = train_test_split(dataset.data, dataset.target,
                                               test_size=0.25, random_state=42,
                                               stratify=dataset.target)
scaler = StandardScaler().fit(x_train)
x_train, x_test = scaler.transform(x_train), scaler.transform(x_test)
model = LogisticRegression(max_iter=2000, random_state=42).fit(x_train, y_train)
x = x_test[0]
baselines = {"Zero": np.zeros(x.size), "Mean": x_train.mean(axis=0),
             "Median": np.median(x_train, axis=0), "Sample": x_train[1]}
fig, ax = plt.subplots(figsize=(7.2, 4.2))
for label, baseline in baselines.items():
    attribution = local_perturbation_attribution(model, x, baseline=baseline)
    score_fn = lambda point: model.predict_proba(point.reshape(1, -1))[0, 1]
    fractions, scores = deletion_curve(score_fn, x, attribution, baseline=baseline, steps=20)
    ax.plot(fractions * 100, scores, marker=".", label=label)
ax.set(xlabel="Top-ranked features removed (%)", ylabel="Class 1 probability")
ax.set_title("Measured baseline sensitivity on one test case")
ax.legend(title="Replacement", frameon=False)
fig.tight_layout()
out = ROOT / "slides/figures"; out.mkdir(parents=True, exist_ok=True)
fig.savefig(out / "baseline_sensitivity.pdf", bbox_inches="tight")
plt.close(fig)
