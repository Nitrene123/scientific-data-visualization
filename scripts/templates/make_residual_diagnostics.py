from __future__ import annotations

import os
from pathlib import Path
from statistics import NormalDist

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "residual_diagnostics_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    n = 220
    fitted = np.linspace(1.2, 8.8, n)
    residual = rng.normal(0, 0.22 + 0.055 * fitted, n) + 0.018 * (fitted - 5.0) ** 2 - 0.18
    residual[[26, 181]] += [1.20, -1.05]
    std_resid = (residual - residual.mean()) / residual.std(ddof=1)
    abs_sqrt = np.sqrt(np.abs(std_resid))
    order = np.argsort(fitted)
    rolling = np.convolve(residual[order], np.ones(21) / 21, mode="same")
    theoretical = np.array([NormalDist().inv_cdf((i + 0.5) / n) for i in range(n)])
    ordered = np.sort(std_resid)
    slope, intercept = np.polyfit(theoretical, ordered, 1)
    leverage = 0.004 + 0.018 * ((fitted - fitted.mean()) / (fitted.max() - fitted.min())) ** 2

    fig, axes = plt.subplots(2, 2, figsize=(8.8, 7.4))
    ax = axes[0, 0]
    ax.scatter(fitted, residual, s=18, color="#2a7f9e", alpha=0.70, edgecolor="none")
    ax.plot(fitted[order], rolling, color="#c65d3b", lw=1.8)
    ax.axhline(0, color="#777777", lw=0.9, ls="--")
    ax.set(xlabel="Fitted values", ylabel="Residuals", title="Residuals vs fitted")

    ax = axes[0, 1]
    ax.scatter(theoretical, ordered, s=18, color="#2a7f9e", alpha=0.70, edgecolor="none")
    ax.plot(theoretical, intercept + slope * theoretical, color="#c65d3b", lw=1.6)
    ax.plot([-2.7, 2.7], [-2.7, 2.7], color="#777777", lw=0.9, ls="--")
    ax.set(xlabel="Theoretical quantiles", ylabel="Standardized residuals", title="Normal Q–Q")

    ax = axes[1, 0]
    ax.scatter(fitted, abs_sqrt, s=18, color="#2a7f9e", alpha=0.70, edgecolor="none")
    ax.plot(fitted[order], np.sqrt(np.abs(rolling / residual.std(ddof=1))), color="#c65d3b", lw=1.8)
    ax.set(xlabel="Fitted values", ylabel="√|standardized residuals|", title="Scale–location")

    ax = axes[1, 1]
    index = np.arange(1, n + 1)
    ax.scatter(index, std_resid, s=18, color="#2a7f9e", alpha=0.70, edgecolor="none")
    ax.axhline(0, color="#777777", lw=0.9, ls="--")
    ax.axhline(2, color="#c65d3b", lw=0.9, ls=":")
    ax.axhline(-2, color="#c65d3b", lw=0.9, ls=":")
    ax.set(xlabel="Observation index", ylabel="Standardized residuals", title="Outlier / influence screen")
    ax.text(0.97, 0.92, f"max |r| = {np.max(np.abs(std_resid)):.2f}", transform=ax.transAxes, ha="right", va="top", fontsize=8.5, color="#555555")

    for ax in axes.flat:
        ax.grid(True, color="#b8c2c9", alpha=0.25, linewidth=0.55)
        ax.tick_params(labelsize=8.2)
    fig.suptitle("Regression residual diagnostics", y=0.985, fontsize=13, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    save(fig)


if __name__ == "__main__":
    main()
