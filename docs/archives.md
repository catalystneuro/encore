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
