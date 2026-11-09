I had nothing to answer for DANDI:001361, so I changed nothing.

- **No questions file:** `questions/001361.yaml` is not in the working tree, and git has no history of it on any branch.
- **The author asked no reader questions:** their report (`transcripts/001361/author-report.md`) says "I asked a reader no questions."
- **The three questions in the attempt record are for the paper's authors:** they sit in `attempts/001361-sosa-2025-01.yaml` (around lines 1214 to 1239) and are marked `methods_unavailable`. They ask about:
  - the OASIS time constant and shuffle details in the unpublished TwoPUtils package;
  - how cells were registered across days and how the matching threshold was chosen;
  - how the active-trial threshold for place fields is defined.

  None of them says the claims file misreads the paper. They ask for method details the paper does not give, which a reader does not settle (Reader, step 6).

I did not create a questions file, edit `claims/001361/`, run `tools/claims_check.py`, commit or push. If a questions file was meant to be supplied for this run, it is missing and needs adding before this step can be done.
