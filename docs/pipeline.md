# The pipeline

Each dataset goes through a fixed series of steps. Each step reads files that
earlier steps wrote and writes its own, so a step can run on its own, with its
own model, and with only the access it needs. A dataset can be in any archive
([archives.md](archives.md)); its files are under its folder name, the
identifier on DANDI and `<archive>-<id>` otherwise. The runner keeps one state per
dataset per step, and the dashboard's Pipeline page shows them.

## Steps

| # | Step | Reads the paper | Runs as | Writes |
|---|---|---|---|---|
| 1 | Triage | no | script, and a person | `papers/triage.yaml`: corrections to the papers a target names (dataset DOIs, background reviews, a missing paper) |
| 2 | Paper text | yes | script, and a person for closed papers | the paper store (below); `papers/manifest.yaml` |
| 3 | Claims | yes | agent, `papers` environment | `claims/<folder>/<doi>.yaml` |
| 4 | Claims check | yes | a second agent, `papers` environment | `checks` at the end of the claims file |
| 5 | Attempt | yes | agent (author), `papers` environment | the entry, the attempt record |
| 6 | Verification | yes | agents (verifier rounds, revisions), `papers` environment | the record's verifications |
| 7 | Questions | yes | a reader, `papers` environment | answers in `questions/<folder>.yaml`, and amendments to the claims |
| 8 | Confirmation | no | CI | executed notebooks, passing checks |
| 9 | Record | no | agent (recorder) | pilot notes; merged |
| 10 | Report | no | script, sent by a person | issues to the dataset's owners |
| 11 | Upkeep | depends | runner | deprecation; repeat attempts |

New targets come from the [Track DANDI](../.github/workflows/targets.yml)
workflow. Every day it rebuilds `targets/dandisets.json` from the archive. When
the list has changed, it opens or updates a pull request that says what
changed: new dandisets that name a paper, papers added to existing targets
(an attempted one needs claims for each new paper), and new published versions
of attempted dandisets, which are candidates for a repeat attempt. Merging the
pull request puts the new targets in the runner's queue.
A person asks for a particular attempt, such as a repeat after a conversion was
fixed, with a run request ([queue.md](queue.md)); requests run before the
targets the runner chooses itself.

Steps 3 and 4 fix every claim and its method from the paper before anyone
analyses the data: the claims agent never sees the dataset's contents. The
author reads the paper to understand the claims, but cannot change a claim's
statement, expected values or criterion. When the claims file does not say a
method detail the attempt needs, the author takes it from the paper and cites
the passage. Where the paper leaves the detail open, the author runs every
reading, adopts the best-supported one as a stated assumption (or blocks the
claim as `methods_underspecified` when no choice is defensible), and records
the question for the paper's authors in the claim's notes and the attempt's
findings. Only when the author or a verifier believes the claims file misreads
the paper is a question written, citing the passage, in
`questions/<folder>.yaml`. It goes to step 7, where a reader decides whether to
amend the claims file; once it is answered, the attempt resumes from the claims
file.

When the claims check says the file is ready, the runner commits the claims
file straight to `main`, with no pull request, once it validates against its
schema (`tools/runner/merge_claims.sh`), ahead of the
attempt: a checkpoint that fixes the claims, and their methods, in the record
before any analysis of the data is merged. The Pipeline page shows them as
done from then on. The attempt goes on in its branch; when it is merged, git
drops the claims change `main` already has. A deprecated attempt is not held
to the claims file that replaces its own.

When a dataset's paper is a preprint that has since been published in a journal,
the publication replaces it: `papers/triage.yaml` lists the preprint under
`not_papers` and the publication under `papers`, and the paper store holds the
publication's text and supplement. An attempt whose claims were read from the
preprint is deprecated, and its claims file is removed. The runner takes a
dataset whose latest attempt is deprecated as it takes one with no attempt, and
reads its claims again before the new attempt.

## Access

The papers are kept in a private repository, `catalystneuro/registry-papers`.
Only jobs that declare the GitHub environment `papers` can read it: the
environment holds a read-only deploy key for it and may be used only by
workflows on `main`. Every agent job declares it, and `tools/get_papers.sh`
copies the dataset's papers to `paper/` and deletes the key before the agent
starts. Only steps 3, 4 and 7 may change the claims file; `paper/` is never
committed, and every transcript leaves out everything under it. Claims files quote the paper only in short passages.

## Accounts

Agent runs use one of two subscription accounts: one verified for sensitive
life-science work (`CLAUDE_CODE_OAUTH_TOKEN`) and one that is not
(`CLAUDE_CODE_OAUTH_TOKEN_UNVERIFIED`). The workflows take an `account` input,
`verified` by default. The runner tries each role on the unverified account
first. On that account, `tools/flagged.py` reads the run's output after the
agent stops: a refusal, a switch away from the model asked for, or an error
naming the usage policy means the run was flagged. A flagged run commits
nothing and fails with `FLAGGED`. The runner then puts the branch back and
runs the role again on the verified account, along with the dataset's
remaining roles. A missing unverified token (`UNVERIFIED-UNAVAILABLE`) is
treated the same way. The recorder reads no paper, so it starts on the unverified account even for a
dataset whose paper was flagged. Each
run's commit records its account.

## The paper store

`catalystneuro/registry-papers` holds, per dataset:

```
<folder>/
  <doi as a file name>.txt      the full text: main text, Methods, supplement; cleaned
  <doi as a file name>.pdf      the PDF it came from, in Git LFS, when there is one
  <doi as a file name>.supp.pdf a supplement PDF, in Git LFS
```

Each text file starts with a header: the DOI, the version (the version of
record, or a preprint version), the source (Europe PMC, PubMed Central,
bioRxiv, the publisher's PDF), the date and the extractor. Open papers are
stored too, so that no run depends on a publisher's rate limits. The claims job
reads the text; it opens a PDF page only to read a figure or a table that the
text garbles.

`papers/manifest.yaml` in this repository, which is public, records for each
target paper whether its full text is in the store, from where, and what is
missing (the paper, a supplement), without any of the text. The dashboard reads
it; it is the list of papers a person needs to supply.

## State

A step's state is read from the repository where it can be: the target, the
manifest, the claims file and its check record, the attempt branch, the record
and its verifications, the merge, a deprecation. The runner's queue holds only
what is waiting to start. The Pipeline page shows one row per dataset and one
column per step, each cell done, running, failed, or waiting on a person (a
paper to supply, a question, an issue to send), with counts per column.
