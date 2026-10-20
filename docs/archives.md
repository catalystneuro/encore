# Archives

The registry tests papers against data in public archives. So far it reads one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. `tools/datasets.py` holds the table of
archives and turns one form of a dataset's name into another. The workflows
take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
  paper cites, or the latest published one. For a draft, record its
  modification time under `dataset: modified` in the attempt.
- **Reading.** List the assets and read metadata with the DANDI REST API
  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
  to disk.
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS

- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
  `targets/crcns.json`, written by hand; for now it holds one data set, to test
  the pipeline beyond DANDI.
- **Versions.** CRCNS data sets are not versioned. Record the version as
  `unversioned`, with the data set's DOI under `dataset: doi`, and give in the
  notebook header the MD5 sums from the data set's `checksums.md5` for the
  files read, so a later change is detectable.
- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
  us-west-2), under `<id>/`, readable without an account at
  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
  set with `?list-type=2&prefix=<id>/` on the bucket's address. The site
  crcns.org asks for a login to download; the bucket does not. Most data sets
  are zip files of MATLAB or other files: open the zip in place with
  `fsspec.open(url, block_size=2**20).open()` and Python's `zipfile`, which
  read only the parts needed over range requests (`remfile` lacks what
  `zipfile` needs to read a member), and load members in memory
  (`scipy.io.loadmat`, or `h5py` for MATLAB 7.3 files). Do not download whole
  files to disk. The data set's `docs/` folder describes the files.
- **In an entry.** The entry names the data set as `crcns:<id>/unversioned`
  under `related`.

## EBRAINS

- **Datasets.** A dataset version in the EBRAINS Knowledge Graph, identified by
  its id (a UUID, `0162668e-bef0-4754-8562-40440db5bc0c`), with a DOI of its own
  (`10.25493/...`). Its record is at `https://search.kg.ebrains.eu/instances/<id>`.
  The registry's list is `targets/ebrains.json`, written by hand; for now it
  holds one dataset, to test the pipeline beyond DANDI. Only datasets marked
  "free access" can be read without an account.
- **Versions.** Each version has its own id, so the id pins it. Record the
  version's name (`v1`) under `dataset: version` and its DOI under
  `dataset: doi`.
- **Reading.** List the files with
  `https://data-proxy.ebrains.eu/api/v1/public/datasets/<id>?limit=500` (JSON,
  under `objects`). Read a file at
  `https://data-proxy.ebrains.eu/api/v1/public/datasets/<id>/<file>`, which
  redirects to the object at CSCS; open it with `fsspec` and read it into memory
  (`scipy.io.loadmat` for MATLAB files, `h5py` for MATLAB 7.3 or HDF5). The
  data proxy answers no HEAD requests, so open files for reading only. Do not
  download whole files to disk. The dataset's data descriptor (a PDF among its
  files) describes them.
- **In an entry.** The entry names the dataset as `ebrains:<id>/<version>`
  under `related`.

## Adding an archive

1. Add the archive to `ARCHIVES` in `tools/datasets.py`: its label, its name,
   the address of a dataset's page, the target list's file name, and the
   sentence agents get about reading it.
2. Write a builder for its target list in `targets/`. Each target needs an
   `id`, a `name` and its `papers` (DOI, title, whether a preprint), as in
   `targets/dandisets.json`.
3. Add a section here, as for DANDI: what a dataset and a version are, how to
   pin one, and how to read files without downloading them.
4. Give attempts on it the archive's name in their `dataset` block (`archive`,
   `id`, `version`, and `doi` or `modified`), and give entries a relation
   `<archive>:<id>/<version>`.

The site, the Pipeline page, the paper store and the runner then handle the
archive's datasets without further changes.
