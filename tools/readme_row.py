"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row
    python tools/readme_row.py DATASET --write    # add it to README.md, or replace the dataset's row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import datasets  # noqa: E402
from agent_run import attempt_of  # noqa: E402

COLUMNS = ("reproduced", "partially_reproduced", "not_reproduced", "blocked")


def lead(folder: str) -> str:
    """The row's first cell: the dataset, linked to its archive (DANDI's rows show the bare id, as before)."""
    key = datasets.key_of_folder(folder)
    shown = folder if datasets.split_key(key)[0] == "dandi" else datasets.label(key)
    return f"| [{shown}]({datasets.url(key)})"


def claim_kinds(dandiset: str, paper: str) -> dict[str, str]:
    for path in sorted((ROOT / "claims" / dandiset).glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        if data.get("paper") == paper:
            return {c["id"]: "link" if c.get("kind") == "link" else c.get("data", "dataset")
                    for c in data["claims"]}
    raise SystemExit(f"error: no claims file for {dandiset} and {paper}")


def row(dandiset: str) -> str:
    found = attempt_of(dandiset)
    if found is None:
        raise SystemExit(f"error: no attempt on {datasets.label(datasets.key_of_folder(dandiset))}")
    record, entry_dir = found
    kinds = claim_kinds(dandiset, record["paper"])
    cells = []
    for outcome in COLUMNS:
        mine = [o for o in record["outcomes"] if o["outcome"] == outcome]
        n = sum(1 for o in mine if kinds.get(o["claim"], "dataset") in ("dataset", "with_labels"))
        m = sum(1 for o in mine if kinds.get(o["claim"]) == "with_inputs")
        cells.append(f"{n} (+{m})" if m else str(n))
    if record.get("deprecated"):
        cells = ["–"] * len(COLUMNS)
    _, surname, year = entry_dir.name.rsplit("-", 2)
    doi = record["paper"].removeprefix("doi:")
    note = " (deprecated)" if record.get("deprecated") else ""
    return (f"{lead(dandiset)} "
            f"| [{surname.capitalize()} et al. {year}](https://doi.org/{doi}) | " + " | ".join(cells)
            + f" | [`{entry_dir.name}`](entries/{entry_dir.name}){note} |")


def write(dandiset: str, readme: Path = ROOT / "README.md") -> None:
    lines = readme.read_text().splitlines(keepends=True)
    new = row(dandiset) + "\n"
    mine = f"{lead(dandiset)} "
    rows = [i for i, line in enumerate(lines) if line.startswith("| [") and "](entries/" in line]
    if not rows:
        raise SystemExit("error: no outcome table in README.md")
    existing = [i for i in rows if lines[i].startswith(mine)]
    if existing:
        lines[existing[0]] = new
    else:
        lines.insert(rows[-1] + 1, new)
    readme.write_text("".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("dataset")
    parser.add_argument("--write", action="store_true", help="add the row to README.md")
    args = parser.parse_args()
    folder = datasets.folder(datasets.parse(args.dataset))
    if args.write:
        write(folder)
    else:
        print(row(folder))
    return 0


if __name__ == "__main__":
    sys.exit(main())
