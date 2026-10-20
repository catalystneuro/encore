"""Write papers/manifest.yaml: for each target's papers, whether the paper store has the full text.

    python tools/papers_manifest.py STORE        # STORE: a checkout of catalystneuro/registry-papers

The store is private; the manifest is public and holds none of the text, only where each text
came from and what is missing (docs/pipeline.md). A target's papers are those its archive's metadata
names (the lists in targets/, tools/datasets.py), corrected by hand in papers/triage.yaml, and the paper of each of
its claims files.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def clean_doi(doi: str) -> str:
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi.strip().lower())
    doi = re.sub(r"[?#].*$", "", doi)
    doi = re.sub(r"\.(full|short|abstract)$", "", doi).rstrip(".)")
    # eLife: a figure's DOI (.001) or a reviewed preprint's version (.1, .2) names the article.
    doi = re.sub(r"(elife\.[0-9]+)\.[0-9]{1,3}$", r"\1", doi)
    return re.sub(r"(10\.(1101|64898)/[0-9.]+)v[0-9]+$", r"\1", doi)


def slug(doi: str) -> str:
    return doi.replace("/", "-")


def header(path: Path) -> dict:
    out = {}
    for line in path.read_text(errors="replace").splitlines()[:8]:
        if line.startswith("-----"):
            break
        key, _, value = line.partition(": ")
        out[key.lower()] = value
    return out


def target_papers() -> dict[str, list[str]]:
    triage = (yaml.safe_load((ROOT / "papers" / "triage.yaml").read_text()) or {}).get("targets", {})
    papers: dict[str, list[str]] = {}
    for t in datasets.targets():
        papers[t["folder"]] = [clean_doi(p["doi"]) for p in t.get("papers") or []]
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        if data.get("paper"):
            papers.setdefault(path.parent.name, []).append(clean_doi(data["paper"]))
    for d, fix in triage.items():
        drop = {clean_doi(x) for x in fix.get("not_papers", {})}
        papers[d] = [p for p in papers.get(d, []) if p not in drop] + [clean_doi(x) for x in fix.get("papers", {})]
    return {d: list(dict.fromkeys(ps)) for d, ps in papers.items()}


def manifest(store: Path) -> dict:
    triage = (yaml.safe_load((ROOT / "papers" / "triage.yaml").read_text()) or {}).get("targets", {})
    out = {}
    for d, dois in sorted(target_papers().items()):
        unavailable = {clean_doi(k): v for k, v in triage.get(d, {}).get("unavailable", {}).items()}
        rows = []
        for doi in dois:
            text = store / d / f"{slug(doi)}.txt"
            if text.is_file():
                h = header(text)
                row = {"doi": doi, "status": "stored", "version": h.get("version"), "source": h.get("source"),
                       "pdf": text.with_suffix(".pdf").is_file(),
                       "supplements": len(list(store.joinpath(d).glob(f"{slug(doi)}.supp*.pdf")))}
            elif doi in unavailable:
                row = {"doi": doi, "status": "unavailable", "note": unavailable[doi]}
            else:
                row = {"doi": doi, "status": "missing"}
            rows.append(row)
        out[d] = rows
    return out


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    data = manifest(Path(sys.argv[1]))
    counts: dict[str, int] = {}
    for rows in data.values():
        for r in rows:
            counts[r["status"]] = counts.get(r["status"], 0) + 1
    path = ROOT / "papers" / "manifest.yaml"
    path.write_text("# Written by tools/papers_manifest.py from the private paper store; do not edit by hand.\n"
                    + yaml.safe_dump({"schema_version": 1, "targets": data}, sort_keys=False, width=100))
    print(path.relative_to(ROOT), ", ".join(f"{n} {k}" for k, n in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
