import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'cross' pattern with clear horizontal and vertical arms."""
    alpha = 0.6

    def draw_cross(ax, s, n):
        """Draw a cross pattern for the n-th figure."""

        # HORIZONTAL ARM: (2n+1) squares horizontally centered at y=0
        horizontal_color = plotmath.COLORS.get("red")
        arm_length = 2 * n + 1
        start_x = -(arm_length - 1) * s / 2

        for i in range(arm_length):
            x0 = start_x + i * s
            y0 = 0
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(
                A, B, C, D, ax=ax, alpha=alpha, color=horizontal_color
            )

        # VERTICAL ARM: (2n+1) squares vertically centered at x=0
        # But exclude the center square to avoid double counting
        vertical_color = plotmath.COLORS.get("blue")

        # Upper part of vertical arm
        for j in range(1, n + 1):
            x0 = -s / 2
            y0 = j * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=vertical_color)

        # Lower part of vertical arm
        for j in range(1, n + 1):
            x0 = -s / 2
            y0 = -j * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=vertical_color)

        # CENTER SQUARE: overlap of the two arms (different color to show it's shared)
        center_color = plotmath.COLORS.get("purple")
        x0 = -s / 2
        y0 = 0
        A = (x0, y0)
        B = (x0 + s, y0)
        C = (x0 + s, y0 + s)
        D = (x0, y0 + s)
        plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=center_color)

    # --- Create figure with multiple cross patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(10, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw crosses of different sizes
    s = 1
    draw_cross(axs[0], s=s, n=1)
    draw_cross(axs[1], s=s, n=2)
    draw_cross(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares mathematically
        n = i + 1
        # Horizontal arm: (2n+1) squares
        # Vertical arm: (2n+1) squares
        # But they share 1 center square, so total = 2(2n+1) - 1 = 4n + 1
        horizontal_squares = 2 * n + 1
        vertical_squares = 2 * n + 1
        total_squares = horizontal_squares + vertical_squares - 1  # subtract overlap

        ax.text(
            x=0,
            y=-(n + 2) * s,
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        # Mathematical breakdown
        ax.text(
            x=0,
            y=-(n + 3) * s,
            s=f"Antall ruter: {total_squares} = 4×{n} + 1",
            fontsize=12,
            ha="center",
            va="center",
        )

        # Parts explanation
        ax.text(
            x=0,
            y=-(n + 4) * s,
            s=f"Horisontalt: {horizontal_squares} + Vertikalt: {vertical_squares} - Overlapp: 1",
            fontsize=10,
            ha="center",
            va="center",
            style="italic",
        )

        # Set axis limits
        max_extent = n + 1.5
        ax.set_xlim(-max_extent * s, max_extent * s)
        ax.set_ylim(-(n + 4.5) * s, max_extent * s)

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
