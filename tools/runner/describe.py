"""Text and choices for the queue runner (tools/runner).

    python tools/runner/describe.py title FOLDER       # the pull request's title
    python tools/runner/describe.py body FOLDER        # the pull request's description
    python tools/runner/describe.py next [SKIP ...]    # the next dataset in the queue, by folder name
    python tools/runner/describe.py next-claims [SKIP ...]
                                                       # the next dataset to read claims for
    python tools/runner/describe.py published FOLDER   # "true" when the dataset has a published version
    python tools/runner/describe.py claims-ready FOLDER
                                                       # "true" when main has a claims file whose check passed
    python tools/runner/describe.py folder DATASET     # a dataset's folder name (tools/datasets.py)
    python tools/runner/describe.py label FOLDER       # how the dataset is shown: DANDI:000003
    python tools/runner/describe.py deprecated FOLDER  # "true" when its latest attempt is deprecated
    gh run list ... --json databaseId,displayTitle,status | python tools/runner/describe.py run FOLDER ROLE
                                                       # "<id> <status>" of the newest run of a role, if any,
                                                       # on either account

`title` and `body` read the latest attempt in the working tree. `next` reads main (origin/main), so
it can run from any checkout: the first published target with no attempt on main, no branch of its
own and not in SKIP, from every archive's list, taking datasets converted by CatalystNeuro first and otherwise the
lists' own order. `next-claims` chooses among the targets whose papers are all in the paper store
(papers/manifest.yaml on main) and which have no claims file on main, from the end of that order, so
that a claims-only runner and a full one running at the same time do not reach for the same dataset.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

# The clone to read; the runner runs a copy of this file from outside it.
ROOT = Path(os.environ.get("REGISTRY_ROOT") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "tools"))


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def title(dandiset: str) -> str:
    from agent_run import attempt_of
    record, entry_dir = attempt_of(dandiset)
    _, surname, year = entry_dir.name.rsplit("-", 2)
    repeat = "" if record["id"].endswith("-01") else " (repeat attempt)"
    return f"{dandiset}: {surname.capitalize()} et al. {year}{repeat}"


def body(dandiset: str) -> str:
    from readme_row import row
    return (f"Attempt on {dandiset}, run by the queue runner (`tools/runner`), which rebased it on main, "
            "had the recorder run add the README row and the pilot notes, and merges it once the checks "
            f"pass.\n\n{row(dandiset)}\n\nThe outcomes, the verification rounds and the findings are in the "
            "attempt record; the summary is in docs/pilot-notes.md.\n\n"
            "🤖 Generated with [Claude Code](https://claude.com/claude-code)\n")


def main_yaml(path: str):
    import yaml
    try:
        return yaml.safe_load(git("show", f"origin/main:{path}"))
    except subprocess.CalledProcessError:
        return None


def claims_ready(folder: str) -> bool:
    """Whether main has a claims file for the dataset whose latest check says it is ready."""
    for path in git("ls-tree", "--name-only", "origin/main", f"claims/{folder}/").split():
        checks = (main_yaml(path) or {}).get("checks") or [{}]
        if checks[-1].get("ready") is True:
            return True
    return False


PREPRINT_SERVERS = ("10.1101/", "10.64898/", "10.48550/", "10.21203/")   # bioRxiv and medRxiv, arXiv, Research Square


def has_publication(target: dict, fix: dict) -> bool:
    """Whether a target names a paper that is not a preprint, after the hand corrections in papers/triage.yaml."""
    drop = {d.lower() for d in fix.get("not_papers", {})}
    papers = [p for p in target.get("papers", []) if p["doi"].lower() not in drop]
    return (any(not p.get("preprint") and not p["doi"].lower().startswith(PREPRINT_SERVERS) for p in papers)
            or any(not d.lower().startswith(PREPRINT_SERVERS) for d in fix.get("papers", {})))


def latest_deprecated(folder: str, records: list[str]) -> bool:
    """Whether the newest attempt record of a dataset is deprecated, so that it is to be done again."""
    mine = sorted(r for r in records if r.startswith(folder + "-") and r.endswith(".yaml"))
    return bool(mine) and bool((main_yaml(f"attempts/{mine[-1]}") or {}).get("deprecated"))


def published(target: dict) -> bool:
    """Whether a target has a published version: a DANDI draft can still change under an attempt.
    The other archives publish every dataset they list."""
    return target.get("archive", "dandi") != "dandi" or bool(target.get("published_version"))


def next_target(skip: set[str], claims: bool = False) -> str | None:
    import datasets
    targets = []
    for archive, spec in datasets.ARCHIVES.items():
        try:
            listed = json.loads(git("show", f"origin/main:targets/{spec['list']}"))["targets"]
        except subprocess.CalledProcessError:
            continue
        targets += [{**t, "archive": archive,
                     "folder": datasets.folder(datasets.key_of(archive, t.get("id") or t["dandiset"]))}
                    for t in listed]
    targets = [t for t in targets if published(t)]
    records = [Path(p).name for p in git("ls-tree", "--name-only", "origin/main", "attempts/").split()]
    branches = {line.split("refs/heads/attempt/", 1)[1] for line in git("ls-remote", "--heads", "origin",
                                                                          "attempt/*").split("\n") if line}
    # An attempt record is named <folder>-<first author>-<year>-<nn>.yaml. A dataset whose latest attempt
    # is deprecated is to be done again (its claims too, see chain.sh), so it is open.
    attempted = {t["folder"] for t in targets if any(r.startswith(t["folder"] + "-") for r in records)}
    attempted -= {f for f in attempted if latest_deprecated(f, records)}
    open_ = [t for t in targets if t["folder"] not in attempted | branches | skip]
    if claims:
        papers = (main_yaml("papers/manifest.yaml") or {}).get("targets", {})
        read = {Path(p).name for p in git("ls-tree", "--name-only", "origin/main", "claims/").split()}
        open_ = [t for t in open_ if t["folder"] not in read and papers.get(t["folder"])
                 and all(p["status"] == "stored" for p in papers[t["folder"]])]
    # Datasets whose paper is published come first, so that fewer attempts rest on a preprint that is
    # published later; then ours. Python's sort is stable, so the list's order holds within each group.
    fix = (main_yaml("papers/triage.yaml") or {}).get("targets", {})
    order = sorted(open_, key=lambda t: (not has_publication(t, fix.get(t["folder"], {})), not t.get("catalystneuro")))
    if not order:
        return None
    if claims:   # from the other end of the same group as the full runner, so the two do not meet
        return [t for t in order if has_publication(t, fix.get(t["folder"], {})) == has_publication(
            order[0], fix.get(order[0]["folder"], {}))][-1]["folder"]
    return order[0]["folder"]


def newest_run(runs: list[dict], dandiset: str, role: str) -> str:
    """The id and status of the newest run of a role on a dandiset, or "" when there is none."""
    names = {f"{kind}: {dandiset} {role}{account}" for kind in ("Agent run", "Paper run") for account in ("", " (unverified)")}
    mine = [r for r in runs if r["displayTitle"] in names]
    return f'{mine[0]["databaseId"]} {mine[0]["status"]}' if mine else ""


def main() -> int:
    command, *rest = sys.argv[1:]
    if command == "title":
        print(title(rest[0]))
    elif command == "body":
        print(body(rest[0]))
    elif command == "run":
        print(newest_run(json.load(sys.stdin), *rest))
    elif command == "folder":
        import datasets
        try:
            print(datasets.folder(datasets.parse(rest[0])))
        except ValueError as err:
            raise SystemExit(f"error: {err}")
    elif command == "label":
        import datasets
        print(datasets.label(datasets.key_of_folder(rest[0])))
    elif command == "deprecated":
        from agent_run import attempt_of
        found = attempt_of(rest[0])
        print("true" if found and found[0].get("deprecated") else "false")
    elif command == "published":
        import datasets
        key = datasets.key_of_folder(rest[0])
        found = next((t for t in datasets.targets() if t["key"] == key), None)
        print("true" if found and published(found) else "false")
    elif command == "claims-ready":
        print("true" if claims_ready(rest[0]) else "false")
    elif command in ("next", "next-claims"):
        found = next_target(set(rest), claims=command == "next-claims")
        if found is None:
            return 1
        print(found)
    else:
        raise SystemExit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
