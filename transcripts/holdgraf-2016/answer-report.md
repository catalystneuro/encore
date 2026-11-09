There are no questions to answer for CRCNS:ac-4, so I changed nothing in `claims/crcns-ac-4/` and did not create `questions/crcns-ac-4.yaml`.

- **No questions file:** `questions/crcns-ac-4.yaml` doesn't exist. It never appears in the history of any branch, and the other `questions/crcns-*.yaml` files belong to other datasets.
- **The author asked none:** the author report (`transcripts/crcns-ac-4/author-report.md`) says "Questions for a reader: none."
- **The attempt's four questions are for the paper's authors:** `attempts/crcns-ac-4-holdgraf-2016-01.yaml` (lines 458 to 474) records them as `methods_unavailable` findings. They ask how high-frequency power was z-scored to pick the speech-responsive electrodes, how the ridge parameter and the receptive-field fit bound were computed, what bandwidth the coherence used, and what scale the Figure 9c RMS is on. These are missing method details, which under step 6 are the author's to take from the paper, not mine to settle. None of them says the claims file misreads the paper.

I didn't run `tools/claims_check.py`, since no claim changed.
