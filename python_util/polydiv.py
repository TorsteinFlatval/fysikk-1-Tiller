import os


def polylongdiv(
    fname: str, p: str, q: str, stage: int = None, svg: bool = True, vars=None
):
    if not vars:
        vars = "x"

    # Generate unique temp filenames
    import uuid

    temp_id = uuid.uuid4().hex[:8]
    tex_file = f"tmp_{temp_id}.tex"
    pdf_file = f"tmp_{temp_id}.pdf"

    # Format LaTeX command
    if stage is None:
        div_cmd = r"\polylongdiv[style=C, div=:, vars=None]{{p}}{{q}}"
        div_cmd = div_cmd.replace("{p}", p).replace("{q}", q).replace("None", str(vars))
    else:
        div_cmd = r"\polylongdiv[style=C, div=:, stage={stage}]{{p}}{{q}}"
        div_cmd = (
            div_cmd.replace("{p}", p).replace("{q}", q).replace("{stage}", str(stage))
        )

    # Create LaTeX file
    s = f"""\\documentclass[border=0.2cm]{{standalone}}
\\usepackage{{polynom}}
\\begin{{document}}
{div_cmd}
\\end{{document}}
    """

    # Remove .svg extension properly if present
    if fname.endswith(".svg"):
        fname = fname[:-4]  # Correct way to remove extension

    # Write and process files
    with open(tex_file, "w") as f:
        f.write(s)

    os.system(f"pdflatex {tex_file}")

    if svg:
        os.system(f"pdf2svg {pdf_file} {fname}.svg")
    else:
        os.system(f"mv {pdf_file} {fname}.pdf")

    # Cleanup with more specific pattern
    os.system(f"rm tmp_{temp_id}.*")
