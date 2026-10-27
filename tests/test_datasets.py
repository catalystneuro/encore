"""Tests for tools/datasets.py: how datasets are named, keyed and filed."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import datasets  # noqa: E402


@pytest.mark.parametrize("text", ["000003", "dandi:000003", "DANDI:000003", "Dandi:000003"])
def test_every_way_of_writing_a_dandi_dataset_gives_one_key(text):
    assert datasets.parse(text) == "dandi:000003"


def test_another_archive_is_filed_under_archive_and_id():
    key = datasets.parse("example:abc-123")
    assert key == "example:abc-123" and datasets.folder(key) == "example-abc-123"
    assert datasets.parse("example-abc-123") == key and datasets.label(key) == "EXAMPLE:abc-123"


def test_dandi_keeps_its_bare_folders_and_links():
    assert datasets.folder("dandi:000003") == "000003" and datasets.key_of_folder("000003") == "dandi:000003"
    assert datasets.url("dandi:000003") == "https://dandiarchive.org/dandiset/000003"


@pytest.mark.parametrize("text", ["3", "dandi:", "../000003", "dandi:00 3", "x"])
def test_anything_else_is_refused(text):
    with pytest.raises(ValueError):
        datasets.parse(text)


def test_targets_carry_their_key_and_folder():
    found = datasets.targets()
    assert found and all(t["key"] == f"{t['archive']}:{t['id']}" and t["folder"] == datasets.folder(t["key"])
                         for t in found)


def test_a_crcns_dataset_is_a_target_with_its_own_page():
    ret = next(t for t in datasets.targets() if t["key"] == "crcns:ret-1")
    assert ret["folder"] == "crcns-ret-1" and datasets.label(ret["key"]) == "CRCNS:ret-1"
    assert datasets.url(ret["key"]) == "https://crcns.org/data-sets/retina/ret-1"
    assert "crcnsarchive" in datasets.access(ret["key"])


def test_an_ebrains_dataset_is_named_by_its_doi_and_read_by_its_kg_id():
    key = datasets.parse("EBRAINS:Q0FG-1X8")
    found = next(t for t in datasets.targets() if t["key"] == key)
    assert key == "ebrains:q0fg-1x8" and found["folder"] == "ebrains-q0fg-1x8"
    assert datasets.label(key) == "EBRAINS:Q0FG-1X8" and datasets.parse("ebrains-q0fg-1x8") == key
    assert f'/public/datasets/{found["kg_id"]}/' in datasets.access(key)


def test_a_key_ignores_the_case_of_an_identifier_that_ignores_case():
    assert datasets.key_of("ebrains", "Q0FG-1X8") == datasets.key_of("ebrains", "q0fg-1x8") == "ebrains:q0fg-1x8"
    assert datasets.key_of("crcns", "ret-1") == "crcns:ret-1"


def test_a_dryad_dataset_is_named_by_its_doi_and_pinned_by_its_version_id():
    key = datasets.parse("DRYAD:BVQ83BKK9")
    found = next(t for t in datasets.targets() if t["key"] == key)
    assert key == "dryad:bvq83bkk9" and found["folder"] == "dryad-bvq83bkk9"
    assert datasets.label(key) == "DRYAD:bvq83bkk9" and datasets.parse("dryad-bvq83bkk9") == key
    assert found["doi"] == "10.5061/dryad.bvq83bkk9"
    assert f'/versions/{found["published_version"]}/files' in datasets.access(key)


def test_every_archive_is_an_adapter_with_a_section_in_the_docs():
    from archives import ALL
    docs = (REPO / "docs" / "archives.md").read_text()
    assert set(ALL) == set(datasets.ARCHIVES) and list(ALL)[0] == "dandi"
    for key, archive in ALL.items():
        assert archive.key == key and archive.list.endswith(".json")
        if key in ("local", "remote"):
            continue
        assert f"## {archive.name.removeprefix('the ')}" in docs or f"## {archive.label}" in docs, key
        assert archive.hosts, f"{key}: no hosts for an agent to reach"
        assert bool(archive.stage) == bool(archive.secrets), f"{key}: stage() and secrets go together"


def test_staging_skips_archives_agents_read_directly_and_needs_its_secrets(monkeypatch, capsys):
    import stage_files
    monkeypatch.delenv("DRYAD_CLIENT_ID", raising=False)
    monkeypatch.delenv("DRYAD_CLIENT_SECRET", raising=False)
    monkeypatch.setattr(sys, "argv", ["stage_files.py", "000003", "crcns-ret-1", "dryad-bvq83bkk9"])
    assert stage_files.main() == 0
    out = capsys.readouterr().out
    assert "DRYAD:bvq83bkk9: no DRYAD_CLIENT_ID" in out and "000003" not in out and "ret-1" not in out


def test_a_figshare_dataset_is_named_by_its_article_id_and_pinned_by_its_version():
    key = datasets.parse("FIGSHARE:24949470")
    found = next(t for t in datasets.targets() if t["key"] == key)
    assert key == "figshare:24949470" and found["folder"] == "figshare-24949470"
    assert datasets.label(key) == "FIGSHARE:24949470" and datasets.parse("figshare-24949470") == key
    assert found["doi"] == f'10.6084/m9.figshare.24949470.v{found["published_version"]}'
    assert f'/articles/24949470/versions/{found["published_version"]}' in datasets.access(key)


def test_figshare_targets_are_small_datasets_with_a_paper_and_checksums():
    from archives import ALL
    found = [t for t in datasets.targets() if t["archive"] == "figshare"]
    assert len(found) == 3 and ALL["figshare"].stage is None and not ALL["figshare"].secrets
    for t in found:
        assert t["item_type"] == "dataset" and t["papers"] and t["size_gb"] < 0.2, t["id"]
        assert all(len(f["md5"] or "") == 32 and isinstance(f["file_id"], int) for f in t["files"]), t["id"]


@pytest.mark.parametrize("text, expected", [
    ("24949470", ("24949470", None, "")),
    ("10.6084/m9.figshare.23974902.v2=10.1038/s41597-024-03206-2", ("23974902", 2, "10.1038/s41597-024-03206-2")),
    ("https://springernature.figshare.com/articles/dataset/Unveiling_Insights/26877211", ("26877211", None, "")),
    ("https://figshare.com/articles/dataset/BAAM/26311921/1/", ("26311921", 1, "")),
])
def test_the_figshare_builder_takes_an_id_a_doi_or_a_page(text, expected):
    import build_figshare_targets
    assert build_figshare_targets.parse(text) == expected
