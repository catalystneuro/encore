"""Tests for tools/agent_run.py: the prompts and materials of an agent run."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import agent_run as tool  # noqa: E402


@pytest.mark.parametrize("role", tool.ROLES)
def test_every_role_has_a_prompt(role):
    assert (REPO / "docs" / "agents" / f"{tool.TEMPLATES[role]}.md").is_file()


def test_the_author_prompt_names_the_target():
    text = tool.fill("author", "000147", "claude-opus-5-5")
    assert "dandiset 000147" in text and "doi:10.7554/elife.74478" in text and "claude-opus-5-5" in text
    assert "{" not in text


def test_a_verifier_prompt_names_the_pinned_version():
    text = tool.fill("verifier-1", "000207", "m")
    assert "version 0.220216.0323" in text and "{" not in text


def test_a_revision_needs_the_verifiers_report():
    with pytest.raises(SystemExit, match="run verifier-1 first"):
        tool.fill("author-revise-1", "000207", "m")


def test_proposals_are_found_from_the_record():
    assert tool.proposals("001097") == ["fig2e-glm-behaviour-explains-little"]
    assert tool.proposals("001453") == []


def test_an_author_on_a_dandiset_with_an_attempt_gets_the_repeat_prompt():
    latest = tool.attempt_of("001754")[0]["id"]
    n = int(latest.rsplit("-", 1)[1])
    text = tool.fill("author", "001754", "m", version="draft")
    assert latest in text and f"attempts/001754-knierim-2000-{n + 1:02d}.yaml" in text
    assert "Use version draft" in text and "{" not in text


def test_a_first_author_without_a_version_picks_a_published_one(monkeypatch):
    monkeypatch.setattr(tool, "attempt_of", lambda dandiset: None)
    text = tool.fill("author", "001933", "m")
    assert "pinned published version" in text and "Use version" not in text
