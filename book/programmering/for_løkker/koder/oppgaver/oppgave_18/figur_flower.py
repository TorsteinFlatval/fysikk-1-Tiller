import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'flower'-like pattern with petals around a center."""
    alpha = 0.6

    def draw_flower(ax, s, n):
        """Draw a flower-like pattern for the n-th figure."""

        # CENTER: n×n square in the middle
        center_color = plotmath.COLORS.get("yellow")
        center_offset = -(n - 1) * s / 2  # Center the n×n square

        for i in range(n):
            for j in range(n):
                x0 = center_offset + i * s
                y0 = center_offset + j * s
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(
                    A, B, C, D, ax=ax, alpha=alpha, color=center_color
                )

        petal_color = plotmath.COLORS.get("pink")

        # TOP PETALS: n squares extending upward from center
        for i in range(n):
            x0 = center_offset + i * s
            y0 = center_offset + n * s  # Above the center
            for j in range(n):  # Each petal is n squares tall
                A = (x0, y0 + j * s)
                B = (x0 + s, y0 + j * s)
                C = (x0 + s, y0 + (j + 1) * s)
                D = (x0, y0 + (j + 1) * s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=petal_color)

        # BOTTOM PETALS: n squares extending downward from center
        for i in range(n):
            x0 = center_offset + i * s
            y0 = center_offset - s  # Below the center
            for j in range(n):  # Each petal is n squares tall
                A = (x0, y0 - j * s)
                B = (x0 + s, y0 - j * s)
                C = (x0 + s, y0 - (j + 1) * s)
                D = (x0, y0 - (j + 1) * s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=petal_color)

        # LEFT PETALS: n squares extending leftward from center
        for j in range(n):
            y0 = center_offset + j * s
            x0 = center_offset - s  # Left of the center
            for i in range(n):  # Each petal is n squares wide
                A = (x0 - i * s, y0)
                B = (x0 - (i + 1) * s, y0)
                C = (x0 - (i + 1) * s, y0 + s)
                D = (x0 - i * s, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=petal_color)

        # RIGHT PETALS: n squares extending rightward from center
        for j in range(n):
            y0 = center_offset + j * s
            x0 = center_offset + n * s  # Right of the center
            for i in range(n):  # Each petal is n squares wide
                A = (x0 + i * s, y0)
                B = (x0 + (i + 1) * s, y0)
                C = (x0 + (i + 1) * s, y0 + s)
                D = (x0 + i * s, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=petal_color)

        # CORNER PETALS: diagonal extensions at 45-degree angles
        corner_color = plotmath.COLORS.get("green")

        # Top-right corner petal
        for i in range(n):
            x0 = center_offset + n * s + i * s
            y0 = center_offset + n * s + i * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=corner_color)

        # Top-left corner petal
        for i in range(n):
            x0 = center_offset - s - i * s
            y0 = center_offset + n * s + i * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=corner_color)

        # Bottom-right corner petal
        for i in range(n):
            x0 = center_offset + n * s + i * s
            y0 = center_offset - s - i * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=corner_color)

        # Bottom-left corner petal
        for i in range(n):
            x0 = center_offset - s - i * s
            y0 = center_offset - s - i * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=corner_color)

    # --- Create figure with multiple flower patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(12, 4.5),  # Wide enough for flower shapes
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw flowers of different sizes
    s = 1
    draw_flower(axs[0], s=s, n=1)
    draw_flower(axs[1], s=s, n=2)
    draw_flower(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares for this figure
        n = i + 1
        center_squares = n * n
        # 4 main petals, each with n*n squares
        main_petal_squares = 4 * n * n
        # 4 corner petals, each with n squares
        corner_petal_squares = 4 * n
        total_squares = center_squares + main_petal_squares + corner_petal_squares

        ax.text(
            x=0,  # Center under the figure
            y=-(2 * n + 3) * s,
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        ax.text(
            x=0,  # Center under the figure
            y=-(2 * n + 4) * s,
            s=f"Antall ruter: {total_squares}",
            fontsize=12,
            ha="center",
            va="center",
        )

        # Set reasonable axis limits to show the entire flower
        max_extent = 2 * n + 1
        ax.set_xlim(-max_extent * s, max_extent * s)
        ax.set_ylim(-(max_extent + 2) * s, max_extent * s)

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
