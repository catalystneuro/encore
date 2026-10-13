"""Print one line per step of an agent run, as it happens, for the workflow log.

    claude -p ... --output-format stream-json --verbose | tee run.jsonl | python tools/progress.py

Reads the stream on stdin and prints the time and, for each message of the
agent or a subagent, its first line, and for each tool call, the tool and a
short form of its input (the command, the file or the URL). Tool results are
not printed, so the text of the paper and of the data never reaches the log;
tools/transcript.py writes the full record at the end.
"""

from __future__ import annotations

import datetime
import json
import re
import sys

WIDTH = 160
RUNNER_HOME = re.compile(r"/home/runner/work/[^/\s]+/[^/\s]+/?")


def short(text: str) -> str:
    line = RUNNER_HOME.sub("", " ".join(str(text).split()))
    return line if len(line) <= WIDTH else line[:WIDTH - 1] + "…"


def describe(event: dict) -> list[str]:
    if event.get("type") == "system" and event.get("subtype") == "init":
        return [f"started: model {event.get('model')}, Claude Code {event.get('claude_code_version')}"]
    if event.get("type") == "result":
        return [f"finished: {event.get('subtype')}, {event.get('num_turns')} turns"]
    if event.get("type") != "assistant":
        return []
    who = "subagent " if event.get("parent_tool_use_id") else ""
    lines = []
    for block in (event.get("message") or {}).get("content") or []:
        if block.get("type") == "text" and block.get("text", "").strip():
            lines.append(f"{who}says: {short(block['text'].strip().splitlines()[0])}")
        elif block.get("type") == "tool_use":
            args = block.get("input") or {}
            detail = next((args[k] for k in ("command", "file_path", "path", "url", "pattern", "description",
                                              "query") if args.get(k)), "")
            lines.append(f"{who}{block.get('name')}: {short(detail)}")
    return lines


def main() -> int:
    for line in sys.stdin:
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        for text in describe(event):
            print(f"{datetime.datetime.now(datetime.timezone.utc):%H:%M:%S} {text}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
