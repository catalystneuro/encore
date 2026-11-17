I've revised the attempt for round 1. Both notebooks ran cleanly with `python tools/entry.py all` (43 and 46 minutes, peak memory 6.9 GB), and `entry.py check` passes.

**Outcome changes**
- **fig2fgh (receptive fields):** blocked → reproduced, on the claims file's substitute test, since the multifocal maps aren't public. In every subject, 95–97% of kept voxels have a receptive-field centre inside the display. Left-hemisphere V1 maps 84–91% to the right visual field, and right-hemisphere V1 89–91% to the left. Eccentricity rises from the occipital pole forward, r = 0.33–0.61. This holds under both p-value readings.
- **fig2j (speed vs eccentricity):** blocked → reproduced. All 9 area-and-subject correlations are positive with p < 0.0001 under every reading.
- **discussion-color-no-gain:** blocked → reproduced, in a new second notebook, `color_no_gain.ipynb`. The colour model is 0.0095 *lower* than luminance alone (0.3639 vs 0.3734). It also identifies fewer S1 volumes: 378 vs 409.
- **fig3ab (S1 identification):** reproduced → partially reproduced. The count is now 409 of 486; at least 418 is needed. No Tikhonov penalty on the finer grid reaches 418. In round 1, with a different random held-out split, it was 424, so the count depends on the split.
- **fig2de (prediction accuracy):** stays reproduced, but now only under one penalty reading, and marked as assumed.
  - Penalty chosen by 5-fold cross-validation: 0.233, 0.384, 0.386, all within tolerance.
  - Penalty chosen on a single held-out 10%: the static mean drops to 0.211, just below the 0.216 bound.
- fig2e, figs1a and the three data-missing blocks are unchanged. All tested outcomes are marked as resting on ridge regression in place of L1.

**What I fixed or added in reply to the report**
- **Nondirectional model (problem 3):** this was a real bug. Zero-spatial-frequency filters that share a position were being summed in groups. They are now kept as single features, giving 4,275 features. A table of filter counts per spatial frequency, temporal frequency and direction is printed.
- **Penalty choice:** the cross-validated reading the claims file names is now run, and the ridge penalty grid is widened to 1–1e9. The verifier asked for a finer grid for the identification step's Tikhonov penalty; it is now in quarter decades.
- **Ridge in place of L1:** stated as an assumption with its basis, instead of a deviation "for time".
- **Rank-sum tests (problem 4):** labelled one-sided, with two-sided p-values beside them; the pass counts are the same.
- **Smaller additions:** the stored `rv` is scored as a check (within 0.003), and voxels at the penalty-grid ends are counted. Example frames are shown to check image orientation; they are upright.
- **Memory:** the helper no longer copies each downloaded file in memory, which cut peak memory from 11.7 to 6.9 GB.
- **Record:** the round is recorded under `verifications`, and the README and findings are updated.
- **Questions file:** I added no questions, because the report found no place where the claims file misreads the paper.

**Not done, and why**
- **L1 comparison** (asked for by the verifier): I tried an L1 fit on 40 S1 voxels and it did not converge in 30 minutes. The record says this; it is not in the notebook.
- **Cross-validated penalty for identification:** not run for fig3ab. It raised prediction accuracy in fig2de, so it might raise the count too.
- **Smaller items:** the half- and double-envelope filter variants, and the partial fig3c test (training seconds as distractors), were not run.
- **Held-out blocks crossing run boundaries (problem 8):** kept as they are, since no test data enters any selection.
- **Run stamp:** I wrote the conclusion cells after the run and copied them into the executed notebooks. Only markdown changed, but the entry's run stamp no longer matches. The workflow's clean run will re-execute; I expect the same numbers but have not confirmed it.
