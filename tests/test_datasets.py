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


def test_an_openneuro_dataset_is_named_by_its_accession_and_pinned_by_its_snapshot():
    key = datasets.parse("OPENNEURO:ds002778")
    found = next(t for t in datasets.targets() if t["key"] == key)
    assert key == "openneuro:ds002778" and found["folder"] == "openneuro-ds002778"
    assert datasets.label(key) == "OPENNEURO:ds002778" and datasets.parse("openneuro-ds002778") == key
    assert found["doi"] == f'10.18112/openneuro.ds002778.v{found["published_version"]}'
    assert f'snapshot(datasetId: "ds002778", tag: "{found["published_version"]}")' in datasets.access(key)
    assert "{" in datasets.access(key) and "files(recursive: true)" in datasets.access(key)


def test_openneuro_targets_are_bids_datasets_with_a_paper_in_pmc_and_checksums():
    from archives import ALL
    found = [t for t in datasets.targets() if t["archive"] == "openneuro"]
    assert len(found) == 3 and ALL["openneuro"].stage is None and not ALL["openneuro"].secrets
    assert {m for t in found for m in t["modalities"]} >= {"eeg", "ieeg", "mri"}
    for t in found:
        assert t["data_standards"][0] == "BIDS" and len(t["git_commit"]) == 40, t["id"]
        assert any(p["pmcid"] for p in t["papers"]) and not any(p["preprint"] for p in t["papers"]), t["id"]
        assert any(f["path"] == "participants.tsv" for f in t["files"]), t["id"]
        assert all(len(f.get("md5") or f.get("sha256") or f.get("git_sha1") or "") in (32, 40, 64)
                   for f in t["files"]), t["id"]


@pytest.mark.parametrize("text, expected", [
    ("ds002778", ("ds002778", None, "")),
    ("ds004752:1.0.1", ("ds004752", "1.0.1", "")),
    ("10.18112/openneuro.ds000228.v1.1.1=10.1038/s41467-018-03399-2", ("ds000228", "1.1.1", "10.1038/s41467-018-03399-2")),
    ("https://openneuro.org/datasets/ds000117/versions/1.0.5/", ("ds000117", "1.0.5", "")),
    ("https://openneuro.org/datasets/ds000117", ("ds000117", None, "")),
])
def test_the_openneuro_builder_takes_an_accession_a_doi_or_a_page(text, expected):
    import build_openneuro_targets
    assert build_openneuro_targets.parse(text) == expected


@pytest.mark.parametrize("file, expected", [
    ({"id": "MD5E-s4317--9c94ab9a8c2877fe9dd9b1c39a3afead.pos", "annexed": True},
     {"md5": "9c94ab9a8c2877fe9dd9b1c39a3afead"}),
    ({"id": "SHA256E-s10--" + "a" * 64 + ".edf", "annexed": True}, {"sha256": "a" * 64}),
    ({"id": "5a2f8ffa3892e0073152c2362e4e545e5eaa89de", "annexed": False},
     {"git_sha1": "5a2f8ffa3892e0073152c2362e4e545e5eaa89de"}),
])
def test_an_openneuro_file_id_is_its_checksum(file, expected):
    import build_openneuro_targets
    assert build_openneuro_targets.checksum(file) == expected


def test_the_openneuro_builder_finds_papers_and_bids_kinds():
    import build_openneuro_targets as b
    assert b.papers_in(["see https://www.nature.com/articles/s41467-018-03399-2",
                        "doi:10.18112/openneuro.ds000228.v1.1.1", "eLife 11:e78677. https://doi.org/10.7554/eLife.78677."]) \
        == ["10.1038/s41467-018-03399-2", "10.7554/elife.78677"]
    assert b.kind_of("sub-01/ses-01/ieeg/sub-01_ses-01_task-verbalWM_run-01_events.tsv") == "events.tsv"
    assert b.kind_of("dataset_description.json") == "dataset_description.json"
    assert b.kind_of("derivatives/sub-01/beamforming/sub-01-task-verbalWM-LCMVsources.mat") == "derivatives/beamforming/*.mat"
