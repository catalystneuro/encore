"""Build targets/osf.json, the registry's list of OSF datasets, from their GUIDs.

    python tools/build_osf_targets.py qpc2d 10.17605/OSF.IO/ABCDE https://osf.io/xyz12/=10.1038/... [--out targets/osf.json]

OSF (osf.io) holds hundreds of thousands of public projects, most of them study materials, preregistrations and
course pages rather than data, so the list is chosen, not crawled. Give each dataset as its GUID, its OSF DOI
(10.17605/OSF.IO/<GUID>) or a page URL (osf.io/<GUID>/, with or without a path after it), optionally with =<paper
DOI> when the project does not link its paper itself. A GUID may name a project, a component, a registration or a
preprint; for a preprint, the builder takes the project the preprint links as its supplemental materials.

For each, the builder reads OSF's public API v2 (no account needed for a public project): the title, description,
license, contributors and DOI; every file in every storage provider, in every folder, and in every public
component below it, with its size, version, MD5 and SHA-256; and the papers. A project is not versioned as a whole,
so each file is pinned by its own version number and hashes, and published_version is the time the project was
last modified (for a registration, the time it was registered). The papers are the DOI given, a registration's
article DOI, and the preprints that name the project as their supplemental materials, with the journal article
each preprint was published as, titled from Crossref.

A dataset is named by its GUID (OSF:qpc2d, folder osf-qpc2d); GUIDs ignore case. Reading the files needs no
account (docs/archives.md, "OSF").
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.osf.io/v2"
OSF_DOI = "10.17605/osf.io/"
# Storage add-ons that hold code rather than data.
CODE_PROVIDERS = ("github", "gitlab", "bitbucket")
PAGE_SIZE = 100


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.api+json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def paged(url: str) -> str:
    """The address with the largest page OSF gives, unless it already asks for one."""
    if "page[size]" in urllib.parse.unquote(url):
        return url
    return url + ("&" if "?" in url else "?") + f"page[size]={PAGE_SIZE}"


def pages(url: str) -> Iterator[dict]:
    """Every item of a listing, following links.next from page to page."""
    next_url: str | None = paged(url)
    while next_url:
        page = get(next_url)
        yield from page["data"]
        next_url = (page.get("links") or {}).get("next")


def related(item: dict, name: str) -> str | None:
    """The address of an item's relationship, or None when it has none."""
    return (((item.get("relationships") or {}).get(name) or {}).get("links") or {}).get("related", {}).get("href")


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
    """A GUID, in lower case, and a paper DOI or "", from one argument."""
    found_paper = re.fullmatch(r"(.+?)=((?:https?://(?:dx\.)?doi\.org/)?10\.\S+)", spec.strip(), re.I)
    item, paper = found_paper.groups() if found_paper else (spec.strip(), "")
    item = item.strip()
    found = (re.fullmatch(r"(?:osf:)?([a-z0-9]{5})", item, re.I)
             or re.search(r"10\.17605/osf\.io/([a-z0-9]{5})\b", item, re.I)
             or re.search(r"osf\.io/([a-z0-9]{5})(?:[/?#]|$)", item, re.I))
    if not found:
        raise SystemExit(f"error: not an OSF GUID, DOI or page: {item!r}")
    return found.group(1).lower(), clean_doi(paper)


def resolve(guid: str) -> dict:
    """The object a GUID names (a node, registration or preprint), as the API gives it under data."""
    try:
        return get(f"{API}/guids/{guid}/")["data"]   # answers with a redirect to the object itself
    except urllib.error.HTTPError:
        pass
    for kind in ("nodes", "registrations", "preprints"):
        try:
            return get(f"{API}/{kind}/{guid}/")["data"]
        except urllib.error.HTTPError as err:
            if err.code not in (404, 410):
                raise
    raise SystemExit(f"error: OSF:{guid} is not a public project, registration or preprint")


def kind_of(name: str) -> str:
    name = name.lower()
    ext = name.rsplit(".", 1)[-1] if "." in name.rsplit("/", 1)[-1] else ""
    return {"xlsx": "Excel", "xls": "Excel", "csv": "CSV", "tsv": "TSV", "txt": "text", "md": "Markdown",
            "zip": "zip", "gz": "gzip", "rds": "RDS", "rdata": "RData", "pdf": "PDF", "r": "R script",
            "py": "Python", "ipynb": "Jupyter", "m": "MATLAB script", "mat": "MATLAB", "h5": "HDF5", "hdf5": "HDF5",
            "nwb": "NWB", "nc": "NetCDF", "json": "JSON", "npy": "NumPy", "npz": "NumPy", "pkl": "pickle",
            "edf": "EDF", "bdf": "BDF", "set": "EEGLAB", "fif": "FIF", "nii": "NIfTI", "abf": "ABF",
            "tif": "TIFF", "tiff": "TIFF", "docx": "Word", "sav": "SPSS"}.get(ext, ext or "no extension")


def file_record(item: dict, prefix: str = "") -> dict:
    """What the target list keeps of one file in a folder listing. A file outside OSF Storage is named with its
    provider first (github/..., googledrive/...); one in a component, with the component's GUID first."""
    a = item["attributes"]
    path = a["materialized_path"].lstrip("/")
    if a["provider"] != "osfstorage":
        path = f'{a["provider"]}/{path}'
    hashes = (a.get("extra") or {}).get("hashes") or {}
    return {"path": prefix + path, "provider": a["provider"], "size": a.get("size"), "file_id": item["id"],
            "version": a.get("current_version"), "md5": hashes.get("md5"), "sha256": hashes.get("sha256"),
            "modified": a.get("date_modified"), "download": (item.get("links") or {}).get("download")}


def walk(url: str, prefix: str = "") -> Iterator[dict]:
    """Every file under a folder listing, depth first, following each folder's own listing."""
    for item in pages(url):
        if item["attributes"]["kind"] == "folder":
            yield from walk(related(item, "files"), prefix)
        else:
            yield file_record(item, prefix)


def files_of(base: str, prefix: str = "") -> tuple[list[dict], list[str]]:
    """The files of a node or registration in every storage provider, and the providers."""
    files, providers = [], []
    for storage in pages(f"{base}files/"):
        providers.append(storage["attributes"]["provider"])
        files += walk(related(storage, "files"), prefix)
    return files, providers


def components_of(base: str) -> list[dict]:
    """The public components below a node or registration, at every depth, each with its GUID and title."""
    out = []
    for child in pages(f"{base}children/"):
        here = f'{API}/{child["type"]}/{child["id"]}/'
        out.append({"id": child["id"], "title": child["attributes"]["title"],
                    "category": child["attributes"].get("category"), "base": here})
        out += components_of(here)
    return out


def contributors_of(base: str) -> list[str]:
    """The bibliographic contributors' names, in the order OSF cites them."""
    names = []
    for c in pages(f"{base}contributors/?embed=users"):
        if not c["attributes"].get("bibliographic", True):
            continue
        user = ((c.get("embeds") or {}).get("users") or {}).get("data") or {}
        names.append((user.get("attributes") or {}).get("full_name")
                     or c["attributes"].get("unregistered_contributor") or "")
    return [n for n in names if n]


def doi_of(base: str, node: dict) -> str | None:
    """The node's DOI, when one has been minted (OSF mints one for a project only on request)."""
    for ident in pages(related(node, "identifiers") or f"{base}identifiers/"):
        if ident["attributes"].get("category") == "doi":
            return clean_doi(ident["attributes"]["value"])
    return None


def license_of(node: dict) -> dict:
    href = related(node, "license")
    if not href:
        return {}
    a = get(href)["data"]["attributes"]
    return {"name": a.get("name"), "url": a.get("url")}


def preprint_papers(preprint: dict) -> list[dict]:
    """A preprint's own DOI, and the DOI of the article it was published as, when its authors have given one."""
    own = clean_doi((preprint.get("links") or {}).get("preprint_doi"))
    published = clean_doi(preprint["attributes"].get("doi"))
    return ([{"doi": own, "relation": "preprint", "preprint": True}] if own else []) + \
        ([{"doi": published, "relation": "preprint_published", "preprint": False}] if published else [])


def preprints_of(guid: str) -> list[dict]:
    """The papers of the preprints that name a project as their supplemental materials."""
    try:
        return [p for preprint in pages(f"{API}/nodes/{guid}/preprints/") for p in preprint_papers(preprint)]
    except urllib.error.HTTPError:
        return []


def papers_of(paper: str, node: dict, preprints: list[dict]) -> list[dict]:
    listed = ([{"doi": paper, "relation": "given", "preprint": False}] if paper else [])
    article = clean_doi(node["attributes"].get("article_doi"))
    listed += [{"doi": article, "relation": "article_doi", "preprint": False}] if article else []
    listed += preprints
    out, seen = [], set()
    for p in listed:
        if p["doi"] in seen or p["doi"].startswith(OSF_DOI):
            continue
        seen.add(p["doi"])
        title, preprint = title_of(p["doi"])
        out.append({"doi": p["doi"], "title": title, "relation": p["relation"], "resource_type": "JournalArticle",
                    "preprint": p["preprint"] or preprint})
    return out


def target(spec: str) -> dict:
    guid, paper = parse(spec)
    node = resolve(guid)
    preprints = []
    if node["type"] == "preprints":
        # A preprint's GUID: the dataset is the project it links as supplemental materials.
        preprints = preprint_papers(node)
        href = related(node, "node")
        if not href:
            raise SystemExit(f"error: OSF:{guid} is a preprint that links no project")
        node = get(href)["data"]
    guid, api_type, a = node["id"], node["type"], node["attributes"]
    if api_type not in ("nodes", "registrations"):
        raise SystemExit(f"error: OSF:{guid} is a {api_type[:-1]}, not a project or registration")
    base = f"{API}/{api_type}/{guid}/"
    root = re.search(r"/(?:nodes|registrations)/([a-z0-9]+)/", related(node, "root") or "")
    is_component = bool(root and root.group(1) != guid)
    files, providers = files_of(base)
    components = components_of(base)
    for c in components:
        more, also = files_of(c["base"], prefix=f'{c["id"]}/')
        files += more
        providers += also
    if api_type == "nodes":
        preprints = preprints or preprints_of(guid)
    registration = api_type == "registrations"
    names = [f["path"] for f in files]
    return {
        "id": guid,
        "name": a["title"].strip(),
        "url": (node.get("links") or {}).get("html") or f"https://osf.io/{guid}/",
        "doi": doi_of(base, node),
        "api_type": api_type,
        "kind": "registration" if registration else "component" if is_component else "project",
        "category": a.get("category"),
        "published_version": (a.get("date_registered") if registration else None) or a["date_modified"],
        "published": (a.get("date_created") or "")[:10],
        "withdrawn": bool(a.get("withdrawn")) if registration else False,
        "license": license_of(node),
        "contributors": contributors_of(base),
        "description": " ".join((a.get("description") or "").split()),
        "components": [{k: c[k] for k in ("id", "title", "category")} for c in components],
        "providers": sorted(set(providers)),
        "asset_count": len(files),
        "size_gb": round(sum(f["size"] or 0 for f in files) / 1e9, 4),
        "data_standards": sorted({kind_of(n) for n in names} - {"Markdown"}),
        "files": files,
        "readme": any(n.rsplit("/", 1)[-1].lower().startswith("readme") for n in names),
        "code": sorted({p for p in providers if p in CODE_PROVIDERS}),
        "species": [],
        "approaches": [],
        "keywords": a.get("tags") or [],
        "papers": papers_of(paper, node, preprints),
        "catalystneuro": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("items", nargs="+", help="<GUID or OSF DOI or URL>[=<paper DOI>]")
    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "osf.json")
    parser.add_argument("--note", default="OSF projects chosen by hand to test the pipeline on OSF.")
    args = parser.parse_args()
    targets = [target(s) for s in args.items]
    for t in targets:
        if t["withdrawn"]:
            print(f"warning: OSF:{t['id']} is a withdrawn registration", file=sys.stderr)
        if not t["files"]:
            print(f"warning: OSF:{t['id']} has no files", file=sys.stderr)
        if any(f["provider"] != "osfstorage" for f in t["files"]):
            print(f"warning: OSF:{t['id']} has files outside OSF Storage, which OSF does not version",
                  file=sys.stderr)
    out = {"schema_version": 1, "archive": "osf",
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": f"{API}, chosen by hand (tools/build_osf_targets.py)", "note": args.note,
           "counts": {"with_a_paper": sum(1 for t in targets if t["papers"])}, "targets": targets}
    args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(targets)} targets to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
