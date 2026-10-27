"""OpenNeuro (openneuro.org), BIDS datasets of human neuroimaging and electrophysiology: docs/archives.md, "OpenNeuro".

A dataset is named by its accession number (OPENNEURO:ds002778, folder openneuro-ds002778) and pinned by a
snapshot's tag (published_version, 1.0.5), each with its own DOI (10.18112/openneuro.<id>.v<tag>). Metadata and
files are public: OpenNeuro's GraphQL API gives a snapshot's files, each with a URL pinned to that snapshot (an S3
object version in the openneuro.org bucket, or a git object on openneuro.org), so agents read them directly: no
stage(), no secrets.
"""

from . import Archive

ARCHIVE = Archive(
    key="openneuro", label="OPENNEURO", name="OpenNeuro", url="https://openneuro.org/datasets/{id}",
    access=("Read the files of the pinned snapshot ({published_version}, DOI {doi}) anonymously, as docs/archives.md "
            "says under \"OpenNeuro\": list them by POSTing to https://openneuro.org/crn/graphql the query "
            "snapshot(datasetId: \"{id}\", tag: \"{published_version}\") {{ files(recursive: true) {{ filename size "
            "annexed id urls }} }}, and open each file at its urls[0], which is pinned to that snapshot, with pandas "
            "(sep=\"\\t\" for TSV) or fsspec, reading into memory. The dataset is BIDS: start from "
            "dataset_description.json, README, participants.tsv and the *_events.tsv files and JSON sidecars, and "
            "read only the parts of large recordings or images a claim needs. Do not download files to disk, and "
            "do not read the bucket's unversioned keys, which hold the latest snapshot."),
    list="openneuro.json", builder="tools/build_openneuro_targets.py",
    hosts=("openneuro.org", "*.openneuro.org", "*.amazonaws.com"),
)
