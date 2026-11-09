I answered nothing and changed nothing, because there are no questions for DANDI:001785.

- **No questions file.** `questions/001785.yaml` does not exist. No other file under `questions/` mentions 001785, and git history on any branch has no record of one.
- **The author asked none.** The author run's report (`transcripts/001785/author-report.md`) says "Questions to a reader: none". The only open question it raises is for the paper's authors: which FIJI threshold, size filter and watershed they used to count cells. That is a method detail, so it is not a reader's to settle.
- **Quote check still has problems.** `python tools/claims_check.py` on the claims file against the paper text reports 8 problems out of 35 claims, 32 quotes and 51 values. Among them, values for fig5bc-san-no-net-change, fig6b-sham-dacc-cb-decrease, fig6d-sham-scc-little-change and fig6e-sham-no-network-reduction (for example 6.2e-07 and 1.3e-08) are not found in the text. The checker reports values in a form it does not know, so these may just need confirming by reading the paper. No question covers them, so I left them as they are.

Nothing was committed or pushed.
