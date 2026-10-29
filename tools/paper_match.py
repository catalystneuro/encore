"""Whether each paper a dataset names is the paper behind its data (docs/pipeline.md, step 1).

    python tools/paper_match.py checks FOLDER PAPERS   # write papers/match/<folder>.yaml from the cheap checks;
                                                      # prints "agent" when a paper is left for the agent, else "done"
    python tools/paper_match.py status FOLDER          # matched, unchecked, held or no_match
    python tools/paper_match.py validate FILE ...      # check match files against schemas/paper-match.schema.json
    python tools/paper_match.py tally STORE            # the cheap checks over every target, counted; writes nothing

PAPERS is a directory of the dataset's paper texts, `<doi with / as ->.txt`, as tools/get_papers.sh
writes them; STORE is a checkout of the paper store, one such directory per dataset.

An archive's metadata names papers loosely: a review cited as background, a paper whose data are in
another dataset, a mistyped DOI. papers/triage.yaml holds a person's corrections; papers/match/<folder>.yaml
then judges each paper that is left, with one verdict:

    primary       the dataset is the paper's data
    partial       the dataset holds part of the paper's data
    other_data    a paper whose data are elsewhere (`data_in` says where)
    background    a paper cited for context: a review, a method
    not_a_paper   a dataset, a protocol, software
    wrong_doi     the DOI is not the paper the archive means

The cheap checks settle a paper as primary without an agent when its text carries its title and it
names this dataset and no other one, or when the archive says the paper describes the dataset
(IsDescribedBy) and the paper names no dataset at all. Anything else is left for the agent
(docs/agents/paper-match.md). A primary or partial paper is used at once. A verdict that leaves the
dataset no usable paper holds it out of the queue until a person confirms it (`confirmed: true`) or
corrects it.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402
from papers_manifest import clean_doi, slug  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MATCH = ROOT / "papers" / "match"
USABLE = ("primary", "partial")
VERDICTS = USABLE + ("other_data", "background", "not_a_paper", "wrong_doi")
PREPRINTS = ("10.1101/", "10.64898/", "10.48550/", "10.21203/")

# Datasets a paper names. A DANDI dataset by its six digits after "DANDI", "dandiset", its URL or its DOI;
# OpenNeuro by its accession.
DANDI_ID = re.compile(r"(?:dandiarchive\.org/dandiset/|10\.48324/dandi\.|\bdandi(?:set)?\s*(?:archive\s*)?[:#]?\s*)"
                      r"(\d{6})\b", re.I)
OPENNEURO_ID = re.compile(r"\b(ds\d{6})\b", re.I)
HEAD = 6000   # the title is looked for in the first characters of the text: the header and the title page


def triage() -> dict:
    return (yaml.safe_load((ROOT / "papers" / "triage.yaml").read_text()) or {}).get("targets", {})


def load(folder: str, root: Path = ROOT) -> dict | None:
    path = root / "papers" / "match" / f"{folder}.yaml"
    return yaml.safe_load(path.read_text()) if path.is_file() else None


def listed(target: dict, fix: dict) -> list[dict]:
    """The papers a target names after a person's corrections: those triage names first, then the archive's
    papers that triage does not set aside, one per DOI."""
    drop = {clean_doi(d) for d in fix.get("not_papers", {})}
    out = [{"doi": clean_doi(d), "title": None, "relation": "triage", "named": True}
           for d in fix.get("papers", {})]
    for p in target.get("papers") or []:
        doi = clean_doi(p["doi"])
        if doi not in drop and doi not in {q["doi"] for q in out}:
            out.append({"doi": doi, "title": p.get("title"), "relation": p.get("relation"), "named": False,
                        "preprint": bool(p.get("preprint")) or doi.startswith(PREPRINTS)})
    return out


def choose(target: dict, fix: dict, match: dict | None) -> tuple[str, list[dict]]:
    """The match status of a target and the papers an attempt may use, best first.

    `unchecked`: no verdict yet on a paper that could be used (the archive's papers, as before).
    `matched`: at least one paper is primary or partial, or a person named it in triage.
    `held`: no paper is usable, and a person has not yet confirmed every verdict that says so.
    `no_match`: no paper is usable, confirmed.
    """
    papers = listed(target, fix)
    named = [p for p in papers if p["named"]]
    verdicts = {clean_doi(v["doi"]): v for v in (match or {}).get("papers", [])}
    judged = [dict(p, **{k: verdicts[p["doi"]][k] for k in ("verdict", "confirmed") if k in verdicts[p["doi"]]})
              for p in papers if p["doi"] in verdicts and not p["named"]]
    usable = sorted([p for p in judged if p.get("verdict") in USABLE],
                    key=lambda p: (USABLE.index(p["verdict"]), p.get("preprint", False)))
    if named or usable:
        return "matched", named + usable
    if match is None or any(p["doi"] not in verdicts or not verdicts[p["doi"]].get("verdict") for p in papers):
        return "unchecked", sorted(papers, key=lambda p: p.get("preprint", False))
    if all(p.get("confirmed") for p in judged):
        return "no_match", []
    return "held", []


def archives_named(text: str) -> list[str]:
    """The datasets a paper's text names, as DANDI:<id> or OpenNeuro:<id>."""
    found = [f"DANDI:{m}" for m in DANDI_ID.findall(text)] + [f"OpenNeuro:{m.lower()}" for m in OPENNEURO_ID.findall(text)]
    return list(dict.fromkeys(found))


def words(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 3]


def title_in_text(title: str | None, text: str) -> bool | None:
    """Whether the start of a paper's text carries the title the archive gives it; None when there is no title."""
    want = words(title or "")
    if not want:
        return None
    have = set(words(text[:HEAD]))
    return sum(w in have for w in want) / len(want) >= 0.8


def this_dataset(target: dict) -> str:
    return f'{datasets.archive_name(target["key"]) if target.get("archive") != "dandi" else "DANDI"}:{target["id"]}'


def check(target: dict, paper: dict, text: str | None) -> dict:
    """The cheap checks on one paper, and the verdict they settle, if any."""
    row = {"doi": paper["doi"], "relation": paper.get("relation")}
    if text is None:
        return {**row, "checks": {"text": False}}
    named = archives_named(text)
    me = this_dataset(target)
    names_this = me in named or (target.get("archive") != "dandi" and target["id"].lower() in text.lower())
    others = [a for a in named if a != me]
    checks = {"text": True, "title_in_text": title_in_text(paper.get("title"), text),
              "names_this": names_this, "names_others": others}
    row["checks"] = checks
    if checks["title_in_text"] and names_this and not others:
        return {**row, "verdict": "primary", "by": "checks", "reason": f"The paper names {me} and no other dataset."}
    if checks["title_in_text"] and paper.get("relation") == "IsDescribedBy" and not named:
        return {**row, "verdict": "primary", "by": "checks",
                "reason": "The archive says the paper describes the dataset, and the paper names no dataset."}
    return row


def run_checks(target: dict, fix: dict, papers: Path, earlier: dict | None = None) -> dict:
    """A match file for a target from the cheap checks: a verdict on each paper they settle, the rest without one.
    A paper the earlier match file already has a verdict on (from the checks, the agent or a person) keeps it."""
    kept = {clean_doi(r["doi"]): r for r in (earlier or {}).get("papers", []) if r.get("verdict")}
    rows = []
    for p in listed(target, fix):
        if p["named"]:
            continue   # a person named it in triage: it is the paper
        if p["doi"] in kept:
            rows.append(kept[p["doi"]])
            continue
        text = papers / f"{slug(p['doi'])}.txt"
        rows.append(check(target, p, text.read_text(errors="replace") if text.is_file() else None))
    return {"schema_version": 1, "dataset": {"archive": target["archive"], "id": target["id"]},
            "date": datetime.date.today().isoformat(), "papers": rows}


def target_of(folder: str) -> dict:
    key = datasets.key_of_folder(folder)
    found = next((t for t in datasets.targets() if t["key"] == key), None)
    if found is None:
        raise SystemExit(f"error: dataset {datasets.label(key)} is not in the queue")
    return found


def write(folder: str, match: dict) -> Path:
    MATCH.mkdir(parents=True, exist_ok=True)
    path = MATCH / f"{folder}.yaml"
    path.write_text(f"# Whether each paper {this_dataset(target_of(folder))} names is the paper behind its data "
                    "(tools/paper_match.py, docs/pipeline.md step 1).\n"
                    + yaml.safe_dump(match, sort_keys=False, width=100, allow_unicode=True))
    return path


def validate(paths: list[Path]) -> int:
    from jsonschema import Draft202012Validator
    schema = Draft202012Validator(json.loads((ROOT / "schemas" / "paper-match.schema.json").read_text()))
    bad = 0
    for path in paths:
        data = json.loads(json.dumps(yaml.safe_load(path.read_text()), default=str))
        for err in schema.iter_errors(data):
            print(f"{path}: {'/'.join(map(str, err.path)) or '(top level)'}: {err.message}")
            bad += 1
    return 1 if bad else 0


def tally(store: Path) -> dict:
    """How the cheap checks fall over every target the store has texts for, by the archive's relation."""
    fixes, counts = triage(), {}
    for t in datasets.targets():
        if not (store / t["folder"]).is_dir():
            continue
        for row in run_checks(t, fixes.get(t["folder"], {}), store / t["folder"])["papers"]:
            rel = row.get("relation") or "(none)"
            out = "no text" if not row["checks"].get("text") else row.get("verdict") or "agent"
            counts.setdefault(rel, {}).setdefault(out, 0)
            counts[rel][out] += 1
    return counts


def main() -> int:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "checks" and len(args) == 3:
        folder = datasets.folder(datasets.parse(args[1]))
        match = run_checks(target_of(folder), triage().get(folder, {}), Path(args[2]), load(folder))
        write(folder, match)
        print("agent" if any(not r.get("verdict") for r in match["papers"]) else "done")
    elif args[0] == "status" and len(args) == 2:
        folder = datasets.folder(datasets.parse(args[1]))
        print(choose(target_of(folder), triage().get(folder, {}), load(folder))[0])
    elif args[0] == "validate" and len(args) > 1:
        return validate([Path(a) for a in args[1:]])
    elif args[0] == "tally" and len(args) == 2:
        print(yaml.safe_dump(tally(Path(args[1])), sort_keys=True))
    else:
        sys.exit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
