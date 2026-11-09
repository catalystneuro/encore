"""encore: check a dataset against the paper it came from (docs/encore.md).

    encore check DATA --paper PAPER [--doi DOI] [--title T] [--full] [--out DIR] [--model M]
    encore status [DIR]
    encore request DATASET --why TEXT [--draft | --version V]
    encore queue
"""

from __future__ import annotations

import argparse
import datetime
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

from . import __version__
from .run import Dataset, Run, Stop, dataset_of, slug

REPO = "catalystneuro/encore"
MODEL = "claude-opus-5-5"


def check(args) -> int:
    out = args.out
    if out is None:
        name = args.data.rstrip("/").rsplit("/", 1)[-1] or "dataset"
        out = Path(f"encore-{slug(name)}-{datetime.date.today():%Y-%m-%d}")
    out = Path(out)
    state = out / "state.json"
    if state.is_file():
        saved = json.loads(state.read_text())
        dataset = Dataset(**saved["dataset"])
    else:
        dataset = dataset_of(args.data, args.version or ("draft" if args.draft else ""))
    run = Run(out, dataset, args.paper, args.doi, args.title, args.full, args.model, args.ref, sandbox=not args.no_sandbox)
    report = run.go()
    print(f"\n{report.read_text()}\nReport: {report}")
    return 0


def status(args) -> int:
    out = Path(args.dir) if args.dir else max(Path(".").glob("encore-*/state.json"), default=None,
                                              key=lambda p: p.stat().st_mtime)
    if out is None:
        print("No encore run here. Give its directory: encore status DIR")
        return 1
    state_path = out if out.name == "state.json" else out / "state.json"
    state = json.loads(state_path.read_text())
    print(f"{state['title']} · {state['dataset']['location']} · {state['mode']} run, started {state['started'][:16]}")
    for role, r in state["roles"].items():
        print(f"  {role:<18} {r['status']:<8} {r.get('started', '')[11:16]}–{r.get('finished', '')[11:16]}")
    running = [r for r, v in state["roles"].items() if v["status"] == "running"]
    if running:
        stream = state_path.parent / "logs" / f"{running[0]}.jsonl"
        tools = state_path.parent / "registry" / "tools" / "progress.py"
        if stream.is_file() and tools.is_file():
            lines = subprocess.run([sys.executable, str(tools)], input=stream.read_text(), capture_output=True,
                                   text=True).stdout.splitlines()
            print(f"\nThe last steps of {running[0]}:")
            print("\n".join("  " + line for line in lines[-8:]))
    if state.get("finished"):
        print(f"\nFinished {state['finished'][:16]}: {state_path.parent / 'report.md'}")
    return 0


def request(args) -> int:
    if shutil.which("gh") is None:
        print("encore request needs the GitHub CLI (gh), signed in: https://cli.github.com")
        return 1
    version = ("draft" if args.draft else "the published version below" if args.version else "latest published")
    body = (f"### Dataset\n\n{args.dataset}\n\n### Version\n\n{version}\n\n### Published version\n\n"
            f"{args.version or '_No response_'}\n\n### Why\n\n{args.why}\n")
    url = subprocess.run(["gh", "issue", "create", "--repo", REPO, "--title", f"Run request: {args.dataset}",
                          "--label", "run-request", "--body", body], check=True, capture_output=True,
                         text=True).stdout.strip()
    print(f"Requested: {url}\nIts place in the queue: encore queue")
    return 0


def queue(args) -> int:
    api = f"https://api.github.com/repos/{REPO}/issues?labels=queue-board&state=open"
    with urllib.request.urlopen(urllib.request.Request(api, headers={"Accept": "application/vnd.github+json"})) as r:
        boards = json.load(r)
    if not boards:
        print("The queue board is not up yet.")
        return 1
    print(boards[0]["body"])
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="encore", description="Check a dataset against the paper it came from.")
    parser.add_argument("--version", action="version", version=f"encore {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    c = sub.add_parser("check", help="test a paper's claims on a dataset, on this machine")
    c.add_argument("data", help="a directory of files, a URL, or a dataset in an archive (DANDI:000147)")
    c.add_argument("--paper", type=Path, help="the paper, as a PDF or a text file")
    c.add_argument("--doi", help="the paper's DOI, when the PDF does not show it")
    c.add_argument("--title", help="the paper's title, for the report")
    c.add_argument("--full", action="store_true", help="add the verification rounds (several hours more)")
    c.add_argument("--draft", action="store_true", help="for a DANDI dataset: use its draft")
    c.add_argument("--version", dest="version", help="for an archive dataset: the version to use")
    c.add_argument("--out", help="where the run and its report go (default: ./encore-<name>-<date>)")
    c.add_argument("--model", default=MODEL)
    c.add_argument("--ref", default="main", help="the registry's branch or tag to take the protocol from")
    c.add_argument("--no-sandbox", action="store_true", help="run the agents' commands outside Claude Code's sandbox")
    c.set_defaults(func=check)

    s = sub.add_parser("status", help="how far a run has got")
    s.add_argument("dir", nargs="?")
    s.set_defaults(func=status)

    r = sub.add_parser("request", help="ask for an attempt on the registry's shared queue")
    r.add_argument("dataset", help="as in the registry: 000147, DANDI:000147, CRCNS:ret-1")
    r.add_argument("--why", required=True, help="what changed; links to the conversion's issue or pull request")
    g = r.add_mutually_exclusive_group()
    g.add_argument("--draft", action="store_true")
    g.add_argument("--version", dest="version")
    r.set_defaults(func=request)

    q = sub.add_parser("queue", help="the registry's shared queue")
    q.set_defaults(func=queue)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Stop as stop:
        print(f"\nencore: {stop}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nencore: stopped. Run the same command again to go on from where it was.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
