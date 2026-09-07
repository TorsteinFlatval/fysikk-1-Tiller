import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    """Blomst-sekvens med fire trekantede kronblad (kvadratruter).

    Figur n (n>=1) består av:
      - Ett sentrum (1 rute) i (0,0)
      - 4 *trekanter* av kvadrater (kronblad) langs +x, -x, +y, -y.
        Hver trekant har n lag: For x=1..n inneholder kronbladet alle ruter
        (x, y) med |y| <= x-1 (altså 1,3,5,..., (2n-1) ruter på radene i
        hvert kronblad) – dette gir n^2 ruter per kronblad.

    Totalt:
        T(n) = 1 + 4 n^2

    Økning:
        T(n) - T(n-1) = 4( n^2 - (n-1)^2 ) = 4(2n-1) = 8n - 4
        (vekst 4,12,20,28,... for n=1,2,3,4,...)

    Strategier for elever:
      - Dele figuren i 4 like kronblad + sentrum.
      - Gjenkjenne at hvert kronblad er summen av første n oddetall = n^2.
      - Alternativt bygge tabell for vekst (2. differanse konstant 8 -> kvadratisk formel).
    """

    alpha = 0.65
    center_color = plotmath.COLORS.get("yellow")
    petal_colors = [
        plotmath.COLORS.get("common"),
        plotmath.COLORS.get("rare"),
        plotmath.COLORS.get("epic"),
        plotmath.COLORS.get("legendary"),
    ]

    def square(ax, s, x, y, color):
        A = (x * s - s / 2, y * s - s / 2)
        B = (x * s + s / 2, y * s - s / 2)
        C = (x * s + s / 2, y * s + s / 2)
        D = (x * s - s / 2, y * s + s / 2)
        plotmath.plot_polygon(A, B, C, D, ax=ax, alpha=alpha, color=color)

    def draw_flower(ax, s, n):
        # Sentrum
        square(ax, s, 0, 0, center_color)
        # Kronblad langs +x og -x
        for x in range(1, n + 1):
            width = x - 1  # strekker seg i y-retning
            for y in range(-width, width + 1):
                square(ax, s, x, y, petal_colors[0])  # +x kronblad
                square(ax, s, -x, y, petal_colors[1])  # -x kronblad
        # Kronblad langs +y og -y
        for y in range(1, n + 1):
            width = y - 1
            for x in range(-width, width + 1):
                square(ax, s, x, y, petal_colors[2])  # +y kronblad
                square(ax, s, x, -y, petal_colors[3])  # -y kronblad

    # --- Lag panel for n = 1,2,3 ---
    fig, axs = plt.subplots(
        1,
        3,
        figsize=(11, 4),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    s = 1
    for idx, n in enumerate([1, 2, 3]):
        draw_flower(axs[idx], s=s, n=n)

    for i, ax in enumerate(axs):
        n = i + 1
        ax.set_aspect("equal")
        ax.axis("off")

        total = 1 + 4 * n * n
        formula = f"1 + 4·{n}² = {total}"
        diff_prev = 4 if n == 1 else 8 * n - 4
        ax.text(
            0,
            (n + 1.3) * s,
            f"Figur {n}",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold",
        )
        # ax.text(
        #     0,
        #     -(n + 1.4) * s,
        #     f"Antall: {formula}\nØkning fra forrige: {diff_prev}",
        #     fontsize=10,
        #     ha="center",
        #     va="center",
        #     linespacing=1.2,
        # )

        # Aksegrenser: ytterste punkt ligger ved (±n, ±(n-1)) eller (±(n-1), ±n)
        lim = n + 1
        ax.set_xlim(-(lim) * s, (lim) * s)
        ax.set_ylim(-(lim) * s, (lim) * s)

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
