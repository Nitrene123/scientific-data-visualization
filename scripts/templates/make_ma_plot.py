from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, MUTED, PRIMARY, SECONDARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "ma_plot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    mean_expr = rng.uniform(0.0, 9.5, 950)
    log_fc = rng.normal(0, 0.18 + 0.16 * np.exp(-mean_expr / 2.4), mean_expr.size)
    log_fc += 0.85 * np.exp(-((mean_expr - 5.4) / 1.2) ** 2) * (rng.random(mean_expr.size) > 0.62)
    significant = (np.abs(log_fc) > 0.65) & (mean_expr > 1.0)
    colors = np.where(significant & (log_fc > 0), HIGHLIGHT, np.where(significant, SECONDARY, "#C5D0D6"))
    fig, ax = plt.subplots(figsize=(7.8, 5.8))
    ax.scatter(mean_expr, log_fc, s=18, c=colors, alpha=0.72, edgecolor="none")
    ax.axhline(0, color="#7A8790", lw=0.85)
    ax.axhline(0.65, color=MUTED, ls="--", lw=0.85)
    ax.axhline(-0.65, color=MUTED, ls="--", lw=0.85)
    ax.set(xlabel="Mean log expression", ylabel="Log2 fold change")
    ax.set_title("MA plot for differential expression", pad=13, weight="bold")
    ax.grid(True, color=GRID, alpha=0.45, linewidth=0.55)
    ax.text(0.02, 0.96, f"|log2FC| > 0.65 · {significant.sum()} highlighted features", transform=ax.transAxes, va="top", fontsize=8.8, color=MUTED)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
