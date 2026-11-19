**Verification report, round 1: Huszár et al. 2022 on DANDI:000552 (0.261113.1035)**

The claims file has 44 claims. The notebook tests 33 and treats 11 as blocked. My outcomes: 18 reproduced, 10 partially reproduced, 5 not reproduced, 11 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| cohort-birthdates | reproduced | 17 mice, 12 M and 5 F, birthdate counts 4/3/6/4 (cell 8). |
| st1-animal-sessions | reproduced | All 17 mice match the table row by row. Sessions are 96 and 104; light-responsive cells are 664 (cell 10). |
| sessions-durations | partially_reproduced | On the 96 sessions the count is within 92 ± 9.2 and the median is 309.9 min. The range is 113.7 to 475.6 min, exactly the paper's. Two sessions (e13_1f1_200305 and _200307) have no non-REM sleep, so "every session holds non-REM" fails (cell 12). Read literally, the criterion gives not_reproduced, because it has no category for this case (see B14). |
| spwr-duration | reproduced | The median is 36.0 to 36.8 ms under every combination of readings, and no ripple lies outside 20 to 200 ms (cell 18). |
| unit-count | reproduced | On the 96 sessions: 9,472 units, 7,411 pyramidal cells, 2,060 interneurons (1,556 narrow, 504 wide) (cell 14). |
| ed2-light-responsive-count | reproduced | 664 of 7,411 (8.96%) under both readings (cell 16). |
| ed2-waveform-validation | blocked (too_large / data_missing) | The light-evoked waveforms need wide-band data. On the archive the 11 raw files include only 5 homecage-mouse sessions (3 of e13_26m1, 2 of e16_3m1; 52 to 141 GB each). The trough-to-peak part was computed and matches the paper: 0.696 against 0.700 ms, p = 0.134 (cell 86). |
| ed1-brdu-specificity | blocked (data_missing) | The archive holds only 115 ecephys NWB files and no histology. |
| fig1c-radial-depth | blocked (data_missing) | Same reason as ed1. |
| fig1e-labelled-fraction | reproduced | Means and s.d. equal the paper's. F = 8.525, bootstrap p < 0.0002 (cell 20). |
| fig1f-rem-shift | not_reproduced | Fractions 27.96/20.99/19.74/21.54%; the E14.5 and E15.5 fractions are outside tolerance. Slope −2.05 %/day, p ≈ 0.16 across seeds, and p = 0.162 with the 0.05 variant (cell 37). This depends on the theta-channel choice (B1). |
| fig1g-rate-by-birthdate | reproduced | Medians 1.52/1.62/1.54/1.15 Hz, all within tolerance. E16.5 is lowest, p = 0.034 to 0.041 (cell 25). |
| fig1h-burst-by-birthdate | partially_reproduced | p ≤ 0.0004 and the inverted-U holds. All four medians (0.088 to 0.104) are about 25% below the paper's (cell 27). |
| ed3-depth-control | blocked (other) | The analysis was not run ("not reached in the run's time"). The data it needs is in the files, so it is testable (B4). |
| fig2b-synchrony-per-animal | reproduced | Among the 13 animals: reading (a) gives 10, reading (b) gives 12, both within 10 to 12 (cell 33). |
| fig2c-theta-cofiring | reproduced | SBD 0.0180 against DBD 0.0078, p = 1e-41, pair counts exact. The DBD median sits at the edge of its tolerance. The theta channel does not follow the Methods' rule in 62 of 104 sessions. On the sessions where it does, the SBD median is 0.0145, outside tolerance (cell 41, B1). |
| fig2d-theta-depth | reproduced | Wake medians 0.120/0.097/0.090/0.107, all within tolerance and in the claimed order, p ≈ 0. REM p ≈ 0.74 (cell 39). |
| fig2f-ripple-firing-by-birthdate | reproduced | For both measures all medians are within tolerance, the inverted-U holds and p ≤ 0.001 (cell 29). |
| fig2g-ripple-cofiring | reproduced | SBD 0.0385 against DBD 0.0226, p = 5e-98 (cell 31). |
| ed5-matched-controls | blocked (data_missing, for L-ratio only) | The rate-matched parts (a) and (b) could have been tested with data the notebook already holds (B4). |
| fig3c-assembly-cofiring | blocked (other: compute) | The data is present; the analysis was not run. |
| fig3e-assembly-expression | blocked (other: compute) | Same as fig3c. |
| ed6-heldout-assemblies | blocked (other: compute) | Same as fig3c. |
| ed7-sbd-coactivation | blocked (other) | It needs only the SPW-R count matrices that `homecage_session` already builds, so it was cheap to test (B4). |
| fig4d-model-fit | blocked (other: compute) | A simulation; it needs no data beyond published values. |
| maze-cohort | reproduced | 9 familiar-maze mice (2/2/2/3) and 3 novel-environment mice (cell 48). |
| maze-task | not_reproduced | Trial extent 202.8 cm and tracking at 30 Hz both hold. Only 30 of 57 sessions have ≥10 trials of each type, and only 51 of 57 have ≥20 trials (cell 51). The trial counts are not checked against the trials table (B5). |
| novel-explorations | reproduced | 16 explorations in 6 environments: 2 linear tracks, 3 open fields, 1 figure-eight (cell 53). |
| fig5b-spatial-info-by-birthdate | partially_reproduced | Both tests give p < 0.001 and the inverted-U holds under every reading. Information medians are 0.56 to 0.92 bits/s, about 30% low, and the coverage medians are outside tolerance (cell 55). |
| fig5c-sbd-ratemap-overlap | partially_reproduced | SBD 0.0189 is outside tolerance; DBD −0.0239 is within. p = 6e-9 (cell 57). |
| fig5d-overlap-by-distance | partially_reproduced | Birthdate main effect p = 1e-4. The post hoc comparison is significant at 0 and 250 µm and not at 500 µm. Five of the six means are outside tolerance (cell 59). |
| fig5e-pv-decorrelation | partially_reproduced | The stem is highest and p = 0. The turn 1 median, 0.488, is outside tolerance (cell 61). |
| fig5f-remap-together | reproduced | Main effect p = 9e-7, and SBD is above DBD in all three terciles (cell 63). |
| fig6c-theta-rate-preserved | reproduced | ρ = 0.741, n = 2,544 exactly (cell 43). |
| fig6d-rate-lower-novel | reproduced | Familiar 0.755 Hz against novel 0.675 Hz, rank-sum p = 0.0013 (cell 45). |
| fig6d-info-lower-novel | partially_reproduced | Novel is lower, p = 1e-35. The familiar median, 0.661, is outside tolerance. This uses only 8 of the 16 explorations (B2). |
| fig6c-novel-ratemap-corr-higher | not_reproduced | Novel −0.032 against familiar −0.045, p = 0.75 (cell 70). This is not decisive: 8 of 16 explorations are missing, including every open field, and the novel position units are unverified (B2). |
| fig6e-sbd-novel-overlap | partially_reproduced | SBD is above DBD, p = 0.002, but both medians (0.030 and −0.034) are far from the paper's 0.117 and 0.046. Same subset caveat (cell 72, B2). |
| fig6f-remap-together-novel | reproduced | Main effect p = 0.016 under reading (a) and 0.013 under (b), SBD higher. This holds on the subset only (cell 74). |
| fig7b-sbd-convergence | partially_reproduced | SBD is above DBD, p = 1e-79. The medians, 0.45 and 0.36, are far above 0.27 and 0.20 (cell 78, B3). |
| fig7ce-convergence-by-birthdate | partially_reproduced | Both tests give p ≈ 0 and both shapes hold. 7 of the 8 medians are outside tolerance (cell 80). |
| fig7d-transmission-gamma | not_reproduced | The peak bin is 29 to 42 ms, not 13.5 to 25.3 ms. The curve is nearly flat from 20 to 60 ms (cell 82). |
| fig7fg-convergence-cofiring | not_reproduced | 50,618 connections against 31,932 ± 3,193, and 86.2% of pairs share a target against 65.27%; both counts fail. All six slopes are positive with p < 0.001 (cell 84, B3). |
| ed10-waveform-matched-controls | blocked (other) | The notebook blocks it only through its dependency on ed2. Its cofiring and ratemap comparisons for same-shank pairs more than 60 µm apart need no light-evoked waveforms (B4). |

### B. Problems

1. **[affects a conclusion]** `pick_theta_channel`, cells 35, 37, 39, 41. In 62 of 104 sessions no channel with a positive sharp wave was found, so the pyramidal-layer channel was used. The median sharp wave at the chosen channel is negative (−218.7). That breaks the Methods' rule (a channel above the layer centre, "to ensure consistency of extracted phases"). fig1f classifies cells by absolute phase (120 to 300°), so it depends directly on the reference channel, and no fig1f or fig2d variant was run on the 35 sessions that follow the rule. For fig2c, the conforming subset moves the SBD median out of tolerance. Separately, the sharp-wave amplitude is printed as µV but is computed on raw values without the conversion factor.
2. **[affects a conclusion]** `novel_session`, cells 64 to 74.
   - All 7 open-field explorations were dropped, plus the linear track of e16_3m2_211211, whose omission is never explained.
   - The archive's release notes say positions are in cm only for the familiar figure-8 maze, "in the source's own units elsewhere". The linear tracks and the novel figure-eight were nevertheless binned as 1 cm (`nbins = ceil(xmax)`, the 1.5 cm/s speed threshold, bins 51 to 164). Their units and bin counts are never printed.
   - Pearson correlations of open-field maps can be computed with bins chosen from the arena's geometry; the claims file allows this.
   - This affects fig6c-novel, fig6e, fig6d-info and fig6f. Novel pairs number 22,373, against the paper's 41,991.
3. **[affects a conclusion]** `mono_test`/`mono_p`, cell 76. The detector finds 58% more connections than the paper.
   - The test window is fixed at 0.8 to 2.4 ms, whereas the Methods' reliability test uses "3 bins surrounding [the] peak".
   - The hollow fraction of 0.6, and the minimums of 50 CCG counts and 100 presynaptic spikes, are assumptions; the two minimums are not stated as such.
   - Only alpha was varied. This drives the fig7b, fig7ce, fig7d and fig7fg outcomes.
4. **[affects a conclusion]** Cells 85 to 87, blocked claims that were partly testable:
   - ed5's rate-matched parts.
   - ed10's comparisons for pairs more than 60 µm apart (electrode positions and `max_electrode` are in the files).
   - ed7, which needs only SPW-R spike counts.
   - ed3: depth from the sharp-wave profile and the electrode positions; "not reached in time" is not a data limit.
5. **[affects a conclusion]** Cell 51 / `linear_maps`. Trials are counted only after the mapping filters: inside the epoch, at least 5 position samples, arm left or right. Some trials have an extent of 1.8 cm. The counts are never compared with the trials table, even though `S.trials` is computed, so the maze-task failure may be an artefact of the filters.
6. **[does not affect a conclusion]** `acg_counts`: `(d/binsize).astype(int)` truncates floating-point values. In a synthetic test, a lag of exactly 2 ms fell into the 1 ms bin. The effect is small and cannot explain the roughly 25% burst-index offset.
7. **[does not affect a conclusion]** Cell 59: Tukey is run on a six-group one-way model rather than on the two-way model. Shank distance is taken as |Δshank| × 250 µm, which assumes consecutive shank ids on one probe. 1,394 pairs at 750 µm are dropped.
8. **[does not affect a conclusion]** Cell 74, reading (a): the tercile edges are computed on the merged table. Familiar correlations of sessions with two novel environments are counted twice.
9. **[does not affect a conclusion]** Cell 84: 371,756 pyramidal pairs, against the legend's 315,722 (108,468 + 207,254). The pair set differs and the notebook does not say why.
10. **[does not affect a conclusion]** Cell 37: the both-locked counts (93/81/76/65) are not compared with the paper's. The paper's legend n (123/106/143/76) exceed its own REM-locked counts in fig2d, while Fig. 1f (top) gives n = 95 for E13.5, so the paper is internally inconsistent here. This is a point the claims file does not address.

Helper functions I checked on synthetic inputs and found correct:
- interval handling (`subtract`, `in_intervals`) and `ripple_measures`;
- `skaggs_info` (0 for a uniform map, log2(10) for one active bin of ten);
- `rayleigh`, which matches CircStat;
- `boot_kw` and `boot_anova`: about 5% of p values fall below 0.05 when there is no effect;
- `convergence`, theta phase (0° at the peak) and cycle length;
- `ccg_sync`;
- the monosynaptic test: it detects an injected 1.5 ms connection and gave no false positives in 200 independent Poisson pairs.

**Claims-file issues (reported, not corrected):**
11. **[affects a conclusion]** The sessions-durations criterion has no category for "all numbers hold, but some sessions lack non-REM". Read literally it gives not_reproduced, below its own partial case.

### C. What I could not check, and the output that would settle it

- **Units of the novel-environment positions:** print each novel epoch's series unit and description (`META[s]["series"]`) together with `nbins`.
- **Theta channel:** print each session's chosen channel position relative to the pyramidal-layer channel (`rel_y`), and rerun fig1f and fig2d on the 35 sessions that follow the Methods' rule.
- **Maze trial counts:** print the trials table's left and right counts per session next to the counted trials.
- **Units table:** print its column names and the shape of `waveform_mean`. That shows whether an L-ratio exists and whether multi-channel waveforms (needed for ed10's profile distance) are present.
- **The two Awake-only sessions:** print their sleep-state table and durations, to tell "no sleep" from "no scoring".
- **Monosynaptic counts:** give the connection count and fig7d peak under the "3 bins around the CCG peak" reading and under other hollow and s.d. settings.
- **Probe layout:** state whether any session has more than one probe (the `probe side` column), which matters for the shank distances in fig5d.
