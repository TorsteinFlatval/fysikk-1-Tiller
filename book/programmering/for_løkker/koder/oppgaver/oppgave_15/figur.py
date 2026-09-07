import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):

    # List of functions and their labels.
    A = [0, 0]
    B = [2, 0]
    C = [2, 2]
    D = [0, 2]

    plt.plot([A[0], B[0]], [A[1], B[1]], "k-", lw=1, alpha=0.7)
    plt.plot([B[0], C[0]], [B[1], C[1]], "k-", lw=1, alpha=0.7)
    plt.plot([C[0], D[0]], [C[1], D[1]], "k-", lw=1, alpha=0.7)
    plt.plot([D[0], A[0]], [D[1], A[1]], "k-", lw=1, alpha=0.7)

    plt.text(
        x=0 - 0.1,
        y=0.5 * (A[1] + D[1]),
        s="$3$",
        fontsize=20,
        ha="left",
        va="center",
    )

    plt.text(
        x=0.5 * (A[0] + B[0]),
        y=-0.1,
        s="$3$",
        fontsize=20,
        ha="center",
        va="top",
    )

    lengths = ["$2$", "$1$", "$\\frac{1}{2}$"]
    for i in range(10):
        x_midpoint = 0.5 * (A[0] + B[0])
        y_midpoint = 0.5 * (A[1] + C[1])
        height = 0.5 * (C[1] - A[1])
        width = 0.5 * (B[0] - A[0])

        plt.plot([x_midpoint, x_midpoint], [A[1], C[1]], "k--", lw=1, alpha=0.7)
        plt.plot([A[0], B[0]], [y_midpoint, y_midpoint], "k--", lw=1, alpha=0.7)

        A_fill = A[:]
        x_A = A[0]
        y_A = A[1]
        A_fill = (x_A, y_A)

        B_fill = (x_midpoint, B[1])

        C_fill = (x_midpoint, y_midpoint)
        D_fill = (D[0], y_midpoint)

        plt.fill(
            [A_fill[0], B_fill[0], C_fill[0], D_fill[0]],
            [A_fill[1], B_fill[1], C_fill[1], D_fill[1]],
            color=plotmath.COLORS.get("blue"),
            alpha=0.3,
        )

        # if i < 3:
        #     s = lengths[i]
        #     plt.text(
        #         x=A_fill[0] - 0.05,
        #         y=0.5 * (A_fill[1] + D_fill[1]),
        #         s=s,
        #         fontsize=20,
        #         ha="right",
        #         va="center",
        #     )

        A = [x_midpoint, y_midpoint]
        B = [B[0], y_midpoint]
        D = [x_midpoint, D[-1]]

    plt.tight_layout()
    plt.axis("off")
    plt.axis("equal")

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname,
            fname=fname,
            transparent=True,
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
