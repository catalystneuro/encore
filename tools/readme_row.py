"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import datasets  # noqa: E402
import paper_records  # noqa: E402
from agent_run import attempt_of  # noqa: E402

COLUMNS = ("reproduced", "partially_reproduced", "not_reproduced", "blocked")


def lead(record: dict) -> str:
    """The row's first cell: the attempt's datasets, each linked to its archive (DANDI's show the bare id)."""
    cells = []
    for d in paper_records.record_datasets(record):
        key = datasets.key_of(d["archive"], str(d["id"]))
        shown = str(d["id"]) if datasets.split_key(key)[0] == "dandi" else datasets.label(key)
        cells.append(f"[{shown}]({datasets.url(key)})")
    return "| " + ", ".join(cells)


def claim_kinds(record: dict) -> dict[str, str]:
    path = paper_records.claims_for_attempt(record)
    if path is None:
        raise SystemExit(f"error: no claims file for {record['paper']}")
    data = yaml.load(path.read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    return {c["id"]: "link" if c.get("kind") == "link" else c.get("data", "dataset") for c in data["claims"]}


def row(name: str) -> str:
    found = attempt_of(name)
    if found is None:
        raise SystemExit(f"error: no attempt on {name}")
    record, entry_dir = found
    if record.get("deprecated"):
        # No counts, and its claims file may be gone (replaced when the paper behind the data changed).
        cells = ["–"] * len(COLUMNS)
    else:
        kinds = claim_kinds(record)
        cells = []
        for outcome in COLUMNS:
            mine = [o for o in record["outcomes"] if o["outcome"] == outcome]
            n = sum(1 for o in mine if kinds.get(o["claim"], "dataset") in ("dataset", "with_labels"))
            m = sum(1 for o in mine if kinds.get(o["claim"]) == "with_inputs")
            cells.append(f"{n} (+{m})" if m else str(n))
    paper = record["id"].rsplit("-", 1)[0]
    surname, year = re.match(r"^(.+?)-(\d{4})(?:-|$)", paper).groups()
    surname = " ".join(w.capitalize() for w in surname.split("-"))
    doi = record["paper"].removeprefix("doi:")
    note = " (deprecated)" if record.get("deprecated") else ""
    return (f"{lead(record)} "
            f"| [{surname.capitalize()} et al. {year}](https://doi.org/{doi}) | " + " | ".join(cells)
            + f" | [`{entry_dir.name}`](entries/{entry_dir.name}){note} |")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paper")
    args = parser.parse_args()
    print(row(args.paper))
    return 0


if __name__ == "__main__":
    sys.exit(main())
