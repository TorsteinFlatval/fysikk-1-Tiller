import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):

    fig, ax = plt.subplots(figsize=(8, 2))
    alpha = 1
    teal = (0, 140 / 255, 130 / 255)
    k = 0.9  # Scale factor
    n_linjestykker = 100  # Number of line segments

    lengde = 100  # Initial length
    x = 0  # Start at origin
    y = 0

    # Draw first vertical line up
    y = lengde  # First line goes up
    plt.plot([0, 0], [0, y], color=plotmath.COLORS.get("blue"), lw=2, alpha=alpha)

    for i in range(n_linjestykker):
        lengde *= k  # Reduce length by scale factor
        x_prev, y_prev = x, y

        if i % 2 == 0:  # Horizontal line right
            x += lengde
            plt.plot(
                [x_prev, x],
                [y, y],
                color=plotmath.COLORS.get("blue"),
                lw=2,
                alpha=alpha,
            )
        else:  # Vertical line (alternating down/up)
            direction = -1 if (i // 2) % 2 == 0 else 1  # Alternate between down and up
            y += direction * lengde
            plt.plot(
                [x, x],
                [y_prev, y],
                color=plotmath.COLORS.get("blue"),
                lw=2,
                alpha=alpha,
            )

    plt.axis("off")
    plt.axis("equal")

    plt.text(
        x=0 - 1,
        y=0.5 * 100,
        s="$100 \\, \\mathrm{cm}$",
        va="center",
        ha="right",
        fontsize=20,
    )

    plt.text(
        x=0.5 * 0.9 * 100,
        y=100,
        s="$90 \\, \\mathrm{cm}$",
        va="bottom",
        ha="center",
        fontsize=20,
    )

    # plt.tight_layout()

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
