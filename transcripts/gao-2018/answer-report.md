I made no changes, because there are no questions to answer.

- `questions/gao-2018.yaml` doesn't exist, and no branch in the git history has ever had it (or `questions/000007.yaml`).
- The author's report (`transcripts/gao-2018/author-report.md`, section 2) says "**Questions to a reader:** none." Its open points are all method questions for the paper's authors, filed as `methods_unavailable` findings. Settling those is not the reader's job.
- The attempt record (`attempts/gao-2018-01.yaml`) contains no reader questions either.

So no claim was checked against the paper, `claims/gao-2018.yaml` is unchanged, and I didn't run `tools/claims_check.py` because there was nothing to check. Nothing was committed or pushed. If a verifier is expected to have filed questions, that hand-over hasn't happened yet, and this step should run again once `questions/gao-2018.yaml` exists.
