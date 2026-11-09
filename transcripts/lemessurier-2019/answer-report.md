I had nothing to answer, so I changed nothing.

`questions/crcns-ssc-10.yaml` doesn't exist. It isn't on this branch, on `origin/main` (only `questions/crcns-ssc-7.yaml` is there for SSC), or in any commit on any branch. The author's report (`transcripts/crcns-ssc-10/author-report.md`, line 71) says "Questions to a reader: none." No verifier rounds have run yet that could have added any.

The attempt record (`attempts/crcns-ssc-10-lemessurier-2019-01.yaml`) does have three questions, but they are addressed to the paper's authors, not to a reader. They ask how equivalent best whiskers were tested, which responsiveness test was used, and whether the spontaneous activity in Figure 4C had a baseline subtracted. Each says the Methods and the code don't settle a method detail, not that the claims file misreads the paper. Under step 6 those aren't a reader's to settle.

I didn't edit `claims/crcns-ssc-10/` or create a questions file, so there was nothing new to check with `tools/claims_check.py`. If questions were meant to be filed for this run, the questions file is missing and needs to be supplied before an `answer` run can do anything.
