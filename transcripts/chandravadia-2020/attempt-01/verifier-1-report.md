## Verifier report, round 1: Chandravadia et al. 2020 on dandiset 000004 (0.220126.1852)

Of the 24 claims in the claims file, I find 10 reproduced, 8 partially reproduced, 4 not reproduced and 2 blocked.

What I checked independently:
- The paper's full text and tables are saved in `paper/`.
- The helper's copy of Online-only Table 1 matches the paper's table exactly: 87 sessions, 59 subjects, 25 F and 34 M.
- I tested the helper functions on synthetic data:
  - Under the null, `bootstrap_p` gives 5.4% below 0.05 and `anova_p` gives 4.8%.
  - With equal-variance signals, `zroc_slope` returns about 1.0. With old-item SD 1.4 it returns 0.71, where 0.714 is expected.
  - `auc` matches theory to within the trapezoid bias (0.749 against 0.760).
  - `window_rates` counts spikes in (start, stop].
- I compared `bootstrap_p` with `bootstrapMeanEqualTest.m` at commit 1d95162. That function's default (`varCorrection=0`) uses the plain mean difference, so the helper matches it.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| counts-neurons-subjects | reproduced | Cell 12 counts 1864 unit rows (+1 against 1863) and 59 subjects. With duplicated spike trains counted once the count is 1809, also within tolerance. |
| counts-sessions | reproduced | Cell 14: the 87 (subject, session) pairs in the files equal those in Online-only Table 1. The Methods' "89" does not match. |
| table1-demographics | partially_reproduced | Cell 16: 56 of 59 subjects match on age and sex. C24 and H33 differ in age; H48 differs in age (32 vs 54) and sex. The files give F 26 / M 33 against the table's 25 / 34, which is within tolerance. |
| task-structure | partially_reproduced | Cell 18: 79 of 87 sessions have 100 encoding trials with distinct images. All 87 have 100 recognition trials split 50/50 and 5 categories. |
| new-old-label-coding | not_reproduced | Both tests come out reversed. Cell 20: label-1 images appear in the encoding block (median 1.0, against 0.0 for label 0), and label 1 gets more "old" responses in 86 of 87 sessions. The file description repeats the paper's wrong coding. |
| ttl-codes | partially_reproduced | Cell 22: 78 of 87 files meet every condition. The other 9 contain codes not in Table 1 (0, 4, 22, 23, 98, 99). 17019 of 17047 trials show the sequence in order. |
| experiment-ids | partially_reproduced | Cell 24: 83 of 87 files pass. Sessions 55, 77, 100 and 105 use the ids 82 and 83, or 81 for a learning block. |
| session-dates | partially_reproduced | Cell 26: 86 of 87 files fall on the 1st. Session 48 is dated 2010-03-13. Session 68 is dated 2000-01-01, outside the 2006–2019 span of the other sessions. |
| units-table | partially_reproduced | Cell 28: all columns are present and each unit links to one electrode. The stated waveform rate is 98.4 kHz, within tolerance. SNR is non-finite for 86 units and IsolationDist is NaN for 493. |
| electrodes-table | not_reproduced | Cell 30: `imp` is empty for all 887 electrodes. Coordinates are missing for 99 electrodes in 8 files. |
| isi-criterion | partially_reproduced | Cell 32: 1858 of 1864 units (99.7%) are below 3%, which meets the 95% bar but not "every unit". Two of the six failures (session 58) are caused by every spike time being stored twice. |
| fig5a-mtl-locations | reproduced | Cell 34: all 1864 units are in the amygdala or hippocampus. |
| fig5c-auc-all | reproduced | Cell 36: mean 0.753, SD 0.094 (paper 0.74 ± 0.10). |
| fig5c-auc-sites | reproduced | Cell 38: CS 0.760 ± 0.085 and TWH 0.688 ± 0.138. All four values are within tolerance. Welch p = 0.16. |
| fig5b-roc-asymmetric | reproduced | Cell 40: mean z-ROC slope 0.726, t-test against 1 gives p = 1.6e-9, and 70 of 87 sessions are below 1. |
| fig5d-confidence-accuracy | reproduced | Cell 42, fixed split: 80.1% against 60.9%, paired p = 3.2e-16, over 84 sessions (3 left out). The dynamic split agrees. |
| vs-cells-proportion | reproduced | Cell 46: 332 of 1864 (17.8%), within both tolerances. The shuffled null gives 4.5%, close to the expected 5% (the paper states no chance level). The code's window gives exactly 343 (18.4%). |
| ms-cells-proportion | not_reproduced | Cell 48: the main reading gives 110 (5.9%), outside both tolerances and only just above the shuffled null of 5.3%. The code's choices (correct trials only, 200–1700 ms) give 147 (7.9%), and correct trials only in the Methods window give 143 (7.7%). |
| dual-cells-proportion | not_reproduced | Cell 50: the main reading gives 12 (0.6%), below the 19.6 expected if VS and MS were independent. The code's choices give exactly 26 (1.4%). |
| fig5f-site-proportions | partially_reproduced | Cell 52: no Fisher test finds a site difference (p = 0.36, 0.22, 1.0), but only 1 of 6 values is within tolerance. The code's choices reproduce all six paper values to within 0.1 point. |
| twh-sessions | reproduced | Cell 54: 9 sessions, all with institution "Toronto Western Hospital". |
| fig4-example-vs-neuron | reproduced | Cell 56: the single unit on channel 177 of session 132 (Right Amygdala) has ANOVA p = 1.2e-22, and animals have the highest rate (6.75 Hz against at most 0.85 Hz). |
| previous-release-additions | blocked (metadata_insufficient) | The archive does not mark which sessions were in Faraut 2018. The version metadata's relatedResource lists only OSF and the paper. Only the 9 TWH sessions (8 subjects, 77 units) are new by definition. |
| fig3-example-vs-neuron | blocked (data_missing) | No file has session id 144 (cell 3), and session 144 is not in the paper's Online-only Table 1 either (checked against the saved table). |

### B. Problems

1. [affects a conclusion] **Cells 44, 48, 50, 52: the main reading for MS cells probably differs from how the paper's numbers were computed.** The main reading follows the Methods text (all 50/50 trials, 200–1200 ms). The code's choices (`NWB_singleCellAnalysis_release.m` uses correct trials only and 200–1700 ms) reproduce 343, 147, 26 and every Fig. 5f value almost exactly. The not_reproduced outcomes for ms and dual, and the partial outcome for fig5f, therefore come from the Methods text disagreeing with the code, not from the data. The notebook prints both readings but does not state this.
2. [affects a conclusion] **Cell 48: the main-reading MS proportion is barely above chance.** It is 5.9% against a null of 5.3%, and the null uses only 5 shuffles per unit. Under the Methods' reading, MS selectivity is close to chance at the population level. Cell 50's dual count (12) is below the count expected under independence (19.6).
3. [does not affect a conclusion] **Cell 44: no seed sensitivity check.** One RNG (`rng_ms`) is shared across all bootstrap variants, and no second seed is run. With B = 1000, units near p = 0.05 can flip. That noise is far smaller than the 110 vs 146 gap, but it could matter for the 147 vs 146 match.
4. [does not affect a conclusion] **Cell 9: the shared clock is shown in only 38 of 87 sessions.** For the other 49 sessions (801 units) it is assumed. The population curve (peak 17.8% at +0.2 s, about 5% with shuffled labels) supports it overall.
5. [does not affect a conclusion] **Cell 20: the 8 short-encoding sessions are not commented on.** In these sessions only 52–58% of label-1 images (98% in session 123) appear in the file's learning block. Old images are therefore shown in recognition without an encoding trial in the file. This is a data defect beyond "fewer trials", and the notebook does not mention it.
6. [does not affect a conclusion] **Cell 16: some diagnosis differences are more than coarser coding.** For example, C61 is "Left Lateral Frontal" in the file but "Left Mesial Temporal" in the table, and C56 also differs. The notebook lists these without comment.
7. [does not affect a conclusion] **Cell 22: the TTL check has gaps.** `all_ok` does not check that the response kind matches the trial's phase. It also does not count the 7 files with no 55 marker or the file with three 66 markers.
8. [does not affect a conclusion] **Cell 30: `imp` is reported as "empty" without showing its stored values.** The dtype or a sample of values would show whether it is NaN, an empty string or a placeholder.
9. [does not affect a conclusion] **Cell 36: the "paper's coding" AUC variant is not recomputed.** It is taken as 1 − AUC. That is only approximate under the 0/1 rate adjustment, though the conclusion is unaffected.
10. [does not affect a conclusion] **Cell 40: the two p-values agree exactly.** The Wilcoxon and t-test both print p = 1.6e-9. This is plausible but unusual, and I could not check it without the slopes.
11. [does not affect a conclusion] **Cell 52: the Fisher tests have low power.** With 77 TWH units, "no difference" carries little weight. The claim of comparable proportions rests mostly on the point values.

### C. What I could not check

- **Per-unit and per-session values.** I could not recompute anything from the files themselves (by instruction). A saved table of per-unit p-values (cell 44) and per-session AUC and slope (cell 36) would let me check problems 3 and 10, and confirm 1864 against 1863 unit by unit.
- **The extra unit (1864 against 1863).** The notebook does not show which unit is extra. A per-site and per-session list of units compared with the Fig. 5e counts would show it.
- **fig3-example-vs-neuron.** A weak proxy test is possible but not run. An output listing units on origChannel 140 in the Right Hippocampus, with their phone-category ANOVA, would show whether the Figure 3 neuron exists under another session id.
- **previous-release-additions.** This needs the Faraut 2018 session list (Dryad doi:10.5061/dryad.46st5). The notebook could at least print the TWH portion (9 sessions, 8 subjects, 77 units) as a partial count.
- **The `imp` column.** An output of its dtype and unique values (problem 8).
