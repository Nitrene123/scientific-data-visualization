from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, PRIMARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "det_curve_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def curve(scores: np.ndarray, labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    order = np.argsort(-scores, kind="stable")
    y = labels[order]
    tp = np.cumsum(y)
    fp = np.cumsum(1 - y)
    positives, negatives = y.sum(), (1 - y).sum()
    fpr = fp / negatives
    fnr = (positives - tp) / positives
    return np.r_[0.0, fpr, 1.0], np.r_[1.0, fnr, 0.0]


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    labels = np.r_[np.ones(260, dtype=int), np.zeros(740, dtype=int)]
    scores = np.r_[rng.normal(0.72, 0.18, 260), rng.normal(0.30, 0.21, 740)]
    fpr, fnr = curve(np.clip(scores, 0, 1), labels)
    fig, ax = plt.subplots(figsize=(7.3, 5.8))
    ax.plot(fpr, fnr, color=PRIMARY, lw=2.0, label="Model")
    ax.plot([0, 1], [1, 0], color="#7A8790", ls="--", lw=0.9, label="Reference")
    ax.fill_between(fpr, fnr, 0.0, color=PRIMARY, alpha=0.10)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="False positive rate", ylabel="False negative rate")
    ax.set_title("Detection error trade-off (DET curve)", pad=13, weight="bold")
    ax.grid(True, color=GRID, alpha=0.50, linewidth=0.6)
    ax.legend(loc="upper right", frameon=True, framealpha=0.9, fontsize=9)
    ax.text(0.03, 0.04, "Positive class prevalence = 26%", transform=ax.transAxes, fontsize=8.7, color=HIGHLIGHT)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
