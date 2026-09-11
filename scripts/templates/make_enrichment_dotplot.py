from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np

from palette import GRID, INK, SEQUENTIAL


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "enrichment_dotplot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    terms = ["Oxidative phosphorylation", "Cell cycle regulation", "DNA repair", "Lipid metabolism", "Immune response", "Autophagy", "RNA processing", "Stress response", "Chromatin organization"]
    rich_factor = np.array([0.42, 0.31, 0.27, 0.23, 0.21, 0.18, 0.16, 0.13, 0.11])
    counts = np.array([38, 31, 27, 24, 22, 19, 17, 15, 12])
    neg_log_p = np.array([7.8, 6.9, 6.1, 5.6, 5.1, 4.6, 4.2, 3.7, 3.2])
    y = np.arange(len(terms))[::-1]
    fig, ax = plt.subplots(figsize=(8.2, 6.1))
    norm = Normalize(vmin=neg_log_p.min(), vmax=neg_log_p.max())
    ax.scatter(rich_factor, y, s=counts * 8, c=neg_log_p, cmap=SEQUENTIAL, norm=norm, edgecolor="white", linewidth=0.65, alpha=0.92)
    ax.set_yticks(y, terms)
    ax.set_xlabel("Gene ratio / enrichment factor")
    ax.set_ylabel("Pathway")
    ax.set_title("Pathway enrichment dot plot", pad=13, weight="bold")
    ax.grid(True, axis="x", color=GRID, alpha=0.55, linewidth=0.6)
    sm = ScalarMappable(norm=norm, cmap=SEQUENTIAL)
    sm.set_array(neg_log_p)
    cbar = fig.colorbar(sm, ax=ax, fraction=0.035, pad=0.04)
    cbar.set_label("−log₁₀ adjusted p-value")
    size_handles = [ax.scatter([], [], s=v * 8, color=INK, alpha=0.78, edgecolor="white", label=f"{v} genes") for v in [15, 30, 40]]
    ax.legend(handles=size_handles, title="Gene count", loc="lower right", frameon=True, framealpha=0.9, fontsize=8.2, title_fontsize=8.5)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
