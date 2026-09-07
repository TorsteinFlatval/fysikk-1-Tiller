import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create an 'L-shape' pattern with clear rectangular sections."""
    alpha = 0.6

    def draw_L_shape(ax, s, n):
        """Draw an L-shape pattern for the n-th figure."""

        # HORIZONTAL ARM: n×n square in the bottom-right
        horizontal_color = plotmath.COLORS.get("blue")
        for i in range(n):
            for j in range(n):
                x0 = i * s
                y0 = j * s
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(
                    A, B, C, D, ax=ax, alpha=alpha, color=horizontal_color
                )

        # VERTICAL ARM: n×n square in the upper-left
        vertical_color = plotmath.COLORS.get("red")
        for i in range(n):
            for j in range(n):
                x0 = -n * s + i * s
                y0 = n * s + j * s
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(
                    A, B, C, D, ax=ax, alpha=alpha, color=vertical_color
                )

        # CONNECTOR: n×n square connecting the two arms
        connector_color = plotmath.COLORS.get("green")
        for i in range(n):
            for j in range(n):
                x0 = -n * s + i * s
                y0 = j * s
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(
                    A, B, C, D, ax=ax, alpha=alpha, color=connector_color
                )

    # --- Create figure with multiple L-shape patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(12, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw L-shapes of different sizes
    s = 1
    draw_L_shape(axs[0], s=s, n=1)
    draw_L_shape(axs[1], s=s, n=2)
    draw_L_shape(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares mathematically
        n = i + 1
        # Three n×n squares, but they share one n×n overlap
        # Total = 3n² - n² = 2n²
        total_squares = 3 * n * n

        ax.text(
            x=0,
            y=-(n + 1.5) * s,
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        # Mathematical breakdown
        ax.text(
            x=0,
            y=-(n + 2.5) * s,
            s=f"Antall ruter: {total_squares} = 3×{n}²",
            fontsize=12,
            ha="center",
            va="center",
        )

        # Parts explanation
        ax.text(
            x=0,
            y=-(n + 3.5) * s,
            s=f"Horisontalt: {n}² + Vertikalt: {n}² + Kobling: {n}²",
            fontsize=10,
            ha="center",
            va="center",
            style="italic",
        )

        # Set axis limits
        max_extent = n + 1
        ax.set_xlim(-(n + 1) * s, (n + 1) * s)
        ax.set_ylim(-(n + 4) * s, (2 * n + 1) * s)

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
