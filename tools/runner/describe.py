"""Text and choices for the queue runner (tools/runner).

    python tools/runner/describe.py title PAPER        # the pull request's title
    python tools/runner/describe.py body PAPER         # the pull request's description
    python tools/runner/describe.py next [SKIP ...]    # the next in the queue: a paper key, or the folder name of a
                                                       # dataset whose paper is not yet matched
    python tools/runner/describe.py next-claims [SKIP ...]
                                                       # the next dataset to read claims for
    python tools/runner/describe.py next-match [SKIP ...]
                                                       # the next dataset with no paper match on main
    python tools/runner/describe.py match FOLDER       # its paper match on main: matched, unchecked, held
                                                       # or no_match (tools/paper_match.py)
    python tools/runner/describe.py published FOLDER   # "true" when the dataset has a published version
    python tools/runner/describe.py claims-ready PAPER
                                                       # "true" when main has a claims file whose check passed
    python tools/runner/describe.py paper FOLDER       # the key of the paper main lists the dataset for, if any
    python tools/runner/describe.py folder DATASET     # a dataset's folder name (tools/datasets.py)
    python tools/runner/describe.py label FOLDER       # how the dataset is shown: DANDI:000003
    python tools/runner/describe.py deprecated PAPER   # "true" when its latest attempt is deprecated
    gh run list ... --json displayTitle,createdAt,updatedAt,status,conclusion | python tools/runner/describe.py queue [LANES CLAIMS_LANES]
                                                       # both queues, the open branches, how long a chain
                                                       # takes and how long the running ones have left, as
                                                       # JSON for the pipeline page
    gh run list ... --json databaseId,displayTitle,status | python tools/runner/describe.py run FOLDER ROLE
                                                       # "<id> <status>" of the newest run of a role, if any,
                                                       # on either account

The queue is of papers (docs/paper-first.md): a target dataset whose paper match is on main is listed for its
paper (papers/datasets/ on main), and the queue names the paper; one not yet matched is named by its folder, and
its chain makes the match first. A paper is done when an attempt on main has used each of its datasets and its
latest attempt is not deprecated: a dataset added to a paper (a second dandiset of its data) opens it again.
Papers that only reuse a dataset (targets/reuse.yaml) come after every primary target.

`title` and `body` read the latest attempt in the working tree. `next` reads main (origin/main), so
it can run from any checkout: the first published target with no attempt on main, no branch of its
own and not in SKIP, from every archive's list, taking datasets converted by CatalystNeuro first and otherwise the
lists' own order. `next-claims` chooses among the targets whose papers are all in the paper store
(papers/manifest.yaml on main) and which have no claims file on main, from the end of that order, so
that a claims-only runner and a full one running at the same time do not reach for the same dataset.
Neither takes a dataset whose paper match on main leaves it no usable paper (held or no_match). `next-match`
chooses among the published targets, attempted or not, that have no paper match on main and no branch of their
own, for a runner that only matches papers (MATCH_ONLY, run_queue.sh).
"""

from __future__ import annotations

import json
import re
import os
import subprocess
import sys
from pathlib import Path

# The clone to read; the runner runs a copy of this file from outside it.
ROOT = Path(os.environ.get("REGISTRY_ROOT") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "tools"))


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def title(paper: str) -> str:
    from agent_run import attempt_of
    import datasets
    import paper_records
    record, entry_dir = attempt_of(paper)
    m = re.match(r"^(.+?)-(\d{4})(?:-|$)", paper)
    surname, year = (m.group(1), m.group(2)) if m else (paper, "")
    surname = " ".join(w.capitalize() for w in surname.split("-"))
    repeat = "" if record["id"].endswith("-01") else " (repeat attempt)"
    data = ", ".join(datasets.label(datasets.key_of(d["archive"], str(d["id"])))
                     for d in paper_records.record_datasets(record))
    return f"{paper}: {surname} et al. {year} on {data}{repeat}"


def body(paper: str) -> str:
    from readme_row import row
    dandiset = paper
    return (f"Attempt on {paper}, run by the queue runner (`tools/runner`), which merged main into it, "
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


def claims_ready(paper: str) -> bool:
    """Whether main has the paper's claims file (claims/<paper>.yaml) and its latest check says it is ready."""
    checks = (main_yaml(f"claims/{paper}.yaml") or {}).get("checks") or [{}]
    return checks[-1].get("ready") is True


def main_blobs(prefix: str) -> dict[str, str]:
    """The text of every file under a folder on main, by path, read in one `git cat-file --batch`."""
    listed = [line.split(None, 3) for line in git("ls-tree", "-r", "origin/main", prefix).splitlines()]
    shas = [(parts[3], parts[2]) for parts in listed if len(parts) == 4 and parts[1] == "blob"]
    if not shas:
        return {}
    out = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, input="\n".join(sha for _, sha in shas) + "\n",
                         capture_output=True, text=True, check=True).stdout
    texts, pos = {}, 0
    for path, _ in shas:
        header_end = out.index("\n", pos)
        size = int(out[pos:header_end].split()[2])
        body = out[header_end + 1:header_end + 1 + size]
        texts[path] = body
        pos = header_end + 1 + size + 1
    return texts


def main_papers() -> tuple[dict[str, str], dict[str, list[str]]]:
    """From main: each dataset's paper (dataset key -> paper key, a primary paper first), and each paper's
    dataset keys, from papers/datasets/."""
    import datasets
    import yaml
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    of, listed = {}, {}
    for path, text in sorted(main_blobs("papers/datasets/").items()):
        body = yaml.load(text, Loader=loader) or {}
        paper = Path(path).stem
        keys = []
        for d in body.get("datasets") or []:
            if not d.get("available", True):
                continue
            k = datasets.key_of(d["archive"], str(d["id"]))
            keys.append(k)
            if d.get("relation", "primary") == "primary" or k not in of:
                of[k] = paper
        listed[paper] = keys
    return of, listed


def main_attempts() -> dict[str, list[dict]]:
    """From main: each paper's attempt records, oldest first, each with the dataset keys it used."""
    import datasets
    import yaml
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    out: dict[str, list[dict]] = {}
    for path, text in sorted(main_blobs("attempts/").items()):
        m = re.match(r"attempts/(.+)-(\d\d)\.yaml$", path)
        if not m:
            continue
        a = yaml.load(text, Loader=loader) or {}
        used = a.get("datasets") or ([a["dataset"]] if a.get("dataset") else [])
        out.setdefault(m.group(1), []).append({
            "id": a.get("id"), "deprecated": bool(a.get("deprecated")),
            "datasets": {datasets.key_of(d["archive"], str(d["id"])) for d in used}})
    return out


PREPRINT_SERVERS = ("10.1101/", "10.64898/", "10.48550/", "10.21203/")   # bioRxiv and medRxiv, arXiv, Research Square


def has_publication(target: dict, fix: dict) -> bool:
    """Whether a target names a paper that is not a preprint, after the hand corrections in papers/triage.yaml."""
    drop = {d.lower() for d in fix.get("not_papers", {})}
    papers = [p for p in target.get("papers", []) if p["doi"].lower() not in drop]
    return (any(not p.get("preprint") and not p["doi"].lower().startswith(PREPRINT_SERVERS) for p in papers)
            or any(not d.lower().startswith(PREPRINT_SERVERS) for d in fix.get("papers", {})))


def published(target: dict) -> bool:
    """Whether a target has a published version: a DANDI draft can still change under an attempt.
    The other archives publish every dataset they list."""
    return target.get("archive", "dandi") != "dandi" or bool(target.get("published_version"))


def main_targets() -> list[dict]:
    """Every archive's targets as main has them, each with its archive, key, id and folder."""
    import datasets
    targets = []
    for archive, spec in datasets.ARCHIVES.items():
        try:
            listed = json.loads(git("show", f"origin/main:targets/{spec['list']}"))["targets"]
        except subprocess.CalledProcessError:
            continue
        key = lambda t: datasets.key_of(archive, t.get("id") or t["dandiset"])
        targets += [{**t, "archive": archive, "id": t.get("id") or t["dandiset"], "key": key(t),
                     "folder": datasets.folder(key(t))} for t in listed]
    return targets


def matched_on_main() -> set[str]:
    """The datasets with a paper match on main, by folder name."""
    return {Path(p).stem for p in git("ls-tree", "--name-only", "origin/main", "papers/match/").split()}


def match_status(target: dict, fix: dict | None = None) -> str:
    """A target's paper match as main has it: matched, unchecked, held or no_match (tools/paper_match.py)."""
    import paper_match
    if fix is None:
        fix = (main_yaml("papers/triage.yaml") or {}).get("targets", {}).get(target["folder"], {})
    return paper_match.choose(target, fix, main_yaml(f'papers/match/{target["folder"]}.yaml'))[0]


def queue(skip: set[str] = frozenset(), claims: bool = False, match: bool = False) -> list[str]:
    """What a runner will take, in the order it will take it: paper keys, and the folder names of datasets whose
    paper is not yet matched (the module's docstring)."""
    targets = [t for t in main_targets() if published(t)]
    if match:
        done = matched_on_main() | branches() | set(skip)
        return [t["folder"] for t in sorted(targets, key=lambda t: not t.get("catalystneuro"))
                if t["folder"] not in done]
    paper_of, listed = main_papers()
    attempts = main_attempts()
    open_branches = branches()

    def unit(t: dict) -> str:
        return paper_of.get(t["key"], t["folder"])

    def done(paper: str) -> bool:
        mine = attempts.get(paper) or []
        if not mine or mine[-1]["deprecated"]:
            return False
        used = set().union(*(a["datasets"] for a in mine))
        return set(listed.get(paper) or []) <= used

    fix = (main_yaml("papers/triage.yaml") or {}).get("targets", {})
    # A dataset whose paper match leaves it no usable paper waits for a person (held) or is not to be done (no_match).
    has_match = matched_on_main()
    stuck = {t["folder"] for t in targets if t["folder"] in has_match and t["key"] not in paper_of
             and match_status(t, fix.get(t["folder"], {})) in ("held", "no_match")}
    taken = open_branches | set(skip)
    open_ = [t for t in targets if t["folder"] not in stuck and unit(t) not in taken
             and t["folder"] not in taken and not (t["key"] in paper_of and done(unit(t)))]
    if claims:
        papers = (main_yaml("papers/manifest.yaml") or {}).get("targets", {})
        read = {Path(p).stem for p in git("ls-tree", "--name-only", "origin/main", "claims/").split()
                if p.endswith(".yaml")}
        open_ = [t for t in open_ if unit(t) not in read and papers.get(t["folder"])
                 and all(p["status"] == "stored" for p in papers[t["folder"]])]
    # Datasets whose paper is published come first, so that fewer attempts rest on a preprint that is
    # published later; then ours. Python's sort is stable, so the list's order holds within each group.
    published_paper = [t for t in open_ if has_publication(t, fix.get(t["folder"], {}))]
    preprint_only = [t for t in open_ if not has_publication(t, fix.get(t["folder"], {}))]
    groups = [sorted(g, key=lambda t: not t.get("catalystneuro")) for g in (published_paper, preprint_only)]
    if claims:   # each group from its other end, so that the two runners do not meet
        groups = [g[::-1] for g in groups]
    units = [unit(t) for g in groups for t in g]
    # Papers that reuse a dataset, after every primary target (targets/reuse.yaml, listed in papers/datasets/).
    reuse = (main_yaml("targets/reuse.yaml") or {}).get("papers") or []
    for r in reuse:
        paper = r.get("key")
        if paper and paper in listed and paper not in taken and not done(paper) \
                and not (claims and paper in {Path(p).stem for p in git("ls-tree", "--name-only", "origin/main",
                                                                       "claims/").split()}):
            units.append(paper)
    return list(dict.fromkeys(units))


def as_folders(names, listed: dict[str, list[str]]) -> list[str]:
    """Queue names as dataset folder names, for the dashboard, whose rows are datasets: a paper's datasets."""
    import datasets
    out = []
    for n in names:
        out += [datasets.folder(k) for k in listed[n]] if n in listed else [n]
    return list(dict.fromkeys(out))


def next_target(skip: set[str], claims: bool = False, match: bool = False) -> str | None:
    return next(iter(queue(skip, claims, match)), None)


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
    when = lambda s: datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    by_dataset: dict[str, list] = {}
    for r in runs:
        m = re.match(r"(?:Agent|Paper) run: (\S+) (\S+)(?: \([a-z]+\))?$", r.get("displayTitle", ""))
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
    # A run on any account but the verified one carries the account's name: "(unverified)", "(api)".
    name = re.compile(rf"(?:Agent|Paper) run: {re.escape(dandiset)} {re.escape(role)}(?: \([a-z]+\))?")
    mine = [r for r in runs if name.fullmatch(r["displayTitle"])]
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
        try:
            print(datasets.label(datasets.key_of_folder(rest[0])))
        except (ValueError, KeyError):
            print(rest[0])   # a paper key
    elif command == "paper":
        import datasets
        paper_of, _ = main_papers()
        found = paper_of.get(datasets.parse(rest[0])) if not re.search(r"-\d{4}(-|$)", rest[0]) else rest[0]
        if found is None:
            return 1
        print(found)
    elif command == "deprecated":
        from agent_run import attempt_of
        found = attempt_of(rest[0])
        print("true" if found and found[0].get("deprecated") else "false")
    elif command == "queue":
        # The queues, for the dashboard's pipeline page; the runs (as for "run") come on stdin.
        lanes = dict(zip(("full", "claims"), map(int, rest or (3, 1))))
        runs, open_ = json_lists(sys.stdin.read()), branches()
        _, listed = main_papers()
        going = running(runs, open_, lanes)
        going = {f: v for name, v in going.items() for f in as_folders([name], listed)}
        print(json.dumps({"full": as_folders(queue(), listed), "claims": as_folders(queue(claims=True), listed),
                          "branches": as_folders(sorted(open_), listed),
                          "lanes": lanes, "hours": chain_hours(runs), "running": going}))
    elif command == "published":
        import datasets
        # A paper is published when each of its datasets is; a dataset not yet matched, on its own.
        _, listed = main_papers()
        keys = listed.get(rest[0]) or [datasets.key_of_folder(rest[0])]
        # From main, as the rest of the runner: the clone's working tree can be on an attempt's branch, older than
        # main, whose target lists lack datasets added since (as on 2026-11-04, when six CRCNS requests were skipped).
        by_key = {t["key"]: t for t in main_targets()}
        # A reuse paper's dataset may not be a target of any archive's list: it is published if it is listed there.
        print("true" if all((k not in by_key and rest[0] in listed) or (k in by_key and published(by_key[k]))
                            for k in keys) else "false")
    elif command == "claims-ready":
        print("true" if claims_ready(rest[0]) else "false")
    elif command == "match":
        found = next((t for t in main_targets() if t["folder"] == rest[0]), None)
        if found is None:
            raise SystemExit(f"error: {rest[0]} is not a target on main")
        print(match_status(found))
    elif command in ("next", "next-claims", "next-match"):
        found = next_target(set(rest), claims=command == "next-claims", match=command == "next-match")
        if found is None:
            return 1
        print(found)
    else:
        raise SystemExit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
