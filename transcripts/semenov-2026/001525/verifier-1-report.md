**Verifier report, round 1: Semenov et al. 2026 on DANDI:001525 (version 0.261006.1856)**

The claims file has 27 claims. The notebook tests 4 and treats 23 as blocked.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig7a-test-pulse-cosine-up-to-1000 | partially_reproduced | The cosine part holds under reading (b): with the unpaired test, no strength up to 1000 V/cm differs from control (cell 9, every pole). At 1400 V/cm charging is lower than control at every pole (p = 0.018, 0.016, 0.006). At 1200 V/cm it is not significantly lower (p = 0.19 / 0.15 / 0.067). The whole claim holds in only 1 of 18 variants (without c5, mean pole; cell 11). |
| fig7b-test-pulse-unchanged-to-760 | reproduced | With the paper's unpaired test, no strength up to 1000 V/cm differs from control in 18 of 18 variants (cell 14). After 1000 V/cm the test response is 80.0 / 85.6 / 84.0% of control (cathodic / anodic / mean), all within 80 ± 8 (cell 13). This is a claim of absence with low power: the cathodic pole is at 133% after 360 V/cm and 153% after 570 V/cm, and the paired variant gives p = 0.004 at 360 V/cm. |
| fig7b-test-pulse-reduced-1200-1400 | not_reproduced | No pole reading gives p < 0.05 at 1200 V/cm (main reading 0.19 / 0.15 / 0.067), so the claim fails in 18 of 18 variants (cell 17). The anodic values, 73.3% and 50.1%, are within tolerance, but at 1200 V/cm the anodic p is 0.146. |
| fig5b-conductivity-calibration | partially_reproduced | Eq. (2) gives an 11.87% IMP reduction for a 100-fold rise, within 12 ± 1.2. For a 10-fold rise it gives 1.33% (1.20% relative to intact f), outside 2 ± 0.5 (cell 19). |
| fig7c-full-reseal-mild-residual-strong | partially_reproduced (the notebook says blocked) | The reseal and residual parts need only test-pulse data, which is in the dataset. Reseal: 570 and 760 V/cm do not differ from control (unpaired p ≥ 0.17, cell 13). Residual: test dF is below 100% at 1000, 1200 and 1400 V/cm at both poles. The criterion counts those two parts as a partial reproduction. The "cathodic more conductive during the pulse" part needs Fig. 4B data, which is missing. |
| fig7b-conditioning-pulse-below-linear | blocked: data_missing | The only single-pulse files are 50 V (150 V/cm); there is no 360–1400 V/cm single-pulse series. |
| fig7c-conductivity-drops-10-fold | blocked: data_missing | It needs conditioning-pulse lm,eff, which comes from the missing Fig. 4B data. |
| fig1-poles-leaky-equator-intact | blocked: data_missing | No escalating single-pulse sets in the dataset. |
| fig2a-fluovolt-saturation | blocked: data_missing | All 73 files use Di-8-ANEPPS; there is no FluoVolt data. |
| fig2a-fluovolt-stable-within-set | blocked: data_missing | No FluoVolt data. |
| fig2b-di8-climbs-then-declines-in-set | blocked: data_missing | No escalating sets from 43 to 1400 V/cm. |
| fig2cd-stable-at-150-230 | blocked: data_missing | No alternating 150 / 230 V/cm sets. |
| fig2c-within-set-decline-1000 | blocked: data_missing | No 1000 V/cm single-pulse sets. |
| fig2d-lasting-drop-after-1000 | blocked: data_missing | Same as fig2cd. |
| fig3-dye-calibration-slopes | blocked: data_missing | No FluoVolt data, and only one strength (150 V/cm) of the 43–360 V/cm range (see D). |
| fig3-fluovolt-nonlinear-di8-linear | blocked: data_missing | Same as fig3-dye-calibration-slopes. |
| fig4a-fluovolt-limit | blocked: data_missing | No FluoVolt data. |
| fig4b-di8-threshold-570 | blocked: data_missing | No single-pulse escalation. |
| fig4b-first-10-pulses | blocked: data_missing | Same as fig4b-di8-threshold-570. |
| fig4b-cathodic-pole-more-damaged | blocked: data_missing | Same as fig4b-di8-threshold-570. |
| fig4c-equator-follows-cosine | blocked: data_missing | Same as fig4b-di8-threshold-570. |
| fig4d-short-pulses-same-limit | blocked: data_missing | No 0.3-µs pulses. |
| fig5a-gd-extends-anodic-charging | blocked: data_missing | No Gd3+ group. |
| fig5a-gd-cathodic-no-higher-but-no-decline | blocked: data_missing | No Gd3+ group. |
| fig5c-gd-reduces-conductivity | blocked: data_missing | No Gd3+ group. |
| fig6a-ca-single-pulse | blocked: data_missing | No Fluo-4 data. |
| fig6b-ca-train-thresholds | blocked: data_missing | No Fluo-4 data. |

## B. Problems

1. **[affects a conclusion]** Cell 0 table: fig7c-full-reseal-mild-residual-strong is blocked "because it depends on the claim above". But its reseal and residual parts use only test-pulse data, and cells 13–14 already contain the numbers. Under the criterion those two parts give partially_reproduced. The "no pole difference at the test pulse" part could also be tested (paired cathodic vs anodic normalized test dF) but was not run.

2. **[does not affect a conclusion]** Cells 5, 7 and 9, `cosine_fit`: in the main reading the control profile has a mean dF of −4.6%. The source (bleaching or drift) is never identified, and no baseline trend is shown. Effects:
   - The control pole values are asymmetric: cathodic 6.2, anodic −16.5. In a synthetic test, 10·cos − 4 gives poles of +6 / −14, so an offset of this size explains it.
   - Because the criterion fits A cos(θ−φ) with no offset term, fig7a reading (a) fails even for the 150 V/cm control itself (residual −4.71 vs s.e. 2.75). Reading (a) therefore cannot discriminate between strengths.
   - The cathodic and anodic percent-of-control values are biased in opposite directions. The mean-of-poles reading cancels the offset.
   
   The paper reports about ±5% Di-8 bleaching (Results 3.2) and a negative cathodic value at 1400 V/cm, so the offset is plausibly in the paper's data too. None of my outcomes changes because of it.

3. **[does not affect a conclusion]** `STRENGTH_V_CM`: conditioning voltages are mapped to V/cm by rank, which is plausible because the dataset has 7 levels and Fig. 7A has 7 panels. But the file metadata printed in cell 2 contradicts it and is never discussed:
   - The files list strengths of 0.15, 0.52, 0.9, 1.27 and 1.57 kV/cm. Fitted linearly to the voltages, these put 350 V near 1.27 kV/cm, not 1400 V/cm.
   - The files give an electrode gap of 1.00 mm; the paper (Methods 2.2) gives 1.6 mm.

4. **[does not affect a conclusion]** `profiles_by_level`: the control is the single 50 V pulse, not the 150/150 pair that the Fig. 7A legend and the claims file name. No 50/50 pair file exists. This substitution is stated only in a helper comment, not in the notebook.

5. **[does not affect a conclusion]** Cells 5–6: the main reading (annulus background, dark frames dropped) was chosen because it matches the paper's dF scale. It is stated as an assumption, and all four readings are carried through; outcomes do not change across them (absence holds in 18/18 variants for fig7b-unchanged; fig7b-reduced fails in 18/18).

6. **[does not affect a conclusion]** `field_angle`: the field direction is estimated from the same profiles that are then tested, including the 1200 and 1400 V/cm profiles, which are not cosine-shaped (R² 0.04 and −0.63). The per-file phase s.d. is 6.6°, comparable to the ±5° pole arcs. This is minor.

7. **[does not affect a conclusion, under the current criterion text]** The claims file contradicts itself. Its check log says that if the paired and unpaired tests disagree, fig7b-unchanged becomes methods_underspecified; the criterion text makes unpaired decisive. The notebook cites an amendment (questions/001525.yaml) that I do not have. Under the logged rule, fig7b-unchanged would be methods_underspecified: the paired test finds a difference in 16 of 18 variants.

8. **[does not affect a conclusion]** Cell 11 reports reading (a) only combined with "hindered", so cosine-by-reading-(a) is not visible per variant.

**Synthetic tests:** I tested the helpers on synthetic images. `find_cells`, `trace` and `sample_trace` recovered the centre, radius (34.8 vs 35 px), phase (40.0°) and background (200) exactly. `rotate_to_field`, `pole_means` and `cosine_fit` behave as documented. `f_factor(0)` = 1.5.

## C. What I could not check

- **Whether the analysed cell and trace are right.** No per-subject image with the chosen object and trace overlaid is shown. c5's cathodic dF is negative at every strength, including the control, which suggests a trace or angle problem for that cell. Adding the overlays, plus each cell's own cosine phase and amplitude, would settle this.
- **When each single-pulse control was recorded.** For every subject, especially c5 and c6 with two single-pulse files, the order of single vs conditioning files is not printed. If a control was recorded after the 1400 V/cm set, it comes from a damaged cell.
- **Where the offset comes from.** A baseline dF trend per file (frames 1–39) and the profile mean per strength would identify it.
- **Eq. (2) in the PDF.** The notebook says the equation on page 3 matches the claims file's reading. I had no PDF renderer, so I could not confirm it.
- **The questions/001525.yaml amendment** cited for the unpaired test is not among my materials.

## D. Blocked claims, checked against the archive

The DANDI API for version 0.261006.1856 lists 73 assets: 10 subjects, all named `_image.nwb`, total 2.51 GB. The dataset is described as membrane recovery after 1-µs pulses. The notebook's metadata shows every file is Di-8-ANEPPS, holding either a single 50 V pulse or a conditioning pulse of 100–350 V followed by a 50 V test pulse at 1 or 5 µs. There is no FluoVolt, Fluo-4, Gd3+, 0.3-µs, escalating single-pulse or alternating 150/230 V/cm data, so data_missing is correct for 22 of the 23 blocked claims.

Two exceptions:
- **fig7c-full-reseal-mild-residual-strong** is partly testable, as in A and B1.
- **fig3-dye-calibration-slopes**: a Di-8-ANEPPS slope at 150 V/cm alone could be estimated from the single-pulse files of all 10 cells. That would need the outside tau fit, a pixel size, and the field mapping. It still falls short of the criterion, which requires 43–360 V/cm and FluoVolt.
