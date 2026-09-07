import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    # TODO: write code here
    alpha = 0.2

    color = plotmath.COLORS.get("blue")

    def draw_corner(ax, s, n):
        # top n×n
        for i in range(n):
            for j in range(n):
                A = (i * s, j * s)
                B = ((i + 1) * s, j * s)
                C = ((i + 1) * s, (j + 1) * s)
                D = (i * s, (j + 1) * s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)
        # left diag (n+1)
        for k in range(n + 1):
            x0, y0 = (k - 1) * s, -k * s
            A = (x0, y0)
            B = (x0, y0 - s)
            C = (x0 + s, y0 - s)
            D = (x0 + s, y0)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)
        # right col (n)
        for k in range(n):
            x0, y0 = n * s, -k * s
            A = (x0, y0)
            B = (x0, y0 - s)
            C = (x0 + s, y0 - s)
            D = (x0 + s, y0)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

    # --- merge into one figure ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(8, 3),  # 3″ per subplot
        sharex=True,
        sharey=True,  # same data‐to‐pixel scale
        constrained_layout=True,
    )

    # draw each with the same s=1
    s = 1
    draw_corner(axs[0], s=s, n=1)
    draw_corner(axs[1], s=s, n=2)
    draw_corner(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")  # 1 unit = 1 unit
        ax.axis("off")
        ax.text(
            x=(i + 0.5) * s,
            y=-5 * s,
            s=f"Figur {i+1}",
            fontsize=22,
            ha="center",
            va="center",
        )
        # fix axis‐limits so each square shows at the same scale
        # ax.set_xlim(-1, (4 + 1) * 1)  # max_n=4 in this example
        # ax.set_ylim(-(4 + 1) * 1, (4) * 1)

    # NOTE: Automatically saves with correct file format and filename.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)
