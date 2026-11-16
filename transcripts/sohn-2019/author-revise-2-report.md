No outcome changed. The verifier agreed with all 23 outcomes, and I found nothing that called for a proposed change. The counts stay at 8 reproduced, 5 partially reproduced, 7 not reproduced and 3 blocked. I re-ran the entry twice with `python tools/entry.py all entries/sohn-2019`. Both runs passed with 0 errors and gave the same numbers as before, and every number in the record matches the new outputs.

**Overstatements corrected:**
- **alt-speed-unmodulated** (notebook cell 66, the record's notes, the Summary row): these no longer say the slopes come from attrition "without any time course". They now say attrition explains most slopes, but Eye Left Short is above the permutation range (7.926 against 7.796, 2% of permutations as large).
- **short-in-long-control** (cell 46 and the notes): these now give the Hand Left difference of -0.0007, which is zero. They say the smaller Short-prior effect holds only in the unnormalised 2-PC space, and that in the normalised spaces the Bayesian model is better in only 2 and 1 of 4 datasets.
- **beh-bayes-model notes:** "the behaviour is nearly unbiased" is replaced by "the model fits a small wm and so predicts little bias".
- **Pooled or per-session Bayesian fits:** the paper says both. The STAR Methods pool sessions; the Table S3 legend fits each session separately. I added a `paper_inconsistency` finding that quotes both passages. The beh-bayes-model and encoding-r2 deviations, cell 22 and the Summary now give both, consistently.
- **GPFA runtime:** the README and `entry.yaml` said twelve minutes. They now say sixteen; the two runs took 978 and 1026 s.

**Outputs added:**
- Cell 3 now prints the units table's columns (only heldout, spike_times and obs_intervals) and the electrodes table (x, y, z and imp are NaN in all 72 rows). The findings on unit labels and electrodes now rest on printed output.
- Cell 4 now computes the `tp` check over all 1025 completed trials, where it had used the 982 valid ones. `tp` is longer than Go - Set in all 1025, by 0.1 to 162.4 ms (more than 60 ms in 14). The finding and the Summary now give these numbers.

**The record:**
- In the round-1 entries, the pca-dimensionality reason now says which problem it means, in place of "(problem 2)". The glm-prior-ts reason now includes round-1 problem 11, about failed fits counting as "not dependent".
- Round 2 is recorded under `verifications`, with the verifier's reasons and my replies. The points that belong to no single claim (the electrodes, unit-label and `tp` findings) are noted in that round's `reviewed` field, because the schema has no round-level response field.

**Not done:**
- **Normalisation:** pca-dimensionality, encoding-bayes-beats-linear and neural-long-more-bias would change outcome with normalised rates. They stay as tested on the claims file's unnormalised rates, and the question stays open with the authors, as the verifier accepted.
- **Questions file:** no question was added to `questions/sohn-2019.yaml`, because this round reported no new place where the claims file misreads the paper.
- **Claims file:** it still says the supplement was unavailable, and an author may not change it.

As instructed, nothing was committed.
