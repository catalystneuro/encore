**Verifier report, round 1: Markowitz et al. 2023 on DANDI:000559 (0.261113.1911)**

The claims file has 44 claims. The two notebooks test 27: 17 in `photometry.ipynb` and 10 in `optoda.ipynb`. They mark 16 as blocked, and do not mention fig2k at all. The attempt record was not among my materials, so these counts come from the claims file and the notebooks' own tables.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| ed2a-syllable-repertoire | reproduced | Reading (a), photometry cell 6: 36 syllables (37 ± 3.7), median 400 ms, mean 561 ms, all within tolerance. Reading (b), optoda cell 27, misses (467 and 651 ms), but the criterion needs only one reading. |
| fig1e-velocity-timescales | partially_reproduced | Cell 37: transient rate at 1.96 z holds under both significance readings. Amplitude is never significantly positive at bin sizes of 10 s or more and never changes sign, so one measure of two. |
| ed3c-keypoint-velocity | partially_reproduced | Cell 41: 2D velocity r = −0.170 pooled and −0.169 per mouse, within −0.16 ± 0.016. Forelimb r = −0.026 / −0.027 rounds to −0.03, so it misses. |
| fig1f-syllable-vs-movement-onset | partially_reproduced | Cell 13: reading (b) gives syllable > movement in 14/14 mice, P = 0.00012, which meets the criterion. Reading (a) is significant the other way (P = 0.011). Reading (b) wins only because the movement-aligned averages are deep dips in every mouse (problem 2). |
| fig1f-dip-then-peak | reproduced | Cell 15: minimum −15.4 at 0 s, below the shuffle interval. Maximum 1.75 at +0.33 s, above it. Minimum comes first. |
| fig1h-syllable-dlight-differs | partially_reproduced | Cell 11: 518 pairs and P ≤ 1e-38 under all four readings, but H = 274–289 against 209 ± 21. |
| fig1j-weak-kinematic-correlation | reproduced | Cell 18: held-out \|r\| = 0.074 and 0.018 under (a), 0.060 and 0.006 under (b). All are below 0.3. |
| fig1l-identity-not-decodable | blocked (too_large) | Not attempted. The data are present, so a subsampled test is possible (part 4). |
| fig2a-food-reward-transients | blocked (data_missing) | No food-reward sessions can be identified in the archive metadata (part 4). |
| fig2b-dlight-usage-across-syllables | reproduced | Cell 21: held-out r = 0.178, shuffle P = 0.001, n = 703 pairs. |
| fig2i-dlight-entropy-across-syllables | reproduced | Cell 23: held-out r = 0.199, P = 0.001. |
| fig2b-across-experiments | reproduced | Cell 25: held-out r = 0.197, P = 0.002. This uses 145 experiments where the criterion gives 379 (problem 5). |
| fig2e-dlight-predicts-future-usage | reproduced | Cell 33: one-sided P ≤ 0.002 at every n from 10 to 390. |
| fig2e-not-autocorrelation | partially_reproduced | Cell 34: at no n are both curves inside the shuffle band, so the reproduced rule fails. The autocorrelation turns significantly negative (z ≈ −4), which cannot explain a positive usage effect, so the not-reproduced rule is not met either. The criterion does not cover this case. |
| fig2g-usage-crosscorrelation | not_reproduced | Cell 39: reading (a) gives P = 0.10. Reading (b) gives P = 0.039 (0.034–0.054 over seeds), which nominally meets the partial rule, but that P is uncorrected for picking the peak among 31 lags, and its null is miscalibrated (problem 4). |
| fig2h-specific-to-syllable | not_reproduced | Cell 35: offsets −1 and +1 are also significant after Holm, with z = 4.3 and 5.2 against 6.7 at offset 0, so both the reproduced and the partial rule fail. |
| fig2k-dlight-predicts-sequence-variability | blocked (other) | Absent from both notebooks. It is not listed as blocked and was not attempted, although the data needed are loaded. |
| ed6b-encoding-model-average | blocked (other) | The notebook says "see the record", which I did not have. The data are present. |
| ed6e-encoding-model-instantaneous | blocked (other) | As ed6b. |
| ed7-dms-fewer-transients | reproduced | Cell 28: U = 100 (97 ± 9.7), DMS lower, P = 0.0016, Holm-corrected 0.0065. |
| ed7b-dms-transient-shape | not_reproduced | Cell 29: time-to-peak U = 32 against 4, and its Holm P = 0.058, so it is not significant. Width U = 20 against 16 ± 1.6. The significance pattern fails. |
| ed7d-dms-smaller-peaks | not_reproduced | Cell 30: movement initiations U = 51, P = 0.76; syllable transitions U = 77, P = 0.17. The paper has U = 110 and 109. |
| ed7-dms-no-usage-prediction | blocked (other) | "See the record". The data are present. |
| ed7e-velocity-both-areas | blocked (other) | As above. |
| fig3c-calibration | blocked (data_missing) | Confirmed in the archive (part 4). |
| fig3e-optoda-learning | not_reproduced | Optoda cell 6: U = 152, f = 0.63, P = 0.11. |
| fig3f-cumulative-counts | not_reproduced | Cell 8: U = 160, P = 0.062. |
| fig3e-learner-count | not_reproduced | Cell 9: 7 learners, against 9 ± 0.9. |
| fig3h-stim-post-correlation | partially_reproduced | Cell 11: learners r = 0.868 (within tolerance), P = 0.031, but with n = 7. Controls are also significant (P = 0.025). |
| fig3i-optoda-entropy | reproduced | Cell 15: Opto-DA first bin Holm P = 0.017 with higher entropy after stimulation; no control bin is significant. Caveat in problem 9. |
| fig3jk-post-predictable | not_reproduced | Cell 21, main reading (post day): the top-rank 95% bootstrap intervals include 0 (inbound −0.05 to 0.77, outbound −0.13 to 0.55). Only the stimulation-day variant meets the rule. |
| ed10-target-specific | blocked (other) | "See the record". All the inputs are already loaded in optoda.ipynb. |
| ed10d-optoda-vigour | blocked (other) | "See the record". It can be tested in part (part 4). |
| ed10e-no-duration-change | reproduced | Cell 23: P = 0.94 and 0.56. This rests on 7 learners. |
| ed10i-no-place-preference | partially_reproduced | Cell 25: under the criterion's two tests, by pair (P = 0.31) and by mouse (P = 0.52), it is reproduced. The notebook's experiment-wide test, which is closer to the paper's "experiment-wide" statistic, gives P = 0.005, with Opto-DA JSD lower than controls (f = 0.20). |
| fig3l-no-kinematic-effect | reproduced | Cell 17: no Opto-DA bin is significant for any variable, and none in the per-mouse variant either. |
| fig3m-long-stim-velocity | not_reproduced | Cell 19: every Opto-DA bin has Holm P = 1.0, with f from 0.43 to 0.55. |
| fig4b-endo-da-influence-consistent | blocked (other) | "See the record". The ChrimsonR baseline and stimulation files are present. |
| fig4c-endo-da-predicts-learning | blocked (other) | As fig4b. |
| fig4f-catch-dlight-predicts-learning | blocked (other) | As fig4b. |
| fig4h-decoding-model | blocked (other) | Not attempted. The DLS baseline data are present. |
| fig4h-additive-model-optoda | blocked (other) | Not attempted. The data are present. |
| fig4i-extra-da-matches-calibration | blocked (other, not data_missing) | The criterion's comparison distribution is the evoked peaks of stimulated trials in the 250-ms ChrimsonR stimulation experiments, which are in the archive. The calibration mice are not needed. |
| fig5-rl-model | blocked (other) | Not attempted. The data are present. |

No chance level stated in the paper applies to any tested selection; the only one, fig1l's decoding chance, is blocked.

### B. Problems

1. **[affects a conclusion]** Photometry cell 3 checks label/photometry alignment once, pooled over all 14 mice. The best label shift there is −6 samples (H = 941 against 888 at 0). Per-mouse syllable peaks split by group (cells 13 and 30): dls-dlight mice give 2.8–5.0, while dlight-chrimson mice give −4.2 to 2.8, below several DMS mice. A clock or processing problem in the reinforcement-photometry files was never ruled out, and it would weaken fig1f, fig1h, ed7d and the Fig. 2 analyses.
2. **[affects a conclusion]** `movement_onsets` (cell 10) multiplies the derivative by FS before cubing. On synthetic noise this yields about 1,400 "initiations" per 30 min; the data give roughly 700 per experiment. These are not the Methods' "stillness to movement" transitions, and the movement-aligned dLight is a dip in all 22 mice. This drives fig1f reading (b) and the movement half of ed7d.
3. **[affects a conclusion]** In fig2h (cell 32), each offset's 10-syllable window overlaps the offset-0 window, and neighbours of a repeated syllable co-vary with it. The test is the criterion's, but the significance at ±1 may be structural. The notebook shows no check of this.
4. **[affects a conclusion]** `fig2g_run` reading (b) permutes dLight across overlapping sliding windows. That destroys the autocorrelation that the observed curve keeps, so the null is too narrow: z reaches −4.3 at +6 min. P is also taken at the lag with the largest z, with no correction across lags.
5. **[affects a conclusion]** The experiment set is 145 experiments (code reading) or 204 (Methods reading). The paper and criteria give 216 (Fig. 1b) and 378/379, and the notebook never reconciles these. Taking only the first `ts_session_number` per file (cell 2) can misclassify files that serve as baseline for one target and post day for another. Quality-control reading (b) was never run, though the claims file requires it. The dF/F maxima run up to 22,798%, so the code's "raw dF/F > 1.0" rule could drop many files.
6. **[affects a conclusion]** fig1e (cell 37): the 20-s centred sliding z-score in `process_dlight` removes slow dLight variation. That could suppress the long-timescale positive amplitude correlation. Whether the paper's Fig. 1e signal had this window is unchecked. The integer-bin variant the criterion asks for is also missing.
7. **[affects a conclusion]** fig3e, fig3f and the learner count: the Monday-baseline variant the criterion names was not run, and the overlap with the paper's nine learners was not reported. All learner-based claims (fig3h, fig3jk, ed10e) inherit the 7-mouse set.
8. **[affects a conclusion]** ed10i: the claims file reads the paper's "experiment-wide" statistic (n = 32 mice) as per-mouse means of the target-onset JSD. The paper describes experiment-wide locations, which is what the notebook's extra test computes. This is a misreading in the claims file. The notebook's experiment-wide result is significant in the direction opposite to a preference, which suggests a rig or coordinate difference between groups that was never checked.
9. **[does not affect a conclusion]** fig3i: stimulation trials outnumber catch trials 3:1, so the plug-in entropy has a sample-size bias. Controls also show stim > catch in every bin (f 0.51–0.58). The Opto-DA first bin is still significant.
10. **[does not affect a conclusion]** `jsd` (optoda cell 25) returns a negative value, not NaN, when one histogram is empty; on a synthetic input it gives −0.92. The runtime warnings show this happened for a few pairs.
11. **[does not affect a conclusion]** `fig2e_table` requires 390 following syllables for every n. Segment 5 (1,680–1,800 s) is therefore empty ("Mean of empty slice"), and z is averaged over 4 of the 5 segments.
12. **[does not affect a conclusion]** In `fig1e_run`, experiment–bin pairs skipped for zero s.d. still count in `cnt`, which pulls the null toward 0.
13. **[does not affect a conclusion]** ed3c uses RANSAC with an intercept. The criterion cites fig_s03 cell 15, which fits without one, and the notebook does not state the deviation.
14. **[does not affect a conclusion]** fig1j uses 5 cross-validation repeats instead of 100 and a raw-Pearson null instead of a Huber one. Both deviations are stated and do not matter for the \|r\| < 0.3 rule.
15. **[does not affect a conclusion]** ed2a reading (b) uses only the Opto-DA files, not all open-field experiments as the criterion says.
16. **[does not affect a conclusion]** In the claims file, fig2e-not-autocorrelation tests n ≥ 10 syllables (about 5 s). That cannot resolve the paper's "few hundred milliseconds", and the criterion has no rule for a curve that turns significantly negative.

### C. What I could not check, and the output that would settle it

- **Alignment:** the clock-shift H check per mouse, or per group (dls-dlight vs chrimson), and the timestamp offsets between syllable labels and photometry in reinforcement-photometry files.
- **Experiment set:** the number of files excluded at each step and their reasons; the quality-control (b) metrics; the count of files with raw dF/F > 1.0.
- **Movement onsets:** detections per minute and a movement-onset-aligned speed average showing a rise from rest.
- **ed3c:** keypoint `starting_time` and series lengths against the photometry timestamps. The notebook pairs them by sample index without checking alignment.
- **fig2g:** P under a max-over-lags null, and reading (b) with a block or circular shuffle.
- **fig3e:** the Monday-baseline variant, and the learner overlap with the paper.
- **fig3m:** stimulated and catch trial counts per arm in the 3-s files, and confirmation that light followed stimulated detections there.
- **ed10i:** per-group arena coordinate ranges, and the count of empty histograms.
- **Blocked claims:** the reasons in the attempt record. Without it I cannot judge fig2k, ed6b/e, ed7-no-usage, ed7e, fig4b/c/f/h, fig5, ed10-target and ed10d beyond the fact that their data exist.

### Part 4: archive check of the blocked claims

The archive (asset list and per-asset metadata only) has 1,942 NWB files and 69 subjects.

- **fig3c:** only 8 dlight-chrimson subjects are present (1–6, 8, 9). No two calibration mice and no open-loop session descriptions exist, so the claim as defined cannot be tested. The 250-ms closed-loop stimulation sessions (87 "Stim session" reinforcement-photometry files) would give evoked peaks only as a proxy.
- **fig2a:** no session description mentions food or reward. The spontaneous half (reading b, all DLS baseline experiments) is testable; the reward half is not.
- **fig1l:** the data are present; a subsampled random forest is feasible.
- **ed10d:** 20 velocity-modulation stimulation sessions state a direction ("-up" 12, "-down" 8, mice 5891–5894). The 34 others do not, so the claim is testable in part.
- **fig4i, ed10-target-specific, fig2k, the encoding, decoding and RL models, fig4b/c/f:** the inputs are present. These blocks are computational or unexplained, not missing data.
