"""Compare a paper's replicates with its current attempt, claim by claim (docs/replicates.md).

    python tools/replicates.py PAPER [PAPER ...]     a report in Markdown
    python tools/replicates.py --all                 every paper with a replicate branch
    python tools/replicates.py --all --json          the same numbers as JSON

A replicate is the attempt run again, blind, from the same claims, on the branch replicate/<paper>/<rN>
(tools/runner/chain.sh with REPLICATE=rN). Its record is the newest attempts/<paper>-NN.yaml on that branch. The
current attempt is the newest record on main. A replicate is counted once its chain has finished: its second
revision committed, and its third when the second left proposed changes (as chain.sh decides). One still going is
listed and left out.

Link claims (the check that the dataset is the paper's data) are left out, as on the site. Every other claim of
the claims file on main is compared, with its outcome in each run; a claim a run did not record counts as missing.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUTCOMES = ("reproduced", "partially_reproduced", "not_reproduced", "blocked")
SHORT = {"reproduced": "R", "partially_reproduced": "P", "not_reproduced": "N", "blocked": "B", None: "–"}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False).stdout


def show(ref: str, path: str) -> dict | None:
    text = git("show", f"{ref}:{path}")
    return yaml.safe_load(text) if text else None


def records(ref: str, paper: str) -> list[str]:
    """The paper's attempt records on a ref, oldest first; not another paper's whose key begins with this one."""
    names = git("ls-tree", "--name-only", f"{ref}:attempts").split()
    return sorted(f"attempts/{n}" for n in names if re.fullmatch(rf"{re.escape(paper)}-\d{{2}}\.yaml", n))


def finished(branch: str, paper: str, rec: dict) -> bool:
    """Whether a replicate's chain has run its last round: the runs committed on its branch, as chain.sh reads them."""
    done = set(re.findall(rf"^Agent run on {re.escape(paper)}: ([a-z0-9-]+) \(success\)$",
                          git("log", "--format=%s", f"origin/main..origin/{branch}"), re.M))
    if "author-revise-2" not in done:
        return False
    return "author-revise-3" in done or not any(o.get("proposed") for o in rec["outcomes"])


def fetch(paper: str | None = None) -> list[str]:
    """Fetch the replicate branches (of one paper, or all) and return their names."""
    pattern = f"refs/heads/replicate/{paper}/*" if paper else "refs/heads/replicate/*"
    git("fetch", "-q", "origin", "main", f"+{pattern}:refs/remotes/origin/{pattern[len('refs/heads/'):]}")
    return sorted(line.split("\t")[1][len("refs/heads/"):] for line in git("ls-remote", "--heads", "origin", pattern).splitlines())


def runs_of(paper: str) -> tuple[list[dict], list[str]]:
    """The current attempt and each finished replicate, as {name, id, outcomes: {claim: outcome}}; and the names of
    replicates not finished yet."""
    runs, going = [], []
    main = records("origin/main", paper)
    if main:
        rec = show("origin/main", main[-1])
        runs.append({"name": "current", "id": rec["id"], "outcomes": {o["claim"]: o["outcome"] for o in rec["outcomes"]}})
    for branch in fetch(paper):
        name = branch.rsplit("/", 1)[1]
        on = records(f"origin/{branch}", paper)
        rec = show(f"origin/{branch}", on[-1]) if on else None
        if not rec or (main and on[-1] == main[-1]) or not finished(branch, paper, rec):
            going.append(name)
            continue
        runs.append({"name": name, "id": rec["id"], "outcomes": {o["claim"]: o["outcome"] for o in rec["outcomes"]}})
    return runs, going


def fleiss_kappa(table: list[list[str | None]]) -> float | None:
    """Fleiss' kappa for items (rows) each rated by the same number of runs, over the four outcomes. None when it is
    not defined (fewer than two runs, no items, or every rating the same outcome)."""
    rows = [r for r in table if all(x is not None for x in r)]
    if not rows or len(rows[0]) < 2:
        return None
    n = len(rows[0])
    counts = [Counter(r) for r in rows]
    p_i = [(sum(c * c for c in cs.values()) - n) / (n * (n - 1)) for cs in counts]
    p_bar = sum(p_i) / len(rows)
    p_j = [sum(cs[k] for cs in counts) / (len(rows) * n) for k in OUTCOMES]
    p_e = sum(p * p for p in p_j)
    return None if p_e == 1 else (p_bar - p_e) / (1 - p_e)


def pairwise(table: list[list[str | None]]) -> float | None:
    """The share of pairs of runs that give a claim the same outcome, over every claim and pair (missing excluded)."""
    same = total = 0
    for row in table:
        for a, b in itertools.combinations([x for x in row if x is not None], 2):
            same += a == b
            total += 1
    return same / total if total else None


def score(outcomes: list[str]) -> float | None:
    """Reproduced plus half the partial, of the claims tested (blocked left out), as the CRCNS/DANDI comparison."""
    tested = [o for o in outcomes if o and o != "blocked"]
    return (sum(o == "reproduced" for o in tested) + sum(o == "partially_reproduced" for o in tested) / 2) / len(tested) \
        if tested else None


def compare(paper: str) -> dict:
    runs, going = runs_of(paper)
    claims_file = show("origin/main", f"claims/{paper}.yaml") or {}
    claims = [c["id"] for c in claims_file.get("claims") or [] if c.get("kind") != "link"]
    table = [[r["outcomes"].get(c) for r in runs] for c in claims]
    per_run = []
    for i, r in enumerate(runs):
        col = [row[i] for row in table]
        per_run.append({"name": r["name"], "id": r["id"], "counts": {k: col.count(k) for k in OUTCOMES},
                        "missing": col.count(None), "score": score(col)})
    scores = [x["score"] for x in per_run if x["score"] is not None]
    mean = sum(scores) / len(scores) if scores else None
    spread = (sum((s - mean) ** 2 for s in scores) / (len(scores) - 1)) ** .5 if len(scores) > 1 else None
    return {
        "paper": paper, "runs": [r["name"] for r in runs], "not_finished": going, "claims": len(claims),
        "unanimous": sum(1 for row in table if len({x for x in row}) == 1 and None not in row),
        "pairwise_agreement": pairwise(table), "fleiss_kappa": fleiss_kappa(table),
        "score_mean": mean, "score_sd": spread, "per_run": per_run,
        "flips": [{"claim": c, "outcomes": dict(zip([r["name"] for r in runs], row))}
                  for c, row in zip(claims, table) if len(set(row)) > 1],
    }


def pct(x: float | None) -> str:
    return "n/a" if x is None else f"{100 * x:.0f}%"


def markdown(results: list[dict]) -> str:
    out = ["# Replicates", "", "| Paper | Runs | Claims | Unanimous | Pairwise agreement | Fleiss' kappa | Score, mean ± SD |",
           "|---|---|---|---|---|---|---|"]
    for r in results:
        k = "n/a" if r["fleiss_kappa"] is None else f'{r["fleiss_kappa"]:.2f}'
        sd = "" if r["score_sd"] is None else f' ± {100 * r["score_sd"]:.0f}'
        out.append(f'| {r["paper"]} | {len(r["runs"])} | {r["claims"]} | {r["unanimous"]} of {r["claims"]} | '
                   f'{pct(r["pairwise_agreement"])} | {k} | {pct(r["score_mean"])}{sd} |')
    out += ["", "The score is the claims reproduced plus half the partially reproduced, of the claims tested."]
    for r in results:
        out += ["", f'## {r["paper"]}', ""]
        if r["not_finished"]:
            out.append(f'Not finished yet, left out: {", ".join(r["not_finished"])}.')
            out.append("")
        out += ["| Run | Attempt | Reproduced | Partially | Not reproduced | Blocked | Missing | Score |",
                "|---|---|---|---|---|---|---|---|"]
        for x in r["per_run"]:
            c = x["counts"]
            out.append(f'| {x["name"]} | {x["id"]} | {c["reproduced"]} | {c["partially_reproduced"]} | '
                       f'{c["not_reproduced"]} | {c["blocked"]} | {x["missing"]} | {pct(x["score"])} |')
        if r["flips"]:
            out += ["", "Claims whose outcome differs between runs (R reproduced, P partially, N not reproduced, "
                        "B blocked, – not recorded):", "", "| Claim | " + " | ".join(r["runs"]) + " |",
                    "|---|" + "---|" * len(r["runs"])]
            for f in r["flips"]:
                out.append(f'| {f["claim"]} | ' + " | ".join(SHORT[f["outcomes"][n]] for n in r["runs"]) + " |")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("papers", nargs="*")
    ap.add_argument("--all", action="store_true", help="every paper with a replicate branch")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    papers = args.papers or sorted({b.split("/")[1] for b in fetch()})
    if not papers:
        print("no replicate branches", file=sys.stderr)
        return 1
    results = [compare(p) for p in papers]
    print(json.dumps(results, indent=1) if args.json else markdown(results), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
