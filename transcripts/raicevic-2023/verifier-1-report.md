**A. Outcomes** (22 claims in the claims file: the notebook tests 21 and treats 1 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| cross-section-counts | not_reproduced | No combination holds (cell 9). At P1a/P2a/P4b the counts run 390–669, so the most is above 496. At P1b/P2a/P4b the counts (248–415) are in range but the mean spacing is 1.347 µm. P4a leaves 0 sections in 5 segments. |
| segmentation-validation-overlap | blocked: data_missing | I checked the archive API. All three versions (draft, 0.230427.1809, 0.230602.1307) hold 14 NWB files, one 3D z-stack per location, with only TwoPhotonSeries and PlaneSegmentation. There are no 2D time series and no 2D segmentations, so no part can be tested. |
| fig5a-pvs-area-scales-with-vessel-area | not_reproduced | The slope is 1.50–2.72 in all 8 combinations (cell 11). R2 is within tolerance only at P4b (0.149, with intercept), where the slope is 2.22. |
| fig5e-area-ratio-distribution | partially_reproduced | At P1a/P4b/P5a, median 1.718 and IQR 1.831 are within tolerance. The peak (1.546, or 254.6 under P7a) and the 25th percentile (1.046) are not. No combination has all five. |
| fig5bc-area-intersegment-variation | reproduced | Both readings hold in every combination that keeps all 14 segments (P4b), and at P1b/P4a. Only P1a/P4a, with 9 segments, fails reading (b) (cell 15). |
| area-ratio-per-location | not_reproduced | 0 of 128 combinations match. The smallest peak is 0.05–0.79, and at most 10 locations fall within 30% (cell 17). |
| fig5d-polynomial-closest-area-ratio | partially_reproduced | 0 of 96 match. The polynomial share is the largest and above 50% in 92 of 96. The closest combination gives 73.8 / 24.8 / 1.4%, against 73 / 19 / 8%. |
| table2-fit-area-ratio-peaks | partially_reproduced | 0 of 96 match, and at most 6 of 7 values are within tolerance. The partial rule (ellipse > spline > polynomial peaks, spline IQR smallest) is met in 12 of 96 (cell 21). |
| fig6a-resistance-power-law | partially_reproduced | Only P1a/P4a reading (a) meets the partial rule: exponent −1.965, R2 0.941. The other log-log fits give −2.06 to −2.26, and that combination excludes 5 segments entirely (cell 23). |
| fig6b-resistance-segmentation-peak | partially_reproduced | The median, 4.16e15, is within tolerance at P1a/P4b. The peak is never within 1.557–1.903e15; the nearest values are 1.25e15 and 1.94e15 (cell 25). |
| resistance-per-location | not_reproduced | The smallest peak is about 5e13 (location E), the largest is often far above 1.98e16, and the share is 0–50% (cell 27). |
| fig5b-polynomial-closest-resistance | partially_reproduced | The polynomial is the best match in 44–83% of sections, the largest share in every combination. At most 2 of 4 peaks are within tolerance on linear bins (3 with the log variant) (cell 29). |
| ellipse-annulus-underestimate | reproduced (fragile) | Underestimation holds in 16 of 16 combinations. The annulus/ellipse ratios are within tolerance only at P1b/P4a/P5b/P7b (1.831 and 1.675). The peak ratio ranges 0.02–2.25 across combinations (cell 31). |
| spline-resistance-five-times | reproduced (fragile) | The ratio is 5.45 at P1a/P4a/P7b on linear bins (4.94, 4.68 and 5.22 on log bins), and the spline median is above the segmentation median everywhere. Other combinations give 0–4.1 (cell 33). |
| fig7-velocity-profiles | reproduced | All 8 combinations: ellipse faster in ≥99.6% of sections, spline slower in ≥89.5%, polynomial closest in 67–79% (cell 35). |
| vessel-radius-peak | reproduced | The peak is 27.6–30.4 µm in 11 of 24 combinations, with medians of 28–31 µm (cell 37). |
| fig8-ellipse-parameters | not_reproduced | 0 of 72 match, and the partial rule is met in 0. The R3 peak is about 28.8–30 µm against 35 ± 3.5, and R3/R1 and R2/R1 are never both within tolerance (cell 39). |
| fig9c-pvs-two-lobes | reproduced | The HC/R1 peak is within 0.1 of zero and 60–66% of sections with HC > 0 are below 0.5 R1, in 15 of 24 combinations (cell 41). |
| fig9e-pvs-width-asymmetry | not_reproduced | 0 of 24 match, and the WS/WL peak is 0.38–0.63. The medians do match Table 3's medians (WS/R1 1.60–1.71 against 1.60; WS/WL 0.585–0.616 against 0.589), but the criterion tests peaks. |
| left-right-no-difference | blocked: methods_underspecified | Readings (a) and (b) find a difference (p < 1e-15). Reading (c) does not (p 0.25–0.72). The criterion sends a mixed result to methods_underspecified. |
| fig9a-heights-taper | partially_reproduced | No combination puts all three peaks within tolerance. The order H1 > H2 > H3 holds for peaks and medians in many combinations (cell 47). |
| fig9f-pvs-concave | partially_reproduced | 61–72% of values are below 1 in every combination. The peak is never within 0.097–0.119; the nearest are 0.092 and 0.075 (cell 49). |

**B. Problems**

1. **[affects a conclusion]** `centerline`, cells 1 and 9: the longest-path centerline is longer than any straight line through the volume, and this was never checked. Path length is points × spacing in META, e.g. location E is 939 × 0.867 ≈ 814 µm, B ≈ 660 µm and N ≈ 687 µm. The longest straight chord is at most about 480–490 µm (332 × 332 µm field, vessel depth range ≤ 220 µm). On synthetic rough straight cylinders I found only 15–20% excess over the end-to-end distance. So the path most likely runs into branches or doubles back. That would explain:
   - counts above the paper's maximum (669 against 451);
   - slices whose centre misses the vessel (vessel area down to 0.4 µm²; up to 153 slices per segment with no vessel fit, cell 7).
   
   This affects the counts and every distribution.
2. **[affects a conclusion]** `measure_slice`, cells 3 and 7: the slice's PVS is all PVS pixels in the 332 µm plane, not the lobes next to the vessel. Under P4a the median horizontal PVS extent is 240–300 µm. In locations E and F the PVS mask fills 98–99% of the deepest plane and 50–60% of the volume. Cell 4 flags this and says "see below", but nothing follows up. It probably inflates PVS area (up to 40,109 µm²), the area ratios, W and the fig5a slope.
3. **[affects a conclusion]** Robustness of the P4a reading: it keeps 0 cross sections in segments A, B, E, F and G, which is incompatible with the paper's ≥54 per segment. Yet the partial result for fig6a and the reproduced results for ellipse-annulus-underestimate and spline-resistance-five-times each rest on a single P4a combination. The claims file allows P4a, so these outcomes stand by the criterion, but they are fragile.
4. **[does not affect a conclusion]** `cross_sections` / `edge_distance`: slices are centred on the skeleton point and not shifted to the vessel centre, as the Methods do. The edge distance is measured from the skeleton point.
5. **[does not affect a conclusion]** Fit resistances were solved only at erosion 3 (a stated deviation), so P6 is not run for fig5b, ellipse-annulus, spline-five-times or fig7. Missing readings could only add matches, and fig5b's ellipse and annulus peaks are far from tolerance.
6. **[does not affect a conclusion]** Log bins are inconsistent: they count toward spline-five-times (cell 33) but are a "variant" for fig5b and ellipse-annulus (cells 29, 31). The linear-only result for spline-five-times is still 5.45.
7. **[does not affect a conclusion]** Cell 3: location D has an intensity-versus-depth correlation of +0.90, which suggests its z axis may be reversed. The surface-up orientation is assumed for all files, so D's HC, heights and Ov may be flipped.
8. **[does not affect a conclusion]** left-right-no-difference readings (a) and (b) treat 2,000–6,600 autocorrelated slices as independent, so their p-values are not meaningful. Only reading (c) is a sound test, but the criterion fixes the outcome.
9. **[does not affect a conclusion]** fig6a reading (b) (`curve_fit` on the linear scale) is dominated by outliers, with R up to 8e21. It gives exponents from −1.06 to −6.44 and is uninformative.
10. **[does not affect a conclusion]** Overlap pixels are assigned to the vessel (a stated assumption). Location J has 239 slices with more than 5% overlap.

The helper functions behave correctly on synthetic inputs:
- **Circle fit:** recovers the centre and radius to within 0.4 px.
- **Moment ellipse:** returns the semi-axes exactly.
- **`poiseuille`:** gives an ellipse resistance within 1.2% of the exact value for the 1.5 px-eroded domain; two equal lobes halve the resistance.
- **`polynomial_fit`:** returns W, H1–H3 and HC as defined.
- **`optimal_annulus`:** gives 8.70e15 for K = 1.4 and R1 = 23 µm, matching the paper's Discussion.
- **Spline area ratio:** 1.51.

I found no place where the claims file misreads the paper. The paper states no chance level for the fig5d shares.

**C. What I could not check**
- **Centerline geometry:** whether the path follows the main vessel. A per-segment table of path length against end-to-end distance, and a maximum-intensity projection of the vessel mask with the path overlaid, would settle problem 1.
- **PVS content of the slices:** whether stray PVS pixels or the E/F deep-plane blobs are counted. A per-slice count of PVS connected components, the share of PVS area within about 3 R1 of the vessel centre, and one example slice per location with the fits overlaid would settle problem 2.
- **Depth orientation of location D:** a depth intensity profile of the PVS channel or a side view of D would settle it.
- **Truncated outputs:** cells 19, 21, 29 and 39 print truncated tables in my reader. I relied on their summary lines and on filtering the full outputs.
