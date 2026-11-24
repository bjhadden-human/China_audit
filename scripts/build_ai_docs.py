"""Split public/index.html into AI-readable Markdown, CSV, code and source files.

Run from the repository root:  python3 scripts/build_ai_docs.py
Uses only the Python standard library.
"""
import base64
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "public" / "index.html"
OUT = ROOT / "public"
SITE = ""  # links in llms.txt are site-relative so they work on any deployment domain


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


class MarkdownConverter(HTMLParser):
    BLOCK = {"p", "h1", "h2", "h3", "h4", "li", "pre", "summary", "header", "article", "section", "details", "div", "ol", "ul", "nav"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.buf = []
        self.stack = []
        self.href = None
        self.table = None
        self.cell = None
        self.list_stack = []
        self.in_pre = False
        self.skip = 0

    def flush(self, prefix=""):
        text = "".join(self.buf)
        self.buf = []
        if self.in_pre:
            return
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            self.out.append(prefix + text + "\n\n")

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "button"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "table":
            self.flush()
            self.table = []
        elif tag == "tr" and self.table is not None:
            self.table.append([])
        elif tag in ("td", "th") and self.table is not None:
            self.cell = []
        elif tag == "pre":
            self.flush()
            self.in_pre = True
            self.buf = []
        elif tag in ("ol", "ul"):
            self.flush()
            self.list_stack.append([tag, 0])
        elif tag == "li":
            self.flush()
        elif tag in self.BLOCK:
            self.flush()
        elif tag == "a":
            self.href = a.get("href")
            self._target().append("[")
        elif tag == "br":
            self._target().append(" ")
        elif tag in ("strong", "b"):
            self._target().append("**")
        elif tag in ("em", "i"):
            self._target().append("*")
        elif tag == "code" and not self.in_pre:
            self._target().append("`")
        self.stack.append(tag)

    def _target(self):
        return self.cell if self.cell is not None else self.buf

    def handle_endtag(self, tag):
        if tag in ("script", "style", "button"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        if tag in ("td", "th") and self.table is not None and self.cell is not None:
            text = re.sub(r"\s+", " ", "".join(self.cell)).strip().replace("|", "\\|")
            self.table[-1].append(text)
            self.cell = None
        elif tag == "table" and self.table is not None:
            rows = [r for r in self.table if r]
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
                lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                self.out.append("\n".join(lines) + "\n\n")
            self.table = None
        elif tag == "pre":
            self.out.append("```text\n" + "".join(self.buf).strip("\n") + "\n```\n\n")
            self.buf = []
            self.in_pre = False
        elif tag in ("h1", "h2", "h3", "h4"):
            self.flush("#" * int(tag[1]) + " ")
        elif tag == "summary":
            self._flush_summary()
        elif tag == "li":
            kind = self.list_stack[-1] if self.list_stack else ["ul", 0]
            kind[1] += 1
            self.flush(f"{kind[1]}. " if kind[0] == "ol" else "- ")
        elif tag in ("ol", "ul"):
            if self.list_stack:
                self.list_stack.pop()
        elif tag in self.BLOCK:
            self.flush()
        elif tag == "a":
            href = self.href or ""
            if href.startswith("#"):
                self._target().append("]")
            else:
                self._target().append(f"]({href})")
            self.href = None
        elif tag in ("strong", "b"):
            self._target().append("**")
        elif tag in ("em", "i"):
            self._target().append("*")
        elif tag == "code" and not self.in_pre:
            self._target().append("`")

    def _flush_summary(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if text:
            self.out.append(f"**{text}**\n\n")

    def handle_data(self, data):
        if self.skip:
            return
        self._target().append(data)

    def markdown(self):
        self.flush()
        md = "".join(self.out)
        md = md.replace("[]", "")
        return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def to_markdown(fragment):
    conv = MarkdownConverter()
    conv.feed(fragment)
    return conv.markdown()


def main():
    html = SRC.read_text(encoding="utf-8")
    open_tag = '<script type="application/json" id="audit-data">'
    start = html.index(open_tag) + len(open_tag)
    data = json.loads(html[start:html.index("</script>", start)])
    body = html[:start - len(open_tag)]

    title = re.search(r"<title>(.*?)</title>", html).group(1)
    header = to_markdown(re.search(r"<header>.*?</header>", body, re.S).group(0))

    report_dir = OUT / "report"
    report_dir.mkdir(parents=True, exist_ok=True)
    sections = list(re.finditer(r'<section id="([^"]+)">(.*?)</section>', body, re.S))
    index = []
    full = [f"# {title}\n\n", header.replace("# ", "## ", 1) if header.startswith("# ") else header]
    for n, m in enumerate(sections, 1):
        md = to_markdown(m.group(2))
        heading = re.search(r"^## (.+)$", md, re.M).group(1)
        name = f"{n:02d}-{m.group(1)}.md"
        (report_dir / name).write_text(md, encoding="utf-8")
        index.append((name, heading, m.group(1)))
        full.append(md + "\n")
    (OUT / "report.md").write_text("".join(full), encoding="utf-8")

    data_dir = OUT / "data"
    data_dir.mkdir(exist_ok=True)
    csv_index = []
    for name, text in data["csv_tables"].items():
        (data_dir / f"{name}.csv").write_text(text, encoding="utf-8")
        csv_index.append((name, len(data["tables"][name]), len(text.encode("utf-8"))))

    source_dir = OUT / "source"
    source_dir.mkdir(exist_ok=True)
    for name, f in data["original_files"].items():
        raw = base64.b64decode(f["base64"])
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == f["sha256"].removeprefix("sha256:"), f"hash mismatch for {name}"
        (source_dir / name).write_bytes(raw)
    pages = [f"# ARPD codebook text (October 2019, v1.0)\n\nPlain-text extraction of `ARPD-Codebook.pdf`, one section per PDF page.\n\n"]
    for i, page in enumerate(data["codebook_text_by_page"], 1):
        pages.append(f"## Page {i}\n\n{page.strip()}\n\n")
    (source_dir / "ARPD-Codebook.md").write_text("".join(pages), encoding="utf-8")

    code_dir = OUT / "code"
    code_dir.mkdir(exist_ok=True)
    (code_dir / "reproduce.py").write_text(data["reproduction_python"], encoding="utf-8")
    spec = data["frozen_bridge_specification"]
    (code_dir / "frozen_bridge_specification.md").write_text(
        "# Frozen China bridge specification\n\n" + (spec if isinstance(spec, str) else json.dumps(spec, indent=2)) + "\n",
        encoding="utf-8",
    )
    (OUT / "manifest.json").write_text(json.dumps(data["manifest"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    conclusion = (report_dir / index[0][0]).read_text(encoding="utf-8")
    summary = next((p for p in conclusion.split("\n\n") if p and not p.startswith(("#", "|"))), "")

    lines = [
        f"# {title}",
        "",
        f"> {summary}",
        "",
        "Self-contained audit of a survival-model estimate of the probability that the CCP loses decisive authoritarian supremacy over China, built on Michael K. Miller's Autocratic Ruling Parties Dataset (ARPD). All text, tables, data and code below are extracted from the original single-file HTML report.",
        "",
        "## Report",
        "",
        f"- [Full report (single file)]({SITE}/report.md)",
    ]
    lines += [f"- [{h}]({SITE}/report/{f})" for f, h, _ in index]
    lines += ["", "## Data (CSV)", ""]
    lines += [f"- [{n}]({SITE}/data/{n}.csv): {rows} rows" for n, rows, _ in csv_index]
    lines += [
        "",
        "## Code",
        "",
        f"- [Reproduction script (Python)]({SITE}/code/reproduce.py)",
        f"- [Frozen China bridge specification]({SITE}/code/frozen_bridge_specification.md)",
        "",
        "## Optional",
        "",
        f"- [ARPD codebook as text]({SITE}/source/ARPD-Codebook.md)",
        f"- [Original ARPD spreadsheet]({SITE}/source/AutocraticRulingPartiesDataset.xlsx)",
        f"- [Original ARPD codebook PDF]({SITE}/source/ARPD-Codebook.pdf)",
        f"- [Manifest with SHA-256 hashes]({SITE}/manifest.json)",
        f"- [Original interactive HTML report]({SITE}/)",
        "",
    ]
    (OUT / "llms.txt").write_text("\n".join(lines), encoding="utf-8")

    readme = [
        f"# {title}",
        "",
        summary,
        "",
        "This repository publishes one self-contained HTML audit report in two forms:",
        "",
        "1. **For people:** the original interactive report at [`public/index.html`](public/index.html), served unchanged as the website.",
        "2. **For AI assistants and search:** the same content split into Markdown, CSV and code files that are small enough to read directly.",
        "",
        "## Where to start",
        "",
        "- [`public/llms.txt`](public/llms.txt): machine-readable index (also at `/llms.txt` on the website).",
        "- [`public/report.md`](public/report.md): the full report text as one Markdown file.",
        "- [`public/report/`](public/report): the report split into one file per section.",
        "",
        "## Report sections",
        "",
    ]
    readme += [f"{i}. [{h}](public/report/{f})" for i, (f, h, _) in enumerate(index, 1)]
    readme += ["", "## Data tables", "", "| Table | Rows | CSV size |", "|---|---:|---:|"]
    readme += [f"| [`{n}`](public/data/{n}.csv) | {rows:,} | {size / 1024:,.0f} KB |" for n, rows, size in csv_index]
    readme += [
        "",
        "## Code and sources",
        "",
        "- [`public/code/reproduce.py`](public/code/reproduce.py): Python reproduction of the estimates, embedded in the original report.",
        "- [`public/code/frozen_bridge_specification.md`](public/code/frozen_bridge_specification.md): specification of the frozen China bridge.",
        "- [`public/source/`](public/source): the original ARPD spreadsheet and codebook PDF (verified against the SHA-256 hashes in [`public/manifest.json`](public/manifest.json)), plus a page-by-page text version of the codebook.",
        "",
        "## Regenerating",
        "",
        "Everything except `public/index.html` is generated from it:",
        "",
        "```bash",
        "python3 scripts/build_ai_docs.py",
        "```",
        "",
        "## Source dataset",
        "",
        "The Autocratic Ruling Parties Dataset (ARPD) is by Michael K. Miller. See the codebook for citation guidance: Miller, \"The Autocratic Ruling Parties Dataset: Origins, Durability, and Death,\" *Journal of Conflict Resolution*.",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(readme), encoding="utf-8")
    print(f"sections={len(index)} csv={len(csv_index)} files={len(data['original_files'])}")


if __name__ == "__main__":
    main()
