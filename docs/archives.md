# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

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

- **Datasets.** A dataset version in the EBRAINS Knowledge Graph. The registry
  names it by its DOI's suffix: `10.25493/Q0FG-1X8` is `EBRAINS:Q0FG-1X8`, in
  folders `ebrains-q0fg-1x8` (EBRAINS DOIs ignore case). The version's
  Knowledge Graph id, a UUID, is `kg_id` in the registry's list,
  `targets/ebrains.json` (written by hand; for now it holds one dataset, to
  test the pipeline beyond DANDI); its record is at
  `https://search.kg.ebrains.eu/instances/<kg_id>`. Only datasets marked "free
  access" can be read without an account.
- **Versions.** Each version has its own DOI and Knowledge Graph id, so either pins it. Record the
  version's name (`v1`) under `dataset: version` and its DOI under
  `dataset: doi`.
- **Reading.** List the files with
  `https://data-proxy.ebrains.eu/api/v1/public/datasets/<kg_id>?limit=500` (JSON,
  under `objects`). Read a file at
  `https://data-proxy.ebrains.eu/api/v1/public/datasets/<kg_id>/<file>`, which
  redirects to the object at CSCS; open it with `fsspec` and read it into memory
  (`scipy.io.loadmat` for MATLAB files, `h5py` for MATLAB 7.3 or HDF5). The
  data proxy answers no HEAD requests, so open files for reading only. Do not
  download whole files to disk. The dataset's data descriptor (a PDF among its
  files) describes them.
- **In an entry.** The entry names the dataset as `ebrains:<doi suffix>/<version>`
  under `related`.

## Dryad

- **Datasets.** A Dryad dataset, named by its DOI's suffix without the
  `dryad.` prefix: `10.5061/dryad.bvq83bkk9` is `DRYAD:bvq83bkk9`, in folders
  `dryad-bvq83bkk9` (Dryad DOIs ignore case). The registry's list,
  `targets/dryad.json`, is built from chosen DOIs by
  `tools/build_dryad_targets.py`, which reads each dataset's metadata, latest
  version and file list from the public API v2; for now it holds three datasets
  outside neuroscience, to test the pipeline on a general-purpose repository.
  The papers are the dataset's related works marked `primary_article` (and
  `preprint`); related works marked `software` are the paper's code, usually on
  Zenodo.
- **Versions.** The DOI always resolves to the latest version, and versions
  have no DOIs of their own. Each version has an id in the API
  (`/api/v2/versions/<id>`), which is `published_version` in the target list
  and pins it; a version's number (`versionNumber`) counts metadata edits as
  well as file changes, so it is not a pin. Record the version id under
  `dataset: version` and the DOI under `dataset: doi`, and give in the notebook
  header the SHA-256 digest of each file read, which the file list gives.
  List the versions with `/api/v2/datasets/<url-encoded doi:...>/versions`.
- **Reading.** Metadata, versions and file lists are public:
  `https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.<id>` and
  `/api/v2/versions/<version id>/files`. Downloading a file is not:
  `/api/v2/files/<file id>/download` answers 401 without a bearer token, and
  the website's download links (`/downloads/file_stream/<file id>`) answer 403
  to scripts. A token comes from an API account, which a person makes from
  their Dryad account (an ORCID login), "My account", "API account"; its client
  id and secret are exchanged for a token, which lasts 10 hours, at
  `POST https://datadryad.org/oauth/token` (`grant_type=client_credentials`).
  The download answers 302 to a presigned URL in Dryad's S3 bucket, which
  answers 400 if the bearer header comes with it.
- **Staged, not streamed.** An agent's commands never see credentials (the
  workflows and `encore check` strip them), so an agent cannot download from
  Dryad. Before an agent starts, `tools/stage_files.py` (the adapter's
  `stage()`) downloads every file of the pinned version to
  `/tmp/dryad/<id>/<version id>/` and checks each against the SHA-256 the file
  list gives; the agent reads them there, in place, into memory
  (`pandas.read_excel` for the Excel workbooks most datasets hold, listing every
  sheet; `zipfile` for zips). The notebooks read the same paths. The
  credentials are the secrets `DRYAD_CLIENT_ID` and `DRYAD_CLIENT_SECRET` in
  the workflows that run agents and entries (`attempt.yml`, `check.yml`), and
  the same environment variables for `encore check`. The dataset's README
  (`README.md`, shown also on its page) describes the files and columns; there
  may be none, and a data dictionary may be a data file of its own
  (`Metadata.csv`).
- **In an entry.** The entry names the dataset as `dryad:<id>/<version id>`
  under `related`, and gives in the notebook header the SHA-256 of each file
  read.

## Local and remote (`encore check`)

Two kinds of dataset exist only inside a run of `encore check`
([encore.md](encore.md)), and never in the registry's record: `local`, a
directory on the machine running it, and `remote`, files at a URL. The run
writes `targets/local.json` into its own copy of the registry, with the path or
URL and a fingerprint of the files, which stands in for a version. How agents
read them is in [protocol.md](protocol.md), "Local and remote datasets".

## Adding an archive

Each archive is an adapter: one module in `tools/archives/`, which defines
`ARCHIVE = Archive(...)` (see `tools/archives/__init__.py`, and
`tools/archives/crcns.py` for the simplest). Nothing else lists the archives:
the site, the Pipeline page, the paper store, the runner and `encore check`
take them from there.

1. Write the module. Give the archive's key (the first part of a dataset's key
   and folder name), its label and name, the address of a dataset's page, the
   target list's file name, the sentence agents get about reading a dataset
   (with a target's fields as `{field}`), the hosts an agent's commands must
   reach, and whether its identifiers ignore case.
2. If agents cannot read its files directly (the archive needs credentials, as
   Dryad does), give the module a `stage(target, root)` that downloads the
   pinned version's files to `root/<archive>/<id>/<version>/` and checks them,
   and list the environment variables it needs in `secrets`. Add those secrets
   to the staging steps of `attempt.yml` and `check.yml`, and to the
   repository's secrets. The access sentence then points agents to the staged
   directory.
3. Write its target list in `targets/`, by hand or with a builder named in the
   module (`builder`). Each target needs an `id`, a `name` and its `papers`
   (DOI, title, whether a preprint), as in `targets/dandisets.json`, and
   whatever field pins a version (`published_version`).
4. Add a section here, as for DANDI: what a dataset and a version are, how to
   pin one, and how to read files without downloading them.
5. Give attempts on it the archive's name in their `dataset` block (`archive`,
   `id`, `version`, and `doi` or `modified`), and give entries a relation
   `<archive>:<id>/<version>`.
