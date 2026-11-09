"""Build targets/openneuro.json, the registry's list of OpenNeuro datasets, from their accession numbers.

    python tools/build_openneuro_targets.py ds002778 ds004752:1.0.1 ds000228=10.1038/s41467-018-03399-2 ... \
        [--out targets/openneuro.json]

OpenNeuro holds over a thousand BIDS datasets, most of them large imaging studies, so the list is chosen, not
crawled. Give each dataset as its accession number, a snapshot DOI (10.18112/openneuro.<id>.v<tag>) or a page URL
(openneuro.org/datasets/<id>[/versions/<tag>]), optionally with :<tag> to pin a snapshot other than the latest and
with =<paper DOI> when the dataset does not link its paper in a form the builder reads. For each, the builder reads
OpenNeuro's public GraphQL API (no account needed), pins the snapshot by its tag, DOI and git commit, and records
the snapshot's layout: how many files of each BIDS kind it holds, with their sizes, and the top-level files with
their checksums. The papers are the DOI given and the DOIs, PubMed ids and Nature article links in the dataset's
metadata (associatedPaperDOI, openneuroPaperDOI) and dataset_description.json (ReferencesAndLinks,
HowToAcknowledge), titled from Crossref and looked up in Europe PMC for a PMCID. It also records what an agent will
need to know before reading the data: the BIDS validator's errors, whether there are events files, and whether
there are derivatives.

A dataset is named by its accession number (OPENNEURO:ds002778, folder openneuro-ds002778). Reading the files
needs no account (docs/archives.md, "OpenNeuro").
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://openneuro.org/crn/graphql"
QUERY = """query ($id: ID!, $tag: String!) {
  dataset(id: $id) { name latestSnapshot { tag } snapshots { tag }
    metadata { associatedPaperDOI openneuroPaperDOI species } }
  snapshot(datasetId: $id, tag: $tag) { tag created hexsha size
    description { Name DatasetDOI License BIDSVersion ReferencesAndLinks HowToAcknowledge }
    summary { modalities subjects sessions tasks }
    validation { errors warnings codeMessages { code } }
    files(recursive: true) { filename size annexed directory id urls } } }"""
DOI = re.compile(r"10\.\d{4,9}/[^\s,;\"'<>\]\[]+")
FORMATS = {".nii": "NIfTI", ".nii.gz": "NIfTI", ".edf": "EDF", ".bdf": "BDF", ".set": "EEGLAB", ".fif": "FIF",
           ".vhdr": "BrainVision", ".nwb": "NWB", ".mefd": "MEF3", ".ds": "CTF", ".con": "KIT", ".snirf": "SNIRF",
           ".mat": "MATLAB", ".tsv": "TSV", ".csv": "CSV", ".json": "JSON", ".html": "HTML"}


def get(url: str, body: dict | None = None) -> dict:
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Accept": "application/json", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def graphql(id_: str, tag: str) -> dict:
    out = get(API, {"query": QUERY, "variables": {"id": id_, "tag": tag}})
    if out.get("errors"):
        raise SystemExit(f"error: OPENNEURO:{id_}:{tag}: {out['errors'][0]['message']}")
    return out["data"]


def title_of(doi: str) -> str:
    try:
        return " ".join(get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]["title"][0].split())
    except Exception:   # a DOI Crossref does not hold (a DataCite preprint, say)
        return ""


def europepmc(query: str) -> dict:
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": query, "format": "json", "resultType": "lite"})
    try:
        return (get(url)["resultList"]["result"] or [{}])[0]
    except Exception:
        return {}


def parse(spec: str) -> tuple[str, str | None, str]:
    """An accession number, a snapshot tag or None for the latest, and a paper DOI or "", from one argument."""
    item, _, paper = spec.partition("=")
    item = item.strip().rstrip("/")
    found = (re.fullmatch(r"(ds[0-9]{6})(?::([0-9][0-9.]*))?", item)
             or re.search(r"openneuro\.(ds[0-9]{6})\.v([0-9][0-9.]*[0-9])$", item)
             or re.search(r"/datasets/(ds[0-9]{6})(?:/versions/([0-9][0-9.]*))?$", item))
    if not found:
        raise SystemExit(f"error: not an OpenNeuro dataset: {item!r}")
    return found.group(1), found.group(2), paper.strip().lower().removeprefix("https://doi.org/")


def papers_in(texts: list[str]) -> list[str]:
    """The paper DOIs in free text: DOIs, PubMed ids (looked up in Europe PMC), and Nature article links."""
    dois = []
    for text in texts:
        dois += [d.rstrip(".").lower() for d in DOI.findall(text)]
        dois += [f"10.1038/{a.lower()}" for a in re.findall(r"nature\.com/articles/(s[0-9a-z-]+)", text)]
        for pmid in re.findall(r"(?:pubmed/|PMID:?\s*)([0-9]{6,9})", text):
            dois += [europepmc(f"EXT_ID:{pmid} AND SRC:MED").get("doi", "").lower()]
    return [d for d in dict.fromkeys(dois) if d and not d.startswith("10.18112/openneuro.")]


def checksum(f: dict) -> dict:
    """A file's checksum from OpenNeuro's id for it: a git-annex key (MD5E-s<size>--<md5>, SHA256E-...) for an
    annexed file, the git blob's SHA-1 (of b"blob <size>\\0" + content) for a file kept in git."""
    key = re.fullmatch(r"(MD5|SHA256)E?-s[0-9]+--([0-9a-f]+)(?:\..*)?", f["id"])
    if f["annexed"] and key:
        return {key.group(1).lower(): key.group(2)}
    return {} if f["annexed"] else {"git_sha1": f["id"]}


def kind_of(path: str) -> str:
    """A file's BIDS kind: its suffix and extension (events.tsv, eeg.bdf) for a file named with entities
    (sub-01_task-rest_eeg.bdf), its name for any other (participants.tsv), and for a derivative, the pipeline's
    folder and the extension (derivatives/mriqc/*.json)."""
    parts = path.split("/")
    name = parts[-1]
    if parts[0] == "derivatives":
        pipeline = next((p for p in parts[1:-1] if not re.match(r"(sub|ses)-", p)), "")
        return f"derivatives/{pipeline + '/' if pipeline else ''}*.{name.partition('.')[2] or name}"
    stem, dot, ext = name.partition(".")
    return stem.rsplit("_", 1)[-1] + dot + ext if re.match(r"[a-z]+-[^_]+_", stem) else name


def target(spec: str) -> dict:
    id_, tag, paper = parse(spec)
    if not tag:
        latest = get(API, {"query": f'{{ dataset(id: "{id_}") {{ latestSnapshot {{ tag }} }} }}'})
        tag = latest["data"]["dataset"]["latestSnapshot"]["tag"]
    data = graphql(id_, tag)
    ds, snap = data["dataset"], data["snapshot"]
    desc, meta, summary = snap["description"] or {}, ds["metadata"] or {}, snap["summary"] or {}
    files = [f for f in snap["files"] if not f["directory"] and not f["filename"].startswith(".")]
    kinds = collections.defaultdict(lambda: [0, 0])
    for f in files:
        kinds[kind_of(f["filename"])][0] += 1
        kinds[kind_of(f["filename"])][1] += f["size"]
    texts = [meta.get("associatedPaperDOI") or "", meta.get("openneuroPaperDOI") or "", desc.get("HowToAcknowledge") or ""]
    texts += desc.get("ReferencesAndLinks") or []
    found = papers_in(texts)
    papers = []
    for d in dict.fromkeys(([paper] if paper else []) + found):
        pmc = europepmc(f'DOI:"{d}"')
        papers.append({"doi": d, "title": title_of(d), "relation": "given" if d == paper and d not in found else
                       "metadata", "resource_type": "JournalArticle", "preprint": d.startswith("10.1101/"),
                       "pmid": pmc.get("pmid"), "pmcid": pmc.get("pmcid")})
    codes = sorted({c["code"] for c in (snap["validation"] or {}).get("codeMessages") or []})
    ext = lambda p: next((e for e in sorted(FORMATS, key=len, reverse=True) if p.lower().endswith(e)), "")
    return {
        "id": id_,
        "name": desc.get("Name") or ds["name"],
        "url": f"https://openneuro.org/datasets/{id_}/versions/{tag}",
        "doi": f"10.18112/openneuro.{id_}.v{tag}",
        "published_version": tag,
        "git_commit": snap["hexsha"],
        "versions": len(ds["snapshots"]),
        "latest": tag == ds["latestSnapshot"]["tag"],
        "published": snap["created"][:10],
        "license": desc.get("License"),
        "bids_version": desc.get("BIDSVersion"),
        "modalities": summary.get("modalities") or [],
        "subjects": len(summary.get("subjects") or []),
        "sessions": summary.get("sessions") or [],
        "tasks": summary.get("tasks") or [],
        "asset_count": len(files),
        "size_gb": round(sum(f["size"] for f in files) / 1e9, 4),
        "snapshot_size_gb": round(int(snap["size"]) / 1e9, 4),   # OpenNeuro's figure, without derivatives
        "data_standards": ["BIDS"] + sorted({FORMATS[ext(f["filename"])] for f in files if ext(f["filename"])}
                                            - {"TSV", "JSON", "CSV", "HTML"}),
        "validation": {"errors": (snap["validation"] or {}).get("errors"),
                       "warnings": (snap["validation"] or {}).get("warnings"), "codes": codes},
        "events": kinds.get("events.tsv", [0])[0],
        "derivatives": sorted({k.split("/")[1] for k in kinds if k.startswith("derivatives/") and k.count("/") > 1}),
        "layout": {k: {"files": n, "size": s} for k, (n, s) in sorted(kinds.items())},
        "files": [{"path": f["filename"], "size": f["size"], "id": f["id"], **checksum(f)}
                  for f in files if "/" not in f["filename"]],
        "readme": any(f["filename"].upper().startswith("README") for f in files if "/" not in f["filename"]),
        "species": [meta["species"]] if meta.get("species") else [],
        "approaches": [],
        "keywords": [],
        "papers": papers,
        "catalystneuro": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("items", nargs="+", help="<accession or DOI or URL>[:<tag>][=<paper DOI>]")
    parser.add_argument("--out", type=Path, default=ROOT / "targets" / "openneuro.json")
    parser.add_argument("--note", default="BIDS datasets with an open-access paper in PubMed Central, one each of "
                                         "scalp EEG, intracranial EEG and fMRI, chosen by hand to test the pipeline "
                                         "on OpenNeuro.")
    args = parser.parse_args()
    targets = [target(s) for s in args.items]
    for t in targets:
        if not any(p["pmcid"] for p in t["papers"]):
            print(f"warning: OPENNEURO:{t['id']} has no paper in PubMed Central", file=sys.stderr)
    out = {"schema_version": 1, "archive": "openneuro",
           "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "source": f"{API}, chosen by hand (tools/build_openneuro_targets.py)", "note": args.note,
           "counts": {"with_a_paper": sum(1 for t in targets if t["papers"])}, "targets": targets}
    args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(targets)} targets to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
