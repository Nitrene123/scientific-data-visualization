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
    out = ROOT / "outputs" / "manhattan_plot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    n_per_chr = 58
    chroms = np.repeat(np.arange(1, 23), n_per_chr)
    positions = np.tile(np.linspace(0, 1_000_000, n_per_chr), 22) + rng.uniform(0, 18_000, chroms.size)
    p_values = rng.uniform(0.00001, 1.0, chroms.size)
    for chrom, center, amplitude in [(3, 0.46, 7.6), (8, 0.70, 8.4), (14, 0.36, 7.1), (19, 0.82, 9.0)]:
        mask = chroms == chrom
        local = np.abs((positions[mask] / 1_000_000) - center)
        p_values[mask] = np.clip(10 ** (-(1.8 + amplitude * np.exp(-(local / 0.10) ** 2))), 1e-12, 1)
    neg_log_p = -np.log10(p_values)
    cumulative = np.zeros_like(positions)
    offset = 0.0
    tick_positions, tick_labels = [], []
    for chrom in range(1, 23):
        mask = chroms == chrom
        cumulative[mask] = positions[mask] + offset
        tick_positions.append(float(np.mean(cumulative[mask])))
        tick_labels.append(str(chrom))
        offset = float(cumulative[mask].max() + 80_000)
    colors = np.where(chroms % 2 == 0, "#3b6f8f", "#9fc3cf")
    fig, ax = plt.subplots(figsize=(11.0, 5.5))
    ax.scatter(cumulative, neg_log_p, s=11, c=colors, alpha=0.78, edgecolor="none")
    genome_threshold = -np.log10(5e-8)
    suggestive = -np.log10(1e-5)
    ax.axhline(genome_threshold, color="#c65d3b", lw=1.1, ls="--", label="Genome-wide threshold: p = 5×10⁻⁸")
    ax.axhline(suggestive, color="#777777", lw=0.9, ls=":", label="Suggestive threshold: p = 10⁻⁵")
    top = np.argsort(neg_log_p)[-6:]
    for idx in top:
        ax.annotate(f"chr{chroms[idx]}:{int(positions[idx] / 1000)} kb", (cumulative[idx], neg_log_p[idx]), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=7.5, color="#444444")
    ax.set_xticks(tick_positions, tick_labels)
    ax.set_xlabel("Chromosome")
    ax.set_ylabel("−log₁₀(p-value)")
    ax.set_title("Genome-wide association Manhattan plot", pad=13, weight="bold")
    ax.grid(True, axis="y", color="#b8c2c9", alpha=0.25, linewidth=0.55)
    ax.legend(loc="upper right", frameon=True, framealpha=0.90, fontsize=8.5)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
