from . import Archive

# The two kinds of dataset `encore check` runs on (encore_science/, docs/encore.md), which never enter the
# registry's record: a directory on the machine running it, and files at a URL. Their list is written for
# the run alone, into the run's own copy of the registry.
ARCHIVE = Archive(
    key="local", label="local", name="a directory on this machine", url="",
    access=("The dataset is the directory {path} on this machine. Read its files in place: do not copy, "
            "move or change them, and do not look for the dataset in any archive (docs/protocol.md, "
            "\"Local and remote datasets\")."),
    list="local.json",
)
