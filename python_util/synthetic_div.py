import os


def synthetic_div(
    fname: str,
    p: str,
    x: float,
    stage: int = 12,
    svg: bool = True,
    tutor: bool = False,
):

    if not tutor:
        div_cmd = (
            r"\polyhornerscheme[x={x}, resultstyle=\color{red}, showvar=true]{{p}}"
        )
        div_cmd = div_cmd.replace("{p}", p).replace("{x}", str(x))
    else:
        div_cmd = r"\polyhornerscheme[x={x}, stage={stage}, tutor=true, tutorlimit=12, resultstyle=\color{red}, showvar=true]{{p}}"
        div_cmd = (
            div_cmd.replace("{p}", p)
            .replace("{x}", str(x))
            .replace("{stage}", str(stage))
        )

    s = f"""\\documentclass{{standalone}}
\\usepackage{{polynom}}
\\usepackage{{xcolor}}
\\begin{{document}}
{div_cmd}
\\end{{document}}
    """

    with open("tmp.tex", "w") as f:
        f.write(s)

    os.system("pdflatex tmp.tex")
    if fname.endswith(".svg"):
        fname.strip(".svg")

    if svg:
        os.system(f"pdf2svg tmp.pdf {fname}.svg")
    else:
        os.system(f"mv tmp.pdf {fname}.pdf")

    os.system("rm tmp.*")


if __name__ == "__main__":
    synthetic_div(
        fname="test",
        p="x^3 + 2x^2 - 3x - 6",
        x=1,
        stage=None,
    )
