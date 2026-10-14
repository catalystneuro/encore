"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dandiset the entry uses;
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.

Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
script itself. The entry's own dependencies come only from its lock file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import nbformat
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
PYTHON_VERSION = "3.13"
HARNESS = ["ipykernel", "nbconvert"]      # needed to execute, not part of the entry
MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"

EMBEDDED_IMAGE = re.compile(r"data:image/|iVBORw0KGgo|/9j/4AAQ")
READS_A_FIGURE = re.compile(r"""(imread|Image\.open|IPython\.display\.Image|display\.Image)\s*\(""")
LOCAL_PATH = re.compile(r"""["'](?:~/|/(?:Users|home|tmp|mnt|media|Volumes|data|scratch)/|[A-Za-z]:[\\/])""")
LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)


class Report:
    def __init__(self):
        self.errors: list[str] = []

    def error(self, where, message: str) -> None:
        self.errors.append(f"{where}: {message}")


def schema(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text()))


def load(report: Report, path: Path):
    """The parsed file, or None after reporting that it is not valid YAML."""
    try:
        return yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        report.error(path.relative_to(ROOT), f"not valid YAML: {e}")
        return None


def validate(report: Report, path: Path, schema_name: str) -> dict | None:
    data = load(report, path)
    if data is None:
        return None
    for err in sorted(schema(schema_name).iter_errors(_plain(data)), key=lambda e: list(e.path)):
        where = "/".join(str(p) for p in err.path) or "(top level)"
        report.error(path.relative_to(ROOT), f"{where}: {err.message}")
    return data if isinstance(data, dict) else None


def _plain(value):
    """YAML dates as strings, so JSON Schema's string formats apply."""
    if isinstance(value, dict):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def code_of(notebook_path: Path) -> str:
    nb = nbformat.read(notebook_path, as_version=4)
    return "\n".join(c.source for c in nb.cells if c.cell_type == "code")


# --- check --------------------------------------------------------------------

def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
    if entry is None:
        return report
    if entry.get("name") != entry_dir.name:
        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")

    listed = [n["path"] for n in entry.get("notebooks", [])]
    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
    for name in sorted(set(present) - set(listed)):
        report.error(rel / name, "notebook is not listed in entry.yaml")
    for name in sorted(set(listed) - set(present)):
        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
    helpers = entry.get("helpers", [])
    for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

    requirements, lock = entry_dir / "requirements.in", entry_dir / "requirements.lock.txt"
    if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
                  for line in lock.read_text().splitlines() if line and not line.startswith((" ", "#"))}
        for line in requirements.read_text().splitlines():
            name = re.split(r"[=<>!~\[ ;]", line.strip(), maxsplit=1)[0].lower().replace("_", "-")
            if name and not name.startswith("#") and name not in pinned:
                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")

    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if r["id"].startswith("dandi:")]
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
    if entry.get("type") in ("orientation", "reproduction"):
        if not dandisets:
            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dandiset")
        for d, v in versions.items():
            if not v:
                report.error(rel / "entry.yaml", f"pin the version of dandiset {d}, as dandi:{d}/<version>")
    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())

    for name in [n for n in listed if n in present]:
        path = entry_dir / name
        nb = nbformat.read(path, as_version=4)
        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
        code = code_of(path)
        for dandiset in dandisets:
            if dandiset not in code and dandiset not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names dandiset {dandiset}")
            version = versions[dandiset]
            if version and version not in code and version not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
                                         f"of dandiset {dandiset}, which entry.yaml pins")
        _derivation_checks(report, rel / name, code)
    for name in helpers:
        if (entry_dir / name).is_file():
            _derivation_checks(report, rel / name, (entry_dir / name).read_text())

    # Claims and attempts that go with this entry.
    claims_by_target = {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        data = validate(report, path, "claims") or {}
        ids = {c["id"] for c in data.get("claims", [])}
        claims_by_target[(data.get("dandiset"), data.get("paper"))] = ids
        for c in data.get("claims", []):
            for other in c.get("depends_on", []):
                if other not in ids:
                    report.error(path.relative_to(ROOT), f"claim {c['id']!r} depends on {other!r}, which is not in the file")
    for path in sorted((ROOT / "attempts").glob("*.yaml")):
        attempt = load(report, path)
        if not isinstance(attempt, dict) or attempt.get("entry") != entry["name"]:
            continue
        validate(report, path, "attempt")
        where = path.relative_to(ROOT)
        pinned = versions.get(attempt.get("dandiset"))
        if pinned and attempt.get("dandiset_version") != pinned:
            report.error(where, f"dandiset_version {attempt.get('dandiset_version')!r} differs from "
                                f"{pinned!r} in entry.yaml")
        known = claims_by_target.get((attempt.get("dandiset"), attempt.get("paper")))
        if known is None:
            report.error(where, "no claims file for this dandiset and paper")
            continue
        recorded = [o.get("claim") for o in attempt.get("outcomes", [])]
        for claim in sorted(known - set(recorded)):
            report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
        for claim in sorted({c for c in recorded if recorded.count(c) > 1}):
            report.error(where, f"claim {claim!r} has more than one outcome")
        rounds = attempt.get("verifications") or []
        agreed = {r["claim"]: r.get("outcome") for r in (rounds[-1]["results"] if rounds else [])
                  if r.get("agrees") and r.get("outcome")}
        for outcome in attempt.get("outcomes", []):
            verified = agreed.get(outcome.get("claim"))
            if verified and outcome.get("outcome") != verified:
                report.error(where, f"claim {outcome.get('claim')!r} is {outcome.get('outcome')!r}, but the last "
                                    f"verification agreed with {verified!r}; record the change as proposed, or "
                                    "verify it in another round")
            if outcome.get("claim") not in known:
                report.error(path.relative_to(ROOT), f"claim {outcome.get('claim')!r} is not in the claims file")
            notebook = outcome.get("notebook")
            if notebook and notebook not in listed:
                report.error(path.relative_to(ROOT), f"notebook {notebook!r} is not in the entry")
            tag = outcome.get("output")
            if notebook in present and tag:
                nb = nbformat.read(entry_dir / notebook, as_version=4)
                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
    return report


def _derivation_checks(report: Report, where, code: str) -> None:
    if EMBEDDED_IMAGE.search(code):
        report.error(where, "contains an encoded image; figures must be computed from the data")
    if READS_A_FIGURE.search(code):
        report.error(where, "reads an image file; figures must be computed from the data")
    if LOCAL_PATH.search(code):
        report.error(where, "names a local path; stream the data from the archive")
    if LONG_LITERAL.search(code):
        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
                            "results must be computed from the data")


# --- lock and run -------------------------------------------------------------

def lock(entry_dir: Path) -> int:
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
    return r.returncode


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
            return 1

    results, failed = [], False
    for notebook in entry["notebooks"]:
        name = notebook["path"]
        started = time.time()
        r = subprocess.run(
            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
             "--output-dir", str(output_dir.resolve()), "--output", name, name],
            cwd=entry_dir, capture_output=True, text=True,
            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
        seconds = round(time.time() - started)
        ok = r.returncode == 0
        error = None if ok else r.stderr[-3000:]
        if ok and seconds > max_minutes * 60:
            ok = False
            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
        failed |= not ok
        results.append({"notebook": name, "ok": ok, "seconds": seconds, "error": error})
        print(f"{'pass' if ok else 'FAIL'}  {name}  ({seconds} s)")
        if not ok:
            print(error, file=sys.stderr)
    (output_dir / "result.json").write_text(json.dumps(
        {"entry": entry["name"], "python": PYTHON_VERSION, "results": results}, indent=1) + "\n")
    return 1 if failed else 0


# --- handover -----------------------------------------------------------------

def strip_conclusions(nb):
    """The notebook without the author's conclusions, for a verifier's first round."""
    kept = []
    for cell in nb.cells:
        text = cell.source.lstrip()
        if cell.cell_type == "markdown" and text.startswith("## Summary"):
            break
        if cell.cell_type == "markdown" and text.startswith("**Result:"):
            continue
        kept.append(cell)
    nb.cells = kept
    return nb


def handover(entry_dir: Path, output_dir: Path) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    target = output_dir / "handover"
    target.mkdir(parents=True, exist_ok=True)
    for notebook in entry["notebooks"]:
        executed = output_dir / notebook["path"]
        if not executed.is_file():
            print(f"error: no executed copy of {notebook['path']} in {output_dir}; run the entry first",
                  file=sys.stderr)
            return 1
        nb = strip_conclusions(nbformat.read(executed, as_version=4))
        nbformat.write(nb, target / notebook["path"])
    for helper in entry.get("helpers", []):
        shutil.copy(entry_dir / helper, target / helper)
    papers = {r["id"] for r in entry.get("related", []) if r["relation"] == "reproduces"}
    dandisets = {r["id"].split(":", 1)[1].split("/")[0]
                 for r in entry.get("related", []) if r["id"].startswith("dandi:")}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        claims = yaml.safe_load(path.read_text()) or {}
        if claims.get("dandiset") in dandisets and claims.get("paper") in papers:
            shutil.copy(path, target / path.name)
    print(f"wrote {target}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
    parser.add_argument("entry", type=Path, help="the entry directory, e.g. entries/000582-sargolini-2006")
    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
    parser.add_argument("--max-minutes", type=float, default=30,
                        help="a notebook that takes longer than this fails")
    args = parser.parse_args()

    entry_dir = args.entry.resolve()
    if not (entry_dir / "entry.yaml").is_file():
        parser.error(f"{args.entry} has no entry.yaml")
    output_dir = args.output_dir or ROOT / "executed" / entry_dir.name

    if args.command == "lock":
        return lock(entry_dir)
    if args.command == "handover":
        return handover(entry_dir, output_dir)
    if args.command in ("check", "all"):
        report = check(entry_dir)
        for line in report.errors:
            print(f"error: {line}")
        print(f"{len(report.errors)} error(s)")
        if report.errors or args.command == "check":
            return 1 if report.errors else 0
    return run(entry_dir, output_dir, args.timeout, args.max_minutes)


if __name__ == "__main__":
    sys.exit(main())
