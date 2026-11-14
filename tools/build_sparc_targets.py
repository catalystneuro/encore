"""Build targets/sparc.json, the registry's list of SPARC datasets, from their ids.

    python tools/build_sparc_targets.py 206 60:5 212=10.1113/jp278016 ... [--out targets/sparc.json]

SPARC's datasets are many models and tools as well as experiments, so the list is chosen, not crawled. Give each
dataset as its id, a SPARC DOI (10.26275/...) or a page URL (sparc.science/datasets/<id>), optionally with :<n> to
pin a version other than the latest and with =<paper DOI> when the dataset does not link its paper itself. For each,
the builder reads Pennsieve Discover's public API (no account needed), pins the version by its number and DOI, and
reads the version's manifest.json from the public S3 bucket, which gives every file's path, size, S3 object version
and SHA-256. The papers are the DOI given and the dataset's related publications marked IsDescribedBy,
IsReferencedBy, IsSupplementTo or IsDocumentedBy, leaving out SPARC's own DOIs and protocols, titled from Crossref,
with their PubMed Central ids. It also records what an agent will need before reading the data: whether the
dataset has a README, which SPARC Data Structure folders and sheets it has, and which formats it holds.

A dataset is named by its id (SPARC:206, folder sparc-206). Reading the files needs no account (docs/archives.md,
"SPARC").
"""

from __future__ import annotations

import argparse
import base64
import datetime
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.pennsieve.io/discover"
PAPER_RELATIONS = ("IsDescribedBy", "IsReferencedBy", "IsSupplementTo", "IsDocumentedBy")
# DOIs that are not the paper: SPARC's own datasets, and protocols.io.
NOT_PAPERS = ("10.26275/", "10.17504/")
# Preprint servers: bioRxiv and medRxiv, Research Square, SSRN, Preprints.org, arXiv.
PREPRINTS = ("10.1101/", "10.21203/", "10.2139/", "10.20944/", "10.48550/")
SDS_SHEETS = ("dataset_description", "subjects", "samples", "performances", "resources", "code_description")
FILES_LISTED = 2000   # a dataset with more files lists only its top-level files and SDS sheets


def get(url: str) -> dict | list:
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


def pmc_of(dois: list[str]) -> dict[str, dict]:
    """PubMed and PubMed Central ids by DOI, from NCBI's ID converter."""
    if not dois:
        return {}
    try:
        found = get("https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?format=json&ids="
                    + urllib.parse.quote(",".join(dois)))["records"]
    except Exception:
        return {}
    return {r["doi"].lower(): {"pmid": str(r["pmid"]) if r.get("pmid") else None, "pmcid": r.get("pmcid")}
            for r in found if r.get("doi")}


def parse(spec: str) -> tuple[str, int | None, str]:
    """A dataset id or a SPARC DOI, a version number or None for the latest, and a paper DOI or "", from one
    argument. A SPARC DOI is returned as is, to be looked up."""
    # A paper DOI follows the last "=" only when it is one: a page's address has "=" of its own (?type=dataset).
    found_paper = re.fullmatch(r"(.+)=((?:https?://doi\.org/)?10\.\S+)", spec.strip(), re.I)
    item, paper = (found_paper.groups() if found_paper else (spec, ""))
    item = item.strip().rstrip("/")
    paper = paper.strip().lower().removeprefix("https://doi.org/")
    doi = re.search(r"(10\.26275/[a-z0-9-]+)$", item.lower())
    if doi:
        return doi.group(1), None, paper
    found = (re.fullmatch(r"(?:sparc:)?([0-9]+)(?::([0-9]+))?", item, re.I)
             or re.search(r"/datasets/([0-9]+)(?:/version/([0-9]+))?(?:\?.*)?$", item))
    if not found:
        raise SystemExit(f"error: not a SPARC dataset: {item!r}")
    return found.group(1), int(found.group(2)) if found.group(2) else None, paper


def hex_sha256(b64: str | None) -> str | None:
    """Pennsieve gives a file's SHA-256 in base64; the registry's lists give digests in hex."""
    return base64.b64decode(b64).hex() if b64 else None


def kind_of(path: str) -> str:
    name = path.rsplit("/", 1)[-1].lower()
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    return {"xlsx": "Excel", "xls": "Excel", "csv": "CSV", "tsv": "TSV", "txt": "text", "md": "Markdown",
            "json": "JSON", "mat": "MATLAB", "m": "MATLAB code", "h5": "HDF5", "hdf5": "HDF5", "nwb": "NWB",
            "tif": "TIFF", "tiff": "TIFF", "jp2": "JPEG 2000", "jpg": "JPEG", "png": "PNG", "pdf": "PDF",
            "zip": "zip", "py": "Python", "ipynb": "Jupyter", "r": "R script", "xml": "XML", "abf": "ABF",
            "smr": "Spike2", "adicht": "LabChart", "edf": "EDF", "nii": "NIfTI", "gz": "gzip",
            "dcm": "DICOM", "rhd": "Intan", "acq": "AcqKnowledge", "vtk": "VTK", "stl": "STL"}.get(ext, ext or "no extension")


def sds(paths: list[str]) -> dict:
    """Which parts of the SPARC Data Structure the dataset has: its folders under files/, and its sheets."""
    folders = sorted({p.split("/")[1] for p in paths if p.startswith("files/") and p.count("/") >= 2})
    sheets = sorted({p.rsplit("/", 1)[-1].rsplit(".", 1)[0] for p in paths
                     if p.count("/") == 1 and p.startswith("files/")
                     and p.rsplit("/", 1)[-1].rsplit(".", 1)[0] in SDS_SHEETS})
    return {"folders": folders, "sheets": sheets,
            "folder_manifests": sum(1 for p in paths if p.endswith("/manifest.xlsx") or p.endswith("/manifest.csv"))}


def target(spec: str) -> dict:
    id_, version, paper = parse(spec)
    if id_.startswith("10.26275/"):
        found = get(f"{API}/datasets/doi/{id_}")
        id_, version = str(found["id"]), version or found["version"]
    latest = get(f"{API}/datasets/{id_}")
    version = version or latest["version"]
    meta = latest if version == latest["version"] else get(f"{API}/datasets/{id_}/versions/{version}")
    versions = get(f"{API}/datasets/{id_}/versions")
    bucket = meta["uri"].split("/")[2]
    pinned = get(f"{API}/datasets/{id_}/versions/{version}/files?path=manifest.json")
    with urllib.request.urlopen(f"https://{bucket}.s3.amazonaws.com/{id_}/manifest.json?versionId={pinned['s3Version']}",
                                timeout=120) as r:
        raw = r.read()
    # The manifest lists itself, with no checksum or object version: those of the copy just read.
    files = [dict(f, s3VersionId=pinned["s3Version"], sha256=base64.b64encode(hashlib.sha256(raw).digest()).decode())
             if f["path"] == "manifest.json" else f for f in json.loads(raw)["files"]]
    paths = [f["path"] for f in files]
    listed = files if len(files) <= FILES_LISTED else [
        f for f in files if f["path"].count("/") <= 1 or f["path"].rsplit("/", 1)[-1].startswith("manifest.")]
    related = meta.get("externalPublications") or []
    dois = ([paper] if paper else []) + [r["doi"].lower() for r in related if r["relationshipType"] in PAPER_RELATIONS]
    dois = [d for d in dict.fromkeys(dois) if not d.startswith(NOT_PAPERS)]
    ids = pmc_of(dois)
    papers = []
    for d in dois:
        title, posted = title_of(d)
        papers.append({"doi": d, "title": title, "relation": "given" if d == paper else
                       next(r["relationshipType"] for r in related if r["doi"].lower() == d),
                       "resource_type": "Preprint" if posted or d.startswith(PREPRINTS) else "JournalArticle",
                       "preprint": posted or d.startswith(PREPRINTS), **ids.get(d, {"pmid": None, "pmcid": None})})
    return {
        "id": id_,
        "name": meta["name"].strip(),
        "url": f"https://sparc.science/datasets/{id_}?type=dataset",
        "doi": meta["doi"].lower(),
        "published_version": str(version),
        "latest": str(latest["version"]),
        "versions": len(versions),
        # Every version's DOI: a paper may cite any of them (tools/paper_match.py).
        "version_dois": [v["doi"].lower() for v in versions],
        "published": (meta.get("versionPublishedAt") or meta["createdAt"])[:10],
        "license": meta.get("license"),
        "bucket": bucket,
        "manifest_version": pinned["s3Version"],
        "asset_count": len(files),
        "size_gb": round(sum(f["size"] for f in files) / 1e9, 4),
        "data_standards": ["SDS"] + [k for k, _ in Counter(kind_of(p) for p in paths
                                                          if p.startswith("files/")).most_common()],
        "sds": sds(paths),
        "files_listed": "all" if len(listed) == len(files) else "top level and manifests",
        "files": [{"path": f["path"], "size": f["size"], "s3_version": f.get("s3VersionId"),
                   "sha256": hex_sha256(f.get("sha256"))} for f in listed],
        "readme": any(p.lower() in ("readme.md", "files/readme.txt", "files/readme.md") for p in paths),
        "description": (meta.get("description") or "").strip(),
        "code": [r["doi"] for r in related if r["relationshipType"] == "IsSupplementedBy"
                 and not r["doi"].lower().startswith(NOT_PAPERS)],
        "protocols": [r["doi"] for r in related if r["doi"].lower().startswith("10.17504/")],
        "contributors": [{"name": " ".join(x for x in (c.get("firstName"), c.get("lastName")) if x),
                          "orcid": c.get("orcid") or None} for c in meta.get("contributors") or []],
        "species": [],
        "approaches": [],
        "keywords": meta.get("tags") or [],
        "papers": papers,
        "catalystneuro": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("items", nargs="+", help="<id or SPARC DOI or URL>[:<version>][=<paper DOI>]")
    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "sparc.json")
    parser.add_argument("--note", default="Experimental SPARC datasets whose paper is in PubMed Central, chosen by hand "
                                         "to test the pipeline on SPARC.")
    args = parser.parse_args()
    targets = [target(s) for s in args.items]
    for t in targets:
        if not t["papers"]:
            print(f"warning: SPARC:{t['id']} links no paper; give one as {t['id']}=<paper DOI>", file=sys.stderr)
    out = {"schema_version": 1, "archive": "sparc",
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": f"{API}, chosen by hand (tools/build_sparc_targets.py)", "note": args.note,
           "counts": {"with_a_paper": sum(1 for t in targets if t["papers"])}, "targets": targets}
    args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(targets)} targets to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
