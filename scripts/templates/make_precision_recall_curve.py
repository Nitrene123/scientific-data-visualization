from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from palette import MUTED, PRIMARY, apply_paper_style
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "precision_recall_curve_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    apply_paper_style()
    rng = np.random.default_rng(20260911)
    n_pos, n_neg = 170, 830
    scores_pos = rng.normal(0.74, 0.18, n_pos)
    scores_neg = rng.normal(0.27, 0.19, n_neg)
    scores = np.clip(np.r_[scores_pos, scores_neg], 0, 1)
    labels = np.r_[np.ones(n_pos, dtype=int), np.zeros(n_neg, dtype=int)]
    order = np.argsort(-scores, kind="stable")
    sorted_labels = labels[order]
    precision = np.cumsum(sorted_labels) / np.arange(1, labels.size + 1)
    recall = np.cumsum(sorted_labels) / n_pos
    recall = np.r_[0.0, recall]
    precision = np.r_[1.0, precision]
    integrate = getattr(np, "trapezoid", np.trapz)
    ap = float(integrate(precision[1:], recall[1:]))
    baseline = n_pos / labels.size

    fig, ax = plt.subplots(figsize=(7.4, 6.0))
    ax.step(recall, precision, where="post", color=PRIMARY, lw=1.7, label=f"Model (AP = {ap:.3f})")
    ax.axhline(baseline, color=MUTED, ls="--", lw=1.0, label=f"Prevalence baseline = {baseline:.2f}")
    ax.set(xlim=(0, 1), ylim=(0, 1.02), xlabel="Recall / sensitivity", ylabel="Precision / positive predictive value")
    ax.set_title("Precision–recall curve for an imbalanced classifier", pad=13, weight="bold")
    ax.grid(True, color="#D9D9D9", linestyle="--", alpha=0.65, linewidth=0.55)
    ax.legend(loc="lower left", frameon=True, framealpha=0.90, fontsize=9)
    ax.text(0.98, 0.04, "Positive class: 17%", transform=ax.transAxes, ha="right", va="bottom", fontsize=9, color="#555555")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
