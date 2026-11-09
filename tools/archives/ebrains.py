from . import Archive

# A dataset is named by its DOI's suffix (10.25493/Q0FG-1X8 is q0fg-1x8, shown Q0FG-1X8); the data proxy
# needs its Knowledge Graph id, which the target list gives as kg_id.
ARCHIVE = Archive(
    key="ebrains", label="EBRAINS", name="EBRAINS", url="https://doi.org/10.25493/{id}", case="upper",
    access=("Read the files anonymously through the EBRAINS data proxy "
            "(https://data-proxy.ebrains.eu/api/v1/public/datasets/{kg_id}/<file>), as docs/archives.md says "
            "under \"EBRAINS\": stream each file into memory with fsspec; do not download them to disk."),
    list="ebrains.json", hosts=("*.ebrains.eu", "*.cscs.ch"),
)
