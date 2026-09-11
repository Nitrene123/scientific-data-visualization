from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "volcano_plot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    n = 850
    log_fc = rng.normal(0, 1.0, n)
    neg_log_p = np.clip(rng.gamma(1.6, 1.25, n) + np.abs(log_fc) * 0.72 - 0.5, 0, None)
    threshold_fc, threshold_p = 1.0, 1.3
    significant = (np.abs(log_fc) >= threshold_fc) & (neg_log_p >= threshold_p)
    colors = np.where(significant & (log_fc > 0), "#d73027", np.where(significant, "#4575b4", "#bdbdbd"))
    fig, ax = plt.subplots(figsize=(8.0, 6.3))
    ax.scatter(log_fc, neg_log_p, s=22, c=colors, alpha=0.72, edgecolor="none")
    ax.axvline(-threshold_fc, color="#555555", lw=1, ls="--")
    ax.axvline(threshold_fc, color="#555555", lw=1, ls="--")
    ax.axhline(threshold_p, color="#555555", lw=1, ls="--")
    label_idx = np.argsort(neg_log_p + np.abs(log_fc))[-8:]
    for idx in label_idx:
        ax.annotate(f"Gene{idx + 1}", (log_fc[idx], neg_log_p[idx]), xytext=(5, 5), textcoords="offset points", fontsize=8)
    ax.set_xlabel("log2 fold change")
    ax.set_ylabel("−log10 adjusted p-value")
    ax.set_title("Differential-expression volcano plot", pad=14, weight="bold")
    ax.text(0.02, 0.95, f"FDR < {10 ** (-threshold_p):.3f}\n|log2FC| ≥ {threshold_fc:.1f}", transform=ax.transAxes, va="top", fontsize=9, color="#444444")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
