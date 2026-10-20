"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from entry import _plain, schema  # noqa: E402

# Inline markup removed without leaving a space, so that "p<sub>1</sub>" reads "p1".
INLINE = (r"</?(italic|bold|sup|sub|sc|underline|xref|ext-link|named-content|inline-formula|mml:[a-z]+"
          r"|i|b|em|strong|span|a)\b[^>]*>")
SAME = {"−": "-", "–": "-", "—": "-", "‐": "-", "‑": "-", "‘": "'", "’": "'", "“": '"', "”": '"',
        " ": " ", " ": " ", " ": " "}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", html.unescape(s))
    for a, b in SAME.items():
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def flattenings(raw: str) -> list[str]:
    """The text with inline tags removed, with every tag as a space, and both without spaces."""
    tight = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", re.sub(INLINE, "", raw, flags=re.I)))
    loose = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", raw))
    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]


def quote_found(quote: str, texts: list[str]) -> bool:
    fragments = [f for f in (norm(x).strip(" .,;") for x in quote.split("...")) if f]
    for text in texts:
        frags = fragments if " " in text else [f.replace(" ", "") for f in fragments]
        pos = 0
        for f in frags:
            i = text.find(f, pos)
            if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
    return {f.lower() for f in out}


def check(claims_path: Path, paper_paths: list[Path]) -> int:
    doc = yaml.safe_load(claims_path.read_text())
    texts = [t for p in paper_paths for t in flattenings(p.read_text(encoding="utf-8", errors="replace"))]
    problems = 0
    for err in schema("claims").iter_errors(_plain(doc)):
        print("SCHEMA", "/".join(str(x) for x in err.path) or "(top level)", err.message)
        problems += 1
    quotes = values = 0
    for c in doc.get("claims", []):
        if c.get("quote"):
            quotes += 1
            if not quote_found(c["quote"], texts):
                print("QUOTE NOT FOUND", c["id"])
                problems += 1
        for s in c.get("statistics", []):
            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
                if v is None:
                    continue
                values += 1
                if not any(f in t for f in printed_forms(v) for t in texts):
                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
                    problems += 1
    print(f"{claims_path}: {len(doc.get('claims', []))} claims, {quotes} quotes, "
          f"{values} statistical values, {problems} problems")
    return problems


def main() -> int:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    return 1 if check(Path(sys.argv[1]), [Path(p) for p in sys.argv[2:]]) else 0


if __name__ == "__main__":
    sys.exit(main())
