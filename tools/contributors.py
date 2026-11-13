"""Write targets/contributors.yaml: the people each dataset names as its contributors, with their ORCID iDs and
roles, for the dataset pages and the author pages' datasets (tools/build_site.py).

    python tools/contributors.py            # adds the datasets not yet in the file; keeps the rest
    python tools/contributors.py --refresh  # looks every dataset up again

The datasets are every target (tools/datasets.py) and the datasets only a reuse paper names
(targets/reuse_datasets.json). A dandiset's contributors come from its metadata on the DANDI Archive (the draft
version, which is the latest), people only; a dataset of another archive's from its DOI's record at DataCite (its
creators, then its contributors). A person the record gives no ORCID iD for is listed by name and has no author
page. The site reads the file; it does not query the archives.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "targets" / "contributors.yaml"
ORCID = re.compile(r"(\d{4}-\d{4}-\d{4}-\d{3}[\dX])$")
UA = {"User-Agent": "encore-registry (https://encorescience.org)"}


def get(url: str) -> dict | None:
    """The JSON at a URL; None when the archive does not know it or does not answer."""
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as err:
            if err.code in (400, 404):
                return None
            time.sleep(5 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    return None


def given_first(name: str) -> str:
    """A name as a page prints it: "Buzsáki, György" is "György Buzsáki"."""
    name = " ".join((name or "").split())
    family, comma, given = name.partition(",")
    return f"{given.strip()} {family.strip()}" if comma and given.strip() else name


def role(text: str) -> str:
    """A role in words: "dcite:ContactPerson" and "ContactPerson" are "Contact person"."""
    words = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", (text or "").split(":")[-1]).strip()
    return words[:1].upper() + words[1:].lower()


def once(people: list[dict]) -> list[dict]:
    """Each person once, by ORCID iD or else by name, with all their roles."""
    out: dict = {}
    for p in people:
        mine = out.setdefault(p["orcid"] or p["name"].lower(), {"name": p["name"], "orcid": p["orcid"], "roles": []})
        mine["roles"] += [r for r in p["roles"] if r not in mine["roles"]]
    return list(out.values())


def of_dandiset(ident: str) -> list[dict] | None:
    meta = get(f"https://api.dandiarchive.org/api/dandisets/{ident}/versions/draft/")
    if meta is None:
        return None
    people = []
    for c in meta.get("contributor") or []:
        if c.get("schemaKey") != "Person" or not c.get("name"):
            continue
        orcid = ORCID.search(c.get("identifier") or "")
        people.append({"name": given_first(c["name"]), "orcid": orcid.group(1) if orcid else None,
                       "roles": [role(r) for r in c.get("roleName") or []]})
    return once(people)


def of_doi(doi: str) -> list[dict] | None:
    record = get("https://api.datacite.org/dois/" + urllib.parse.quote(doi, safe="/"))
    if record is None:
        return None
    attributes = record["data"]["attributes"]
    people = []
    for kind, listed in (("Creator", attributes.get("creators") or []), (None, attributes.get("contributors") or [])):
        for c in listed:
            if c.get("nameType") == "Organizational" or not c.get("name"):
                continue
            ids = [ORCID.search(i.get("nameIdentifier") or "") for i in c.get("nameIdentifiers") or []
                   if (i.get("nameIdentifierScheme") or "").upper() == "ORCID"]
            orcid = next((m.group(1) for m in ids if m), None)
            name = (" ".join(x for x in (c.get("givenName"), c.get("familyName")) if x) or given_first(c["name"]))
            people.append({"name": name, "orcid": orcid, "roles": [role(kind or c.get("contributorType") or "Contributor")]})
    return once(people)


def listed() -> dict[str, dict]:
    """Every dataset the registry names, by key: the targets, and those only a reuse paper names."""
    out = {t["key"]: t for t in datasets.targets()}
    extra = ROOT / "targets" / "reuse_datasets.json"
    if extra.is_file():
        for t in json.loads(extra.read_text()).get("targets", []):
            out.setdefault(datasets.key_of("dandi", str(t["dandiset"])), t)
    return out


def main() -> int:
    refresh = "--refresh" in sys.argv[1:]
    known = (yaml.safe_load(OUT.read_text()) or {}).get("datasets", {}) if OUT.exists() and not refresh else {}
    todo = {k: t for k, t in listed().items() if k not in known}
    print(f"{len(known) + len(todo)} datasets, {len(todo)} to look up", flush=True)
    for i, (key, t) in enumerate(sorted(todo.items()), 1):
        archive, ident = datasets.split_key(key)
        found = of_dandiset(ident) if archive == "dandi" else of_doi(t["doi"]) if t.get("doi") else None
        if found is not None:
            known[key] = found
        time.sleep(0.2)
        if i % 50 == 0:
            print(f"  {i}/{len(todo)}", flush=True)
    OUT.write_text("# Written by tools/contributors.py from the DANDI Archive and DataCite: the people each dataset names as\n"
                   "# its contributors, with their ORCID iDs and roles.\n"
                   + yaml.safe_dump({"schema_version": 1, "datasets": dict(sorted(known.items()))}, sort_keys=False,
                                    allow_unicode=True, width=120))
    people = [p for v in known.values() for p in v]
    print(f"wrote {OUT.relative_to(ROOT)}: {len(known)} datasets, {len(people)} contributors, "
          f"{sum(1 for p in people if p['orcid'])} with an ORCID iD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
