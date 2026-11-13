No outcome changed. The round-2 verifier agreed with all 30 (23 reproduced, 6 partially reproduced, 1 not reproduced), so nothing goes under `proposed`. I re-ran the entry with `python tools/entry.py all entries/strickland-2022`: it reported 0 errors, the notebook passed in 380 s, and every number I cite matches the new outputs.

**What I corrected**
- **fig3d-supranetwork-lesion:** PC2's probability peak is in the second cue second, not the first. It is still in the first half of the cue, so the outcome holds. Fixed in notebook cell 61 and in the notes.
- **fig4b-tonic-network (cell 73):** k6 no longer reads as the only cluster inhibited to surprising shock. It now says k6 has the lowest mean, and k3, k4, k5 and k9 are also below 0.
- **Why the outcome networks fail (cell 73):** now given in full. In the phasic network, k3 is anticorrelated with k1 and k2. In the tonic network, k6 and k9 are correlated with each other and anticorrelated with k7 and k8. The same fix is made in the tonic notes, the finding on the correlation coefficient, and the existing question in `questions/strickland-2022.yaml`.
- **fig5b-outcome-signal-pca:** under the attempt's own clustering, only the first component (47.80%) is out of tolerance. The second (30.92%) is within it. Fixed in cell 88 and in the notes.

**What I added**
- **cue-outcome-membership-independent:** now has `assumed: true` and a deviation. The outcome is judged on the paper's own cluster membership, which gives the counts in the claim. Under the attempt's own clustering, the median p values over 20 seeds (0.048 and 0.011) would make it not reproduced. The notebook conclusion, the summary table and the README table now say this outcome rests on an assumption.
- **fig2d-danger-latency:** the round-1 reason in the record now includes the verifier's R² values on the paper's own latencies (0.508 and 0.394).
- **Round-2 entry in `verifications`:** all 30 claims are listed with `agrees: true`. Reasons follow the report's wording, and each response says what changed.

**What I did not do, and why**
- I did not change any claim or open a new question. The report found no new place where the claims file misreads the paper. The open points it lists (fig4b r against r², fig5e threshold, fig3c/3d loadings) are already in the questions file. fig2f and fig2d are already recorded as findings.
- The `Shuffle` function is not in the data set, so I left that point as recorded.
- Nothing is committed, as instructed.
