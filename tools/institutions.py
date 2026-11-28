"""Write papers/institutions.yaml: the institutions the authors of each paper list, from OpenAlex, for the table
"Institutions in the registry" on the site's page for institutions.

    python tools/institutions.py            # adds the papers not yet in the file; keeps the rest
    python tools/institutions.py --all      # looks every paper up again

The site reads the file (tools/build_site.py, institution_counts); it does not query OpenAlex itself. The file has
two parts:

    institutions   each institution once, by its ROR id: its name, its type as OpenAlex gives it (education,
                   healthcare, facility, nonprofit, government, company, funder, archive, other), its country, and
                   `parents`, the ROR ids of the institutions OpenAlex places above it (its lineage)
    papers         each paper's DOI with the ROR ids of the institutions its authors list

It holds what OpenAlex says and no more. How a paper is counted for an institution is decided where the site is
built. An affiliation OpenAlex has not matched to an institution with a ROR id is left out. A paper OpenAlex does
not know is not written, so the next run looks for it again; one it knows without affiliations is written with an
empty list.

The requests carry the DOIs and a generic client name, and nothing about who runs the tool.
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402
from journals import key  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers" / "institutions.yaml"
API = "https://api.openalex.org"
CLIENT = "metadata-lookup/1.0"
BATCH = 40          # DOIs, or institutions, in one request


def get(path: str, **params: str) -> dict:
    """One page of results from OpenAlex. A filter's values are sent as they are: OpenAlex reads | between them."""
    url = f"{API}/{path}?" + urllib.parse.urlencode(params, safe="|:/")
    req = urllib.request.Request(url, headers={"User-Agent": CLIENT})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):
                raise
            time.sleep(5 * 3 ** attempt)
        except Exception:
            time.sleep(5)
    raise RuntimeError(f"OpenAlex did not answer: {path}")


def batches(items: list[str]) -> list[list[str]]:
    return [items[i:i + BATCH] for i in range(0, len(items), BATCH)]


def works(dois: list[str]) -> dict[str, list[dict]]:
    """The institutions of each DOI's authors as OpenAlex gives them, for the DOIs it knows. A DOI with a comma or
    a bar cannot be named in a filter and is skipped.

    OpenAlex keeps the versions of a paper (a preprint, each version of an eLife paper, the journal's article) as
    one work under one of their DOIs, and answers a request for any of them with that work. In a batch such a work
    cannot be told from its DOI, so a DOI the batch leaves unanswered is asked for again on its own."""
    def institutions(work: dict) -> list[dict]:
        return [i for author in work.get("authorships") or [] for i in author.get("institutions") or []]

    found: dict[str, list[dict]] = {}
    dois = [d for d in dois if "," not in d and "|" not in d]
    for batch in batches(dois):
        page = get("works", filter="doi:" + "|".join(batch), select="doi,authorships", **{"per-page": "100"})
        for work in page["results"]:
            doi = key((work.get("doi") or "").removeprefix("https://doi.org/"))
            if doi in batch:
                found.setdefault(doi, []).extend(institutions(work))
        time.sleep(1)
    alone = [d for d in dois if d not in found]
    for n, doi in enumerate(alone, 1):
        page = get("works", filter="doi:" + doi, select="doi,authorships")
        if page["results"]:
            found[doi] = [i for work in page["results"] for i in institutions(work)]
        time.sleep(1)
        if n % 25 == 0:
            print(f"  {n}/{len(alone)} asked for alone", flush=True)
    return found


def named(ids: list[str]) -> dict[str, dict]:
    """The institutions with these OpenAlex ids: the ones a lineage names that no author listed."""
    found = {}
    for batch in batches(ids):
        page = get("institutions", filter="openalex:" + "|".join(i.rsplit("/", 1)[-1] for i in batch),
                   select="id,display_name,ror,type,country_code,lineage", **{"per-page": "100"})
        found.update({i["id"]: i for i in page["results"]})
        time.sleep(1)
    return found


def main() -> int:
    body = yaml.safe_load(OUT.read_text()) if OUT.exists() else {}
    institutions, papers = body.get("institutions") or {}, body.get("papers") or {}
    if "--all" in sys.argv[1:]:
        institutions, papers = {}, {}
    # The same papers as tools/journals.py: those the site shows, and every paper the targets and the papers'
    # dataset lists name.
    import build_site
    import paper_records
    shown = {t.get("paper") for t in build_site.collect()["targets"]}
    listed = {p.get("doi") for t in datasets.targets() for p in (t.get("papers") or [])}
    listed |= {paper_records.doi_of(k) for k in paper_records.listed()}
    dois = sorted({key(d) for d in shown | listed if d})
    todo = [d for d in dois if d not in papers]
    print(f"{len(dois)} papers, {len(todo)} to look up", flush=True)

    found = works(todo)
    by_id = {i["id"]: i for insts in found.values() for i in insts}
    above = sorted({a for i in by_id.values() for a in i.get("lineage") or []} - set(by_id))
    by_id.update(named(above))
    ror = {id_: i["ror"] for id_, i in by_id.items() if i.get("ror")}
    for id_, i in by_id.items():
        if id_ not in ror:
            continue
        record = {"name": " ".join(i["display_name"].split()), "type": i.get("type") or "other"}
        if i.get("country_code"):
            record["country"] = i["country_code"]
        parents = sorted({ror[a] for a in i.get("lineage") or [] if a != id_ and a in ror})
        if parents:
            record["parents"] = parents
        institutions[ror[id_]] = record
    for doi, insts in found.items():
        papers[doi] = sorted({ror[i["id"]] for i in insts if i["id"] in ror})

    # Only the institutions a paper lists, and the ones above them.
    used = {r for rors in papers.values() for r in rors}
    used |= {p for r in used for p in institutions.get(r, {}).get("parents", [])}
    institutions = {r: v for r, v in sorted(institutions.items()) if r in used}
    OUT.write_text("# Written by tools/institutions.py from OpenAlex (https://openalex.org, CC0): the institutions the authors "
                   "of each paper list,\n# for the table of institutions on the site's page for institutions.\n"
                   + yaml.safe_dump({"schema_version": 1, "institutions": institutions,
                                     "papers": dict(sorted(papers.items()))},
                                    sort_keys=False, allow_unicode=True, width=120))
    with_some = sum(1 for v in papers.values() if v)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(papers)} papers, {with_some} with an institution, "
          f"{len(institutions)} institutions; OpenAlex does not know {len(dois) - len(papers)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
