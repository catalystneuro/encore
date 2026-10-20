"""Say whether the account's safety checks flagged an agent run.

    python tools/flagged.py RUN.jsonl [STDERR.txt] --model MODEL

Reads Claude Code's stream-json output (and its stderr, if given). A run is flagged when a request
was refused (`stop_reason: refusal`, which in -p ends the turn), when a request was answered by a
model other than the one asked for (a flagged subagent is re-run on a fallback model, such as Opus 5
for a biology flag; small models a subagent uses on purpose are allowed), or when a message says it
was flagged in the words Claude Code uses (code.claude.com/docs/en/errors). The exit code is not
used: a refusal can end a run that exits 0. Prints the reason and exits 1 when flagged, else 0.
Used by the workflows on the unverified account (docs/pipeline.md, "Accounts").
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# The messages Claude Code gives when a request is flagged (code.claude.com/docs/en/errors).
FLAG_TEXT = re.compile(r"safeguards flagged|content filtering policy|violate our usage policy|"
                       r"can't help with this\. start a new session|refused by the safety safeguard", re.I)


def other_model(served: str, model: str) -> bool:
    """A model other than the one asked for, other than a small one a subagent may use on purpose."""
    served = re.sub(r"-\d{8}$", "", served)
    return bool(served) and served not in (model, "<synthetic>") and "haiku" not in served


def reasons(lines: list[str], stderr: str, model: str) -> list[str]:
    found = []
    for line in lines:
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        if msg.get("type") == "assistant":
            body = msg.get("message") or {}
            if body.get("stop_reason") == "refusal":
                category = (body.get("stop_details") or {}).get("category")
                found.append("the model refused" + (f" ({category})" if category else ""))
            # In -p the main conversation ends on a refusal; a subagent is re-run on a fallback model.
            if other_model(body.get("model") or "", model):
                found.append(f"a request was answered by {body['model']}")
            text = " ".join(c.get("text", "") for c in body.get("content") or [] if isinstance(c, dict))
            if FLAG_TEXT.search(text):
                found.append(f"the conversation says: {' '.join(text.split())[:200]}")
        elif msg.get("type") == "result":
            if msg.get("stop_reason") == "refusal":
                found.append("the run ended on a refusal")
            for served in msg.get("modelUsage") or {}:
                if other_model(served, model):
                    found.append(f"a request was answered by {served}")
            text = str(msg.get("result") or "") + " " + " ".join(map(str, msg.get("errors") or []))
            if FLAG_TEXT.search(text):
                found.append(f"the run ended on: {' '.join(text.split())[:200]}")
    for line in stderr.splitlines():
        if FLAG_TEXT.search(line):
            found.append(f"stderr: {line.strip()[:200]}")
            break
    return list(dict.fromkeys(found))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run")
    parser.add_argument("stderr", nargs="?")
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    lines = Path(args.run).read_text(errors="replace").splitlines() if Path(args.run).is_file() else []
    stderr = Path(args.stderr).read_text(errors="replace") if args.stderr and Path(args.stderr).is_file() else ""
    found = reasons(lines, stderr, args.model)
    if found:
        print("; ".join(found))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
