"""Move the records from dataset-first to paper-first names (docs/paper-first.md). Run once, at the cutover.

    python tools/migrate_paper_first.py --plan      # print what would move, change nothing
    python tools/migrate_paper_first.py             # move and rewrite, with git mv, in the working tree

Needs papers/keys.yaml (tools/paper_keys.py) to name every paper with records. Writes:

- papers/datasets/<key>.yaml: each paper's datasets, all `relation: primary` (the records so far are
  all on the paper's own data).
- papers/renamed.yaml: every old attempt id, entry name and record folder with its new name, for the
  site's redirects and the runner's state.

and moves, for a paper on one dataset, and for one on several (`<key>-<folder>` per dataset):

| from | to (one dataset) | to (several) |
|---|---|---|
| attempts/<old id>.yaml | attempts/<key>-NN.yaml | the same, numbered across the paper |
| entries/<old>/ | entries/<key>/ | entries/<key>-<folder>/ |
| claims/<folder>/<doi>.yaml | claims/<key>.yaml | claims/<key>/<folder>.yaml |
| questions/<folder>.yaml | questions/<key>.yaml | questions/<key>/<folder>.yaml |
| transcripts/<folder>/ | transcripts/<key>/ | transcripts/<key>/<folder>/ |
| transcripts/<folder>/paper-match*.md | transcripts/match/<folder>/ | the same |
| summaries/<old id>.md, docs/pilot-notes/<old id>.md | .../<new id>.md | the same |

Attempt records go to schema version 3 (`datasets:` for `dataset:`). Old ids and entry names are
replaced in the records, entries, summaries and pilot notes; transcripts are left as they were
written. Attempts are numbered across a paper in the order they were made.
"""

from __future__ import annotations

import argparse
import collections
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import datasets  # noqa: E402
import paper_keys  # noqa: E402

TEXT_DIRS = ("attempts", "entries", "summaries", "docs/pilot-notes", "claims", "questions")
TEXT_FILES = ("docs/pilot-notes.md",)
TEXT_SUFFIXES = {".yaml", ".yml", ".md", ".ipynb", ".py", ".txt", ".in"}


def load(path: Path):
    return yaml.safe_load(path.read_text())


def folder_of(archive: str, id_: str) -> str:
    return datasets.folder(datasets.key_of(archive, str(id_)))


def plan() -> dict:
    keys = paper_keys.read_keys()
    attempts = []
    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        a = load(path)
        attempts.append({"path": path, "id": a["id"], "date": str(a["date"]), "entry": a.get("entry"),
                         "doi": paper_keys.doi_of(a["paper"]),
                         "folder": folder_of(a["dataset"]["archive"], a["dataset"]["id"]),
                         "dataset": a["dataset"]})
    claims = {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        c = load(path)
        claims[path] = {"doi": paper_keys.doi_of(c["paper"]), "folder": path.parent.name}
    missing = sorted(({a["doi"] for a in attempts} | {c["doi"] for c in claims.values()}) - set(keys))
    if missing:
        raise SystemExit("no key for: " + ", ".join(missing) + " (run tools/paper_keys.py)")

    # The datasets of each paper, from its claims files and attempts, in the order first seen.
    folders = collections.defaultdict(list)
    for c in claims.values():
        if c["folder"] not in folders[c["doi"]]:
            folders[c["doi"]].append(c["folder"])
    for a in attempts:
        if a["folder"] not in folders[a["doi"]]:
            folders[a["doi"]].append(a["folder"])
    several = {doi for doi, f in folders.items() if len(f) > 1}

    def scoped(doi: str, folder: str) -> str:
        return f"{keys[doi]}-{folder}" if doi in several else keys[doi]

    moves: list[tuple[str, str]] = []
    ids, entries = {}, {}
    by_paper = collections.defaultdict(list)
    for a in attempts:
        by_paper[a["doi"]].append(a)
    for doi, mine in by_paper.items():
        for n, a in enumerate(sorted(mine, key=lambda a: (a["date"], a["id"])), 1):
            ids[a["id"]] = f"{keys[doi]}-{n:02d}"
            if a["entry"]:
                entries.setdefault(a["entry"], scoped(doi, a["folder"]))
    for old_id, new_id in ids.items():
        moves.append((f"attempts/{old_id}.yaml", f"attempts/{new_id}.yaml"))
        for d in ("summaries", "docs/pilot-notes"):
            if (ROOT / d / f"{old_id}.md").is_file():
                moves.append((f"{d}/{old_id}.md", f"{d}/{new_id}.md"))
    for old, new in entries.items():
        if (ROOT / "entries" / old).is_dir():
            moves.append((f"entries/{old}", f"entries/{new}"))
    folder_paper = {}   # record folder -> the paper its claims, questions and transcripts belong to
    for path, c in claims.items():
        doi, folder = c["doi"], c["folder"]
        folder_paper[folder] = doi
        new = f"claims/{keys[doi]}/{folder}.yaml" if doi in several else f"claims/{keys[doi]}.yaml"
        moves.append((path.relative_to(ROOT).as_posix(), new))
    for a in attempts:
        folder_paper.setdefault(a["folder"], a["doi"])
    for folder, doi in sorted(folder_paper.items()):
        q = ROOT / "questions" / f"{folder}.yaml"
        if q.is_file():
            moves.append((f"questions/{folder}.yaml",
                          f"questions/{keys[doi]}/{folder}.yaml" if doi in several else f"questions/{keys[doi]}.yaml"))
    for t in sorted(p for p in (ROOT / "transcripts").iterdir() if p.is_dir()):
        folder = t.name
        for f in sorted(t.glob("paper-match*.md")):
            moves.append((f.relative_to(ROOT).as_posix(), f"transcripts/match/{folder}/{f.name}"))
        doi = folder_paper.get(folder)
        if doi is None:
            continue   # a dataset with only a paper match: nothing else to move
        dest = f"transcripts/{keys[doi]}/{folder}" if doi in several else f"transcripts/{keys[doi]}"
        for f in sorted(t.rglob("*")):
            if f.is_file() and not f.name.startswith("paper-match"):
                rel = f.relative_to(t).as_posix()
                # An archived attempt's folder is numbered by the dataset's attempts; renumber it by the paper's.
                m = re.match(r"attempt-(\d\d)/(.*)", rel)
                if m:
                    old_id = next((a["id"] for a in attempts if a["folder"] == folder
                                   and a["id"].endswith("-" + m.group(1))), None)
                    if old_id:
                        rel = f"attempt-{ids[old_id].rsplit('-', 1)[1]}/{m.group(2)}"
                moves.append((f.relative_to(ROOT).as_posix(), f"{dest}/{rel}"))

    paper_datasets = {}
    for doi, fs in folders.items():
        items = []
        for folder in fs:
            key = datasets.key_of_folder(folder)
            archive, id_ = datasets.split_key(key)
            items.append({"archive": archive, "id": id_, "relation": "primary"})
        paper_datasets[keys[doi]] = {"paper": f"doi:{doi}", "datasets": items}
    targets = [b for _, b in moves]
    dup = [t for t, n in collections.Counter(targets).items() if n > 1]
    if dup:
        raise SystemExit("two records would move to the same path: " + ", ".join(dup[:10]))
    return {"moves": moves, "ids": ids, "entries": entries, "several": sorted(keys[d] for d in several),
            "folder_paper": {f: keys[d] for f, d in folder_paper.items()}, "paper_datasets": paper_datasets,
            "attempts": attempts}


def rename_pattern(names: dict[str, str]) -> re.Pattern:
    alternation = "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True))
    return re.compile(rf"(?<![\w-])(?:{alternation})(?![\w])")


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=ROOT, check=True)


def apply(p: dict) -> None:
    for src, dst in p["moves"]:
        (ROOT / dst).parent.mkdir(parents=True, exist_ok=True)
        git("mv", src, dst)
    names = {**p["entries"], **p["ids"]}
    pattern = rename_pattern(names)
    files = [f for d in TEXT_DIRS for f in (ROOT / d).rglob("*") if f.is_file() and f.suffix in TEXT_SUFFIXES]
    files += [ROOT / f for f in TEXT_FILES if (ROOT / f).is_file()]
    for f in files:
        text = f.read_text()
        new = pattern.sub(lambda m: names[m.group(0)], text)
        if new != text:
            f.write_text(new)
    # Attempt records: schema 3, the dataset as a one-item list.
    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        text = path.read_text()
        a = yaml.safe_load(text)
        if a.get("schema_version") == 3:
            continue
        m = re.search(r"^dataset:\n((?:  .*\n)+)", text, re.M)
        if not m:
            raise SystemExit(f"{path}: no dataset block")
        block = "".join("    " + line[2:] + "\n" if i else "- " + line[2:] + "\n"
                        for i, line in enumerate(m.group(1).splitlines()))
        block = block.replace("\n- ", "\n- ", 1)
        items = [line for line in m.group(1).splitlines()]
        listed = "datasets:\n" + "".join(("- " if i == 0 else "  ") + line.strip() + "\n" for i, line in enumerate(items))
        listed += "  relation: primary\n"
        text = text[:m.start()] + listed + text[m.end():]
        text = re.sub(r"^schema_version: 2$", "schema_version: 3", text, count=1, flags=re.M)
        if yaml.safe_load(text)["datasets"][0]["id"] != a["dataset"]["id"]:
            raise SystemExit(f"{path}: the dataset did not convert")
        path.write_text(text)
    out = ROOT / "papers" / "datasets"
    out.mkdir(parents=True, exist_ok=True)
    for key, body in sorted(p["paper_datasets"].items()):
        (out / f"{key}.yaml").write_text(
            "# The datasets this paper is tested on (docs/paper-first.md).\n"
            + yaml.safe_dump({"schema_version": 1, **body}, sort_keys=False, width=100))
    (ROOT / "papers" / "renamed.yaml").write_text(
        "# Old names and the paper-first names they moved to, at the cutover (tools/migrate_paper_first.py).\n"
        "# The site redirects old pages with it; nothing else should need it.\n"
        + yaml.safe_dump({"schema_version": 1, "attempts": p["ids"], "entries": p["entries"],
                          "folders": p["folder_paper"]}, sort_keys=True, width=100))
    git("add", "-A", "attempts", "entries", "claims", "questions", "transcripts", "summaries", "docs", "papers")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    p = plan()
    if args.plan:
        for src, dst in p["moves"]:
            print(f"{src} -> {dst}")
        print(f"\n{len(p['moves'])} moves; {len(p['ids'])} attempts, {len(p['entries'])} entries; "
              f"{len(p['paper_datasets'])} papers, {len(p['several'])} on several datasets: {', '.join(p['several'])}",
              file=sys.stderr)
        return 0
    apply(p)
    print(f"moved {len(p['moves'])} paths; review with git status, then commit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
