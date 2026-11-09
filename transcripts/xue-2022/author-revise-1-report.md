The round-1 response is finished. No outcome changed: 6 claims reproduced, 6 partially reproduced and 1 not reproduced, as before. I re-ran `python tools/entry.py all entries/000223-xue-2022`; the check reports 0 errors and the notebook passes in 19.3 min. Every number the old conclusions used came out the same, and the new text matches the new outputs.

**Outcomes**
- **Verifier agreed on 12 of 13 claims.**
- **fig5d-out-in-vs-fscore:** the verifier would call it reproduced. I kept partially reproduced, resting on the noise-region assumption, and recorded the disagreement. The criterion's "under one reading" refers to its two readings, the 20 rows and the 19 recordings. With the main classification and region 0, both fall outside the tolerance (R = 0.592 and 0.598). Noise region and classification are details the protocol settles by the best-supported choice, so the result in region 1 or with the code's classification does not decide the outcome.

**Added or corrected, by problem in the report**
1. **Misidentified surrogates (the share the paper calls "rare"):** the notebook now reports, for each recording and region, the share of surrogates whose best unit is not their own, with the median GT-R and test-R. The share is 6% to 44%. It tracks max F (Spearman 0.90) and the gap between the Methods and code classifications. It is in the notes and in a new finding that asks the paper's authors what the share was.
2. **Burst reading chosen to match Table 1:** the notes and notebook now say best-R varies widely across the eight readings, and that every later claim depends on the chosen one.
3. **Empty unit in rows 16 and 18:** I re-ran their F-score grids without it. Max F changes by at most 0.002.
4. **Burst merging:** the helper now counts the bursts the code's single merging pass drops (7 of 19 recordings, 18 bursts in row 20). It also has a variant that merges every chain, as the Methods say. With that variant, or with the code's lowess smoothing, OUT/IN still matches 6 of 19 recordings. Best-R with full merging matches 17 of 20 spines (18 before), because row 20 moves from 0.293 to 0.340. This is recorded as a `code_mismatch` finding.
5. **Spike contrast was also used to assign rows to files:** the notes for table1-network-measures now say the spike-contrast match is not independent for rows 14, 15, 16 and 20.
6. **Rows 9 and 10:** the notebook prints each spine's best and second-best unit. Both spines use units 115 and 44, and with row 9's noise estimate row 10's thresholds equal row 9's. That fits Table 1 using one noise estimate per recording. For rows 3 and 16 it prints the GT-R and test-R quantiles; both mismatches look the same in every noise region.
7. **OUT/IN readings:** the notes say the 10-of-19 "any reading" match does not count under the criterion.
- **Other output the verifier asked for:** the notebook prints the elephant version (1.2.1; the paper used 0.10.0). A figure shows the background squares on each spine's mean image. In most windows they sit in dark areas; in rows 10 and 17 they sit in the dimmest gaps between processes.
- **Attempt record:** the `verifications` round 1 block is written, with the verifier's reason and my response for each claim.

**Not done**
- No question was added to `questions/000223.yaml`, because the verifier found no place where the claims file misreads the paper.
- I could not tell from the paper whether its misidentified share was as large as here. It is asked as a question for the paper's authors in the findings.

Nothing was committed or pushed. `tools/runner/chain.sh` was already modified at the start and I did not touch it.
