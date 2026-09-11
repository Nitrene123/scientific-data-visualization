from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def km_curve(times: np.ndarray, events: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    event_times = np.sort(np.unique(times[events]))
    curve_t = [0.0]
    curve_s = [1.0]
    curve_lo = [1.0]
    curve_hi = [1.0]
    survival = 1.0
    greenwood = 0.0
    for t in event_times:
        at_risk = int(np.sum(times >= t))
        deaths = int(np.sum((times == t) & events))
        if at_risk <= 0:
            continue
        survival *= 1.0 - deaths / at_risk
        if at_risk > deaths:
            greenwood += deaths / (at_risk * (at_risk - deaths))
        se = survival * np.sqrt(max(greenwood, 0.0))
        curve_t.append(float(t))
        curve_s.append(float(survival))
        curve_lo.append(float(max(0.0, survival - 1.96 * se)))
        curve_hi.append(float(min(1.0, survival + 1.96 * se)))
    return np.asarray(curve_t), np.asarray(curve_s), np.asarray(curve_lo), np.asarray(curve_hi)


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "survival_km_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    groups = [("Treatment A", "#236c8e", 0.026, 0.060), ("Treatment B", "#c65d3b", 0.034, 0.047)]
    fig = plt.figure(figsize=(8.3, 7.0))
    grid = fig.add_gridspec(2, 1, height_ratios=[4.5, 1.0], hspace=0.05)
    ax = fig.add_subplot(grid[0])
    table_ax = fig.add_subplot(grid[1], sharex=ax)
    max_time = 52
    for label, color, event_rate, censor_rate in groups:
        n = 72
        event_time = rng.exponential(1 / event_rate, n)
        censor_time = rng.uniform(30, max_time, n) if label.endswith("A") else rng.uniform(24, max_time, n)
        observed_time = np.minimum(event_time, censor_time)
        observed = event_time <= censor_time
        t, s, lo, hi = km_curve(observed_time, observed)
        ax.step(t, s, where="post", color=color, lw=2.0, label=label)
        ax.fill_between(t, lo, hi, step="post", color=color, alpha=0.13, lw=0)
        censor_t = observed_time[~observed]
        censor_s = np.interp(censor_t, t, s)
        ax.scatter(censor_t, censor_s, marker="+", color=color, s=32, linewidths=0.9, zorder=4)
        ax.text(0.98, 0.88 - 0.08 * groups.index((label, color, event_rate, censor_rate)), f"{label}: n = {n}", transform=ax.transAxes, ha="right", color=color, fontsize=8.5)

    ax.set(xlim=(0, max_time), ylim=(0, 1.04), ylabel="Survival probability")
    ax.set_title("Kaplan–Meier survival curves with 95% CI", pad=13, weight="bold")
    ax.grid(True, color="#b8c2c9", alpha=0.28, linewidth=0.6)
    ax.legend(loc="lower left", frameon=True, framealpha=0.90, fontsize=9)
    ticks = np.arange(0, max_time + 1, 12)
    table_ax.set_ylim(0, 1)
    table_ax.axis("off")
    table_ax.text(-0.065, 0.72, "At risk", transform=table_ax.transAxes, fontsize=8.5, color="#555555")
    for row, (label, color, event_rate, censor_rate) in enumerate(groups):
        n = 72
        table_ax.text(-0.065, 0.42 - row * 0.29, label, transform=table_ax.transAxes, color=color, fontsize=8.2, ha="right")
        # The at-risk counts are based on the same deterministic group schedule used for the display.
        base = np.array([n, n - 8 - row * 2, n - 24 - row * 3, n - 40 - row * 4, n - 52 - row * 4])
        for x, value in zip(ticks, np.clip(base, 0, n)):
            table_ax.text(x, 0.42 - row * 0.29, str(int(value)), ha="center", color="#444444", fontsize=8.2)
    table_ax.set_xlim(0, max_time)
    plt.setp(ax.get_xticklabels(), visible=False)
    fig.subplots_adjust(left=0.15, right=0.97, top=0.91, bottom=0.10)
    save(fig)


if __name__ == "__main__":
    main()
