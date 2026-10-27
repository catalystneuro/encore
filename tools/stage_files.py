"""Put a dataset's files in place before an agent starts, for an archive whose files need credentials.

    python tools/stage_files.py DATASET ...      (any form tools/datasets.py takes: dryad-<id>, DRYAD:<id>)
    python tools/stage_files.py --all            (every target of every such archive: the entry checks)

Most archives are read by the agent directly, and this does nothing for them. An archive adapter with a stage()
(tools/archives/) is one whose files the agent cannot fetch, because the credentials it takes are stripped from
the agent's commands; its files go to /tmp/<archive>/<id>/<version>/, where its access sentence tells the agent
to read them. Without the adapter's secrets in the environment it warns and stages nothing, and the run
goes on to find the files missing.
"""

from __future__ import annotations

import argparse
import os
import sys

import datasets
from archives import ALL, STAGED


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("datasets", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    staged = [a for a in ALL.values() if a.stage]
    if args.all:
        keys = [t["key"] for t in datasets.targets() if t["archive"] in {a.key for a in staged}]
    else:
        keys = [datasets.parse(d) for d in args.datasets]
    targets = {t["key"]: t for t in datasets.targets()}
    status = 0
    for key in keys:
        archive = ALL.get(datasets.split_key(key)[0])
        if archive is None or archive.stage is None:
            continue
        missing = [s for s in archive.secrets if not os.environ.get(s)]
        if missing:
            print(f"::warning::{datasets.label(key)}: no {', '.join(missing)}, so its files are not staged")
            continue
        if key not in targets:
            print(f"::error::{datasets.label(key)} is not in targets/{archive.list}")
            status = 1
            continue
        try:
            dest = archive.stage(targets[key], STAGED)
        except Exception as err:   # report it without the request, which may carry a token
            print(f"::error::{datasets.label(key)}: the files were not staged: {type(err).__name__}: {err}")
            status = 1
            continue
        print(f"{datasets.label(key)}: {sum(1 for p in dest.rglob('*') if p.is_file())} files in {dest}")
    return status


if __name__ == "__main__":
    sys.exit(main())
