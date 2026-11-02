**Round-2 verification: Silkuniene et al. 2025 (doi:10.1016/j.bioelechem.2025.109016) on DANDI:001277 v0.250701.1610**

The claims file has 17 claims and the attempt record has 17 outcomes, one per claim. Cell numbers below refer to the re-executed notebook. They sit one higher than in round 1 from cell 9 on, because a channel-metadata cell was added.

**1. Outcomes and assumptions**

| Claim | Record | I agree? | Notes |
|---|---|---|---|
| fig6b-peak-900ns-not-significant | reproduced, `assumed: true` | Yes | The assumption (Fig. 6 = the five complete plate rows) is stated in the deviations and is reasonable. Only the "900 ns highest" half depends on it: 900 ns is highest in 14 of 21 subsets (cell 21). No test is significant under any well choice, including the paired variant (cell 23). |
| fig6c-normalized-decline-similar | not_reproduced | Yes | The deviation says the outcome does not rest on the assumption. That is correct: the 300 against 900 ns gap at +2 mm (cell 26) does not involve the 600-ns wells. |
| fig6d-longer-pulses-sharper-peak | blocked, methods_underspecified | Yes | Not reproduced under any well choice except the one that drops both P1 row B wells (cell 31). The notes say this, but the outcome has no `assumed: true`. Under the record's own logic it should carry the flag. |
| fig6d-600-900-differ-from-300 | blocked, methods_underspecified | Yes | Readings differ with the main wells and with all 7 (cell 35: one significant comparison in 12 readings, none in 12, in both sets). It does not rest on the assumption. |
| fig6d-900ns-fwhm | blocked (inherits from parent) | Conditionally | In round 1 I gave reproduced. The claims file does list `depends_on: fig6d-longer-pulses-sharper-peak`. I cannot see docs/protocol.md to check the cited rule (Author, step 1.5). If the rule is as quoted, blocked is correct. The claim's own criterion is met in 6 of 12 readings (cells 38 and 39), and the record says so. The block also inherits the parent's dependence on the well choice, so the missing assumption flag applies here too. |
| fig5-yp-lorentzian-pr-gaussian | blocked, metadata_insufficient | Yes | Now matches my round-1 outcome. |
| fig5-yp-spot-slightly-larger-than-pr | blocked, metadata_insufficient | Yes | Now matches my round-1 outcome. |
| The 10 data_missing claims | blocked, data_missing | Yes | No change from round 1. |

I found no new misreading of the paper in the claims file. My round-1 point 9 still stands as a claims-file comment: the linear trend on the 3 means has 1 degree of freedom, which makes that reading nearly impossible to pass.

**2. Text against the printed outputs**

- **"all 8 readings" in the offset fits.** This appears in cell 44 ("the Gaussian fits the mean Pr profile better than the Lorentzian under all 8 readings"), in the record's fig5-yp-lorentzian-pr-gaussian notes, and in the round-1 response. Cell 43 prints 8 fits, which are 4 readings × 2 functions. The Gaussian is better in all 4 readings.
- **300-ns FWHM range.** Cell 33 and the fig6d-longer notes say "2.11 to 2.13 mm at 300 ns". Cell 30 prints 2.1041 to 2.1352, which is 2.10 to 2.14.
- **1-mm p-value range.** The same text says "10 of 12 with 1-mm steps (p 0.042 to 0.050)". The 10 significant readings run from 0.0419 to 0.0479. The value 0.0504 belongs to the two readings that are not significant.
- **Plate ratio.** Cell 24 and the fig6b notes say "P3 two to four times P1 and P2". Cell 22 gives ratios of 2.1 to 4.6 (at 900 ns, 1630 against 357).
- **Where the fig6c gaps fall.** Cell 28 and the fig6c notes say "The gaps are mostly between 300 and 900 ns at 1 to 2 mm". In cell 26, with the main wells and contiguous ROIs, 8 of the 12 to 14 gaps are 300 against 600 ns, and some gaps lie at 2.4 to 4.9 mm and 6.9 mm. Over all readings, 300 against 900 ns accounts for 52 of 96 gaps.
- **Subsets in fig6c.** Cell 28 lists "every choice of 5 of the 7" among the readings, but cell 26 runs the subsets only for 1-mm steps, ±5 mm and the mean-bar rule. The outcome still holds, because the 300 against 900 ns gap does not depend on the 600-ns wells.
- **Unscaled distances.** The Summary (cell 54) says "unscaled distances give the same outcomes". Cell 39 runs unscaled distances only for the three fig6d claims, not for fig6c or Fig. 5.
- **Cell 0 status table.** It still lists fig6d-900ns-fwhm and both Fig. 5 claims as "tested", which contradicts cells 40, 47, 51 and 54.
- **README overall.**
  - "18 CT26 monolayers exposed to packets of 300-, 600- or 900-ns pulses": cell 4 shows 17 exposed wells and 1 sham.
  - "With those rows the FWHM trend is close to the paper's under most readings": the slope is significant in 28 of 48 readings (cell 30), and p is near 0.003 only in the 12 contiguous readings on individual values.
  - "about ten minutes" and "about 13 GB": no output shows these, and cell 0 says streaming takes about 8 minutes.
- **What checks out.** Every other number in the "**Result:" cells (24, 28, 33, 36, 40, 47, 51), the Summary, the README and the record's notes and findings matches the outputs. I also confirmed from the cell-42 figure that two footprint marks in P1_20240926_B3 fall on no visible footprint, as cell 44 says.
- **My round-1 reasons.** The record states them in my own words and faithfully. For fig6b, fig6d-longer and fig5-yp-lorentzian, points from section B of my report were merged into the outcome reason. The meaning is unchanged.

**3. Round-1 points**

Resolved:
- **Point 1 (Fig. 5 well assumption):** both Fig. 5 claims are now blocked.
- **Point 3 (which channel is Pr):** cell 9 reads the OME metadata: channel 0 is Cy3 (565 nm) in all 5 files.
- **Point 4 (Pr footprints in P1_20240926_B3):** cell 43 adds the rim contrast, and readings that leave that well out are shown.
- **Point 5 (distance scaling):** cell 39 adds the unscaled variant. The fig6d results are unchanged and the 900-ns FWHM is within tolerance in 6 of 12 readings.
- **Point 6 (overlapping contiguous ROIs):** now stated in a deviation and in cell 47.
- **Point 8 (identical pooling readings):** stated in cell 29.
- **Point 10 (plate-row blocking):** cell 23 adds a paired variant, which also finds no difference.
- **Section C:** per-well Pr profiles, fits with an offset and the Pr rim contrast are now shown.

Unchanged, but they do not affect a conclusion:
- Point 7 (the darkest-footprint background).
- Point 9 (claims-file comment, above).
- The pre-exposure Hoechst images are still not used, and plate P3 has no 2-h check that cells were present at the centre.

Remaining issues that bear on a conclusion:
1. **fig6d-longer-pulses-sharper-peak and fig6d-900ns-fwhm** depend on leaving out P1_20240926_B2 and B3. With either well kept, fig6d-longer becomes not reproduced. The notes say this, but neither outcome is marked `assumed: true`.
2. **fig6d-900ns-fwhm** is blocked only through the protocol's dependency rule, which I could not check. If the rule does not apply, its own criterion gives reproduced.
3. **Miscounts and imprecise ranges** listed in section 2 (the "8 readings", the 300-ns FWHM range, the 1-mm p range, the plate ratio, where the fig6c gaps fall, the "same outcomes" claim, the stale cell-0 table). None changes an outcome, but they should be corrected.
