**A. Outcomes per claim**

The claims file has 18 claims. The notebook tests 3 and reports the other 15 as blocked.

| Claim | Outcome | Reason |
|---|---|---|
| fig4-unipolar-strongest | blocked (data_missing) | The archive API lists 10 assets at 0.240605.1859, each a single stitched monolayer image (cell 3). There is no single-cell time-lapse. |
| fig4-bipolar-weaker | blocked (data_missing) | Same as above. |
| fig4-sham-no-uptake | blocked (data_missing) | Same as above. |
| fig4-twenty-fold-cancellation | blocked (data_missing) | Same as above. |
| fig5a-trains-stronger-throughout | blocked (data_missing) | The files have no trains, no 40-packet and no 1Px40 conditions. Every description says 1Px4 at 4 kV (cell 3). |
| fig5a-packet-center-peak-e1-stronger | blocked (data_missing) | Same as above. |
| fig5bc-rotation-focuses-center | blocked (data_missing) | Same as above. |
| fig6a-more-packets-more-uptake | blocked (data_missing) | There are no 5Px4 or 10Px4 dishes. |
| fig6b-center-to-periphery-by-number | blocked (data_missing) | There are no 5Px4 or 10Px4 dishes. Only the 1Px4 value could be compared, and only by assuming Fig. 6 used these 4-kV small-array dishes (see C). |
| fig6-peak-narrower | blocked (data_missing) | Needs three packet numbers; the files have one. |
| fig7a-amplitude-scales-uniformly | blocked (data_missing) | Every file is at 4.0 kV (cell 3). |
| fig7bd-targeting-independent-of-amplitude | blocked (data_missing) | Same as above. |
| array-size-independence | blocked (data_missing) | One amplitude and one array (the small one, cell 7–8). |
| fig9-gap-fades-periphery-faster | blocked (data_missing) | There is no gap condition and no large array. |
| fig9b-gap-boosts-targeting | blocked (data_missing) | Same as above. |
| fig8a-equal-center-uptake | not_reproduced | Main reading: Packet 1 = 649 a.u., Packet 2 = 389, Packet 3 = 383. Packet 1 vs 2 gives p = 4e-4, and Packet 1 differs from both others at p < 0.05 in all 48 readings (largest p: 0.047 and 0.026). Packet 1 is also outside 193.5–258.5 a.u. even after background subtraction (333–381). |
| fig8a-more-uptake-near-electrodes | not_reproduced | Packet 3 is *below* Packet 2 near the electrodes in 48 of 48 readings (t for 3 vs 2 runs from −5.3 to −1.8). Packet 2 is 217–575 a.u., never in 108–132. |
| fig8b-packet2-best-targeting | not_reproduced | Main reading: Packet 1 = 81%, Packet 2 = 83%, Packet 3 = 129%. Packet 3 is the highest in 96 of 96 readings and Packet 2 never exceeds 124%, so even the partial condition fails. |

**B. Problems**

1. [does not affect a conclusion] The files labelled Protocol 3 behave like the paper's Packet 2, and the reverse (cells 22–24 and the profile figure in cell 14). With the two labels swapped, fig8b becomes partially reproduced in 92 of 96 readings and reproduced in 2. The labels look internally consistent, though: each session description defines Protocol 2 as 8 phases without delay and Protocol 3 as 8 phases with 5-µs delays, which matches the paper. So testing the data as labelled is correct, and the variant rightly decides nothing. Still, a possible mislabelling in the deposit should be stated as unresolved, not ignored.
2. [does not affect a conclusion] Imaging-day confound (cells 9–10, 17). The three Packet 1 dishes were imaged on 24 March, with about twice the in-footprint intensity of the 17–18 March dishes. A gain or exposure difference would be multiplicative, so subtracting a background does not remove it. On the center/background ratio (cell 17, not a reading the claims file defines), Packet 1 vs 2 gives p = 0.27, while Packet 1 vs 3 gives p = 0.047. The claims file judges a.u. "as they are", and the fig8a-more-uptake and fig8b failures do not involve Packet 1 at all, so the outcomes stand. But the fig8a-equal-center failure rests largely on a between-day difference, and that should be said.
3. [does not affect a conclusion] `dish_readings`, `near_outcome`, `pct_outcome`: the claims file's reading (b), "the ROI closest to e1", was not run because e1 is not recorded. It could have been run with each electrode in turn as e1. I checked it from the cell 20 output instead. The worst case for the claim is to take the lowest electrode end in each Packet 2 dish and the highest in each Packet 3 dish. That still gives Packet 2 a mean of 363.7 a.u. against 358.1 for Packet 3, and the Packet 3 center (about 383) stays above every Packet 3 end mean. So no choice of e1 gives Packet 3 > Packet 2 or a Packet 3 normalized center below 100%.
4. [does not affect a conclusion] `background`: the background is the median inside each needle footprint. These are not cell-free areas; the panels in cell 11 show texture there. It is stated as an assumption and is the only option available. Every background reading fails the same way.
5. [does not affect a conclusion] `UM_PER_PX = 0.65` is an assumption. It is supported by the tile pitch (about 1840 px ≈ 0.9 × 2048) and by the edge-to-edge diagonals fitting the ±1.65-mm span. The scale-free `rel` geometry gives the same outcomes.
6. [does not affect a conclusion] With `roi_at_zero`, 47 ROIs at the same step put the outermost ROI centers at ±1.65 mm, so the ROI edges reach about half a step past the stated span. This is minor.
7. [does not affect a conclusion] Dish 10 has different metadata: no device, `resolution` 1.0, and a different day. It is kept without comment on its effect, but all three Protocol 3 dishes are at 125–137% (raw), so dropping it changes nothing.
8. Helper checks on synthetic inputs. On a synthetic image (four dark disks, a known radial-plus-linear intensity), `find_electrodes` recovered the centers and radius within 0.1 block and `profiles` matched the analytic values within 1.3 a.u. `summary_values` puts the ends in electrode order 0, 2, 1, 3, and `background` returned the disk level. The criteria's tolerance bounds in cells 16, 19 and 22 match the claims file. The t-test is Student's (equal variances), two-sided, as the criteria say.
9. Claims-file reading. I agree with its reading of "~120 a.u. for packet 1" as Packet 2; the paper's Fig. 8B and 183% figure support it. I found no misreading of the paper that bears on the tested claims.

**C. What I could not check**

- **The blocked claims, checked against the archive.** I queried the archive myself. Version 0.240605.1859 (also the draft) has exactly 10 assets, 3,667,103,151 bytes, and is described as protocols at 4 kV, applied once from each electrode. So the 15 claims are blocked within this dataset.
  - Searching the archive for "CANCAN" also finds other dandisets from the same group whose titles look like Figs. 6, 7 and 9: 000875 (number of packets), 001025 (voltage and array sizes), 001028 (3D) and 000686. Those claims may be testable outside the dataset the claims file names. That is a scoping question for the registry, not something this notebook could do.
  - fig6b's 1Px4 value could be checked against these dishes only if Fig. 6 used 4 kV and the small array, which the paper does not state.
- **Per-dish profiles.** The notebook shows only per-dish center and end values and group means. A per-dish profile plot under the main reading, raw and background-subtracted, would show whether the Protocol 2 and 3 difference holds in every dish or comes from one.
- **Electrode identity across dishes.** E0–E3 are assigned by angle in the image, not by physical identity. An output naming the pulse order or the physical electrode would allow reading (b) to be run properly.
- **Gain and exposure.** The files hold no camera settings, so the between-day intensity difference cannot be resolved. An image region without cells would have given a proper background.
