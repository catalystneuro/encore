I revised the attempt for verifier round 1: two outcomes changed, and the other 20 stay as the verifier agreed. The last run of `python tools/entry.py all entries/churchland-2012` passed: the checks gave 0 errors and the notebook ran in 16 minutes. Every conclusion matches the new numbers.

**Outcomes that changed**
- **fig6-complex-kinematic-model: partially reproduced → not reproduced.** The verifier was right that the peak test let any negative angle pass, so J-array's peak at −0.972π counted as a peak near zero. The test now requires the peak to be within π/4 of zero (the stricter version, between 0 and π/4, is shown too). The main reading peaks at −0.972π (J-array) and 0.806π (N-array) and fails under all five seeds. It is no longer seed-sensitive.
- **fig6-velocity-model: not reproduced → partially reproduced.** The verifier pointed out that the switch from preparatory to movement tuning fell inside the analysed window. In the main reading the preparatory term now ends when the simulated movement activity starts, 100 ms before the hand moves; I chose this from how the model is built, before running it. N-array then passes (peak 0.083π) and J-array fails (peak 0.472π), under all five seeds. The old timing is kept as a reading and still gives not reproduced. The outcome still rests on the model assumptions, and every reading now runs under five seeds.

**What I added or corrected**
- **Onset columns:** the notebook prints both columns' descriptions from the files. `move_begins_time` is described only as "movement onset time". The hand is already moving at 137 and 160 mm/s at that time, against 43 and 15 mm/s at `offline_move_onset_time`, which supports the offline column as the main reading.
- **Curvature claim:** under the `move_begins_time` readings the hand paths are now aligned on that column too; the outcome is unchanged. The J-array conditions that don't rotate counter-clockwise are listed with their curvature: four of the five curve strongly clockwise.
- **Phase claim:** I added the two outputs the verifier asked for, as variants that don't decide the outcome:
  - With the shuffled data projected onto the original plane, the data beat the shuffles in both datasets.
  - Predicted from the state at the dividing point, the data beat the shuffles but stay far below the 0.5 bar (0.103 and 0.252).
- **Lag between the arrays:** after target onset the two N-array arrays respond within 9 ms of each other. So a fixed clock offset of 25 ms or more is not supported, and the later M1 change around movement looks like a real response. The clock finding is updated.
- **Smaller fixes:** I removed a dead sign check in `jpca`, which changes no number. I updated the notebook text, the entry README, the runtime in `entry.yaml`, and two findings (onset columns, and the authors' question about the models).
- **Record:** round 1 is recorded under `verifications`, with the verifier's reasons in its words and my response for each claim. It agreed with 21 of 22 outcomes; the exception was the complex model.

**What I did not do**
- **Claims file:** I left it unchanged. The verifier's three points about how it reads the paper are now questions for a reader in the new file `questions/churchland-2012.yaml`:
  - the shuffle-3 reference for the phase claim;
  - whether R2(M_skew) is the right measure for shuffles 2 and 3;
  - whether the "typically 20–35%" range applies to the whole population.
- **Critical findings:** none of the record's findings are rated critical, so there was nothing to review.
- **Commit:** nothing is committed or pushed; the workflow does that.
