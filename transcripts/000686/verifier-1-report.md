## A. Outcomes

The claims file has 20 claims. The notebook tests 4 (all Fig. 5). It marks 5 blocked as data_missing (Figs. 3–4) and 11 blocked as other (Figs. 6–9). I checked the archive's API: version 0.240515.1909 holds only 18 NWB files, each one stitched YO-PRO-1 image of a Fig. 5 dish (40p-CC / 40p-Ctrl / 1p-x4-10cycles CC / Ctrl). There are no field maps, no single-cell time series and no Fig. 6–9 conditions.

| Claim | Outcome | Reason |
|---|---|---|
| fig3-field-simulation | blocked (data_missing) | No simulated field maps are in the asset list, and the criterion forbids a field model built by the author. |
| fig4-sham-no-uptake | blocked (data_missing) | No confocal time-lapse of single cells in the dataset; all 18 assets are monolayer images. |
| fig4-unipolar-uptake | blocked (data_missing) | Same as above. |
| fig4-bipolar-weaker | blocked (data_missing) | Same as above. |
| fig4-8phase-cancellation | blocked (data_missing) | Same as above; it also depends on the two claims above. |
| fig5a-trains-stronger | not_reproduced | Fails under all 8 readings (cell 12). At the e3 end trains are not above packets (1099 vs 1285 a.u., p=0.52). At the e1 end the difference misses p<0.05 (13565 vs 6347, p=0.059). Centre (p 0.004–0.044) and train e1 > centre (p≈0.03) hold. All readings agree, so it is not methods_underspecified. |
| fig5a-packet-center-enhanced | not_reproduced | "e1 end > centre" fails in all 16 readings (p 0.10–0.16), although every dish has e1 > centre (ratios 1.35–3.6, n=4). It also fails with 3-step ROIs (p=0.163, cell 20). Centre > trough holds in 10 of 16 readings. Since one required part fails under every reading, the readings do not split the outcome. |
| fig5b-rotation-center-peak | not_reproduced | Both parts hold in only 12 of 32 readings (cell 16). Under the centre-ROI reading, 1P×40 centre > trough has p=0.073 unpaired and 0.125 paired. Under the paired LOESS readings, 1T×40 periphery > centre has p=0.05–0.08. All directions are as claimed, and the criterion requires every reading. |
| fig5c-normalized-contrast | not_reproduced | Holds in 24 of 32 readings (cell 18). 7 of 8 centre-ROI readings have p=0.051–0.057, and one LOESS 0.3 reading has p=0.0515. 1P×40 is above 100% in every reading (134–268%), against 42–63% for 1T×40. A near miss in a consistent direction. |
| fig6a-more-packets-more-uptake | blocked (data_missing) | No 1Px4, 5Px4 or 10Px4 dishes in 000686. The notebook says "other" (see B1). |
| fig6b-center-to-periphery | blocked (data_missing) | Same as above. |
| fig6-void-between | blocked (data_missing) | Same as above. |
| fig6-peak-narrower | blocked (data_missing) | Same as above. |
| fig7a-amplitude-scales-uniformly | blocked (data_missing) | Only 6.4 kV dishes are in the dataset (session descriptions, cell 3). |
| fig7-amplitude-no-effect-on-distribution | blocked (data_missing) | Same as above. |
| fig8-center-equal-packets | blocked (data_missing) | Only Packet 2 and its train are in the dataset. |
| fig8a-periphery-packets-1-3-higher | blocked (data_missing) | Same as above. |
| fig8b-normalized-center | blocked (data_missing) | Same as above. |
| fig9a-gap-reduces-periphery-more | blocked (data_missing) | No electrode-gap conditions in the dataset. |
| fig9b-gap-boosts-targeting | blocked (data_missing) | Same as above. |

None of the blocked claims could be tested in part from 000686. No chance levels apply.

## B. Problems

1. **[does not affect a conclusion]** Cell 21: the 11 Fig. 6–9 claims are blocked as `other`. The claims file sets the data to dataset 000686, and those conditions are not in it, so the reason is `data_missing`. The notebook says the data sit in 000875, 001025, 001027 and 001028; I did not check that, since outside data is out of scope.
2. **[affects a conclusion: fig5b, fig5c]** Function `roi_means` and cell 20: ROI width is open in the paper and missing from the claims file's readings, and it changes outcomes.
   - With 3-step square ROIs, 1P centre > trough goes from p=0.073 to 0.003, the 5C contrast from p=0.051 to 0.014, and the 5A e1-end comparison from p=0.059 to 0.004.
   - The 5B and 5C failures rest mainly on the single 66-µm centre ROI. Its mean is driven by one dish: 1P×40 dish2 has a centre of 8148 against ends of 1583, which shows as the spike at 0 mm in cell 9.
   - The variant is run only for the main reading. Its squares widen along the diagonal too, so they overlap, which does not fit the paper's 224 ROIs of about 65 µm. A band one step long and wider across the diagonal would be the consistent variant.
   - fig5a-trains and fig5a-packet stay not reproduced at width 3: the e3 end still fails, and e1 > centre has p=0.163.
3. **[does not affect a conclusion]** Cells 14, 16 and 20: the trough is the minimum of the group mean profile, chosen and then tested on the same dishes. This biases centre > trough toward significance. The criterion asks for it, and the tests still fail, so the bias only makes the negative outcomes more conservative.
4. **[does not affect a conclusion, unverified]** Functions `footprint_radius` and `roi_positions`: the ROI end depends on each dish's footprint radius, estimated from intensity. Estimates run 1.15–1.44 mm and are larger in the train dishes, which have bright uptake rings, although the needles are identical. This links where the outermost ROI sits (±~0.15 mm, about 2 ROI steps) to the measured signal, near the electrodes where the gradient is steep. That matters for the e1-end and periphery values and for the 5C normalization. A fixed physical radius would remove it.
5. **[does not affect a conclusion]** Cell 9, function `prof_both`: the O2(b) "e1 end" on the averaged profile is the mean of the e1 and e2 ends. Which ends are averaged together by signed distance is a labelling choice stated in the code, so it is not "e1 alone". Both O2 readings give the same pattern.
6. **[does not affect a conclusion]** Cell 18: the O3(b) test (each dish's centre divided by its group's mean periphery) is the author's construction and is not labelled as an assumption. The O3(b) point values are correct.
7. **[does not affect a conclusion]** Assumptions I checked and found reasonable:
   - **Pixel size and diagonal:** 0.65 µm/px (tile arithmetic, cell 3), with the 8.4-mm diagonal read as inner edge to inner edge (measured 8.42–8.81 mm, footprints 1.15–1.44 mm against 1.5-mm needles).
   - **e1 identity:** top right in all 8 non-rotated dishes. The train images, where only e1 is energized, are unambiguous (cell 5).
   - **Background:** the footprint median (180–360 a.u.) is small next to the signals, and the bg rows match the raw rows.
   - **Electrodes and ROIs:** the four footprints and both ROI diagonals sit on the needles in all 18 images.
   - **Group counts:** n = 4 and 4 for Fig. 5A and 5 and 5 for Fig. 5B, matching the paper's "n = 4 to 5".

## C. Could not check

- **Synthetic tests of the helpers:** no numpy or scipy in this environment. I checked `signed_profile`, `roi_positions`, `centre_value` and `ttest` by reading the code only.
- **Whether the 1P×40 dish2 centre value (8148) is cells or debris:** a crop of dish2 around the array centre would settle it.
- **Sensitivity to the ROI end point:** O1–O4 tables with a fixed physical footprint radius, and with ROIs one step long and 3–5 steps wide across the diagonal, run under all readings rather than only the main one.
- **Paired 5A tests and the 3-step ROI result:** per-dish values at width 3 and the paired variants for 5A's trains-vs-packets place comparisons were not printed.
