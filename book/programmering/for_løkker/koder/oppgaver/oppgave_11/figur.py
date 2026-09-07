import plotmath
import matplotlib.pyplot as plt


def main(dirname: str, save: bool = True) -> None:
    """Visualise *centred 8‑point star numbers*.

    The *n*-th figure consists of a centre cell plus four orthogonal arms and
    four diagonal arms (a thin ✱).  Its square‑count obeys the **linear**
    polynomial

        p(n) = 8 n + 1,

    i.e. 1, 9, 17, 25, 33, … for n = 0, 1, 2, 3, 4 …
    """

    alpha = 0.25  # square transparency

    # ──────────────────────────────────────────────────────────────────
    # Helper: draw centred 8‑point star of radius n ────────────────────
    # ──────────────────────────────────────────────────────────────────
    def draw_star(ax, s: float, n: int) -> None:
        """Plot squares whose centres satisfy (x = 0) ∨ (y = 0) ∨ (|x| = |y|)."""
        # Plus‑sign arms (vertical & horizontal)
        for k in range(-n, n + 1):
            # Horizontal arm (y = 0)
            x0 = k * s - 0.5 * s
            y0 = -0.5 * s
            plotmath.plot_polygon(
                (x0, y0),
                (x0 + s, y0),
                (x0 + s, y0 + s),
                (x0, y0 + s),
                ax=ax,
                alpha=alpha,
                color=plotmath.COLORS.get("rare"),
            )

            if k == 0:
                continue  # central square drawn once only

            # Vertical arm (x = 0)
            x0 = -0.5 * s
            y0 = k * s - 0.5 * s
            plotmath.plot_polygon(
                (x0, y0),
                (x0 + s, y0),
                (x0 + s, y0 + s),
                (x0, y0 + s),
                ax=ax,
                alpha=alpha,
                color=plotmath.COLORS.get("rare"),
            )

        # Diagonal arms (y = ±x)
        for k in range(1, n + 1):  # skip k = 0 (already centre)
            # Main diagonal (y = x)
            x0 = k * s - 0.5 * s
            y0 = k * s - 0.5 * s
            plotmath.plot_polygon(
                (x0, y0),
                (x0 + s, y0),
                (x0 + s, y0 + s),
                (x0, y0 + s),
                ax=ax,
                alpha=alpha,
                color=plotmath.COLORS.get("rare"),
            )

            x0 = -k * s - 0.5 * s
            y0 = -k * s - 0.5 * s
            plotmath.plot_polygon(
                (x0, y0),
                (x0 + s, y0),
                (x0 + s, y0 + s),
                (x0, y0 + s),
                ax=ax,
                alpha=alpha,
                color=plotmath.COLORS.get("rare"),
            )

            # Anti‑diagonal (y = −x)
            x0 = k * s - 0.5 * s
            y0 = -k * s - 0.5 * s
            plotmath.plot_polygon(
                (x0, y0),
                (x0 + s, y0),
                (x0 + s, y0 + s),
                (x0, y0 + s),
                ax=ax,
                alpha=alpha,
                color=plotmath.COLORS.get("rare"),
            )

            x0 = -k * s - 0.5 * s
            y0 = k * s - 0.5 * s
            plotmath.plot_polygon(
                (x0, y0),
                (x0 + s, y0),
                (x0 + s, y0 + s),
                (x0, y0 + s),
                ax=ax,
                alpha=alpha,
                color=plotmath.COLORS.get("rare"),
            )

    # ──────────────────────────────────────────────────────────────────
    # Figure setup ─────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
    max_n = 3  # show n = 0 … 3
    fig, axs = plt.subplots(
        1,
        max_n,
        figsize=(9, 3),  # ~2.7″ per subplot
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    s = 1  # unit‑square side length

    for i, n in enumerate(range(1, max_n + 1)):
        draw_star(axs[i], s=s, n=n)
        ax = axs[i]
        ax.set_aspect("equal")
        ax.axis("off")
        ax.text(
            x=0,
            y=-(max_n + 2) * s,
            s=f"Figur {i + 1}",
            fontsize=22,
            ha="center",
            va="center",
        )
        limit = (n + 0.5) * s * 1.5 + (max_n - n) * 0  # loose padding
        limit = (max_n + 1) * s
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)

    # ──────────────────────────────────────────────────────────────────
    # Output ───────────────────────────────────────────────────────────
    # ──────────────────────────────────────────────────────────────────
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
