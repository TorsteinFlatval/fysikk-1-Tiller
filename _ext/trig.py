"""Trig directive — triangles with smart labels and SymPy support

This directive renders one or more triangles with optional fills, vertex
markers, and labels for sides and angles (numeric or exact). Coordinates may
be SymPy expressions (pi, sqrt(2), etc.). Output is cached as an SVG in
``_static/trig/`` keyed by a content hash, similar to the plot directive.

Quick start (MyST)
------------------
:::{trig}
triangle: T1, (0, 0), (4, 0), (2, 3), solid, blue
fill: T1, lightblue, 0.2
label-sides: T1, exact
label-angles: T1, numeric
:::
"""

from __future__ import annotations

import hashlib
import math
import os
import re
import shutil
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives


def _hash_key(*parts) -> str:
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


def _strip_root_svg_size(svg_text: str) -> str:
    import re as _re

    def repl(m):
        tag = m.group(0)
        tag = _re.sub(r'\swidth="[^"]+"', "", tag)
        tag = _re.sub(r'\sheight="[^"]+"', "", tag)
        return tag

    return _re.sub(r"<svg\b[^>]*>", repl, svg_text, count=1)


def _rewrite_ids(txt: str, prefix: str) -> str:
    import re as _re

    ids = _re.findall(r'\bid="([^"]+)"', txt)
    if not ids:
        return txt
    skip_prefixes = (
        "DejaVu",
        "CM",
        "STIX",
        "Nimbus",
        "Bitstream",
        "Arial",
        "Times",
        "Helvetica",
    )
    mapping = {}
    for i in ids:
        if i.startswith(skip_prefixes):
            continue
        mapping[i] = f"{prefix}{i}"
    if not mapping:
        return txt

    def repl_id(m):
        old = m.group(1)
        new = mapping.get(old, old)
        return f'id="{new}"'

    txt = _re.sub(r'\bid="([^"]+)"', repl_id, txt)

    def repl_url(m):
        old = m.group(1).strip()
        new = mapping.get(old, old)
        return f"url(#{new})"

    txt = _re.sub(r"url\(#\s*([^\)\s]+)\s*\)", repl_url, txt)

    def repl_href(m):
        attr = m.group(1)
        quote = m.group(2)
        old = m.group(3).strip()
        new = mapping.get(old, old)
        return f"{attr}={quote}#{new}{quote}"

    txt = _re.sub(r'(xlink:href|href)\s*=\s*(["\"])#\s*([^"\"]+)\s*\2', repl_href, txt)
    return txt


def _safe_literal(val: str):
    import ast

    try:
        return ast.literal_eval(val)
    except Exception:
        return None


def _parse_text_positioning(pos: str) -> Tuple[str, str]:
    if not isinstance(pos, str):
        return ("top", "left")
    key = pos.strip().lower().replace("_", "-")
    mapping = {
        "top-left": ("bottom", "right"),
        "top-right": ("bottom", "left"),
        "bottom-left": ("top", "right"),
        "bottom-right": ("top", "left"),
        "top-center": ("bottom", "center"),
        "bottom-center": ("top", "center"),
        "center-left": ("center", "right"),
        "center-right": ("center", "left"),
        "center-center": ("center", "center"),
        # long variants (use larger offsets)
        "longtop-left": ("longbottom", "left"),
        "longbottom-left": ("longtop", "left"),
        "longtop-right": ("longbottom", "right"),
        "longbottom-right": ("longtop", "right"),
    }
    return mapping.get(key, ("top", "left"))


# ------------------------
# Trig directive
# ------------------------


@dataclass
class Triangle:
    tid: str
    pts: List[Tuple[float, float]]  # A, B, C in CCW order
    color: str | None = None
    linestyle: str | None = None

    # Computed geometry
    sides: Tuple[float, float, float] | None = None  # a,b,c opposite A,B,C
    angles_deg: Tuple[float, float, float] | None = None  # A,B,C in degrees


class TrigDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        "width": directives.length_or_percentage_or_unitless,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,
        "nocache": directives.flag,
        "debug": directives.flag,
        "alt": directives.unchanged,
        "figsize": directives.unchanged,
        "fontsize": directives.unchanged,
        "lw": directives.unchanged,
    }

    def _parse_kv_block(self) -> Tuple[Dict[str, Any], Dict[str, List[str]], int]:
        """Parse front matter supporting repeated keys for triangle primitives."""
        lines = list(self.content)
        scalars: Dict[str, Any] = {}
        lists: Dict[str, List[str]] = {
            "triangle": [],
            "fill": [],
            "show_vertices": [],
            "label-sides": [],
            "label-angles": [],
            "axis": [],
        }
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                if not line.strip():
                    idx += 1
                    continue
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
                if m:
                    key, value = m.group(1), m.group(2)
                    if key in lists:
                        lists[key].append(value)
                    else:
                        scalars[key] = value
                idx += 1
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return scalars, lists, idx

        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
            if m:
                key, value = m.group(1), m.group(2)
                if key in lists:
                    lists[key].append(value)
                else:
                    scalars[key] = value
                caption_start = i + 1
            else:
                break
        return scalars, lists, caption_start

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        try:
            import plotmath  # type: ignore
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(text=f"Kunne ikke importere plotmath: {e}")
            return [err]

        scalars, lists, caption_idx = self._parse_kv_block()
        merged: Dict[str, Any] = {**scalars, **self.options}

        # Numeric helpers
        _num_cache: Dict[str, float] = {}

        def _eval_expr(val) -> float:
            import sympy

            if val is None:
                raise ValueError("Empty value")
            if isinstance(val, (int, float)):
                return float(val)
            s0 = str(val).strip()
            if not s0:
                raise ValueError("Blank numeric expression")
            if s0 in _num_cache:
                return _num_cache[s0]
            allowed = {
                k: getattr(sympy, k)
                for k in [
                    "pi",
                    "E",
                    "exp",
                    "sqrt",
                    "log",
                    "sin",
                    "cos",
                    "tan",
                    "asin",
                    "acos",
                    "atan",
                    "Rational",
                ]
                if hasattr(sympy, k)
            }
            expr = sympy.sympify(s0, locals=allowed)
            valf = float(expr.evalf())
            _num_cache[s0] = valf
            return valf

        def _parse_figsize(val: Any):
            if not isinstance(val, str):
                return None
            s = val.strip()
            if not s:
                return None
            lit = _safe_literal(s)
            if isinstance(lit, (list, tuple)) and len(lit) >= 2:
                try:
                    w = float(lit[0])
                    h = float(lit[1])
                    if w > 0 and h > 0:
                        return (w, h)
                except Exception:
                    return None
            m = re.match(
                r"\(\s*([0-9]+(?:\.[0-9]+)?)\s*,\s*([0-9]+(?:\.[0-9]+)?)\s*\)", s
            )
            if m:
                try:
                    w = float(m.group(1))
                    h = float(m.group(2))
                    if w > 0 and h > 0:
                        return (w, h)
                except Exception:
                    return None
            return None

        fontsize = None
        try:
            fontsize = int(float(merged.get("fontsize", 20)))
        except Exception:
            fontsize = 20
        try:
            lw = float(merged.get("lw", 2.5))
        except Exception:
            lw = 2.5
        parsed_figsize = _parse_figsize(merged.get("figsize"))

        # Parse axis commands
        axis_cmds: List[str] = []
        for a in lists.get("axis", []):
            parts = [p.strip() for p in str(a).split(",") if p.strip()]
            for p in parts:
                if (p.startswith("'") and p.endswith("'")) or (
                    p.startswith('"') and p.endswith('"')
                ):
                    p = p[1:-1].strip()
                if p:
                    axis_cmds.append(p.lower())

        # Parse triangles
        triangles: Dict[str, Triangle] = {}

        def _extract_coord_pairs(seq: str) -> List[Tuple[str, str]]:
            pairs: List[Tuple[str, str]] = []
            i = 0
            n = len(seq)
            while i < n:
                if seq[i] == "(":
                    depth = 0
                    j = i
                    while j < n:
                        ch = seq[j]
                        if ch == "(":
                            depth += 1
                        elif ch == ")":
                            depth -= 1
                            if depth == 0:
                                inner = seq[i + 1 : j].strip()
                                # split inner on top-level comma
                                depth2 = 0
                                comma_index = -1
                                for k, ch2 in enumerate(inner):
                                    if ch2 == "(":
                                        depth2 += 1
                                    elif ch2 == ")":
                                        depth2 -= 1
                                    elif ch2 == "," and depth2 == 0:
                                        comma_index = k
                                        break
                                if comma_index != -1:
                                    x_expr = inner[:comma_index].strip()
                                    y_expr = inner[comma_index + 1 :].strip()
                                    if x_expr and y_expr:
                                        pairs.append((x_expr, y_expr))
                                i = j
                                break
                        j += 1
                i += 1
            return pairs

        _allowed_styles = {"solid", "dotted", "dashed", "dashdot"}

        for tline in lists.get("triangle", []):
            s = str(tline).strip()
            # expect: id, (x1,y1), (x2,y2), (x3,y3)[, linestyle][, color]
            parts: List[str] = []
            cur: List[str] = []
            depth = 0
            for ch in s:
                if ch == "(":
                    depth += 1
                    cur.append(ch)
                elif ch == ")":
                    depth -= 1
                    cur.append(ch)
                elif ch == "," and depth == 0:
                    tok = "".join(cur).strip()
                    if tok:
                        parts.append(tok)
                    cur = []
                else:
                    cur.append(ch)
            tail = "".join(cur).strip()
            if tail:
                parts.append(tail)
            if len(parts) < 4:
                continue
            tid = parts[0].strip().strip("'\"")
            pts_raw = _extract_coord_pairs(s)
            if len(pts_raw) < 3:
                continue
            pts: List[Tuple[float, float]] = []
            for xy in pts_raw[:3]:
                try:
                    xv = _eval_expr(xy[0])
                    yv = _eval_expr(xy[1])
                    pts.append((float(xv), float(yv)))
                except Exception:
                    pts = []
                    break
            if len(pts) != 3:
                continue
            # Optional style/color tokens after 3 tuples
            style_tok: str | None = None
            color_tok: str | None = None
            # Remove the id token and three tuple tokens from s to get the extras
            # Simplify by scanning remaining parts after the first 4 tokens
            for extra in parts[4:]:
                low = extra.strip().lower()
                if low in _allowed_styles and style_tok is None:
                    style_tok = low
                elif color_tok is None:
                    color_tok = extra.strip()
            tri = Triangle(tid=tid, pts=pts, linestyle=style_tok, color=color_tok)
            triangles[tid] = tri

        # Refs: fill/show_vertices/labels
        fills: List[Tuple[str, str | None, float | None]] = []
        for fline in lists.get("fill", []):
            toks = [p.strip() for p in fline.split(",") if p.strip()]
            if not toks:
                continue
            tid = toks[0].strip().strip("'\"")
            color = toks[1] if len(toks) >= 2 else None
            alpha: float | None = None
            if len(toks) >= 3:
                try:
                    alpha = float(_eval_expr(toks[2]))
                except Exception:
                    alpha = None
            fills.append((tid, color, alpha))

        vertex_marks: List[str] = [
            p.strip().strip("'\"") for p in lists.get("show_vertices", []) if p
        ]

        label_sides: Dict[str, str] = {}
        for ls in lists.get("label-sides", []):
            toks = [p.strip() for p in ls.split(",") if p.strip()]
            if not toks:
                continue
            mode = toks[1].lower() if len(toks) >= 2 else "numeric"
            label_sides[toks[0].strip().strip("'\"")] = (
                "exact" if mode == "exact" else "numeric"
            )

        label_angles: Dict[str, str] = {}
        for la in lists.get("label-angles", []):
            toks = [p.strip() for p in la.split(",") if p.strip()]
            if not toks:
                continue
            mode = toks[1].lower() if len(toks) >= 2 else "numeric"
            label_angles[toks[0].strip().strip("'\"")] = (
                "exact" if mode == "exact" else "numeric"
            )

        # Geometry helpers
        def _ccw_order(pts: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
            # order by signed area
            x1, y1 = pts[0]
            x2, y2 = pts[1]
            x3, y3 = pts[2]
            area2 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if area2 < 0:
                return [pts[0], pts[2], pts[1]]
            return pts

        def _sides_angles(tri: Triangle) -> None:
            import sympy as sp

            A, B, C = _ccw_order(tri.pts)
            tri.pts = [A, B, C]

            def dist(p, q):
                return math.hypot(q[0] - p[0], q[1] - p[1])

            # sides opposite A,B,C
            a = dist(B, C)
            b = dist(C, A)
            c = dist(A, B)
            tri.sides = (a, b, c)

            # angles via law of cosines
            def ang(opposite, s1, s2):
                if opposite <= 0 or s1 <= 0 or s2 <= 0:
                    return float("nan")
                val = max(
                    -1.0,
                    min(1.0, (s1 * s1 + s2 * s2 - opposite * opposite) / (2 * s1 * s2)),
                )
                return math.degrees(math.acos(val))

            Adeg = ang(a, b, c)
            Bdeg = ang(b, c, a)
            Cdeg = ang(c, a, b)
            tri.angles_deg = (Adeg, Bdeg, Cdeg)

            # store simplified "exact" side strings on the instance for later if requested
            tri.side_exact = None  # type: ignore[attr-defined]
            tri.angle_exact = None  # type: ignore[attr-defined]
            try:
                Ax, Ay = map(sp.nsimplify, A)
                Bx, By = map(sp.nsimplify, B)
                Cx, Cy = map(sp.nsimplify, C)

                def exact_len(P, Q):
                    dx = sp.nsimplify(Q[0] - P[0])
                    dy = sp.nsimplify(Q[1] - P[1])
                    s2 = sp.simplify(dx * dx + dy * dy)
                    try:
                        return sp.sqrt(s2)
                    except Exception:
                        return sp.sqrt(s2)

                ea = exact_len(B, C)
                eb = exact_len(C, A)
                ec = exact_len(A, B)
                tri.side_exact = (ea, eb, ec)  # type: ignore[attr-defined]

                # angles: only generate exact if nicely rational multiples; otherwise keep numeric
                def exact_angle(alpha_deg: float):
                    # Try to snap to common exacts
                    snaps = [
                        0,
                        15,
                        18,
                        22.5,
                        30,
                        36,
                        45,
                        60,
                        72,
                        90,
                        108,
                        120,
                        135,
                        150,
                        180,
                    ]
                    for s in snaps:
                        if abs(alpha_deg - s) < 1e-6:
                            return s
                    return None

                tri.angle_exact = tuple(
                    exact_angle(v) for v in (Adeg, Bdeg, Cdeg)
                )  # type: ignore[attr-defined]
            except Exception:
                pass

        for tri in triangles.values():
            _sides_angles(tri)

        # Build content hash for caching
        content_hash = _hash_key(
            ";".join(
                [
                    f"{tid}:{','.join(f'{x},{y}' for x,y in tri.pts)}:{tri.linestyle or ''}:{tri.color or ''}"
                    for tid, tri in sorted(triangles.items())
                ]
            ),
            ";".join(
                [f"{t}:{c or ''}:{a if a is not None else ''}" for (t, c, a) in fills]
            ),
            ",".join(vertex_marks),
            ";".join([f"{k}:{v}" for k, v in sorted(label_sides.items())]),
            ";".join([f"{k}:{v}" for k, v in sorted(label_angles.items())]),
            "|".join(axis_cmds),
            "axis-defaults:off+equal@2025-10-03",
            fontsize,
            lw,
            str(parsed_figsize),
        )
        explicit_name = merged.get("name")
        base_name = explicit_name or f"trig_{content_hash}"

        rel_dir = os.path.join("_static", "trig")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        debug_mode = "debug" in merged

        if regenerate:
            import matplotlib

            matplotlib.use("Agg")
            try:
                import matplotlib.pyplot as _plt

                fig, ax = _plt.subplots()
                # Defaults similar to plot directive
                fig.set_size_inches(6.0, 6.0)
                # Axis behavior: always off and equal by default
                axis_off = True
                axis_equal = True
                ax.axis("off")
                ax.axis("equal")

                # Draw triangles
                style_map = {
                    "solid": "-",
                    "dotted": ":",
                    "dashed": "--",
                    "dashdot": "-.",
                }
                default_edge_color = plotmath.COLORS.get("black") or "black"

                # First pass: draw edges and collect global bounds
                all_x: List[float] = []
                all_y: List[float] = []
                for tri in triangles.values():
                    xs = [p[0] for p in tri.pts] + [tri.pts[0][0]]
                    ys = [p[1] for p in tri.pts] + [tri.pts[0][1]]
                    all_x.extend([p[0] for p in tri.pts])
                    all_y.extend([p[1] for p in tri.pts])
                    ls = style_map.get((tri.linestyle or "solid").lower(), "-")
                    col = plotmath.COLORS.get(tri.color) if tri.color else None
                    col_use = (col if col else tri.color) or default_edge_color
                    ax.plot(xs, ys, linestyle=ls, color=col_use, lw=lw)

                # Auto bounds with small padding if not equal (equal is default)
                if all_x and all_y and not axis_equal:
                    minx, maxx = min(all_x), max(all_x)
                    miny, maxy = min(all_y), max(all_y)
                    dx = max(1e-6, (maxx - minx))
                    dy = max(1e-6, (maxy - miny))
                    ax.set_xlim(minx - 0.1 * dx, maxx + 0.1 * dx)
                    ax.set_ylim(miny - 0.1 * dy, maxy + 0.1 * dy)

                # Compute pixel metrics for consistent visual offsets
                try:
                    fig.canvas.draw()
                    _bbox_px = ax.get_window_extent()
                    _ax_w_px, _ax_h_px = _bbox_px.width, _bbox_px.height
                except Exception:
                    _ax_w_px = _ax_h_px = None

                def _offset_point(
                    x0: float, y0: float, pos: str
                ) -> Tuple[float, float]:
                    va, ha = _parse_text_positioning(pos)
                    _fx_short = 0.015
                    _fy_short = 0.015
                    _fx_long = 0.03
                    _fy_long = 0.03
                    use_fx = _fx_short
                    use_fy = _fy_short
                    if va == "longbottom":
                        va = "bottom"
                        use_fy = _fy_long
                    elif va == "longtop":
                        va = "top"
                        use_fy = _fy_long
                    if ha == "longright":
                        ha = "right"
                        use_fx = _fx_long
                    elif ha == "longleft":
                        ha = "left"
                        use_fx = _fx_long
                    xmin, xmax = ax.get_xlim()
                    ymin, ymax = ax.get_ylim()
                    ax_dx = xmax - xmin
                    ax_dy = ymax - ymin
                    if _ax_w_px and _ax_h_px:
                        dx_px = 0.0
                        dy_px = 0.0
                        if ha == "right":
                            dx_px = -_ax_w_px * use_fx
                        elif ha == "left":
                            dx_px = _ax_w_px * use_fx
                        if va == "bottom":
                            dy_px = _ax_h_px * use_fy
                        elif va == "top":
                            dy_px = -_ax_h_px * use_fy
                        x_disp, y_disp = ax.transData.transform((x0, y0))
                        x1, y1 = ax.transData.inverted().transform(
                            (x_disp + dx_px, y_disp + dy_px)
                        )
                        return (x1, y1)
                    # fallback
                    dx = (use_fx * ax_dx) * (
                        1 if ha == "left" else -1 if ha == "right" else 0
                    )
                    dy = (use_fy * ax_dy) * (
                        1 if va == "bottom" else -1 if va == "top" else 0
                    )
                    return (x0 + dx, y0 + dy)

                # Fills
                for tid, color, alpha in fills:
                    tri = triangles.get(tid)
                    if not tri:
                        continue
                    xs = [p[0] for p in tri.pts]
                    ys = [p[1] for p in tri.pts]
                    c = plotmath.COLORS.get(color) if color else None
                    col_use = (c if c else color) or plotmath.COLORS.get("blue")
                    a = 0.1 if alpha is None else alpha
                    try:
                        ax.fill(xs, ys, color=col_use, alpha=a, linewidth=0)
                    except Exception:
                        pass

                # Vertex markers
                for tid in vertex_marks:
                    tri = triangles.get(tid)
                    if not tri:
                        continue
                    for x0, y0 in tri.pts:
                        ax.plot(x0, y0, "o", markersize=8, alpha=0.9, color="black")

                # Side labels
                for tid, mode in label_sides.items():
                    tri = triangles.get(tid)
                    if not tri or not tri.sides:
                        continue
                    A, B, C = tri.pts
                    mids = [
                        ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2),
                        ((C[0] + A[0]) / 2, (C[1] + A[1]) / 2),
                        ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2),
                    ]
                    texts: List[str] = []
                    if mode == "exact" and getattr(tri, "side_exact", None):
                        import sympy as sp

                        for s in tri.side_exact:  # type: ignore[attr-defined]
                            try:
                                texts.append(f"${sp.latex(sp.simplify(s))}$")
                            except Exception:
                                texts.append(f"{float(s):.2f}")
                    else:
                        for s in tri.sides:
                            texts.append(f"{s:.2f}")
                    # Place labels slightly outward from triangle center along normal
                    center = (
                        sum(x for x, _ in tri.pts) / 3.0,
                        sum(y for _, y in tri.pts) / 3.0,
                    )
                    edges = [(B, C), (C, A), (A, B)]
                    for mid, text, (P, Q) in zip(mids, texts, edges):
                        # edge direction
                        ex, ey = Q[0] - P[0], Q[1] - P[1]
                        # outward normal: pick one and nudge away from center
                        nx, ny = -ey, ex
                        # choose sign so that it points away from center
                        vx, vy = mid[0] - center[0], mid[1] - center[1]
                        if nx * vx + ny * vy < 0:
                            nx, ny = -nx, -ny
                        # normalize and scale via pixel metric
                        nlen = math.hypot(nx, ny) or 1.0
                        nx /= nlen
                        ny /= nlen
                        # convert ~1.5% of axis to data units using pixel transform
                        px = 0.0
                        py = 0.0
                        if _ax_w_px and _ax_h_px:
                            x_disp, y_disp = ax.transData.transform(mid)
                            # offset in pixels along normal: use smaller of width/height fraction
                            dpx = 0.015 * min(_ax_w_px, _ax_h_px)
                            x1, y1 = ax.transData.inverted().transform(
                                (x_disp + nx * dpx, y_disp + ny * dpx)
                            )
                            px, py = x1 - mid[0], y1 - mid[1]
                        else:
                            xmin, xmax = ax.get_xlim()
                            ymin, ymax = ax.get_ylim()
                            px = 0.015 * (xmax - xmin) * nx
                            py = 0.015 * (ymax - ymin) * ny
                        ax.text(
                            mid[0] + px,
                            mid[1] + py,
                            text,
                            fontsize=fontsize,
                            ha="center",
                            va="center",
                        )

                # Angle arcs and labels; right-angle mark when applicable
                def _draw_angle(ax, O, P, Q, label_text: str | None):
                    import numpy as _np

                    # vectors
                    v1 = (P[0] - O[0], P[1] - O[1])
                    v2 = (Q[0] - O[0], Q[1] - O[1])
                    a1 = math.atan2(v1[1], v1[0])
                    a2 = math.atan2(v2[1], v2[0])
                    # Normalize to CCW sweep
                    while a2 < a1:
                        a2 += 2 * math.pi
                    ang = a2 - a1
                    # Arc radius via pixel metric
                    base_r = 0.0
                    if _ax_w_px and _ax_h_px:
                        x_disp, y_disp = ax.transData.transform(O)
                        # Use ~3% of min axis dimension
                        dpx = 0.03 * min(_ax_w_px, _ax_h_px)
                        x1, y1 = ax.transData.inverted().transform(
                            (x_disp + dpx, y_disp)
                        )
                        base_r = abs(x1 - O[0])
                    else:
                        xmin, xmax = ax.get_xlim()
                        ymin, ymax = ax.get_ylim()
                        base_r = 0.06 * min(xmax - xmin, ymax - ymin)
                    # Right-angle square if angle ~ 90°
                    if abs(math.degrees(ang) - 90.0) < 1e-3:
                        # make a small square inside angle
                        r_sq = base_r * 0.8

                        # unit directions
                        def unit(v):
                            L = math.hypot(v[0], v[1]) or 1.0
                            return (v[0] / L, v[1] / L)

                        u1 = unit(v1)
                        u2 = unit(v2)
                        p1 = (O[0] + u1[0] * r_sq, O[1] + u1[1] * r_sq)
                        p2 = (p1[0] + u2[0] * (r_sq), p1[1] + u2[1] * (r_sq))
                        p3 = (O[0] + u2[0] * r_sq, O[1] + u2[1] * r_sq)
                        ax.plot([O[0], p1[0]], [O[1], p1[1]], color="black", lw=1)
                        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="black", lw=1)
                        ax.plot([p2[0], p3[0]], [p2[1], p3[1]], color="black", lw=1)
                        ax.plot([O[0], p3[0]], [O[1], p3[1]], color="black", lw=1)
                    # arc
                    t = _np.linspace(a1, a2, 128)
                    xs = O[0] + base_r * _np.cos(t)
                    ys = O[1] + base_r * _np.sin(t)
                    ax.plot(xs, ys, color="black", lw=1)
                    # label at mid-angle
                    if label_text:
                        am = 0.5 * (a1 + a2)
                        xm = O[0] + (base_r + 0.02 * base_r) * math.cos(am)
                        ym = O[1] + (base_r + 0.02 * base_r) * math.sin(am)
                        ax.text(
                            xm,
                            ym,
                            label_text,
                            fontsize=fontsize,
                            ha="center",
                            va="center",
                        )

                for tid, mode in label_angles.items():
                    tri = triangles.get(tid)
                    if not tri or not tri.angles_deg:
                        continue
                    A, B, C = tri.pts
                    angles = tri.angles_deg
                    labels: List[str] = []
                    if mode == "exact" and getattr(tri, "angle_exact", None):
                        for i, val in enumerate(getattr(tri, "angle_exact")):  # type: ignore[attr-defined]
                            if val is not None:
                                labels.append(f"{val:.0f}°")
                            else:
                                labels.append(f"{angles[i]:.1f}°")
                    else:
                        labels = [f"{a:.1f}°" for a in angles]
                    # Draw arcs with labels
                    _draw_angle(ax, A, B, C, labels[0])
                    _draw_angle(ax, B, C, A, labels[1])
                    _draw_angle(ax, C, A, B, labels[2])

                # Apply figsize at end
                if parsed_figsize is not None:
                    try:
                        fig.set_size_inches(*parsed_figsize)
                    except Exception:
                        pass

                try:
                    fig.tight_layout()
                except Exception:
                    pass

                fig.savefig(
                    abs_svg,
                    format="svg",
                    transparent=True,
                )
                if debug_mode:
                    try:
                        fig.savefig(
                            os.path.join(abs_dir, f"{base_name}.pdf"),
                            format="pdf",
                            transparent=True,
                        )
                    except Exception:
                        pass

                matplotlib.pyplot.close(fig)
            except Exception as e:
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av trig-figur: {e}", line=self.lineno
                    )
                ]

        if not os.path.exists(abs_svg):
            return [
                self.state_machine.reporter.error(
                    "trig: SVG mangler.", line=self.lineno
                )
            ]

        env.note_dependency(abs_svg)
        # copy into build _static
        try:
            out_static = os.path.join(app.outdir, "_static", "trig")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"trig inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

        if "viewBox" in raw_svg and "debug" not in merged:
            raw_svg = _strip_root_svg_size(raw_svg)

        if "debug" not in merged:
            raw_svg = _rewrite_ids(
                raw_svg, f"trg_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = "Trekantfigur"
        alt = merged.get("alt", alt_default)

        width_opt = merged.get("width")
        percent = isinstance(width_opt, str) and width_opt.strip().endswith("%")

        def _augment(m):
            tag = m.group(0)
            if "class=" not in tag:
                tag = tag[:-1] + ' class="graph-inline-svg"' + ">"
            else:
                tag = tag.replace('class="', 'class="graph-inline-svg ')
            if alt and "aria-label=" not in tag:
                tag = tag[:-1] + f' role="img" aria-label="{alt}"' + ">"
            if width_opt:
                if percent:
                    wval = width_opt.strip()
                else:
                    wval = width_opt.strip()
                    if wval.isdigit():
                        wval += "px"
                style_frag = f"width:{wval}; height:auto; display:block; margin:0 auto;"
                if "style=" in tag:
                    import re as _re

                    tag = _re.sub(
                        r'style="([^"]*)"',
                        lambda mm: f'style="{mm.group(1)}; {style_frag}"',
                        tag,
                        count=1,
                    )
                else:
                    tag = tag[:-1] + f' style="{style_frag}"' + ">"
            return tag

        import re as _re

        raw_svg = _re.sub(r"<svg\b[^>]*>", _augment, raw_svg, count=1)

        figure = nodes.figure()
        figure.setdefault("classes", []).extend(
            ["adaptive-figure", "trig-figure", "no-click"]
        )
        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            ["graph-image", "no-click", "no-scaled-link"]
        )
        figure += raw_node

        extra_classes = merged.get("class")
        if extra_classes:
            figure["classes"].extend(extra_classes)
        figure["align"] = merged.get("align", "center")

        caption_lines = list(self.content)[caption_idx:]
        while caption_lines and not caption_lines[0].strip():
            caption_lines.pop(0)
        if caption_lines:
            caption = nodes.caption()
            caption += nodes.Text("\n".join(caption_lines))
            figure += caption

        if explicit_name:
            self.add_name(figure)
        return [figure]


def setup(app):  # pragma: no cover
    app.add_directive("trig", TrigDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
