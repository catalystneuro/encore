"""The cutover to paper-first records, outside main (docs/paper-first.md). Run once, after main's records are
converted (tools/migrate_paper_first.py) and merged, with the lanes stopped. Each step prints what it would do;
--apply does it.

    python tools/runner/cutover_paper_first.py keys [--apply]         # keys for papers only open branches have records of
    python tools/runner/cutover_paper_first.py branches [NAME...] [--apply]   # open attempt branches (or those named)
    python tools/runner/cutover_paper_first.py executed [--apply]     # the executed-notebooks branch
    python tools/runner/cutover_paper_first.py issues [--apply]       # open `needs-you` issues
    python tools/runner/cutover_paper_first.py state DIR [--apply]    # the runner's state (~/registry-runner)

`--main REF` takes another ref as main and `--try` converts and merges the branches without pushing, to try
the steps out before the cutover.

Run from a clone whose origin/main has the converted records. Names come from main's papers/datasets/ and
papers/renamed.yaml.

- keys: run in the checkout to be converted, before tools/migrate_paper_first.py: a paper that only an open
  branch has records of gets its key in papers/keys.yaml, from the branch's entry name or claims header.
- branches: every attempt/<folder> branch not merged into main is converted the way main was (the conversion
  run on the branch, with main's tools and keys), main is merged into it, and it is pushed as attempt/<paper>
  when its dataset is listed for a paper, the old branch deleted. A branch that does not merge is left as it
  was and reported.
- executed: each entry's executed notebooks move to the entry's new name.
- issues: "<dataset>: waiting on you" becomes "<paper>: waiting on you"; when two of a paper's datasets have
  one, the later is closed in favour of the other.
- state: in the queue files (*.txt: resume-*, started, queue, done), a dataset's folder name becomes its
  paper's key, as do the marks attempt-*, verified-*, flagged-* and put-back-*.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path.cwd()
REPO = "catalystneuro/encore"
MAIN = "origin/main"   # --main REF: another ref as main, to try the steps out locally
TRY = False            # --try: convert and merge the branches, but push nothing
COMMIT = ["-c", "user.name=github-actions[bot]", "-c", "user.email=github-actions[bot]@users.noreply.github.com"]


def git(*args, cwd=ROOT, check=True) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=check, capture_output=True, text=True).stdout


def main_yaml(path: str):
    try:
        return yaml.safe_load(git("show", f"{MAIN}:{path}"))
    except subprocess.CalledProcessError:
        return None


def paper_of_folder() -> dict[str, str]:
    """Dataset folder -> paper key, from main's papers/datasets/ (a primary paper first)."""
    sys.path.insert(0, str(ROOT / "tools"))
    import datasets
    out, rank = {}, {}
    for path in git("ls-tree", "--name-only", MAIN, "papers/datasets/").split():
        body = main_yaml(path) or {}
        for d in body.get("datasets") or []:
            folder = datasets.folder(datasets.key_of(d["archive"], str(d["id"])))
            r = 0 if d.get("relation", "primary") == "primary" else 1
            if folder not in out or r < rank[folder]:
                out[folder], rank[folder] = Path(path).stem, r
    return out


def keys(apply: bool) -> int:
    sys.path.insert(0, str(ROOT / "tools"))
    import paper_keys
    git("fetch", "-q", "origin", "main", "+refs/heads/attempt/*:refs/remotes/origin/attempt/*")
    open_ = [b.strip() for b in git("branch", "-r", "--no-merged", MAIN, "--list", "origin/attempt/*").splitlines()
             if b.strip()]
    have = paper_keys.read_keys()
    found: dict[str, dict] = {}
    for ref in open_:
        for path in git("diff", "--name-only", f"{MAIN}...{ref}", "--", "attempts", "claims").split():
            try:
                text = git("show", f"{ref}:{path}")
            except subprocess.CalledProcessError:
                continue
            body = yaml.safe_load(text) or {}
            doi = paper_keys.doi_of(str(body.get("paper") or ""))
            if not doi or doi in have:
                continue
            p = found.setdefault(doi, {})
            m = paper_keys.ENTRY.match(str(body.get("entry") or ""))
            if m:
                p["name"] = m.group(1)
            m = paper_keys.CLAIMS_FOR.match(text.split("\n#\n", 1)[0]) if path.startswith("claims/") else None
            if m and "name" not in p:
                p.update(surname=m.group(1).strip(), year=m.group(2))
    for doi, p in sorted(found.items()):
        if "name" in p:
            surname, year = p["name"].rsplit("-", 1)
        else:
            surname, year = p.get("surname", ""), p.get("year", "")
        if apply:
            print(f"{doi}: {paper_keys.add_key(doi, surname=paper_keys.ascii_slug(surname), year=year)}")
        else:
            print(f"{doi}: would get a key ({surname or 'from Crossref'} {year})")
    return 0


def branches(apply: bool, only: list[str] | None = None) -> int:
    git("fetch", "-q", "origin", "main", "+refs/heads/attempt/*:refs/remotes/origin/attempt/*")
    open_ = [b.strip().removeprefix("origin/attempt/") for b in
             git("branch", "-r", "--no-merged", MAIN, "--list", "origin/attempt/*").splitlines() if b.strip()]
    papers = paper_of_folder()
    keys = set(papers.values())
    bad = 0
    for name in open_:
        if name in keys or (only and name not in only):
            continue   # already a paper's branch, or not one asked for
        target = papers.get(name, name)
        print(f"attempt/{name} -> attempt/{target}", end="")
        if not apply and not TRY:
            print()
            continue
        tmp = Path(tempfile.mkdtemp())
        try:
            git("worktree", "add", "-q", "--detach", str(tmp), f"origin/attempt/{name}")
            # Main's tools and keys, so that the branch is converted exactly as main was.
            # Main's tools, keys, target lists, triage and paper matches, so that the branch is converted exactly as
            # main was; a branch from before some of them existed would otherwise lack them.
            git("checkout", MAIN, "--", "tools", "schemas", "targets", "papers/keys.yaml", "papers/triage.yaml",
                "papers/match", cwd=tmp)
            several = tmp / ".main-renamed.yaml"
            several.write_text(git("show", f"{MAIN}:papers/renamed.yaml"))
            run = subprocess.run([sys.executable, "tools/migrate_paper_first.py"], cwd=tmp, capture_output=True,
                                 text=True, env={**os.environ, "MIGRATE_SEVERAL_FROM": str(several)})
            several.unlink()
            if run.returncode:
                print(f": conversion failed: {run.stderr.strip()[-300:]}"); bad += 1; continue
            # Main's lists of papers and their datasets, which it has for every matched dataset: the branch's own
            # conversion lists only the papers it has records of.
            on_main = set(git("ls-tree", "-r", "--name-only", MAIN, "papers/datasets", "papers/renamed.yaml").split())
            if on_main:
                git("checkout", MAIN, "--", *sorted(on_main), cwd=tmp)
            git("add", "-A", cwd=tmp)
            git(*COMMIT, "commit", "-q", "-m", "Paper-first names (the cutover, docs/paper-first.md)", cwd=tmp, check=False)
            converted = git("rev-parse", "HEAD", cwd=tmp).strip()
            # Main's version wins everywhere but in the branch's own paper's records, the branch's work: main has
            # converted the same older records with later changes, which the branch never had.
            subprocess.run(["git", *COMMIT, "merge", "-q", "--no-edit", "-X", "theirs", "-m",
                            f"Merge main into attempt/{target}", MAIN], cwd=tmp, capture_output=True, text=True)
            for path in git("diff", "--name-only", "--diff-filter=U", cwd=tmp).split():
                if subprocess.run(["git", "checkout", "--theirs", "--", path], cwd=tmp, capture_output=True).returncode:
                    git("rm", "-q", "--", path, cwd=tmp, check=False)   # gone on main
                else:
                    git("add", "--", path, cwd=tmp)
            own = [p for p in git("ls-tree", "-r", "--name-only", converted, cwd=tmp).split()
                   if re.match(rf"^(attempts/{re.escape(target)}-\d\d\.yaml|claims/{re.escape(target)}(\.yaml|/)|"
                               rf"questions/{re.escape(target)}(\.yaml|/)|entries/{re.escape(target)}/|"
                               rf"transcripts/(match/)?{re.escape(target)}/)", p)]
            if own:
                git("checkout", converted, "--", *own, cwd=tmp)
            git("add", "-A", cwd=tmp)
            merging = Path(git("rev-parse", "--absolute-git-dir", cwd=tmp).strip(), "MERGE_HEAD").exists()
            if merging:
                git(*COMMIT, "commit", "-q", "--no-edit", cwd=tmp)
            elif git("status", "--porcelain", cwd=tmp).strip():
                git(*COMMIT, "commit", "-q", "-m", f"attempt/{target}: the branch's own records over main's", cwd=tmp)
            check = subprocess.run([sys.executable, "tools/entry.py", "check", *sorted(
                {"/".join(p.split("/")[:2]) for p in own if p.startswith("entries/")})], cwd=tmp,
                capture_output=True, text=True) if any(p.startswith("entries/") for p in own) else None
            if check is not None and check.returncode:
                print(f": merged, but its entry does not check: {check.stdout.strip()[-300:]}"); bad += 1; continue
            if TRY:
                print(": converts and merges (not pushed)"); continue
            if target != name and git("ls-remote", "--heads", "origin", f"attempt/{target}").strip():
                print(f": attempt/{target} exists already; left as it was"); bad += 1; continue
            git("push", "-q", "origin", f"HEAD:refs/heads/attempt/{target}", cwd=tmp)
            if target != name:
                git("push", "-q", "origin", "--delete", f"attempt/{name}")
            print(": done")
        finally:
            git("worktree", "remove", "--force", str(tmp), check=False)
            shutil.rmtree(tmp, ignore_errors=True)
    return 1 if bad else 0


def executed(apply: bool) -> int:
    renamed = (main_yaml("papers/renamed.yaml") or {}).get("entries") or {}
    git("fetch", "-q", "origin", "executed")
    have = set(git("ls-tree", "--name-only", "FETCH_HEAD").split())
    moves = [(o, n) for o, n in sorted(renamed.items()) if o != n and o in have]
    for o, n in moves:
        print(f"{o} -> {n}")
    if not apply or not moves:
        return 0
    tmp = Path(tempfile.mkdtemp())
    try:
        git("worktree", "add", "-q", "--detach", str(tmp), "FETCH_HEAD")
        for o, n in moves:
            git("mv", o, n, cwd=tmp)
        git(*COMMIT, "commit", "-q", "-m", "Executed notebooks under the entries' paper-first names", cwd=tmp)
        git("push", "-q", "origin", "HEAD:refs/heads/executed", cwd=tmp)
    finally:
        git("worktree", "remove", "--force", str(tmp), check=False)
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


def gh(*args) -> str:
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def issues(apply: bool) -> int:
    sys.path.insert(0, str(ROOT / "tools"))
    import datasets
    papers = paper_of_folder()
    found = json.loads(gh("issue", "list", "--repo", REPO, "--label", "needs-you", "--state", "open",
                          "--limit", "500", "--json", "number,title"))
    by_paper: dict[str, list] = {}
    for i in found:
        m = re.match(r"^(.+): waiting on you$", i["title"])
        if not m:
            continue
        try:
            folder = datasets.folder(datasets.parse(m.group(1)))
        except ValueError:
            continue   # already a paper's
        if folder in papers:
            by_paper.setdefault(papers[folder], []).append(i)
    for paper, mine in sorted(by_paper.items()):
        keep, *rest = sorted(mine, key=lambda i: i["number"])
        print(f"#{keep['number']} {keep['title']!r} -> {paper + ': waiting on you'!r}"
              + "".join(f"; close #{i['number']}, the same paper" for i in rest))
        if apply:
            gh("issue", "edit", str(keep["number"]), "--repo", REPO, "--title", f"{paper}: waiting on you")
            gh("issue", "comment", str(keep["number"]), "--repo", REPO, "--body",
               f"Records are now by paper (docs/paper-first.md): this is paper `{paper}`'s issue. To run it again, "
               f"start the chain on `{paper}`.")
            for i in rest:
                gh("issue", "close", str(i["number"]), "--repo", REPO, "--comment",
                   f"Records are now by paper: the paper `{paper}`'s issue is #{keep['number']}.")
    return 0


def state(directory: Path, apply: bool) -> int:
    papers = paper_of_folder()
    for f in sorted(directory.glob("*.txt")):
        if not re.match(r"^(resume-.*|started|queue|done)\.txt$", f.name):
            continue
        lines = f.read_text().splitlines()
        renamed = []
        for line in lines:
            first, _, rest = line.partition(" ")
            renamed.append(" ".join(x for x in (papers.get(first, first), rest) if x))
        # A paper whose two datasets were both queued is taken once.
        new = list(dict.fromkeys(renamed))
        if new != lines:
            changes = sorted({f"{a.split()[0]} -> {b.split()[0]}" for a, b in zip(lines, renamed) if a != b})
            print(f"{f.name}: {len(changes)} renamed ({', '.join(changes[:8])}{', ...' if len(changes) > 8 else ''})"
                  + (f"; {len(lines) - len(new)} duplicates dropped" if len(new) < len(lines) else ""))
            if apply:
                f.write_text("\n".join(new) + ("\n" if new else ""))
    for mark in sorted(directory.iterdir()):
        m = re.match(r"^(attempt|verified|flagged|put-back)-(.+)$", mark.name)
        if not m or m.group(2) not in papers:
            continue
        dest = directory / f"{m.group(1)}-{papers[m.group(2)]}"
        print(f"{mark.name} -> {dest.name}" + (" (exists; kept)" if dest.exists() else ""))
        if apply and not dest.exists():
            mark.rename(dest)
    return 0


def main() -> int:
    global MAIN, TRY
    args = sys.argv[1:]
    apply = "--apply" in args
    TRY = "--try" in args
    if "--main" in args:
        MAIN = args[args.index("--main") + 1]
        args = [a for i, a in enumerate(args) if a != "--main" and (i == 0 or args[i - 1] != "--main")]
    args = [a for a in args if a not in ("--apply", "--try")]
    if not args:
        raise SystemExit(__doc__)
    if args[0] == "keys":
        return keys(apply)
    if args[0] == "branches":
        return branches(apply, args[1:])
    if args[0] == "executed":
        return executed(apply)
    if args[0] == "issues":
        return issues(apply)
    if args[0] == "state" and len(args) == 2:
        return state(Path(args[1]).expanduser(), apply)
    raise SystemExit(__doc__)


if __name__ == "__main__":
    raise SystemExit(main())
