I addressed all ten points in the round-1 report and re-ran the entry. Three outcomes changed. `entry.py all` passes with 0 errors, the notebook runs in 3.4 min, and two runs gave identical numbers. Nothing is committed.

**Outcome changes**
- **supp-errors-by-trial-class**: not reproduced → partially reproduced, the verifier's outcome. The class effect is present (p ≈ 1e-14, Enter highest in 24 of 24 participants), but the rates do not match. It is now marked as resting on two assumptions: one error per block, and the class taken from the trial before the block.
- **fig2-two-back-state-space**: not reproduced → partially reproduced, the verifier's outcome. The two-back space decodes worse than the hypothesised one. Its accuracy is within tolerance only where it is not significantly lower (p = 0.07 to 0.14).
- **fig4b-error-vs-matched**: reproduced → not reproduced, resting on an assumption. The verifier had agreed with "reproduced" but flagged a class confound (point 3), so round 2 should review this change. Every error trial that can be given a state is an Enter trial. On single volumes, correct Enter trials decode at 0.90%, against 11.8% for Exit and 14.3% for Internal trials (maps z-scored by voxel). I added a class-matched comparison and adopted it, since the paper's errors and matched courses covered all classes. Against Enter trials, error trials are not lower: 1.59% against 1.42%, p = 0.57, and p ≥ 0.45 in every reading.

Totals are now 10 reproduced, 6 partially reproduced, 5 not reproduced and 8 blocked.

**Added or corrected**
- **Post-error trials (point 1)**: the notebook wrongly said these sat inside the 'err' regressor. I corrected that and built both of the claims file's readings from the error blocks. 16-way accuracy is 8.10 to 9.38% under them, all above chance and below tolerance. The component, current-age and Enter/non-Enter claims keep their outcomes under both readings.
- **Error block composition (point 2)**:
  - In trial slots by the class of the trial before the block, 82 of 172 blocks after an Exit trial span about two slots; the rest mostly span three to five.
  - A fit over runs gives 1.52 designed trials per block after an Exit trial and 1.87 per other block.
  - Blocks after an Exit trial are 79% of all blocks, against the 48% the paper's class rates imply.

  behavior-error-rate stays blocked.
- **Trial-count control for the Euclidean result (point 4)**: distance falls with a state's number of correct trials (p = 0.013 raw maps, 0.003 voxel z-scored). With that count held constant, distance no longer predicts error rate (p = 0.21 and 0.14). The paper's analysis has the same coupling, so figs5 stays reproduced and the notes say the result may come from trial counts.
- **Slow signal (point 5)**: the data check now states it (accuracy above chance with regressors shifted +6 TRs, t = 2.18) and gives single-volume accuracy by trial class. The error-trial claims take this into account.
- **Two-back fixes (points 6 and 7)**: reading (b) now uses the error trial as the trial two back, and the comparison against the rebuilt hypothesised space is added.
- **Which trial is repeated after an error (point 8)**: the helper docstring now follows the Methods and cites both passages. I asked the conflict as a question for a reader in `questions/crcns-ofc-4.yaml`.
- **RT model (point 9)**: a variant with per-participant category slopes gives χ²(1) = 54.1, p = 1.9e-13, so the faces-faster result holds.
- **Run file contents (point 10)**: the notebook now lists every variable in all 119 run files. None is a mask or coordinates.
- **Stale numbers fixed**: decline-before-errors (smallest voxel p is 0.37; the map slope is p = 0.019, not 0.039) and the map-z-scored 8-way numbers (14.90%, p = 0.018).
- **Record**: round 1 is under `verifications`, with the verifier's reasons in its words and my responses. I also updated the README table and set the notebook's recorded runtime in `entry.yaml` to 4 min.

**Not done**
- The question for point 8 is borderline. The verifier reported an omission in the claims file, not a misreading, but I asked it so a reader can decide.
- `entry.py handover` was not run again, since round 2 gets the full executed notebook.
