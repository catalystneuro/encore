"""Tests for tools/flagged.py: telling when the account's safety checks flagged a run."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import flagged  # noqa: E402

MODEL = "claude-opus-5-5"


def assistant(model=MODEL, stop="end_turn", parent=None):
    return json.dumps({"type": "assistant", "parent_tool_use_id": parent,
                       "message": {"model": model, "stop_reason": stop, "content": []}})


def test_a_clean_run_is_not_flagged():
    lines = [assistant(), assistant(), json.dumps({"type": "result", "is_error": False, "result": "done"})]
    assert flagged.reasons(lines, "", MODEL) == []


def test_a_refusal_is_flagged():
    assert flagged.reasons([assistant(), assistant(stop="refusal")], "", MODEL) == ["the model refused"]


def test_a_refusal_names_its_category():
    msg = json.dumps({"type": "assistant", "message": {"model": MODEL, "stop_reason": "refusal",
                                                       "stop_details": {"type": "refusal", "category": "bio"}}})
    assert flagged.reasons([msg], "", MODEL) == ["the model refused (bio)"]


def test_a_request_answered_by_a_fallback_model_is_flagged_but_not_a_small_subagent_model():
    assert flagged.reasons([assistant("claude-haiku-5-5", parent="toolu_1")], "", MODEL) == []
    assert flagged.reasons([assistant(f"{MODEL}-20261001")], "", MODEL) == []
    assert flagged.reasons([assistant("claude-opus-5", parent="toolu_1")], "", MODEL) == [
        "a request was answered by claude-opus-5"]
    usage = json.dumps({"type": "result", "is_error": False, "result": "done",
                        "modelUsage": {MODEL: {}, "claude-haiku-5-5": {}, "claude-opus-4-8": {}}})
    assert flagged.reasons([usage], "", MODEL) == ["a request was answered by claude-opus-4-8"]


def test_a_response_stopped_by_a_safety_classifier_is_flagged():
    # wang-2019's reader, 2026-11-18: the classifier stopped the response that wrote the claims file, the run went
    # on and ended as a success, and the chain stopped for a person. It is a flag: the role runs again on verified.
    stop = ("Your response above was stopped by a safety classifier — this is not a tool or API error. The rest of "
            "it was withheld, and tool calls in it that had not finished did not run.")
    done = json.dumps({"type": "result", "is_error": False, "result": "I didn't write the file."})
    for content in (stop, [{"type": "text", "text": stop}]):
        lines = [assistant(), json.dumps({"type": "user", "message": {"role": "user", "content": content}}), assistant(), done]
        assert flagged.reasons(lines, "", MODEL) == ["a safety classifier stopped a response, and its tool calls did not run"]
    # The same words in a tool's result (a transcript the agent read) are not a flag, nor in the agent's own text.
    quoted = json.dumps({"type": "user", "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "t1", "content": stop}]}})
    assert flagged.reasons([assistant(), quoted, done], "", MODEL) == []


def test_claude_codes_flag_messages_are_flagged_and_other_errors_are_not():
    flag = json.dumps({"type": "result", "is_error": True,
                       "result": "API Error: Opus 5.5's safeguards flagged this message."})
    limit = json.dumps({"type": "result", "is_error": True, "result": "Claude AI usage limit reached"})
    report = json.dumps({"type": "result", "is_error": False, "result": "Two sessions were flagged as duplicates."})
    assert flagged.reasons([flag], "", MODEL)
    assert flagged.reasons([limit], "", MODEL) == [] and flagged.reasons([report], "", MODEL) == []
    assert flagged.reasons([], "API Error: Output blocked by content filtering policy", MODEL)
