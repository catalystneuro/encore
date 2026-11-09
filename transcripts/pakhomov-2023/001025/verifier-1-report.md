**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig4-unipolar-strongest | blocked (data_missing) | The archive holds 21 single-time-point stitched monolayer images. The asset metadata I queried has no single-cell time-lapse data. |
| fig4-bipolar-cancellation | blocked (data_missing) | Same reason as above. |
| fig5a-center-enhanced-without-rotation | blocked (data_missing) | Every session description is a rotated CANCAN protocol repeated 1 or 10 times. There are no 40-from-e1 dishes and no train dishes. |
| fig5bc-rotation-focuses-center | blocked (data_missing) | There are no 1Px40 or 1Tx40 dishes. |
| fig6a-more-packets-more-uptake | blocked (data_missing) | There are no 5Px4 dishes. 1Px4 is only on the small array and 10Px4 only on the large array, and the Fig. 6 legend names neither array nor voltage. |
| fig6b-normalized-center-by-packets | blocked (data_missing) | Same reason as fig6a. |
| fig7a-amplitude-scales-uptake | not_reproduced | 5.6/2.4 kV ratios over all 36 readings: periphery 5.11–10.91, half-way 5.31–6.15, centre 5.88–7.71. None is within tolerance of 15.5/16.2/16.8 (cell 14). With the footprint background subtracted, which is not the criterion, the main reading gives 13.4/15.9/15.2 (cell 15). |
| fig7b-targeting-independent-of-amplitude | not_reproduced | Under the main reading, 1 of 20 pairs differs: centre, 2.4 vs 4.8 kV, 108.6% vs 136.9%, p = 0.0037 (cell 17). 50 of 72 readings have at least one pair at p < 0.05 (cell 18). The result is fragile: with background subtracted, the main reading has no significant pair and 59 of 72 readings have none (see B1). |
| fig7cd-holds-for-large-array | not_reproduced (borderline) | Main reading: normalized centre 232.6% (n = 2) vs 126.0% (n = 3), p = 0.0494 (cell 20). Both 4.8 kV dishes (271%, 195%) lie above all three 6.4 kV dishes (102–150%). Only 10 of 72 readings reach p < 0.05, but with n = 2 against 3 a non-significant result cannot establish absence. Only two of the paper's large-array voltages are in the dataset. |
| discussion-independent-of-array-size | not_reproduced | The criterion requires both fig7b and fig7cd to be reproduced, and neither is. |
| fig8a-packets-differ-near-electrodes | blocked (data_missing) | There are no Packet 1 or Packet 3 dishes. The Packet 2 condition (4 kV, 1Px4) may be present; see B5. |
| fig8b-packet2-best-targeting | blocked (data_missing) | Same reason; see B5. |
| fig9-gap-boosts-targeting | blocked (data_missing) | The 0-mm condition (large array, 10Px4, 6.4 kV) is present, but there are no gap dishes. Every expected value is a ratio to a gap condition. |
| fig9c-restricted-to-center | blocked (data_missing) | There are no gap dishes. |

**B. Problems**

1. **[affects a conclusion] Background offset (cells 15, 17, 18; claims file fig7a criterion).** The no-background reading builds amplitude dependence into the normalized profile.
   - The raw images carry an offset that varies by session: dark floor 33–81 a.u. (cell 5), footprint background 150–376 a.u. (cell 10).
   - Normalizing (C+B)/(P+B) pulls dim dishes toward 100%. The 2.4 kV dishes are much dimmer than the 4.8 kV ones, so the one significant fig7b pair is plausibly this artefact. With background subtracted, the main reading has 0 significant pairs.
   - The paper's a.u. do not look like raw values. Fig. 8A gives Packet 2 at 4 kV, 1Px4 as about 120 a.u. near the electrodes and 215–235 a.u. in the centre. The dataset's 4.0 kV dishes give 615 and 719 a.u. (cell 15). The 5.6/2.4 kV ratios reach about 15 only after background subtraction.
   - The claims file says "none is subtracted, as in the Methods". The Methods (Section 2.4) are silent on this, and Section 2.2 does background-correct (F − F0). I report this as a possible misreading of the paper by the claims file. The notebook follows the criterion and shows background only as a variant. This choice decides fig7b and plausibly fig7a.
2. **[does not affect a conclusion] The `diag8.4` scale reading is geometrically impossible (cell 5, cancan docstring).** With an 8.4 mm centre-to-centre diagonal and 1.5 mm needles, the needle edge sits at 3.45 mm on the large array and 1.55 mm on the small one. The paper's spans are ±3.65 mm and ±1.65 mm, so the end ROIs would lie on the needle.
   - The notebook's "ends N px before the electrode footprint" check uses the detection template radius (`DISK_R`, 0.38–0.54 mm), not the 0.75 mm needle radius, so it hides this.
   - The reading inflates periphery values: periphery ratio up to 10.91 (cell 14).
   - It only changes the "x of 72 readings" counts, not the main-reading outcomes.
3. **[does not affect a conclusion] Even on the main camera scale, the end ROIs may touch the excluded zone (cell 5).** The span ends about 0.12 mm (small array) and 0.22 mm (large array) from a 0.75 mm-radius needle edge. That is inside the paper's "<5% of diagonal" exclusion zone, about 0.25 mm and 0.46 mm. The scale assumption, 0.65 µm with no binning, is reasonable, but it gives a large diagonal of 9.23 mm against the paper's 8.4 mm and an array ratio of 1.83 against "about 2-fold". This is never resolved.
4. **[does not affect a conclusion] Packet identity is assumed, not checked.** The session descriptions say "CanCan protocol … 12.5% lower" and never name the packet. Assuming Packet 2, as in Fig. 7, is reasonable given the dandiset's title.
5. **[does not affect a conclusion] Packet 2 data for Figs. 8 and 9 is in the dataset but not reported.**
   - The 4.0 kV 1Px4 dishes match Fig. 8's Packet 2 condition, if Fig. 8 used the small array. Their values (periphery 615, centre 719 a.u.; normalized centre about 119–128%, cells 15 and 17) could have been set against the paper's 120 a.u., 215–235 a.u. and 183%. They disagree with all three.
   - The 6.4 kV 10Px4 dishes are Fig. 9's 0-mm group.
   - The claims stay blocked, because their criteria need Packets 1 and 3 and the gap dishes.
6. **[does not affect a conclusion] 2.4 kV has n = 4 against the paper's n = 3, and fig7b has no leave-one-out (cell 17).** I checked by hand from the per-dish values: any three of the 2.4 kV dishes (maximum 114.7%) stay below every 4.8 kV dish (minimum 131.9%). The significant pair survives.
7. **[does not affect a conclusion] LOESS is local-linear with `it=0` (`loess`).** It is fitted over the whole diagonal with span 0.75. On a synthetic profile it flattened a narrow centre peak (fit 128 against ROI mean 144). The span comes from the claims file, and the LOESS readings do not change any outcome.
8. **[does not affect a conclusion] Helper and detection checks passed.**
   - On a synthetic radial image, `strip_histograms`, `roi_profile`, `roi_at`, `diagonal_measures` and `summarize` returned the exact end, half-way and centre values.
   - The cell 8 overlays show all four electrodes correctly located in all 21 images.
   - Every number derives from the loaded data. There is no train/test split, so no leakage to check, and no chance level applies.

**C. What I could not check**

- **Whether these dishes are the paper's Fig. 7 dishes.** The counts differ: 4 dishes at 2.4 kV and 2 at 4.8 kV on the large array, against n = 3. The figure's plotted values and its large-array voltages were not readable without the PDF.
- **The true pixel scale.** An output measuring the radius of each needle's dark footprint in pixels, on both arrays, against the 1.5 mm needle diameter would settle it, and with it the placement of the end ROIs.
- **The background effect across readings.** It would help to have the full background-subtracted fig7b and fig7cd tables per reading, plus per-dish normalized values with background removed. The notebook prints only counts and the main-reading result.
- **A Packet 2 comparison against Fig. 8.** A cell setting the 4.0 kV 1Px4 values against Fig. 8's Packet 2 numbers, and the 6.4 kV 10Px4 profile against Fig. 9's 0-mm curve, would show whether the dataset's a.u. are on the paper's scale at all.
