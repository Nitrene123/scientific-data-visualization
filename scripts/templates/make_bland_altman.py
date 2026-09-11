from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, INK, PRIMARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "bland_altman_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    reference = rng.uniform(10, 95, 100)
    difference = 1.8 + rng.normal(0, 3.0, reference.size) + 0.025 * (reference - 50)
    mean_value = reference + difference / 2
    bias = float(difference.mean())
    sd = float(difference.std(ddof=1))
    loa_low, loa_high = bias - 1.96 * sd, bias + 1.96 * sd

    fig, ax = plt.subplots(figsize=(7.4, 5.9))
    ax.scatter(mean_value, difference, s=28, color=PRIMARY, alpha=0.68, edgecolor="white", linewidth=0.35)
    ax.axhline(bias, color=HIGHLIGHT, lw=1.8, label=f"Bias = {bias:.2f}")
    ax.axhline(loa_low, color=HIGHLIGHT, ls="--", lw=1.0, label=f"95% limits: {loa_low:.1f} to {loa_high:.1f}")
    ax.axhline(loa_high, color=HIGHLIGHT, ls="--", lw=1.0)
    ax.fill_between([mean_value.min(), mean_value.max()], loa_low, loa_high, color=HIGHLIGHT, alpha=0.08, zorder=0)
    ax.axhline(0, color="#7A8790", lw=0.9)
    ax.set_xlabel("Mean of methods (unit)")
    ax.set_ylabel("Method A − Method B (unit)")
    ax.set_title("Bland–Altman agreement plot", pad=13, weight="bold")
    ax.grid(True, color=GRID, alpha=0.55, linewidth=0.6)
    ax.legend(loc="upper left", frameon=True, framealpha=0.9, fontsize=8.5)
    ax.text(0.98, 0.04, "Difference should be interpreted against a pre-specified acceptable agreement range.", transform=ax.transAxes, ha="right", va="bottom", fontsize=8.2, color=INK)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
