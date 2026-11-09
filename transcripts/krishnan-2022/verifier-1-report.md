**Verifier report, round 1: Krishnan et al. 2022 on DANDI:000462 (0.230416.2132)**

The claims file has 41 claims. The notebook tests 31 and blocks 10. The archive API confirms 14 assets: 10 wild-type mice (5 ran R-UR-RR-Novel, 5 ran R-UR) and 4 DAT-Cre hM4D(Gi) mice. Every count below therefore uses 10 of the paper's 12 wild-type mice, 5 of its 6 RR/Novel mice and 4 of its 6 DREADD mice.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| session-lap-counts | reproduced | Cell 9, complete laps: R 35.3, UR 29.7, RR 28.2, Novel 32.8. All are within tolerance. |
| lick-persistence-ur | not_reproduced | Cell 11: RE high laps per mouse average 6.6 / 7.6 / 8.6 under L1–L3, against 5 ± 1. Reading (a) gives 4 random lickers, but the mean condition fails. |
| fig1d-decoder-drop-ur | reproduced | Cell 15, Methods decoder: holds in 8 of 10 mice under every lick-stop reading. That is 80%, above the 9 of 12 (75%) the criterion fixes. Only 10 mice exist, and the notebook does not say how it scales the threshold. |
| fig1e-decoder-follows-licking | reproduced | Cell 17: fit r 0.979 and fit R² 0.959 (paper 0.94 ± 0.094). Maximum change at lap 11.23, rounded to 11 (10 ± 1). The lick minimum is at lap 14, exactly 3 laps away, the edge of the allowed window. |
| fig1f-decoder-r2 | partially_reproduced | Cell 13, main reading, L1/L2: all four means are within tolerance and R vs RE low is significant. But R vs RE high is significant (p = 0.0047; 0.028 Bonferroni) under every decoder and reading, against the paper's "similar". R vs RR is significant only uncorrected (0.035; 0.21 Bonferroni). |
| fig1g-decoder-error-all-locations | reproduced | Cell 19: RE low error is higher than R at p < 0.01 in start, middle and end, under every decoder and reading. |
| supp4-lickstop-definition-robust | reproduced | Cell 21, "first" start reading: all four judged definitions are significant with Bonferroni ×5. Median RE high is 0.91 and median RE low 0.66–0.67, both in range. Median R is 0.976 and median RR 0.842, both within tolerance. |
| supp4-lapwise-r2 | partially_reproduced | Cell 23: all means are within their SD tolerances. No lick-stop reading puts all lap counts in tolerance. RR has 141 laps from 5 mice against the paper's 121 from 6, which the missing mice cannot explain. |
| supp2-decoder-stable-control | blocked (data_missing) | The archive has no time-control mice. |
| supp5-not-running-speed | partially_reproduced | Cell 25: median R² values (0.985 / 0.763 / 0.695) are within tolerance, and the Wilcoxon p is 0.006. Matched lap counts (172 or 203 against 233) and lap times (12.2 s, or 8.5 s from the code variant, against 7.34 s) miss. |
| approach-ratio | not_reproduced | Cell 27: R ratio is 5.17 (whole lap), 2.21 (traversal) or 1.26 (code variant, traversal), against 1.30 ± 0.02. UR is 1.199 at best, against 1.22 ± 0.02. The dark sessions are not in the archive. |
| engaged-lap-counts | blocked (other) | The engaged/disengaged split is an artefact (problems 1–2). The lick-stop-only part also misses: RE high is 66 and 76 laps under L1/L2, against 90 ± 9. |
| supp6b-decoder-engaged-laps | blocked (other) | Cell 31 meets the criterion numerically, but on the invalid engagement split. The archive supports a valid rerun. |
| disengaged-laps-uniform | blocked (other) | Cell 33 gives p ≥ 0.05 for both tests. For a claim of absence, a split driven largely by NaN laps is no evidence. |
| supp6-pupil-engagement | blocked (data_missing) | API asset metadata lists only ProcessingModule, OpticalChannel and ImagingPlane; there are no pupil assets. |
| fig2a-pv-cluster-transition | reproduced | Cell 55: holds in 2 of 3 mice under L1 and L2. Laps are filtered by the flawed engagement split. |
| fig2c-spatial-correlation-drop | partially_reproduced | Cell 37, reading S2: RE low 0.566 against within-R 0.872 (p ≈ 1e-64); RR 0.708 lies between and is above RE low (p ≈ 1e-17). Reading S1 cannot be run because the control mice are absent, and the criterion requires S1 and S2 to agree. |
| fig2d-remapping-all-locations | partially_reproduced | Cell 39: 3 of 3 position groups at p < 0.01 under S2; S1 cannot be run. |
| fig2e-place-field-fates | not_reproduced | Cell 49: F1–F3 all disagree with the paper (2 of 11 values at most). For example, R fields lost in RE low are 80.8% against 41.2%. |
| fig3a-field-numbers-similar | not_reproduced | Cell 41: R 608 and RR 631 are within tolerance; RE low engaged is 265 against 663 ± 66. |
| fig3b-reliability | reproduced | Cell 43: per-mouse means 0.556 / 0.321 / 0.493 are within tolerance, and RE low is below R. |
| fig3b-out-in-ratio | reproduced | Only L2 per-mouse passes: RE low 0.120, exactly at the tolerance bound of 0.12. L1 and L3 give 0.119 and fail. |
| fig3b-width-intensity | not_reproduced | Width is about 94–97 cm against 53 / 61 / 54 cm under every reading. |
| fig3c-degradation-all-locations | partially_reproduced | Cell 45: reliability holds in 3 of 3 groups; out/in fails at the start (KS p = 0.02). |
| supp11-all-mice-parameters | not_reproduced | Cell 47: 0 of 12 (reading a) and 3 of 12 (reading b) medians within 10%. The directions hold. |
| fig3d-reward-overrepresentation | not_reproduced | Cell 53: NR23's R end-minus-middle is −4.2, and RE low is not below R in all mice and has a positive mean. The Gaussian fits match. |
| reward-zone-field-turnover | not_reproduced | Cell 51: lost end fields are 173–182 against 104; new RE low fields per bin are 30–45 against 62–83. |
| controls-no-change-over-time | blocked (data_missing) | The archive has no control mice. |
| supp13-novel-environment | partially_reproduced | Cell 57: 2 of 4 hold (decoder R², reliability). Pre-licking (p = 0.38) and out/in fail. |
| supp14-reward-cells | blocked (methods_underspecified) | The block is defensible for the count of 43. Part is testable, though: R and Novel exist for 5 mice, and Supplementary Fig. 14a defines on-track reward cells by field COM near reward, which the notebook's fields could have used. |
| supp16-dreadd-running-speed | not_reproduced | Cell 61: 0 of 6 means within tolerance (about 26 against 42 cm/s), although DCZ and CNO slow running and saline does not. |
| fig4f-dreadd-spatial-correlation | partially_reproduced | Cell 63: the overall and per-position patterns all hold. Place-cell counts (610 / 676 / 842 / 641) are all outside tolerance. |
| supp18-saline-slow-laps | not_reproduced | Cell 65: speeds and reliability are outside tolerance, and the split drop (0.207) exceeds half the DCZ drop. |
| fig4h-dreadd-reliability-outin | not_reproduced | Cell 67: saline out/in changes, p = 0.013 per mouse and p = 8e-8 on cumulative-histogram bins (both pairings agree). Per-mouse CNO reliability does not fall. |
| fig4m-dreadd-overrepresentation | reproduced | Cell 69: DCZ change (2.1) is below saline (4.3), p = 0.40, and the RE low change is larger in size than the DCZ change. The test uses n = 4, and CNO goes the wrong way (5.8), which the criterion does not judge. |
| supp15-tdtomato-controls | blocked (data_missing) | The 4 DREADD files are described as hM4D(Gi) mice; no tdTomato mice appear. |
| fig5-da-axon-ramps | blocked (data_missing) | There are no axon-imaging assets. |
| fig5k-ramp-slope-max | blocked (data_missing) | There are no axon-imaging assets. |
| fig5l-ramps-return-rr | blocked (data_missing) | There are no axon-imaging assets. |
| supp20-novel-axons | blocked (data_missing) | There are no axon-imaging assets. |
| supp21-heterogeneous-axons | blocked (data_missing) | There are no axon-imaging assets. |

Totals: 9 reproduced, 8 partially reproduced, 11 not reproduced, 13 blocked (10 for data or methods, 3 "other" because of the engagement bug). The paper states no chance level for any selection; the 10 s label-shift control in cell 6 is the only reference.

### B. Problems

1. **[affects a conclusion]** The main approach-ratio reading includes the end-of-lap pause (`binned_lap_velocity` / `approach_ratio`, `traversal=False`). The Methods compute velocity "at each point along the 2 m track", and the paper's dark ratio of 1.01 is impossible if a stationary pause is included.
   - On a synthetic lap with a true ratio of 2.0 and a 1.5 s pause, the helper returns 2.40.
   - On the real data, R ratios range up to 64.9 and UR up to 150.7, and 73 of 352 R laps and 76 of 297 UR laps are NaN (cell 27).
2. **[affects a conclusion]** `behaviour_summary` classifies laps with `ratios >= thr`, so a NaN-ratio lap counts as disengaged. The threshold (mean − 1.5 SD) is negative in 5 of 10 mice because of the outliers. In those mice no finite ratio (minimum −0.23) falls below the threshold, so at least 36 of the 68 disengaged laps under L1 are NaN laps (cell 29). This split feeds:
   - engaged-lap-counts, supp6b and disengaged-laps-uniform;
   - the selection of the 3 mice with more than 12 engaged laps (`FIG23`); under the traversal reading NR21 would have only 2 engaged laps;
   - every "RE low engaged" place-field analysis.

   The traversal variant was computed but no downstream analysis was rerun with it.
3. **[affects a conclusion]** `reward_zone_start` does not limit the first lick to before reward delivery, so consumption licks set the zone. The zone starts at 185–198 cm in 8 of 10 mice. This drives the lick stop, and so every RE high / RE low split, and the pre-licking measure in supp13. The code variant zone is 0 cm in every mouse (post-teleport licks fill bin 0), so it is not a working alternative.
4. **[affects a conclusion]** Every speed and time measure is about 1.65 times slower than the paper's, in both datasets: wild-type R lap time 12.2 s against 7.34 s, DREADD lap speed 26 against 42.7. The volts-to-cm rule (99.9th percentile = 200 cm) and the 30 Hz behaviour clock were never checked against an independent quantity such as the 1.5 s reward pause. Affects supp5, supp16 and supp18 (cells 25, 61, 65).
5. **[affects a conclusion]** fig2c and fig2d: the criterion requires readings S1 and S2 to agree, and S1 cannot be run. The notebook does not state that this leaves the claims undecided under the claims-file rule.
6. **[affects a conclusion]** fig1d (cell 15): the 9-of-12 rule was applied to 10 mice without stating how it scales.
7. **[does not affect a conclusion]** Four mice receive a reward at the end of their first UR lap (cell 5). This may put an R lap into UR and inflate RE high by 1 lap in those mice. The lick-persistence mean would still be at least 6.2.
8. **[does not affect a conclusion]** supp18: the pooled-percentile reading the criterion requires was not run. Also, the split correlation uses fields defined on 11–19 fast laps, against all laps for the saline pair, which lowers r. Speeds and reliability fail regardless.
9. **[does not affect a conclusion]** supp13 `block_params`: out/in under the "session fields" reading reaches 0.4–1.05, out of scale with every other value. Both readings fail the out/in test anyway.
10. **[does not affect a conclusion]** Claims-file readings, reported not corrected:
    - lick-persistence-ur: the "first no-lick lap" index from cell 11 averages 4.8 laps, matching 5 ± 1. That reading is not listed, and the paper's own 90 RE high laps over 12 mice (7.5 per mouse) is inconsistent with 5 ± 1.
    - fig4m: the criterion tests DCZ only, although the statement covers CNO as well.

### C. What I could not check

- **The 1.65× speed and time discrepancy (problem 4).** I could not tell whether it comes from the data or the definitions. Needed: the duration in frames of the end pause after reward, and the interval between consecutive rewards.
- **The reward-zone start (problem 3).** Needed: each R lap's first-lick position plotted against reward-delivery time.
- **The NaN ratios (problems 1–2).** Needed: NaN ratio counts per mouse and condition, and the speed trace across a teleport.
- **Whether the engagement-dependent claims survive a valid split.** Needed: cells 29–55 rerun with the traversal (or code-variant) ratio, NaN laps excluded rather than counted as disengaged.
- **Whether any file holds pupil or other data.** The notebook never lists the HDF5 groups or the NWB processing-module contents, and I did not stream the files.
- **Whether any of the 4 DREADD files is a tdTomato control.** The subject descriptions are truncated at 40 characters in cell 4, and the dandiset description says "DREADD … and controls".
- **The paper's code.** The repository is not here, so I could not confirm which laps `plot_shuffleerror_withlickstop` draws from.
- **dF/F, transients and place-field quality.** Needed: example traces with their transient masks, and per-field maps. Widths near 95 cm suggest that keeping whole transients plus the "mean > 0" extent rule widens fields.
