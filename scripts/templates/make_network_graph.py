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
    out = ROOT / "outputs" / "network_graph_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans"})
    labels = ["Gene A", "Gene B", "Gene C", "Gene D", "Gene E", "Gene F", "Gene G", "Gene H", "Gene I", "Gene J"]
    groups = np.array([0, 0, 1, 1, 1, 2, 2, 0, 2, 1])
    colors = ["#4e79a7", "#e15759", "#59a14f"]
    edges = [(0, 1, 4), (0, 2, 2), (0, 7, 3), (1, 3, 2), (1, 4, 1), (2, 4, 3), (2, 5, 2), (3, 6, 3), (4, 8, 2), (5, 6, 4), (5, 9, 1), (6, 8, 2), (7, 9, 3), (8, 9, 2)]
    theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False) + 0.12
    xy = np.column_stack([np.cos(theta), np.sin(theta)])
    fig, ax = plt.subplots(figsize=(7.6, 7.0))
    for i, j, weight in edges:
        ax.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]], color="#98a6b3", lw=0.7 + weight * 0.45, alpha=0.52, zorder=1)
    sizes = np.array([850, 700, 930, 600, 780, 640, 1020, 560, 720, 660])
    ax.scatter(xy[:, 0], xy[:, 1], s=sizes, c=[colors[g] for g in groups], edgecolor="white", linewidth=1.8, zorder=3)
    for (x, y), label in zip(xy, labels):
        ax.text(1.14 * x, 1.14 * y, label, ha="center", va="center", fontsize=9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Interaction network with weighted edges", pad=18, weight="bold")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
