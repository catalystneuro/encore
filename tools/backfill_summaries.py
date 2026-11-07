"""Write summaries/<attempt>.md for attempts recorded before the recorder wrote summaries (docs/agents/recorder.md, step 2).

    python tools/backfill_summaries.py [--model MODEL] [--limit N] [ATTEMPT_ID ...]

Without ids it takes every current attempt on the checkout that has no summary. For each, it gives the agent the
same sources the recorder reads, inline (the attempt record, its claims file and the agents' reports), with the
instructions of the recorder's step 2, and writes the paragraph it returns. It uses the Claude Code CLI on this
machine (`claude -p`), so it runs on the account that CLI is logged in to.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def step2() -> str:
    text = (ROOT / "docs" / "agents" / "recorder.md").read_text()
    m = re.search(r"\n2\. Write the attempt's summary.*?(?=\n\nWrite prose plainly)", text, re.S)
    style = re.search(r"Write prose plainly:.*?the sources do not state\.", text, re.S)
    return m.group(0).strip() + "\n\n" + style.group(0).replace(" Do not commit or push: the workflow commits your changes.", "")


def sources(attempt_id: str) -> str:
    a_path = ROOT / "attempts" / f"{attempt_id}.yaml"
    folder = folder_of(attempt_id)
    parts = [f"=== attempts/{attempt_id}.yaml\n{a_path.read_text()}"]
    for c in sorted((ROOT / "claims" / folder).glob("*.yaml")):
        parts.append(f"=== {c.relative_to(ROOT)}\n{c.read_text()}")
    t = ROOT / "transcripts" / folder
    for r in sorted(t.glob("*report*.md")) if t.is_dir() else []:
        parts.append(f"=== {r.relative_to(ROOT)}\n{r.read_text()[:20000]}")
    return "\n\n".join(parts)


def folder_of(attempt_id: str) -> str:
    return re.sub(r"-[a-z][^-]*-\d{4}-\d{2}$", "", attempt_id)


META = re.compile(r"write tool|file-writing|no tools|I could(?:n't| not) (?:write|save)|I did not (?:write|save)|<invoke|parameter name|the paragraph above", re.I)


def paragraph(reply: str) -> str:
    """The summary in a reply: inside <summary> tags, or a mock Write call's content, without notes about files."""
    for pat in (r"<summary>(.*?)</summary>", r'<parameter name="content">(.*?)</parameter>'):
        m = re.search(pat, reply, re.S)
        if m:
            reply = m.group(1); break
    sentences = re.split(r"(?<=[.!?])\s+", " ".join(reply.split()))
    return " ".join(x for x in sentences if not META.search(x)).strip()


def write(attempt_id: str, model: str) -> str:
    prompt = (f"You are writing the summary of a finished attempt in the reproduction registry. The attempt is `{attempt_id}`.\n\n"
              + step2().replace("{attempt}", attempt_id).replace("From the same sources as the notes:", "From the sources below:")
              + "\n\nReply with the paragraph only.\n\n" + sources(attempt_id))
    for _ in range(2):
        out = subprocess.run(["claude", "-p", "--model", model, "--tools", ""], input=prompt,
                             capture_output=True, text=True, timeout=1200)
        if out.returncode != 0 or not out.stdout.strip():
            raise RuntimeError((out.stderr or out.stdout)[-400:])
        text = paragraph(out.stdout)
        if text and not META.search(out.stdout):
            break
    if not text:
        raise RuntimeError("no paragraph in the reply")
    (ROOT / "summaries" / f"{attempt_id}.md").write_text(text + "\n")
    return text


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("ids", nargs="*"); ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--limit", type=int, default=0); args = ap.parse_args()
    ids = args.ids or sorted(p.stem for p in (ROOT / "attempts").glob("*.yaml")
                             if not (ROOT / "summaries" / f"{p.stem}.md").exists())
    for i, aid in enumerate(ids[: args.limit or None], 1):
        try:
            text = write(aid, args.model); print(f"[{i}/{len(ids)}] {aid}: {len(text.split())} words", flush=True)
        except Exception as err:  # one failure does not stop the rest
            print(f"[{i}/{len(ids)}] {aid}: FAILED {err}", file=sys.stderr, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
