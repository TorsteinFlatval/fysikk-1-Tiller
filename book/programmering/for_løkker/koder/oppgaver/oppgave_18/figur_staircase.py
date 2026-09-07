import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'staircase' pattern with clear triangular structure."""
    alpha = 0.6

    def draw_staircase(ax, s, n):
        """Draw a staircase pattern for the n-th figure."""

        # Colors for different rows
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        # Each row k (k=1,2,...,n) has k squares
        # Row k is positioned at height (k-1) and starts at x=0
        for row in range(1, n + 1):
            color = plotmath.COLORS.get(colors[(row - 1) % len(colors)])

            for col in range(row):
                x0 = col * s
                y0 = (row - 1) * s
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

    # --- Create figure with multiple staircase patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(10, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw staircases of different sizes
    s = 1
    draw_staircase(axs[0], s=s, n=1)
    draw_staircase(axs[1], s=s, n=2)
    draw_staircase(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares mathematically
        n = i + 1
        # Sum of first n natural numbers: n(n+1)/2
        total_squares = n * (n + 1) // 2

        ax.text(
            x=n * s / 2,  # Center under the staircase
            y=-(1.5) * s,
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        # Mathematical breakdown
        # ax.text(
        #     x=n * s / 2,
        #     y=-(2.5) * s,
        #     s=f"Antall ruter: {total_squares} = {n}×{n+1}/2",
        #     fontsize=12,
        #     ha="center",
        #     va="center",
        # )

        # Sum explanation
        # sum_text = " + ".join([str(k) for k in range(1, n + 1)])
        # ax.text(
        #     x=n * s / 2,
        #     y=-(3.5) * s,
        #     s=f"Rad-sum: {sum_text}",
        #     fontsize=10,
        #     ha="center",
        #     va="center",
        #     style="italic",
        # )

        # Set axis limits
        ax.set_xlim(-0.5 * s, (n + 0.5) * s)
        ax.set_ylim(-4 * s, (n + 0.5) * s)

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
    main(dirname=dirname, save=False)
