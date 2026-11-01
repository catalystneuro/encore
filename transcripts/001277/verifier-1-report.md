**A. Outcomes** (17 claims in the claims file; the notebook tests 7 and treats 10 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| fig6b-peak-900ns-not-significant | reproduced | Cell 20, main wells: 900 ns has the highest centre YP (899 against 866 and 551). Bonferroni t-tests give p ≥ 0.876 and the ANOVA gives p = 0.543. No test reaches p < 0.05 with all 7 600-ns wells, with the all-4-footprint background, with Lorentzian `a`, or in any of the 21 subsets. |
| fig6c-normalized-decline-similar | not_reproduced | Cell 23: every reading (1-mm or contiguous ROIs, to 5 mm or to 7 mm, main or all 7 wells, mean or longer bar) has at least one distance where the error-bar gap is longer than the bars. The gaps mostly fall at 1 to 2 mm, where 300 ns is broader. The readings agree, so the criterion gives not reproduced. |
| fig6d-longer-pulses-sharper-peak | blocked (methods_underspecified) | Cell 26: the slope is negative with p < 0.05 in only 28 of 48 readings. Contiguous ROIs on individual values give p = 0.002 to 0.004. 1-mm ROIs on individual values with a linear trend give p = 0.045 to 0.050 (0.0504 at the 6-mm half-range). Fits to the 3 means mostly fail. With all 7 600-ns wells it is significant in 0 of 48 readings (cell 27). |
| fig6d-600-900-differ-from-300 | blocked (methods_underspecified) | Cell 30: 900 v 300 is significant only with contiguous ROIs (corrected p = 0.005 to 0.009), and 600 v 300 is never significant (p ≥ 0.058). The readings differ (one comparison significant in 12, none in 12), and no reading reproduces the claim. Its parent claim is also blocked. |
| fig6d-900ns-fwhm | reproduced | Cell 32: with contiguous ROIs, FWHM is 1.69 to 1.71 mm and 11.0 to 11.1% of 15.3 mm, both inside tolerance, in 6 of 12 readings. With 1-mm ROIs it is 1.78 to 1.80 mm, just outside. All five 900-ns wells are used, so this does not depend on the choice of 600-ns wells. |
| fig5-yp-lorentzian-pr-gaussian | blocked (metadata_insufficient) | The test assumes that the dandiset's 600-ns wells are Fig. 5's 0-mm group. Nothing in the archive says so: the dandiset description names only the pulse-duration experiment, and the raised-electrode wells that would belong to the same series are absent. If the assumption holds, the claim fails in every reading: in cell 36 the Pr Lorentzian R² (0.81 to 0.95) is above the Gaussian R² (0.72 to 0.86) in 12 of 12 readings. |
| fig5-yp-spot-slightly-larger-than-pr | blocked (metadata_insufficient) | Same assumption. If it holds, the claim also fails: in cell 38 the YP/Pr FWHM ratio is 0.20 to 0.41 and the Pr spot is 6.4 to 8.9 mm wide, so it is larger than the YP spot in every reading. |
| fig5-raised-electrodes-weaker-centre | blocked (data_missing) | The archive description says the array sat at 0 mm, and no file has raised electrodes. |
| fig3-cancan-centre-enhancement | blocked (data_missing) | There is no packet-rate series and no single-pulse control. The 0.2-MHz part could be looked at on the 600-ns wells (cell 15 shows 0 mm above 4 mm in every main well), but the controls are absent. |
| fig3-lorentzian-decline | blocked (data_missing) | There is no packet-rate series. Only the 0.2-MHz-like protocol is present; cell 27 shows per-well fit R of 0.95 to 0.99, but these are not the Fig. 3 wells. |
| fig4b-suppression-near-electrodes | blocked (data_missing) | There is no rate series. On the 600-ns wells the centre/near ratio is 25 at 6 mm and 10 at 7 mm (cell 41), well below 40. This is shown, not judged. |
| fig4b-centre-no-rate-effect | blocked (data_missing) | Only one packet rate is present. |
| fig4c-fwhm-falls-with-rate | blocked (data_missing) | Only one packet rate is present. |
| fig7be-burst-number-centre | blocked (data_missing) | Every file says "repeated 2 time(s)", and there are no CHO cells (the archive strain is CT26 only). |
| fig7-fwhm-burst-number | blocked (data_missing) | Same reason. |
| fig7-sharpest-peak-1-burst-ct26 | blocked (data_missing) | There are no 1-burst wells. |
| fig2-heating-below-44c | blocked (data_missing) | There are no thermochromic film images. All 49 assets are well images (checked via the API). |

**B. Problems**

1. [affects a conclusion] Cells 33 to 38: the two Fig. 5 claims rest on assigning the 600-ns wells to Fig. 5's 0-mm group. The only support is the same protocol and matching n (7 YP and 5 Pr against n = 6–7 and 4–5). Against it: Pr images also exist for the 300- and 900-ns wells on P1 and P2, and the dandiset title and description describe the pulse-duration experiment only. The cell-34 Pr images also show bright Pr rings at every footprint and a broad Pr level across the whole array, about 40 to 55% of the centre within ±5 mm (cell 39). A Gaussian with no offset cannot fit that, so these may not be comparable to the paper's Pr data. The notebook reports the results as tested; they should rest on the assumption explicitly, or be blocked.
2. [affects a conclusion] Cells 16 and 17: the choice of the five main 600-ns wells (the five complete plate rows) is stated, decided independently of the results, and reasonable. P1_B2 has uptake over the whole array and a fitted FWHM of 19 mm (R = 0.64); P1_B3 lost cells at the centre. But fig6d-longer changes from blocked to not reproduced in every reading if either well is kept (cell 27: only the subset that drops both reaches any significance). The fig6d conclusions therefore depend on this exclusion.
3. [affects a conclusion if wrong] Cell 8 takes channel 0 of the Cy3-DAPI files as Pr and channel 1 as Hoechst, inferred from the series name. This is never checked against the OME channel names. The dark footprints and central peak in channel 0 make Pr likely, but it is unverified.
4. [does not affect a conclusion] The cell-34 Pr image of P1_20240926_B3 shows the two left footprint marks on no visible footprint. The YP image of the same well (cell 13) has one mark slightly off its footprint. Both are in the non-main well P1_B3, which is used only in the Fig. 5 readings and the all-7 variants.
5. [does not affect a conclusion] `diagonal_profiles` rescales each diagonal so the footprint centre sits at 9.05 mm. This is the author's choice, not the paper's. The docstring says unscaled distances are "checked in the notebook", but only the footprint diagonal lengths are shown (17.7 to 18.5 mm, within 3%). That is too small to move the 900-ns FWHM across its tolerance edges.
6. [does not affect a conclusion] `positions("contiguous")` with axis-aligned 406 × 325 µm boxes on a ~45° diagonal: a 0.406-mm step moves the box only 0.29 mm along each axis, so neighbouring ROIs overlap. Fit p-values (cell 36 "max fit p") treat overlapping samples as independent.
7. [does not affect a conclusion] `background(which="darkest")` takes the minimum of four footprints, which biases the background low. The all-4 variant is shown and does not change any outcome (cells 20 and 28).
8. [does not affect a conclusion] The "avg" and "all" pooling readings give identical fits (cells 26, 30 and 32), as cell 25 notes, so that reading adds nothing.
9. [does not affect a conclusion; claims file] The fig6d criterion includes a linear regression on the 3 means, which has 1 degree of freedom and is nearly unwinnable. Dropping it would not change the outcome, because the 1-mm and contiguous readings still disagree.
10. [does not affect a conclusion] Cell 21: centre YP differs about 2-fold between plates (P3 against P1 and P2). The unpaired t-tests and ANOVA in fig6b follow the criterion but ignore that the experiments are blocked by plate row.

Helper functions checked on synthetic inputs: `fit_curve` recovers a known Lorentzian FWHM and the Gaussian 2.4σ exactly. `gap_rule` is correct. `find_electrodes` finds synthetic footprints within about 1.5 blocks. `background` and `diagonal_profiles` recover a 1.70-mm Lorentzian as 1.73 mm (1-mm steps) and 1.74 mm (contiguous); the roughly 2% inflation comes from averaging over the ROI.

**C. What I could not check**

- Which Cy3-DAPI channel is Pr. Printing the OME `Channel Name` and emission wavelengths for one file would settle it.
- Whether the 600-ns wells are the Fig. 5 wells. Nothing in the archive identifies them.
- The Pr profiles of individual wells and an R² for a fit with an offset. Showing these would tell a broad pedestal apart from a misplaced background.
- FWHM under unscaled pixel distances (`diagonal_profiles` without the 9.05-mm rescaling). The docstring says it is checked in the notebook, but no output shows it.
- Footprint accuracy in the Pr images. A per-well minimum rim contrast for the Pr images, like the one cell 11 prints for YP, would have shown it.
- Hoechst images taken before exposure, to confirm cells were present at the centre of the main wells. They are not used, and plate P3 has no 2-h Hoechst image.
