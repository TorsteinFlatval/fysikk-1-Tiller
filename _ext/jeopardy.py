from __future__ import annotations

import json
import html as _html
import os
import re
import uuid
from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class JeopardyDirective(SphinxDirective):
    """Directive that renders a Jeopardy-like board with categories and values.

    Content format:

    Category: Algebra
    100:
      Q: What is 2+3?
      A: 5
    200:
      Q: ![{width="60%" class="adaptive-figure"}](path/to/image.png)\nSolve x+2=5
      A: x = 3

    Category: Geometry
    100:
      Q: $a^2+b^2=c^2$
      A: Pythagoras

    - Images in questions/answers are handled like the quiz directive using
      Markdown image syntax and copied to _static/figurer/... with a unique name.
    - Math is supported via KaTeX (same includes as quiz).
    """

    has_content = True
    required_arguments = 0
    option_spec = {
        "teams": directives.unchanged,  # number of teams (default 2)
    }

    def run(self):
        self.board_id = uuid.uuid4().hex
        container_id = f"jeopardy-{self.board_id}"

        # Parse content into data structure
        data = self._parse_board()

        # Compute relative prefix to _static (like in quiz image logic)
        source_file = self.state.document["source"]
        source_dir = os.path.dirname(source_file)
        app_src_dir = self.env.srcdir
        depth = os.path.relpath(source_dir, app_src_dir).count(os.sep)
        rel_prefix = "../" * (depth + 1)

        # Include KaTeX like quiz does
        # Embed JSON config safely in an HTML attribute: use double quotes and HTML-escape
        cfg_str = _html.escape(json.dumps(data, ensure_ascii=False), quote=True)
        json_str = json.dumps(data, ensure_ascii=False)
        html = f"""
        <div id="{container_id}" class="jeopardy-container" lang="no" data-config="{cfg_str}"></div>
        <script type="application/json" class="jeopardy-data">{json_str}</script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css">
        <script defer src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js"></script>
        <script defer src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/auto-render.min.js"></script>
        <link rel="stylesheet" href="{rel_prefix}_static/jeopardy/jeopardy.css" />
        <script defer src="{rel_prefix}_static/jeopardy/jeopardy.js"></script>
        """

        return [nodes.raw("", html, format="html")]

    # -------------------- parsing helpers --------------------
    def _parse_board(self) -> Dict[str, Any]:
        teams_opt = self.options.get("teams")
        try:
            teams = max(1, int(str(teams_opt).strip())) if teams_opt is not None else 2
        except Exception:
            teams = 2

        categories: List[Dict[str, Any]] = []
        current_cat: Dict[str, Any] | None = None
        current_tile: Dict[str, Any] | None = None
        current_section: str | None = None  # 'Q' or 'A'
        values_set = set()

        def flush_tile():
            nonlocal current_tile
            if current_cat is not None and current_tile is not None:
                # normalize strings
                for k in ("question", "answer"):
                    if current_tile.get(k) is None:
                        current_tile[k] = ""
                (current_cat.setdefault("tiles", [])).append(current_tile)
            current_tile = None

        for raw in self.content:
            line = self._process_figures(raw)
            if line is None:
                line = raw
            s = line.rstrip("\n")

            # Category header
            m = re.match(r"^\s*Category\s*:\s*(.+?)\s*$", s, flags=re.IGNORECASE)
            if m:
                flush_tile()
                current_cat = {"name": m.group(1).strip(), "tiles": []}
                categories.append(current_cat)
                current_section = None
                continue

            # New tile with just value:
            m = re.match(r"^\s*(\d+)\s*:\s*$", s)
            if m and current_cat is not None:
                flush_tile()
                v = int(m.group(1))
                values_set.add(v)
                current_tile = {"value": v, "question": "", "answer": ""}
                current_section = None
                continue

            # Section Q:/A:
            m = re.match(r"^\s*Q\s*:\s*(.*)$", s, flags=re.IGNORECASE)
            if m and current_tile is not None:
                current_section = "Q"
                current_tile["question"] = (
                    current_tile.get("question") or ""
                ) + m.group(1)
                continue
            m = re.match(r"^\s*A\s*:\s*(.*)$", s, flags=re.IGNORECASE)
            if m and current_tile is not None:
                current_section = "A"
                current_tile["answer"] = (current_tile.get("answer") or "") + m.group(1)
                continue

            # Continuation lines for section
            if current_section == "Q" and current_tile is not None:
                current_tile["question"] = (
                    (current_tile.get("question") or "") + "\n" + s
                )
                continue
            if current_section == "A" and current_tile is not None:
                current_tile["answer"] = (current_tile.get("answer") or "") + "\n" + s
                continue

        flush_tile()

        # Determine values order (ascending: 100, 200, ...)
        values = sorted(values_set)

        # Ensure each category has tiles aligned to values; keep only recognized value tiles
        for cat in categories:
            by_val = {t.get("value"): t for t in (cat.get("tiles") or [])}
            cat["tiles"] = [by_val.get(v) for v in values if v in by_val]

        # Post-process code blocks in questions/answers (same approach as quiz)
        for cat in categories:
            for t in cat.get("tiles") or []:
                for key in ("question", "answer"):
                    s = t.get(key) or ""
                    t[key] = self._process_code_blocks(s)

        return {"teams": teams, "categories": categories, "values": values}

    def _process_figures(self, text):
        """Copy images to _static/figurer/... and rewrite to HTML, like quiz."""
        import shutil
        import json as _json

        # image counter per directive instance
        if not hasattr(self, "_image_counter"):
            self._image_counter = 0

        def _parse_figure_options(alt_text):
            # Support JSON-like {width: 60%, class: adaptive-figure}
            # Also support key=value pairs with or without quotes, inside or outside braces
            opts: Dict[str, Any] = {}
            s = (alt_text or "").strip()

            def parse_pairs(text: str):
                for m in re.finditer(
                    r'(\w+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s}]+))', text
                ):
                    val = m.group(2) or m.group(3) or m.group(4) or ""
                    opts[m.group(1)] = val

            if s.startswith("{") and s.endswith("}"):
                inner = s[1:-1].strip()
                # Try JSON-ish with colon first
                ok = False
                try:
                    js = s
                    js = re.sub(r"(\w+)\s*:", r'"\1":', js)
                    js = re.sub(r':\s*([^",}]+)', r': "\1"', js)
                    opts.update(_json.loads(js))
                    ok = True
                except Exception:
                    ok = False
                if not ok:
                    parse_pairs(inner)
            else:
                parse_pairs(s)
                if not opts and s:
                    opts["alt"] = s
            return opts

        def _build_figure_html(html_img_path, options):
            def _normalize_wh(val: Any) -> str:
                s = str(val).strip()
                # If numeric (int/float) or digits-only string, default to px
                if re.fullmatch(r"\d+(?:\.\d+)?", s):
                    return f"{s}px"
                # Allow common CSS units and percent
                # Remove whitespace before units (e.g. '50 %' -> '50%')
                s = re.sub(r"\s+(?=(px|%|em|rem|vh|vw)$)", "", s)
                if re.search(r"(px|%|em|rem|vh|vw)$", s):
                    return s
                return s

            # Start with default classes; append user-provided classes if any
            user_opts = dict(options or {})
            user_class = user_opts.pop("class", "").strip()
            classes = "jeopardy-image adaptive-figure" + (
                f" {user_class}" if user_class else ""
            )

            alt_text = user_opts.pop("alt", "Figure")
            title = user_opts.pop("title", None)
            width = user_opts.pop("width", None)
            height = user_opts.pop("height", None)
            extra_style = user_opts.pop("style", None)

            styles: List[str] = []
            if width is not None:
                styles.append(f"width: {_normalize_wh(width)};")
            if height is not None:
                styles.append(f"height: {_normalize_wh(height)};")
            if extra_style:
                styles.append(str(extra_style))

            attrs = [
                f'src="{html_img_path}"',
                f'class="{classes}"',
                f'alt="{alt_text}"',
            ]
            if title:
                attrs.append(f'title="{title}"')
            if styles:
                attrs.append(f'style="{' '.join(styles)}"')
            # Preserve any other attributes passed in options
            for k, v in user_opts.items():
                # Avoid duplicating common attributes already handled
                if k not in {
                    "src",
                    "class",
                    "alt",
                    "title",
                    "width",
                    "height",
                    "style",
                }:
                    attrs.append(f'{k}="{v}"')

            img = f"<img {' '.join(attrs)}>"
            return f'<div class="jeopardy-image-container">{img}</div>'

        def replace(m):
            alt_or_opts = m.group(1).strip()
            raw_src = m.group(2)

            self._image_counter += 1

            options = _parse_figure_options(alt_or_opts)

            source_file = self.state.document["source"]
            source_dir = os.path.dirname(source_file)
            app_src_dir = self.env.srcdir

            abs_fig_src = os.path.normpath(os.path.join(source_dir, raw_src))
            if not os.path.exists(abs_fig_src):
                return f'<img src="{raw_src}" class="jeopardy-image adaptive-figure" alt="Figure (missing)">'

            relative_doc_path = os.path.relpath(source_dir, app_src_dir)
            figure_dest_dir = os.path.join(
                app_src_dir, "_static", "figurer", relative_doc_path
            )
            os.makedirs(figure_dest_dir, exist_ok=True)

            rel_path_from_source = os.path.relpath(abs_fig_src, source_dir)
            safe_path = rel_path_from_source.replace(os.sep, "_").replace("/", "_")
            base, ext = os.path.splitext(safe_path)
            fig_filename = f"{self.board_id}_img{self._image_counter}_{base}{ext}"
            fig_dest_path = os.path.join(figure_dest_dir, fig_filename)
            shutil.copy2(abs_fig_src, fig_dest_path)

            depth = os.path.relpath(source_dir, app_src_dir).count(os.sep)
            rel_prefix = "../" * (depth + 1)
            html_img_path = (
                f"{rel_prefix}_static/figurer/{relative_doc_path}/{fig_filename}"
            )
            return _build_figure_html(html_img_path, options)

        return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, text)

    def _process_code_blocks(self, text: str) -> str:
        """Process HTML code blocks to handle escaped newlines (like quiz).

        Looks for <pre><code class="..."></code></pre> and replaces \\n with
        actual newlines so code renders correctly.
        """

        def replace_newlines(match):
            code = match.group(2)  # code content
            # Replace escaped newlines with actual newlines
            code = code.replace("\\n", "\n")
            lang = match.group(1)
            return f'<pre><code class="{lang}">{code}</code></pre>'

        pattern = r'<pre><code class="([\w-]+)">(.*?)</code></pre>'
        return re.sub(pattern, replace_newlines, text, flags=re.DOTALL)


def setup(app):
    app.add_directive("jeopardy", JeopardyDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
