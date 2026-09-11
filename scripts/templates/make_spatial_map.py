from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "spatial_map_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    regions = [np.array([[0.2, 0.7], [2.3, 1.0], [2.8, 2.5], [1.5, 3.5], [0.1, 2.7]]), np.array([[2.8, 2.5], [4.3, 3.1], [5.5, 2.2], [4.9, 0.8], [2.3, 1.0]]), np.array([[0.1, 2.7], [1.5, 3.5], [3.0, 4.4], [4.3, 3.1], [2.8, 2.5]])]
    colors = ["#d9edf7", "#91c9e8", "#357ebd"]
    rng = np.random.default_rng(20260911)
    fig, ax = plt.subplots(figsize=(8.1, 6.3))
    for region, color in zip(regions, colors):
        ax.add_patch(Polygon(region, closed=True, facecolor=color, edgecolor="white", lw=2.2))
    points = rng.uniform([0.35, 0.95], [5.1, 3.5], (85, 2))
    values = np.exp(rng.normal(1.8, 0.55, points.shape[0]))
    ax.scatter(points[:, 0], points[:, 1], s=values * 3.4, c=values, cmap="YlOrRd", alpha=0.72, edgecolor="white", linewidth=0.5)
    ax.text(0.45, 0.72, "Region 1", fontsize=9)
    ax.text(4.05, 2.45, "Region 2", fontsize=9)
    ax.text(2.45, 3.75, "Region 3", fontsize=9)
    ax.set_xlim(-0.25, 5.9)
    ax.set_ylim(0.35, 4.7)
    ax.set_xlabel("Longitude (schematic)")
    ax.set_ylabel("Latitude (schematic)")
    ax.set_title("Spatial sampling intensity map", pad=14, weight="bold")
    cb = fig.colorbar(ax.collections[-1], ax=ax, pad=0.02)
    cb.set_label("Sampling intensity")
    ax.grid(color="#ffffff", lw=0.8, alpha=0.8)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
