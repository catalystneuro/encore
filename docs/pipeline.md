# The pipeline

Each dandiset goes through a fixed series of steps. Each step reads files that
earlier steps wrote and writes its own, so a step can run on its own, with its
own model, and with only the access it needs. The runner keeps one state per
dandiset per step, and the dashboard's Pipeline page shows them.

## Steps

| # | Step | Reads the paper | Runs as | Writes |
|---|---|---|---|---|
| 1 | Triage | no | script, and a person | `papers/triage.yaml`: corrections to the papers a target names (dataset DOIs, background reviews, a missing paper) |
| 2 | Paper text | yes | script, and a person for closed papers | the paper store (below); `papers/manifest.yaml` |
| 3 | Claims | yes | agent, `papers` environment | `claims/<dandiset>/<doi>.yaml` |
| 4 | Claims check | yes | a second agent, `papers` environment | `checks` at the end of the claims file |
| 5 | Attempt | yes | agent (author), `papers` environment | the entry, the attempt record |
| 6 | Verification | yes | agents (verifier rounds, revisions), `papers` environment | the record's verifications |
| 7 | Questions | yes | a reader, `papers` environment | answers in `questions/<dandiset>.yaml`, and in the claims |
| 8 | Confirmation | no | CI | executed notebooks, passing checks |
| 9 | Record | no | agent (recorder) | README row, pilot notes; merged |
| 10 | Report | no | script, sent by a person | issues to the dandiset's owners |
| 11 | Upkeep | depends | runner | deprecation; repeat attempts |

Steps 3 and 4 fix every claim and its method from the paper before anyone
analyses the data: the claims agent never sees the dandiset's contents. The
author reads the paper to understand the claims, but cannot change a claim's
statement or method. When the claims file does not say something the attempt
needs, the author does not choose it, even when the paper gives it: it writes
the question, citing the passage, in
`questions/<dandiset>.yaml` and leaves the claim blocked as `methods_underspecified` or runs
the readings the claim names. The question goes to step 7; once it is answered,
the attempt resumes from the claims file.

## Access

The papers are kept in a private repository, `catalystneuro/registry-papers`.
Only jobs that declare the GitHub environment `papers` can read it: the
environment holds a read-only deploy key for it and may be used only by
workflows on `main`. Every agent job declares it, and `tools/get_papers.sh`
copies the dandiset's papers to `paper/` and deletes the key before the agent
starts. Only steps 3, 4 and 7 may change the claims file; `paper/` is never
committed, and every transcript leaves out everything under it. Claims files quote the paper only in short passages.

## The paper store

`catalystneuro/registry-papers` holds, per dandiset:

```
<dandiset>/
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
what is waiting to start. The Pipeline page shows one row per dandiset and one
column per step, each cell done, running, failed, or waiting on a person (a
paper to supply, a question, an issue to send), with counts per column.
