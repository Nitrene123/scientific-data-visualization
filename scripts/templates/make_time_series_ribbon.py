from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, PRIMARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "time_series_ribbon_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    x = np.arange(0, 36)
    mean = 48 + 0.42 * x + 4.4 * np.sin(x / 3.4) + 0.07 * x**1.45
    width = 3.4 + 0.06 * x
    lower, upper = mean - width, mean + width
    fig, ax = plt.subplots(figsize=(8.5, 5.7))
    ax.axvspan(13, 20, color=HIGHLIGHT, alpha=0.10, label="Intervention window")
    ax.fill_between(x, lower, upper, color=PRIMARY, alpha=0.16, linewidth=0, label="95% uncertainty band")
    ax.plot(x, mean, color=PRIMARY, lw=2.1, marker="o", ms=3.2, label="Estimated mean")
    ax.axvline(13, color=HIGHLIGHT, ls="--", lw=1.0)
    ax.axvline(20, color=HIGHLIGHT, ls="--", lw=1.0)
    ax.set(xlabel="Study week", ylabel="Outcome (unit)")
    ax.set_title("Time series with uncertainty ribbon and event window", pad=13, weight="bold")
    ax.grid(True, color=GRID, alpha=0.55, linewidth=0.6)
    ax.legend(loc="upper left", frameon=True, framealpha=0.9, fontsize=8.5)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
