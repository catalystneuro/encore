"""Figshare (figshare.com and its institutional and publisher portals): docs/archives.md, "Figshare".

A dataset is a Figshare item, named by its article id (FIGSHARE:24949470, folder figshare-24949470); portals
such as springernature.figshare.com share the one API and id space. Each version has its own DOI
(10.6084/m9.figshare.<id>.v<n>); published_version is the version number, which pins it. Metadata and files are
public, so agents read them directly: no stage(), no secrets.
"""

from . import Archive

ARCHIVE = Archive(
    key="figshare", label="FIGSHARE", name="Figshare", url="https://doi.org/10.6084/m9.figshare.{id}",
    access=("Read the files of the pinned version ({published_version}, DOI {doi}) anonymously, as docs/archives.md "
            "says under \"Figshare\": list them with https://api.figshare.com/v2/articles/{id}/versions/"
            "{published_version} (under files, each with an id and computed_md5), and stream each from "
            "https://ndownloader.figshare.com/files/<file id>, which redirects to S3, with fsspec, reading it into "
            "memory (pandas, openpyxl, zipfile; list every sheet of a workbook). Do not download files to disk."),
    list="figshare.json", builder="tools/build_figshare_targets.py",
    hosts=("api.figshare.com", "ndownloader.figshare.com", "*.amazonaws.com"),
)
