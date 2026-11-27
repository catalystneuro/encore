"""Build targets/zenodo.json, the registry's list of Zenodo datasets, from their record ids.

    python tools/build_zenodo_targets.py 3924718 10.5281/zenodo.17624449 https://zenodo.org/records/17794764=10.1/... \
        [--out targets/zenodo.json]

Zenodo holds every GitHub release archived through its integration, posters and slides as well as data, so the list
is chosen, not crawled. Give each dataset as its record id, its DOI (10.5281/zenodo.<id>) or its page
(zenodo.org/records/<id>), optionally with =<paper DOI> when the record does not link its paper itself. A concept id
or concept DOI names the whole deposit; the builder pins its latest version.

For each, the builder reads Zenodo's public REST API (no account needed for an open record): the title,
description, license, keywords and resource type; every file, with its key, size and MD5; the deposit's concept id
and the ids of all its versions; and the papers. Each version of a deposit is a record of its own whose files
cannot change, so the record id pins it, and published_version is the record id. The papers are the DOI given and
the related identifiers marked isSupplementTo, isDescribedBy, isPublishedIn, isCitedBy, isReferencedBy or
isDocumentedBy that are not GitHub
repositories or other Zenodo records, titled from Crossref; GitHub repositories go under code.

A dataset is named by its record id (ZENODO:3924718, folder zenodo-3924718). Reading the files needs no account
(docs/archives.md, "Zenodo").
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
API = "https://zenodo.org/api"
PAPER_RELATIONS = {"issupplementto", "isdescribedby", "iscitedby", "isreferencedby", "isdocumentedby",
                   "ispublishedin"}
# Zenodo refuses an anonymous listing with more than 25 items to a page (400 Bad Request).
PAGE_SIZE = 25


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def title_of(doi: str) -> tuple[str, bool]:
    """The work's title, and whether Crossref calls it a preprint; ("", False) for a DOI Crossref does not hold."""
    try:
        work = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]
    except Exception:
        return "", False
    return " ".join((work.get("title") or [""])[0].split()), work.get("type") == "posted-content"


def clean_doi(text: str | None) -> str:
    text = (text or "").strip().lower()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", text)


def parse(spec: str) -> tuple[str, str]:
    """A record id and a paper DOI or "", from one argument."""
    found_paper = re.fullmatch(r"(.+?)=((?:https?://(?:dx\.)?doi\.org/)?10\.\S+)", spec.strip(), re.I)
    item, paper = found_paper.groups() if found_paper else (spec.strip(), "")
    item = item.strip().rstrip("/")
    found = (re.fullmatch(r"(?:zenodo:)?([0-9]+)", item, re.I)
             or re.search(r"10\.5281/zenodo\.([0-9]+)$", item, re.I)
             or re.search(r"zenodo\.org/(?:records?|deposit)/([0-9]+)(?:[/?#]|$)", item, re.I))
    if not found:
        raise SystemExit(f"error: not a Zenodo record id, DOI or page: {item!r}")
    return found.group(1), clean_doi(paper)


def kind_of(name: str) -> str:
    name = name.lower()
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    return {"xlsx": "Excel", "xls": "Excel", "csv": "CSV", "txt": "text", "md": "Markdown", "zip": "zip",
            "tsv": "TSV", "pdf": "PDF", "r": "R script", "py": "Python", "m": "MATLAB script", "mat": "MATLAB",
            "h5": "HDF5", "hdf5": "HDF5", "nwb": "Neurodata Without Borders (NWB)", "abf": "ABF", "json": "JSON",
            "npy": "NumPy", "npz": "NumPy", "gz": "gzip", "tar": "tar"}.get(ext, ext or "no extension")


def md5_of(checksum: str | None) -> str | None:
    algorithm, _, value = (checksum or "").partition(":")
    return value.lower() if algorithm.lower() == "md5" and len(value) == 32 else None


def resource_type(meta: dict) -> str:
    rt = meta.get("resource_type") or {}
    return rt.get("type") or rt.get("id") or rt.get("title") or ""


def version_ids(record: dict) -> list[str]:
    """The ids of every version of the record's deposit, oldest first, following links.next from page to page.
    (sort=version gives the newest first.)"""
    ids, url = [], f"{API}/records/{record['id']}/versions?size={PAGE_SIZE}&sort=oldest"
    try:
        while url:
            page = get(url)
            ids += [str(h["id"]) for h in page["hits"]["hits"]]
            url = (page.get("links") or {}).get("next")
    except Exception as err:
        print(f"warning: ZENODO:{record['id']}: could not list its versions ({err}); listing it alone",
              file=sys.stderr)
        return [str(record["id"])]
    return ids or [str(record["id"])]


def papers_of(paper: str, meta: dict) -> tuple[list[dict], list[str]]:
    """The papers (the DOI given first) and the code a record's related identifiers name."""
    papers, code = [], []
    dois = [paper] if paper else []
    for r in meta.get("related_identifiers") or []:
        ident, relation = (r.get("identifier") or "").strip(), (r.get("relation") or "").lower()
        if "github.com" in ident.lower():
            code.append(ident)
        elif relation in PAPER_RELATIONS and (r.get("scheme") == "doi" or ident.lower().startswith("10.")) \
                and not clean_doi(ident).startswith("10.5281/zenodo."):
            dois.append(clean_doi(ident))
    for d in dict.fromkeys(dois):
        title, preprint = title_of(d)
        relation = "given" if d == paper else next(
            (r["relation"] for r in meta.get("related_identifiers") or [] if clean_doi(r.get("identifier")) == d), "")
        papers.append({"doi": d, "title": title, "relation": relation,
                       "resource_type": "Preprint" if preprint else "JournalArticle", "preprint": preprint})
    return papers, code


def target(spec: str) -> dict:
    id_, paper = parse(spec)
    record = get(f"{API}/records/{id_}")
    if str(record.get("id")) != id_:   # a concept id answers with its latest version
        print(f"note: ZENODO:{id_} is a concept id; pinning its latest version, {record['id']}", file=sys.stderr)
    meta = record["metadata"]
    files = record.get("files") or []
    papers, code = papers_of(paper, meta)
    return {
        "id": str(record["id"]),
        "name": re.sub(r"<[^>]+>", "", meta["title"]).strip(),
        "url": f"https://zenodo.org/records/{record['id']}",
        "doi": (record.get("doi") or f"10.5281/zenodo.{record['id']}").lower(),
        "published_version": str(record["id"]),
        "concept_id": str(record.get("conceptrecid") or ""),
        "concept_doi": (record.get("conceptdoi") or "").lower(),
        "version_ids": version_ids(record),
        "version": meta.get("version"),
        "resource_type": resource_type(meta),
        "access_right": meta.get("access_right"),
        "published": meta.get("publication_date"),
        "license": (meta.get("license") or {}).get("id"),
        "description": re.sub(r"<[^>]+>", "", meta.get("description") or "").strip(),
        "asset_count": len(files),
        "size_gb": round(sum(f.get("size", 0) for f in files) / 1e9, 4),
        "data_standards": sorted({kind_of(f["key"]) for f in files} - {"Markdown"}),
        "files": [{"path": f["key"], "size": f.get("size"), "file_id": f.get("id"), "md5": md5_of(f.get("checksum"))}
                  for f in files],
        "readme": any(f["key"].lower().startswith("readme") for f in files),
        "code": code,
        "species": [],
        "approaches": [],
        "keywords": meta.get("keywords", []),
        "papers": papers,
        "catalystneuro": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("items", nargs="+", help="<record id or DOI or URL>[=<paper DOI>]")
    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "zenodo.json")
    parser.add_argument("--note", default="Zenodo records chosen by hand to test the pipeline on Zenodo.")
    args = parser.parse_args()
    targets = [target(s) for s in args.items]
    for t in targets:
        if t["resource_type"] != "dataset":
            print(f"warning: ZENODO:{t['id']} is a {t['resource_type'] or 'record of no type'}, not a dataset",
                  file=sys.stderr)
        if t["access_right"] not in (None, "open"):
            print(f"warning: ZENODO:{t['id']} is {t['access_right']}, so agents cannot read it", file=sys.stderr)
        if not t["papers"]:
            print(f"warning: ZENODO:{t['id']} names no paper; give one as <id>=<paper DOI>", file=sys.stderr)
    out = {"schema_version": 1, "archive": "zenodo",
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": f"{API}, chosen by hand (tools/build_zenodo_targets.py)", "note": args.note,
           "counts": {"with_a_paper": sum(1 for t in targets if t["papers"])}, "targets": targets}
    args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(targets)} targets to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
