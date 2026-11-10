**Verifier report, round 1: Jones et al. 2019 on CRCNS hc-26**

The claims file has 65 claims. The notebook records an outcome for all 65, and one of them (`table-s4-young-no-prediction`) is blocked.

The finding that matters most: the notebook's CA3 mouse selection doesn't match the paper's in either cohort, and the notebook never says so. Every CA3 outcome below rests on it.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| fig1e-swr-abundance-genotype | reproduced | Cell 13: t(27)=8.21, p=8e-09, E4 0.113 Hz against E3 0.245 Hz. |
| fig1f-sg-power-genotype | reproduced | Cell 15: E4 lower with p<0.05 in CA1-sr, CA3 and DG under all four readings. CA3 uses 13 E3 / 16 E4 mice against the paper's 11/13 (B1). |
| figs1a-mua-during-swrs | reproduced | Cell 17: paired p ≤ 0.0015 in both genotypes under both baselines; genotype p = 0.49–0.72 before and during. |
| fig1g-mwm-impaired | reproduced | Cell 19: ART F(1,37)=13.08, p=0.0009, the paper's exact value. Sidak p<0.05 on days 1, 3 and 5. |
| screen-88-comparisons | not_reproduced | Cell 21: 5 of 88 significant, binomial p=0.45; tolerance is 9±1. Two of the five are CA3 at n=16 (B1); the DG selection is also off (B2). |
| fig2b-swr-slope-days-1-2 | not_reproduced | Cell 25: R=-0.471, p=0.066. |
| figs1b-swr-slope-days-1-3 | partially_reproduced | Cell 27: R=-0.572, p=0.021; outside -0.66±0.066. |
| fig2c-swr-latency-day-3 | not_reproduced | Cell 29: R=-0.434, p=0.093. |
| fig2d-swr-overnight | partially_reproduced | Cell 31: R=-0.524, p=0.037; outside -0.64±0.064. |
| fig2e-learning-score | partially_reproduced | Cell 59: R=0.61, R²=0.375–0.377, p=0.012; 0.51±0.051 needed. |
| screen-features-independent | not_reproduced | Cell 63: abundance against CA3 R=-0.53, p=0.034. This is on 16 E4 mice; the criterion asks for 13 (B1). The score correlation is p=0.60. |
| fig2f-ca3-probe1-quadrant | not_reproduced | Cell 33: R=0.487, p=0.056 at n=16, where the paper has 13 (B1). |
| figs1d-ca3-probe2-quadrant | not_reproduced | Cell 35: R=0.356, p=0.18 (n=16). |
| fig2g-ca3-probe1-crossings | partially_reproduced | Cell 37: R=0.641, p=0.0075; outside 0.78±0.078 (n=16). |
| fig2h-ca3-probe1-auc | not_reproduced | Cell 39: R=-0.460, p=0.073 (n=16). |
| figs1f-ca3-probe2-auc | not_reproduced | Cell 41: R=-0.270, p=0.31 (n=16). |
| fig2i-memory-precision-score | partially_reproduced | Cell 61: R=0.64–0.66, p<0.01; outside 0.844±0.084. R²=0.41–0.44, against 0.71 and 0.77 (n=16). |
| rep-mwm-swr-slope-days-1-2 | not_reproduced | Cell 43: R=-0.021, p=0.95, n=11 (matches the paper's n). |
| rep-mwm-swr-latency-day-3 | not_reproduced | Cell 45: R=-0.113, p=0.74. |
| rep-mwm-swr-overnight | not_reproduced | Cell 47: R=-0.087, p=0.80. |
| rep-mwm-swr-slope-days-1-3 | not_reproduced | Cell 49: R=-0.250, p=0.46. |
| fig2n-rep-learning-score | not_reproduced | Cell 65: R²=0.017, p=0.70. |
| rep-mwm-ca3-probe1-quadrant | not_reproduced | Cell 51: R=0.03, p=0.94. n=8 against the paper's 10 (B1). |
| rep-mwm-ca3-probe1-crossings | not_reproduced | Cell 53: R=0.20, p=0.64 (n=8). |
| rep-mwm-ca3-probe1-auc | not_reproduced | Cell 55: R=+0.415, wrong sign (n=8). |
| rep-mwm-ca3-probe2 | not_reproduced | Cell 57: R=0.36 (p=0.38) and -0.285 (p=0.49), n=8. |
| fig2r-rep-memory-score | not_reproduced | Cell 67: R²=0.02–0.03, p≥0.67 (n=8). |
| rep-all-replicated | not_reproduced | Cell 69: 0 of 9 relationships hold. |
| cohort-swr-differences | reproduced | Cell 71: abundance 0.113 against 0.197 Hz, p=9.7e-05. Baseline is within tolerance only under reading (b): 16.18 against 11.43, t(51). Reading (c), the one whose df fits t(25), gives 9.77, out of tolerance. Units were not established (B6). |
| robust-single-point | not_reproduced | Cell 142: fig2d has 5 failing removals and figs1b has 1. If only fully "reproduced" claims count, it would be reproduced (B4). |
| robust-detection-parameters | not_reproduced | Cell 73: 8 of 26 hold. Even if the 10 uncomputed correlations all held, 18 of 36 is below the 32 needed. |
| age-no-correlation | reproduced | Cell 75: 0 significant under both readings. |
| figs2-nonspatial-no-difference | reproduced | Cell 77: 0 of 10 tests have p<0.05. |
| nonspatial-not-correlated | not_reproduced | Cell 79: 2 of 60 significant, which is under the 3 expected by chance. The criterion is strict, so this fails. One of the two has n=5 (hot plate against CA3). |
| ca1-dg-not-predictive | not_reproduced | Cell 81: DG against latency day 1 p=0.045 (1 of 44). Rests on unconfirmed DG sites (B2). |
| e3-relationships | not_reproduced | Cell 83: screen E3 day 2 p=0.053; replication E3 R=+0.41 at n=6 (paper 9); the genotype ranges overlap. |
| fig3b-apa-entrances-day1 | reproduced | Cell 85: t(23)=3.43, Sidak p=0.009, matching the paper. |
| figs3-apa-day1-and-probe | partially_reproduced | Cell 87: 3 of 4 hold. Distance per bout runs E3 > E4, against the text, but the sign of the port is unchecked (B5). |
| apa-40-comparisons | not_reproduced | Cell 89: 2 of 40 significant, 1 of them on day 2. |
| apa-day2-variance | partially_reproduced | Cell 91: day 2 variance is higher under every reading, but no reading is within tolerance. |
| figs3fg-day2-predicts-later | reproduced | Cell 93: R=0.904 and 0.773. Group differences on days 3 and 4 but not day 1, under both readings. |
| fig3c-swr-latency-first-entrance | not_reproduced | Cell 95: R=0.32, p=0.37, n=10. |
| fig3de-swr-path-and-quadrant | not_reproduced | Cell 97: R=0.28 (p=0.44) and 0.28 (p=0.43). |
| fig3f-apa-learning-score | not_reproduced | Cell 104: R² ≤ 0.13, p ≥ 0.31 under both metric readings. |
| fig3g-ca3-entrances | not_reproduced | Cell 99: day 2 R=-0.59, p=0.16, n=7 (paper 9). |
| fig3h-ca3-distance-per-bout | not_reproduced | Cells 101–102: p ≥ 0.08 under both bout columns (n=7). |
| fig3i-apa-memory-score | not_reproduced | Cell 106: R²=0.41, p=0.12 (n=7). |
| figs3ij-mwm-predicts-apa | partially_reproduced | Cell 108: learning R=0.638, p=0.047, within tolerance (2-metric score, E4 z-scores). Memory n=7, p=0.13. |
| figs4ab-young-deficits | not_reproduced | Cell 110: the CA3 genotype effect has p=0.087. That test has only 4 E3 mice at 13-17 months against the paper's 9 (B1). Abundance holds. |
| figs4ab-aging-increase | partially_reproduced | Cell 112: 2 of 3 hold under reading (b). CA3 E3 at 13-17 months is n=4. |
| figs4cd-baseline-sd-swr-band | reproduced | Cell 114: all three decreases have adjusted p<0.05; E3 SD p=0.97. |
| figs4ef-ca3-sg-baseline-stable | not_reproduced | Cell 116: E4 baseline (Sidak p=0.002) and E4 SD (p=0.038) both fall. |
| figs4g-young-no-deficit | reproduced | Cell 118: F=0.08, p=0.78. |
| table-s4-young-no-prediction | blocked (metadata_insufficient) | Cell 1. I agree after checking the archive (section C). |
| fig4bc-swr-not-stable | reproduced | Cell 120: 0 of 4 significant. |
| fig4de-ca3-sg-stable | not_reproduced | Cell 122: E4 R=-0.08 and 0.37. E3 n=7 and 4 against the paper's 11 and 9. |
| ca3-sg-5-8-vs-13-17 | reproduced (weak) | Cell 124: E3 p=0.11 meets the criterion, but on 4 of 9 mice with R=+0.89 against the printed 0.2. |
| fig4g-young-ca3-slope-days-1-2 | not_reproduced | Cell 126: R=-0.03, n=8 (paper 11; B7). |
| fig4h-young-ca3-latency-day-3 | not_reproduced | Cell 128: R=+0.07 (n=8). |
| figs4h-young-ca3-slope-days-1-3 | not_reproduced | Cell 130: R=+0.18 (n=8). |
| fig4i-young-mwm-learning-score | not_reproduced | Cell 134: R²=0.003. |
| fig4jk-young-ca3-apa | not_reproduced | Cell 132: R=-0.07 and -0.155, wrong sign (n=8). |
| fig4l-young-apa-learning-score | not_reproduced | Cell 136: R² ≤ 0.02. |
| table-s4-30-comparisons | not_reproduced | Cell 138: 4 of 30, which is within the count tolerance, but binomial p=0.061 ≥ 0.05 (n=8). |
| figs4i-young-ca3-predicts-later-swr | not_reproduced | Cell 140: E4 R=0.447, p=0.19, n=10 (paper 15). |

**Chance levels.** The notebook's binomial tests use chance = 0.05, the same as the paper's. My checks give 9/88 → 0.032, 8/40 → 0.00071 and 5/30 → 0.016, matching the claims file.

### B. Problems

1. **[affects a conclusion]** CA3 mouse selection doesn't match Table S1 or the claims file (`swr._site_groups`; cells 11, 15, 110, 112, 122).
   - Screen cohort: CA3 values for 13 E3 / 16 E4 mice; the paper has 11/13.
   - Replication 13-17 months: E3 4 against 9, E4 11 against 14. At 9-11 months: E3 7 against 11, E4 14 against 16.
   - The notebook never shows these numbers next to each other.
   - In the screen cohort, every mouse has chinfo-labelled CA3 sites, so the paper's histology exclusions can't be reproduced from labels. A sensitivity run over all 560 subsets of 13 out of 16 E4 mice was cheap and wasn't done.
   - In Cohort 2 the notebook finds fewer CA3 mice than the paper, which points to missed sites. It wasn't investigated.
   - Every CA3 claim rests on this.
2. **[affects a conclusion]** DG uses every gc/hil site. The Methods' restriction to sites with confirmed dentate spikes isn't applied, and the `dgval` variant is not that restriction (`swr` docstring, cell 15). The only failing correlation in `ca1-dg-not-predictive` (p=0.045) and one of the five in `screen-88-comparisons` are DG.
3. **[affects a conclusion]** The "5 SD, Methods" SG reading times its window from the 3 SD threshold crossing (`session_rows` uses `swr_power_det_events`), not from the 5 SD detection. `swr_power_det_events_5sd` is computed but never used, so the Methods reading is never actually run. This could move borderline screen CA3 results: fig2f p=0.056, fig2h p=0.073.
4. **[affects a conclusion]** `robust-single-point` (cell 142) counts the partially reproduced claims as "reproduced here". Counting only fully reproduced claims leaves the two figs3fg correlations, with 0 failing removals, which would make it reproduced. Only one reading was run.
5. **[affects a conclusion]** APA distance per bout (`analysis.apa_metrics` defaults to `dist_per_bout_walk_cm`; `behavior.apa_distance_per_bout`).
   - The main column is the walk-bout one. Claims (D) names "Avg Travel Away from SZ (cm)", which the module's own docstring identifies as the all-bouts column. The all-bouts column is run only for fig3h and S3C, not for fig3i, apa-40, table-s4-30, figs3ij or nonspatial.
   - The U=30 match with Figure S3C doesn't depend on the metric's sign, so it doesn't confirm the port's sign. The paper says E4 "moved further" and the port gives E4 lower.
   - If the port's sign is reversed relative to the paper's metric, figs3-apa-day1-and-probe becomes reproduced (4 of 4).
6. **[affects a conclusion]** In `cohort-swr-differences` (cell 71), int16 counts are compared with µV values without the units being established, which the claims file asked the author to do. Only reading (b), with t(51), lands within tolerance; reading (c), which fits t(25), doesn't.
7. **[affects a conclusion]** The archive holds 14 E4 mice at 5-8 months, not 17; `Cohort_2/animaldef.m` lists exactly 14. So the Figure 4 and Table S4 claims run on 8 of 11 (MWM) and 8 of 10 (APA) mice. The notebook doesn't call these tests partial or flag the missing data.
8. **[affects a conclusion]** Mice are lost in linking with no explanation: replication E3 with MWM, 6 against 9 (e3-relationships); hot plate E4, 10 against 13; visible platform, 13/14 against 12/15 (cells 77, 83).
9. **[does not affect a conclusion]** The Holm-Sidak adjusted p values that the replication criteria ask to see are never reported; `stats.holm_sidak` is unused.
10. **[does not affect a conclusion]** Cell 73 says 18 of 36 correlations were not computed; the true number is 10 (26 were run).
11. **[does not affect a conclusion]** `stats.loo_pearson` counts removals over rows with NaN too (e.g. "n=8 … 11 removals"), so the LOO column is inflated for correlations with missing values. The set used for `robust-single-point` has no NaNs.
12. **[does not affect a conclusion]** The "all mice" z-score reading uses only recorded mice that have behavior (inner join in `score_table`), not all mice of the cohort. The E4-only and "all" readings give nearly the same results.
13. **[does not affect a conclusion]** The multitaper uses 5 tapers (`dpss(100,3,5)`); claims (B) says 3. The claims file may be misreading Chronux's `[3 5]`; I couldn't check the code.
14. **[does not affect a conclusion]** `task.age` ranges don't fit the paper's age groups: Cohort 1 is 14.1-20.3 months, and the Cohort 2 "13-17 mo" group spans 9.0-17.3 (cell 5). This wasn't checked before using age in `age-no-correlation`.
15. **[does not affect a conclusion]** Cell 5 reports "sessions with MUA: 163 of 151 Cohort 1 sessions", more sessions than exist. This isn't explained; the MUA claim uses Cohort 1 only.

I found no leakage between training and test data: the method G model is fitted on Cohort 1 only. Synthetic checks all behaved as expected:
- `extract_events` drops a 10 ms event and gives the right `maxthresh`.
- `immobile_mask` applies the 30 s rule.
- `holm_sidak`, `binom_greater` and `scores` give the hand-computed values.

### C. Not checked, and the output that would have settled it

- **The blocked claim.** The bucket listing holds only the tar files, the two `animaldef.m` files (ephys names and genotypes only), docs and `All_Figures.pzfx`. I confirmed the Prism file is binary (`PCFF` header). Without downloading `Cohort_2/Behavior.tar.gz` I couldn't see whether the 6-9 month MWM file carries ear tags (`Mouse #`) that would link it through the APA manifest. That output would settle it: the 6-9 month file's ID columns next to the manifest's columns.
- **Which mice have CA3 and DG sites.** A per-mouse, per-age table of CA3 and DG site labels set against Table S1. For the screen cohort, the CA3 outcomes over all 13-of-16 subsets.
- **SG timing.** SG power triggered at the 5 SD detection, using the already computed `swr_power_det_events_5sd`.
- **Distance-per-bout sign.** Its sign against `pull_apa_metrics.py` output for one mouse or session, and the all-bouts column for every APA claim.
- **LFP units.** The int16-to-µV scale of the deposited LFP, from the descriptor or the eeg struct fields.
- **Panel values.** Values "read from the panel" (Figures 2E, 2I, 2K–R, 4D–E, S3, S4I) couldn't be checked; no PDF renderer was used.
