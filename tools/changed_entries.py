"""The entries whose notebooks, code or requirements changed between two commits, one a line.

    python tools/changed_entries.py BASE [HEAD]

An entry that was only renamed (as when records moved to paper-first names, docs/paper-first.md), or whose
README changed, or whose entry.yaml changed only in its `name`, is left out: running it again would give
the same notebooks.
"""

from __future__ import annotations

import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def changed(base: str, head: str = "HEAD") -> list[str]:
    names = set()
    for line in git("diff", "-M", "--name-status", base, head, "--", "entries").splitlines():
        status, *paths = line.split("\t")
        new = paths[-1]
        if status == "R100" or new.endswith("/README.md") or not new.startswith("entries/"):
            continue
        if new.endswith("/entry.yaml") and status.startswith("R"):
            diff = git("diff", "-M", base, head, "--", paths[0], new)
            body = [x for x in diff.splitlines() if re.match(r"^[-+](?![-+])", x)]
            if all(re.match(r"^[-+]name: ", x) for x in body):
                continue
        names.add(new.split("/")[1])
    return sorted(names)


if __name__ == "__main__":
    print("\n".join(changed(*sys.argv[1:])))
