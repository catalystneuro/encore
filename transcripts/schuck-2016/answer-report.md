I can't do this task because there are no questions to answer. `questions/crcns-ofc-4.yaml` does not exist in the working tree, and no other file in the repository holds questions for this dataset.

- **The author asked no reader questions.** The author run (commit adfd5b213c) says in `transcripts/crcns-ofc-4/author-report.md:58`: "Questions to a reader: none."
- **The author's two open questions are for the paper's authors.** Both ask how a method was done (how beta maps were z-scored within runs, and how errors were counted). They are recorded in `attempts/crcns-ofc-4-schuck-2016-01.yaml` (lines 373 and 379) as `methods_unavailable` findings. Neither says the claims file misreads the paper, so neither is a reader question under docs/protocol.md, Reader, step 6.
- **No verifier has run yet** on this attempt, so there are no verifier questions either.

I changed nothing in `claims/crcns-ofc-4/` and did not create a questions file. I didn't run `tools/claims_check.py`, since there were no edits to check. The answer step can run again if a verifier or a later author revision adds questions.
