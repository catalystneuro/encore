There are no questions to answer, so I changed nothing.

- **No questions file:** `questions/crcns-hc-14.yaml` does not exist on this branch, and git history on all branches shows it never has.
- **The author asked none:** the author's report (`transcripts/crcns-hc-14/author-report.md:1`) says "I asked no reader questions." No verifier has run yet.
- **Two questions are aimed at the paper's authors, not a reader.** The attempt records them as `methods_unavailable` findings (`attempts/crcns-hc-14-girardeau-2017-01.yaml:520-527`):
  - which StatesFR column is REM;
  - where the air puff location in BehavioralMeasures.m comes from.

  Both are method details and neither says the claims file misreads the paper. Under step 6 they are the author's to settle, so even as reader questions they would change nothing.

I left `claims/crcns-hc-14/` alone and did not create a questions file. I did not run `tools/claims_check.py`, since no claim was edited. Nothing was committed or pushed.
