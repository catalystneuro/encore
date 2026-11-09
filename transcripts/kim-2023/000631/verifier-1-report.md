**Verifier report, round 1: Kim et al. 2023 (doi:10.3390/ijms241310921) on DANDI:000631 v0.231012.1508**

The claims file has 12 claims. The notebook tests 6: five on Figure 2 and one on Figure 4. It treats 6 as blocked: four on Figure 3 and two on Figure 5.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig2-180-cancellation | partially_reproduced | Under background (b), no ROI layout gives both values (cell 21). Layout L2 gives 18.5 / 22.0-fold at 833 kHz (holds), but 2.42–2.51-fold at 1 Hz, outside 2 ± 0.2. Layout L1 gives 1.92 / 2.19-fold at 1 Hz (holds), but only about 11-fold at 833 kHz. Cancellation at 180°, and stronger cancellation at 833 kHz, are clear under every reading. |
| fig2-crossover-angle | reproduced | Cell 24: 1 Hz crosses at 145.3–149.6° (tolerance 144–176) and 833 kHz at 125.3–125.9° (117–143), under every layout, angle model and normalisation. The 1 Hz value is fragile; see problem 4. |
| fig2-facilitation-plateau | partially_reproduced | At 833 kHz with layout L2, the level is 2.58–2.96, reached at 94.5–96°, and the plateau holds (cell 26). At 1 Hz the 90–100° level is only 1.15–1.36-fold. The 1 Hz slope below 90° is significantly non-zero under every reading, and uptake keeps rising to about 3-fold near 0°, so there is no plateau. The criterion needs both frequencies. |
| fig2-frequency-dependence | reproduced | Cell 28: all conditions met in all 16 readings. The 180° value is lower at 833 kHz (4.5–8.9% against 40–52% at 1 Hz), the crossover angle is smaller (125° against 145–150°), and the curves are above 100% at the smallest angle and below 100% at the largest. |
| fig2-60-fold-co-counter | reproduced (low confidence) | Under background (b) with layout L2, plateau level ÷ lowest-ROI value gives 54.8 / 61.6 (level2) and 56.8 (level1, norm ii), inside 60 ± 6 (cell 30). Layout L1 gives at most 34.5 and fails. I take L2 as the reading that decides, because L1 never reaches 180°: its largest angle is about 170° (cell 11), while the paper puts 180° at the base. The ratio rests on a denominator of about 5% of control and is very sensitive to the background estimate (problem 1). |
| fig4-unipolar-pattern | reproduced | Cell 32: all 8 readings agree. In 3 of 3 paired dishes the apex is above both bases, and in 3 of 3 single dishes the energised base is above the apex. In the single dishes both bases exceed the apex, so which base is taken as energised does not matter. Field-map Spearman ρ is 0.50, 0.96 and 0.93 for single dishes, and negative for paired dishes (cell 33). |
| fig3-1hz-co-equals-cross | blocked (data_missing) | I checked the archive: all 15 assets are triangular-array YP/MemBrite images from the Figure 2 experiment (1 Hz / 833 kHz, BP/UP). There is no square-array data. |
| fig3-770khz-co-enhanced | blocked (data_missing) | Same as above; no 770 kHz files. |
| fig3-770khz-cross-same-as-1hz | blocked (data_missing) | Same as above. |
| fig3-no-area-dependence | blocked (data_missing) | The claims file judges it by fig3-1hz-co-equals-cross, which is blocked. The Figure 2 plateau result does not decide it. |
| fig5-base-sawtooth | blocked (data_missing) | No FluoVolt strobe or CHO-K1 files in the archive. All 15 assets are single stitched 2-channel images with no time series. |
| fig5-apex-larger-polarization | blocked (data_missing) | Same as above. |

### B. Problems

1. **[affects a conclusion]** Background estimate, `swing.footprint_background` / `FOOTPRINT_BG_MM = 0.5`.
   - Methods 4.4 says the footprint cells were "shielded from the field". The needles are hollow, with a 0.5 mm inner diameter, so the shielded lumen has a radius of 0.25 mm.
   - The 0.5 mm disk the notebook uses is about 75% steel-wall annulus by area, where the needle tip sits on the glass. That is not clearly the shielded cells.
   - The fold values are extremely sensitive to this number. From cell 18 at 833 kHz near 180°, paired YP is only about 25 counts above a background of about 215, against about 570 counts for the controls. A 10-count shift in background moves the 20-fold value to roughly 16 or 36, and moves the 60-fold ratio with it.
   - The paper's 1 Hz 2-fold sits between the (a) and (b) readings (1.3–1.5 and 2.4–2.5).
   - No sensitivity run was done, using the lumen only or other radii. This affects fig2-180, fig2-60-fold and the plateau levels.
2. **[affects a conclusion]** ROI layout, cells 16–30 and `roi_centres`.
   - The claims-file layout (32 contiguous ROIs from the base midpoint, outside the footprints) cannot fit: it spans 6.4 mm, but the midpoint-to-apex-footprint distance is 5.37 mm (cell 9). This is not stated as a deviation from the claims file.
   - The two substitutes give different outcomes for fig2-60-fold (`combine` output in cell 30: L1 not met, L2 met). No printed rule says which layout decides.
   - L1 overlaps ROIs by about 15% and never reaches 180°, which argues against it. That argument is mine, not the notebook's.
3. **[affects a conclusion, fig2-180 and fig2-60]** Selection bias. Reading (2), "ROI of lowest mean", takes a minimum over 32 noisy ROIs. This biases the fold upward, and it is the only route by which 833 kHz reaches 20 ± 2 (reading 1 gives 11.8–12.7) and 60 ± 6. The claims file permits this reading; the bias is not discussed.
4. **[does not affect a conclusion]** The 1 Hz crossover rests on one ROI. In cell 18 (L2), ROI 11 at 147.8° is 108%, while ROIs 12–14 fall back to 79–93%. Without that ROI the crossover would be about 128°, outside the tolerance. Also, the 8-9-21-only controls give 130.5° under normalisation (ii) (cell 24). The criterion is still met as written.
5. **[does not affect a conclusion]** In `plateau_measures` (cell 26), P2 needs ROIs below 10°. Model C has none (smallest angle about 22°), so P2 is automatically False. This creates a spurious disagreement between angle models B and C at 833 kHz. It should be reported as untestable, not "not met".
6. **[does not affect a conclusion]** Plateau level1, "between 90 and 100°", contains a single ROI (94.3° or 94.5°) under L2. It is a one-ROI estimate, not a mean.
7. **[does not affect a conclusion]** Some choices are made without the paper specifying them:
   - Which 1 Hz controls count toward n: all 5 unique dishes from two days are used, while the paper gives n = 3 for paired dishes only.
   - The 833 kHz controls were imaged on a different day with a larger mosaic. Normalisation therefore assumes the same exposure and gain across days, which is never checked.
   - Variants are shown for the control subsets.
8. **[does not affect a conclusion]** Checks that were sound:
   - The duplicate file (7-31-21 BPAE-03/18) was correctly dropped.
   - The mislabelled 833 kHz BPAE-13 is used, with an exclusion variant.
   - The pixel-size assumption of 0.65 µm is supported by the measured footprint radius (0.72 mm) and the field range (5–10 kV/cm at 4 kV).
   - I tested `crossover`, `at_180`, `normalised`, `square_mean`, `field_line_sources` and `GridModel` on synthetic inputs. They behave correctly, and models B and C agree to within about 1° away from the apex.

### C. What I could not check

- **Background sensitivity.** Needed: the radial YP profile inside each footprint (rings at r < 0.25 mm and 0.25–0.5 mm) and the fig2-180 / fig2-60 values recomputed with a lumen-only background.
- **Cross-day intensity comparability.** Needed: the exposure and gain metadata, which the files lack, or at least the MemBrite and unexposed-region YP levels compared per day.
- **Saturation inside ROIs.** Needed: the fraction of pixels at or above 60000 within the bisector and adjacent ROIs, before block averaging.
- **Which layout the paper used.** Needed: the paper's Figure 7B, which was not available, or the notebook printing the angle at the base midpoint and the position of the 180° point relative to the base line.
- **Pairing of control and paired ROIs.** Needed: a per-dish table of the ROI-0 to ROI-5 values for paired and control dishes, to see whether the 833 kHz denominator is driven by one dish. Per-dish values are shown only for the largest-angle ROI (cell 22: 5.8–9.0%).
