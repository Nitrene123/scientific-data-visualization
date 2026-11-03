from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from palette import QUALITATIVE, apply_paper_style
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "grouped_comparison_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    apply_paper_style()
    rng = np.random.default_rng(20260911)
    groups = ["Control", "Low dose", "Medium dose", "High dose"]
    colors = QUALITATIVE[: len(groups)]
    means = np.array([1.02, 1.34, 1.72, 2.06])
    samples = [rng.normal(mu, 0.18 + i * 0.015, 12) for i, mu in enumerate(means)]
    x = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    for i, (values, color) in enumerate(zip(samples, colors)):
        mean = values.mean()
        ci = 2.201 * values.std(ddof=1) / np.sqrt(values.size)  # 95% t interval, n=12
        ax.errorbar(i, mean, yerr=ci, fmt="o", color=color, ecolor=color, capsize=3.2, lw=1.1, ms=5.5, zorder=4)
        jitter = rng.normal(0, 0.055, values.size)
        ax.scatter(i + jitter, values, s=24, color=color, edgecolor="white", linewidth=0.45, alpha=0.78, zorder=3)
    ax.plot(x, [v.mean() for v in samples], color="#555555", lw=1.0, alpha=0.65, zorder=2)
    ax.set_xticks(x, [f"{group}\n(n={values.size})" for group, values in zip(groups, samples)])
    ax.set_ylabel("Normalized response")
    ax.set_title("Grouped comparison with raw observations and 95% CI", pad=14, weight="bold")
    ax.grid(axis="y", color="#dddddd", lw=0.8, alpha=0.7)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
