"""Tests for tools/progress.py: the live log of an agent run."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import progress as tool  # noqa: E402


def test_prints_messages_and_tool_calls_but_not_tool_output():
    events = [
        {"type": "system", "subtype": "init", "model": "m", "claude_code_version": "1"},
        {"type": "assistant", "message": {"content": [
            {"type": "text", "text": "Reading the paper.\nSecond line."},
            {"type": "tool_use", "name": "Bash",
             "input": {"command": "cd /home/runner/work/registry/registry/entries && ls"}}]}},
        {"type": "user", "message": {"content": [
            {"type": "tool_result", "content": "Methods. We recorded from twenty patients."}]}},
        {"type": "assistant", "parent_tool_use_id": "x", "message": {"content": [
            {"type": "tool_use", "name": "WebFetch", "input": {"url": "https://doi.org/10.1/x", "prompt": "p"}}]}},
        {"type": "result", "subtype": "success", "num_turns": 3},
    ]
    lines = [line for e in events for line in tool.describe(e)]
    assert lines == ["started: model m, Claude Code 1", "says: Reading the paper.",
                     "Bash: cd entries && ls", "subagent WebFetch: https://doi.org/10.1/x",
                     "finished: success, 3 turns"]


def test_long_input_is_cut():
    event = {"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": "Bash", "input": {"command": "x" * 500}}]}}
    assert len(tool.describe(event)[0]) <= tool.WIDTH + len("Bash: ")
