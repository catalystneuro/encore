"""Text and choices for the queue runner (tools/runner).

    python tools/runner/describe.py title DANDISET     # the pull request's title
    python tools/runner/describe.py body DANDISET      # the pull request's description
    python tools/runner/describe.py next [SKIP ...]    # the next dandiset in the queue
    gh run list ... --json databaseId,displayTitle,status | python tools/runner/describe.py run DANDISET ROLE
                                                       # "<id> <status>" of the newest run of a role, if any

`title` and `body` read the latest attempt in the working tree. `next` reads main (origin/main), so
it can run from any checkout: the first target with no attempt on main, no branch of its own and not
in SKIP, taking dandisets converted by CatalystNeuro first and otherwise the queue's own order.
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
    _, surname, year = entry_dir.name.split("-", 2)
    repeat = "" if record["id"].endswith("-01") else " (repeat attempt)"
    return f"{dandiset}: {surname.capitalize()} et al. {year}{repeat}"


def body(dandiset: str) -> str:
    from readme_row import row
    return (f"Attempt on {dandiset}, run by the queue runner (`tools/runner`), which rebased it on main, "
            "had the recorder run add the README row and the pilot notes, and merges it once the checks "
            f"pass.\n\n{row(dandiset)}\n\nThe outcomes, the verification rounds and the findings are in the "
            "attempt record; the summary is in docs/pilot-notes.md.\n\n"
            "🤖 Generated with [Claude Code](https://claude.com/claude-code)\n")


def next_target(skip: set[str]) -> str | None:
    targets = json.loads(git("show", "origin/main:targets/dandisets.json"))["targets"]
    attempted = {Path(p).name.split("-", 1)[0] for p in git("ls-tree", "--name-only", "origin/main",
                                                             "attempts/").split()}
    branches = {line.rsplit("/", 1)[1] for line in git("ls-remote", "--heads", "origin", "attempt/*").split("\n")
                if line}
    open_ = [t["dandiset"] for t in targets
             if t["dandiset"] not in attempted | branches | skip]
    ours = [d for d in open_ if next(t for t in targets if t["dandiset"] == d).get("catalystneuro")]
    return (ours or open_ or [None])[0]


def newest_run(runs: list[dict], dandiset: str, role: str) -> str:
    """The id and status of the newest run of a role on a dandiset, or "" when there is none."""
    mine = [r for r in runs if r["displayTitle"] == f"Agent run: {dandiset} {role}"]
    return f'{mine[0]["databaseId"]} {mine[0]["status"]}' if mine else ""


def main() -> int:
    command, *rest = sys.argv[1:]
    if command == "title":
        print(title(rest[0]))
    elif command == "body":
        print(body(rest[0]))
    elif command == "run":
        print(newest_run(json.load(sys.stdin), *rest))
    elif command == "next":
        found = next_target(set(rest))
        if found is None:
            return 1
        print(found)
    else:
        raise SystemExit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
