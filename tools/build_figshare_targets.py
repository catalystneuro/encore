"""Build targets/figshare.json, the registry's list of Figshare datasets, from their article ids.

    python tools/build_figshare_targets.py 24949470=10.1038/s41597-024-03777-0 26877211 ... [--out targets/figshare.json]

Figshare holds millions of items, most of them figures and journals' supplementary tables, so the list is chosen,
not crawled. Give each dataset as its article id, a Figshare DOI (10.6084/m9.figshare.<id>[.v<n>]) or a page URL
(including an institutional portal's, *.figshare.com), optionally with .v<n> to pin a version other than the
latest and with =<paper DOI> when the item does not link its paper itself. For each, the builder reads Figshare's
public API v2 (no account needed), pins the version by its number and DOI, and lists its files with their sizes,
ids and MD5 digests. The papers are the DOI given, the item's related materials marked IsSupplementTo,
IsDocumentedBy, IsDescribedBy or IsReferencedBy, and its resource DOI, titled from Crossref. It also records what
an agent will need to know before reading the data: whether the item has a README, which formats it holds, and
whether it is a dataset at all (Figshare's item type).

A dataset is named by its article id (FIGSHARE:24949470, folder figshare-24949470). Reading the files needs no
account (docs/archives.md, "Figshare").
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.figshare.com/v2"
PAPER_RELATIONS = {"IsSupplementTo", "IsDocumentedBy", "IsDescribedBy", "IsReferencedBy"}


def get(url: str) -> dict | list:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def title_of(doi: str) -> str:
    try:
        return " ".join(get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]["title"][0].split())
    except Exception:   # a DOI Crossref does not hold (a DataCite preprint, say)
        return ""


def parse(spec: str) -> tuple[str, int | None, str]:
    """An article id, a version number or None for the latest, and a paper DOI or "", from one argument."""
    item, _, paper = spec.partition("=")
    item = item.strip().rstrip("/")
    found = (re.fullmatch(r"([0-9]+)(?:\.v([0-9]+))?", item) or re.search(r"figshare\.([0-9]+)(?:\.v([0-9]+))?$", item)
             or re.search(r"/([0-9]{5,})(?:/([0-9]+))?$", item))
    if not found:
        raise SystemExit(f"error: not a Figshare item: {item!r}")
    return found.group(1), int(found.group(2)) if found.group(2) else None, \
        paper.strip().lower().removeprefix("https://doi.org/")


def kind_of(name: str) -> str:
    name = name.lower()
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    return {"xlsx": "Excel", "xls": "Excel", "csv": "CSV", "txt": "text", "md": "Markdown", "zip": "zip",
            "tsv": "TSV", "rds": "RDS", "rdata": "RData", "pdf": "PDF", "r": "R script", "py": "Python",
            "mat": "MATLAB", "h5": "HDF5", "nc": "NetCDF", "json": "JSON", "gpkg": "GeoPackage"}.get(ext, ext or "no extension")


def target(spec: str) -> dict:
    id_, version, paper = parse(spec)
    latest = get(f"{API}/articles/{id_}")
    version = version or latest["version"]
    item = latest if version == latest["version"] else get(f"{API}/articles/{id_}/versions/{version}")
    files = item["files"]
    related = [r for r in item.get("related_materials", []) if r.get("identifier_type") == "DOI"]
    dois = ([paper] if paper else []) + [r["identifier"].lower() for r in related if r["relation"] in PAPER_RELATIONS]
    dois += [item["resource_doi"].lower()] if item.get("resource_doi") else []
    papers = [{"doi": d, "title": title_of(d), "relation": "given" if d == paper else
               next((r["relation"] for r in related if r["identifier"].lower() == d), "resource_doi"),
               "resource_type": "JournalArticle", "preprint": False} for d in dict.fromkeys(dois)]
    return {
        "id": id_,
        "name": re.sub(r"<[^>]+>", "", item["title"]).strip(),
        "url": item["url_public_html"],
        "doi": item["doi"].lower(),
        "published_version": str(version),
        "versions": len(get(f"{API}/articles/{id_}/versions")),
        "item_type": item["defined_type_name"],
        "published": item["published_date"][:10],
        "license": item["license"]["url"],
        "asset_count": len(files),
        "size_gb": round(sum(f["size"] for f in files) / 1e9, 4),
        "data_standards": sorted({kind_of(f["name"]) for f in files} - {"Markdown"}),
        "files": [{"path": f["name"], "size": f["size"], "file_id": f["id"], "md5": f.get("computed_md5") or None}
                  for f in files],
        "readme": any(f["name"].lower().startswith("readme") for f in files),
        "code": [r["link"] for r in item.get("related_materials", []) if re.search(r"github\.com|zenodo", r["link"])],
        "species": [],
        "approaches": [],
        "keywords": item.get("tags", []),
        "categories": [c["title"] for c in item.get("categories", [])],
        "papers": papers,
        "catalystneuro": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("items", nargs="+", help="<article id or DOI or URL>[.v<n>][=<paper DOI>]")
    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "figshare.json")
    parser.add_argument("--note", default="Scientific Data deposits outside neuroscience and ecology, chosen by hand "
                                         "to test the pipeline on a general-purpose repository.")
    args = parser.parse_args()
    targets = [target(s) for s in args.items]
    for t in targets:
        if t["item_type"] != "dataset":
            print(f"warning: FIGSHARE:{t['id']} is a {t['item_type']}, not a dataset", file=sys.stderr)
    out = {"schema_version": 1, "archive": "figshare",
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": f"{API}, chosen by hand (tools/build_figshare_targets.py)", "note": args.note,
           "counts": {"with_a_paper": sum(1 for t in targets if t["papers"])}, "targets": targets}
    args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(targets)} targets to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
