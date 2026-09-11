from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": 9.5,
            "axes.linewidth": 0.75,
        }
    )


def surface_a(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return 0.38 + 0.34 * np.sin(x * 1.15) * np.cos(y * 0.80) + 0.18 * x**2 - 0.08 * y


def surface_b(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return 0.30 + 0.23 * np.cos(x * 0.95) + 0.20 * np.sin(y * 1.20) + 0.12 * x * y


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "3d_response_surface_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    configure_matplotlib()
    x = np.linspace(-2.2, 2.2, 45)
    y = np.linspace(-1.8, 1.8, 42)
    xx, yy = np.meshgrid(x, y)
    functions = [(surface_a, "Response surface A", "GnBu"), (surface_b, "Response surface B", "YlOrBr")]
    path_x = np.linspace(-1.9, 1.95, 150)
    path_y = 0.65 * np.sin(path_x * 1.45) - 0.15 * path_x

    fig = plt.figure(figsize=(11.4, 5.9))
    for idx, (func, title, cmap) in enumerate(functions, start=1):
        ax = fig.add_subplot(1, 2, idx, projection="3d")
        zz = func(xx, yy)
        surf = ax.plot_surface(
            xx,
            yy,
            zz,
            cmap=cmap,
            linewidth=0,
            antialiased=True,
            alpha=0.90,
            rcount=42,
            ccount=42,
        )
        z_floor = float(zz.min()) - 0.08
        ax.contour(xx, yy, zz, zdir="z", offset=z_floor, levels=7, cmap=cmap, linewidths=0.65, alpha=0.75)
        path_z = func(path_x, path_y) + 0.025
        ax.plot(path_x, path_y, np.full_like(path_x, z_floor + 0.01), color="#d73027", lw=1.5, ls="--", alpha=0.75)
        ax.plot(path_x, path_y, path_z, color="#d73027", lw=2.7, solid_capstyle="round")
        ax.scatter(path_x[[0, -1]], path_y[[0, -1]], path_z[[0, -1]], color="#d73027", s=20, depthshade=False)
        ax.set_title(title, pad=13, weight="bold", fontsize=11)
        ax.set_xlabel("Input 1", labelpad=5)
        ax.set_ylabel("Input 2", labelpad=5)
        ax.set_zlabel("Predicted response", labelpad=5)
        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(y.min(), y.max())
        ax.set_zlim(z_floor, float(zz.max()) + 0.11)
        ax.view_init(elev=28, azim=-58)
        ax.set_box_aspect((1.25, 1.0, 0.78))
        ax.xaxis.pane.set_facecolor((0.95, 0.96, 0.96, 0.35))
        ax.yaxis.pane.set_facecolor((0.95, 0.96, 0.96, 0.35))
        ax.zaxis.pane.set_facecolor((0.98, 0.98, 0.98, 0.24))
        ax.grid(True, color="#b7c2c2", alpha=0.25, linewidth=0.5)
        cbar = fig.colorbar(surf, ax=ax, fraction=0.045, pad=0.04, shrink=0.72)
        cbar.set_label("Response", labelpad=5)
        cbar.ax.tick_params(labelsize=7.5)

    fig.suptitle("Two-input response surfaces with path and ground projection", y=0.98, fontsize=13, weight="bold")
    fig.legend(
        [Line2D([0], [0], color="#d73027", lw=2.7), Line2D([0], [0], color="#d73027", lw=1.5, ls="--")],
        ["Path on surface", "Ground projection"],
        loc="lower center",
        ncol=2,
        bbox_to_anchor=(0.5, 0.005),
        frameon=False,
        fontsize=9,
    )
    fig.subplots_adjust(left=0.02, right=0.98, top=0.89, bottom=0.11, wspace=0.08)
    save(fig)


if __name__ == "__main__":
    main()
