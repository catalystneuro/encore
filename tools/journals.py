"""Write papers/journals.yaml: the journal of every target's paper, from Crossref, for the site's journal filter.

    python tools/journals.py            # adds the papers not yet in the file; keeps the rest

The site reads the file (tools/build_site.py); it does not query Crossref itself. A preprint is recorded as
"Preprint" (its server, such as bioRxiv, as `server`).
"""
from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402

VERSION = re.compile(r"^(10\.1101/[\d.]+)v\d+$")


def key(doi: str) -> str:
    """A DOI as the file keys it: lower case, without a bioRxiv version suffix (10.1101/...v1), which Crossref
    does not know."""
    doi = doi.strip().lower()
    m = VERSION.match(doi)
    return m.group(1) if m else doi

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers" / "journals.yaml"


def journal_of(doi: str) -> dict | None:
    req = urllib.request.Request("https://api.crossref.org/works/" + urllib.parse.quote(doi),
                                 headers={"User-Agent": "encore-registry (https://encorescience.org)"})
    for attempt in range(4):
        try:
            m = json.load(urllib.request.urlopen(req, timeout=60))["message"]
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(5 * 3 ** attempt)
        except Exception:
            time.sleep(5)
    else:
        return None
    if m.get("type") == "posted-content":
        return {"journal": "Preprint", "server": (m.get("institution") or [{}])[0].get("name") or (m.get("publisher") or "")}
    names = m.get("container-title") or []
    return {"journal": clean(names[0])} if names else None


# Crossref's names as journals print them: entities decoded, and a few casings fixed.
CASING = {"eneuro": "eNeuro", "elife": "eLife"}


def clean(name: str) -> str:
    name = " ".join(html.unescape(name).split())
    return CASING.get(name.lower(), name)


def main() -> int:
    known = yaml.safe_load(OUT.read_text())["papers"] if OUT.exists() else {}
    for v in known.values():
        if v.get("journal") and v["journal"] != "Preprint":
            v["journal"] = clean(v["journal"])
    # The papers the site shows (after papers/triage.yaml and the paper matches), and every paper the targets name.
    import build_site
    shown = {t.get("paper") for t in build_site.collect()["targets"]}
    named = {p.get("doi") for t in datasets.targets() for p in (t.get("papers") or [])}
    known = {key(k): v for k, v in known.items()}
    dois = sorted({key(d) for d in shown | named if d})
    todo = [d for d in dois if d not in known]
    print(f"{len(dois)} papers, {len(todo)} to look up", flush=True)
    for i, doi in enumerate(todo, 1):
        j = journal_of(doi)
        if j:
            known[doi] = j
        time.sleep(1)
        if i % 50 == 0:
            print(f"  {i}/{len(todo)}", flush=True)
    OUT.write_text("# Written by tools/journals.py from Crossref; the journal of each target's paper, for the site's filter.\n"
                   + yaml.safe_dump({"schema_version": 1, "papers": dict(sorted(known.items()))}, sort_keys=False, allow_unicode=True))
    print(f"wrote {OUT.relative_to(ROOT)}: {len(known)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
