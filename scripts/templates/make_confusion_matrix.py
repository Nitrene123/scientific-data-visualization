from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import INK, GRID, MUTED


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "confusion_matrix_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    cm = np.array([[845, 65], [42, 48]])
    row_pct = cm / cm.sum(axis=1, keepdims=True)
    fig, ax = plt.subplots(figsize=(6.5, 5.8))
    image = ax.imshow(cm, cmap="Blues", vmin=0, vmax=cm.max())
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            color = "white" if cm[i, j] > cm.max() * 0.55 else INK
            ax.text(j, i, f"{cm[i, j]:,}\n({row_pct[i, j]:.1%})", ha="center", va="center", color=color, fontsize=11, weight="bold")
    ax.set_xticks([0, 1], ["Negative", "Positive"])
    ax.set_yticks([0, 1], ["Negative", "Positive"])
    ax.set_xlabel("Predicted class")
    ax.set_ylabel("Observed class")
    ax.set_title("Confusion matrix with row-normalized percentages", pad=13, weight="bold")
    ax.set_xticks(np.arange(-.5, 2, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 2, 1), minor=True)
    ax.grid(which="minor", color=GRID, lw=1.2)
    ax.tick_params(which="minor", bottom=False, left=False)
    cbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Number of observations")
    cbar.ax.tick_params(labelsize=8)
    ax.text(0.98, -0.17, "Rows are normalized for comparison; counts remain shown.", transform=ax.transAxes, ha="right", fontsize=8.5, color=MUTED)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
