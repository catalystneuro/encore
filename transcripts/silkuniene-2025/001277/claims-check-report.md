The file is ready for an attempt. I made 12 corrections from the paper, the last entry under `checks` has `ready: true`, and the checker still passes after the edits.

**Checker result:** `17 claims, 17 quotes, 14 statistical values, 0 problems` (13 statistical values before my edits).

**Changes, by claim:**
- **fig6c-normalized-decline-similar:** the -5 to 5 mm range was the writer's choice, since the text gives no range. I added "every measured distance" as a second reading, and the claim is blocked if the readings disagree.
- **fig6d-longer-pulses-sharper-peak:** the Fig. 6D legend doesn't say whether the trend was fitted to the 15 individual FWHM values or the 3 means. Both are now readings.
- **fig6d-600-900-differ-from-300:** the statement tied p = 0.028 to 600 ns and p = 0.0072 to 900 ns. The legend doesn't say which is which, so I reworded it.
- **fig3-cancan-centre-enhancement:** the criterion required centre YP to exceed YP at 6 and 7 mm at every packet rate. The paper doesn't say that; it reports the suppression near the electrodes as depending on rate. It is now judged as a peak at the centre, compared against 4 mm (the edge of the Fig. 3 fit range). The 6 and 7 mm values are shown but not judged.
- **fig3-lorentzian-decline:** added the paper's p < 0.001 to the criterion.
- **fig4b-suppression-near-electrodes:** the source now reads paragraphs 2 and 4. The rate-dependent decline at 6 and 7 mm is stated in paragraph 4, not paragraph 3.
- **fig4b-centre-no-rate-effect:** added what happens when the two readings of which rates are compared disagree (blocked).
- **fig4c-fwhm-falls-with-rate:** the statement's "no further gain at 0.2 MHz" was never tested. It is now checked with the error-bar gap rule from the Methods.
- **fig5-yp-lorentzian-pr-gaussian:** added the reported fit significance (p < 0.0001) under statistics.
- **fig7be-burst-number-centre** and **fig7-fwhm-burst-number:** the paper doesn't say whether the linear fits used individual experiments or means. Both are now readings.
- **fig7-sharpest-peak-1-burst-ct26:**
  - The expected ratio of 45 ± 9.5 covered 35.5 to 54.5, not the 36 to 55 that the protocol's rule gives. I set the value to 45.5.
  - I added a check that this is the smallest FWHM in the study, which the statement claims.
- **fig2-heating-below-44c:** the statement said "under the electrodes" and dropped the 2-burst and 6-burst details. I reworded it to match Methods 2.3.

**Still open (logged in the check entry):**
- **fig3-cancan-centre-enhancement:** "enhanced at the center" could also mean higher centre YP than the control's centre. I kept the reading of a peak at the centre, because the text contrasts it with the control's decrease toward the centre.
- **fig7-sharpest-peak-1-burst-ct26:** the paper doesn't say how it gets 2.3% of the array area. A 1.1-mm circle over the array square gives 0.8%. The figure is reported, not judged.
- **Fitting details:** the fit range for individual FWHM fits (4, 5 or 6 mm) and the spacing of measurement regions along the diagonals are not settled by the paper. They stay as readings in the criteria.

Each of the paper's main findings has a claim, and all claims come from this paper. Nothing was committed or pushed.
