from . import Archive

ARCHIVE = Archive(
    key="crcns", label="CRCNS", name="CRCNS.org", url="https://crcns.org/data-sets",
    access=("Read the files anonymously from the public S3 bucket crcnsarchive "
            "(https://crcnsarchive.s3-us-west-2.amazonaws.com/{id}/), as docs/archives.md says under "
            "\"CRCNS\": stream them, opening a zip in place with fsspec and zipfile; do not download them "
            "to disk."),
    list="crcns.json", hosts=("crcns.org", "*.amazonaws.com"),
)
