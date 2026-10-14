"""Turn an agent run's transcript into a Markdown record that can be published.

    python tools/transcript.py run.jsonl transcripts/<dandiset>/<name>.md [--title TITLE]
        [--omit PATH ...] [--home DIR] [--report REPORT.md]

Reads the newline-delimited JSON that `claude -p --output-format stream-json
--verbose` prints, or a Claude Code session file (~/.claude/projects/...jsonl).
Writes the prompt, every message of the agent and of its subagents, and every
tool call. It leaves out what should not be republished or is not part of the
run:

- the session context: system reminders, attachments, the system prompt;
- thinking blocks;
- the text of fetched web pages (WebFetch, WebSearch, and curl or wget of a
  URL), which are papers more often than not; the URL is kept;
- the output of any tool call that names a path given with --omit, by
  default `paper/`, where the prompts tell agents to keep a paper's text;
- all but the first lines of every other tool result.

Anything left that looks private, an e-mail address, a token or key, a
private key block or a path in a home directory, is replaced by a note saying
what was removed, and each removal is reported by kind and line, never by its
text. --home DIR rewrites DIR to
`~`, and the user's name elsewhere to `user`, for a run exported from a local
machine. Runs in CI on a fresh runner
have none of these; the check is there in case one is exported from elsewhere.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MAX_LINES = 20           # of a tool result
MAX_CHARS = 2000
FETCHING = re.compile(r"\b(curl|wget)\b[^\n]*https?://")
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
RUNNER_HOME = re.compile(r"/home/runner/work/[^/\s]+/[^/\s]+/?")

PRIVATE = {
    # A real top-level domain, so that code such as `X@np.ones` is not taken for an address.
    "an e-mail address": re.compile(r"\b[A-Za-z0-9._%+-]+@(?!(?:anthropic\.com|users\.noreply\.github\.com)\b)"
                                    r"(?:[A-Za-z0-9-]+\.)+(?:com|org|net|edu|gov|mil|int|io|ai|co|me|info|"
                                    r"[a-z]{2})\b(?!\()"),
    "an Anthropic key or token": re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}"),
    "a GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"),
    "an AWS key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "a private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "a home directory path": re.compile(r"(?:/Users/|/home/(?!runner\b))[A-Za-z0-9._-]+"),
}


def messages(path: Path):
    """(kind, message, subagent) for each user or assistant message, in order."""
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        if event.get("type") in ("user", "assistant") and isinstance(event.get("message"), dict):
            subagent = bool(event.get("parent_tool_use_id"))
            yield event["type"], event["message"], subagent
        elif event.get("type") == "system" and event.get("subtype") == "init":
            yield "init", event, False
        elif event.get("type") == "result":
            yield "result", event, False


def clean(text: str) -> str:
    return RUNNER_HOME.sub("", REMINDER.sub("", text)).strip()


def shorten(text: str) -> str:
    lines = text.splitlines()
    out = "\n".join(lines[:MAX_LINES])[:MAX_CHARS]
    dropped = len(lines) - len(out.splitlines())
    if dropped > 0 or len(text) > len(out) + 1:
        out += f"\n[... {max(dropped, 1)} more lines not kept]"
    return out


def result_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")
    return ""


def fence(text: str, info: str = "") -> str:
    ticks = "````" if "```" in text else "```"
    return f"{ticks}{info}\n{text}\n{ticks}\n"


def render(path: Path, title: str, omit=("paper/",), home: str | None = None) -> str:
    out = [f"# {title}\n"]
    calls: dict[str, dict] = {}         # tool_use id -> the call, to treat its result
    first_prompt = True
    for kind, msg, subagent in messages(path):
        if kind == "init":
            out.append(f"Model `{msg.get('model')}`, Claude Code {msg.get('claude_code_version', 'version not given')}, "
                       f"permission mode `{msg.get('permissionMode')}`. Tools: "
                       + ", ".join(f"`{t}`" for t in msg.get("tools", [])) + ".\n")
            continue
        if kind == "result":
            out.append(f"## End of run\n\n{msg.get('num_turns')} turns, "
                       f"{round((msg.get('duration_ms') or 0) / 60000)} minutes, "
                       f"result: {msg.get('subtype')}.\n")
            continue
        who = "Subagent" if subagent else ("Prompt" if kind == "user" else "Agent")
        content = msg.get("content")
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        for block in content or []:
            t = block.get("type")
            if t == "text":
                text = clean(block["text"])
                if not text:
                    continue
                if kind == "user" and first_prompt and not subagent:
                    out.append(f"## Prompt\n\n{text}\n")
                    first_prompt = False
                elif kind == "user":
                    out.append(f"**{'Subagent prompt' if subagent else 'Message'}**\n\n{text}\n")
                else:
                    out.append(f"**{who}**\n\n{text}\n")
            elif t == "tool_use":
                calls[block["id"]] = block
                args = dict(block.get("input") or {})
                command = args.pop("command", None)
                label = f"**{who} calls {block['name']}**"
                if command is not None:
                    out.append(f"{label}\n\n" + fence(clean(command), "bash"))
                else:
                    out.append(f"{label}\n\n" + fence(clean(json.dumps(args, indent=1, ensure_ascii=False)), "json"))
            elif t == "tool_result":
                call = calls.get(block.get("tool_use_id"), {})
                name = call.get("name", "")
                command = (call.get("input") or {}).get("command", "")
                if name in ("WebFetch", "WebSearch") or FETCHING.search(command or ""):
                    out.append("Result: the fetched text is not kept.\n")
                    continue
                if any(o in json.dumps(call.get("input") or {}) for o in omit):
                    out.append("Result: not kept, because it reads the paper's text.\n")
                    continue
                text = clean(result_text(block.get("content")))
                out.append(fence(shorten(text)) if text else "Result: no output.\n")
    return redact_home("\n".join(out), home)


def redact_home(text: str, home: str | None) -> str:
    """The home directory as ~, and the user's name, which appears in other paths and listings, as `user`."""
    if not home:
        return text
    home = home.rstrip("/")
    return re.sub(rf"\b{re.escape(Path(home).name)}\b", "user", text.replace(home, "~"))


def final_message(path: Path) -> str:
    """The text of the run's last message: the `result` event, else the last text of the main agent."""
    last = ""
    for kind, msg, subagent in messages(path):
        if kind == "result" and msg.get("result"):
            return clean(msg["result"])
        if kind == "assistant" and not subagent:
            content = msg.get("content")
            texts = [b["text"] for b in content if isinstance(b, dict) and b.get("type") == "text"] \
                if isinstance(content, list) else [content or ""]
            if any(t.strip() for t in texts):
                last = clean("\n".join(texts))
    return last


def redact(text: str) -> tuple[str, list[str]]:
    """The text with anything that looks private replaced, and where each removal was (kind and line)."""
    removed = []
    for what, pattern in PRIVATE.items():
        for m in pattern.finditer(text):
            removed.append(f"{what} near line {text.count(chr(10), 0, m.start()) + 1}")
        text = pattern.sub(f"[removed: {what}]", text)
    return text, removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", default="Transcript of an agent run")
    parser.add_argument("--omit", action="append", default=None,
                        help="leave out the output of tool calls that name this path (default: paper/)")
    parser.add_argument("--home", help="rewrite this home directory to ~")
    parser.add_argument("--report", type=Path, help="also write the run's final message here")
    args = parser.parse_args()
    text = render(args.source, args.title, tuple(args.omit or ["paper/"]), args.home)
    report = final_message(args.source)
    report = redact_home(report, args.home)
    text, removed = redact(text)
    report, removed_from_report = redact(report)
    for where, items in (("transcript", removed), ("report", removed_from_report if args.report else [])):
        if items:
            print(f"removed from the {where}:", *items, sep="\n  ", file=sys.stderr)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text)
    print(f"wrote {args.output} ({len(text) // 1024} KB)")
    if args.report:
        args.report.write_text(report + "\n")
        print(f"wrote {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
