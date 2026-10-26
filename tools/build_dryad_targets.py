"""Build targets/dryad.json, the registry's list of Dryad datasets, from their DOIs.

    python tools/build_dryad_targets.py 10.5061/dryad.bvq83bkk9 ... [--out targets/dryad.json]

Dryad has thousands of datasets with a linked article, so the list is chosen, not crawled: give the DOIs. For each,
the builder reads Dryad's public API v2 (no account needed for metadata), pins the latest version by its version id,
and lists its files with their sizes, types and SHA-256 digests. The papers are the dataset's related works marked
`primary_article` (and `preprint`), titled from Crossref. It also records what an agent will need to know before
reading the data: whether the dataset has a README, which file formats it holds, and the code it links to.

A dataset is named by its DOI's suffix without the "dryad." prefix (10.5061/dryad.bvq83bkk9 is DRYAD:bvq83bkk9,
folder dryad-bvq83bkk9); Dryad DOIs ignore case. Reading the files needs an API token (docs/archives.md, "Dryad").
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://datadryad.org/api/v2"


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def title_of(doi: str) -> str:
    try:
        return " ".join(get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]["title"][0].split())
    except Exception:   # a DOI Crossref does not hold (a DataCite preprint, say)
        return ""


def id_of(doi: str) -> str:
    suffix = doi.split("/", 1)[1].lower()
    return suffix.removeprefix("dryad.")


def kind_of(f: dict) -> str:
    name = f["path"].lower()
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    return {"xlsx": "Excel", "xls": "Excel", "csv": "CSV", "txt": "text", "md": "Markdown", "zip": "zip",
            "tsv": "TSV", "rds": "RDS", "rdata": "RData", "nex": "NEXUS", "tre": "Newick", "pdf": "PDF",
            "r": "R script"}.get(ext, ext or "no extension")


def target(doi: str) -> dict:
    doi = doi.lower().removeprefix("doi:").removeprefix("https://doi.org/")
    ds = get(f"{API}/datasets/{urllib.parse.quote('doi:' + doi, safe='')}")
    version_href = ds["_links"]["stash:version"]["href"]          # /api/v2/versions/<id>, the latest published
    version_id = version_href.rsplit("/", 1)[1]
    files = get(f"https://datadryad.org{version_href}/files?per_page=100")["_embedded"]["stash:files"]
    related = ds.get("relatedWorks", [])
    papers = [{"doi": w["identifier"].removeprefix("https://doi.org/").lower(),
               "title": title_of(w["identifier"].removeprefix("https://doi.org/")),
               "relation": w["relationship"], "resource_type": "JournalArticle" if w["relationship"] ==
               "primary_article" else "Preprint", "preprint": w["relationship"] == "preprint"}
              for w in related if w["relationship"] in ("primary_article", "preprint")]
    return {
        "id": id_of(doi),
        "name": ds["title"].removeprefix("Data from: ").strip(),
        "url": f"https://datadryad.org/dataset/doi:{doi}",
        "doi": doi,
        "published_version": version_id,
        "version_number": ds.get("versionNumber"),
        "published": ds.get("publicationDate"),
        "license": ds.get("license"),
        "asset_count": len(files),
        "size_gb": round((ds.get("storageSize") or 0) / 1e9, 4),
        "data_standards": sorted({kind_of(f) for f in files} - {"Markdown"}),
        "files": [{"path": f["path"], "size": f["size"], "file_id": int(f["_links"]["self"]["href"].rsplit("/", 1)[1]),
                   "sha256": f.get("digest") if f.get("digestType") == "sha-256" else None} for f in files],
        "readme": any(f["path"].lower().startswith("readme") for f in files),
        "code": [w["identifier"] for w in related if w["relationship"] == "software"],
        "species": [],
        "approaches": [],
        "keywords": ds.get("keywords", []),
        "papers": papers,
        "catalystneuro": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("dois", nargs="+")
    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "dryad.json")
    parser.add_argument("--note", default="Datasets outside neuroscience, chosen by hand to test the pipeline on "
                                         "a general-purpose repository.")
    args = parser.parse_args()
    targets = [target(d) for d in args.dois]
    out = {"schema_version": 1, "archive": "dryad",
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": f"{API}, chosen by hand (tools/build_dryad_targets.py)", "note": args.note,
           "counts": {"with_a_paper": sum(1 for t in targets if t["papers"])}, "targets": targets}
    args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(targets)} targets to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
