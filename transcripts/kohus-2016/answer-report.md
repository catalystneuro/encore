I had no questions to answer, so I changed nothing.

`questions/crcns-hc-7.yaml` does not exist, and git history shows it never has. The attempt agrees with that: the author's report (`transcripts/crcns-hc-7/author-report.md:76`) says "Questions to a reader: none." The attempt record mentions no misreadings of the claims file either.

The attempt does raise three questions, but they are for the paper's authors, not for a reader. They are recorded as `methods_unavailable` findings in `attempts/crcns-hc-7-kohus-2016-01.yaml`:
- how the onset of asynchronous release was found;
- which APs and fit windows gave the CCK+ pairs' single-AP uIPSCs;
- how the recovery half-time was fitted.

`python tools/claims_check.py` passes on the claims file as it stands: 44 claims, 43 quotes, 0 problems.

If a verifier's questions should be here, the revision that adds them to `questions/crcns-hc-7.yaml` has not happened yet. Once it does, this answer run needs to be started again.
