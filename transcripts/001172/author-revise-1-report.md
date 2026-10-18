I've answered every point in the round-1 report. The entry was re-run three times with `python tools/entry.py all entries/001172-lohani-2022`, and the last run passed in 12.1 minutes. The last two runs gave identical numbers. Nothing is committed.

**Outcome change (1 of 26)**
- **fig2c-face-best-predictor-calcium: reproduced → partially_reproduced.** The verifier noted that the wheel predictor was signed speed, while the paper says "locomotion speed". I made |speed| the main predictor and kept the signed series as a variant.
  - With |speed|, wheel speed beats face PC1 in grabAM06 (0.147 vs 0.142), so face is best in 3 of 4 mice. Its unique contribution is largest in 3 of 4 mice (Friedman p = 0.105).
  - With signed speed the claim would still be reproduced. The record lists this dependence as a deviation.
  - The change lowers the outcome. No other outcome moved: the ACh claim and fig2a/fig2b hold under both predictors.

The verifier agreed with all 26 outcomes as they stood. The new tally is 12 reproduced, 8 partially reproduced, 1 not reproduced and 5 blocked.

**Outputs added**
- **Mask check on the 4 visual-stimulus sessions:** all 8 movies agree at 1.0. The 263 always-zero pixels in one calcium movie all lie in the right AUD parcel, which the left-hemisphere analyses don't use.
- **Hemodynamic check (one session, first 2000 frames, slow drift removed):** raw blue and violet correlate at r = 0.576, while the archived blue and violet ΔF/F correlate at 0.070. The archived blue follows raw blue (0.825) but not raw violet (0.032). This fits a correction having been applied, but doesn't show which one.
- **Null for the transient peaks:** the same peak at random times during quiescence, 200 draws. Every mouse's transient is above the null's 95th percentile.
- **Variant keeping the last quiescent period for face onsets:** the code's `extractFacePupilTStamps.m` drops it. Keeping it gives ACh 0.728 and calcium 0.871, still outside tolerance.
- **Robustness without grabAM06**, plus per-mouse epoch durations by state. Every direction holds in both remaining mice, but fig3c-ACh (p = 0.207) and fig3d (p = 0.247) lose significance. The conclusions now say those p-values rest on grabAM06.
- **Exact Friedman p-values:** 0.0046 and 0.042.
- **Visual-stimulus screen coordinates:** identical in every session. The files don't say where the monitor stood, which is recorded as a finding.
- **grabAM08 calcium-wheel lag of −13 frames:** described in the notebook but not explained. That session's frame timing is fixed independently from the raw movie.

**Corrections**
- Predictors are now scaled using only the training folds (the leakage the verifier flagged). This moves fig2 numbers only in the third decimal.
- The s7-ach conclusion said "two mice each way"; the output shows three negative and one positive.
- The conclusions for the two absence results now say they carry little weight.
- I added findings on signed WheelSpeed, the zeroed pixels and the missing monitor position. The README, header, runtime (13 min) and data size (about 110 GB, measured) are updated.
- `verifications` round 1 is recorded for all 26 claims, with the verifier's reasons and my responses.

**Not done**
- **Native-space hemodynamic regression for s3:** the registration transforms are not in the files, so it would mean reimplementing the spatial regression on about 50 GB per session. s3 stays blocked, and the notes now give that reason for its ACh3.0 part.
- **Fidelity of the ridgeMML port:** can't be checked because the paper's regression code is not public.
- **Paper text:** I didn't download any, so `paper/` is empty.
- **Untracked files:** dotfiles, `.idea`, `scripts` and similar are in the working tree. I didn't create them and left them alone.
