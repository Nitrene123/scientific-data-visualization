from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "sankey_flow_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def ribbon(ax: plt.Axes, x0: float, x1: float, y0: float, y1: float, width0: float, width1: float, color: str) -> None:
    control = (x1 - x0) * 0.45
    vertices = [
        (x0, y0), (x0 + control, y0), (x1 - control, y1), (x1, y1),
        (x1, y1 + width1), (x1 - control, y1 + width1), (x0 + control, y0 + width0), (x0, y0 + width0),
    ]
    ax.add_patch(Polygon(vertices, closed=True, facecolor=color, edgecolor="none", alpha=0.42))


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    colors = {"A": "#4e79a7", "B": "#f28e2b", "C": "#59a14f", "D": "#e15759"}
    flows = [("A", "A", 34), ("A", "B", 18), ("B", "B", 24), ("B", "C", 20), ("C", "C", 28), ("C", "D", 13), ("D", "A", 10), ("D", "D", 18)]
    fig, ax = plt.subplots(figsize=(8.5, 5.8))
    left_y = {"A": 3.35, "B": 2.15, "C": 1.05, "D": 0.15}
    right_y = {"A": 2.95, "B": 2.0, "C": 1.0, "D": 0.05}
    offsets_left = {key: 0.0 for key in left_y}
    offsets_right = {key: 0.0 for key in right_y}
    for source, target, amount in flows:
        width = amount / 22
        ribbon(ax, 0.18, 0.82, left_y[source] + offsets_left[source], right_y[target] + offsets_right[target], width, width, colors[source])
        offsets_left[source] += width
        offsets_right[target] += width
    for x, positions, title in [(0.12, left_y, "Baseline state"), (0.83, right_y, "Follow-up state")]:
        for key, y in positions.items():
            ax.add_patch(Rectangle((x, y), 0.08, 0.64, facecolor=colors[key], edgecolor="white", lw=1.0, zorder=3))
            ax.text(x + (-0.025 if x < 0.5 else 0.105), y + 0.32, f"State {key}", ha="right" if x < 0.5 else "left", va="center", fontsize=9)
        ax.text(x + 0.04, 4.38, title, ha="center", weight="bold", fontsize=11)
    ax.set_xlim(0, 1.12)
    ax.set_ylim(-0.15, 4.55)
    ax.axis("off")
    ax.set_title("Alluvial flow of samples between states", pad=16, weight="bold")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
