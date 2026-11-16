"""SPARC (sparc.science), the NIH SPARC program's data portal, on Pennsieve Discover: docs/archives.md, "SPARC".

A dataset is named by its Pennsieve Discover id (SPARC:206, folder sparc-206) and pinned by its version number
(published_version), each version with its own DOI (10.26275/...). Metadata and files are public: every SPARC
dataset is in the AWS Open Data bucket sparc-prod-aod-discover-publish50-use1, and each version's manifest.json
gives every file's S3 object version, which pins it, and SHA-256. Agents read the files directly, with range
requests: no stage(), no secrets.
"""

from . import Archive

ARCHIVE = Archive(
    key="sparc", label="SPARC", name="SPARC", url="https://sparc.science/datasets/{id}",
    access=("Read the files of the pinned version ({published_version}, DOI {doi}) anonymously from the public S3 "
            "bucket {bucket}, as docs/archives.md says under \"SPARC\": the version's manifest, "
            "https://{bucket}.s3.amazonaws.com/{id}/manifest.json?versionId={manifest_version}, lists every file "
            "with its path, size, s3VersionId and sha256, and each file is at "
            "https://{bucket}.s3.amazonaws.com/{id}/<path>?versionId=<s3VersionId>, pinned to this version. Open "
            "files with fsspec (block_size=2**20) and read into memory; read only the parts of large files a claim "
            "needs. The dataset follows the SPARC Data Structure: start from readme.md, files/README.txt if any, "
            "files/dataset_description.xlsx, files/subjects.xlsx and files/samples.xlsx, and the manifest.xlsx in "
            "each folder of files/ (primary, derivative, code, docs, protocol), which describes its files. Do not "
            "download whole files to disk, and do not read keys without a versionId, which hold the latest version."),
    list="sparc.json", builder="tools/build_sparc_targets.py",
    hosts=("api.pennsieve.io", "*.pennsieve.io", "sparc.science", "*.amazonaws.com"),
)
