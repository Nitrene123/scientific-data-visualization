from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, INK, PRIMARY, SECONDARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "waterfall_contribution_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    labels = ["Baseline", "Volume", "Price", "Mix", "Returns", "Other", "Final"]
    contributions = np.array([120, 38, 24, -18, -11, 9, 0], dtype=float)
    cumulative = np.r_[0, np.cumsum(contributions[:-1])]
    bottoms = np.where(contributions >= 0, cumulative, cumulative + contributions)
    heights = np.abs(contributions)
    bottoms[-1], heights[-1] = 0, cumulative[-1]
    colors = [PRIMARY] + [SECONDARY if v >= 0 else HIGHLIGHT for v in contributions[1:-1]] + [PRIMARY]
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    x = np.arange(len(labels))
    ax.bar(x, heights, bottom=bottoms, color=colors, width=0.68, edgecolor=INK, linewidth=0.35)
    for i in range(len(labels) - 1):
        top = cumulative[i + 1]
        ax.plot([x[i] + 0.34, x[i + 1] - 0.34], [top, top], color="#7A8790", lw=0.75, ls=":")
    for xi, bottom, height, value in zip(x, bottoms, heights, contributions):
        ax.text(xi, bottom + height + 4, f"{value:+.0f}" if xi not in [0, len(labels) - 1] else f"{(bottom + height):.0f}", ha="center", va="bottom", fontsize=8.8, color=INK)
    ax.set_xticks(x, labels)
    ax.set_ylabel("Contribution to total (units)")
    ax.set_title("Waterfall contribution analysis", pad=13, weight="bold")
    ax.grid(True, axis="y", color=GRID, alpha=0.55, linewidth=0.6)
    ax.text(0.98, 0.04, "Green = positive contribution · orange = negative contribution", transform=ax.transAxes, ha="right", va="bottom", fontsize=8.4, color=INK)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
