from . import Archive

ARCHIVE = Archive(
    key="dandi", label="DANDI", name="the DANDI Archive", url="https://dandiarchive.org/dandiset/{id}",
    access=("Use the DANDI API (docs/archives.md, \"DANDI\") and stream the NWB files; do not download "
            "them to disk."),
    list="dandisets.json", builder="tools/build_targets.py",
    hosts=("dandiarchive.org", "*.dandiarchive.org", "*.amazonaws.com"),
)
