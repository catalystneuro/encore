I've finished checking the claims file against the paper, and it is ready for an attempt. Nothing is committed.

**Checker:** `claims/000139/10.1016-j.neuron.2010.09.015.yaml: 23 claims, 23 quotes, 9 statistical values, 0 problems` (it was 22 claims before I added one).

**Changes, by claim:**
- **Opening comment, PD model:** the file said the PCA-based spaces stay fixed across the leave-one-out folds. It cited "The matrix S is the same for every neuron", but that sentence is about neurons, not folds. Whether the PCA is redone without the left-out condition is now listed as open, with two readings. `fig6d-perimovement-best-j-array` now needs its result to hold under both.
- **fig4abc-mean-correlation-other-datasets:** added the Spearman means from the statement (0.20, 0.20, 0.06) as expected values with 10% tolerance.
- **fig4-broad-unimodal:** the statement now keeps the paper's exception for monkey B ("except perhaps weakly in panel B").
- **fig4e-correlation-time-course:** the window of 400 ms before to 100 ms after movement onset is not in the paper. The criterion now cites the spliced firing-rate trace from the supplement and lists the time range as open, with two readings. It also marks the 10% decline rule and the 300 to 100 ms window as readings, not the paper's values.
- **fig6-dimensionality-peak:** "middle range", read as a best k of 2 to 10, is now marked as a reading.
- **fig6-maze-task-spaces:**
  - The paper lists the spaces that performed reasonably well without saying for which task. The statement now says this, and cites the Figure 7D legend for segment directions on the maze task.
  - Initial velocity on the maze task is marked as a reading.
  - The "points above zero" sentence was credited to the Figure 6 legend; it is in the Results, and the citation is fixed.
- **fig6-preparatory-dimensionality:** the supplement says "every neuron" and does not say whether rates are normalized. Both are now open, with readings.
- **fig7c-anterior-posterior-performance:** the statement says anterior sites do slightly better, but the criterion never tested it. It now requires it for "reproduced" and gives "partially reproduced" otherwise. The 10% band for "only slightly different" is marked as a reading.
- **New claim, `high-dimensional-task-spaces-underperform`:** the Controls finding that the high-dimensional task spaces, including kitchen-sink, always did worse than the peri-movement space had no claim.

The other claims stand as written. No claim draws on the other paper in `paper/` (nature11129).

**Still open (recorded under `checks`):**
- The paper links no code, so these stay as readings the attempt must run in each form:
  - how tuning strength is measured
  - how movement onset is detected
  - what the reference "proto-trial" is
  - where the kinematic window ends
  - the Figure 4E time range
  - which test was used for the mean correlation
- The paper gives two J-array trial counts, 2166 (Results) and 2155 (Methods). The file accepts either and only reports the count.

**Ready:** yes. The checks entry is recorded with `ready: true`.
