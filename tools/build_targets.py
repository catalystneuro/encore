"""Build the queue of reproduction targets from the DANDI Archive.

A target is a public, non-empty dandiset that names at least one paper in its
metadata (`relatedResource`). For each one this records the dandiset, its
size and data standards, and the papers, so an agent can pick one up and
try to reproduce the papers' key findings from the data. It also records any
sign that CatalystNeuro converted the dandiset (`catalystneuro`): a related
resource in a catalystneuro GitHub repository, or a contributor affiliated
with CatalystNeuro or with a catalystneuro.com address. Problems an attempt
finds in those can be fixed in our own conversion code.

The queue is regenerated from the archive on each run. Anything that records
work done on a target (who claimed it, what was reproduced) lives with the
attempts, not here, so regenerating never loses state.

Usage:
    python tools/build_targets.py [--output targets/dandisets.json] [--limit N]

Uses only the standard library and the public DANDI API (no token).
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

API = "https://api.dandiarchive.org/api"
DOI = re.compile(r"10\.\d{4,9}/\S+", re.I)

# relatedResource types that are not papers even when they carry a DOI.
NOT_A_PAPER = {"dcite:Dataset", "dcite:Software", "dcite:ComputationalNotebook",
               "dcite:Workflow", "dcite:Model", "dcite:Image", "dcite:Audiovisual"}
PREPRINT_HOSTS = ("10.1101/", "10.48550/", "10.21203/", "10.31234/", "10.20944/")
# DOIs minted by data and file repositories: a dataset, a resource table or a
# code archive, not a paper, unless the metadata says it is an article.
REPOSITORY_DOIS = ("10.5281/", "10.6084/", "10.17605/", "10.48324/", "10.5061/",
                   "10.7910/", "10.12751/", "10.60533/", "10.80507/")
ARTICLE_TYPES = {"dcite:JournalArticle", "dcite:Preprint", "dcite:DataPaper",
                 "dcite:ConferencePaper", "dcite:ConferenceProceeding"}


def get(url: str) -> dict:
    last = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
    raise RuntimeError(f"{url}: {last}")


def list_dandisets() -> list[dict]:
    """Every public dandiset that holds at least one asset."""
    out, url = [], f"{API}/dandisets/?page_size=200&empty=false&embargoed=false&order=id"
    while url:
        page = get(url)
        out.extend(page["results"])
        url = page.get("next")
    return out


def doi_of(resource: dict) -> str | None:
    for field in ("identifier", "url"):
        m = DOI.search(resource.get(field) or "")
        if m:
            return m.group(0).rstrip(".,;)").lower()
    return None


def papers(metadata: dict) -> list[dict]:
    """The papers a dandiset's metadata relates it to, one per DOI."""
    seen, out = set(), []
    for r in metadata.get("relatedResource") or []:
        doi = doi_of(r)
        if not doi or doi in seen or r.get("resourceType") in NOT_A_PAPER:
            continue
        if doi.startswith(REPOSITORY_DOIS) and r.get("resourceType") not in ARTICLE_TYPES:
            continue
        seen.add(doi)
        out.append({
            "doi": doi,
            "title": r.get("name"),
            "relation": (r.get("relation") or "").removeprefix("dcite:") or None,
            "resource_type": (r.get("resourceType") or "").removeprefix("dcite:") or None,
            "preprint": doi.startswith(PREPRINT_HOSTS) or r.get("resourceType") == "dcite:Preprint",
        })
    return out


def catalystneuro(metadata: dict) -> list[str]:
    """Signs in the metadata that CatalystNeuro converted the dandiset, one line each."""
    signs = []
    for r in metadata.get("relatedResource") or []:
        url = r.get("url") or ""
        if "github.com/catalystneuro/" in url.lower():
            signs.append(f"conversion code at {url}")
    for c in metadata.get("contributor") or []:
        affiliations = [a.get("name") or "" for a in c.get("affiliation") or []]
        if (any("catalystneuro" in a.lower().replace(" ", "") for a in affiliations)
                or (c.get("email") or "").lower().endswith("@catalystneuro.com")
                or "catalystneuro.com" in (c.get("url") or "").lower()):
            signs.append(f"contributor {c.get('name')} of CatalystNeuro")
    return signs


def target(summary: dict) -> dict | None:
    dandiset_id = summary["identifier"]
    metadata = get(f"{API}/dandisets/{dandiset_id}/versions/draft/")
    found = papers(metadata)
    draft = summary.get("draft_version") or {}
    published = summary.get("most_recent_published_version") or {}
    assets = metadata.get("assetsSummary") or {}
    return {
        "dandiset": dandiset_id,
        "name": draft.get("name") or metadata.get("name"),
        "published_version": published.get("version"),
        "asset_count": draft.get("asset_count"),
        "size_gb": round((draft.get("size") or 0) / 1e9, 2),
        "data_standards": [s.get("name") for s in assets.get("dataStandard") or []],
        "species": [s.get("name") for s in assets.get("species") or []],
        "approaches": [s.get("name") for s in assets.get("approach") or []],
        "papers": found,
        "catalystneuro": catalystneuro(metadata),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, default=Path("targets/dandisets.json"))
    parser.add_argument("--limit", type=int, help="only the first N dandisets (for testing)")
    args = parser.parse_args()

    dandisets = list_dandisets()
    if args.limit:
        dandisets = dandisets[:args.limit]
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(target, dandisets))

    with_paper = [t for t in results if t["papers"]]
    out = {
        "schema_version": 1,
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "source": API,
        "counts": {
            "public_dandisets": len(results),
            "with_a_paper": len(with_paper),
            "with_a_published_version": sum(1 for t in with_paper if t["published_version"]),
            "papers": len({p["doi"] for t in with_paper for p in t["papers"]}),
            "converted_by_catalystneuro": sum(1 for t in with_paper if t["catalystneuro"]),
        },
        "targets": with_paper,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out["counts"], indent=1))
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
