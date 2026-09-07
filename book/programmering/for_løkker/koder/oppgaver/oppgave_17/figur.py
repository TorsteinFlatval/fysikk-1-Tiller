import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Create a 'cat'-like pattern with tail, head, and body components."""
    alpha = 0.6

    def draw_cat(ax, s, n):
        """Draw a cat-like pattern for the n-th figure."""

        # TAIL: diagonal line going upper-left, f(n) = n squares
        # Starts from origin and goes diagonally up-left
        tail_offset_x = -n * s
        tail_offset_y = n * s
        for k in range(n):
            x0 = tail_offset_x - k * s
            y0 = tail_offset_y + k * s
            # x0, y0 = -k * s, k * s
            A = (x0, y0)
            B = (x0 - s, y0)
            C = (x0 - s, y0 + s)
            D = (x0, y0 + s)

            color = plotmath.COLORS.get("blue")  # Tail color
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

        # HEAD: n×n square at upper-right
        # Position it so it's connected but distinct
        head_offset_x = (n + 1) * s  # Move right
        head_offset_y = n * s  # Move up

        for i in range(n):
            for j in range(n):
                x0 = head_offset_x + i * s
                y0 = head_offset_y + j * s
                A = (x0, y0)
                B = (x0 + s, y0)
                C = (x0 + s, y0 + s)
                D = (x0, y0 + s)

                color = plotmath.COLORS.get("blue")  # Head color
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

        # BODY: bridge-like structure connecting tail and head
        # (n + 1) * n - 1 squares forming a bridge
        # Let's create a horizontal bridge from tail end to head start
        # Create left part of the bridge

        for i in range(n):
            for j in range(n):
                x0 = -s * (i + 1)
                y0 = j * s
                A = (x0, y0)
                B = (x0, y0 - s)
                C = (x0 + s, y0 - s)
                D = (x0 + s, y0)

                color = plotmath.COLORS.get("blue")  # Body color
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

        # Build the right part of the bridge
        for i in range(n):
            for j in range(n):
                x0 = s * (i + 1)
                y0 = j * s
                A = (x0, y0)
                B = (x0, y0 - s)
                C = (x0 + s, y0 - s)
                D = (x0 + s, y0)

                color = plotmath.COLORS.get("blue")  # Body color
                plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

        # build the top part of the bridge
        for i in range(-n, n + 1):
            x0 = -s * i
            y0 = s * (n - 1)
            A = (x0, y0)
            B = (x0 + s, y0)
            C = (x0 + s, y0 + s)
            D = (x0, y0 + s)

            color = plotmath.COLORS.get("blue")  # Body color
            plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

    # --- Create figure with multiple cat patterns ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(8, 3),  # Wider to accommodate cat shapes
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Draw cats of different sizes
    s = 1
    draw_cat(axs[0], s=s, n=1)
    draw_cat(axs[1], s=s, n=2)
    draw_cat(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Calculate total squares for this figure
        n = i + 1
        tail_squares = n
        head_squares = n * n
        body_squares = (n + 1) * n - 1
        total_squares = tail_squares + head_squares + body_squares

        ax.text(
            x=n * s / 2,  # Center under the figure
            y=-2 * s,
            s=f"Figur {n}",
            fontsize=20,
            ha="center",
            va="center",
            weight="bold",
        )

        # Set reasonable axis limits
        ax.set_xlim(-(3.2 + n) * s, (5 + n) * s)
        ax.set_ylim(-(3 + n) * s, (5 + n) * s)

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
    main(dirname=dirname, save=True)
