I made no changes because there are no questions to answer.

- `questions/sohn-2019.yaml` doesn't exist. Nothing under `questions/` mentions sohn-2019, and git history has no such file on any branch.
- The author's report (`transcripts/sohn-2019/author-report.md:39`) says "Questions to a reader: none." The reports in `transcripts/sohn-2019/attempt-01/` (verifier-1, verifier-2 and the author revisions) don't mention any reader questions either.
- The one open issue in the attempt went to the paper's authors as a `methods_unavailable` finding, not to a reader. It asks whether the tp-on-ts regression had an intercept, whether rates were normalised before PCA, and how many GPFA EM iterations were run. These are method details, which the author settles from the paper (Author, step 1.6), so they aren't the reader's to answer.

I didn't edit `claims/sohn-2019.yaml` and had nothing to run `tools/claims_check.py` on. If a questions file should exist, it was probably not handed to this run and would need to be supplied.
