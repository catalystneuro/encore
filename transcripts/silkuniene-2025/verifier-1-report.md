**Verifier report, round 1: Silkuniene et al. 2025, claims file `silkuniene-2025.yaml` (28 claims)**

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| fig1e-field-simulation | blocked: data_missing | I checked the session descriptions of all 329 assets on the archive. None mentions a simulation or Sim4Life. |
| fig2-heating-below-44c | blocked: data_missing | No asset mentions thermochromic film. Every file is a fluorescence image of one well. |
| fig3a-centre-enhanced | blocked: data_missing | All 88 assets of 001047 state a 3.8-mm array and a 3.2-kV first pulse, which I confirmed in the archive metadata. That is not the paper's array. Part of the claim is testable on 001276 (see A2). |
| fig3bc-rate-suppresses-off-target | blocked: data_missing | Same as above. The 6 and 7 mm part could be tested on 001276 at 1 Hz (n=2) against 0.2 MHz (n=6). |
| fig3-lorentzian-profile | blocked: data_missing | Same as above. Only 1 Hz and 0.2 MHz exist on the 15.3-mm array. |
| fig3-tail-deviation-falls-with-rate | blocked: data_missing | Same as above. Two rates cannot give a meaningful trend. |
| fig4b-40-fold-ratio | blocked: data_missing | Correct for 001047. In the 001276 variant (cell 19, n=6), the mean of per-well ratios at 6 mm is 36.7, inside 36 to 44. |
| fig4b-centre-no-rate-effect | blocked: data_missing | No 1-kHz or 10-kHz wells exist in any of the four dandisets; I checked every asset description. |
| fig4b-near-electrode-decline | blocked: data_missing | Only two rates exist, so the power-law fit is degenerate. |
| fig4c-fwhm-falls-with-rate | blocked: data_missing | There are no 1-kHz or 10-kHz wells anywhere. |
| fig4c-log-trend | blocked: data_missing | Same as above. |
| fig5-raised-electrodes-weaken-centre | not_reproduced | Cell 22: at 1 mm the gap rule fails (48.7±11.9 against 100±24.3). At 2 mm it holds. The criterion needs both. The well selection is in question (B2). |
| fig5-killing-focused-centre | reproduced | Cell 24, 0 mm: Pr at the centre is 1188±339; at 6 mm it is 8.4±2.4 and at 7 mm 16.5±5.9. The gap rule holds and t-test p≈0.008, under both ROI readings. |
| fig5ab-yp-spot-slightly-larger-than-pr | not_reproduced | Cell 26: YP/Pr FWHM ratio is 0.66 to 0.75 at 0 mm under every reading. The YP spot is narrower than the Pr spot. The raw profiles agree: at 1 mm YP is 37% of its peak and Pr is 52%. |
| fig5b-gaussian-pr-lorentzian-yp | reproduced | Cell 28: all four R² are within tolerance, both orderings hold under every reading, and every F-test p is below 1e-6. |
| fig5b-reversible-beyond-2mm | reproduced | Cell 30: reading (b) gives 2.08 and 2.11 mm, inside 1.8 to 2.2. Reading (a) gives 2.84 to 3.0. The criterion needs one reading. |
| fig5c-nuclear-yp-centre | partially_reproduced | Cell 32: zone 1 is brighter than zones 2 and 3, and the footprint is darker than both, in 12 of 12 wells. Footprint Hoechst is present in 5 of 5. The nuclear part is blocked because every 001284 file is a 4x whole-well image, which is the criterion's "partially" case. |
| fig6b-peak-900ns-not-significant | reproduced | Cell 36: 900 ns has the highest mean (891, against 800 and 538). Bonferroni-corrected p is 0.58 and 1.0, and the ANOVA p is 0.51. This also holds with all 7 wells at 600 ns. |
| fig6c-normalized-decline-similar | not_reproduced | Cell 38: the gap rule finds 5 to 20 distance-pairs that differ, mostly 300 against 600/900 ns at 1 to 3 mm. With all 7 wells at 600 ns there are still 2 to 10. |
| fig6d-longer-pulses-sharper-peak | partially_reproduced | Cell 40: fitted to individual wells (O4a) with the two 600-ns wells left out, all slopes are negative with p = 0.0008 to 0.0058. Fitted to group means, p = 0.048 to 0.165. With all 7 wells at 600 ns, p is about 0.9. |
| fig6d-600-900-differ-from-300 | partially_reproduced | Cell 42: 900 against 300 ns has corrected p = 0.006 to 0.018 under every reading. 600 against 300 ns falls below 0.05 in only one reading. |
| fig6d-900ns-fwhm | reproduced | Cell 44: 1.69 to 1.77 mm and 11.0 to 11.6% of the gap, within 1.7±0.08 and 11.1±0.6 under every reading. The 900-ns group is the same in both well sets. |
| fig7be-center-linear-with-bursts | partially_reproduced | Cell 48: fitted to individual wells, CT26 p = 9.1e-4 (just under 0.001) and CHO p = 2e-11. Fitted to group means, p = 0.036 and 0.0015. The criterion needs every reading. |
| fig7b-ct26-saturation | partially_reproduced | Cell 50: the 6-burst mean (4847) is below the line (5719) but inside the 95% band (4028 to 7410). This is the criterion's "partially" case. |
| fig7cf-fwhm-with-bursts | partially_reproduced | Cell 52: fitted to individual wells, CT26 p < 1e-6 and CHO p = 0.07 to 0.33, which meets the criterion. Fitted to group means, CT26 p = 0.0005 to 0.016, under 0.001 in only one combination. The CHO group-means p of 0.436 matches the paper's 0.44, which suggests the paper fitted group means. |
| fig7-sharpest-peak-one-burst | reproduced | Cell 54: FWHM 1.03 to 1.13 mm, 6.7 to 7.4% of the gap, area reading (b) 2.04 to 2.47%. It is the smallest group in every reading (next smallest 1.69 mm). |
| fig7-offtarget-40-50-fold | not_reproduced (provisional) | Cell 56: with the darkest footprint as background, every group is outside 36 to 55. Reading A depends on which footprint is used, and the notebook did not run all choices (B5). |
| fig7-cho-replicates-ct26 | reproduced | Cell 58: the centre is above 6 and 7 mm by a gap in every cell line, burst number from 2 up, and ROI reading. |

**A2. Blocked claims checked against the archive (step 4)**

- 001047: all 88 assets give a 3.8-mm electrode distance and 3.2 kV. Cell 3 prints NaN spacing for 54 of them, which is a parsing gap in the notebook; the archive descriptions all say 3.8 mm.
- Packet rates: across 001276, 001277 and 001284, the only rates stated are 0.2 MHz and 1 Hz. No asset holds a 1-kHz or 10-kHz well.
- What 001276 holds that the claims file does not assign: CT26 at 2 bursts (x4) on the 15.3-mm array, with CANCAN at 1 Hz (n=2), CANCAN at 0.2 MHz (n=6) and control (n=4).
  - With these wells, fig3a, the 6 and 7 mm part of fig3bc, fig4b-40-fold-ratio and fig3-lorentzian could be tested in part, for two rates only. fig4c-* and the trend claims cannot.
  - Cell 19 already hints at two outcomes. fig4b-40-fold-ratio would be reproduced under one combination (36.7). The control part of fig3a would likely fail: in 3 of 4 control wells the centre is not below 6 and 7 mm.

**B. Problems**

1. **[affects a conclusion]** Claims file header and the dataset lists of the fig3 and fig4 claims. The file assigns the packet-rate series of Figs. 3 and 4 to 001047 from its description. The archive shows 001047 is a 3.8-mm, 3.2-kV array study, which is a misreading in the claims file. The only 15.3-mm packet-rate wells are in 001276, which those claims do not list. That is why nine claims are blocked when parts of them could be tested.
2. **[affects a conclusion]** Cells 22, 26, 28 and 30 (Fig. 5). The notebook uses all 12, 11 and 11 YP wells per elevation, where the paper reports n = 6 to 7.
   - The August 2024 batch has 7, 6 and 7 wells, which matches the paper's n. The October batch has 5, 5 and 4, which matches the Pr n and holds all the Pr images.
   - That subset was never run as a reading, although Fig. 6 was matched to the paper's n. By batch, the 1-mm and 2-mm centre values differ a lot (Aug 57.5 and 41.4; Oct 38.0 and 7.1), so fig5-raised could change.
3. **[affects a conclusion]** Cell 34 (Fig. 6). The two 600-ns wells P1-20240926-B2 and B3 were dropped after looking at their profiles. The paper gives no basis for dropping them; B2's spot is 5.4 mm off the array centre (cell 10), which supports leaving that one out.
   - The other 5-of-7 subsets were not run.
   - With all 7 wells, fig6d-longer fails (p about 0.9) and the 600-ns part of fig6d-600-900 fails.
4. **[affects a conclusion]** `cc._one_well` and `geometry_from_centre`. Where no footprints are found, the profile is centred on the YP spot itself, with rotation fixed at -3°. This applies to 20 of 54 wells in 001276, 12 of 18 in 001277 and 23 of 34 in 001284.
   - Centring on the spot tends to make the peak higher and the FWHM narrower than measuring from the array centre, as the paper does.
   - A rotation error of up to about 8° moves the 7-mm ROI about 1 mm sideways.
   - The notebook does not report which method each well used in each group. This bears on fig6d-900ns-fwhm and fig7-sharpest, whose values sit near the tolerance edges.
5. **[affects a conclusion]** `cc.profiles`, background as the minimum over footprints. The claims file leaves the background footprint open (O1). For the ratio claims, the near-electrode value is only about 47 a.u., and the footprints in one well differ by up to about 35 a.u.
   - Using the mean of the four footprints raises CT26 at 2 bursts to 43.8 (cell 56).
   - My estimate from the printed values: using the brightest footprint for CT26 at 1 burst gives a ratio of about 50 at 6 mm, inside 36 to 55. fig7-offtarget would then be reproduced under reading A.
6. **[affects a conclusion]** Cells 46 and 48 (Fig. 7). CT26 at 2 bursts has n=6 from three dates, where the paper reports 3 to 5. CHO has 5 to 8 wells per burst number, where the paper reports 4. The CT26 slope p of 9.1e-4 sits just under the 0.001 bound, so the selection could flip fig7be. No subset matching the paper's n was run.
7. **[does not affect a conclusion]** Cell 30. Only O2 reading (a) was run for fig5b-reversible-beyond-2mm. The claim is already reproduced under reading (b).
8. **[does not affect a conclusion]** `cc._one_well`. The Cy3 and DAPI order in the two-channel files is taken by position and never checked against the OME channel names (`ome_channels`). The printed intensity levels are consistent with the assumed order.
9. **[does not affect a conclusion]** Cell 54. The "sharpest in the study" comparison leaves out the Fig. 5 groups (001284), which the criterion says to report. The margin to the next group is large (1.03 against 1.69 mm).
10. **[does not affect a conclusion]** I checked the helpers on synthetic inputs:
    - `fit` recovers the Lorentzian FWHM exactly, and the Gaussian FWHM equals 2.4σ.
    - `gap_exceeds` behaves as documented. It takes the larger of the two s.e., which is conservative.
    - `find_array` recovers the centre and rotation exactly, but underestimates the side by 0.38 mm (12.42 against 12.8). That only changes the ROI direction slightly.
    - Averaging over a 406-µm ROI widens a 1.1-mm FWHM to about 1.17 mm, which comes from the paper's method.

**C. What I could not check, and the outputs that would have settled it**

- Which wells were measured from the footprints and which from the spot centre, per group. A per-group table with each well's geometry method and its FWHM and centre value would let me judge problem B4.
- Ratios and near-electrode values with each single footprint as background, for fig7-offtarget and the 001276 variant of fig4b-40-fold (problem B5).
- Fig. 5 results restricted to the August YP batch (n = 7, 6, 7): centre mean ± s.e., the gap rule, the FWHM ratio and R² (problem B2).
- fig6d results over every 5-of-7 subset of the 600-ns wells (problem B3).
- Fig. 7 results on subsets matching the paper's n (CT26 3 to 5 per burst number, CHO 4).
- The figure montages (cells 5 and 11) are stored only as images, so I could not check the footprint detections or the "no central peak" judgement from text. A per-well table of corner scores and spot offsets would have let me.
