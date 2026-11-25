"""Tests for tools/build_osf_targets.py: OSF projects named, listed and pinned from OSF's API v2.

The builder is tested against a small stand-in for the API, with responses in the shapes OSF's API v2 gives
(JSON:API: data, links.next for the next page, relationships.<name>.links.related.href for related listings), so
that the tests run without the network.
"""

from __future__ import annotations

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import build_osf_targets as b  # noqa: E402

API = "https://api.osf.io/v2"


def rel(href: str) -> dict:
    return {"links": {"related": {"href": href, "meta": {}}}}


def listing(items: list[dict], next_url: str | None = None) -> dict:
    return {"data": items, "links": {"first": None, "last": None, "prev": None, "next": next_url,
                                     "meta": {"total": len(items), "per_page": b.PAGE_SIZE}}}


def node(guid: str, title: str, kind: str = "nodes", root: str | None = None, **attributes) -> dict:
    base = f"{API}/{kind}/{guid}/"
    return {"id": guid, "type": kind,
            "attributes": {"title": title, "description": "  Spikes   and\nbehaviour. ", "category": "project",
                           "date_created": "2021-03-01T10:00:00.000000", "date_modified": "2024-05-06T07:08:09.000000",
                           "public": True, "tags": ["neurons"], **attributes},
            "relationships": {"files": rel(f"{base}files/"), "children": rel(f"{base}children/"),
                              "contributors": rel(f"{base}contributors/"), "identifiers": rel(f"{base}identifiers/"),
                              "license": rel(f"{API}/licenses/563c1cf88c5e4a3877f9e96a/"),
                              "root": rel(f"{API}/{kind}/{root or guid}/")},
            "links": {"self": base, "html": f"https://osf.io/{guid}/"}}


def storage(guid: str, provider: str) -> dict:
    return {"id": f"{guid}:{provider}", "type": "files",
            "attributes": {"node": guid, "path": "/", "kind": "folder", "name": provider, "provider": provider},
            "relationships": {"files": rel(f"{API}/nodes/{guid}/files/{provider}/")}}


def folder(guid: str, osf_id: str, name: str, provider: str = "osfstorage") -> dict:
    return {"id": osf_id, "type": "files",
            "attributes": {"kind": "folder", "name": name, "materialized_path": f"/{name}/", "path": f"/{osf_id}/",
                           "provider": provider, "size": None, "current_version": 1,
                           "extra": {"hashes": {"md5": None, "sha256": None}}},
            "relationships": {"files": rel(f"{API}/nodes/{guid}/files/{provider}/{osf_id}/")}}


def file(guid: str, osf_id: str, path: str, size: int, version: int = 1, provider: str = "osfstorage") -> dict:
    return {"id": osf_id, "type": "files",
            "attributes": {"kind": "file", "name": path.rsplit("/", 1)[-1], "materialized_path": path,
                           "path": f"/{osf_id}", "provider": provider, "size": size, "current_version": version,
                           "date_modified": "2024-05-01T00:00:00.000000",
                           "extra": {"hashes": {"md5": f"md5-{osf_id}", "sha256": f"sha-{osf_id}"}}},
            "links": {"download": f"https://files.osf.io/v1/resources/{guid}/providers/{provider}/{osf_id}",
                      "info": f"{API}/files/{osf_id}/"}}


@pytest.fixture
def osf(monkeypatch):
    """A stand-in for OSF's API: a project, abcde, with a folder, two pages of files, a GitHub add-on, a component
    xyz23 with a file of its own, a minted DOI, two contributors (one not registered, one not bibliographic), and a
    preprint published as a journal article."""
    responses = {
        f"{API}/guids/abcde/": {"data": node("abcde", "Place cells in CA1 ")},
        f"{API}/nodes/abcde/files/?page[size]=100": listing([storage("abcde", "osfstorage"), storage("abcde", "github")]),
        f"{API}/nodes/abcde/files/osfstorage/?page[size]=100": listing(
            [file("abcde", "f1", "/README.txt", 1200), folder("abcde", "d1", "sessions")],
            next_url=f"{API}/nodes/abcde/files/osfstorage/?page=2&page[size]=100"),
        f"{API}/nodes/abcde/files/osfstorage/?page=2&page[size]=100": listing(
            [file("abcde", "f2", "/units.csv", 3_000_000, version=3)]),
        f"{API}/nodes/abcde/files/osfstorage/d1/?page[size]=100": listing(
            [file("abcde", "f3", "/sessions/s01.mat", 500_000_000)]),
        f"{API}/nodes/abcde/files/github/?page[size]=100": listing([file("abcde", "g1", "/analysis.py", 900, provider="github")]),
        f"{API}/nodes/abcde/children/?page[size]=100": listing([node("xyz23", "Behaviour", root="abcde")]),
        f"{API}/nodes/xyz23/children/?page[size]=100": listing([]),
        f"{API}/nodes/xyz23/files/?page[size]=100": listing([storage("xyz23", "osfstorage")]),
        f"{API}/nodes/xyz23/files/osfstorage/?page[size]=100": listing([file("xyz23", "f4", "/licks.csv", 4000)]),
        f"{API}/nodes/xyz23/identifiers/?page[size]=100": listing([]),
        f"{API}/nodes/xyz23/contributors/?embed=users&page[size]=100": listing([]),
        f"{API}/nodes/abcde/identifiers/?page[size]=100": listing(
            [{"id": "i1", "type": "identifiers", "attributes": {"category": "ark", "value": "c7605/osf.io/abcde"}},
             {"id": "i2", "type": "identifiers", "attributes": {"category": "doi", "value": "10.17605/OSF.IO/ABCDE"}}]),
        f"{API}/nodes/abcde/contributors/?embed=users&page[size]=100": listing([
            {"id": "abcde-u1", "type": "contributors", "attributes": {"bibliographic": True, "index": 0},
             "embeds": {"users": {"data": {"id": "u1", "attributes": {"full_name": "Ada Lovelace"}}}}},
            {"id": "abcde-u2", "type": "contributors", "attributes": {"bibliographic": False, "index": 1},
             "embeds": {"users": {"data": {"id": "u2", "attributes": {"full_name": "A Lab Manager"}}}}},
            {"id": "abcde-u3", "type": "contributors",
             "attributes": {"bibliographic": True, "index": 2, "unregistered_contributor": "Grace Hopper"},
             "embeds": {"users": {"errors": [{"detail": "not found"}]}}}]),
        f"{API}/licenses/563c1cf88c5e4a3877f9e96a/": {"data": {"id": "563c1cf88c5e4a3877f9e96a", "type": "licenses",
                                                              "attributes": {"name": "CC-By Attribution 4.0 International",
                                                                             "url": "https://creativecommons.org/licenses/by/4.0/legalcode"}}},
        f"{API}/nodes/abcde/preprints/?page[size]=100": listing([
            {"id": "pre12", "type": "preprints", "attributes": {"title": "Place cells", "doi": "10.1016/J.NEURON.2024.01.001"},
             "links": {"html": "https://osf.io/preprints/psyarxiv/pre12/",
                       "preprint_doi": "https://doi.org/10.31234/osf.io/pre12"}}]),
    }
    asked = []

    def get(url):
        asked.append(url)
        if url.startswith("https://api.crossref.org/"):
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))
        if url not in responses:
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))
        return json.loads(json.dumps(responses[url]))

    monkeypatch.setattr(b, "get", get)
    return asked


@pytest.mark.parametrize("text, expected", [
    ("abcde", ("abcde", "")),
    ("OSF:ABCDE", ("abcde", "")),
    ("10.17605/OSF.IO/ABCDE", ("abcde", "")),
    ("https://doi.org/10.17605/OSF.IO/ABCDE=10.1016/j.neuron.2024.01.001", ("abcde", "10.1016/j.neuron.2024.01.001")),
    ("https://osf.io/abcde/", ("abcde", "")),
    ("https://osf.io/abcde/files/osfstorage", ("abcde", "")),
    ("osf.io/abcde=https://doi.org/10.1038/S41586-020-0001-0", ("abcde", "10.1038/s41586-020-0001-0")),
    # A preprint, by its versioned GUID or its page on a preprint server.
    ("uwge3_v3", ("uwge3", "")),
    ("https://osf.io/preprints/psyarxiv/uwge3_v3", ("uwge3", "")),
    ("https://osf.io/preprints/psyarxiv/uwge3/", ("uwge3", "")),
])
def test_the_osf_builder_takes_a_guid_a_doi_or_a_page(text, expected):
    assert b.parse(text) == expected


@pytest.mark.parametrize("text", ["abcd", "https://osf.io/preprints/psyarxiv", "10.5061/dryad.bvq83bkk9"])
def test_the_osf_builder_refuses_anything_else(text):
    with pytest.raises(SystemExit):
        b.parse(text)


def test_a_listing_is_read_page_by_page_at_the_largest_page_size(osf):
    found = list(b.pages(f"{API}/nodes/abcde/files/osfstorage/"))
    assert [f["id"] for f in found] == ["f1", "d1", "f2"]
    assert osf == [f"{API}/nodes/abcde/files/osfstorage/?page[size]=100",
                   f"{API}/nodes/abcde/files/osfstorage/?page=2&page[size]=100"]
    assert b.paged(f"{API}/nodes/abcde/contributors/?embed=users") == \
        f"{API}/nodes/abcde/contributors/?embed=users&page[size]=100"


def test_a_project_is_listed_with_every_file_in_every_folder_provider_and_component(osf):
    t = b.target("https://osf.io/abcde/")
    assert t["id"] == "abcde" and t["name"] == "Place cells in CA1" and t["kind"] == "project"
    assert t["url"] == "https://osf.io/abcde/" and t["doi"] == "10.17605/osf.io/abcde" and t["api_type"] == "nodes"
    # Depth first: a folder's files come where the folder is listed, before the next page.
    assert [f["path"] for f in t["files"]] == ["README.txt", "sessions/s01.mat", "units.csv", "github/analysis.py",
                                               "xyz23/licks.csv"]
    units = t["files"][2]
    assert units == {"path": "units.csv", "provider": "osfstorage", "size": 3_000_000, "file_id": "f2", "version": 3,
                     "md5": "md5-f2", "sha256": "sha-f2", "modified": "2024-05-01T00:00:00.000000",
                     "download": "https://files.osf.io/v1/resources/abcde/providers/osfstorage/f2"}
    assert t["components"] == [{"id": "xyz23", "title": "Behaviour", "category": "project"}]
    assert t["providers"] == ["github", "osfstorage"] and t["code"] == ["github"]
    assert t["asset_count"] == 5 and t["size_gb"] == 0.503 and t["readme"]
    assert t["data_standards"] == ["CSV", "MATLAB", "Python", "text"]


def test_a_project_is_pinned_by_when_it_was_last_modified_and_each_file_by_its_version(osf):
    t = b.target("abcde")
    assert t["published_version"] == "2024-05-06T07:08:09.000000" and t["published"] == "2021-03-01"
    stored = [f for f in t["files"] if f["provider"] == "osfstorage"]
    assert all(f["version"] for f in stored) and all(f["sha256"] for f in stored)


def test_a_file_in_a_storage_add_on_has_no_version(osf):
    # OSF gives a GitHub file current_version 1, but its download address answers ?version=1 with 404.
    t = b.target("abcde")
    github = next(f for f in t["files"] if f["provider"] == "github")
    assert github["path"] == "github/analysis.py" and github["version"] is None


def test_crossref_is_asked_for_json_and_osf_for_json_api(monkeypatch):
    # Crossref answers a request that accepts only application/vnd.api+json with 406 Not Acceptable.
    asked = {}

    class Response(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    def urlopen(req, timeout=None):
        asked[req.full_url] = req.get_header("Accept")
        return Response(b'{"message": {"title": ["Place cells"], "type": "journal-article"}}')

    monkeypatch.setattr(b.urllib.request, "urlopen", urlopen)
    assert b.title_of("10.1016/j.neuron.2024.01.001") == ("Place cells", False)
    b.get(f"{API}/nodes/abcde/")
    assert asked == {"https://api.crossref.org/works/10.1016/j.neuron.2024.01.001": "application/json",
                     f"{API}/nodes/abcde/": "application/vnd.api+json"}


def test_the_project_metadata_names_the_license_and_the_cited_contributors(osf):
    t = b.target("abcde")
    assert t["license"] == {"name": "CC-By Attribution 4.0 International",
                            "url": "https://creativecommons.org/licenses/by/4.0/legalcode"}
    assert t["contributors"] == ["Ada Lovelace", "Grace Hopper"]
    assert t["description"] == "Spikes and behaviour." and t["keywords"] == ["neurons"]


def test_the_papers_are_the_one_given_and_the_preprints_that_name_the_project(osf):
    t = b.target("abcde=10.1000/given")
    assert [(p["doi"], p["relation"], p["preprint"]) for p in t["papers"]] == [
        ("10.1000/given", "given", False),
        ("10.31234/osf.io/pre12", "preprint", True),
        ("10.1016/j.neuron.2024.01.001", "preprint_published", False)]


def test_a_component_knows_it_is_one(osf, monkeypatch):
    real = b.get

    def get(url):
        if url == f"{API}/guids/xyz23/":
            return {"data": node("xyz23", "Behaviour", root="abcde")}
        return real(url)

    monkeypatch.setattr(b, "get", get)
    t = b.target("xyz23")
    assert t["kind"] == "component" and [f["path"] for f in t["files"]] == ["licks.csv"] and t["doi"] is None


def test_a_registration_is_pinned_by_when_it_was_registered_and_names_its_article(monkeypatch):
    reg = node("reg45", "Frozen copy", kind="registrations", date_registered="2023-02-03T04:05:06.000000",
               article_doi="10.7554/eLife.12345", withdrawn=False)
    responses = {
        f"{API}/guids/reg45/": {"data": reg},
        f"{API}/registrations/reg45/files/?page[size]=100": listing([storage("reg45", "osfstorage")]),
        f"{API}/nodes/reg45/files/osfstorage/?page[size]=100": listing([file("reg45", "r1", "/data.csv", 10)]),
        f"{API}/registrations/reg45/children/?page[size]=100": listing([]),
        f"{API}/registrations/reg45/identifiers/?page[size]=100": listing(
            [{"id": "i1", "type": "identifiers", "attributes": {"category": "doi", "value": "10.17605/OSF.IO/REG45"}}]),
        f"{API}/registrations/reg45/contributors/?embed=users&page[size]=100": listing([]),
        f"{API}/licenses/563c1cf88c5e4a3877f9e96a/": {"data": {"attributes": {"name": "CC0 1.0", "url": None}}},
    }

    def get(url):
        if url not in responses:
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))
        return responses[url]

    monkeypatch.setattr(b, "get", get)
    t = b.target("10.17605/OSF.IO/REG45")
    assert t["kind"] == "registration" and t["api_type"] == "registrations" and not t["withdrawn"]
    assert t["published_version"] == "2023-02-03T04:05:06.000000" and t["doi"] == "10.17605/osf.io/reg45"
    assert [(p["doi"], p["relation"]) for p in t["papers"]] == [("10.7554/elife.12345", "article_doi")]


def test_a_preprint_guid_gives_the_project_it_links_and_the_preprint_as_a_paper(osf, monkeypatch):
    real = b.get
    preprint = {"id": "pre12", "type": "preprints",
                "attributes": {"title": "Place cells", "doi": None},
                "relationships": {"node": rel(f"{API}/nodes/abcde/")},
                "links": {"preprint_doi": "https://doi.org/10.31234/osf.io/pre12"}}

    def get(url):
        if url == f"{API}/guids/pre12/":
            return {"data": preprint}
        if url == f"{API}/nodes/abcde/":
            return {"data": node("abcde", "Place cells in CA1")}
        return real(url)

    monkeypatch.setattr(b, "get", get)
    t = b.target("pre12")
    assert t["id"] == "abcde" and [(p["doi"], p["preprint"]) for p in t["papers"]] == [("10.31234/osf.io/pre12", True)]


def test_a_guid_the_guids_endpoint_does_not_answer_is_looked_up_as_a_node_then_a_registration(monkeypatch):
    asked = []

    def get(url):
        asked.append(url)
        if url == f"{API}/registrations/qqqqq/":
            return {"data": {"id": "qqqqq", "type": "registrations"}}
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))

    monkeypatch.setattr(b, "get", get)
    assert b.resolve("qqqqq")["type"] == "registrations"
    assert asked == [f"{API}/guids/qqqqq/", f"{API}/nodes/qqqqq/", f"{API}/registrations/qqqqq/"]


def test_a_file_outside_osf_storage_is_named_with_its_provider_and_kinds_are_named():
    item = file("abcde", "g1", "/src/run.py", 10, provider="googledrive")
    assert b.file_record(item)["path"] == "googledrive/src/run.py"
    assert b.file_record(item, prefix="xyz23/")["path"] == "xyz23/googledrive/src/run.py"
    assert b.kind_of("sessions/s01.NWB") == "NWB" and b.kind_of("v1.2/Makefile") == "no extension"


def test_a_storage_add_on_that_answers_403_is_left_out_with_a_warning(osf, monkeypatch, capsys):
    # OSF:r7aes links a GitHub add-on whose files answer 403 to an anonymous reader.
    real = b.get

    def get(url):
        if url == f"{API}/nodes/abcde/files/github/?page[size]=100":
            raise urllib.error.HTTPError(url, 403, "Forbidden", {}, io.BytesIO(b""))
        return real(url)

    monkeypatch.setattr(b, "get", get)
    t = b.target("abcde")
    assert "github" not in t["providers"] and not any(f["provider"] == "github" for f in t["files"])
    assert "README.txt" in [f["path"] for f in t["files"]] and "github cannot be read" in capsys.readouterr().err
