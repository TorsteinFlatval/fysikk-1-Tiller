import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'butterfly'-like pattern with wings, body, and antennae components."""
    alpha = 0.7

    def draw_butterfly(ax, s, n):
        """Draw a butterfly-like pattern for the n-th figure."""

        # LEFT WING: triangular pattern in upper-left quadrant
        # Creates n rows, with row i having i squares
        wing_color = plotmath.COLORS.get("purple")
        for row in range(n):
            for col in range(row + 1):
                x0 = -s * (col + 1)
                y0 = s * (n - row - 1)
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=wing_color)

        # RIGHT WING: mirror of left wing in upper-right quadrant
        for row in range(n):
            for col in range(row + 1):
                x0 = s * col
                y0 = s * (n - row - 1)
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=wing_color)

        # LOWER LEFT WING: inverted triangular pattern in lower-left quadrant
        for row in range(n):
            for col in range(n - row):
                x0 = -s * (col + 1)
                y0 = -s * (row + 1)
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=wing_color)

        # LOWER RIGHT WING: mirror of lower left wing
        for row in range(n):
            for col in range(n - row):
                x0 = s * col
                y0 = -s * (row + 1)
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=wing_color)

        # BODY: vertical line of n squares along the center
        body_color = plotmath.COLORS.get("orange")
        for i in range(n):
            x0 = -s / 2
            y0 = -s / 2 + i * s - (n - 1) * s / 2
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=body_color)

        # ANTENNAE: two single squares above the body
        antenna_color = plotmath.COLORS.get("red")
        # Left antenna
        x0 = -s * 1.5
        y0 = s * (n + 0.5)
        A = (x0, y0)
        B = (x0 + s, y0)
        C = (x0 + s, y0 + s)
        D = (x0, y0 + s)
        plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=antenna_color)

        # Right antenna
        x0 = s * 0.5
        y0 = s * (n + 0.5)
        A = (x0, y0)
        B = (x0 + s, y0)
        C = (x0 + s, y0 + s)
        D = (x0, y0 + s)
        plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=antenna_color)

    # --- Create figure with multiple butterfly patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(10, 4),  # Wide enough for butterfly shapes
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw butterflies of different sizes
    s = 1
    draw_butterfly(axs[0], s=s, n=1)
    draw_butterfly(axs[1], s=s, n=2)
    draw_butterfly(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares for this figure
        n = i + 1
        # Upper wings: sum from 1 to n = n(n+1)/2 for each wing
        upper_wing_squares = 2 * n * (n + 1) // 2
        # Lower wings: sum from 1 to n = n(n+1)/2 for each wing
        lower_wing_squares = 2 * n * (n + 1) // 2
        body_squares = n
        antenna_squares = 2
        total_squares = (
            upper_wing_squares + lower_wing_squares + body_squares + antenna_squares
        )

        ax.text(
            x=0,  # Center under the figure
            y=-s * (n + 2.5),
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        ax.text(
            x=0,  # Center under the figure
            y=-s * (n + 3.5),
            s=f"Antall ruter: {total_squares}",
            fontsize=12,
            ha="center",
            va="center",
        )

        # Set reasonable axis limits
        max_extent = max(n + 2, 4)
        ax.set_xlim(-max_extent * s, max_extent * s)
        ax.set_ylim(-(max_extent + 1) * s, (max_extent + 1) * s)

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
