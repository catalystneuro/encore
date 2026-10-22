**A. Outcomes** (all 33 claims in the claims file: 13 reproduced, 3 partially reproduced, 7 not reproduced, 10 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| early-lick-fraction | reproduced | Cell 14: 13.24% (mean over planes, all trials), and every reading falls within 13.3 ± 10. |
| imaging-sample | partially_reproduced | Cell 16: 6 mice, 105 planes, 92.15 trials per plane, 73.83% correct and 3.09 planes per session (range 1–6) all match. The files have no location identifier: the subject × area stand-in gives 10 locations against 12 expected, so locations and planes per location are blocked (metadata_insufficient). |
| trials-per-type | reproduced | Cell 18: CR 34.06, CL 35.51, ER 12.18, EL 10.40; all within tolerance. |
| neuron-counts | reproduced | Cell 20: 15,431 total, 8,837 ALM and 6,594 MM, exact under reading A1. |
| fraction-selective-alm-mm | not_reproduced | Cell 22: no reading meets the criterion. The closest (T1/R2/W1) has ALM in tolerance (2,877, 32.6%) but MM too high (1,755 > 1,675; 26.6% > 25.3%). The permuted null under R2 is already about 11%. |
| figs5-single-coefficient | reproduced (on the criterion only) | Cell 24: pure/selective is above 0.5 in 59 of 59 bins (0.845–0.928). On synthetic null data I get about 0.93 for the same ratio, so the measure cannot tell the result from chance (problem 2). |
| fig4a-lick-direction-epochs | reproduced | Cell 26: 4,125 delay, 3,611 first after the go cue, 4,426 more than 2 s after it; all above the permuted null (3,273 / 2,526 / 3,196). The last-lick reading is report-only and was not done. |
| fig4b-object-location-memory | reproduced | Cell 28: 2,148 / 2,487 / 1,149, all above the null (1,694 / 1,719 / 707). |
| fig4c-outcome-after-lick | not_reproduced | Cell 30: only 0.413 (T1) and 0.418 (T2) of purely outcome-selective ROIs have their first selective bin after the go cue; the criterion needs more than half. Both gamma signs occur. The 0.785 from two consecutive bins is the author's variant, not in the criterion. |
| fig5-mixed-response-epoch | reproduced | Cell 32: 0.765 (T1) and 0.776 (T2) of mixed ROI-bins fall after the go cue; null 0.523. |
| fig6-object-location-mm | reproduced | Cell 34: MM above ALM in 27/31 bins (to 2.2 s) and 34/38 (to 2.7 s); T2 similar. |
| fig6-lick-direction-deep-alm-first | blocked (metadata_insufficient) | No plane depth in the asset metadata (checked on the API) or among the ImagingPlane fields the notebook lists. The text of ImagingPlane.description was never printed. |
| fig6-lick-direction-spread | partially_reproduced | Cell 36: (a) holds (ALM fraction peaks at 4.44 s, mean \|β\| at 4.66 s) and (c) holds (MM max 0.0256, above its delay mean and delay max, below the ALM max 0.0618). (b) needs depth and is blocked. |
| fig6-outcome-response-uniform | not_reproduced | Cell 38: (a) fails for MM (pre-go max 0.0112 is not below 0.0268/3 = 0.0089; T2 likewise). (b) passes (ratio 1.457). The MM pre-go value is at the null level (0.0067–0.0105), which hints the criterion ignores chance (problem 3). |
| fig6h-preparatory-alm-object-mm | reproduced | Cell 40: ALM above MM on both lick-direction measures in 24/42 delay bins (T2 30/45); MM above ALM on both object measures in 52/59 bins. The \|β\| part is narrow (24/42). |
| figs9-photoinhibition-alm-mm | blocked (data_missing) | The archive holds 210 two-photon NWB files only. |
| widefield-mm-to-alm | blocked (data_missing) | Same: no wide-field imaging; the only image is a 2P reference ("GCaMP at 940nm"). |
| widefield-contralateral-bilateral | blocked (data_missing) | As above. |
| figs4-peak-shift | not_reproduced (reading-dependent) | Cell 42: over the whole −0.8 to 9.2 s window MM peaks after ALM (6.09 vs 4.52 s, V1); 0 of 8 combinations pass. Peak taken before the go cue (V2 variant): MM 1.51 s, ALM 4.09 s. That would pass, but the criterion does not set the peak window and the V1 version was not run (problem 4). |
| fig8c-pt-deep-only | partially_reproduced | Cell 44: PT 719 and IT 2,631, exact, in 3 mice. The depth conditions are blocked (no depth). |
| fig8d-alm-deep-lick-direction | blocked (metadata_insufficient) | Needs depth. |
| fig8d-pt-contra-bias | not_reproduced | Cell 46: mean β over the delay is 0.0284, 1.71 bootstrap SD (needs >2). T2 gives 1.56; V2 gives 1.97 and 1.86. |
| fig8d-pt-earlier-than-it | reproduced (fragile) | Cell 48: T2/S2/H2 with O1 (1.80 s, p = 0.003) or O2 (1.40 s, p = 0.006) passes, and PT max 0.231 > IT max 0.085. The other 14 of 16 combinations fail p < 0.01, including every hierarchical (H1) and every T1 one. Reading I1 was not run. |
| ephys-pt-it-onset-not-detected | reproduced (weak) | Cell 59: 0 of 8 combinations find PT earlier at p < 0.01. The baseline is two windows (O1 = O2), so the test carries little information (problem 5). |
| li2015-tagged-units-link | reproduced | Cell 56: exactly 45 PT and 27 IT units in DANDI:000010. |
| fig8d-mm-object-location | blocked (metadata_insufficient), partly testable | Needs depth for most groups. Part (a) for PT (MM PT against ALM PT; PT are deep by the paper) could have been run (problem 6). |
| fig8d-mm-posterior-preferring | not_reproduced | Cell 50: 1.87 SD (T1) and 1.94 SD (T2); needs >2. All 5 mice are positive. |
| fig8d-error-outnumber-correct | not_reproduced | Cell 52: (a) holds (2,825 against 2,004, p = 3e-32). (b) fails under V1 (−1.81 SD; T2 −1.70); only V2/T1 passes (−2.20). The criterion needs both. |
| fig8ef-area-explains-variance | blocked (metadata_insufficient), partly testable | Area against projection type needs no depth and was not computed. If area < projection type, the claim fails whatever depth shows (problem 6). |
| ephys-selective-counts | blocked (data_missing) | Not in the dandiset. A DANDI search finds no other Chen 2017 dandiset; the paper's CRCNS DOI is said (cell 0) to be a placeholder, which I did not check. |
| fig7d-ephys-area-distribution | blocked (data_missing) | As above. |
| fig1c-whisking-similar | blocked (data_missing) | Cell 7's object list shows only BehavioralEvents under processing/behavior and nothing under stimulus/presentation: no whisker series. |
| alm-pt-it-lick-fraction-below-20 | reproduced | Cell 54: max PT 15.6% and IT 6.0% (β significant; T2 16.1%), below 22%. |

**B. Problems**

1. **Pervasive dF/F outliers** [affects a conclusion] (`dff_trials`; cells 9, 42, 46, 50, 52). With neuropil subtraction, F0 is ≤ 0 on 0.26% of ROI-trials in 1,262 ROIs, and the 99.9th percentile of |dF/F| is 8,829. The V1 MM mean dF/F reaches −1.15 (cell 42). V1 against V2 decides pass or fail in fig8d-error-outnumber-correct (−1.81 against −2.20 SD) and moves figs4-peak-shift's MM peak (6.09 against 4.80 s). V1 follows the claims file; the sensitivity is real.
2. **Chance-level selection measures** [affects a conclusion] (claims file: figs5, fig4a, fig4b, fig4c; cells 24–30). With a single-bin p < 0.01 rule over 140 bins:
   - figs5's pure/selective ratio is about 0.93 under the null (my synthetic test with `anova3` and `classify`), so "reproduced" there carries no information.
   - fig4a and fig4b's existence tests are met by the permuted null.
   - fig4c's "first bin after go" is pulled before the go cue by chance hits (null 0.296).
   - The notebook computed the null but used it nowhere decisive. The paper states no chance level, so there was nothing to compare with.
   This is a weakness of the claims file, reported not corrected.
3. **fig6-outcome-response-uniform (a) has no allowance for chance** [affects a conclusion] (cell 38). The pre-go maximum of a per-bin fraction includes the roughly 1% false-positive floor; the MM pre-go maximum (1.12%) sits at the null maximum (1.05%).
4. **figs4-peak-shift peak window is open** [affects a conclusion] (cell 42). The notebook takes the peak over a window that includes 5 s of response, while the claim concerns "over the course of the delay". Only the V2 pre-go variant was printed; the V1 pre-go peak was not.
5. **Li et al. onset baseline is two windows** [affects a conclusion] (cell 59). The stored span starts −0.524 s from the sample event, so O1 and O2 are the same two windows (centres −0.3 and −0.2 s). The IT baseline SD is 0.0004, so the 6 SD threshold is arbitrary, and the PT S1 onset of 0.1 s falls in the sample epoch. One IT unit (no ER trials) was dropped, leaving 26.
6. **Blocked claims with testable parts not run** [affects a conclusion] (cells 0, 44):
   - fig8ef: variance explained by area against projection type needs no depth.
   - fig8d-mm-object-location (a): MM PT against ALM PT.
   - Depth itself: the text of ImagingPlane.description, session_description and PlaneSegmentation's description was never printed, so "no plane depth" rests on field names alone.
7. **"No lick times" is not shown** [does not affect a conclusion] (cell 7). The object listing stops at three levels, so the children of BehavioralEvents are never listed. Only cell 5's sample, delay and go are read. This matters only for fig4a's report-only last-lick reading.
8. **fig8d-pt-earlier-than-it depends on the choice of combination** [does not affect a conclusion under the criterion's "under one combination" rule]. It passes only with T2, S2 and the over-cells bootstrap. T2's 66.7 ms interpolated bins oversample the 71.7 ms frames (13.95 Hz) and correlate neighbouring bins; T2 also raises R2 counts (cell 22: 45% against 32.6%).
9. **Helper checks passed** [does not affect a conclusion]:
   - `anova3` matches statsmodels' type-3 ANOVA to 5 decimals.
   - Coefficients match the convention M formulas.
   - The null false-positive rate is 1.0% per factor.
   - `onset` S1 and S2, `joint_resample` group integrity, `grid`, and `dff_trials` baseline and alignment all behave correctly on synthetic inputs.
   - The DESIGN codes give α > 0 posterior, β > 0 lick right, γ > 0 correct.

   No train/test split exists, so there is no leakage. Only one permutation was used for the null (seed 0).
10. **Duplicate-file identity was not checked in the run** [does not affect a conclusion] (cell 4). Full identity of the paired files was checked on 2 pairs, outside the run; in the run they are paired on the first 200 frames.

**C. What I could not check**

- **Depth:** whether ImagingPlane.description, session_description or PlaneSegmentation hold plane depth or coordinates. Printing those strings for a few planes would settle whether 4 blocked claims and 2 partial ones are testable.
- **Lick times:** whether BehavioralEvents holds them. Its key list would settle it.
- **figs5 null:** the null pure/selective ratio from `A["T1"]["shuffled"]`, to show the figs5 result is at chance on the real data.
- **figs4 V1 peak:** the V1 peak restricted to before the go cue.
- **Variance explained:** SSB/SST for area against projection type (fig8ef), and MM PT against ALM PT |α| (fig8d-mm-object-location (a)).
- **Locations:** a location identifier (for example from matching reference images), for imaging-sample.
- **Figures:** I did not view the rendered images and relied on the printed ranges.
- **CRCNS:** that the CRCNS DOI is a placeholder. That page is not on the archive API, so I did not check it.
