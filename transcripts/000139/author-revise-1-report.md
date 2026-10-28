I've worked through all 12 points in the verifier's report and re-run the entry. `python tools/entry.py all` passes: 0 check errors, the notebook runs in 623 s, and a second run gave the same numbers. Nothing is committed.

## Outcome changes
- **fig6-maze-task-spaces**: blocked (methods_underspecified) → **reproduced**, resting on segments equal in time. The verifier was right that the claims file names both segment divisions, and the criterion holds under one of them. Segment directions score 0.008, initial velocity 0.030 and endpoints + maximum speed −0.045. Chance for those three is −0.429, −0.172 and −0.222. The record says the result is fragile: segment directions are above zero in only 2 of 8 trial-selection readings.
- **prep-activity-more-anterior**: not_reproduced → **blocked (metadata_insufficient)**, as the verifier gave it. The notebook now prints the electrode location column, the electrode groups and the units columns. None of them says whether unit-id prefix 1 or 2 is the PMd array.
- **fig6-dimensionality-peak**: kept as reproduced, resting on S computed once from all conditions (the reading I took from the Methods). The verifier would give partially reproduced, and the record says so. The new chance curves support its point: with conditions shuffled, the curve falls 2.292 from k = 6 to 14 with S fixed but only 0.094 with S recomputed in each fold.

## Added or corrected
- **5 spikes/s threshold (problem 1)**: with condition labels shuffled, 59 of 152 units still pass, against 75 observed. Only 43 of the 76 neurons used for the preferred-direction analyses have tuning distinguishable from noise. On those 43 the Figure 6 result is stronger: peri-movement best 0.336, against 0.116 kinematic and 0.143 task.
- **Chance levels (problem 5)**: every space is below zero by chance and above its chance level at every dimensionality, which supports the paper's "above zero is better than chance".
- **Figure 7C (problem 2)**: now run with the paper's upper limit, which includes the fitted neuron (Supplemental Experimental Procedures: "every neuron"). It stays **not reproduced**: array 1 scores 0.761, array 2 −0.402 and random halves 0.455. Neither half is within 10% of random, so the outcome doesn't depend on which array is PMd.
- **Supplemental Figure 1 (problem 6)**: added a version that ranks conditions on half the trials and measures on the other half. For the claim's 17 neurons the onset difference (0.045) is then no longer smaller than the preparatory one (0.040). I kept the outcome as **reproduced**, because the criterion follows the paper's legend and the verifier agreed with it. The notes say plainly that the result doesn't survive cross-validation.
- **Preparatory dimensionality**: a noise-corrected count (cross-validated PCA) gives 7 PCs, inside 6.3 to 11. The outcome stays **not reproduced**, since the criterion uses the plain count (12). The notes say the failure is likely due to the few trials per condition.
- **Recording identity (problem 7)**: the notebook prints the file's session description and shows the trial timeline was rebuilt. I added a reader question to `questions/000139.yaml`: does the criterion's partial clause fit a 27-condition session, when the paper says the J-array recording interleaved all 108 conditions?
- **Smaller fixes**: the median reaction-time splice in fig4e is now labelled an assumption (problem 8), and the some-neurons-better-elsewhere notes now say most of its fraction is expected from noise.
- The README, the summary, the header, the runtime (10 min) and the `verifications` round-1 record are updated.

## Not done
- **Unsmoothed kinematic velocity (problem 11)**: not changed. The kinematic best (≤ 0.024) is far below the peri-movement best. I said why in the record but did not run the smoothed version.
- **SD tuning measure (problem 9)**: it leaves no neurons, but it is a reading the claims file names, so it stays shown rather than dropped.
- I did not rerun the Figure 4 correlations on the 43 noise-robust neurons.
- One unused check: outside the notebook, I looked up the benchmark's 108-condition dandiset 000128. It is a 2009-09-25 session with 182 units. The record mentions this but no outcome relies on it.
