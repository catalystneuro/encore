"""Tests for tools/claims_check.py and tools/papers_manifest.py: no network, no paper store."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import claims_check as cc  # noqa: E402
import papers_manifest as pm  # noqa: E402


def test_a_quote_is_found_across_markup_dashes_and_cuts():
    texts = cc.flattenings("<p>Firing rates <italic>increased</italic> by 20% (P&nbsp;=&nbsp;0.002) in all "
                           "mice – none decreased.</p>")
    assert cc.quote_found("Firing rates increased by 20% ... none decreased.", texts)
    assert cc.quote_found("all mice - none decreased", texts)
    assert not cc.quote_found("Firing rates decreased", texts)
    assert not cc.quote_found("none decreased ... Firing rates", texts)   # fragments in order


def test_printed_forms_of_a_p_value():
    assert "2.4 × 10-5" in cc.printed_forms(2.4e-5) and "0.000024" in cc.printed_forms(2.4e-5)
    assert ".002" in cc.printed_forms(0.002) and "10-10" in cc.printed_forms(1e-10)


def test_dois_are_cleaned_as_the_targets_need():
    assert pm.clean_doi("10.1101/2020.03.31.018820v1") == "10.1101/2020.03.31.018820"
    assert pm.clean_doi("10.1117/1.JBO.24.10.106504.full?tab=articlelinkcited") == "10.1117/1.jbo.24.10.106504"
    assert pm.clean_doi("10.7554/eLife.06619.001") == "10.7554/elife.06619"
    assert pm.clean_doi("https://doi.org/10.64898/2025.12.12.694045v1") == "10.64898/2025.12.12.694045"


def test_the_manifest_reads_the_store(tmp_path):
    (tmp_path / "000582").mkdir()
    (tmp_path / "000582" / "10.1126-science.1125572.txt").write_text(
        "DOI: 10.1126/science.1125572\nVersion: version of record\nSource: PDF\n" + "-" * 72 + "\ntext")
    rows = pm.manifest(tmp_path)
    assert rows["000582"][0]["status"] == "stored" and rows["000582"][0]["version"] == "version of record"
    assert all(r["status"] == "missing" for r in rows["000005"])
    assert [r["doi"] for r in rows["000483"]] == ["10.1038/s41467-023-37704-5"]   # triage: the Dryad DOI is not a paper
