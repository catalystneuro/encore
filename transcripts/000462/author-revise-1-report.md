I've revised the attempt after the round-1 report, and nine outcomes changed. The entry re-ran cleanly with `tools/entry.py all` (0 check errors, notebook passed in 857 s), its outputs match my development run exactly, and `entry.py check` passes on the updated record. Nothing is committed.

**Outcomes now:** 9 reproduced, 8 partially reproduced, 14 not reproduced, 10 blocked.

| Claim | Before | Now | Why |
|---|---|---|---|
| lick-persistence-ur | partially | not reproduced | Adopted the verifier's view: the mean of 6.6 to 8.6 laps fails under every reading. |
| engaged-lap-counts | partially | not reproduced | Tested on the corrected split: 106 engaged and 125 disengaged laps (46%), against 170 and 74. |
| supp6b-decoder-engaged-laps | reproduced | reproduced | Same outcome, now on the corrected split: engaged 0.759, disengaged 0.424. |
| disengaged-laps-uniform | reproduced | reproduced | Same outcome, now on the corrected split: p = 0.094 and KS p = 0.853. |
| fig2a-pv-cluster-transition | reproduced | not reproduced | Only NR6 and NR23 now have more than 12 engaged laps, and the rule holds in neither. |
| fig2c, fig2d | reproduced | partially | Reading S1 needs the control mice, and the criterion requires S1 and S2 to agree. |
| fig3b-out-in-ratio | reproduced | not reproduced | On the corrected split, RE low is 0.086 to 0.092, against 0.16 ± 0.04. |
| fig3d-reward-overrepresentation | partially | not reproduced | Adopted the verifier's view: the per-mouse conditions fail. |
| supp16-dreadd-running-speed | partially | not reproduced | Adopted the verifier's view: 0 of the 6 means are within tolerance. |
| fig4h-dreadd-reliability-outin | partially | not reproduced | Adopted the verifier's view: saline changes out/in under both ways of pairing. |

**What I fixed or added:**
- **Approach ratio (problems 1–2):** it is now taken from the lap start to the track end, leaving out the pause after the reward. Laps with no defined ratio now count as neither engaged nor disengaged. Every analysis that uses engaged laps was rerun. The paper's code version of the ratio comes much closer to the paper's numbers (67% engaged, 4 qualifying mice). It is shown alongside as a variant but does not decide outcomes, as the claims file requires.
- **Synthetic check of the ratio:** for a lap with a true ratio of 1.600, the helper gives 1.601 with the new window and 1.895 when the pause is included.
- **Reward zone (problem 3):** it now starts at the first lick before the reward. This moves it by 0.3 to 3.9 cm and changes no lick stop.
- **Clock check (problem 4):** the teleport follows the reward by 46 to 49 frames (1.53 to 1.63 s at 30 Hz), matching the paper's 1.5 s pause. Lap time does not depend on the volts-to-cm scale. So the longer lap times here are not a clock or scale error.
- **Other additions:**
  - every HDF5 object in every file is listed (no pupil, axon or other data);
  - full subject descriptions are printed (no tdTomato mice);
  - the fig1d scaling of 9 of 12 mice to 8 of 10 is stated;
  - the pooled-percentile saline split now runs;
  - a check of the outlier out/in values in supp13, and a field-width variant.
- **Questions for a reader:** I created `questions/000462.yaml` with two questions. One covers the lick-persistence reading and the paper's 90 RE high laps; the other covers fig4m judging DCZ but not CNO.
- **Record:** I added a `paper_inconsistency` finding, updated the findings for the authors, and wrote the round-1 entry under `verifications`. The verifier agreed with 32 of the 41 outcomes as they stood before this revision.

**Not done:**
- supp14-reward-cells stays blocked. The count of 43 cells decides the claim, and the correlation test needs reading S1, which needs the control mice.
- I did not add example dF/F traces with their transients. The new candidate-field widths (31 to 41 cm) only partly answer the verifier's point that the width rule widens fields.
- I could not check the paper's code for which laps its decoder plots use, because the repository is not here.
