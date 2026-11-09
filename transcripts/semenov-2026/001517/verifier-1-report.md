**Verifier report, round 1: Semenov et al. 2026 on DANDI:001517 (0.261006.1856)**

The claims file has 31 claims. The notebook tests 16 and marks 15 blocked for data_missing.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1-pole-dimming | reproduced | Cell 13: cathodic dF at 780 V/cm is 38.6%, at or below the 41.7% at 570. At 1400 V/cm the cathode-side maximum (22.0%) is at −65°, against 8.3% at the pole. Holds for all three backgrounds; 56/56 five-cell subsets (far background). |
| fig2a-fluovolt-saturation | not_reproduced | Cell 15: cathodic dF at 360 V/cm is 49.4% (far), 78.5% (near) and 23.7% (none), against 66 ± 6.6. Anodic dF at 570 V/cm is in tolerance only with the near background (−88.6), and that reading fails the 1000–1400 condition. |
| fig2a-fluovolt-stable | not_reproduced | Cell 17: with far and with no background, both start/end readings find significant changes (far (a): 1400 V/cm anodic p = 0.043 and a baseline p = 0.005; (b): 2 pulse sets and 4 baselines). The near background splits between the readings, but it is not a cell-free region. The changes are small (problem 5). |
| fig2b-di8-climbs-to-570 | reproduced | Cell 19: mean \|dF\| rises at every step from 43 to 570 V/cm at both poles, under every background, 56/56 subsets. |
| fig2b-di8-bleaching | reproduced (fragile) | Cell 21: reading (b), the offset common to both poles, is −5.11 (far) and −5.00 (near), within −5 ± 0.5. Reading (a) fails (anodic −3.39). It also fails with no background (−2.63) or with dark frames kept (−2.18), and only 39/56 five-cell subsets pass (my count from the printed per-cell values). |
| fig2b-di8-decline-within-set | reproduced | Cell 23: with far and with no background, the cathodic end is below the start at every set from 780 to 1400 V/cm under both readings (far (b): 41.1→34.3, 37.0→25.2, 24.2→15.2, 15.6→9.2). The near background fails at 1400 V/cm under reading (a). Bleaching is a confound (problem 4). |
| fig2cd-stable-before-electroporation | blocked (data_missing) | No alternating 150/230 V/cm protocol in the archive (C). |
| fig2c-1000-within-set | blocked (data_missing) | Same reason. |
| fig2d-lasting-reduction | blocked (data_missing) | Same reason. |
| fig3-dye-sensitivity | partially_reproduced | Cell 25, pixel 0.267 µm: slopes 21.6 and 7.4 fail, Pearson 0.964 and 0.762 pass. Cell 26, pixel giving the paper's 8-µm mean radius: slopes 26.6 and 9.53, Pearson 0.976 and 0.831, all in tolerance. So the slopes depend on a pixel size the files may not store; the correlations and the slope ratio (2.92 vs the paper's 2.86) match either way. |
| fig3-fluovolt-nonlinear | not_reproduced | Cell 28: under every background and smooth, the Di-8-ANEPPS smooth departs from the line between 150 and 500 mV (smooth/line as low as 0.63–0.84). Cell 29 shows this is a cathodic-side deficit: own-side slope 3.13 vs 11.63 anodic. |
| fig4a-fluovolt-limits | not_reproduced | Cell 32: maxima 49.3 / −72.1 (far) and 23.6 / −40.4 (none) miss both values. Near gives 80.6 (in tolerance) and −89.1 (just outside). With far, measured differs from calculated at 150 V/cm (paired p = 0.037 / 0.0045). |
| fig4a-fluovolt-cathodic-decline | not_reproduced | Cell 34: 360 V/cm is 49.3 (far), outside 71 ± 10. Near gives 78.3, but then 1000/1200/1400 V/cm are 66.6/68.0/80.6, outside 40.5–55. |
| fig4b-di8-limits | not_reproduced | Cell 36: under every background the maxima are not both at 570 V/cm (anodic peak at 780 V/cm, or cathodic at 1200 with near), and neither maximum pair is within tolerance; 0/56 subsets. |
| fig4b-first-10-pulses | not_reproduced | Cell 38: first-10 cathodic maximum is 43.1% (far), 88.5% at 1200 V/cm with s.e. 38 (near), 16.5% (none), against 66 ± 15. |
| fig4b-cathodic-asymmetry | partially_reproduced | Cell 40, far and no background: the decline from 780 V/cm, the larger cathodic loss (0.78 vs 0.55) and a cathodic 1400 V/cm value not different from zero (p = 0.24) all hold. The anodic 1400 V/cm value is −18.5 / −21.7 / −9.4, against −30 ± 3. |
| fig4c-equator-follows-cosine | not_reproduced | Cell 42: some arcs differ under both paired and unpaired tests for every background (far 16/24, near 1/24, none 24/24). The 8-µm variant also has differing arcs (7 paired, 9 unpaired). |
| fig4d-short-pulses-same-limit | blocked (data_missing) | Every file is a 1-µs pulse (C). |
| fig5a-gd-extends-anodic | blocked (data_missing) | No Gd3+ recordings (C). |
| fig5a-gd-linear | blocked (data_missing) | Same reason. |
| fig5a-gd-cathodic | blocked (data_missing) | Same reason. |
| fig5a-gd-differences | blocked (data_missing) | Same reason. |
| fig5b-conductivity-calibration | partially_reproduced | Cell 44: a 100-fold rise gives 11.87% / 11.75%, in tolerance; a 10-fold rise gives 1.33% / 1.20%, against 2 ± 0.2. I checked Eq. (2) in `f_factor` against the paper's text and recomputed 1.33% and 11.87%. The claims file already flags this. |
| fig5c-gd-reduces-conductivity | blocked (data_missing) | Needs the Gd3+ data. |
| fig6a-ca-single-pulse | blocked (data_missing) | No Fluo-4 / Ca2+ imaging (C). |
| fig6b-ca-train-responders | blocked (data_missing) | Same reason. |
| fig6b-ca-650 | blocked (data_missing) | Same reason. |
| fig7b-charging-during-pulse | reproduced (depends on the volts mapping) | Cell 46, far: every reading passes (cathodic per cell: 1.465 at 570, 2.153 at 780, >2 above, max p 0.001); 43/56 subsets. But the result depends entirely on matching volts to V/cm in order (problem 1). |
| fig7ab-test-pulse-recovery | blocked (data_missing) | Every file is a single pulse (C). |
| fig7c-fast-conductivity-drop | blocked (data_missing) | Same reason. |
| fig7c-full-reseal-mild | blocked (data_missing) | Same reason. |

### B. Problems

1. **[affects a conclusion]** Volts to V/cm (`strobe.VOLT_TO_VCM`, cell 8). The files give volts (25–350 V); the notebook matches them in order to the paper's nine field strengths and never runs the other reading, field proportional to volts. Its own check (cell 8) says the volts fit as well or better. The paper says current scales linearly with voltage, which argues for proportionality; the files also give a 1.0-mm electrode gap against the paper's 1.6 mm.
   - The evidence is mixed. The FluoVolt dF ratio from 25 to 50 V is 3.05, closer to the paper's 3.49 than to 2.0. The R² comparison is distorted by FluoVolt saturating.
   - With field proportional to volts, the fig7b line at the 150-V step is 300% instead of 380%. The ratio then becomes 1.15–1.27 (my computation from cell 46's numbers), which fails 1.5 ± 0.15.
   - The same assumption sets IMPC in fig3, fig4a, fig4b and fig4c.
2. **[affects a conclusion]** Pixel size (`UM_PER_PIXEL`). The adopted 16/60 µm gives a mean radius of 11.1 µm (cell 5), against the paper's ~8 µm. The fig3 slopes pass only under the 8-µm variant (cell 26). That variant is not run for fig3-fluovolt-nonlinear (which depends on fig3) or for the measured-vs-calculated tests in fig4a and fig4b.
3. **[affects a conclusion]** Background distance (`BG_OFFSETS`). The author chose 30–36 px. The near and far readings bracket the paper's magnitudes: FluoVolt cathodic dF at 360 V/cm 49 vs 78 (paper 66); Di-8-ANEPPS cathodic maximum 41.7 vs 71.3 (paper 57); first-10 dF at 570 V/cm 43 vs 69 (paper 66). The not_reproduced outcomes of fig2a-saturation, fig4a, fig4a-decline, fig4b-limits and fig4b-first-10 therefore rest on a distance the paper does not give. The far reading is the reasonable reading of "cell-free", but no sweep over distance is shown.
4. **[does not affect a conclusion]** fig2b-di8-decline-within-set (cell 23): a bleaching drift of about −5% per set (cell 21) by itself shrinks cathodic \|dF\| over a set. The decline at 780 V/cm (4–7 points) is about that size. There is no control from the sets at 43–570 V/cm.
5. **[does not affect a conclusion; issue in the claims file]** fig2a-fluovolt-stable: the criterion counts any significant result among 24 tests with n = 4, which has a family-wise false-positive rate near 70%. The notebook applies it as written. The significant changes are small (−0.5 to −13%, mostly under 5%), and some are increases (cathodic +8.0 at 1200 V/cm).
6. **[does not affect a conclusion]** Di-8-ANEPPS claims use all 8 cells where the paper has n = 5. Subset shares are given for most claims but not for fig2b-di8-bleaching (39/56 by my count) or fig4c.
7. **[does not affect a conclusion]** `measured_vs_calc` / `pole_impc` use only the perimeter radius; the claims file's equal-area radius reading is not run for fig4a and fig4b. Both claims fail on their maxima anyway.
8. **[does not affect a conclusion]** `_bg` averages the background ROIs at the two poles into one value per frame. Reference [20]'s "ROIs near the poles" could mean subtracting each pole's own background. The "none" reading leaves in the camera offset (floor 177 of a ~280 frame mean), which roughly halves dF. That is a legitimate reading of "no subtraction", but it is not a physical estimate.
9. **Helper functions pass synthetic tests.** On a synthetic cell with a known cosine modulation (±30%) and a constant offset, `find_cell`, `membrane_line`, `field_angle`, `collapsed_df`, `per_image_pole_df` and `pole_values` recover the centre, radius, axis and pole dF exactly. `impc_profile` matches Eq. (1) by hand. Units are correct (V/cm ×100 → V/m, µm → m, V → mV).
10. **Blocked claims confirmed in the archive.** All 220 session descriptions give a single 1-µs pulse, the standard solution with no Gd3+, and FluoVolt or Di-8-ANEPPS only; there is no Fluo-4 and no two-pulse or 0.3-µs protocol.
    - Two 2025-01-22 cells come closest to a protocol: c2 has repeated sets (50 ×3, 75 ×3 V), and c3 has low-amplitude sets after 200 V.
    - At most these give a one-cell description. They are not the alternation, the 1000-V/cm step or the n = 8 of fig2c/fig2d, and that day's escalation has no mapping to the paper's field strengths.
    - So no blocked claim is testable as specified.

### C. What I could not check, and the output that would settle it

- **Pixel size.** Whether the NWB files really hold no pixel size: the notebook never prints the ImagingPlane, Device or field-of-view metadata. A dump of the NWB object tree would settle the radius question.
- **Volts mapping.** Whether volts map to V/cm in order. Needed: the fig3, fig4 and fig7b results re-run with field proportional to volts, plus per-step dF ratios for FluoVolt below saturation.
- **Background sensitivity.** Needed: pole dF as a function of the background-ROI distance (8–40 px) for the magnitude claims.
- **Cell outline.** How well the automatic outline matches the membrane, especially Di-8-ANEPPS c7 at 300/350 V. Needed: overlay images of the traced outline per cell.
- **Bleaching control.** Needed: the cathodic start and end for Di-8-ANEPPS sets at 43–570 V/cm in cell 23.
- **8-µm variant.** Needed: fig3-fluovolt-nonlinear and the fig4a/fig4b measured-vs-calculated tests under that pixel size.
- **Which five cells.** The paper's n = 5 Di-8-ANEPPS cells are not identified in the paper or the archive, so no output in the notebook can settle this.
