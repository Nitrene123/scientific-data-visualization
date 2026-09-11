from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, SEQUENTIAL_SAFE


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "3d_volume_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"], "svg.fonttype": "none", "pdf.fonttype": 42})
    axis = np.linspace(-2.0, 2.0, 9)
    xx, yy, zz = np.meshgrid(axis, axis, axis, indexing="ij")
    values = np.exp(-((xx + 0.65) ** 2 + (yy - 0.25) ** 2 + (zz + 0.25) ** 2) / 1.05) + 0.85 * np.exp(-((xx - 0.75) ** 2 + (yy + 0.55) ** 2 + (zz - 0.55) ** 2) / 0.72)
    filled = values > 0.28
    norm = mpl.colors.Normalize(vmin=float(values[filled].min()), vmax=float(values.max()))
    colors = plt.get_cmap(SEQUENTIAL_SAFE)(norm(values))
    colors[..., 3] = np.where(filled, 0.90, 0.0)
    fig = plt.figure(figsize=(8.3, 6.8))
    ax = fig.add_subplot(111, projection="3d")
    ax.voxels(filled, facecolors=colors, edgecolor=(1, 1, 1, 0.14), linewidth=0.25)
    ax.set(xlabel="X coordinate", ylabel="Y coordinate", zlabel="Z coordinate")
    ax.set_title("3D voxel volume of a thresholded intensity field", pad=15, weight="bold")
    ax.set_xticks([0, 4, 8], ["−2", "0", "2"])
    ax.set_yticks([0, 4, 8], ["−2", "0", "2"])
    ax.set_zticks([0, 4, 8], ["−2", "0", "2"])
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=25, azim=-58)
    ax.grid(True, color=GRID, alpha=0.30, linewidth=0.5)
    save(fig)


if __name__ == "__main__":
    main()
