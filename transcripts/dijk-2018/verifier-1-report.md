**Verifier report, round 1: van Dijk & Fenton 2018 on CRCNS hc-17**

The claims file has 44 claims. The notebook tests 40 and treats 4 as blocked. My outcomes: 22 reproduced, 4 partially reproduced, 14 not reproduced, 4 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1-single-field-proportion | not_reproduced | CA single-field share is 45–55% under all four readings (needs 75 ± 7.5) (cell 14). DG is within tolerance only at M2b/M5a (62.2%). Rests on M5 (see B1). |
| fig1-field-number-scaling | not_reproduced | No reading gets the means: DG circular 0.71–1.20 against 1.48, DG removed 0.74–1.47 against 2.70 (cell 16). Rests on M5. |
| fig1b-stability-dg-below-ca-removal | reproduced | Region p = 0.0036 (CA 0.42 > DG 0.31). Manipulation p = 0.0001. Interaction p = 0.76. Fisher's LSD puts removal below replication and relocation (p ≤ 0.0002). The other M2 reading agrees (cell 19). |
| fig1-rate-remapping-no-difference | reproduced | Absolute ratio: region p = 0.54, manipulation p = 0.59, interaction p = 0.70 (cell 21). The signed variant has an interaction (p = 0.034), but the sign depends on an arbitrary session order. |
| fig1c-field-rate-change-no-difference | reproduced | All p ≥ 0.30 for both M5 masks, raw and log (cell 23). Only 120 or 149 values against the 170 the paper's df imply. Rests on M5. |
| tables1-dg-ca-similar | partially_reproduced | No property differs (all p ≥ 0.19) and both firing rates are within tolerance. Coherence is outside tolerance (DG 0.54 vs 0.46 ± 0.06, CA 0.63 vs 0.51 ± 0.08). Information in bits/s is outside (0.83 vs 1.31); see B7 (cell 25). |
| fig2c-cfos-reduced | blocked (data_missing) | No optogenetic or cFos data in the archive (section C). |
| fig2d-conflict-deficit | blocked (data_missing) | Same. |
| fig2-quadrant-preference | blocked (data_missing) | Same. |
| fig2e-shock-off-deficit | blocked (data_missing) | Same. |
| fig3b-avoidance-learning | not_reproduced | Under the reading the df support (multivariate, F(2,4)), F = 5.70, p = 0.067; the paper has 18.2, p = 0.01 (cell 44). The univariate F(2,10) gives p = 0.038, but its df do not fit 6 mice. Also see B4. |
| fig3b-shock-off-avoidance | not_reproduced | Shock status is significant for errors (mixed model p = 0.0001) and errors per meter (p = 0.004). Errors per meter also has an interaction (p = 0.024) (cell 46). Caveats in B4 and B5. |
| speed-no-difference | reproduced | Training 1, training 2, conflict, shock-off sessions: F(2,13) = 1.94, p = 0.18. This matches the paper's F2,13 = 1.93 exactly (cell 48). |
| tables2-firing-quality-similar | not_reproduced | Room coherence differs (p = 0.011), as do arena field counts (p = 0.002). Room information in bits/s is outside tolerance (cell 30). |
| fig3c-stability-no-difference | reproduced | Kruskal-Wallis p = 0.093 (M11a) and p = 0.17 (M11b) (cell 32). |
| fig3c-replication-vs-relocation | reproduced | Rank-sum p = 0.051 (M11a, borderline) and p = 0.14 (M11b) (cell 34). |
| fig3c-stability-vs-environment | reproduced | Against environment DG: p ≥ 0.42. Against environment CA: p ≤ 0.008, CA higher. Holds in all four reading combinations (cell 36). |
| fig3d-rate-remapping-task | partially_reproduced | Whole-cell part holds under M11b: H p = 0.0025, addition and relocation above replication, no difference between them. The field part fails under every reading run (p = 0.089 to 0.61), on only 13–15 cells per group (cell 38). |
| interneuron-rate-remapping | not_reproduced | p = 0.72 (M11a) and p = 0.27 (M11b) (cell 40). |
| ipos-speed-correlation | not_reproduced | r² is 0.10%, 0.19%, 0.55% and 1.08% across the four readings; none is within 0.69 ± 0.069% (cell 82). |
| fig4b-room-preference-pretraining | reproduced | 8-px location: interaction p = 0.0046 (0.0066 with the paper's df). Room > arena in pretraining (p = 0.023), no difference in training or conflict. At 16 px the interaction is p = 0.058 (cell 84). |
| fig4c-ipos-before-avoidance | reproduced | The criterion is met in all 12 variants (interaction p ≤ 0.0001) (cell 86). |
| fig4d-room-maps-uncorrelated | reproduced | Adopted 8-px reading: r = 0.068, p = 0.076. Fragile: at 16 px, r = 0.16, p < 0.001 (cell 88). |
| fig4d-room-ipos-near-active-zone | partially_reproduced | Training zone holds: p < 0.0001 and training highest in post hoc tests (p ≤ 0.003). Conflict zone: the ANOVA is significant (p ≈ 0.03) and conflict has the highest mean, but the post hoc tests are not significant (p = 0.08–0.17) (cell 90; B3). |
| figs2a-pc-pairs-no-change | reproduced | Tau p = 0.75; change p = 0.67 (M11a) and 0.43 (M11b) (cell 52). |
| standardized-rates-no-difference | reproduced | Reading (a): p = 0.08. Reading (b) is broken, with only 14 conflict passes (cell 94). |
| overdispersion-similar | reproduced | Variances 5.28, 5.34 and 5.72, all within tolerance. F tests p = 0.77 and 0.078; per-cell ANOVA p = 0.97 (cell 96, reading a). |
| network-consistency-overall | reproduced | Mean NC is positive in every condition (0.042–0.061) and p = 0.49 (cell 99, reading a). That reading's "overlap" is loose: 9,079 values against the paper's 2,526. |
| fig5b-network-consistency-zones | not_reproduced | Interaction p = 0.48 under reading (a); reading (b) has no conflict passes (cell 100). |
| fig5d1-pc-int-tau-no-difference | reproduced | H p = 0.50, n = 438, matching the paper's df (cell 54). |
| fig5d2-pc-int-change-relocation | reproduced | M11b: F(2,425) = 7.63, p = 0.0006; LSD puts relocation above replication (p = 0.0002) and addition (p = 0.004). Under M11a it fails on relocation vs addition (cell 56). |
| pc-int-fraction-increased | partially_reproduced | M11b with the > 0 threshold gives 78.4%, 76.2% and 91.7%, all within tolerance. But relocation vs replication is z = 1.59, p = 0.11, where the criterion needs p < 0.05 (cell 58). |
| figs2bc-other-timescales | reproduced | M11b: tau p = 0.77 and 0.48; change p = 0.031 (20 ms) and < 0.0001 (250 ms), relocation highest. Under M11a the 20-ms change test fails (p = 0.058) (cell 60). |
| pc-int-pair-classes | not_reproduced | No reading gets positive pairs within 81 ± 8.1; the closest is 71 (cell 62). |
| fig5d3-independent-pairs-increase | reproduced | Relocation highest with p < 0.05 under several class and M11 readings, e.g. (a)(i) M11a p = 0.0025 and (a)(iii) M11b p = 0.015 (cell 64). The classes themselves do not match the paper's counts. |
| fig5d4-positive-pairs-decrease | reproduced | (a)(iii): H p ≤ 0.0004. Replication and addition medians below zero (signed-rank p ≤ 0.0001); relocation not different from zero (p = 0.27 / 0.69) (cell 64). |
| negative-pairs-no-change | not_reproduced | p < 0.05 in 6 of the 8 class × M11 combinations; only class reading (b)(i) gives p ≥ 0.05 (cell 64). |
| fig5e1-correlation-near-zone | not_reproduced | Interaction p = 0.65; conflict-near-conflict is not above other cells in LSD (cell 68). |
| fig5e2-e4-change-near-zone | not_reproduced | All interactions p ≥ 0.17, in every reading (cell 70). |
| correlation-not-speed | reproduced | Speed p = 0.105, acceleration p = 0.05004 (right at the threshold), place cell and interneuron rates p < 1e-9, rate ANOVAs not significant (cell 74). |
| fig5e1-inset-rate-change-near-zone | not_reproduced | Manipulation effect p = 0.059 (M11b) and 0.12 (M11a) (cell 72). |
| fig6b-correlation-before-avoidance | not_reproduced | Interaction p = 0.30–0.44 (ordinary ANOVA) and 0.08–0.12 (mixed model) (cell 76). |
| fig6c-no-increase-before-errors | reproduced | Interaction p = 0.72 and 0.93 (cell 76). |
| fig6-inset-rate-changes | reproduced | Avoidances: manipulation p ≤ 0.007, zone and interaction not significant. Errors: zone p ≤ 0.0075, manipulation p ≤ 0.013 (cell 78, M11b only). |

The paper states no chance level for any selection, so there was nothing to compare.

### B. Problems

1. **[affects a conclusion] Field detection does not match the paper's cells.** The field definition (claims file M2/M5, run in `H.place_fields` on unsmoothed 8-px maps) finds no field in 19 of 45 DG place cells (cell 14). Avoidance place cells average 0.19–0.49 room fields (cell 30), where Table S2 gives 1.81–2.36. On synthetic data, a true single Gaussian field at 0.1 s occupancy per bin was scored as zero fields in 48 of 50 runs: isolated one-spike bins set the 20%-of-peak threshold. This is a claims-file problem (the readings are unreasonable for unsmoothed maps), not a coding error. Affected: fig1-single-field-proportion, fig1-field-number-scaling, fig1c, the field part of fig3d, and the field-based readings of M10 and network consistency.
2. **[affects a conclusion] One field reading was never run for fig3d.** The M5b field mask is run only with M11a (`MVb`, cell 38), never with M11b, the adopted reading. Under M5a the field part rests on 13–15 cells per group.
3. **[affects a conclusion] Wrong post hoc test in fig4d-room-ipos-near-active-zone (cell 90).** It uses paired t-tests over 5–6 mice, not Fisher's LSD with the model's pooled error. The partial outcome turns on this step.
4. **[affects a conclusion] Some "shock-off" recordings had the shock on.** WT15's training 1 recording (WT15Ini1_2, 33 shocks) and WT16's training 2 recording (WT16Ini2_1, 20 shocks) log shocks in their own Tracker files. WT15's training 2 recording is byte-identical to the shock-on file, which is 20 min long where training 2 should be 10. Cells 8 and 46 print this, but cells 42–48 still use these as shock-off sessions, and WT15's training 2 enters both shock levels as the same file. This affects fig3b-avoidance-learning, which is borderline (p = 0.067), and fig3b-shock-off-avoidance. In the other four mice the shock-off excess is large, so the shock-off outcome likely holds.
5. **[does not affect a conclusion] Errors are counted differently on and off shock (cell 42).** Shock-off errors are geometric zone entries from the spike-file positions; shock-on errors are the Tracker's own entrances. On shock-on files the geometric count runs 1.18× the Tracker's. Training 2 compares 10-min shock-on against 20-min shock-off sessions as raw counts. The 2–3× shock-off excess, also seen in errors per meter, is larger than these biases.
6. **[does not affect a conclusion] Approximate df in the mixed models (`H.mixed_terms`).** They use residual df (28) rather than the paper's fractional df. Recomputed with the paper's df, fig4b's interaction is p = 0.0066 and fig4d's conflict-zone test is p ≈ 0.036–0.038, both still significant.
7. **[does not affect a conclusion] Information content units (cells 25, 30).** Table S1/S2 values labelled "bits/s" match the notebook's bits/spike (1.32, 1.59, 1.60), not its bits/s (0.83, 1.15, 0.73). The claims file takes the label literally, which may be a misreading of a mislabel in the paper. The notebook prints both but never applies the tolerances. The tables1 outcome stays partial either way because coherence is outside tolerance.
8. **[does not affect a conclusion] Pair classes don't match the paper (cell 62).** No reading reproduces the paper's pair-class counts, so fig5d3, fig5d4 and negative-pairs-no-change use classes that differ from the paper's. The adopted reading (a)(iii) is the author's own choice, though every reading is shown.
9. **[does not affect a conclusion] Alignment check fails for two kept sessions (cell 10).** 140731_WT15_testbox1 and 140803_WT16_rotated90dcircleintestbox2 fail the spike–position alignment check but stay in the analysis. Testbox2 was dropped as a duplicate of testbox1's positions even though its spike trains differ (cell 7). Only a few cells are involved.
10. **[does not affect a conclusion] Grid and distance scale.** The 8-px grid (1.25 cm in the arena) is reasonable: it reproduces the deposited TIME map exactly (r = 1.0). But "3 pixels" on that grid is 3.75 cm, not the 4.5 cm the notebook uses for zone vicinity.
11. **[does not affect a conclusion] Approach events on the raw distance are mostly jitter (cell 66).** The raw 30-Hz distance gives about 1,000 approach events per session. Both readings were run and the outcomes agree.
12. **[does not affect a conclusion] correlation-not-speed passes by a hair.** The acceleration test is p = 0.05004, so this outcome is fragile.

### C. Not checked

- **Blocked claims:** I listed the S3 prefix `hc-17/live`. It holds only `data.zip`, `checksums.md5`, `filelist.txt` and the docs. I also read the zip's central directory (file list only, 11,972 members). The only behaviour folders are `recordingDAT`, `DATfilesPlaceAvoidanceShockON` and `EnvironmentalChangesTask`, all named with the recorded WT mice. There are no Cre, POMC, Halo or cFos files. No part of the four optogenetic claims can be tested.
- **Cluster identity across sessions:** whether the same tetrode/cluster label is the same cell in every session is an assumption the files can't settle.
- **Field detection (B1):** whether the failure is the definition or the implementation. A comparison of the notebook's maps and field counts against the deposited `data/SPIKE` maps would show this.
- **Shock-off sessions (B4):** the shock-off results with WT15 and WT16's shock-logging sessions dropped, and an error count using the Tracker's entrance rule on shock-off positions.
- **fig4d (B3):** pooled-error Fisher's LSD for the conflict zone.
- **fig3d (B2):** the field-part Kruskal-Wallis under M5b with M11b.
- **Mixed models (B6):** Kenward-Roger df.

I ran nothing from the notebook. Every outcome above comes from its printed outputs, plus synthetic tests of `map_stability`, `place_fields`, `rm_multivariate`/`rm_univariate`, `ipos_series` and `coherence`, all of which behaved as specified.
