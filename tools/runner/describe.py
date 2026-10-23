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
    gh run list ... --json displayTitle,createdAt,updatedAt,status,conclusion | python tools/runner/describe.py queue [LANES CLAIMS_LANES]
                                                       # both queues, the open branches, how long a chain
                                                       # takes and how long the running ones have left, as
                                                       # JSON for the pipeline page
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
    return (f"Attempt on {dandiset}, run by the queue runner (`tools/runner`), which merged main into it, "
            "had the recorder run add the pilot notes, and merges it once the checks "
            f"pass.\n\n{row(dandiset)}\n\nThe outcomes, the verification rounds and the findings are in the "
            "attempt record; the summary is in docs/pilot-notes/.\n\n"
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


def queue(skip: set[str] = frozenset(), claims: bool = False) -> list[str]:
    """The datasets a runner will take, by folder name, in the order it will take them."""
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
    # An attempt record is named <folder>-<first author>-<year>-<nn>.yaml. A dataset whose latest attempt
    # is deprecated is to be done again (its claims too, see chain.sh), so it is open.
    attempted = {t["folder"] for t in targets if any(r.startswith(t["folder"] + "-") for r in records)}
    attempted -= {f for f in attempted if latest_deprecated(f, records)}
    taken = attempted | branches() | set(skip)
    open_ = [t for t in targets if t["folder"] not in taken]
    if claims:
        papers = (main_yaml("papers/manifest.yaml") or {}).get("targets", {})
        read = {Path(p).name for p in git("ls-tree", "--name-only", "origin/main", "claims/").split()}
        open_ = [t for t in open_ if t["folder"] not in read and papers.get(t["folder"])
                 and all(p["status"] == "stored" for p in papers[t["folder"]])]
    # Datasets whose paper is published come first, so that fewer attempts rest on a preprint that is
    # published later; then ours. Python's sort is stable, so the list's order holds within each group.
    fix = (main_yaml("papers/triage.yaml") or {}).get("targets", {})
    published_paper = [t for t in open_ if has_publication(t, fix.get(t["folder"], {}))]
    preprint_only = [t for t in open_ if not has_publication(t, fix.get(t["folder"], {}))]
    groups = [sorted(g, key=lambda t: not t.get("catalystneuro")) for g in (published_paper, preprint_only)]
    if claims:   # each group from its other end, so that the two runners do not meet
        groups = [g[::-1] for g in groups]
    return [t["folder"] for g in groups for t in g]


def next_target(skip: set[str], claims: bool = False) -> str | None:
    return next(iter(queue(skip, claims)), None)


def branches() -> set[str]:
    """The datasets with an attempt branch that is not merged into main: an attempt going on, or one stopped
    for a person. A merged branch is left behind by an earlier attempt and is deleted when the next one
    starts (chain.sh), so it does not hold its dataset back."""
    git("fetch", "-q", "origin", "+refs/heads/attempt/*:refs/remotes/origin/attempt/*")
    merged = {b.strip() for b in git("branch", "-r", "--merged", "origin/main", "--list", "origin/attempt/*").split("\n")}
    return {line.split("refs/heads/attempt/", 1)[1] for line in git("ls-remote", "--heads", "origin",
                                                                    "attempt/*").split("\n")
            if line and "origin/attempt/" + line.split("refs/heads/attempt/", 1)[1] not in merged}


def json_lists(text: str) -> list:
    """The items of one or more JSON lists written one after another, as two `gh run list` calls write them."""
    decoder, items, text = json.JSONDecoder(), [], text.strip()
    while text:
        found, end = decoder.raw_decode(text)
        items += found
        text = text[end:].strip()
    return items


def chains(runs: list[dict]) -> dict[str, list[list[tuple]]]:
    """Each dataset's agent runs (gh run list --json displayTitle,createdAt,updatedAt,status,conclusion), split
    into chains: runs more than three hours apart belong to different chains. A run is (start, end, role,
    conclusion, status)."""
    import datetime
    import re
    when = lambda s: datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    by_dataset: dict[str, list] = {}
    for r in runs:
        m = re.match(r"(?:Agent|Paper) run: (\S+) (\S+)(?: \(unverified\))?$", r.get("displayTitle", ""))
        if m:
            by_dataset.setdefault(m.group(1), []).append((when(r["createdAt"]), when(r["updatedAt"]), m.group(2),
                                                          r.get("conclusion"), r.get("status", "completed")))
    out = {}
    for dataset, found in by_dataset.items():
        found.sort()
        out[dataset] = [[found[0]]]
        for run in found[1:]:
            if (run[0] - max(x[1] for x in out[dataset][-1])).total_seconds() > 3 * 3600:
                out[dataset].append([])
            out[dataset][-1].append(run)
    return out


def chain_kind(chain: list[tuple]) -> str | None:
    """"full" for a finished attempt (author to recorder), "claims" for a claims-only chain, else None."""
    roles = {x[2] for x in chain if x[3] == "success"}
    if {"author", "recorder"} <= roles:
        return "full"
    if {"claims", "claims-check"} <= roles and "author" not in roles:
        return "claims"
    return None


def chain_hours(runs: list[dict]) -> dict[str, float | None]:
    """How long a chain takes, from the agent runs: the median time from a dataset's first run to its last,
    for full attempts (author to recorder) and for claims-only chains."""
    import statistics
    found = {"full": [], "claims": []}
    for chain in (c for cs in chains(runs).values() for c in cs):
        kind = chain_kind(chain)
        if kind:
            found[kind].append((max(x[1] for x in chain) - min(x[0] for x in chain)).total_seconds() / 3600)
    return {k: statistics.median(v) if v else None for k, v in found.items()}


def running(runs: list[dict], folders: set[str], lanes: dict[str, int], now=None) -> dict[str, dict]:
    """The chains going now on these datasets (a run of theirs is queued or in progress), with the runner
    each is on and about how many hours it has left: the median time, in finished chains of its kind, from
    the start of a run of the role it is on to the chain's end, less the time that run has taken so far.

    A chain on any role past the claims check is the full runner's. One that has only read claims so far
    could be either runner's; it is taken to be the claims runner's when the full runner's lanes are taken."""
    import datetime
    import statistics
    now = now or datetime.datetime.now(datetime.timezone.utc)
    done = {k: v for k, v in chain_hours(runs).items() if v}
    after: dict[tuple, list] = {}   # (kind, role) -> hours from that role's start to the chain's end
    for chain in (c for cs in chains(runs).values() for c in cs):
        kind = chain_kind(chain)
        if kind:
            end = max(x[1] for x in chain)
            for x in chain:
                if x[3] == "success":
                    after.setdefault((kind, x[2]), []).append((end - x[0]).total_seconds() / 3600)
    going = {}
    for d, cs in chains(runs).items():
        current = [x for x in cs[-1] if x[4] in ("queued", "in_progress")]
        if d in folders and current:
            going[d] = (cs[-1], current[-1])
    past_claims = lambda chain: any(x[2] not in ("claims", "claims-check") for x in chain)
    full = sum(1 for chain, _ in going.values() if past_claims(chain))
    out = {}
    for d, (chain, run) in sorted(going.items(), key=lambda kv: kv[1][1][0]):
        if past_claims(chain) or full < lanes.get("full", 3):
            kind = "full"
            full += not past_claims(chain)
        else:
            kind = "claims"
        hours = None
        if after.get((kind, run[2])):
            hours = statistics.median(after[(kind, run[2])]) - (now - run[0]).total_seconds() / 3600
        elif kind in done:
            hours = done[kind] - (now - min(x[0] for x in chain)).total_seconds() / 3600
        out[d] = {"kind": kind, "hours": None if hours is None else max(hours, 0.0)}
    return out


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
    elif command == "queue":
        # The queues, for the dashboard's pipeline page; the runs (as for "run") come on stdin.
        lanes = dict(zip(("full", "claims"), map(int, rest or (3, 1))))
        runs, open_ = json_lists(sys.stdin.read()), branches()
        print(json.dumps({"full": queue(), "claims": queue(claims=True), "branches": sorted(open_),
                          "lanes": lanes, "hours": chain_hours(runs), "running": running(runs, open_, lanes)}))
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
