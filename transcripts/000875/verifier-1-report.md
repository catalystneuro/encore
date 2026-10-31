**A. Outcomes**

The claims file has 17 claims. The notebook tests 4 and treats 13 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| fig6a-more-packets-more-uptake | reproduced | In cell 15, the main reading (r2, b1, c1, e1, t1) gives means of 544/3240/9712 at the periphery, 674/2631/5172 at the center and 479/1148/1880 at the trough. The 40-against-4 t-test gives p = 0.016, 0.0008 and 0.0008. The order holds in 108 of 108 combinations, and 48 of them are fully reproduced. The variant that sets the ROI extent from the footprints also passes (cell 17, periphery p = 0.035). |
| fig6b-peak-relative-to-periphery | partially_reproduced (fragile) | No combination puts all three treatments within tolerance. The main reading gives 124/87/59%, against 200/100/100% (cell 19). All 7 partial combinations use b2, which subtracts the median inside the footprints. With raw intensities (b1), 1Px4 never falls in 180–220%. The partial rows have s.e. of 31–81 points, and in cell 20 only dish 23 is near 200%. The outcome depends on whether the footprint is a valid "cell-free or dark offset" (problem 1). |
| fig6-trough-half-of-center | partially_reproduced | The main reading gives 1.40/2.16/2.80, so only 5Px4 is within 1.8–2.2 (cell 22). 10Px4 is never within tolerance (2.66–12.06 across all 144 rows), and all ratios are above 1. That gives 41 partial and 0 reproduced, under b1 and b2 alike. |
| fig6-peak-narrower | reproduced | Under the main reading, w1 is 1.051, 0.545 and 0.488 mm, so width falls from 4 to 20 to 40 packets. It also falls under LOESS 0.25 (0.80/0.65/0.56) and 0.5 (0.99/0.86/0.82), and w2 falls under LOESS 0.5 (cells 25 and 26). It holds in the variant that sets the ROI extent from the footprints too (cell 27). The criterion asks for no test. With n = 3, the per-dish w2 values overlap (cell 26). |
| fig4-bipolar-cancellation | blocked: data_missing | The archive holds 9 files, all monolayer images (Packet 2, 3.2 kV). There is no single-cell time-lapse. |
| fig4-twenty-fold-cancellation | blocked: data_missing | Same as above. |
| fig5a-packet-without-rotation | blocked: data_missing | There are no 1Tx40 or unrotated Packet 2 dishes, and no large array. |
| fig5bc-rotation-focuses-center | blocked: data_missing | Same as above. |
| fig7ab-amplitude-scales-uptake | blocked: data_missing | There is only one voltage (3.2 kV), and a ratio between voltages needs two. |
| fig7-targeting-independent-of-amplitude | blocked: data_missing | Same as above: only one voltage. |
| fig7-targeting-independent-of-array-size | blocked: data_missing | Only the small array is present: the center-to-center diagonal is 5.2–5.6 mm, against 8.4 mm for the large array. |
| fig8-packet2-best-targeting | blocked: data_missing | There are no Packet 1 or Packet 3 dishes and no 4 kV dishes. |
| fig8b-normalized-center | blocked: data_missing | Same as above. |
| fig8-cancellation-predicts-targeting | blocked: data_missing | It needs both the Fig. 4 data and the Fig. 8 data, and neither is present. |
| fig9-gap-fades-periphery | blocked: data_missing | There are no dishes with the array lifted above the monolayer. |
| fig9b-six-fold-targeting | blocked: data_missing | Same as above. |
| fig3-field-simulation | blocked: data_missing | No Sim4Life model has been deposited. |

I checked the blocked claims against the archive API myself. Version 0.240515.1925 and the draft both have the same 9 assets: 1p, 5p and 10p, x4, 3.2 kV, 3 dishes each. The metadata list no other resources, so no part of any blocked claim can be tested.

**B. Problems**

1. **[affects a conclusion]** `cancan.footprint_level` and the b2 reading (cells 19, 20 and 22). The footprint median is used as a "cell-free or dark offset", but nothing shows the footprint is cell-free.
   - The paper uses blunt hollow needles (Methods 2.3). Cells inside the lumen would sit in a nearly field-free region, unpermeabilized but still present.
   - Methods 2.4 calls the areas next to the electrodes "mechanical damage", not cell-free.
   - The footprint median (239–403 counts) is about the same as the whole-image median (228–364) and well above the image minima (110–200), so it looks more like the baseline of unexposed cells than a dark level.
   - fig6b's partial outcome rests only on b2.
   - A camera dark-offset reading, such as the region minimum or the ORCA's roughly 100-count offset, is the clearer instance of b2 and was not run. My rough estimate is that it could also put r1-dA, c2, n2 into the partial range. So the fig6b outcome is open between partial and not reproduced, as things stand.
2. **[does not affect a conclusion]** `PIXEL_UM = 0.65` (cells 7 and 8). Two independent cues point to about 0.53 µm per pixel:
   - the footprints measure 1.66–2.09 mm against a 1.5 mm needle;
   - "approximately a 2-fold size difference" from the 8.4 mm large array implies a small-array diagonal of about 4.2 mm, against 5.35 mm measured.

   The notebook raises the first cue but not the second. At 0.65 µm, the end ROIs of some dishes fall inside the excluded zone (margin 1.5–5.6% of the diagonal). The variant that sets the extent from the footprint geometry removes the dependence on pixel size, and it gives the same outcomes for all four claims (cells 17, 19, 22 and 27).
3. **[does not affect a conclusion]** Cell 15: in 60 of 108 combinations the periphery test fails (single diagonals and one-end readings), with p up to 0.13. The verdict stands only because the claims file accepts a claim that holds under any combination. Saturation of up to 5% in the 10Px4 periphery ROIs (cell 5) works against the order, so it is conservative here.
4. **[does not affect a conclusion]** Cell 25: w2 does not depend on the center reading, yet every row appears twice, so counts such as "104 of 144" double-count. Rows with n2 are also not independent combinations.
5. **[does not affect a conclusion]** Cell 25, w1 without smoothing: 1Px4 measures 1.05 mm under c1 and 0.59 mm under c2, so the measure is sensitive to the center reading. The order holds under both.
6. **[does not affect a conclusion]** Cell 3 metadata: the species is *Bos taurus* while the cells are CHO, and two pairs of dishes share a session start time. The notebook checks this correctly in cell 9: no two images are identical, and the array centers differ.
7. **[does not affect a conclusion]** I ran the helpers on synthetic inputs, and they behave correctly:
   - `roi_values` gives the right signed positions and means;
   - `side_minima` and `center_index` (c1 and c2) find the right indices;
   - `half_max_width` returns a sensible width;
   - `mean_profile` n1 and n2 normalize correctly.

   The tests are two-sided `ttest_ind` with equal variances, as the claims file says. No training and test split is involved, so leakage does not apply.

**C. What I could not check**

- **Footprint content.** I could not see what the footprints contain. These outputs would settle problem 1:
  - a full-resolution crop of one footprint and its rim;
  - intensity histograms of the footprint interior, the unexposed monolayer outside the array, and the darkest pixels;
  - a b2 variant that subtracts a camera dark level.
- **Electrode detection at full resolution.** I saw only the summary geometry, not the image. A full-resolution overlay of the fitted circles for each dish would let me check it.
- **Per-dish profiles.** These outputs would let me judge how much the n = 3 means rest on single dishes:
  - per-dish profile plots for each treatment;
  - per-dish values for the fig6b partial rows (r1-dA and r1-dB with b2).
- **Pixel scale.** There is no output testing the scale against the array-size ratio of Methods 2.3. A scale check on the center-to-center diagonal would close problem 2.
