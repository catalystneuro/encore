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
- **Attempt id**: `<paper key>-NN`, numbered across the paper (`semenov-2026-01`). The attempt
  names its datasets.

## One attempt, every dataset the paper relies on

- A paper's claims are extracted once, for the paper. Most papers rely on one dataset, and then
  claims name none: they rest on it. Only when the paper lists more than one does each claim
  carry `datasets:`, naming the ones it rests on. An attempt tests the paper against as many of those datasets as can be found and
  loaded: Semenov 2026's next attempt loads all 7 dandisets.
- The paper's datasets are listed in `papers/datasets/<paper key>.yaml`: each with archive, id,
  relation (primary or reuses) and how it was found (archive metadata, the paper's data
  availability statement, find_reuse). A dataset the paper relies on that is in no open archive,
  or cannot be loaded, is listed with `available: false` and why.
- **Missing datasets do not stop an attempt.** It runs on what is there; its record lists the
  rest under `missing_datasets`, and each claim that needs one is blocked with
  `blocked_by: dataset_missing`. The attempt is flagged on the site and in "waiting on you", so
  the dataset can be found, converted or uploaded and a later attempt can add it.

## Layout

| Now | Paper-first |
|---|---|
| `claims/<dataset>/<doi>.yaml` | `claims/<paper key>.yaml` |
| `entries/<dataset>-<author>-<year>/` | `entries/<paper key>/` |
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
missing_datasets: []       # datasets the paper relies on that this attempt could not use, each with why
entry: tingley-2021
```

## Targets and queue

- Primary targets stay as they are (archive listings → `papers/match/`), and become paper-first
  once matched. A primary target whose paper is already listed (a second dandiset of Semenov 2026,
  a CRCNS mirror) adds its dataset to that paper rather than starting a new one.
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

## The 19 papers already tested per dataset

Their existing attempts and claims are kept as they are, converted to the new names
(`semenov-2026-01` … `-07`, each with one dataset), and their claims files to
`claims/<paper key>/<dataset>.yaml`, marked as per-dataset. Their next attempt extracts the
paper's claims once and tests them across all its datasets. Mirrors on two archives (Girardeau
2017, Fujisawa 2008) are compared, not combined: an attempt uses one copy of each dataset, and
the site compares attempts on the two copies.

## Cutover steps

With the lanes stopped (STOP_LANES, and wait for the running chains to end or stop them):

1. On this branch: merge main, then `python tools/paper_keys.py` (keys for papers added since),
   `python tools/runner/cutover_paper_first.py keys --apply` (keys for papers only open branches have records
   of) and `python tools/migrate_paper_first.py`; run the tests; commit; merge the pull request.
2. `python tools/runner/cutover_paper_first.py branches --apply`: the open attempt branches, converted the
   same way and renamed attempt/<paper>. Any it reports as not merging are fixed by hand.
3. `... executed --apply` (the executed notebooks under the new entry names), `... issues --apply` (the
   `needs-you` issues retitled by paper), `... state ~/registry-runner --apply` (queue files and marks).
4. On the runner: a new release of tools/runner into releases/<sha>/bin and pools.yaml pointed at it;
   `mv pool_lane.sh.paper-first pool_lane.sh` (the circuit breaker reads a chain's last line by paper).
5. Start the lanes, and watch the first chains through the paper match and the claims.
