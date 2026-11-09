I checked all five tested claims against their criteria. Four reproduce and the air-puff direction claim does not. The sixth claim, that rats learned the puff location, is blocked. The paper is not open access, so I worked from the abstract alone, saved as `paper/abstract_pubmed_28892057.txt`. The abstract gives no numbers and no chance level. There is no attempt record in the working directory, so the counts below come from the claims file (6 claims) and the notebook outputs.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| hpc-bla-reactivation-post-sleep | reproduced | Cell 24: 36 significant patterns in all 15 usable sessions. Post minus pre median is 0.0119, 28 of 36 positive, Wilcoxon p = 3.6e-05. The median is above zero in all three rats (Rat08 0.017, Rat10 0.0024, Rat11 0.019), where the criterion needs two. The Rat10 margin is thin (5 of 8 positive, p = 0.74). The session-level test agrees (14 of 15 sessions, p = 1.2e-4, which I recomputed), and so do all variants in cell 25. |
| reactivation-peaks-at-ripples | reproduced | Reading (a), cell 28: the mean post-sleep curve peaks at lag 0. Peak minus flanks has median 0.103, 30 of 36 positive, p = 6e-06. Reading (b), cell 29: ripple minus non-ripple change has median 0.054, 25 of 36 positive, p = 0.0033. Both readings hold. |
| bla-ripple-up-subgroup | reproduced | Cell 31: 103 of 822 BLA units are positively modulated (0.125), against a 7 s-shift chance level of 0.007 (binomial p = 9.8e-90). Each rat is above chance: Rat08 0.103, Rat10 0.048 (p = 0.003), Rat11 0.198. The fraction is below 1. The chance level matches the nominal alpha of 0.01; the paper states none to compare with. |
| reactivation-involves-ripple-up-cells | reproduced | Cell 33: 31 patterns in 13 sessions. Mean squared BLA weight of up units minus other units has median 0.034, 24 of 31 positive, p = 0.0013. The variant on patterns that reactivate gives p = 0.0018. Rat10 goes the other way (3 patterns, median −0.041), but the criterion is pooled only. |
| aversive-direction-stronger | not_reproduced | Cell 35: median puff minus safe is 0.0133, 9 of 15 positive, Wilcoxon p = 0.11. Recomputed from the printed per-session differences, p = 0.107, which is above the 0.1 cut-off for "partial". Variants do not change the outcome (cell 36: first pattern p = 0.048, equal bins p = 0.28, post-sleep alone p = 0.45). |
| rats-learn-puff-location | blocked (other / too_large) | The archive has no position series (asset `variableMeasured` lists only Units, ElectricalSeries and LFP). The files are `ecephys+image` and hold the video frames themselves (cell 9, e.g. 54,431 run frames), so position could be tracked from video, but that needs streaming files of 9 to 254 GB. It is not strictly `data_missing`. A direction-level proxy can be tested from the reward and puff events; see C. |

**B. Problems**

1. [does not affect a conclusion] `hpcbla.laps` / `run_laps`, cell 35. A lap runs from one reward to the next reward at the other end, so it includes all time spent waiting at the ends. In early Rat08 sessions this makes the directional templates very unequal and mostly not running: Rat08-20130709 has 7 laps giving 66,804 puff bins against 5,610 safe bins. The direction contrast is therefore poorly defined. The outcome is negative either way.
2. [does not affect a conclusion] `puff_direction` has no minimum number of puffs. Rat08-20130708 (3 puffs) and Rat08-20130709 (2 puffs) get a puff direction and enter the direction test, while the cell 17 check required at least 5 puffs. Leaving them out gives p = 0.146 (my recomputation), still not reproduced.
3. [does not affect a conclusion] `reactivation(equal_bins=True)` keeps the first bins of the longer direction, not a random or interleaved subset, so bin count is mixed with time in session.
4. [does not affect a conclusion] Cell 33 does not control for firing rate. Whether a unit can reach p ≤ 0.01 in `ripple_modulation` depends on its rate, and rate can also raise SVD weights. "Up units carry more weight" may partly mean "high-rate units carry more weight". No rate-matched comparison is shown.
5. [does not affect a conclusion] Cell 28: the ripple-locked peak is already large in pre-sleep (0.136 at lag 0 against about 0.04 on the flanks). Much of reading (a) is generic co-activation at ripples, not run-specific. Only the post minus pre contrast (p = 0.022) and reading (b) speak to reactivation; both are positive.
6. [does not affect a conclusion] Cells 28, 29 and 33 test patterns as if independent, though several come from one session (36 patterns in 15 sessions, 31 in 13). Only claim 1 also has a session-level test.
7. [does not affect a conclusion] Cell 31 runs the per-rat binomial tests against the pooled chance level (0.007), not each rat's own (Rat10's own is 0). All rats pass either way.
8. [does not affect a conclusion] The notebook's reason for blocking the last claim ("no position tracking") skips the embedded video and the lap-duration proxy.

Checks that passed:
- Epoch times are converted from ms to s, consistent with the exact ratio of 1000 in cell 7.
- Units 0 and 1 with mixed spike trains are excluded.
- Templates come from the run and are tested on sleep; up-units come from sleep and weights from the run, so there is no train/test leakage.
- Synthetic tests: `intersect`, `in_intervals`, `ripple_bins` and `laps` give the expected results. `joint_patterns` flags 5% of null data as significant and recovers a planted pattern, and on template data the mean `strength` equals the singular value. `ripple_modulation` flags about 0.5% of null units and detects a planted up unit.

**C. What I could not check, and the output that would have let me**

- The behaviour claim. Per-session median lap duration and lap count by direction (puff vs safe) in the pre-run, run and post-run epochs. The claims file says the author computed these, but the notebook never prints them.
- Whether the directional templates reflect running. The distribution of lap durations and the fraction of template bins inside the time between rewards spent travelling.
- Whether firing rate explains claim 4. Run-epoch firing rates of up vs other BLA units, and the weight comparison within rate-matched groups.
- The ripple modulation null. The fraction of shifted windows that land outside Non-REM.
- Claims 2 and 4 at session level. Session-level versions of the cell 28, 29 and 33 tests.
- Whether the run epoch is the right one. Rat08-20130708 has two runs and only the first is used; the notebook does not print which epoch boundaries were used.

I could not open the NWB files myself (no h5py here, and I did not download the data), so everything above rests on the notebook's printed outputs.
