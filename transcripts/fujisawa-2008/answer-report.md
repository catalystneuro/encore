There are no questions for me to answer, so I changed nothing.

- **No questions file:** `questions/fujisawa-2008.yaml` does not exist on this branch (`attempt/fujisawa-2008`), and no other questions file for this paper is here either.
- **The author asked none:** the latest author run says "**Questions to a reader:** none." (`transcripts/fujisawa-2008/author-report.md:75`). The author sent their open method points (rate normalisation, surrogate counts, the Figure 7 definitions, the layer 5 rat and units) to the paper's authors as `methods_unavailable` findings. Under the protocol those are not reader questions.
- **Files untouched:** I did not edit `claims/fujisawa-2008.yaml` and did not create a questions file. With no edit to check, I did not run `tools/claims_check.py`.

One thing you might trip over: `main` still has an older file, `questions/fujisawa-2008/crcns-pfc-2.yaml`. It holds two unanswered questions (`odor-unrelated-to-stem`, `speed-not-correlated`) about the old per-dataset claims file for CRCNS. That file is not on this branch and is not the file this task names, so I left it alone. If those two questions should be carried over to the merged claims file, that needs a new questions file and a new reader run.
