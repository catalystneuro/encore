"""tools/publish_site.py: which files a publish uploads and deletes in the site's bucket."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import publish_site  # noqa: E402


def test_only_new_and_changed_files_are_uploaded_and_only_files_no_longer_built_are_deleted():
    local = {"index.html": "a", "papers/x/index.html": "b", "api/new.json": "c"}
    remote = {"index.html": "a", "papers/x/index.html": "old", "papers/gone/index.html": "d",
              "pr-preview/pr-7/index.html": "e"}
    upload, delete = publish_site.plan(local, remote, "")
    assert upload == ["api/new.json", "papers/x/index.html"]
    # The site's publish keeps the previews of open pull requests.
    assert delete == ["papers/gone/index.html"]


def test_a_preview_replaces_only_its_own_folder():
    local = {"pr-preview/pr-7/index.html": "new"}
    remote = {"pr-preview/pr-7/index.html": "old", "pr-preview/pr-7/papers/gone/index.html": "x",
              "pr-preview/pr-8/index.html": "y", "index.html": "z"}
    upload, delete = publish_site.plan(local, remote, "pr-preview/pr-7/")
    assert upload == ["pr-preview/pr-7/index.html"] and delete == ["pr-preview/pr-7/papers/gone/index.html"]


def test_each_kind_of_file_is_served_with_its_type():
    assert publish_site.content_type(Path("a/index.html")) == "text/html; charset=utf-8"
    assert publish_site.content_type(Path("badge/x.svg")) == "image/svg+xml"
    assert publish_site.content_type(Path("api/p.json")) == "application/json"
    assert publish_site.content_type(Path("assets/fonts/inter.woff2")) == "font/woff2"
