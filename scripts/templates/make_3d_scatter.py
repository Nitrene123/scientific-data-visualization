from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, QUALITATIVE


def configure_matplotlib() -> None:
    mpl.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"], "svg.fonttype": "none", "pdf.fonttype": 42, "font.size": 9.5})


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "3d_scatter_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    configure_matplotlib()
    rng = np.random.default_rng(20260911)
    centers = np.array([[-1.4, -0.7, -0.8], [0.2, 0.9, 0.6], [1.35, -0.2, 1.0], [0.25, -1.1, -0.1]])
    fig = plt.figure(figsize=(8.5, 6.8))
    ax = fig.add_subplot(111, projection="3d")
    for idx, center in enumerate(centers):
        points = rng.normal(size=(55, 3)) @ np.array([[0.32, 0.06, 0.02], [0.02, 0.25, 0.05], [0.02, 0.06, 0.28]]) + center
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=22, color=QUALITATIVE[idx], alpha=0.76, edgecolor="white", linewidth=0.25, label=f"Cluster {idx + 1}")
        ax.scatter(*center, s=75, color=QUALITATIVE[idx], edgecolor="black", linewidth=0.7, marker="X", depthshade=False)
    ax.set_xlabel("Feature 1", labelpad=6)
    ax.set_ylabel("Feature 2", labelpad=6)
    ax.set_zlabel("Feature 3", labelpad=6)
    ax.set_title("3D scatter with clustered observations", pad=15, weight="bold")
    ax.view_init(elev=26, azim=-55)
    ax.set_box_aspect((1.1, 1.0, 0.9))
    ax.grid(True, color=GRID, alpha=0.35, linewidth=0.5)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.98), frameon=True, framealpha=0.9, fontsize=8.5)
    save(fig)


if __name__ == "__main__":
    main()
