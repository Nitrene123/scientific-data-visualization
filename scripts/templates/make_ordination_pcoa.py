from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "ordination_pcoa_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    names = ["Control", "Treatment A", "Treatment B", "Treatment C"]
    centers = np.array([[-1.6, -0.7], [0.4, 0.7], [1.55, -0.45], [0.25, -1.55]])
    colors = ["#4c78a8", "#f58518", "#54a24b", "#b279a2"]
    fig, ax = plt.subplots(figsize=(7.8, 6.6))
    for name, center, color in zip(names, centers, colors):
        points = rng.normal(size=(34, 2)) @ np.array([[0.34, 0.10], [-0.04, 0.26]]) + center
        ax.scatter(points[:, 0], points[:, 1], s=38, color=color, alpha=0.78, edgecolor="white", linewidth=0.5, label=name)
        ellipse = Ellipse(center, 1.35, 1.05, angle=18, facecolor=color, edgecolor=color, alpha=0.12, lw=1.8)
        ax.add_patch(ellipse)
    ax.axhline(0, color="#aaaaaa", lw=0.7, ls="--")
    ax.axvline(0, color="#aaaaaa", lw=0.7, ls="--")
    ax.set_xlabel("PCoA axis 1 (32.4%)")
    ax.set_ylabel("PCoA axis 2 (18.7%)")
    ax.set_title("Principal coordinates analysis", pad=14, weight="bold")
    ax.legend(frameon=False, title="Group", loc="upper left")
    ax.text(0.98, 0.02, "PERMANOVA p = 0.003", transform=ax.transAxes, ha="right", fontsize=9, color="#555555")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
