I couldn't check anything: there is no claims file for DANDI:000230. `claims/000230/` doesn't exist, and git history has no file under that path.

**Checker result:** not run, because there was no file to give it.

**Why there is no file:** the previous reader run (commit 00e6bf3a6, report in `transcripts/000230/claims-report.md`) stopped on purpose and wrote no claims. Its reason was that the supplement the dataset's findings rest on is not under `paper/`. I checked that against the paper text and it holds:
- `paper/10.1016-j.crmeth.2022.100221.txt` (the version of record, PMC9142754.1) only lists "Document S1. Figures S1–S4 and Tables S1 and S2" and "Document S2. Article plus supplemental information". The supplement's contents are not there.
- The bioRxiv preprint text doesn't include them either, and there is no PDF.
- The paper says it reports no original code, so there is no code that could stand in.

**Changes, by claim:** none. I did not create a claims file or a `checks` entry. Writing claims is the reader's job (steps 1 to 3), not the checker's, and the protocol says to stop when a supplement the results rest on is missing.

**Still open:** Document S1 or S2 needs to be added to `paper/`. Both are linked from https://doi.org/10.1016/j.crmeth.2022.100221 and from PMC9142754. After that, the `claims` reader role can be run again, followed by a new check.

**Ready:** no. There are no claims to attempt.
