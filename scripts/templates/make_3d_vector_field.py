from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, PRIMARY, SECONDARY, SEQUENTIAL_SAFE


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "3d_vector_field_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"], "svg.fonttype": "none", "pdf.fonttype": 42})
    axis = np.linspace(-1.5, 1.5, 5)
    xx, yy, zz = np.meshgrid(axis, axis, axis, indexing="ij")
    u, v, w = -yy, xx, 0.45 * zz
    magnitude = np.sqrt(u**2 + v**2 + w**2)
    colors = plt.get_cmap(SEQUENTIAL_SAFE)((magnitude - magnitude.min()) / (magnitude.max() - magnitude.min()))
    fig = plt.figure(figsize=(8.6, 6.8))
    ax = fig.add_subplot(111, projection="3d")
    ax.quiver(xx, yy, zz, u, v, w, length=0.28, normalize=True, colors=colors.reshape(-1, 4), arrow_length_ratio=0.25, linewidth=0.75, alpha=0.78)
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], color=HIGHLIGHT, lw=2.0, label="Reference axis")
    ax.scatter([0], [0], [0], color=PRIMARY, s=65, edgecolor="white", linewidth=0.8, depthshade=False, label="Origin")
    ax.set(xlabel="X coordinate", ylabel="Y coordinate", zlabel="Z coordinate")
    ax.set_title("3D vector field / quiver plot", pad=15, weight="bold")
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=24, azim=-58)
    ax.grid(True, color=GRID, alpha=0.30, linewidth=0.5)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.98), frameon=True, framealpha=0.9, fontsize=8.5)
    ax.text2D(0.02, 0.03, "Arrow direction encodes the vector; length is normalized for readability.", transform=ax.transAxes, fontsize=8.5, color=SECONDARY)
    save(fig)


if __name__ == "__main__":
    main()
