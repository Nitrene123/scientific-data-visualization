from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from palette import GRID, INK, QUALITATIVE, WHITE


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "treemap_hierarchy_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    data = [("Metabolism", [("Carbohydrate", 28), ("Lipid", 17), ("Amino acid", 12)]), ("Signaling", [("MAPK", 18), ("PI3K", 14), ("Wnt", 9)]), ("Cellular", [("Transport", 13), ("Cycle", 11), ("Apoptosis", 7)]), ("Immune", [("Innate", 10), ("Adaptive", 8), ("Cytokine", 6)])]
    total = sum(value for _, children in data for _, value in children)
    fig, ax = plt.subplots(figsize=(8.8, 5.8))
    x0 = 0.0
    for group_idx, (group, children) in enumerate(data):
        group_total = sum(value for _, value in children)
        width = group_total / total
        ax.add_patch(Rectangle((x0, 0), width, 1, facecolor=QUALITATIVE[group_idx], alpha=0.18, edgecolor=WHITE, lw=2.0))
        ax.text(x0 + width * 0.02, 0.96, group, ha="left", va="top", fontsize=10, weight="bold", color=INK)
        y0 = 0.0
        for child_idx, (child, value) in enumerate(children):
            height = value / group_total
            ax.add_patch(Rectangle((x0, y0), width, height, facecolor=QUALITATIVE[group_idx], alpha=0.42 + 0.12 * child_idx, edgecolor=WHITE, lw=1.1))
            if width * height > 0.035:
                ax.text(x0 + width * 0.03, y0 + height * 0.50, f"{child}\n{value}", ha="left", va="center", fontsize=8.5, color=INK)
            y0 += height
        x0 += width
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("Hierarchical composition treemap", pad=16, weight="bold", fontsize=13)
    ax.text(0, -0.06, "Area encodes contribution; nested blocks preserve parent–child structure.", transform=ax.transAxes, fontsize=8.7, color="#667784")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
