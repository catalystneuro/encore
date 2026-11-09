# Paper-first records

Status: proposal, 2026-11-09. Nothing here is implemented yet.

Encore has so far been organized by dataset: a target is a dataset, the pipeline finds its paper,
and records are named after the dataset (`000233-tingley-2021`). We now also want to test papers
that reuse a dataset (the find_reuse REUSE pairs), and a dataset can have many of those. So the
paper becomes the unit, and each paper names the datasets it is tested on.

## What the records hold today

- 253 attempts on 208 papers. 19 papers are tested on more than one dataset, as separate attempts:
  mirrors on two archives (Girardeau 2017 on DANDI 000061 and CRCNS hc-14; Fujisawa 2008), and one
  paper's data split across dandisets (Semenov 2026 on 7, Churchland 2010 on 4, Pakhomov 2023 on 4).
- Each such pair has its own claims, chosen for what that dataset holds: Semenov 2026 has 30 to 34
  claims per dandiset, with different ids.
- No dataset is tested against more than one paper yet. Reuse papers will change that.

## Names

- **Paper key**: first author's surname and year, `tingley-2021`, lower case ASCII. Where two
  papers would share one (3 today: guan-2022, daume-2024, moaddab-2021), the later-added one takes
  the first distinctive word of its title: `daume-2024-hippocampal`. Keys are assigned once and
  kept in `papers/keys.yaml` (DOI → key), never recomputed.
- **Scope**: the datasets one set of claims is tested on, named by their folder names
  (`000233`, `crcns-hc-14`), joined with `+` when there is more than one.
- **Attempt id**: `<paper key>-NN`, numbered across the paper, whatever its scope
  (`semenov-2026-01` … `-07`). The attempt names its datasets.

## Layout

| Now | Paper-first |
|---|---|
| `claims/<dataset>/<doi>.yaml` | `claims/<paper key>/<scope>.yaml` |
| `entries/<dataset>-<author>-<year>/` | `entries/<paper key>/` (one scope) or `entries/<paper key>-<scope>/` |
| `attempts/<dataset>-<author>-<year>-NN.yaml` | `attempts/<paper key>-NN.yaml` |
| `papers/match/<dataset>.yaml` | unchanged: it maps a dataset to its own paper |
| paper store, `<dataset>/<id>.pdf` | `<paper key>/…`, one copy per paper |
| site: `/dandisets/<id>/` pages per dataset | `/papers/<key>/` per paper; dataset pages list every paper tested on it |

Attempt records go to schema version 3:

```yaml
schema_version: 3
id: tingley-2021-01
paper: doi:10.1038/s41586-021-03811-w
datasets:
- archive: dandi
  id: "000233"
  version: 0.250624.0414
  relation: primary        # the paper the data were published with; or: reuses
scope: "000233"
entry: tingley-2021
```

## Targets and queue

- Primary targets stay as they are (archive listings → `papers/match/`), and become paper-first
  once matched: (paper, scope = that dataset, relation primary).
- Reuse targets come from `targets/reuse.yaml`, written from find_reuse's REUSE pairs:
  paper DOI, dataset(s), relation `reuses`, and the quote find_reuse found. No paper-match step.
  They are taken only when no primary target is waiting.
- Claims extraction for a reuse paper adds one question: does this claim rest only on this
  dataset? Claims that need the paper's own new recordings, or another dataset, are recorded as
  not testable here rather than attempted.
- Run requests accept a DOI as well as a dataset.

## Converting what exists

A script (`tools/migrate_paper_first.py`) rewrites every attempt, entry, claims file, transcript
and summary path, the runner's state (`resume-*.txt`, `attempt-<folder>` marks) and the paper store,
in one commit, and writes `papers/keys.yaml`. The old site URLs get redirect pages. It is run in a
cutover window with the lanes stopped, because running attempts write to the old paths.

## Open question

For a paper whose data are split across datasets (Semenov 2026 on 7 dandisets), should the claims
be tested **per dataset**, as now (seven scopes, seven sets of claims), or **once across all of
them** (one scope, `001515+001516+…`, one set of claims, one attempt that loads every dataset)?
The conversion keeps the existing per-dataset scopes either way; the question is what new
attempts on such papers should do. Testing across all of them matches how the paper reports its
results, but needs bigger runs.
