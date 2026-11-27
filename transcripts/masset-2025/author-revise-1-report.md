I've revised the attempt for round 1. Three outcomes changed, the other points are fixed or answered, and the record now has the round under `verifications`. The entry has no clean-run stamp, for reasons given at the end. `python tools/entry.py check` passes with 0 errors.

**Outcomes that changed**
- **cued-delay-neurons: not reproduced → reproduced (rests on an assumption).** The paper's table, `FinalAverageArray.mat`, holds 10 ms firing rates for the 11 flagged neurons that the spike file lacks. For the 67 units in both, the cue responses from those rates match the spike counts closely (mean difference 0.43 spikes/s per trial, median correlation 0.987). With those 11 added, there are 78 neurons and 48 pass the selection (48 to 50 over the five seeds). Both counts are within tolerance. From the spike file alone the counts are still 67 and 43.
- **session-trial-counts: reproduced → partially reproduced (rests on the same assumption).** The 11 extra neurons come from 5 more sessions. On all 78, the cued delay task has 44 sessions under one reading and 32 under the other, both outside 36 ± 3.6. The trial means and the VR counts still hold.
- **ed9g-models-agree: blocked → partially reproduced.** I wrote analytic gradients for the model's fit, which made all 200 fits run in about 19 minutes, in a new notebook, `vr_reward_expectation.ipynb`. The two models' discount factors correlate at rho = 0.743, against 0.93 ± 0.093.

**Kept, with the disagreement recorded**
- **ed3f-discount-factor-reliable and ed8b-slope-correlates-with-discount:** the verifier gives not reproduced. I kept partially reproduced, because the criterion has no partial clause and the correlations are strong and significant, only weaker than reported.
- **ed10-cross-task-decoding:** the verifier gives reproduced but fragile. The two readings now use the same shuffles, and I added 20 shuffle draws. At 9.375 s, under the claim's seed, the first draw gives p = 0.098 and only 6 of 20 draws pass, so it stays partially reproduced. One other seed (+2000) passes, so it is marked seed-sensitive.

**Other fixes and added outputs**
- **Decoding readings:** I confirmed the verifier's point that the "all components" and "first 12" readings give the same decodings (largest difference 1.9e-6 s). They now share their shuffles, and 20 draws are reported for fig2k, ed5g and ed10. For ed5g, mouse 3044 at 9.375 s passes in 5 of 20 draws, so it stays partially reproduced.
- **ed6g:** I added 10 simulation draws. None matches the paper at all four delays and 3 match at three, so it stays not reproduced.
- **ed8ej gains:** I downloaded the paper's code from its Mendeley deposit. It does compare the population's a/γ^0.1 with the per-mouse a. The like-for-like versions give 0.698 and 0.674 for mouse 3044, also below the 0.702 bound, so the outcome doesn't change. I added a `code_mismatch` finding at the end of the findings list.
- **Last VR bin:** it extends a median 0.042 s past reward. Leaving it out of the z-score s.d. changes the mean slope only slightly (0.0836 to 0.0849), and the counts stay the same.
- **Smaller fixes:** the `split_halves` docstring now calls disjoint halves a deviation from the code. A held-out R² that can't be computed is now left out of the mean instead of giving −inf. Decodings with no defined distance are left out of the test.

I added no question for a reader, because the report names no place where the claims file misreads the paper.

**How the run was done**
- **The `all` command didn't run.** I started it in the background and it was killed with no output. Running it in the foreground wasn't possible: the four notebooks take about 2 hours together, which is the tool's limit for one command.
- **What I ran instead:** I ran `check`, then executed each notebook in the foreground with the same nbconvert command and environment that `run` uses. Timings: 28, 34, 27 and 16 minutes. I updated `result.json` with them.
- **Conclusions written after the run:** I wrote the conclusions once the numbers were in, then copied the new text cells into the executed copies. Before copying, I checked that every code cell matches the run.
- **No clean-run stamp:** this run therefore left no `.clean-run.json`. A fresh `all` run in CI should give the same outputs.
- **New notebook:** `vr_reward_expectation.ipynb` is a new file and is not yet tracked by git.
