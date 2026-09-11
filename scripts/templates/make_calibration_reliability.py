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
    out = ROOT / "outputs" / "calibration_reliability_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    n = 1500
    latent = rng.normal(0, 1, n)
    true_prob = 1 / (1 + np.exp(-1.25 * latent))
    y = rng.binomial(1, true_prob)
    predicted = np.clip(0.04 + 0.92 * true_prob + rng.normal(0, 0.055, n), 0.01, 0.99)
    bins = np.linspace(0, 1, 11)
    idx = np.digitize(predicted, bins[1:-1], right=True)
    mean_pred, frac_pos, counts = [], [], []
    for b in range(10):
        mask = idx == b
        counts.append(int(mask.sum()))
        mean_pred.append(float(predicted[mask].mean()) if mask.any() else np.nan)
        frac_pos.append(float(y[mask].mean()) if mask.any() else np.nan)
    mean_pred = np.asarray(mean_pred)
    frac_pos = np.asarray(frac_pos)
    valid = np.isfinite(mean_pred)
    ece = float(np.sum(np.asarray(counts)[valid] * np.abs(mean_pred[valid] - frac_pos[valid])) / n)

    fig = plt.figure(figsize=(7.6, 7.0))
    grid = fig.add_gridspec(2, 1, height_ratios=[3.7, 1.0], hspace=0.08)
    ax = fig.add_subplot(grid[0])
    hist_ax = fig.add_subplot(grid[1], sharex=ax)
    ax.plot([0, 1], [0, 1], color="#777777", ls="--", lw=1.0, label="Perfect calibration")
    ax.plot(mean_pred[valid], frac_pos[valid], color="#2a7f9e", marker="o", ms=6, lw=1.9, label="Model")
    ax.fill_between(mean_pred[valid], np.clip(frac_pos[valid] - 0.035, 0, 1), np.clip(frac_pos[valid] + 0.035, 0, 1), color="#2a7f9e", alpha=0.14, lw=0)
    ax.set(xlim=(0, 1), ylim=(0, 1), ylabel="Observed event frequency")
    ax.set_title("Calibration / reliability diagram", pad=13, weight="bold")
    ax.text(0.97, 0.08, f"ECE = {ece:.3f}", transform=ax.transAxes, ha="right", va="bottom", fontsize=9, color="#555555")
    ax.legend(loc="upper left", fontsize=9, frameon=True, framealpha=0.9)
    ax.grid(True, color="#b8c2c9", alpha=0.28, linewidth=0.6)
    hist_ax.hist(predicted, bins=bins, color="#8cb8c6", edgecolor="white", linewidth=0.55)
    hist_ax.set(xlabel="Mean predicted probability", ylabel="Count")
    hist_ax.grid(True, axis="y", color="#b8c2c9", alpha=0.25, linewidth=0.6)
    hist_ax.tick_params(axis="x", labelsize=8.5)
    plt.setp(ax.get_xticklabels(), visible=False)
    fig.subplots_adjust(left=0.13, right=0.96, top=0.92, bottom=0.11)
    save(fig)


if __name__ == "__main__":
    main()
