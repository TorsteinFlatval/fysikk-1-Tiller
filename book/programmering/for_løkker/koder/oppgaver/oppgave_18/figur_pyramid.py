import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'pyramid' pattern with clear layers that can be analyzed mathematically."""
    alpha = 0.6

    def draw_pyramid(ax, s, n):
        """Draw a pyramid pattern for the n-th figure."""

        # BASE: A horizontal line of (2n-1) squares at the bottom
        base_color = plotmath.COLORS.get("red")
        base_width = 2 * n - 1
        base_start_x = -(base_width - 1) * s / 2

        for i in range(base_width):
            x0 = base_start_x + i * s
            y0 = 0
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=base_color)

        # LAYERS: Each layer k has (2n-1-2k) squares for k = 0, 1, ..., n-1
        layer_colors = ["orange", "yellow", "green", "blue", "purple"]

        for layer in range(1, n):
            layer_width = 2 * n - 1 - 2 * layer
            if layer_width <= 0:
                break

            layer_start_x = -(layer_width - 1) * s / 2
            layer_y = layer * s
            color = plotmath.COLORS.get(layer_colors[(layer - 1) % len(layer_colors)])

            for i in range(layer_width):
                x0 = layer_start_x + i * s
                y0 = layer_y
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

        # TOP: Single square at the peak (when n is reached)
        if n > 0:
            top_color = plotmath.COLORS.get("pink")
            x0 = -s / 2
            y0 = (n - 1) * s
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=top_color)

    # --- Create figure with multiple pyramid patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(12, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw pyramids of different sizes
    s = 1
    draw_pyramid(axs[0], s=s, n=1)
    draw_pyramid(axs[1], s=s, n=2)
    draw_pyramid(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares mathematically
        n = i + 1
        # Sum of first n odd numbers: n²
        total_squares = n * n

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
            s=f"Antall ruter: {total_squares} = {n}²",
            fontsize=12,
            ha="center",
            va="center",
        )

        # Formula explanation
        formula_text = f"Sum av oddetall 1+3+5+...+{2*n-1}"
        ax.text(
            x=0,
            y=-(n + 3.5) * s,
            s=formula_text,
            fontsize=10,
            ha="center",
            va="center",
            style="italic",
        )

        # Set axis limits
        max_extent = max(n + 1, 3)
        ax.set_xlim(-max_extent * s, max_extent * s)
        ax.set_ylim(-(n + 4) * s, (n + 1) * s)

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
