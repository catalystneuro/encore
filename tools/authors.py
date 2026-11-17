"""Write papers/authors.yaml: the authors of every paper the registry lists, in order, with their ORCID iDs, from
OpenAlex, for the paper pages' author lists and the author pages (tools/build_site.py).

    python tools/authors.py            # adds the papers not yet in the file; keeps the rest
    python tools/authors.py --refresh  # looks every paper up again

The papers are those listed for datasets (papers/datasets/). OpenAlex links authors to their ORCID iDs far more
often than Crossref does (84% of authors against 21%, on a sample of 25 papers on 2026-11-11); an author OpenAlex
gives no ORCID for is listed by name and has no author page. The site reads the file; it does not query OpenAlex.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paper_records  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers" / "authors.yaml"
ORCID = re.compile(r"(\d{4}-\d{4}-\d{4}-\d{3}[\dX])$")


def key(doi: str) -> str:
    """A DOI as the file keys it: lower case, without a bioRxiv version suffix (10.1101/...v1)."""
    doi = doi.strip().lower()
    m = re.match(r"^(10\.1101/[\d.]+)v\d+$", doi)
    return m.group(1) if m else doi


def authors_of(doi: str) -> list[dict] | None:
    """The paper's authors in order: name, ORCID iD (or none) and OpenAlex author id. None when OpenAlex does not
    know the DOI."""
    req = urllib.request.Request("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi, safe="/"),
                                 headers={"User-Agent": "encore-registry (https://encorescience.org)"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                work = json.load(r)
            break
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            time.sleep(5 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    else:
        return None
    out = []
    for a in work.get("authorships") or []:
        who = a.get("author") or {}
        orcid = ORCID.search(who.get("orcid") or "")
        out.append({"name": " ".join((who.get("display_name") or a.get("raw_author_name") or "").split()),
                    "orcid": orcid.group(1) if orcid else None,
                    "openalex": (who.get("id") or "").rsplit("/", 1)[-1] or None})
    return once([a for a in out if a["name"]])


def once(authors: list[dict]) -> list[dict]:
    """The list with each person once: OpenAlex lists an author twice on some papers (a consortium's members, also
    named in the byline). A second entry with an ORCID iD already seen is dropped."""
    seen, out = set(), []
    for a in authors:
        if a["orcid"] and a["orcid"] in seen:
            continue
        seen.add(a["orcid"])
        out.append(a)
    return out


def main() -> int:
    refresh = "--refresh" in sys.argv[1:]
    known = (yaml.safe_load(OUT.read_text()) or {}).get("papers", {}) if OUT.exists() and not refresh else {}
    dois = sorted({key(paper_records.doi_of(k)) for k in paper_records.listed()})
    todo = [d for d in dois if d not in known]
    print(f"{len(dois)} papers, {len(todo)} to look up", flush=True)
    for i, doi in enumerate(todo, 1):
        found = authors_of(doi)
        if found is not None:
            known[doi] = found
        time.sleep(0.2)
        if i % 50 == 0:
            print(f"  {i}/{len(todo)}", flush=True)
    known = {doi: once(found) for doi, found in known.items()}
    OUT.write_text("# Written by tools/authors.py from OpenAlex: each paper's authors in order, with their ORCID iDs.\n"
                   + yaml.safe_dump({"schema_version": 1, "papers": dict(sorted(known.items()))}, sort_keys=False,
                                    allow_unicode=True, width=120))
    n = sum(len(v) for v in known.values())
    with_orcid = sum(1 for v in known.values() for a in v if a["orcid"])
    print(f"wrote {OUT.relative_to(ROOT)}: {len(known)} papers, {n} authors, {with_orcid} with an ORCID iD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
