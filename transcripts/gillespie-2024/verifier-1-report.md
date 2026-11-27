## A. Outcomes

The claims file has 35 claims. Nine use 000115 alone; the other 26 are marked `data: elsewhere` (DANDI 000629). I did not have the attempt record, so these counts come from the claims file only.

**Claims on 000115**

| Claim | Outcome | Reason |
|---|---|---|
| control-cohort-trial-counts | reproduced | Cell 21: 2557, 2663, 2042, 3081 against 2490, 2629, 2027, 3021. All four are within tolerance (+0.7 to +2.7%). |
| control-decode-counts | partially_reproduced | The dandiset has no gooddecode flag, so the criterion says the epoch counts are not comparable, which rules out "reproduced". Cell 23: the 4E and 4G trial counts are within tolerance for roquefort, despereaux and montague. jaq is over by 15.0% (4E) and 10.9% (4G), with 27 epochs against 24. |
| fig2s1h-control-dwell-increases | partially_reproduced | Cell 25: r is positive in all 4 rats under leave reading (b), but only in 3 under reading (a), where roquefort has r = -0.129, p = 0.48. Neither reading comes from the paper or the code, and this criterion does not say "under one reading". |
| fig3a-control-speed | reproduced | Cell 27: the median and the mean are below 4 cm/s for all four rats at every smoothing (largest 3.02 cm/s at sd 0.1 s). Reading (i), a speed stored in the dandiset, does not exist; the archive's variableMeasured lists only ElectricalSeries and Position. |
| fig5s1-control-search-efficiency-increases | reproduced | Cell 29: r is positive in 4 of 4 rats under both redundant-search readings (0.14 to 0.33; none significant alone, and the criterion asks only for the sign). This uses the criterion's variant epoch set. |
| fig2s1c-control-prereward-swr-counts | blocked (too_large) | Accepted. The per-rat totals need SWR detection over all 116 epochs: about 1.1 TB of single-channel raw data (cell 19). The archive holds only ElectricalSeries and Position, with no LFP or SWR table (I confirmed this on two more files). |
| fig2s1f-control-rate-increase | blocked (too_large) | Debatable; see B9. Each rat's sign of post minus pre could be tested on a subset of epochs. |
| fig2b-control-timecourse | blocked (too_large) | Debatable, as above. |
| fig4g-control-replay-glm (and the control part of fig4s1-replay-glm-pre-post) | blocked (too_large) | Accepted. Clusterless decoding needs every channel: 9.1 TB (cell 19 and the archive's assetsSummary). |

**Data-elsewhere claims the notebook tested anyway, on 000629 with rats 2 to 4 only**

These are outside the record's dataset (see B1). Rat1 (remy) is missing, so no criterion that requires all four rats can be fully met.

| Claim | Outcome | Reason |
|---|---|---|
| fig1s1c-prereward-dwell-matched | not_reproduced (narrowly) | Cell 31, matched plateau: bernard differs by 10.2% against the 10% threshold. last7 passes 3 of 3 and last10 passes 1 of 3. The ranksum pattern matches the paper (rat2 not significant, rats 3 and 4 significant). |
| fig2e-postreward-dwell | partially_reproduced | Cell 33: the ranksums and both mixed models hold in the claimed direction. The NF/control ratio is 0.36 to 0.40 under every reading, outside 0.4 to 0.6. The delay/control ratio of 0.48 to 0.53 is inside. |
| fig3a-speed-below-immobility | partially_reproduced | Cell 35: every condition holds under every reading, but rat1 is untested and the 000629 spatial scale is assumed. |
| fig5a-search-efficiency | not_reproduced | Cell 39: the delay-against-control model gives p = 0.58 to 0.75 under reading (a) and 0.064 to 0.18 under (b); the paper has 0.0069. Rat1, which has the most epochs (37), is missing, so this may be a matter of power. |
| fig5b-redundant-search-balanced | partially_reproduced | Cell 41: no rat has p < 0.05 under last7 or last10. Under the matched plateau gus has p = 0.013 (a) and 0.004 (b). |
| fig5c-repeat-accuracy-unchanged | partially_reproduced | Cell 43: no test reaches p < 0.05 (p_bh ≥ 0.44, mixed models ≥ 0.38); rat1 untested. |
| fig5d-repeat-errors-balanced | partially_reproduced | Cell 45: at most 1 rat has p < 0.05 under every reading, and it is fievel, the same rat as the paper's p = 0.0227. Rat1 untested. |

The remaining 19 data-elsewhere claims (SWR, replay and timecourse claims on the neurofeedback cohort) are untested; on this record's data they are data elsewhere.

## B. Problems

1. **[affects a conclusion] Cells 0 and 11 to 45.** The notebook tests seven claims that the claims file marks `data: elsewhere` (DANDI 000629), arguing that 000629 "is not listed for the paper in the registry". These outcomes are not results on 000115 and should not be counted with them. They are also limited to three rats with an inferred plateau, and no criterion can be fully met without rat1.
2. **[affects a conclusion] `parse_trials`.** The pre-reward period starts at the *first* beam break at the lit port after the home reward. If the rat withdraws and re-pokes, the gap is counted as pre-reward time. The code's RWstart comes from an upstream parser and is unknown, and the alternative (the last entry before the pump) was not run. This could flip fig1s1c, where bernard sits at 10.2%. The speed claims are unaffected because their margins are large.
3. **[affects a conclusion] Cells 25 and 33, the leave readings.** fig2s1h flips between 3 and 4 rats depending on the reading, and neither reading is tied to the paper or the code. Running both was the right call, but the outcome has to reflect the disagreement.
4. **[does not affect a conclusion] `plateau_days`, "matched" reading.** It chooses days by fitting the paper's Figure 2C trial counts, so the selection is tuned to the target. It is stated as a reading and is not used to test any count claim.
5. **[does not affect a conclusion] Cell 14, the 0.2 cm/px scale for 000629.** The notebook says the head positions "then span the same range as in 000115". Its own output says otherwise: 105.8 to 158.7 cm against 107.6 to 119.2 cm. The NF-against-delay tests do not depend on scale, and the below-4 cm/s margins survive a 40% error.
6. **[does not affect a conclusion] `lme_cohort`.** It uses statsmodels REML with Wald z p-values. MATLAB fitlme defaults to ML with t-based p-values. With n in the thousands of trials or about 170 epochs the difference is negligible here.
7. **[does not affect a conclusion] Cell 23.** The jaq "without first 3 epochs" count (2076) is a post-hoc exploration. It is printed for scale and not used in the outcome.
8. **[does not affect a conclusion] `label_task_phase`.** The redundant-search rule is the author's assumption. Reading (a) matches the paper's definition ("visits an arm not yet sampled"). Synthetic tests confirm the labels, the 200 ms withdrawal bridging and the block-closer handling behave as documented.
9. **[affects a conclusion; the blocked reason] Cell 19 and the cells that block these claims.** The notebook's own numbers are about 10 GB per epoch, about 1.1 TB for one channel per tetrode in total, and 1.7 h at 64 streams. That makes a test of fig2s1f-control-rate-increase and fig2b-control-timecourse (a per-rat sign or ratio) on a subset of epochs feasible. The electrode groups carry location "ca1"; the cell-layer subset is missing, but it could be chosen by ripple-band power as a stated assumption. "too_large" fits fig2s1c (totals over all epochs) and the replay claims, not these two.

## C. What I could not check

- **Whether testing data-elsewhere claims on 000629 is allowed.** docs/protocol.md is not in my materials.
- **How often the pre-reward window contains withdrawals.** A count per rat of trials with more than one entry, or a withdrawal over 200 ms, between the home reward and the center pump would size problem 2. So would the fig1s1c and fig3a results with RWstart taken as the last entry before the pump.
- **The 000629 spatial scale.** A per-epoch distribution of the head-position range for 000629 against 000115 would test the 0.2 cm/px assumption.
- **Goal carry-over between epochs.** The goal arm at each epoch's start, compared with the previous epoch's last goal on the same day, would show whether a goal carried across epochs makes the first trials of an epoch "search" trials wrongly. That affects fig5s1 and the 4G counts.
- **Rat1's corrupted port events.** I took this from the pump-onset counts in cell 12. A raw excerpt of remy's pump DIO timestamps would let me confirm it.
