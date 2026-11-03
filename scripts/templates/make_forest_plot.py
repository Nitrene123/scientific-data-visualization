from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from palette import PRIMARY, apply_paper_style
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "forest_plot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    apply_paper_style()
    labels = ["Overall", "Age > 65", "Female", "High exposure", "Comorbidity", "Follow-up > 1 y"]
    estimates = np.array([0.72, 0.58, 0.88, 1.24, 1.06, 0.69])
    lower = np.array([0.57, 0.38, 0.64, 0.91, 0.77, 0.48])
    upper = np.array([0.91, 0.89, 1.19, 1.69, 1.47, 0.98])
    y = np.arange(len(labels))[::-1]
    fig, ax = plt.subplots(figsize=(8.3, 5.9))
    ax.axvline(1, color="#777777", lw=1.1, ls="--")
    ax.errorbar(
        estimates,
        y,
        xerr=[estimates - lower, upper - estimates],
        fmt="o",
        color=PRIMARY,
        ecolor=PRIMARY,
        capsize=3,
        elinewidth=1.2,
        capthick=1.0,
        ms=5.5,
    )
    ax.set_yticks(y, labels)
    ax.set_xlabel("Odds ratio (95% CI)")
    ax.set_xlim(0.25, 1.85)
    ax.set_title("Forest plot of subgroup estimates", pad=14, weight="bold")
    ax.grid(axis="x", color="#D9D9D9", linestyle="--", lw=0.6, alpha=0.7)
    ax.text(0.98, 0.04, "reference = 1.0", transform=ax.transAxes, ha="right", fontsize=9, color="#555555")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
