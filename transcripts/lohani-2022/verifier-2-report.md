## Verifier report, round 2: Lohani, Moberly et al. 2022 on dandiset 001172 (0.260129.0829)

The claims file has 26 claims. The attempt record has 26 outcomes: 12 reproduced, 8 partially_reproduced, 1 not_reproduced and 5 blocked (data_missing). The paper text (PMC10661869, BioC JSON and plain text) is saved in `paper/`.

### 1. Outcomes

I agree with 25 of the 26 outcomes. The one I do not accept as it stands is fig2c-face-best-predictor-calcium (partially_reproduced).

- **fig2c-face-best-predictor-calcium.** I don't dispute the arithmetic. With |speed|, wheel beats face in grabAM06 (0.147 vs 0.142, cell 35), so the result is partial. I dispute the reason for switching to |speed|. The record says "The paper's predictor is speed, so the main analysis now uses |WheelSpeed|". That is my round-1 point 3, and checked against the sources it was wrong:
  - The Methods define speed as "a differential of distance" after unwrapping (paper/PMC10661869.txt, line 64), which keeps its sign.
  - The paper's code computes it signed: `wheel_changepoints.m` line 50, `db1SpeedMpS = conv(diff(db1RunDistM)…)`. The code takes `abs` only for the threshold on mean epoch speed (line 135).
  - The file's WheelSpeed is very likely that same series: the code's change-point method run on it recovers every WheelActivation epoch to the sample (cell 13).
  - The code repository the attempt already uses as an input contains `Figure2Regression/Fig2RawData.mat`, the paper's own per-mouse R² values (6 × 52). For calcium, its single-variable face R² is above wheel in all 6 mice. If its rows 1 to 4 are grabAM05 to grabAM08 (not established), its wheel R² for mouse 1 is 0.0246 (calcium) and 0.0014 (ACh). This attempt gets 0.0253 and 0.0017 with signed speed for grabAM05, and 0.0483 and 0.0031 with |speed|. The other mice are mixed: for calcium, mice 3 and 4 sit closer to |speed|.
  
  On this evidence signed speed is the better-supported reading, and under it the claim is reproduced (cell 37). The outcome should either go back to reproduced with |speed| as the variant, or stay partial with a reason that matches the sources.
- **allen-parcel-link (partially_reproduced).** I agree. The record says openly that the per-session reading was chosen after the data were seen, and that the per-movie reading would make it not reproduced.

### 2. Statements the printed outputs do not support

- **Cell 0 and README** say the run "takes about 13 minutes". Cell 82 prints "notebook ran in 16.5 min".
- **Cell 81:** "Without grabAM06 … the tests across mice lose significance". The same cell's output (cell 80) has calcium locomotion minus high face at LSD p = 0.019, which is still significant.
- **Cell 81:** "The anterior-posterior gradients stay (rho = -0.874 and 0.437)". The calcium gradient does not stay the same. It goes from not significant with 3 mice (p = 0.125, cell 61) to p = 0.037 without grabAM06 (cell 80), which would meet that half of the s7-ap-gradient-sustained criterion. The record's response for s7-ap-gradient-sustained gives only the rho values and leaves out this change.
- **Summary (cell 83):** "without it the directions of Figures 3c and 3d hold but their tests across mice are not significant". Same issue: fig3c-calcium locomotion vs high face has p = 0.019 (cell 80).
- **fig2c-calcium, record deviation and response:** "The paper's predictor is speed". The paper's speed is signed (see section 1).
- **Minor, not shown by any output:**
  - Cell 6, "The pattern fits the code's removal of saturated pixels".
  - Cell 0, "6 visual stimulus sessions". Only 4 are opened.
  - README, "streams about 110 GB".
  - Cell 12, last sentence ("Locomotion onsets at lag 0 … tells a response from an offset"). It is unclear and backed by no output.
- **Cell 19 oddity:** keeping the final quiescent period should only add face onsets, but grabAM08 goes from 30 to 29. Cell 20's "changes no other mouse by more than 1" is literally true but hides the fact that the count went down. This does not affect a conclusion.

I checked every other "**Result:**" sentence, the Summary, the README table and the record's notes and findings against the outputs, and they match.

On my round-1 reasons: the `verifications` block carries every per-claim reason I gave in round 1, in my words or a close paraphrase, and the ones I attached to specific claims are there. Problems 9, 10, 12 and 14 do not appear in any reason. All four were marked as not affecting a conclusion, so this is acceptable. Problem 12 is discussed in cell 12.

### 3. Round-1 points

**Resolved:**
- 1: mask agreement per movie is now shown for the vis-stim sessions, and the 263 pixels are located in R-AUD.
- 2: per-mouse durations and a variant without grabAM06 were added, though cells 81 and 83 misdescribe the variant (above).
- 4 and 5: the wording is fixed.
- 6: a random-time null was added; all mice are above its 95th percentile.
- 7: predictors are now scaled within training folds.
- 8: exact Friedman p-values were added.
- 11: the code's behaviour is shown, with a variant.
- 13: the s3 notes were updated and a blue/violet correlation check was added.
- 9, 10 and 14 needed no change.
- 12 is described but not explained, which is acceptable.

**Addressed, but the fix is wrong:**
- 3: the switch to |speed| is not supported by the Methods or the code (section 1).

**Remaining items that bear on a conclusion:**
1. **fig2c-face-best-predictor-calcium.** Decide the wheel predictor from the sources: the code's signed `db1SpeedMpS` and the Methods' definition. Compare the per-mouse single-variable and ΔR² values with `Fig2RawData.mat`, after confirming its row-to-mouse mapping. This would also give the first external check of the ridgeMML port, which was still open from round 1. As one data point, in that file the calcium ΔR² of mouse 1 has pupil above face (0.026 vs 0.023), just as grabAM05 does here.
2. **The robustness text without grabAM06** (cells 81 and 83, and the record response for s7-ap-gradient-sustained). Correct it to say that fig3c-calcium locomotion vs high face stays significant (p = 0.019) and that the calcium sustained-state gradient becomes significant (p = 0.037). The outcomes don't change, because the criteria fix the 3 mice, but the stated conclusion about robustness does.
