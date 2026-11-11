"""Copies of the entries that open and run in Google Colab, for the `colab` branch.

    python tools/colab.py build OUT [ENTRY ...]     # every entry, or those named, into OUT/entries/<name>/

Colab opens a notebook from GitHub (https://colab.research.google.com/github/catalystneuro/encore/blob/colab/
entries/<name>/<notebook>.ipynb), but not the files beside it, and with its own Python and packages. Each copy has:

- the entry's notebooks, each with a first cell that, on Colab only, fetches the entry's files from the `colab`
  branch and installs its pinned packages, and does nothing anywhere else;
- the entry's helpers, entry.yaml, requirements.in and requirements.lock.txt, as they are;
- requirements.colab-<version>.txt: the same requirements locked for each Python version Colab may run
  (COLAB_PYTHONS), as Colab picks its own and changes it over time. The setup cell takes the one for the running
  Python; the entry's own lock stays the record of how its results were produced.

Run by .github/workflows/colab.yml, which commits OUT to the `colab` branch.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import nbformat
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPO = "catalystneuro/encore"
BRANCH = "colab"
# The Python versions Colab has run or may run next; a lock is made for each. Add one when Colab moves.
COLAB_PYTHONS = ("3.12", "3.13")

SETUP = '''# On Google Colab: fetch this entry's files and install its pinned packages. Elsewhere this cell does nothing.
import sys
if "google.colab" in sys.modules:
    import os, subprocess
    if not os.path.isdir("/content/encore"):
        subprocess.run(["git", "clone", "-q", "--depth", "1", "--branch", "{branch}", "--filter=blob:none", "--sparse",
                        "https://github.com/{repo}", "/content/encore"], check=True)
        subprocess.run(["git", "-C", "/content/encore", "sparse-checkout", "set", "entries/{name}"], check=True)
    os.chdir("/content/encore/entries/{name}")
    sys.path.insert(0, os.getcwd())
    version = f"{{sys.version_info.major}}.{{sys.version_info.minor}}"
    lock = f"requirements.colab-{{version}}.txt"
    if not os.path.exists(lock):
        print(f"No lock for Python {{version}}: installing the entry's unpinned requirements (requirements.in).")
        lock = "requirements.in"
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "uv"], check=True)
    subprocess.run(["uv", "pip", "install", "--system", "-q", "-r", lock], check=True)
    print("Installed. If Colab asks to restart the session, restart it and run the notebook from the top again.")
'''

INTRO = ("**Running this on Google Colab.** The first code cell fetches this entry's files and installs the "
         "packages it was run with, pinned for Colab's Python version. The results in the registry come from the "
         "entry's own environment ([requirements.lock.txt](requirements.lock.txt), Python {python}); a different "
         "Python or platform can change the last digits of some numbers.")


def entry_python(entry_dir: Path) -> str:
    sys.path.insert(0, str(ROOT / "tools"))
    import entry as entry_tool
    return entry_tool.python_of(entry_dir)


def build_entry(entry_dir: Path, out: Path) -> list[str]:
    """Write the entry's Colab copy into out/<name>/; return the problems found (a lock that could not be made)."""
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    name = entry["name"]
    dest = out / name
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for f in ["entry.yaml", "requirements.in", "requirements.lock.txt", *(entry.get("helpers") or [])]:
        if (entry_dir / f).is_file():
            shutil.copy(entry_dir / f, dest / f)
    python = entry_python(entry_dir)
    for n in entry["notebooks"]:
        nb = nbformat.read(entry_dir / n["path"], as_version=4)
        intro = nbformat.v4.new_markdown_cell(INTRO.format(python=python))
        setup = nbformat.v4.new_code_cell(SETUP.format(branch=BRANCH, repo=REPO, name=name))
        setup.metadata["tags"] = ["colab-setup"]
        intro.metadata["tags"] = ["colab-setup"]
        nb.cells = [intro, setup, *nb.cells]
        nb.metadata.setdefault("colab", {})["name"] = n["path"]
        nbformat.write(nb, dest / n["path"])
    problems = []
    for version in COLAB_PYTHONS:
        r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
                            "--python-platform", "linux", "requirements.in", "-o", str(dest / f"requirements.colab-{version}.txt")],
                           cwd=entry_dir, capture_output=True, text=True)
        if r.returncode:
            problems.append(f"{name}: no lock for Python {version}: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ''}")
    return problems


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] != "build":
        raise SystemExit(__doc__)
    out = Path(sys.argv[2]) / "entries"
    out.mkdir(parents=True, exist_ok=True)
    names = sys.argv[3:]
    dirs = [ROOT / "entries" / n for n in names] if names else sorted(p.parent for p in (ROOT / "entries").glob("*/entry.yaml"))
    problems = []
    for d in dirs:
        if not (d / "entry.yaml").is_file():
            # An entry removed or renamed on main: its copy goes too.
            shutil.rmtree(out / d.name, ignore_errors=True)
            print(f"removed {d.name}")
            continue
        problems += build_entry(d, out)
        print(f"built {d.name}")
    for p in problems:
        print(f"warning: {p}", file=sys.stderr)
    (Path(sys.argv[2]) / "README.md").write_text(
        "# Colab copies of the registry's entries\n\nBuilt by tools/colab.py on the main branch; do not edit here. "
        "Open a notebook in Colab at https://colab.research.google.com/github/catalystneuro/encore/blob/colab/"
        "entries/<entry>/<notebook>.ipynb\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
