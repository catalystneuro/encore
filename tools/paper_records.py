"""Where a paper's records are, and which datasets it is tested on (docs/paper-first.md).

    python tools/paper_records.py key DATASET_OR_PAPER   # the paper key: a key as is, a DOI, or a matched dataset's paper
    python tools/paper_records.py datasets PAPER         # the paper's dataset folders, one a line
    python tools/paper_records.py claims PAPER           # the paper's claims file (claims/<key>.yaml)
    python tools/paper_records.py doi PAPER              # the paper's DOI
    python tools/paper_records.py adopt DATASET          # after its paper match: list the dataset for its paper,
                                                         # giving the paper a key if it has none; prints the key

A paper is named by its key (papers/keys.yaml, tools/paper_keys.py), and lists its datasets in
papers/datasets/<key>.yaml. Its records:

    claims/<key>.yaml                      the paper's claims, for all its datasets
    questions/<key>.yaml                   the author's questions on them
    transcripts/<key>/<role>.md            the runs of its latest attempt; earlier ones in attempt-NN/
    attempts/<key>-NN.yaml                 its attempts, numbered across the paper
    entries/<key>/                         the entry its attempts write

A paper tested per dataset before the cutover (21 of them) also has claims/<key>/<folder>.yaml,
questions/<key>/<folder>.yaml, transcripts/<key>/<folder>/ and entries/<key>-<folder>/, one per dataset.
"""

from __future__ import annotations

import functools
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datasets  # noqa: E402
import paper_keys  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
KEY = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*-\d{4}(?:-[a-z0-9]+)?$")


def root() -> Path:
    return ROOT


@functools.cache
def keys() -> dict[str, str]:
    """DOI (lower case, no doi:) -> key."""
    return paper_keys.read_keys()


def key_of_doi(doi: str) -> str | None:
    return keys().get(paper_keys.doi_of(doi))


@functools.cache
def listed() -> dict[str, dict]:
    """Every paper's papers/datasets/<key>.yaml, by key, each dataset with its key and folder."""
    out = {}
    for path in sorted((ROOT / "papers" / "datasets").glob("*.yaml")):
        body = yaml.load(path.read_text(), Loader=LOADER) or {}
        for d in body.get("datasets") or []:
            d["id"] = str(d["id"])
            d["key"] = datasets.key_of(d["archive"], d["id"])
            d["folder"] = datasets.folder(d["key"])
        out[path.stem] = body
    return out


def is_paper(name: str) -> bool:
    return name in listed() or name in set(keys().values())


def paper_dois() -> dict[str, str]:
    """key -> DOI."""
    return {k: d for d, k in keys().items()}


def doi_of(key: str) -> str:
    body = listed().get(key)
    if body and body.get("paper"):
        return paper_keys.doi_of(body["paper"])
    return paper_dois()[key]


def datasets_of(key: str, available_only: bool = False) -> list[dict]:
    items = (listed().get(key) or {}).get("datasets") or []
    return [d for d in items if d.get("available", True)] if available_only else items


def several(key: str) -> bool:
    return len(datasets_of(key)) > 1


def paper_of_dataset(dataset: str) -> str | None:
    """The paper whose datasets include this one (a key, label or folder), primary first."""
    key = datasets.parse(dataset)
    found = [(d.get("relation") != "primary", k) for k, body in listed().items()
             for d in body.get("datasets") or [] if d["key"] == key]
    return min(found)[1] if found else None


def resolve(name: str) -> str:
    """A paper key from a paper key, a DOI, or a dataset that is listed for a paper."""
    if is_paper(name):
        return name
    if name.lower().startswith(("doi:", "10.")):
        k = key_of_doi(name)
        if k:
            return k
        raise SystemExit(f"error: {name} has no paper key yet (tools/paper_keys.py)")
    k = paper_of_dataset(name)
    if k:
        return k
    # A dataset in the queue that no paper lists yet (a local dataset `encore check` runs on, or one matched since
    # papers/datasets/ was last written): its matched paper, tested on it alone.
    try:
        key = datasets.parse(name)
    except ValueError:
        key = None
    if key and any(t["key"] == key for t in datasets.targets()):
        doi = matched_doi(name)
        # Under the paper's key unless the paper is already listed with other datasets: then under the dataset's
        # folder name, so that this run uses only the dataset it was asked for.
        paper = key_of_doi(doi)
        if paper is None or paper in listed():
            paper = datasets.folder(key)
        archive, id_ = datasets.split_key(key)
        listed().setdefault(paper, {"paper": f"doi:{doi}", "datasets": [
            {"archive": archive, "id": id_, "relation": "primary", "key": key, "folder": datasets.folder(key)}]})
        return paper
    raise SystemExit(f"error: {name} is neither a paper key nor a dataset listed for a paper")


def matched_doi(dataset: str) -> str:
    """The paper behind a dataset's data, as the paper match and papers/triage.yaml leave it (the paper a person
    names in triage first, then the primary papers, then the partial ones), with its DOI cleaned."""
    import paper_match
    key = datasets.parse(dataset)
    folder = datasets.folder(key)
    for t in datasets.targets():
        if t["key"] == key:
            status, papers = paper_match.choose(t, paper_match.triage().get(folder, {}), paper_match.load(folder))
            if not papers:
                raise SystemExit(f"error: no paper matches dataset {datasets.label(key)} ({status}): "
                                 f"see papers/match/{folder}.yaml")
            return papers[0]["doi"]
    raise SystemExit(f"error: dataset {datasets.label(key)} is not in the queue")


def claims_file(key: str) -> Path:
    return ROOT / "claims" / f"{key}.yaml"


def claims_files(key: str) -> list[Path]:
    """The paper's claims: the paper's own file, then any per-dataset ones from before the cutover."""
    own = [claims_file(key)] if claims_file(key).is_file() else []
    return own + sorted((ROOT / "claims" / key).glob("*.yaml"))


def claims_for_attempt(record: dict) -> Path | None:
    """The claims file an attempt was tested on: before the cutover, the per-dataset file of its one dataset;
    otherwise the paper's own."""
    key = key_of_doi(record["paper"])
    if key is None:
        return None
    used = record_datasets(record)
    if len(used) == 1:
        per = ROOT / "claims" / key / f'{datasets.folder(datasets.key_of(used[0]["archive"], str(used[0]["id"])))}.yaml'
        if per.is_file():
            return per
    return claims_file(key) if claims_file(key).is_file() else None


def questions_file(key: str) -> Path:
    return ROOT / "questions" / f"{key}.yaml"


def transcripts_dir(key: str) -> Path:
    return ROOT / "transcripts" / key


def attempt_paths(key: str) -> list[Path]:
    """The paper's attempt records, oldest first."""
    pattern = re.compile(rf"^{re.escape(key)}-(\d\d)\.yaml$")
    return sorted((p for p in (ROOT / "attempts").glob(f"{key}-*.yaml") if pattern.match(p.name)),
                  key=lambda p: p.name)


def record_datasets(record: dict) -> list[dict]:
    """An attempt record's datasets, whatever its schema version (2 has one `dataset:`)."""
    if record.get("datasets"):
        return record["datasets"]
    return [record["dataset"]] if record.get("dataset") else []


def record_dataset_keys(record: dict) -> list[str]:
    return [datasets.key_of(d["archive"], str(d["id"])) for d in record_datasets(record)]


def label(key: str) -> str:
    """How a paper is shown where a name is wanted: its key, then its datasets."""
    ds = datasets_of(key)
    return f"{key} ({', '.join(datasets.label(d['key']) for d in ds)})" if ds else key


def adopt(dataset: str, relation: str = "primary") -> str:
    """List a dataset for the paper its match settled on (papers/datasets/<key>.yaml), giving the paper a key
    first if it has none (papers/keys.yaml). A dataset already listed is left as it is. Returns the key."""
    key = datasets.parse(dataset)
    doi = matched_doi(dataset)
    title = ""
    for t in datasets.targets():
        if t["key"] == key:
            title = next((p.get("title") or "" for p in t.get("papers") or []
                          if paper_keys.doi_of(p.get("doi") or "") == doi), "") or ""
    paper = paper_keys.add_key(doi, title)
    keys.cache_clear()
    path = ROOT / "papers" / "datasets" / f"{paper}.yaml"
    body = yaml.safe_load(path.read_text()) if path.is_file() else None
    body = body or {"schema_version": 1, "paper": f"doi:{doi}", **({"title": title} if title else {}), "datasets": []}
    archive, id_ = datasets.split_key(key)
    if not any(d["archive"] == archive and str(d["id"]) == id_ for d in body["datasets"]):
        body["datasets"].append({"archive": archive, "id": id_, "relation": relation})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# The datasets this paper is tested on (docs/paper-first.md).\n"
                        + yaml.safe_dump(body, sort_keys=False, width=100, allow_unicode=True))
    listed.cache_clear()
    return paper


def main() -> int:
    command, *rest = sys.argv[1:]
    if command == "key":
        print(resolve(rest[0]))
    elif command == "datasets":
        for d in datasets_of(resolve(rest[0]), available_only="--available" in rest):
            print(d["folder"])
    elif command == "adopt":
        print(adopt(rest[0]))
    elif command == "doi":
        print(doi_of(resolve(rest[0])))
    elif command == "claims":
        print(claims_file(resolve(rest[0])).relative_to(ROOT).as_posix())
    else:
        raise SystemExit(f"unknown command {command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
