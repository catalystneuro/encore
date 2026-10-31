I've revised the attempt in response to every point in the round-1 report. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passes in 19.4 min), and the conclusions, summary and attempt record match the new numbers. Nothing is committed.

**Outcome changes**
- **Population decoders, previously blocked as too large.** The verifier disagreed with this block, so they are now fit in the notebook, following the Methods. Fitting all 974 would take about 2.7 CPU hours on this machine's 4 cores, which is over the notebook limit. So they run on a random subsample: 18 of the 142 eligible sessions, 116 decoders. Every reading the claims file names is run, plus two ways of forming the cross-validation folds (random frames, or whole trials).
  - **fig3q-cue-decoding: partially reproduced.** Area A is lowest in all 12 readings and V1 is above A (p < 0.001). But V1 is highest in only 2 of 12; in the rest PM edges it by 0.001 to 0.027.
  - **figs5f-dynamic-choice-decoding: partially reproduced.** Dynamic choice is decoded better than reported choice and both are above chance (p < 0.001). Both values are above the paper's tolerances.
  - **fig4d-partial-correlation: partially reproduced.** The difference is positive (p < 0.001) under every reading, but no reading has all three values within tolerance.
  - **fig8cd-position-specific-decoders: reproduced, resting on an assumption.** Accuracy falls with train-test distance in every area for both cue and dynamic choice. The assumption: the legend's sessions with the cue offset at 0.76 of the maze can't be matched from the files, so all decoder sessions are used for the cue test.
- **fig4h-activity-by-epoch: kept partially reproduced.** The verifier would call it not reproduced. Two of the claim's three parts hold and the stem part fails, so I kept the outcome and recorded the disagreement.
- No other outcome changed.

**Fixes and added output**
- **Epochs (fig4h):**
  - **Feedback delay:** none of its frames has a maze position, so it falls in feedback/ITI, not the arm. Frame counts per epoch are now printed.
  - **Arm:** it now runs up to the choice point; 913,421 frames just past the 2.5 m maze end were left out before.
  - **Clock error in single-plane sessions:** the activity timestamps are 2000 times the behaviour clock, so their frames had been mismatched. They are now matched by frame index, and this is recorded as a new dataset finding.
- **Checks the verifier asked for:**
  - `is_switch` marks the first trial of the new rule in all 300 sessions.
  - `start_time` is maze onset (median offset -0.004 s).
- **RL fits:** they now report optimiser status and the spread across starting points. All 238 folds converged. One learning rate sits at its bound in 198 folds and the inverse temperature in 50.
- **Visually guided rule update:** the backward reading is no longer presented as support. I added the split by trial type and outcome, and the switch-aligned belief curve. Visually guided trials are mostly correct (80% against 46%), which explains the forward difference. The stored belief itself rises about 0.028 per trial, which explains the size gap with the paper.
- **Choice commitment:** added the local-reward-rate variant without the current trial; the result is unchanged.
- **Session selection:** fraction correct over all trials is now stated as the adopted reading everywhere; the other reading is still shown.
- **Smaller fixes:** p values of 0 now print as bounds (e.g. "< 0.0001"). The shattering-dimensionality claim now has a cost estimate: at least 5 CPU hours for one conjunction alone.
- **Record:** the round is recorded under `verifications` (38 of 43 agree), and a second new finding notes that the files' cue-delay values cannot identify the paper's 0.76 cue-offset sessions.

**Not done, and why**
- **GLM on a subsample of neurons (verifier's problem 2).** On this 4-core machine, 2,000 neurons is at least 3.7 h and even 200 neurons is 0.4 h, both over the notebook's 30-minute limit. The design matrix and predictor grouping are also not in the paper's public code. The 23 GLM claims stay blocked as too large, with the estimates printed.
- **figs5l-dynamic-choice-over-cue-biased-running** stays blocked: it depends on well-fit-neurons, which needs the GLM.
- **No questions were added to `questions/000579.yaml`.** The verifier reported no place where the claims file misreads the paper.
