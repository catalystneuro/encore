I wrote `claims/001047/10.1016-j.bioelechem.2025.109016.yaml`. The quote checker passes: 20 claims, 20 quotes, 15 statistical values, 0 problems.

**Text read.** The NIH author manuscript from PMC (NIHMS2087238, PMC12331426): main text, Methods, Results, Discussion and the legends of Figures 1 to 7. PMC lists no supplement and the paper cites none. I did not read the version of record. There is no PDF, so I saw none of the figures. The paper links no code ("Data will be made available on request"), so no method detail is settled by code. The dataset's title on DANDI and its species (mouse and hamster) match the paper's CT26 and CHO monolayer experiments.

**Claims.**
- **Count:** 20 claims, all quoted and none inferred.
- **Statistics:** 7 claims carry them, 15 entries in all. They are the fit p-values, the t-tests against 1 Hz with Bonferroni correction (p = 0.03, 0.02, 0.09), R = 0.77, the slope tests (p < 0.0001, 0.003, < 0.001, 0.44) and p = 0.028 and 0.0072 in Figure 6D.
- **Criteria:** all 20 have one. Three are claims of absence judged on the paper's own test: no rate effect at the centre, 900 ns not significantly higher, and no burst effect on the FWHM in CHO cells.
- **Coverage:** heating (Fig. 2); centre enhancement and off-target suppression (Fig. 3); Lorentzian fit and tail deviation; the 40-fold ratio; FWHM against packet rate and the log trend (Fig. 4); 3D experiments, YP against Pr spot size, the fit R² values and nuclear staining (Fig. 5); pulse duration (Fig. 6); burst number in both cell lines and the sharpest peak (Fig. 7).
- **Method details fixed from the paper (F1 to F10):** ROI size, background subtraction, pooling, the Lorentzian and Gaussian formulas, fit ranges, t-tests with Bonferroni, and percent of the 15.3 mm diagonal. For claims the paper states without a test, I used its own rule: a gap between error bars longer than the bars means p < 0.05.

**Details left open, with the readings named:**
- **O1, ROI positions:** ROIs at whole-mm distances, or contiguous ROIs. Which ROI side lies along the diagonal is a standard choice.
- **O2, "pooled" diagonals:** two diagonals averaged at each signed position, or all four half-diagonals averaged by distance. Figures 3B and 4A word this differently.
- **O3, fit range for FWHM in single experiments:** ±4 or ±5 mm for Figure 6D; ±4, ±5 or ±6 mm for Figure 7 (the Methods say "4–6 mm").
- **O4, what the regressions fit:** values from single experiments, or group means (Figures 6D and 7).
- **O5, "near electrodes" for the ratios:** 6 mm or 7 mm.
- **Figure 6D trend:** the text says "logarithmic fit" and the legend says "best linear fit"; both are run.
- **Figure 6D p-values:** which of 600 or 900 ns has p = 0.028 and which 0.0072 is not said.
- **Figure 6C normalization:** each experiment normalized, or the mean profile.
- **Figure 7C:** whether the CT26 6-burst point enters the FWHM fit.
- **Figure 3C "perimeter":** the outermost parallel ROIs, or all parallel ROIs at 4 mm or more.
- **Tail deviation:** measured in a.u. or in percent of the peak.
- **"Slightly larger" (YP against Pr spot):** a ratio of 1 to 1.25, or 1 to 1.5. The paper gives no bound.
- **Heating colours:** two sets of hue limits, as the paper gives none.
- **Figure 5C zones and the cytoplasm ring:** two ring widths. The zone positions are shown only in the figure.

**Missing from the paper:**
- The packet rates and burst numbers tested and the measured distances are only in the figures, which I could not see.
- How "2.3% of the electrode array area" was computed is not given, so that number is not tested.
- The Figure 4A legend cites "Fig. 2" for its data, which looks like a typo for Fig. 3.
- No code or data repository is linked.
