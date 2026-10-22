"""The run queue: requests for attempts, made as issues from the "Request a run" form (docs/queue.md).

    python tools/runner/run_requests.py check NUMBER          # validate a request and label its state
    python tools/runner/run_requests.py sweep                 # check every open request that has no state yet
    python tools/runner/run_requests.py board                 # rewrite the queue-board issue
    python tools/runner/run_requests.py next                  # take the next request: "FOLDER [VERSION]"
    python tools/runner/run_requests.py finish FOLDER STATUS  # report a chain's last line on its request
    python tools/runner/run_requests.py order                 # the queued requests, in order, as JSON

A request's state is its label: `awaiting-approval`, `queued`, `running`, `needs-you`, or `invalid`;
a request that merged is closed. `check` runs in .github/workflows/run-requests.yml on every change
to a request; `next` and `finish` run in the queue runner (tools/runner/run_queue.sh), which takes
requests after the items in its queue.txt and before the targets it chooses itself.

Who may steer the queue is queue/priority.yaml on main: their requests need no approval, and only
their `approved` and `priority` labels count; any other is taken off. Queued requests run with
priority first, then oldest first. The form's text is untrusted: `next` re-reads and re-validates
it, and passes the runner only a dataset and a version that match a strict pattern.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

# The clone to read; the runner runs a copy of this file from outside it.
ROOT = Path(os.environ.get("REGISTRY_ROOT") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "tools"))

import datasets  # noqa: E402

REPO = os.environ.get("GITHUB_REPOSITORY", "catalystneuro/encore")
SERVER = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
KIND = "run-request"
STATES = ["awaiting-approval", "queued", "running", "needs-you", "invalid"]
BOARD = "queue-board"
VERSION = re.compile(r"0\.[0-9]{6}\.[0-9]{4}")


def gh(*args: str, input: str | None = None) -> str:
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True, input=input).stdout


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def allowed() -> set[str]:
    """The users in queue/priority.yaml, read from main so that a branch cannot widen the list."""
    try:
        text = git("show", "origin/main:queue/priority.yaml")
    except subprocess.CalledProcessError:
        text = (ROOT / "queue" / "priority.yaml").read_text()
    return {u.lower() for u in (yaml.safe_load(text) or {}).get("priority") or []}


def form(body: str) -> dict[str, str]:
    """The answers of an issue form, by the label of each field."""
    fields, name = {}, None
    for line in (body or "").splitlines():
        if line.startswith("### "):
            name = line[4:].strip()
            fields[name] = ""
        elif name is not None:
            fields[name] += line + "\n"
    return {k: ("" if v.strip() == "_No response_" else v.strip()) for k, v in fields.items()}


def request(body: str) -> tuple[str, str, list[str]]:
    """A request's dataset folder and version ("" for one the author chooses), and what is wrong with it."""
    answers, problems = form(body), []
    folder = version = ""
    try:
        folder = datasets.folder(datasets.parse(answers.get("Dataset", "").splitlines()[0] if answers.get("Dataset") else ""))
    except ValueError:
        problems.append(f"`{answers.get('Dataset', '')[:40]}` is not a dataset: give a DANDI id (000147) or <archive>:<id>.")
    choice = answers.get("Version", "")
    if choice == "draft":
        version = "draft"
    elif choice == "the published version below":
        version = answers.get("Published version", "").strip()
        if not VERSION.fullmatch(version):
            problems.append(f"`{version[:40]}` is not a published version id (such as 0.260521.2201).")
            version = ""
    elif choice != "latest published":
        problems.append("Choose a version.")
    if folder and not re.fullmatch(r"[A-Za-z0-9._-]+", folder):
        problems.append("The dataset's folder name has characters the runner does not take.")
    return folder, version, problems


def last_labeler(events: list[dict], label: str) -> str | None:
    """Who added a label most recently, when it is still on: None when it was taken off since."""
    who = None
    for e in events:
        if (e.get("label") or {}).get("name") != label:
            continue
        if e.get("event") == "labeled":
            who = (e.get("actor") or {}).get("login")
        elif e.get("event") == "unlabeled":
            who = None
    return who


def state(issue: dict, events: list[dict], steer: set[str]) -> tuple[str, list[str], list[str]]:
    """A request's state, the steering labels to take off (added by someone not in the list), and notes."""
    labels = {lab["name"] for lab in issue.get("labels", [])}
    drop, notes = [], []
    for lab in ("approved", "priority"):
        if lab in labels and (last_labeler(events, lab) or "").lower() not in steer:
            drop.append(lab)
            notes.append(f"The `{lab}` label counts only when someone in queue/priority.yaml adds it; it was taken off.")
    folder, version, problems = request(issue.get("body", ""))
    if problems:
        return "invalid", drop, problems
    for kept in ("running", "needs-you"):
        if kept in labels:
            return kept, drop, notes
    author = ((issue.get("author") or issue.get("user") or {}).get("login") or "").lower()
    if author in steer or ("approved" in labels and "approved" not in drop):
        return "queued", drop, notes
    return "awaiting-approval", drop, notes


def order(issues: list[dict]) -> list[dict]:
    """Queued requests in the order they run: priority first, then oldest first."""
    queued = [i for i in issues if any(lab["name"] == "queued" for lab in i.get("labels", []))]
    return sorted(queued, key=lambda i: (not any(lab["name"] == "priority" for lab in i.get("labels", [])),
                                         i.get("createdAt", ""), i.get("number", 0)))


def open_requests() -> list[dict]:
    return json.loads(gh("issue", "list", "--repo", REPO, "--label", KIND, "--state", "open", "--limit", "500",
                         "--json", "number,title,body,labels,author,createdAt,url"))


def events_of(number: int) -> list[dict]:
    return json.loads(gh("api", "--paginate", f"repos/{REPO}/issues/{number}/events")) or []


def set_state(number: int, new: str, have: set[str], drop: list[str] = ()) -> None:
    remove = [s for s in STATES if s in have and s != new] + [d for d in drop if d in have]
    args = ["issue", "edit", str(number), "--repo", REPO, "--add-label", new]
    for lab in remove:
        args += ["--remove-label", lab]
    gh(*args)


def comment(number: int, text: str) -> None:
    gh("issue", "comment", str(number), "--repo", REPO, "--body-file", "-", input=text)


def check(number: int) -> None:
    issue = json.loads(gh("issue", "view", str(number), "--repo", REPO, "--json", "number,body,labels,author,state"))
    if issue["state"] != "OPEN":
        return
    have = {lab["name"] for lab in issue["labels"]}
    new, drop, notes = state(issue, events_of(number), allowed())
    if new == "invalid":
        notes = ["This request cannot be queued yet:", *[f"- {n}" for n in notes], "", "Edit the request to fix it."]
    elif new == "awaiting-approval" and "awaiting-approval" not in have:
        notes.append("Waiting for someone in queue/priority.yaml to approve it with the `approved` label.")
    elif new == "queued" and "queued" not in have:
        place = next((k for k, i in enumerate(order(open_requests()), 1) if i["number"] == number), None)
        notes.append(f"Queued{f', number {place} in line' if place else ''}. The runner comments here when it starts.")
    if new not in have or any(d in have for d in drop):
        set_state(number, new, have, drop)
    if notes:
        comment(number, "\n".join(notes))


def sweep() -> None:
    """Check every open request without a state label. The workflow's runs share one concurrency group, in which
    GitHub keeps only one waiting run and cancels the rest, so requests opened together can miss their check."""
    for issue in open_requests():
        if not {lab["name"] for lab in issue["labels"]} & set(STATES):
            check(issue["number"])


def board() -> None:
    """Rewrite the queue-board issue: what runs now, and the queued requests in order."""
    issues = open_requests()
    running = [i for i in issues if any(lab["name"] == "running" for lab in i["labels"])]
    rows = ["| | Request | Dataset | Version | Asked by |", "|---|---|---|---|---|"]
    for k, i in enumerate(order(issues), 1):
        folder, version, _ = request(i["body"])
        star = " (priority)" if any(lab["name"] == "priority" for lab in i["labels"]) else ""
        rows.append(f"| {k}{star} | #{i['number']} | {folder} | {version or 'latest published'} | @{i['author']['login']} |")
    waiting = [f"#{i['number']}" for i in issues if any(lab["name"] == "awaiting-approval" for lab in i["labels"])]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    text = "\n".join([
        f"The run queue, as of {now}. It is rewritten whenever a request changes; how it works is in docs/queue.md.",
        "", "**Running:** " + (", ".join(f"#{i['number']} ({request(i['body'])[0]})" for i in running) or "none"),
        "", "**Queued, in the order they will run:**", "", *(rows if len(rows) > 2 else ["None."]),
        "", "**Waiting for approval:** " + (", ".join(waiting) or "none"),
        "", f"[Request a run]({SERVER}/{REPO}/issues/new?template=run-request.yml)"])
    found = json.loads(gh("issue", "list", "--repo", REPO, "--label", BOARD, "--state", "open", "--json", "number"))
    if found:
        gh("issue", "edit", str(found[0]["number"]), "--repo", REPO, "--body-file", "-", input=text)
    else:
        gh("issue", "create", "--repo", REPO, "--title", "Run queue", "--label", BOARD, "--body-file", "-", input=text)


def next_request() -> str:
    """Mark the first queued request running and return its "FOLDER [VERSION]", re-validated; "" when none."""
    steer = allowed()
    for issue in order(open_requests()):
        new, _, _ = state(issue, events_of(issue["number"]), steer)
        if new != "queued":
            continue
        folder, version, _ = request(issue["body"])
        set_state(issue["number"], "running", {lab["name"] for lab in issue["labels"]})
        comment(issue["number"], f"Started {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC on `{folder}`"
                                 f"{f' ({version})' if version else ''}. The runner comments here when the attempt ends.")
        return f"{folder} {version}".strip()
    return ""


def finish(folder: str, status: str) -> None:
    """Report a chain's last line on the running request for this dataset: close it on a merge."""
    for issue in open_requests():
        if not any(lab["name"] == "running" for lab in issue["labels"]) or request(issue["body"])[0] != folder:
            continue
        have = {lab["name"] for lab in issue["labels"]}
        if " MERGED " in f" {status} ":
            comment(issue["number"], f"Done: {status}")
            gh("issue", "edit", str(issue["number"]), "--repo", REPO, "--remove-label", "running")
            gh("issue", "close", str(issue["number"]), "--repo", REPO)
        else:
            set_state(issue["number"], "needs-you", have)
            comment(issue["number"], f"The attempt stopped: `{status}`.\n\nThe dataset's `needs-you` issue has "
                                     "the details. To run it again once that is sorted, swap `needs-you` for `queued`.")


def main(argv: list[str]) -> int:
    cmd, *rest = argv or ["help"]
    if cmd == "check" and len(rest) == 1:
        check(int(rest[0]))
    elif cmd == "sweep" and not rest:
        sweep()
    elif cmd == "board" and not rest:
        board()
    elif cmd == "next" and not rest:
        print(next_request())
    elif cmd == "finish" and len(rest) == 2:
        finish(*rest)
    elif cmd == "order" and not rest:
        print(json.dumps([{"number": i["number"], "dataset": request(i["body"])[0]} for i in order(open_requests())]))
    else:
        print(__doc__, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
