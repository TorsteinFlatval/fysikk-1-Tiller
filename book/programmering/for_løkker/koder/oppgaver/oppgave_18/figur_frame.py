import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'border frame' pattern with clear inner and outer rectangles."""
    alpha = 0.6

    def draw_frame(ax, s, n):
        """Draw a frame pattern for the n-th figure."""

        # OUTER BORDER: Forms the outer edge of an (n+2)×(n+2) square
        border_color = plotmath.COLORS.get("blue")
        outer_size = n + 2

        # Top border
        for i in range(outer_size):
            x0 = i * s - outer_size * s / 2
            y0 = (outer_size - 1) * s - outer_size * s / 2
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=border_color)

        # Bottom border
        for i in range(outer_size):
            x0 = i * s - outer_size * s / 2
            y0 = 0 * s - outer_size * s / 2
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=border_color)

        # Left border (excluding corners already drawn)
        for j in range(1, outer_size - 1):
            x0 = 0 * s - outer_size * s / 2
            y0 = j * s - outer_size * s / 2
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=border_color)

        # Right border (excluding corners already drawn)
        for j in range(1, outer_size - 1):
            x0 = (outer_size - 1) * s - outer_size * s / 2
            y0 = j * s - outer_size * s / 2
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=border_color)

        # INNER FILL: n×n square in the center
        inner_color = plotmath.COLORS.get("yellow")
        for i in range(n):
            for j in range(n):
                x0 = (i + 1) * s - outer_size * s / 2
                y0 = (j + 1) * s - outer_size * s / 2
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=inner_color)

    # --- Create figure with multiple frame patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(10, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw frames of different sizes
    s = 1
    draw_frame(axs[0], s=s, n=1)
    draw_frame(axs[1], s=s, n=2)
    draw_frame(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares mathematically
        n = i + 1
        outer_size = n + 2
        # Total squares = outer area - inner empty area
        # But since we fill the inner area: Total = outer_area = (n+2)²
        total_squares = outer_size * outer_size
        border_squares = total_squares - n * n
        inner_squares = n * n

        ax.text(
            x=0,
            y=-(outer_size / 2 + 1.5) * s,
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        # Mathematical breakdown
        ax.text(
            x=0,
            y=-(outer_size / 2 + 2.5) * s,
            s=f"Antall ruter: {total_squares} = {outer_size}²",
            fontsize=12,
            ha="center",
            va="center",
        )

        # Parts explanation
        ax.text(
            x=0,
            y=-(outer_size / 2 + 3.5) * s,
            s=f"Ramme: {border_squares} + Indre: {inner_squares}",
            fontsize=10,
            ha="center",
            va="center",
            style="italic",
        )

        # Set axis limits
        max_extent = outer_size / 2 + 0.5
        ax.set_xlim(-max_extent * s, max_extent * s)
        ax.set_ylim(-(outer_size / 2 + 4) * s, max_extent * s)

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
