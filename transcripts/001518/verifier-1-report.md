**A. Outcomes (30 claims in the claims file)**

| Claim | My outcome | Reason |
|---|---|---|
| fig1-pole-dimming | not_reproduced | Under `top`, condition 1 fails in all 6 readings: cathodic dF is higher at 780 than at 570 V/cm (e.g. 18.1 vs 13.0%, cell 50). Under `bottom` there is no 570 V/cm set. Di-8 cathodic dF rises through 90 to 250 V, so condition 1 also fails for any factor that puts 570 and 780 V/cm inside the data. |
| fig2a-fluovolt-saturation | not_reproduced | No set under any reading comes near the paper's values. The largest FluoVolt cathodic mean over all 19 sets is 36.1%, against 66 ± 6.6, and the most negative anodic is −49.5%, against −83 ± 8.3 (cell 28). This holds for every volts-to-V/cm factor. |
| fig2a-fluovolt-stable | not_reproduced | The baseline shows significant start-to-end changes in 4 to 9 of 38 tests in every reading (cell 30), e.g. 150 V/cm cathodic −2.6%, p = 0.010 (cell 31). The pulse sets at 1000 V/cm and above exist only under `top`. There, 0 of 6 tests are significant on experiment means and 1 of 6 on centre-cell and all-cells means, with changes of 4.4% or less. |
| fig2b-di8-climbs-to-570 | partially_reproduced | Under both factors, \|dF\| rises at every step on experiment and all-cells means (cell 38). It fails for the centre cell, which is the closest reading to the paper's one cell per experiment. The 570 V/cm level exists only under `top`, and 43 V/cm exists only under `bottom`. |
| fig2b-di8-decline-within-set | reproduced (only if the factor is `top`-like) | Under `top` the cathodic end is below the start in every set from 780 V/cm, under both start/end readings (cell 40, reading c). The anodic pole does not decline, so reading (d) fails. Most of the cathodic drop is a drift shared by both poles (problem 6). Under `bottom` the claim cannot be tested. |
| fig2cd-stable-before-electroporation | blocked: data_missing | Every subject is one rising escalation with each voltage once (cell 5), so there is no alternation protocol. I confirmed this from the archive's session descriptions. |
| fig2c-1000-within-set | blocked: data_missing | Same as above. |
| fig2d-lasting-reduction | blocked: data_missing | Same as above. |
| fig3-dye-sensitivity | blocked: metadata_insufficient | The slope scales directly with the volts-to-V/cm factor. That factor is not recorded, and the adopted value was chosen by matching these same slopes (cells 15 and 16), so the test is circular. Correlation coefficients are within tolerance under `bottom` (FluoVolt 0.90 to 0.91, Di-8 0.80 to 0.82, cell 21). Even with the fitted factor, no reading meets both slopes (0 of 32). Under physically plausible factors the slopes would be 3 to 4 times too low. |
| fig3-fluovolt-nonlinear | not_reproduced | The Di-8 smooth departs from the line under all four smooths and both factors, for example at 83 to 86% of the line at +150 to +300 mV (cells 24 and 25). The FluoVolt departure condition holds under `bottom` only. |
| fig4a-fluovolt-limits | not_reproduced | The maxima are 31.7 to 35.9% and −48.8 to −51.1% in every reading, against 71 ± 10 and −83.5 ± 5 (cell 33). This holds for any factor. The 43/150 V/cm match also fails. |
| fig4a-fluovolt-cathodic-decline | not_reproduced | No set reaches 61% cathodic under any factor. The value at 360 V/cm is 20 to 28% (cell 35). |
| fig4b-di8-limits | not_reproduced | The largest Di-8 means over all 19 sets are 24.3% and −29.2%, against 57 ± 14 and −55 ± 4 (cell 42). This holds for every factor that includes 570 V/cm. Measured IMP is also already below IMPC at 43 to 360 V/cm. |
| fig4b-first-10-pulses | not_reproduced | The largest first-10 mean is 27.0%, against 66 ± 15 (cell 44), under any factor. |
| fig4b-cathodic-asymmetry | not_reproduced (only if the factor is `top`-like) | Under `top`, cathodic dF rises from 780 to 1400 V/cm (18.1 to 24.3%) and is non-zero at 1400 V/cm (p < 0.001, cell 46). Only the anodic −29.2% meets its target. |
| fig4c-equator-follows-cosine | not_reproduced (only if the factor is `top`-like) | 9 to 12 of 12 arcs differ in every reading. Some differences do not depend on the factor: the cathode-side arcs near 90° read about zero or negative where IMPC is positive (cell 48). |
| fig4d-short-pulses-same-limit | blocked: data_missing | No 0.3-µs pulses. All 190 session descriptions say "single 1 µs" pulse. |
| fig5a-gd-extends-anodic | blocked: data_missing | No Gd3+ in any session description. |
| fig5a-gd-linear | blocked: data_missing | Same as above. |
| fig5a-gd-cathodic | blocked: data_missing | Same as above. |
| fig5a-gd-differences | blocked: data_missing | Same as above. |
| fig5b-conductivity-calibration | partially_reproduced | `f_factor` matches Eq. (2) as printed. A 100-fold rise gives 11.87% or 11.75%, within 12 ± 1.2. A 10-fold rise gives 1.33% or 1.20%, against 2 ± 0.2 (cell 54). |
| fig5c-gd-reduces-conductivity | blocked: data_missing | Needs the Gd3+ data. |
| fig6a-ca-single-pulse | blocked: data_missing | No Fluo-4 or Ca2+ data in any asset. |
| fig6b-ca-train-responders | blocked: data_missing | Same as above. |
| fig6b-ca-650 | blocked: data_missing | Same as above. |
| fig7b-charging-during-pulse | not_reproduced (only if the factor is `top`-like) | Best reading (anodic pole, experiment means, cell 52): 1.46 at 560 V/cm passes, 1.62 at 780 V/cm fails against 2 ± 0.2, and 1000 to 1200 V/cm ratios are 1.72 to 1.77, not above 2. |
| fig7ab-test-pulse-recovery | blocked: data_missing | No two-pulse protocol in any asset. |
| fig7c-fast-conductivity-drop | blocked: data_missing | Same as above. |
| fig7c-full-reseal-mild | blocked: data_missing | Same as above. |

**B. Problems**

1. [affects a conclusion] Cells 15–16 and `pef.FIELD_PER_VOLT`: the adopted `bottom` factor (1.72 V/cm per V) is a poor assumption, for two reasons.
   - It is circular. It was picked because it reproduces the paper's dye sensitivities, which is the quantity fig3-dye-sensitivity tests.
   - It does not fit the electrode geometry. I modelled two 0.5-mm rods as line charges: the field at the midpoint is about 4.6 to 7.2 V/cm per V for the paper's 1.6-mm spacing, and 8 to 17.5 V/cm per V for the files' 1.00 mm. Both are 3 to 10 times above 1.72. The `top` factor (5.6) falls within the paper's range.
2. [affects a conclusion] Cells 0 and 36 mark eight Di-8 claims as "blocked: data missing" because of the adopted factor. The sets exist; what is missing is the V/cm factor, so the reason would be metadata_insufficient. Under any physically plausible factor, the sets do reach 570 to 1400 V/cm, and the `top` results the notebook already prints are the ones to judge. They fail except for fig2b-climbs (on cell means) and fig2b-decline (cathodic pole).
3. [affects a conclusion] Cell 0 says the tested outcomes "rest on" the factor. For fig2a-fluovolt-saturation, fig4a-fluovolt-limits, fig4a-fluovolt-cathodic-decline, fig4b-di8-limits and fig4b-first-10-pulses they do not: the largest dF anywhere in the data (FluoVolt 36% / −51%, Di-8 24% / −29%) is about half the paper's under every factor. The notebook never checks whether its automated trace underestimates dF, which would explain a uniform shortfall (see C).
4. [affects a conclusion] Cells 24–25: the Di-8 departure on the positive side comes from a uniform offset of about −4% at 25 V (cell 15), since the fit is forced through the origin. Whether the paper removed this bleaching offset is not stated. The fig3-fluovolt-nonlinear outcome depends on this unexamined choice.
5. [does not affect a conclusion] Cell 30: the baseline tests are 38 uncorrected tests per reading. About 2 false positives are expected; 4 to 9 are significant, and almost all changes are negative (consistent with real slow bleaching) and 3.3% or less. The criterion counts any significant test, so the outcome stands.
6. [does not affect a conclusion] Cell 40: in the within-set Di-8 decline, the cathodic pole falls while the anodic |dF| rises. At 780 V/cm, `top`, readings b and experiment: the shared offset of both poles drops about 1.9%, while the polarization amplitude drops about 0.8%. No low-field set was run as a control for drift. The criterion is met anyway.
7. [does not affect a conclusion] `load_set` and `dF_profile`: background reading (b) subtracts the cell-free median (about 330 counts), which sits about 120 counts above the camera offset seen in dark frames (about 208). A reading that subtracts only the camera offset was not run. It would give dF between readings (a) and (b), so it cannot rescue the magnitudes.
8. [does not affect a conclusion] `responding` selects cells using their own response. Only 3 of 43 tracked cells are dropped. The "experiment" reading averages 1 to 5 cells per experiment against the paper's one cell, and the data have 5 FluoVolt experiments against the paper's n = 4. Per-experiment FluoVolt values stay below 42%, so no verdict changes.
9. [does not affect a conclusion] Cell 52: in the per-cell normalization (reading a) for the mean-pole reading, the 150 V/cm values are near zero, so the ratios become meaningless (−10.7, 16.9).
10. [does not affect a conclusion] Cell 0 still contains an outcome table "from the attempt record". I did not use it.
11. Checked and correct:
    - Eq. (1) and Eq. (2).
    - `arc`, `cos_phase`, `dF_profile` and `good_frames` on a synthetic polarized ring cell: the phase is recovered at 100.0°.
    - Per-image and collapsed pole dF are identical by construction, and the code respects that.
    - The 40/60 image boundary (cell 13).
    - No duplicate recordings (cell 11).

**C. What I could not check**

- Whether the automated membrane trace and cell detection (`find_cells`, `trace`) reach the paper's dF magnitudes. This would need, per experiment, a baseline image with the trace overlaid and one cell's raw F0 and F profiles at the highest set.
- How every outcome changes across the factor. A table of each criterion's result over a sweep of about 1.5 to 8 V/cm per V would show directly which outcomes do not depend on it. Only two factors were run.
- The Di-8 and FluoVolt pole values at all 19 sets as numbers. They appear only in the cell 18 plot. I relied on the plot and the level tables to say they rise monotonically.
- Within-set drift in the low-voltage sets, as a control for fig2b-di8-decline-within-set.
- Whether reference [20] gives the volts-to-V/cm factor or a pixel size. I was not given it, and the archive records neither. The NWB files hold only the voltage, a 1.00-mm electrode distance (the paper says 1.6 mm) and no pixel size or field direction.
