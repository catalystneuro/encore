I made no changes, because there are no questions to answer for DANDI:001887.

- **The questions file doesn't exist.** There is no `questions/001887.yaml` in the working tree, and git history has no commit that ever touched it.
- **The author didn't ask any.** The author run's report says "**Questions to a reader:** none." (`transcripts/001887/author-report.md:50`).
- **The three "Question for the authors" entries are something else.** They are in `attempts/001887-gabriel-2025-01.yaml` (lines 743 to 756) and cover the ROC routine, how mixed cells are counted for Figure 1K to 1M, and which class is positive in the decoding F1 score. They are open method questions to the paper's authors, recorded in the attempt itself, not questions saying the claims file misreads the paper.

I didn't edit `claims/001887/` or create a questions file, so I didn't run `tools/claims_check.py`.

If a verifier run adds `questions/001887.yaml` later, this answer step needs to run again.
