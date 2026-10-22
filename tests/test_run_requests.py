"""Tests for tools/runner/run_requests.py: reading run requests and ordering the queue."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools" / "runner"))

import run_requests as rr  # noqa: E402

STEER = {"bendichter", "pauladkisson"}


def body(dataset="000147", version="draft", published="_No response_", why="Fixed the units."):
    return (f"### Dataset\n\n{dataset}\n\n### Version\n\n{version}\n\n"
            f"### Published version\n\n{published}\n\n### Why\n\n{why}\n")


def issue(number=1, author="bendichter", labels=(), created="2026-10-22T10:00:00Z", **form):
    return {"number": number, "author": {"login": author}, "labels": [{"name": x} for x in labels],
            "createdAt": created, "body": body(**form)}


def labeled(label, who, event="labeled"):
    return {"event": event, "label": {"name": label}, "actor": {"login": who}}


def test_the_form_is_read_by_its_labels():
    answers = rr.form(body(why="Line one.\nLine two."))
    assert answers == {"Dataset": "000147", "Version": "draft", "Published version": "", "Why": "Line one.\nLine two."}


def test_a_request_gives_a_folder_and_a_version():
    assert rr.request(body())[:2] == ("000147", "draft")
    assert rr.request(body(version="latest published"))[:2] == ("000147", "")
    assert rr.request(body(version="the published version below", published="0.260521.2201"))[:2] == \
        ("000147", "0.260521.2201")
    assert rr.request(body(dataset="CRCNS:ret-1"))[0] == "crcns-ret-1"


def test_a_request_that_could_reach_the_shell_is_refused():
    for bad in ("000147; rm -rf ~", "$(curl x)", "000147 draft", ""):
        assert rr.request(body(dataset=bad))[2], bad
    assert rr.request(body(version="the published version below", published="draft; echo"))[2]
    assert rr.request(body(version="something else"))[2]


def test_a_label_counts_for_whoever_added_it_last():
    assert rr.last_labeler([labeled("priority", "x"), labeled("priority", "bendichter")], "priority") == "bendichter"
    assert rr.last_labeler([labeled("priority", "bendichter"), labeled("priority", "y", "unlabeled")], "priority") is None
    assert rr.last_labeler([labeled("approved", "bendichter")], "priority") is None


def test_a_request_from_the_list_is_queued_and_others_wait_for_approval():
    assert rr.state(issue(), [], STEER)[0] == "queued"
    assert rr.state(issue(author="someone"), [], STEER)[0] == "awaiting-approval"
    approved = issue(author="someone", labels=["approved"])
    assert rr.state(approved, [labeled("approved", "pauladkisson")], STEER)[0] == "queued"


def test_steering_labels_from_outside_the_list_are_taken_off():
    new, drop, notes = rr.state(issue(author="someone", labels=["approved", "priority"]),
                                [labeled("approved", "someone"), labeled("priority", "someone")], STEER)
    assert new == "awaiting-approval" and drop == ["approved", "priority"] and len(notes) == 2


def test_running_and_stopped_requests_keep_their_state():
    assert rr.state(issue(labels=["running"]), [], STEER)[0] == "running"
    assert rr.state(issue(labels=["needs-you"]), [], STEER)[0] == "needs-you"
    assert rr.state(issue(labels=["running"], dataset="nope!"), [], STEER)[0] == "invalid"


def test_priority_runs_first_then_the_oldest():
    a = issue(1, labels=["queued"], created="2026-10-22T09:00:00Z")
    b = issue(2, labels=["queued", "priority"], created="2026-10-22T11:00:00Z")
    c = issue(3, labels=["queued"], created="2026-10-22T08:00:00Z")
    d = issue(4, labels=["awaiting-approval"], created="2026-10-22T07:00:00Z")
    assert [i["number"] for i in rr.order([a, b, c, d])] == [2, 3, 1]
