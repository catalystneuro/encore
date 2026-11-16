**Verifier report, round 2: kay-2008-01 (doi:10.1038/nature06713, CRCNS vim-1)**

The claims file has 23 claims and the attempt record has 23 outcomes, with the same IDs: 10 blocked, 7 reproduced, 3 partially_reproduced and 3 not_reproduced. Cell numbers below are 0-based indices in the re-executed notebook, which has shifted since round 1.

### 1. Outcomes and assumptions

| Claim | Agree? | Comment |
|---|---|---|
| fig3-s1-repeated-120 | yes | Cell 11: 109/120 under O1a-O5a and O1b-O5a. |
| fig4a-s2-repeated-120 | yes | Cell 11: 87/120 and 86/120. |
| fig4a-single-trial | yes as blocked, but weakly founded | The record admits the too_large estimate is overstated. Point 2 below. |
| fig4a-noise-ceiling | yes | Follows single-trial. |
| fig4b-set-size-1000, fig4b-extrapolation, fig4c-retinotopy-only-extrapolation, suppfig8-constrained-models, time-two-months, time-fourteen-months, suppfig10-retinotopy-validation | yes | data_missing. |
| suppm8-retinotopy-only-120 | yes, with a caveat | The outcome rests on reading the luminance channel relative to the grey background, which departs from SM 8. The record states this only as a deviation, without `assumed: true`, and the SM 8 reading was not run. It should carry `assumed: true` or be run. |
| errors-similar-images | yes | Cell 27. |
| suppfig4-500-voxels | yes | Cell 39. |
| supptable1-voxel-counts | yes | Cell 19. |
| supptable1-predictive-power-by-area (`assumed: true`) | yes | The assumption is stated and reasonable: Supplementary Table 1's totals equal the label counts including the NaN voxels. Over voxels without NaN the values come out above the paper's (S1 V1 42.3 against 40, S1 V3 20.1 against 17, S2 V1 29.0 against 25), which is consistent with the paper counting those voxels as not significant. |
| supptable1-snr | yes as blocked, but weakly founded | As fig4a-single-trial. |
| methods-v4-poor | yes, fragile | 17.5% against 18.2% from one seed. |
| fig2-representative-voxel (`assumed: true`) | yes | Adopting O5 (a) is stated and reasonable: the criterion itself names 2.9 cycles/deg as the highest frequency, and only O5 (a) gives it. Under O5 (b) all three parts hold. |
| suppfig7-roi-tuning | yes, incomplete | Readings (b) of the models and of the voxels were not run. The criterion says "under one reading", so not_reproduced covers only the readings run. The record says so. |
| suppfig11-rf-size-eccentricity (`assumed: true`) | yes | Adopting the circular bounds is stated and reasonable, since Figure 2's legend calls the circle "the bounds of the stimulus". The disc filter actually run (2 SD disc inside 9.5°) is not the ±2 SD square inside 10° that the reading implies. |
| suppdisc1-classification-extension | yes | Cell 29. |
| suppm7-selected-voxels-v1 | yes | Cell 25. |

### 2. Statements the printed numbers do not support

- **Record, fig4a-single-trial notes:** "The notebook's estimate (about 605 minutes)". Cell 17 prints "about 581 minutes".
- **Record, supptable1-snr notes:** "The notebook's estimate (about 172 minutes)". Cell 17 prints "about 161 minutes". Both figures look like leftovers from the earlier run.
- **Notebook cell 32 (criterion text for suppfig11):** "'Inside the stimulus' is read as inside the 20 degree square; inside the circular aperture is shown too." This contradicts the adopted reading in cell 34 and in the record, which use the circle.
- **Record, suppfig7-roi-tuning notes:** "gratings inside the aperture remove them ... without changing the spatial frequency curve's shape." Cell 37 shows the curve does change shape. Under S1 O5a, full-field gives [-2.25, -3.59, -0.28, 65.4, 285.4] and the aperture gives [0.145, 0.257, 0.483, 0.802, 0.935]. Only the peak at the highest level is unchanged. Cell 38's own wording ("still rise to the highest level") is correct.
- **Record deviation and vim1.py docstring:** "about 30% of the initial fits" stop at iteration 0. Cell 7 shows 29% to 38% across the six fits (S1 1944, 2100 and 2401 of 6702; S2 2059, 2240 and 2316 of 6083), so about a third.
- **Entry README:** "Predictive power falls from V1 to V2 to V3 | Reproduced" has no "(assumed)", although the record sets `assumed: true` and the other assumed rows carry the label. The same applies to the Summary in cell 41.
- **Summary (cell 41):** "`Stimuli.mat` ... (it is MATLAB 5)". No printed output shows this; it rests on the markdown in cell 6. This is minor.

Every other sentence I checked matches the printed outputs. That covers cells 0, 6, 10, 15, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40 and 41, the README and all other record notes. Examples:
- 44 and 45 errors.
- p ≤ 0.00015.
- "3.8 and 2.4 points".
- ρ 0.535 to 0.676 and p < 1e-26.
- SE about 740.
- 39.1 min against "about 40 minutes".

**My round-1 reasons in the record:** they are restated faithfully in my own words, merged from my table and my problem list. One omission: problem 10 (the stopping-rule reading) appears in no `reason`, only in the author's response under fig3.

### 3. Round-1 points

**Resolved:**
- 1: suppfig4 is now partially_reproduced. Two of the four O1/O5 combinations are still unprinted; this does not affect the conclusion.
- 3: the gratings docstring is corrected, and the ratios with the DC offset are no longer cited.
- 5: the NaN-voxel choice is stated as an assumption, with a sound reason.
- 8 and 10: now stated as deviations.
- 12: I accept the response; the criterion's "other 119" includes the selected image.
- 13: reported to a reader.

**Remaining, and bearing on a conclusion:**
- **Point 2.** fig4a-single-trial, fig4a-noise-ceiling, supptable1-snr and the single-trial half of suppfig4 stay "too_large" on an estimate the author agrees is overstated. A BRS fit exists but is not in the notebook. The record's estimates also mismatch cell 17, as quoted above.
- **Point 4.** suppm8 rests on the non-SM 8 luminance channel, which was not run. The margins are 3.8 and 2.4 points. The outcome should be marked `assumed: true`.
- **Point 6.** For suppfig11, the strict filter (±2 SD square inside a 10° circle) was not run, and the adopted circular reading uses a 9.5° disc filter. The partial outcome could change either way.
- **Point 7.** For suppfig7, the model-I and fixed-voxel-set readings were not run, so not_reproduced is incomplete.
- **Point 11.** There is no seed sensitivity check. methods-v4-poor rests on a 0.7-point S1 margin from one seed.
- **fig2 (from section C).** There is no Gaussian fit to the final envelope. The O5 (a) peak at +0.24° sits on a plateau (0.98 to 1.0 in cell 35), so the "just below" failure is fragile.

**Remaining, not bearing on a conclusion:**
- Point 9: bootstrap averaging under O5 (a) was not run.
