## A. Outcomes by claim

The claims file has 24 claims. The notebook tests 18 and blocks 6.

| Claim | Outcome | Reason |
|---|---|---|
| fig3-field-simulation | blocked (data_missing) | I checked the archive: all 70 assets across the five dandisets are single-time-point `ScanningImaging` monolayer images. None holds a simulated field map. |
| fig4-sham-no-uptake | blocked (data_missing) | No single-cell confocal time lapse is in any dandiset (cell 14; archive asset list and session descriptions). |
| fig4-unipolar-strongest | blocked (data_missing) | Same reason. |
| fig4-bipolar-weaker | blocked (data_missing) | Same reason. |
| fig4-twenty-fold-cancellation | blocked (data_missing) | Same reason. |
| fig5a-trains-stronger | not_reproduced | Trains exceed packets at the e1 end and the centre in 16/16 readings, but not at the e3 end (ratio 0.75, p = 0.40). The train profile does fall from e1 to the centre. The criterion requires all three places, so it fails; but see problem 1. |
| fig5a-packet-center-enhanced | partially_reproduced | Reading (a), centre above the trough, holds in 16/16 readings, paired and unpaired. The e1 end above the centre fails in 0/16 (main reading p = 0.39). The criterion's partial rule applies. |
| fig5b-rotation-center-peak | reproduced | The 1P×40 centre is above its trough in 48/48 readings, both ways. The 1T×40 void holds in 100% of readings unpaired but 79% paired; under the main reading the paired test gives p = 0.055. The outcome rests on the unpaired choice (problem 5). |
| fig5c-normalized-contrast | reproduced | Holds in 32/32 readings. Main reading: 213% vs 57%, p = 0.0088. |
| fig6a-more-packets-more-uptake | partially_reproduced | The rise 4 < 20 < 40 packets with 40 > 4 holds at all three places in 48/48 readings. The centre-above-trough test fails for 1Px4 and 5Px4 (p ≈ 0.15). The criterion has no rule for this combination (problem 10). |
| fig6b-peak-relative-to-periphery | partially_reproduced | All three values are never within tolerance (0/576). The 1Px4 value is within tolerance and above both others in 8/576 readings, all using one diagonal, background subtraction and w1. Main reading: 128 / 70 / 64%. A thin pass. |
| fig6-trough-half-of-center | partially_reproduced | All three ratios are never in 1.8 to 2.2 (0/288). One or two are in range with all above 1 in 173/288. |
| fig6-peak-narrower | reproduced | Under the half-height width, the width falls 1 > 5 > 10 in 88% of readings, including the main reading (0.66 / 0.64 / 0.44 mm). Under the trough-to-trough width it falls in 62%, but not in the main reading. |
| fig7a-amplitude-scales-uptake | partially_reproduced | At most one of the three ratios is within 10%, in 8/288 readings. Main ratios are 6.7 / 5.7 / 7.3 against 15.5 to 16.8. This meets the letter of the partial rule only. |
| fig7b-targeting-independent-of-amplitude | not_reproduced | At least one voltage pair differs in 74% of readings (98% without background subtraction). The paper's own error-bar rule finds 3 pairs differing under the main reading. The 4.8 kV normalized centre is 229% against about 120% at the other voltages. The main reading, with no pair differing (min p = 0.052), is an outlier among the readings (problem 2). |
| fig7cd-holds-for-large-array | reproduced | No pair differs in 96% of readings, including the main one (p = 0.95 at the centre). It rests on n = 2 against n = 3 and only two voltages (problem 3). |
| discussion-independent-of-array-size | not_reproduced | Its criterion needs both fig7b and fig7cd reproduced, and fig7b is not. |
| fig8a-equal-center-uptake | not_reproduced | Centres are in range in 0/576 readings. Some pair differs in 100% of raw readings: P1 against P2, p = 0.0009. |
| fig8a-more-uptake-near-electrodes | not_reproduced | Values are in range in 0/576 readings. Both tests hold in 0% of readings. Packet 3 is below Packet 2 at the periphery. |
| fig8b-packet2-best-targeting | not_reproduced | 0/576 readings are within tolerance, and the partial pattern holds in 0. Packet 3 has the highest normalized centre in every reading. The archive's protocol descriptions confirm the file labels (problem 4). |
| fig8-cancellation-predicts-targeting | blocked (data_missing) | The Fig. 4 ranking is in no dataset. The Fig. 8 half is testable, and under the files' labels it points to Packet 3, not Packet 2. |
| fig9a-gap-reduces-periphery-more | partially_reproduced | At most 5 of the 6 ratios are within 10% in any reading (4 in the main reading). The near-electrode ratio exceeds the centre ratio at every gap in 99% of readings. |
| fig9b-gap-boosts-targeting | reproduced | The 2-mm value is in 540 to 660% and is the largest in 202/576 readings. The main reading is 541%, at the lower edge. |
| fig9c-restricted-to-center | not_reproduced | The centre is never the highest point at all three gaps (0/96 readings); the peak is at 0 to 0.73 mm. At 3 mm, the centre above the periphery fails (p ≈ 0.3). |

## B. Problems

1. **[affects a conclusion]** Cells 16 and 17, `e1e3_values`; `cancan._roi_means`. In the four 40-train dishes the stitched image is cut by the dish edge at the lower-left. The BL needle, which the notebook takes as e3, sits in a dark, cell-free area (cell 9 overlay: dishes 11, 12, 14 and 9). `_roi_means` drops an ROI only when more than 20% of its pixels are exactly 0, so the e3-end values may come from off-monolayer pixels. The only failing part of fig5a-trains-stronger (trains 864 vs packets 1150 at e3) may be an imaging artefact. Nothing checks ROI coverage.

2. **[affects a conclusion]** Cells 11/12 (`test_rule`, `primary`) and cell 36. Where readings disagree, the notebook adopts `cc.PRIMARY`. The claims file allows that only for "the reading the paper best supports, as an assumption". PRIMARY is a convention of the notebook, not argued from the paper. For fig7b it is the single passing reading among 48 without background subtraction, so adopting it reverses the majority result.

3. **[affects a conclusion]** Cells 33 and 38. Group sizes differ from the Fig. 7 legend (n = 3) and are never commented on. The 2.4 kV small-array group has n = 4 (sub-15, 16, 17, 21; I confirmed in the archive that all four are 2.4 kV). The 4.8 kV large-array group has n = 2 (sub-02, sub-15). This affects fig7a, fig7b and fig7cd. With n = 2, the absence result in fig7cd has almost no power.

4. **[does not affect a conclusion]** Cells 47 and 48. The Protocol 2 and 3 label swap is shown as a "check of the labels". The archive's session descriptions define Protocol2 as "8 phases … without delay" and Protocol3 as "8 phases … with 5us delays", which matches Packets 2 and 3 in Methods 2.3. The notebook does not cite this, and the swap has no support. The outcomes correctly use the files' labels.

5. **[affects a conclusion]** Cell 11, O8. Within-dish comparisons default to unpaired tests, justified by the error-bar rule. That rule is about comparing groups in figures; for centre against periphery within the same dishes, paired is the standard choice. The fig5b void result (paired p = 0.055 under the main reading) depends on this choice. For fig9c the outcome is unaffected.

6. **[does not affect a conclusion]** Cell 36, ANOVA variant. It treats each ROI as an independent observation (701 residual df from 16 dishes). That is pseudoreplication, so its p ≈ 0 is inflated. The variant should not be read as support for the fig7b outcome.

7. **[does not affect a conclusion]** `group_values` and `_trough` (O9). The trough is the minimum of the same mean profile it is then tested against, which biases centre-against-trough tests toward significance. This follows the claims file's definition, and the outcome it bears on, fig6a, fails anyway.

8. **[does not affect a conclusion]** `lowess_profile`. LOESS is fitted to the one-sided profile from 0 to R. That puts the boundary bias of the fit exactly at the centre and the most peripheral ROI, the two points the claims test. Every partial or reproduced outcome also holds on a raw reading, so no verdict depends on it.

9. **[does not affect a conclusion]** `dish_profiles`. Under the reading that uses the mean of the ROIs next to the centre, `centre_b` averages all four half-diagonals even when only one diagonal is selected.

10. **[does not affect a conclusion]** Claims-file gaps, reported and not corrected:
    - fig6a defines no outcome for "rise at all three places, peak tests fail".
    - fig9c's "centre is the highest point of the mean profile" is strict at ROI resolution under noise.
    - The fig8a absolute a.u. ranges assume the paper's intensity scale (MetaMorph) matches the raw uint16 counts, which the paper does not establish.

11. **[does not affect a conclusion]** `UM_PER_PX_FULL = 0.65`. The assumption is reasonable: the measured inner-edge diagonal of the large array is 8.25 mm against the paper's 8.4 mm. The footprint diameter (1.28 mm against 1.5-mm needles) comes from a coarse filter radius, not a measurement.

I tested the helper functions on a synthetic radial image. `dish_profiles`, `corner_names` and `dish_values` give the expected orientations, the 46 ROIs per half, and the expected normalized centre (24.8% against an analytic 24.2%; the difference comes from square ROIs averaging a nonlinear field). `peak_width` returns the correct half-height width and trough distance on a synthetic peak.

## C. What I could not check, and the output that would have allowed it

- **e3 ROIs in the train dishes:** whether they lie on cells. Needed: per-dish crops at each end ROI, and the fraction of ROI pixels below a cell-free threshold.
- **Electrode squares for the 2 and 3 mm dishes:** the needle-mark method is validated only at 0 and 1 mm. Footprint and mark centres differ by 1.2 to 1.6 mm for dishes 06, 09 and 14. Needed: second-channel crops with the fitted circles overlaid, and centre-region profiles under both geometries.
- **Fig. 7 group membership:** why 2.4 kV has n = 4 and large-array 4.8 kV has n = 2. Needed: fig7b and fig7cd re-run with each 2.4 kV dish left out in turn, and per-dish normalized values under the background-subtracted readings.
- **Flat-field tiling:** visible tile shading in the 2.4 kV dishes and the 001027 dishes may bias normalized profiles. No output quantifies it.
- **Figure-only values:** no PDF was supplied, so axis values and the Fig. 7C/D voltages could not be compared.
