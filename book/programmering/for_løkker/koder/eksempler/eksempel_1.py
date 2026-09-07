import plotmath
import matplotlib.pyplot as plt
import numpy as np


def main(dirname, save):
    """
    Draw three triangular-number figures side by side,
    each using p(n)=n(n+1)/2 small squares.
    Squares are 1×1 data-units and share the same axes
    so they appear at identical physical size.
    """
    alpha = 0.2
    s = 1  # side length of each small square
    orders = [1, 2, 3]  # triangle orders
    n_max = max(orders)

    def draw_triangle(ax, n):
        for i in range(1, n + 1):
            row_len = i
            x0 = -row_len * s / 2
            y0 = (n - i) * s
            for j in range(row_len):
                A = (x0 + j * s, y0)
                B = (x0 + (j + 1) * s, y0)
                C = (x0 + (j + 1) * s, y0 + s)
                D = (x0 + j * s, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha)

    # create 3 subplots sharing axes so 1 data-unit → same physical size
    fig, axs = plt.subplots(
        1, 3, figsize=(9, 3), sharex=True, sharey=True, constrained_layout=True
    )

    for idx, (ax, n) in enumerate(zip(axs, orders), start=1):
        draw_triangle(ax, n)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.text(0, -0.2 * s, f"Figur {idx}", fontsize=16, ha="center", va="top")

    # fix identical limits + small margin so each 1×1 square is identical and edges aren't clipped
    half_w = n_max * s / 2
    height = n_max * s
    for ax in axs:
        ax.set_xlim(-half_w, half_w)
        ax.set_ylim(0, height)
        ax.margins(x=0.02, y=0.02)

    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(dirname=dirname, fname=fname)
    else:
        plotmath.show()


if __name__ == "__main__":
    import pathlib

    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break
    dirname = "/".join(parts)
    main(dirname=dirname, save=True)
