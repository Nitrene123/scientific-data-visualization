from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.colors import to_rgba
import numpy as np

from palette import INK, QUALITATIVE, WHITE


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "sunburst_hierarchy_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    data = [("Metabolism", [("Carbohydrate", 28), ("Lipid", 17), ("Amino acid", 12)]), ("Signaling", [("MAPK", 18), ("PI3K", 14), ("Wnt", 9)]), ("Cellular", [("Transport", 13), ("Cycle", 11), ("Apoptosis", 7)]), ("Immune", [("Innate", 10), ("Adaptive", 8), ("Cytokine", 6)])]
    total = sum(value for _, children in data for _, value in children)
    fig, ax = plt.subplots(figsize=(7.2, 7.2), subplot_kw={"aspect": "equal"})
    start = 90.0
    for group_idx, (group, children) in enumerate(data):
        group_total = sum(value for _, value in children)
        span = 360 * group_total / total
        end = start - span
        base_color = QUALITATIVE[group_idx]
        ax.add_patch(Wedge((0, 0), 0.46, end, start, width=0.44, facecolor=base_color, edgecolor=WHITE, lw=1.4))
        child_start = start
        for child_idx, (child, value) in enumerate(children):
            child_span = span * value / group_total
            child_end = child_start - child_span
            color = to_rgba(base_color, 0.45 + 0.13 * child_idx)
            ax.add_patch(Wedge((0, 0), 0.90, child_end, child_start, width=0.43, facecolor=color, edgecolor=WHITE, lw=1.1))
            mid = (child_start + child_end) / 2
            if child_span > 22:
                angle = np.deg2rad(mid)
                ax.text(0.69 * np.cos(angle), 0.69 * np.sin(angle), child, ha="center", va="center", fontsize=7.7, color=INK, rotation=mid - 90 if -90 < mid < 90 else mid + 90)
            child_start = child_end
        mid = (start + end) / 2
        angle = np.deg2rad(mid)
        ax.text(0.28 * np.cos(angle), 0.28 * np.sin(angle), group, ha="center", va="center", fontsize=8.6, weight="bold", color=INK)
        start = end
    ax.text(0, 0, "Total\ncomposition", ha="center", va="center", fontsize=10, weight="bold", color=INK)
    ax.set_xlim(-1.04, 1.04)
    ax.set_ylim(-1.04, 1.04)
    ax.axis("off")
    ax.set_title("Sunburst hierarchy of pathway composition", pad=18, weight="bold", fontsize=13)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
