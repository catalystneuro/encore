from . import Archive

# Files at a URL, for encore check; the run adds the URL's host to the sandbox itself.
ARCHIVE = Archive(
    key="remote", label="remote", name="files at a URL", url="",
    access=("The dataset is the files at {url}. Stream them with fsspec, or the store's own client; do not "
            "download them to disk, and do not look for the dataset in any archive (docs/protocol.md, "
            "\"Local and remote datasets\")."),
    list="local.json",
)
