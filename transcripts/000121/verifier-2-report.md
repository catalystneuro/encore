**Round 2 verification: Even-Chen et al. 2019 (doi:10.1371/journal.pcbi.1006808) on DANDI:000121, version 0.220124.2156**

The claims file has 20 claims, and the attempt record gives an outcome for all 20: 6 reproduced, 7 partially reproduced, 6 not reproduced, 1 blocked (data_missing). The paper's JATS XML and a text extraction are saved in `paper/`.

**1. Stated outcomes**

I agree with all 20 outcomes. Two need a comment:

- **plane-timecourse (partially_reproduced).** By the letter of the criterion this is reproduced. All four main times are within tolerance (cell 35: 70/90 ms and 270/350 ms; R's 350 ms sits exactly on its bound). I accept the downgrade, because R's divergence cannot be told from baseline noise: 6 of the 10 pre-onset bins are below 0.9. The record should say plainly that this is a judgment beyond the criterion. That matters because pca-variance follows the letter in the other direction: its variant passes (80.5%) and the outcome is not raised.
- **distance-error-and-plane-projection (reproduced).** This is correct by the criterion. The claim also says projection raises the error "to the level of the direction errors", and the paper gives p > .05 for every ring in J and R. In cell 73 this holds for only 1 of 6 rings (J 4 cm, p = 0.46). The notes disclose it.

**2. Sentences the printed outputs do not support**

- **Cell 36:** "J's times are robust". This is true only for the two checks added (pre-onset SD 0.03, and the non-overlapping converged state). Under the other thresholds in cell 35, J diverges at 150 ms (threshold 0.8, outside 0 to 100 ms) and converges at 390 ms (threshold 0.05, outside 250 to 350 ms). The same cell gives "(convergence 310 ms)" for R's variant without saying it is also outside 400 ± 50 ms. The attempt record's notes repeat "J's times are robust".
- **Cell 39:** "off axis J 0.101, R 0.083, p at most 3.0e-21". J's p is 3.1e-21 (cell 38).
- **Cell 42:** "Split by task and session, 110 to 180 trials per distance". No per-task, per-session trial counts are printed in cell 41.
- **Summary (cell 75):** the array labelled PMd "has 29 silent channels and no target signal". Cell 26 prints 40 of 96 of those channels as significant for R when sessions are pooled. Cell 9 shows up to 6 significant delay channels and 16 movement channels per session. Cell 10's wording, "almost no target information", fits the decoding results. "No target signal" does not. The record's electrode_group finding should also mention the 40 of 96.
- **Attempt record, delays-and-times notes:** "the means are 342 ms (J) and 340 ms (R), just inside". Only R's value is just inside (bound 342). J's 342 ms is well inside its range of 311 to 381 ms. Cell 24 states this correctly.

Every other sentence I checked matches the printed numbers. That covers the "**Result:**" cells 18 to 74, the Summary, the README and the record's notes and findings. The checks include:
- the trial-count percentages;
- the 484 to 1963 s gaps between trials;
- 99.93 to 99.95% of spikes inside trials;
- the 12 of 13 PCA values within tolerance;
- the share of seven plane values within tolerance under any pairing (at most three);
- the threshold ranges of 10 to 150 ms and 230 to 390 ms;
- the per-session counts;
- the Fig 4d inset restriction, which I confirmed against the paper's legend.

The record states my round-1 reasons faithfully and in my own wording. Each problem from round 1 is attached to the claim it bears on. The only cuts are minor details, such as B3's per-session rate range, and those are covered in the responses.

**3. Round-1 points**

Resolved:
- **B1:** the variant with onset searched only after the go cue is added, the share of early onsets is printed, and the conclusion says R's mean matches only because those trials are kept.
- **B2:** with deviations from session × condition means the correlations barely change.
- **B3:** spikes fall within trials, so the main day mean is the rate over trial time.
- **B4:** the pre-onset spread of D and the non-overlapping converged state are added, the outcome is changed to partial, and "starts at the center" is addressed.
- **B5:** counts per task and session are added.
- **B6:** the per-session p values now print correctly.
- **B7:** the ring task is dropped from the per-task test.
- **B8:** a paired test is added and the leak is recorded.
- **B9:** the reading that counts failed trials without a go cue is added.
- **B10 to B13:** each is now stated in the notebook.

Under C:
- Done: spikes between trials, session confounds, divergence robustness.
- Cannot be settled: whether the horizontal/vertical swap comes from the paper or the conversion, and the paper's trial subsets (912 trials, 2237 held-out).

Still open and bearing on a conclusion:
- **plane-timecourse:** the record should say the outcome is a judgment beyond the criterion, and should note that both monkeys' times depend on the threshold.
- **distance-error-and-plane-projection:** the part of the claim about projected error matching the direction errors holds for 1 of 6 rings. The test also compares against unrestricted arc errors, while the paper's Fig 4d inset uses errors within the 4 cm ring's range. The restricted comparison was not run.
- **pca-variance:** this stays fragile. The outcome depends on how the day's mean is taken (72.8% against 80.5% for R's PC1). The choice is now justified and disclosed, so nothing more is needed beyond the statement already made.
