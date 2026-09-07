import plotmath
import numpy as np
import matplotlib.pyplot as plt


def main(dirname, save):
    """Lag en sekvens av "diamant"-mønstre (Manhattan-sirkler).

    Figur n består av alle ruter (x, y) med |x| + |y| <= n.
    Dette gir et veldig regelmessig mønster der hvert nytt lag k (1..n)
    består av 4k nye ruter. Dermed:

        Total(n) = 1 + 4 * (1 + 2 + ... + n) = 1 + 2 n (n + 1).

    Denne sekvensen er lettere å analysere enn den gamle spiralen:
    - Ett sentralt kvadrat (n=0)
    - Lag 1: 4*1 nye
    - Lag 2: 4*2 nye
    - ...
    - Lag n: 4*n nye

    Elever kan først finne antall i hvert lag og så summere.
    """
    alpha = 0.65

    def draw_diamond(ax, s, n):
        """Tegn diamant (Manhattan radius n)."""
        colors = ["blue", "green", "orange", "purple", "red", "pink", "yellow"]

        # Lag 0 (sentrum)
        center_color = plotmath.COLORS.get(colors[0])
        A = (-s / 2, -s / 2)
        B = (s / 2, -s / 2)
        C = (s / 2, s / 2)
        D = (-s / 2, s / 2)
        plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=center_color)

        # Lag k: alle (x,y) med |x| + |y| = k
        for k in range(1, n + 1):
            layer_color = plotmath.COLORS.get(colors[k % len(colors)])
            for x in range(-k, k + 1):
                y_abs = k - abs(x)
                # To punkter: (x, y_abs) og (x, -y_abs) (dersom y_abs != 0)
                coords = [(x, y_abs)] if y_abs == 0 else [(x, y_abs), (x, -y_abs)]
                for px, py in coords:
                    A = (px * s - s / 2, py * s - s / 2)
                    B = (px * s + s / 2, py * s - s / 2)
                    C = (px * s + s / 2, py * s + s / 2)
                    D = (px * s - s / 2, py * s + s / 2)
                    plotmath.plot_polygon(
                        A, B, C, D, ax=ax, alpha=alpha, color=layer_color
                    )

    # --- Lag figur med tre diamantskikt ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(11, 4),  # Bred nok for diamant-mønstre
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    # Tegn diamant for n = 1, 2, 3
    s = 1
    draw_diamond(axs[0], s=s, n=1)
    draw_diamond(axs[1], s=s, n=2)
    draw_diamond(axs[2], s=s, n=3)

    for i, ax in enumerate(axs):
        ax.set_aspect("equal")
        ax.axis("off")

        # Beregn total antall ruter med formelen 1 + 2 n (n + 1)
        n = i + 1
        total_squares = 1 + 2 * n * (n + 1)
        # Antall i lag k er 4k for k>=1, lag 0 er 1
        layer_breakdown = " + ".join(["1"] + [f"4·{k}" for k in range(1, n + 1)])

        ax.text(
            x=0,
            y=-(n + 2.5) * s,
            s=f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )

        # ax.text(
        #     x=0,
        #     y=-(n + 3.5) * s,
        #     s=f"Antall ruter: {total_squares} = {layer_breakdown}",
        #     fontsize=11,
        #     ha="center",
        #     va="center",
        # )

        max_extent = n + 2
        ax.set_xlim(-max_extent * s, max_extent * s)
        ax.set_ylim(-(max_extent + 1) * s, max_extent * s)

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
