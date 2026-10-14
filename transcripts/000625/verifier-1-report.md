**Verifier report, round 1: Geiller, Vancura et al. 2020 (doi:10.1016/j.neuron.2020.09.013) on DANDI 000625 v0.231114.0019**

The paper text is the PMC7736348 author manuscript, saved under `paper/`. The archive was checked through the REST API: version and asset metadata for the three assets.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1-cells-per-mouse | partially_reproduced | Imaged ROIs (231 in files, 228 imaged at least once) fall inside 226.6 ± 27.3. ROIs with a subtype (74 in the six subtypes, 83 not UNIDENTIFIED) fall below the 92.6–149.4 range under both allowed readings (cell 16). |
| fig1-depth-distribution | blocked (data_missing) | No depth or z coordinate is read. The asset metadata lists only one PlaneSegmentation and ImagingPlane per file (see C). |
| fig2c-most-positive | reproduced | Under the six-subtype reading, 0.905 are positive and 0.095 (7/74) negative, inside 0.088–0.108. The all-ROI reading gives 0.035, far outside (cell 18). The result is fragile: 6/74 would fail. Per-session all-ROI fractions (0.065, 0.111, 0.089) are close to 10% but are not the criterion. |
| fig2c-cck-negative | reproduced | 6 of 15 CCKC are negative (0.40, which is ≥ 0.35), against 1 of 59 in the other five subtypes; one-sided Fisher p = 1.7e-4 (cell 21). |
| fig2c-subtypes-differ | reproduced | ANOVA p = 0.0015 (cell 23). The difference is driven by CCKC: Tukey is significant only for PVBC–CCKC and CCKC–IvC/NGFC. Only one of three sessions is significant on its own. |
| fig2c-ngfc-less-modulated | not_reproduced | IvC/NGFC mean r is 0.511 against 0.484 for the pooled four subtypes, the wrong direction; Mann-Whitney p = 0.58 for both r and \|r\| (cell 25). Only session 21324 alone goes the claimed way. |
| fig2d-negative-cells-in-oriens | blocked (data_missing) | No depth or layer per ROI. |
| s2-lags | not_reproduced | The median lag of positive ROIs is −1.67 s, which meets the criterion. But negative ROIs have larger \|lag\| (2.06 s), not smaller; p = 0.60, and every session gives p ≥ 0.82 (cell 27). |
| s2-cck-run-stop | partially_reproduced | CCKC run-stop responses are higher than the other subtypes (Mann-Whitney p ≈ 9e-4 at 3, 5 and 10 s separation). The mean CCKC run-stop response is −0.003, not positive; only the 6 negatively correlated CCKC respond positively (0.084) (cell 29). |
| s3-subtype-classification | blocked (data_missing) | No depth, and one mouse with 74 labelled ROIs. The dF/F and velocity feature sets exist, so a weak cell-wise variant could be run but would not be comparable. |
| fig3-swr-pvbc-vs-somc, fig3-swr-bimodal | blocked (data_missing) | variableMeasured has no ecephys or LFP series. Imaging is at 4.4–5.8 Hz, not the 40 Hz SWR protocol. |
| fig4-fraction-spatial | not_reproduced | 0.010 with the 100% peak rule and 0.698 without it, against 0.175 ± 0.064 (cell 31). Only 1.1% of ROIs have a tuning peak above 1.0 dF/F. The 50% peak variant (0.130) would fall in range but is not an allowed reading. |
| fig4-fraction-negative | not_reproduced | 0.664 against 0.127 ± 0.083 (cells 31, 32). See problem 1. |
| fig4d-decoding | not_reproduced | Holds in 1 of 3 sessions; at least 2 are required. In 21333 the selected subset (25.2 cm) is worse than random subsets (24.8 cm). In 21322 the 6 peak-rule cells give 1.97 times the all-ROI error (cell 34). Where the no-peak rule applies, the "subset" is 55–75% of ROIs, so this barely tests the claim. |
| fig4e-bic-recurrence | blocked (data_missing) | Only 3 BiC are imaged per session (cell 5); the criterion needs 5. |
| fig4f-selectivity-no-difference | reproduced | ANOVA p = 0.17, which is ≥ 0.05 (cell 36). This is a null result with low power. The selection is mostly the no-peak rule, so it covers nearly every subtyped ROI. |
| fig4h-pvbc-more-stable | not_reproduced | PVBC 0.678 (n = 22) against SomC 0.736 (n = 9), the opposite direction; t-test p = 0.42 (cell 38). |
| s6-within-session-order | partially_reproduced | CCKC are the lowest (0.500), as claimed. The highest is SomC (0.606), with PVBC just below (0.598); ANOVA p = 0.56 (cell 40). |
| s6-later-lower-above-chance | partially_reproduced | Across-session r is lower than within-session r for all three pairs (Wilcoxon p ≤ 6.5e-5). Above chance holds only for the same-day pair with all-ROI shuffling (p = 0.047, within-subtype p = 0.10). Both two-day pairs fail (p = 0.075 and 0.53) (cell 42). |
| fig5-context-decorrelation, fig5-novel-context-decrease | blocked (data_missing) | All three asset session descriptions read "Random foraging: session 1 of 4"; there is no novel belt. |
| fig6-reward-somc-bic, fig6-old-zone | blocked (data_missing) | Random-foraging sessions only. The loader reads reward and water epochs but no licking; whether other BehavioralEpochs exist was not shown. |
| fig7-vip-subtypes-immobility, fig7-isi-correlations | blocked (data_missing) | The stored labels (cell 5) contain no VIP, CR, M2R or ISI classes. ISI3 is identifiable in VGAT-Cre mice per the paper, but no such label is present. |

On chance levels:
- The paper gives no numeric chance level for the place-field selection.
- The notebook's surrogate shows the no-peak rule has a false-positive rate of 0.04–0.16 per session. My AR-noise test gave 0.22 positive and 0.20 negative, so the no-peak reading is anti-conservative.
- The decoding chance (52.7 cm, a quarter of the belt) agrees with the shuffled control (49–53 cm).
- For s6, the paper defines chance as shuffling subtype identity, which the within-subtype shuffle implements.

### B. Problems

1. **`place_fields`, cells 31–32** [affects a conclusion]: positive and negative fields are mechanically coupled. On synthetic data, a cell with only a positive field (1.5 in 10 bins) was also flagged as having a negative field, and a cell with only a negative field was flagged positive under the no-peak rule. Out-of-field bins sit below the shuffled 5th percentile because rotated curves spread the field everywhere. This explains why the positive and negative fractions are both about 0.66. The fig4-fraction-negative estimate is therefore not comparable to the paper's 12.7%. The notebook neither reports the overlap of the two sets nor discusses it.
2. **`fit_frame_rate`, cells 8–10** [does not affect a conclusion]: the clock is fitted by maximising the population–speed correlation, and fig2c then tests velocity correlations, which is partly circular. The independent evidence is strong, though: all three sessions come out at about 898 s, and 4.39 Hz falls in the paper's stated 3–5 Hz. Session 21333, which was not refitted, gives a similar per-session negative fraction (0.065).
3. **Cells 18 and 27, averaging over sessions** [affects a conclusion]: averaging r over sessions (the paper's method) cuts the all-ROI negative fraction from 0.065–0.111 per session to 0.035. That is why fig2c passes only under the 74-ROI reading. Lags are averaged across sessions even when the sign of r flips between them.
4. **Cell 34, selection leakage** [does not affect a conclusion]: spatial cells are selected on whole-session data, including the held-out lap. This probably matches the paper and would only flatter the subset, which fails anyway.
5. **Cells 13 and 42, ROI identity** [affects a conclusion]: cross-session identity is assumed. Tuning-curve agreement beats the shuffle only for 21333–21324, and mask area for 21333–21322 has r = −0.05. The s6 "above chance" failure may reflect identity mismatch as much as drift.
6. **Session order, cells 5 and 41** [affects a conclusion]: session IDs run 21322 < 21324 < 21333, but the start times put 21333 two days earlier, and all three files say "session 1 of 4". The notebook does not note this. If the timestamps are wrong, the 1 h and 24 h stand-ins and the "earlier session" in the s6 test change.
7. **`run_events`** [does not affect a conclusion]: it thresholds at 0.2 cm/s on a speed trace derived from sample-and-hold position with noise down to −0.8 cm/s. It behaved correctly on synthetic steps, but on real data brief jitter can create events. Event counts (16–29 per session) look plausible.
8. **`sparsity_index`, cell 36** [does not affect a conclusion]: the formula matches Acharya et al. and my synthetic check (0 for a flat curve, 0.9 for a 10-bin field). The values here (0.01–0.03) are near flat, so the ANOVA mostly compares noise.
9. **Synthetic checks** [does not affect a conclusion]: `velocity_correlation` (lag sign and r), `decode_position` (0 cm on clean tuning, about 51 cm on noise) and `lap_tuning` all behaved correctly.

### C. What I could not check

- **Depth and coordinates (fig1, fig2d, s3).** I could not confirm from the REST API that no depth or z coordinate exists, for example a z field in `pixel_mask`, ImagingPlane `origin_coords` or `grid_spacing`, or per-ROI offsets in the cropped image series. Adding output that lists the PlaneSegmentation columns, the `pixel_mask` dtype fields and the ImagingPlane attributes would settle it.
- **Behavioural series (fig6).** I could not check whether licking or other series exist. A printed tree of `processing/behavior` and `acquisition` for each file would settle it.
- **Spatial selection (fig4).** I could not count the ROIs flagged both positive and negative. Their fraction per session, plus a variant that excludes them, would show how much of fig4-fraction-negative is the coupling artifact.
- **Run-stop responses (s2-cck-run-stop).** Per-session CCKC run-stop means are not printed. They would show whether the near-zero average hides a session-dependent sign.
- **Velocity correlations (fig2c).** A per-ROI table of r in each session for the subtyped ROIs would show how many cells flip sign between sessions.
- **Session order.** The ID versus start-time conflict cannot be resolved from the files or the API. Only an output of any other acquisition timestamps in the files (raw image series `starting_time`, file `create_date`) would help.
- **Frame-rate fit.** The score-curve figure is only an image. A printed second-best peak would show whether the fitted rate is unique.
