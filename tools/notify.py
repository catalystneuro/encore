"""Open, update or close a dataset's `needs-you` issue, from the last line of its runner chain.

    python tools/notify.py FOLDER STATUS [--detail TEXT] [--run ID] [--mention USER] [--dry-run]

STATUS is the last line tools/runner/chain.sh printed. "<folder> MERGED <pr>" and "<folder> CLAIMS
MERGED" close the dataset's open issue, if it has one. Any other ending ("STOPPED ...", "CHECKS
FAILED <pr>") means the chain is waiting on a person: the dataset's issue is opened, or commented
on when one is open already, with what stopped it, the reader's report when the claims step is
what stopped, and links to the run, the branch and the pull request. Run by .github/workflows/notify.yml
with `gh` authenticated; --dry-run prints what it would do instead.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import datasets  # noqa: E402

LABEL = "needs-you"
REPO = os.environ.get("GITHUB_REPOSITORY", "catalystneuro/encore")
SERVER = os.environ.get("GITHUB_SERVER_URL", "https://github.com")

# The report that explains a stop, for the stops a report explains.
REPORTS = [("wrote no claims file", "claims-report.md", "The reader's report"),
           ("claims file is not ready", "claims-check-report.md", "The claims check's report")]


def gh(*args: str) -> str:
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def title(folder: str) -> str:
    return f"{datasets.label(datasets.key_of_folder(folder))}: waiting on you"


def open_issue(folder: str) -> int | None:
    found = json.loads(gh("issue", "list", "--repo", REPO, "--label", LABEL, "--state", "open",
                          "--limit", "200", "--json", "number,title"))
    return next((i["number"] for i in found if i["title"] == title(folder)), None)


def branch_file(folder: str, path: str) -> str | None:
    """A file on the dataset's attempt branch, as the workflow fetched it."""
    try:
        return subprocess.run(["git", "show", f"origin/attempt/{folder}:{path}"], cwd=ROOT, check=True,
                              capture_output=True, text=True).stdout
    except subprocess.CalledProcessError:
        return None


def body(folder: str, status: str, detail: str, run: str, mention: str) -> str:
    what = re.sub(r"^STOPPED:? ", "", status.removeprefix(folder).strip())
    lines = [f"{'@' + mention + ' ' if mention else ''}The runner stopped on "
             f"{datasets.label(datasets.key_of_folder(folder))} and is waiting on a person.", "",
             f"**What stopped it:** {what}"]
    if detail:
        lines.append(f"**Why:** {detail}")
    links = []
    if run:
        links.append(f"[the run]({SERVER}/{REPO}/actions/runs/{run})")
    if branch_file(folder, "README.md") is not None:
        links.append(f"[the branch]({SERVER}/{REPO}/tree/attempt/{folder})")
    links += [f"[the pull request]({url})" for url in re.findall(r"https://\S+/pull/\d+", status)]
    if links:
        lines.append("**Links:** " + ", ".join(links))
    for phrase, name, heading in REPORTS:
        report = branch_file(folder, f"transcripts/{folder}/{name}") if phrase in status else None
        if report:
            lines += ["", f"<details open><summary>{heading}</summary>", "", report.strip(), "", "</details>"]
    lines += ["", "When it is fixed, start the chain on this dataset again (`tools/runner/chain.sh "
              f"{folder}`, or add `{folder}` to the runner's `queue.txt`). This issue closes when the "
              "dataset's attempt or its claims are merged."]
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("folder")
    p.add_argument("status")
    p.add_argument("--detail", default="")
    p.add_argument("--run", default="")
    p.add_argument("--mention", default="")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    if not args.status.startswith(args.folder + " "):
        raise SystemExit(f"error: the status does not start with {args.folder}: {args.status!r}")
    number = None if args.dry_run else open_issue(args.folder)

    if re.match(rf"{re.escape(args.folder)} (CLAIMS )?MERGED\b", args.status):
        if args.dry_run:
            print(f"would close the open issue {title(args.folder)!r}, if any")
        elif number:
            gh("issue", "close", str(number), "--repo", REPO, "--comment",
               f"Done: {args.status.removeprefix(args.folder).strip()}.")
            print(f"closed #{number}")
        return 0

    text = body(args.folder, args.status, args.detail, args.run, args.mention)
    if args.dry_run:
        print(f"would {'comment on' if number else 'open'} {title(args.folder)!r}:\n\n{text}")
    elif number:
        gh("issue", "comment", str(number), "--repo", REPO, "--body", text)
        print(f"commented on #{number}")
    else:
        gh("label", "create", LABEL, "--repo", REPO, "--color", "D93F0B", "--force",
           "--description", "The runner is waiting on a person")
        print(gh("issue", "create", "--repo", REPO, "--title", title(args.folder), "--label", LABEL,
                 "--body", text).strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
