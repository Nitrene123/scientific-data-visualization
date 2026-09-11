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
    out = ROOT / "outputs" / "umap_clusters_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    centers = np.array([[-1.8, 0.9], [-0.35, 1.2], [1.45, 0.55], [-1.15, -1.15], [0.55, -1.0], [1.75, -1.45]])
    colors = ["#e15759", "#59a14f", "#4e79a7", "#f28e2b", "#b07aa1", "#76b7b2"]
    fig, ax = plt.subplots(figsize=(7.8, 6.6))
    for idx, (center, color) in enumerate(zip(centers, colors)):
        angle = idx * 0.55
        transform = np.array([[0.34, 0.10 * np.cos(angle)], [0.02 * np.sin(angle), 0.26]])
        points = rng.normal(size=(42, 2)) @ transform + center
        ax.scatter(points[:, 0], points[:, 1], s=29, color=color, alpha=0.78, edgecolor="white", linewidth=0.4, label=f"Cluster {idx + 1}")
        ax.text(*center, f"C{idx + 1}", ha="center", va="center", fontsize=11, weight="bold", color="#202020")
    ax.set_xlabel("UMAP 1")
    ax.set_ylabel("UMAP 2")
    ax.set_title("UMAP embedding with annotated clusters", pad=14, weight="bold")
    ax.legend(frameon=False, ncol=2, loc="upper left", fontsize=9)
    ax.grid(color="#eeeeee", lw=0.7)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
