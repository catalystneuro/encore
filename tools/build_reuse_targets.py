"""Papers that reuse a dataset, from find_reuse's classifications, as targets (docs/paper-first.md).

    python tools/build_reuse_targets.py CLASSIFICATIONS.json [--doi DOI ...] [--limit N]

Reads find_reuse's full-text classifications (catalystneuro/find_reuse, output/fulltext_classifications.json)
and keeps the pairs a paper's analysis can be tested on here:

- classified REUSE, at confidence 9 or more, by a lab other than the data's (same_lab false);
- data the paper says it took from DANDI (find_reuse's source_archive), a dandiset in targets/dandisets.json, and
  the only dandiset the paper reuses: an attempt is made on the data the paper used, and a paper that took the same
  recordings from another archive (CRCNS, say) is tested there instead, not here;
- a reuse whose claims are findings about the data: NOVEL_ANALYSIS or CONFIRMATORY (not a tool demonstration,
  benchmark, simulation or model training, whose claims are about a method);
- a paper that is not already a primary paper of the registry's.

With --checked CHECKS.json the papers come from an independent check of find_reuse's pairs instead (a JSON list,
one item per paper: doi, title, datasets, reuse_type, same_lab, testable_alone, other_datasets, evidence, notes):
an agent read each paper and its dandiset's metadata without find_reuse's verdict, and kept the papers that
analyze the dandiset's data for findings of their own. The check stands in for the filters above, so a paper by
the data's own lab, one on a dandiset outside the archive's targets, and one on several dandisets are all taken;
each is listed for every dandiset it was checked on.

With --doi, only those papers (a pilot). For each it gives the paper a key (papers/keys.yaml), lists its dataset
with `relation: reuses` (papers/datasets/<key>.yaml), and adds it to targets/reuse.yaml, which the queue takes
after every primary target (tools/runner/describe.py). The paper's text goes in the paper store separately, under
the dataset's folder.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import paper_keys  # noqa: E402

TYPES = ("NOVEL_ANALYSIS", "CONFIRMATORY")
HEADER = """\
# Papers that reuse a dataset, queued after every primary target (tools/build_reuse_targets.py, from
# catalystneuro/find_reuse's classifications; docs/paper-first.md). Each is listed for its dataset in
# papers/datasets/<key>.yaml with relation: reuses.
"""


def candidates(classifications: list[dict], dandisets: set[str], primary: set[str]) -> list[dict]:
    reuse = [c for c in classifications if c.get("classification") == "REUSE" and c.get("dandiset_id")]
    per_paper: dict[str, set] = {}
    for c in reuse:
        per_paper.setdefault(paper_keys.doi_of(c["citing_doi"]), set()).add(str(c["dandiset_id"]).zfill(6))
    out, seen = [], set()
    for c in reuse:
        doi = paper_keys.doi_of(c["citing_doi"])
        ds = str(c["dandiset_id"]).zfill(6)
        if (c.get("confidence") or 0) < 9 or c.get("same_lab") is not False or c.get("source_archive") != "DANDI Archive":
            continue
        if c.get("reuse_type") not in TYPES or len(per_paper[doi]) != 1 or ds not in dandisets:
            continue
        if doi in primary or doi in seen:
            continue
        seen.add(doi)
        quote = next((q["quote"] for q in c.get("evidence_quotes") or [] if q.get("verbatim")), None)
        out.append({"doi": doi, "dataset": ds, "title": c.get("title"), "reuse_type": c["reuse_type"],
                    "reasoning": " ".join((c.get("reasoning") or "").split()), "quote": quote})
    return out


def describe_outside_datasets() -> list[str]:
    """Write targets/reuse_datasets.json: the dandisets that papers are listed for (papers/datasets/) and no
    archive's list has, each described as a target is (tools/build_targets.py), from the DANDI Archive. A paper
    that reuses a dandiset can name one whose own metadata names no paper, which the target list leaves out; the
    site shows it as a dataset all the same (tools/build_site.py, collect)."""
    import build_targets
    import datasets
    import paper_records
    have = {t["key"] for t in datasets.targets()}
    wanted = sorted({d["id"] for body in paper_records.listed().values() for d in body.get("datasets") or []
                     if d["archive"] == "dandi" and d["key"] not in have})
    path = ROOT / "targets" / "reuse_datasets.json"
    known = {t["dandiset"]: t for t in json.loads(path.read_text())["targets"]} if path.is_file() else {}
    out = []
    for id_ in wanted:
        if id_ not in known:
            summary = build_targets.get(f"{build_targets.API}/dandisets/{id_}/")
            known[id_] = {**build_targets.target(summary), "papers": [], "reuse_only": True}
        out.append(known[id_])
    path.write_text(json.dumps({"schema_version": 1, "source": "tools/build_reuse_targets.py, from the DANDI Archive",
                                "targets": out}, indent=1, ensure_ascii=False) + "\n")
    return wanted


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classifications", type=Path, nargs="?")
    ap.add_argument("--checked", type=Path, help="papers from an agent's check of the pairs, in place of the filters")
    ap.add_argument("--doi", nargs="*", default=[])
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()
    if not args.checked and not args.classifications:
        ap.error("give find_reuse's classifications, or --checked")
    found = json.loads(args.classifications.read_text()) if args.classifications else []
    found = found.get("classifications", found) if isinstance(found, dict) else found
    dandisets = {str(t["dandiset"]).zfill(6) for t in json.loads((ROOT / "targets" / "dandisets.json").read_text())["targets"]}
    primary = set()
    for path in (ROOT / "papers" / "datasets").glob("*.yaml"):
        body = yaml.safe_load(path.read_text()) or {}
        if any(d.get("relation", "primary") == "primary" for d in body.get("datasets") or []):
            primary.add(paper_keys.doi_of(body["paper"]))
    if args.checked:
        picked = [{"doi": paper_keys.doi_of(c["doi"]), "dataset": str(c["datasets"][0]).zfill(6),
                   "datasets": [str(x).zfill(6) for x in c["datasets"]], "title": c.get("title"),
                   "reuse_type": c["reuse_type"], "quote": c.get("evidence"), "checked": True,
                   "reasoning": " ".join(filter(None, [
                       c.get("notes"),
                       "The paper's authors overlap with the dandiset's contributors." if c.get("same_lab") else None,
                       None if c.get("testable_alone") else "Its findings also rest on other data"
                       + (f" ({', '.join(map(str, c['other_datasets'][:6]))})" if c.get("other_datasets") else "")
                       + ", so some claims cannot be tested here."]))}
                  for c in json.loads(args.checked.read_text())
                  if c["reuse_type"] in TYPES and paper_keys.doi_of(c["doi"]) not in primary]
    else:
        picked = candidates(found, dandisets, primary)
    if args.doi:
        wanted = {paper_keys.doi_of(d) for d in args.doi}
        picked = [p for p in picked if p["doi"] in wanted]
        missing = wanted - {p["doi"] for p in picked}
        if missing:
            print(f"not among the candidates: {', '.join(sorted(missing))}", file=sys.stderr)
    picked = picked[:args.limit] if args.limit else picked
    reuse_path = ROOT / "targets" / "reuse.yaml"
    listed = (yaml.safe_load(reuse_path.read_text()) or {}).get("papers", []) if reuse_path.is_file() else []
    have = {p["doi"] for p in listed}
    for p in picked:
        key = paper_keys.add_key(p["doi"], p.get("title") or "")
        body = {"schema_version": 1, "paper": f"doi:{p['doi']}", **({"title": p["title"]} if p.get("title") else {}),
                "datasets": [{"archive": "dandi", "id": ds, "relation": "reuses"}
                             for ds in p.get("datasets") or [p["dataset"]]]}
        path = ROOT / "papers" / "datasets" / f"{key}.yaml"
        if not path.is_file():
            path.write_text("# The datasets this paper is tested on (docs/paper-first.md).\n"
                            + yaml.safe_dump(body, sort_keys=False, width=100, allow_unicode=True))
        if p["doi"] not in have:
            listed.append({"key": key, "doi": p["doi"], "dataset": f"dandi:{p['dataset']}",
                           "reuse_type": p["reuse_type"], "evidence": p["quote"], "reasoning": p["reasoning"],
                           "source": "find_reuse, checked by an agent" if p.get("checked") else "find_reuse"})
            have.add(p["doi"])
        print(f"{key}: {p['doi']} reuses DANDI:{p['dataset']} ({p['reuse_type']})")
    reuse_path.write_text(HEADER + yaml.safe_dump({"schema_version": 1, "papers": listed}, sort_keys=False,
                                                  width=110, allow_unicode=True))
    print(f"{len(picked)} papers; targets/reuse.yaml lists {len(listed)}", file=sys.stderr)
    outside = describe_outside_datasets()
    print(f"targets/reuse_datasets.json describes {len(outside)} dandisets outside the target list", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
