"""Open, update or close a paper's `needs-you` issue (or a dataset's, before its paper match), from the last line
of its runner chain.

    python tools/notify.py FOLDER STATUS [--detail TEXT] [--run ID] [--mention USER] [--dry-run]

STATUS is the last line tools/runner/chain.sh printed. "<folder> MERGED <pr>" and "<folder> CLAIMS
MERGED" close the dataset's open issue, if it has one. Any other ending ("STOPPED ...", "CHECKS
FAILED <pr>") means the chain is waiting on a person: the dataset's issue is opened, or commented
on when one is open already, with what stopped it, why (the failed checks or the failed step of the run,
with the end of its log), what the person can do about it, the reader's report when the claims step is
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


def shown(name: str) -> str:
    """How the chain's name is shown: a dataset's label (DANDI:000147) before its paper match, else the paper's key.
    A paper is one papers/datasets/ lists: the dataset parser would take "holdgraf-2016" for archive "holdgraf"."""
    if (ROOT / "papers" / "datasets" / f"{name}.yaml").is_file():
        return name
    try:
        return datasets.label(datasets.key_of_folder(name))
    except (ValueError, KeyError):
        return name


def title(folder: str) -> str:
    return f"{shown(folder)}: waiting on you"


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


def gh_try(*args: str) -> str:
    """`gh`, or nothing when it fails: a notice is still written when its diagnosis cannot be."""
    try:
        return subprocess.run(["gh", *args], check=True, capture_output=True, text=True, timeout=120).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return ""


# Lines of a failed job's log that say what went wrong, for the excerpt.
TELLING = re.compile(r"##\[error\]|\bFAILED\b|Traceback|\bError\b|Exception|timed out|exit code \d+|"
                     r"FLAGGED|UNAVAILABLE|limit|fatal:|refused|denied", re.I)


def failed_run(run: str, lines: int = 30) -> dict:
    """What failed in a run: its failed jobs and steps, and the end of the failed steps' log."""
    found = {"steps": [], "log": ""}
    if not run:
        return found
    try:
        jobs = json.loads(gh_try("run", "view", run, "--repo", REPO, "--json", "jobs") or "{}").get("jobs", [])
    except ValueError:
        jobs = []
    for job in jobs:
        if job.get("conclusion") == "failure":
            steps = [s["name"] for s in job.get("steps") or [] if s.get("conclusion") == "failure"]
            found["steps"].append(f"job `{job['name']}`" + (f", step \"{steps[0]}\"" if steps else ""))
    raw = gh_try("run", "view", run, "--repo", REPO, "--log-failed")
    # Each line is "job<TAB>step<TAB>timestamp text"; the text is what a person reads.
    text = [re.sub(r"^\S+Z ", "", line.split("\t")[-1]).rstrip() for line in raw.splitlines()]
    # Colour codes go (gh prints the escape as "^["), and so does a step's preamble (its command and environment).
    text = [re.sub(r"(\x1b|\^\[)\[[0-9;]*m", "", t) for t in text if t.strip()]
    last = max((i for i, t in enumerate(text) if TELLING.search(t)), default=len(text) - 1)
    shown = text[max(0, last + 1 - lines):last + 1]
    preamble = max((i for i, t in enumerate(shown) if t.startswith(("##[group]", "##[endgroup]"))), default=-1)
    found["log"] = "\n".join(t[:300] for t in shown[preamble + 1:])
    return found


def failed_checks(pr: str) -> list[dict]:
    """The checks of a pull request that failed, each with its run."""
    try:
        checks = json.loads(gh_try("pr", "checks", pr, "--repo", REPO, "--json", "name,bucket,link,workflow") or "[]")
    except ValueError:
        return []
    out = []
    for c in checks:
        if c.get("bucket") == "fail":
            m = re.search(r"/actions/runs/(\d+)", c.get("link") or "")
            out.append({"name": c["name"], "workflow": c.get("workflow") or "", "link": c.get("link"),
                        "run": m[1] if m else ""})
    return out


def restart(folder: str) -> str:
    return (f"Start the chain again: put `{folder}` first in the runner's queue (the first line of its resume "
            f"file or `queue.txt`), or run `tools/runner/chain.sh {folder}`. It carries on from the step that "
            "stopped; the steps before it are kept on the branch.")


def diagnose(folder: str, status: str, detail: str, run: str) -> tuple[list[str], list[str], str]:
    """Why the chain stopped, what a person can do about it, and the log that shows it. The first is a list of
    sentences, the second a list of steps; the first is empty when the chain's own words (detail) say it all."""
    what = status.removeprefix(folder).strip()
    why, steps, log = [], [], ""
    pr = next(iter(re.findall(r"https://\S+/pull/\d+", status)), "")

    if what.startswith("CHECKS FAILED") and pr:
        checks = failed_checks(pr)
        own_tests = False
        for c in checks:
            found = failed_run(c["run"])
            where = "; ".join(found["steps"]) or "see its log"
            why.append(f"The attempt is finished and its pull request is open, but the check "
                       f"[{c['workflow'] or c['name']} / {c['name']}]({c['link']}) failed ({where}).")
            log = log or found["log"]
            own_tests = own_tests or bool(re.search(r"FAILED tests/|tests/test_\w+\.py", found["log"]))
        if not checks:
            why.append("The attempt is finished and its pull request is open, but its checks did not all pass.")
        if own_tests:
            steps.append("The failure is in one of the repository's own tests (`tests/`), so it is probably not "
                         "about this attempt. See whether the same test fails on `main` and in other attempts' "
                         "pull requests; if so, fix it on `main`, then update this branch from `main`.")
        else:
            steps.append(f"Read the error below. If it is about the entry (a notebook that does not run, a record "
                         f"that does not validate), fix it on the branch `attempt/{folder}`: a push runs the checks "
                         "again.")
        rerun = next((c["run"] for c in checks if c["run"]), "")
        steps.append("If it looks like a passing failure (the network, a timeout), run the failed check again"
                     + (f": `gh run rerun {rerun} --failed`." if rerun else "."))
        steps.append(f"When the checks pass, merge {pr}. Nothing needs to be queued again: the attempt itself is done.")
        return why, steps, log

    role = re.match(r"STOPPED at ([\w-]+)", what)
    if role:
        found = failed_run(run)
        log = found["log"]
        both = f"{detail}\n{log}"
        where = f" ({'; '.join(found['steps'])})" if found["steps"] else ""
        if re.search(r"FLAGGED on the \w+ account|-UNAVAILABLE", both):
            why.append(f"The agent's run of `{role[1]}` was refused on the account it ran on, and the chain was "
                       "told not to fall back to the verified account.")
            steps.append(f"Run it on the verified account: create the file `verified-{folder}` in the runner's "
                         "state folder. " + restart(folder))
        elif re.search(r"session limit|weekly limit", both):
            why.append(f"The run of `{role[1]}` hit the account's usage limit{where}.")
            steps.append("Wait for the limit to reset, or move the dataset to a pool with usage left. "
                         + restart(folder))
        elif re.search(r"(CellTimeoutError|Cell execution timed out|FAIL\s+\S+\.ipynb\s+\(\d+ s\))", log) \
                and re.search(r"(Prepare|Run the notebooks|execute)", " ".join(found["steps"]), re.I):
            # The notebooks are run again before a role's agent starts (the verifier's materials, say): a notebook
            # over the time limit stops the chain there, before any agent.
            nb = re.search(r"FAIL\s+(\S+\.ipynb)\s+\((\d+) s\)", log)
            took = f" ({nb[1]}, stopped after {int(nb[2]) // 60} minutes)" if nb else ""
            why.append(f"A notebook ran over the time limit when it was run again before `{role[1]}`{where}{took}. "
                       "The agent of that role had not started.")
            steps += ["Once can be a slow download from the archive: start it again. " + restart(folder),
                      "If it runs over again, the notebook is too slow for the limit (60 minutes a notebook, 60 a "
                      "cell): the author's next revision should load less or cache per session; note it in the "
                      "dataset's pilot notes."]
        elif "timed out after" in both:
            why.append(f"The agent ran out of time in `{role[1]}`{where}.")
            steps += ["Once is usually bad luck with a slow download or a long notebook. " + restart(folder),
                      "If it has timed out here before, read the end of the transcript (the run's artifact) for "
                      "what it was doing, and raise the role's time limit or note the cause in the dataset's "
                      "pilot notes before trying again."]
        elif re.search(r"exit code 143|shutdown signal|lost communication", both):
            why.append(f"The machine running `{role[1]}` was shut down or ran out of memory{where}. The chain "
                       "had already tried it again.")
            steps.append("If the data are large, the agent has to load less at a time: say so in the dataset's "
                         "pilot notes. " + restart(folder))
        elif re.search(r"Check the token, the permission mode", both):
            why.append(f"The pre-flight check failed before the agent started{where}: nothing about this dataset.")
            steps.append("See the log below for which check failed. When the cause is fixed: " + restart(folder))
        else:
            why.append(f"The run of `{role[1]}` failed{where}." + (f" The chain says: {detail}." if detail and
                       detail != f"the run of {role[1]} failed" else ""))
            steps += ["Read the end of the log below for the error. A failure before the agent starts (checkout, "
                      "the paper store, set-up) is not about the dataset.",
                      restart(folder)]
        return why, steps, log

    if "wrote no claims file" in what:
        why.append("The reader could not read the claims from the paper's text as stored. Its report, below, says "
                   "what is missing: usually a supplement, the methods, or figure legends.")
        steps += ["Add what the report asks for to the paper store (catalystneuro/registry-papers, in this "
                  "dataset's folder): the article's PDF or the supplementary files.",
                  restart(folder)]
    elif "claims file is not ready" in what:
        why.append("The claims check found problems in the claims file that the reader did not settle; its report "
                   "is below.")
        steps += [f"If the report asks for text the store lacks, add it. If it disputes a claim, correct "
                  f"`claims/{folder}.yaml` on the branch `attempt/{folder}`, or leave it for the reader to read again.",
                  restart(folder)]
    elif "no paper matches the dataset" in what or "without a verdict" in what:
        why.append("The paper match found no paper whose data this dataset holds, or left one undecided.")
        steps += [f"Open `papers/match/{folder}.yaml` on `main` and read the verdicts. If they are right, set "
                  "`confirmed: true` (the dataset is then skipped for good). If a paper does match, correct its "
                  "verdict, or name the right paper in `papers/triage.yaml`.",
                  restart(folder)]
    elif "claims are on data elsewhere" in what:
        why.append("Most of the paper's claims rest on data that are not in its datasets here, so the paper is "
                   "probably matched to the wrong dataset, or its other datasets are not listed.")
        steps += [f"Check `papers/datasets/{folder}.yaml` and the `papers/match/` files of its datasets: add the "
                  "missing datasets, or correct the match.",
                  restart(folder)]
    elif "conflicts with main" in what or "does not merge with main" in what:
        why.append(f"The branch `attempt/{folder}` conflicts with `main`, so GitHub runs no checks on it.")
        steps += [f"Merge `main` into `attempt/{folder}`, resolve the conflict (for `claims/`, keep the branch's "
                  "file), and push.",
                  restart(folder)]
    elif re.search(r"could not (push|check out|open a pull request)|merging .* failed|did not go into main", what):
        why.append("A git or GitHub step of the runner failed, after the agents' work: nothing about the dataset.")
        steps += ["Check that GitHub is up and that the branch is not checked out in another worktree of the "
                  "runner's clone.",
                  restart(folder)]
    else:
        steps.append(restart(folder))
    return why, steps, log


def body(folder: str, status: str, detail: str, run: str, mention: str) -> str:
    what = re.sub(r"^STOPPED:? ", "", status.removeprefix(folder).strip())
    why, steps, log = diagnose(folder, status, detail, run)
    lines = [f"{'@' + mention + ' ' if mention else ''}The runner stopped on "
             f"{shown(folder)} and is waiting on a person.", "",
             f"**What stopped it:** {what}"]
    if why or detail:
        lines.append("**Why:** " + " ".join(why or [detail]))
    if steps:
        lines += ["", "**What you can do:**"] + [f"{i}. {step}" for i, step in enumerate(steps, 1)] + [""]
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
    if log:
        lines += ["", "<details open><summary>The end of the failed step's log</summary>", "", "```",
                  log.replace("```", "~~~"), "```", "", "</details>"]
    lines += ["", "This issue closes when the attempt or its claims are merged."]
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
