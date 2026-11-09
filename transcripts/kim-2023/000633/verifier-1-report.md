**Verification report, round 1: Kim et al. 2023 (doi:10.3390/ijms241310921) against DANDI:000633 v0.231013.2226**

### A. Outcomes

The claims file has 12 claims. The notebook tests 3 and treats 9 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| fig2-cancellation-at-180 | blocked (data_missing) | The archive API lists 2 assets, both single stitched triangle-array images. There are no 1 Hz data, no per-ROI data for the n = 3 experiments and no simulated angles. Cell 19 builds an 833 kHz curve from the two Fig 4 dishes (n = 1, angles from a substitute model). It gives 5.8-fold against the paper's 20, which is outside tolerance. It cannot decide the claim. |
| fig2-crossover-angle | blocked (data_missing) | Same reason. For information only: cell 19's 833 kHz crossings are 128.4°, 123.7° and 120.4°, near the paper's 130°. There is no 1 Hz curve. |
| fig2-facilitation-plateau | blocked (data_missing) | Same reason. For information only: the single ROI at 90–100° gives 378% (paper about 300%), and the ROIs below 90° do not form a plateau (mean 1460%). |
| fig2-60-fold-co-counter | blocked (data_missing) | Same reason. For information only: 85-fold (plateau reading) and 56-fold (nearest-0° reading), from one dish. |
| fig3-1hz-co-cross-same | blocked (data_missing) | There are no square-array images and no 1 Hz or cross-directional groups. Cell 5 finds 3 footprints in both images. |
| fig3-770khz-co-enhanced | blocked (data_missing) | The single-pulse file's description does mention "4 co-directional paired-pulse trains, 770 kHz", but it names a triangular array, there is only one dish and there is no 1 Hz comparison group. Nothing in the claim can be tested. |
| fig3-770khz-cross-same-as-1hz | blocked (data_missing) | Same as above. |
| fig4a-single-pulse-follows-field | reproduced, with a caveat | Cell 11, reading (a): Spearman ρ = 0.666 (p ≈ 0) with E1 = base_a and 0.460 (p = 1e-137) with E1 = base_b, positive under all 16 variants. Reading (b): the electrode order matches only with E1 = base_a. The file does not record which electrode is E1, so the pass depends on choosing E1 from the data (problem 2). |
| fig4bc-paired-pulse-focal-apex | reproduced | Cell 14. In the paired-pulse image, apex YP is above both base electrodes at 100 µm (843.9 vs 255.3 and 104.1) and at 500 µm (725.7 vs 269.6 and 119.0). The apex/base ratios rise from 0.05–0.20 in the single-pulse image to 2.7–8.1 in the paired-pulse image. Both readings pass. |
| fig4-comet-shape | partially_reproduced | Cell 16. With the maximum taken literally as the claims file states it (3999), the region fails at both thresholds: 0 mm² at half maximum, and at quarter maximum its reach toward the base is −707 µm. With the 99.5th-percentile or median-filter maximum it passes at both thresholds (toward the base 2.6–4.1 mm, across 1.2–2.3 mm). The literal maximum comes from one hotspot that the notebook never examines (problem 3). |
| fig5-base-sawtooth | blocked (data_missing) | The dandiset holds no FluoVolt strobe data. |
| fig5-apex-larger-polarization | blocked (data_missing) | Same reason. |

The claims file gives no chance levels, so there were none to compare.

### B. Problems

1. **[affects a conclusion] Cells 3–4: the single-pulse file's metadata describe a different exposure.** Its `session_description` reads "4 co-directional paired-pulse (600 + 600 ns) trains … 770 kHz, 10 kV/cm". Figure 4A is 5 single 600 ns pulses at 833 kHz and 4 kV. The paired-pulse file says 2 kV where the paper says 4 kV.
   - The notebook mentions both conflicts but still treats the file as Fig 4A, based only on its name and the dandiset title.
   - Both readings are one-direction exposures, so the qualitative pattern for fig4a and the single/paired contrast in fig4bc probably survive. Even so, both outcomes rest on an identification the metadata contradict, and the report should say so.
2. **[affects a conclusion] Cell 11: which electrode is E1 is never resolved.** The notebook runs both assignments, which is correct, but reaches no verdict between them.
   - Reading (b) passes only with E1 = base_a. That is the assignment under which the brightest base electrode is the pulsed one, so it is inferred from the data under test.
   - The two base electrodes are nearly symmetric (base side 4.64 mm, apex sides 6.59 and 6.78 mm). The asymmetry in YP (650 vs 263) therefore does point to base_a as E1, but this is an assumption and should be stated as one.
   - With E1 = base_b, the two readings disagree, which the criterion calls methods_underspecified.
3. **[affects a conclusion] Cell 16: the comet maximum is never inspected.** The literal maximum sits at binned pixel (562, 804), 2.47 mm from the apex. Its binned YP peaks at 26996, against a 99.9th percentile of 2953, and the next-highest smoothed value is 1562.
   - It looks like debris or saturation, but the notebook shows no crop of it and no MemBrite channel there.
   - The two alternative maxima are the author's own choices. They are stated in the notebook but are not in the claims file, and the outcome depends on them.
4. **[does not affect a conclusion] Cell 11: the Spearman p-values treat 1600–2600 contiguous ROIs as independent.** Spatial autocorrelation makes p far too small. With ρ between 0.42 and 0.75 under every variant, the positive sign is not in doubt.
5. **[does not affect a conclusion] Cell 5, `find_footprints`: footprints in the single-pulse image fit poorly.**
   - The fitted diameters average 1.22 mm, one is 1.03 mm, and edge s.d. is 12–14 bins (about 130 µm), against 3–9 bins in the paired image.
   - Both the electrode positions for the fig4a field map and the near-electrode ROIs in fig4bc depend on these fits.
   - The fig4bc result agrees at 100 and 500 µm, and the triangle side lengths match between the two images, so the outcome is unlikely to change.
   - The scale (0.654 µm/px) comes from the paired image only. It matches the 0.65 µm of the camera and objective.
6. **[does not affect a conclusion] Field map (`solve_potential`, cell 7): the 2D finite-difference model replaces Sim4Life, as the notebook states.**
   - This is reasonable: the needles touch the glass and span the solution, so conduction is two-dimensional.
   - My synthetic test of the symmetric triangle gave 4.7–10 kV/cm on the bisecting line at 4 kV and angles from 170° near the base to 16° near the apex, consistent with Section 2.1.
   - The grid check in cell 7 differs by 1.3%. The dish centre is assumed to be the image centre; this is unchecked but has little effect with the wall 17.5 mm away.
7. **[does not affect a conclusion] Cell 16: smoothing runs before masking.** `uniform_filter` and `median_filter` mix the dark footprints and the zero-valued image corners into nearby smoothed values. This lowers values next to the apex footprint, which works against the "touches apex" test, and the test still passes.
8. **[does not affect a conclusion] Cell 11: the neighbourhood radius is not really varied.** Results at 500 and 1000 µm are identical. That is expected for ρ, but it means the order test never actually changes with this choice.
9. **Helper functions tested on synthetic inputs, all correct:** `fit_circle` (recovers centre and radius with 5 outliers), `vector_angle` (180°, 90°, 0°), `roi_mean`, `label_electrodes`, `find_footprints` (three synthetic discs recovered to 0.1 px) and `solve_potential` (symmetric, physically sensible).
10. **Claims file:** I found no place where it misreads the paper.

### C. What I could not check

- **Whether the comet maximum is an artifact.** A full-resolution crop of both channels around binned pixel (562, 804) of the paired-pulse image would settle problem 3.
- **Which electrode is E1, and whether the deposited images match Figure 4 in orientation.** The paper text I had lacks the figure images. A downsampled view of each file with the electrode labels, placed beside Figure 4A and 4B, would let the labelled E1 confirm or overturn problem 2.
- **Footprint fits in the single-pulse image.** An overlay of the fitted circles on a zoomed view of that image would show whether problem 5 matters.
- **Whether the single-pulse file really is Fig 4A.** Nothing in the data can settle problem 1. Only the authors could.
- **Spearman significance under spatial correlation.** A block-permutation or spatially thinned version of the test would give an honest p-value (problem 4).
