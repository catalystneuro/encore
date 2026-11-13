**A. Outcomes**

The claims file has 40 claims. The notebook tests 28 and blocks 12: 11 on the kernel regression and 1 on histology.

| Claim | Outcome | Reason |
|---|---|---|
| fig1c-easy-performance | reproduced | Reading b (the dataset's `included` flag) gives 1.71% incorrect and 10.12% Misses, against 1.7 ± 2.5 and 10.1 ± 8.3 (cell 7). |
| fig1c-low-contrast-performance | reproduced | 5.07 / 29.84 under b, and also within tolerance under a (cell 9). |
| fig1c-competing-performance | reproduced | 20.01 / 13.89 under b (cell 11). |
| fig1d-reaction-time-difficulty | reproduced | Trials b, F1: p = 2.9e-10. The high-contrast class is shortest (0.206 s, against 0.226 and 0.221 s). Reading a fails (cell 13). |
| ed1q-wheel-choice-decoding | reproduced | Reading a gives 48.9% at −50 ms and 94.8% at +50 ms. Chance stated in the paper is 47.7%; at −50 ms 92% of velocities are zero, so reading a sits at 50% by construction. Reading b is 59% at −50 ms, which looks like the class prior; no per-session chance was computed (cell 15). |
| early-response-fraction | reproduced | Reading a gives 61.5% and 95.8%; reading b 67.5% and 94.9% (cell 17). |
| passive-no-movement | not_reproduced | 84.6 to 85.0% under all four readings, against 94.1 ± 0.6 (cell 19). |
| recording-counts | reproduced | Reading b: 29,283 neurons, 750.8 ± 38.0 per session, 22,434 or 22,273 localized. 39 sessions, 10 mice, 92 probes, 9,538 engaged trials (cell 23). |
| edtable1-region-counts | reproduced | Reading a: 38 of 42 regions pass, exactly the threshold. ACA, MOs, VPL and ZI differ. This depends on the parent-label mapping (problem 11; cell 25). |
| supptable2-sessions | reproduced | All 39 sessions found; sex and genotype match for 10 of 10 subjects; areas match in 38 of 39 sessions under reading a (Muller 2017-01-08 lacks MOs; cell 27). I checked the reference tables in the helper against the supplement's Word file: they match. |
| task-modulated-fraction | reproduced | 13,439 active (60.3%). Reading a gives 74.95% increasing and 20.89% decreasing (cell 29). |
| suppfig2-rate-amplitude | not_reproduced | The amplitude d' is 0.050 (a) or 0.060 (b), against 0.10 ± 0.02. The rate d' is within tolerance only under b (0.316); under a it is 0.392 against a bound of 0.39 (cell 31). The qualitative pattern, amplitude d' much smaller than rate d', holds. |
| fig2de-activity-order | reproduced | Under L1, for all three responsive readings: on contralateral trials VISp ranks 0.024, SCs 0.06–0.08 and the VIS mean ≤ 0.21; on ipsilateral trials VISp and SCs both rank above 0.70 (cell 34). |
| fig2fg-miss-restricted | not_reproduced | Under Z1 finite, conditions (i) and (ii) hold. Condition (iii) fails by about 0.00005: ipsilateral 0.0119 against a threshold of 0.0237/2 = 0.01185. The two sides are computed on different session sets (problem 1; cell 36). |
| fig5b-miss-more-than-passive | not_reproduced | Fails only on the session count: 36 sessions kept (or 38), against the required 34. Under Z1 finite the pooled Miss fraction exceeds the passive one, and 29–30 of 42 regions have a positive excess (cell 38). |
| fig5c-prestimulus-task-vs-passive | reproduced | Passive a, factors a: all 9 differing neocortical regions are lower, all 11 differing other regions are higher, VISp is lower and CP higher (cells 40–41). |
| ed6b-prestimulus-order | reproduced | 11 of 15 (a) or 12 of 15 (b) subcortical regions are ordered Passive < Miss < Go; 12 of 14 neocortical regions have Passive on top. Each group passes separately as well (cell 43). |
| fig5d-go-miss-matches-task-passive | reproduced | r = 0.64, p < 1e-5 (cell 45). |
| ed7f-detect-probability-engagement | reproduced | r = 0.515, p = 0.0005 (a) and r = 0.488, p = 0.001 (b), against 0.48 ± 0.048 (cell 47). |
| fig5f-engagement-index | reproduced | Mean 7.85 against 8.42 ± 0.84; p = 1.2e-5; 344 neurons per session. The expected session count is not met: 36 against 34 (cell 50). |
| fig5e-engagement-predicts-go | reproduced | Slope 0.44 with 95% interval 0.35 to 0.53 (cell 52). |
| ed9i-engagement-beyond-arousal | reproduced | Deviance test p = 2e-15 to 6e-20 under all readings (cell 54). |
| ed9cf-engagement-controls | reproduced | All four trial sets give Go higher with p < 0.005 under every reading (cell 56). |
| ed9k-engagement-vector-specific | reproduced | Go-Miss is larger for all four variables. Pupil, motion energy and inter-trial interval have p < 0.005; previous reward has p = 0.13 or 0.077, consistent with the paper's 0.096 (cell 58). |
| suppfig3-nonresponsive-neurons | reproduced | All three neuron sets give Go higher with p < 0.001 (cell 60). |
| ed7b-detect-probability-widespread | reproduced | 42 of 42 regions (a) or 40 of 42 (b) are marked above the 5% chance level (cell 62). |
| fig4d-jpecc-vis-leads | reproduced, weakly | Only the trials-b reading passes. VIS leads Frontal at 5 of 16 points before movement; the VIS–Midbrain lead near 0.1 s rests on one uncorrected point (0.08 s). The per-bin PCA variant fails (cell 66). |
| fig4d-jpecc-no-lag-frontal-midbrain | not_reproduced | One uncorrected point is significant (−0.12 s, p = 0.028 or 0.017); none survives Bonferroni. The criterion counts any uncorrected point (cell 68). |
| fig3c, fig3d, fig3e, ed4f, ed5h, fig4b, fig4c, fig4f, fig4fg, ed5g, ed7c | blocked (too_large) | The data needed are all in the files. The block rests on an extrapolated cost of 4.6 core-hours (1.1 h on 4 cores) against a "1 h" limit that I cannot find in my materials (cell 70). ed7c, and parts of fig3c and fig4c, could be tested without the full test (problem 2). |
| histology-alignment-error | blocked (data_missing) | Confirmed on the archive API: 39 NWB files with ephys, behaviour and pupil data, and no histology or DiI spot data. |

**B. Problems**

1. [affects a conclusion] fig2fg, cell 36. The contralateral Miss fraction uses the 19 sessions with at least 10 matched single-stimulus trials. The ipsilateral Miss fraction uses all 39 sessions, with unmatched and different trial counts. Z1 grows with the square root of the trial count, so this comparison is confounded, and the outcome turns on a difference of 0.00005.
2. [affects a conclusion] Cell 70 (the kernel block). The time estimate comes from one neuron in one session, using a per-session basis rather than the pooled one. Some of the blocked claims do not need the kernel test:
   - ed7c: the regional choice-probability pattern and the count of six excluded sessions need only `combined_cp` on Left against Right trials, which the helper already has.
   - fig3c: the median full-model variance explained needs only the full model (estimated at 2.8 h).
   - fig4c: the population counts per area group could be checked.
   - Only the 20.8% MOs share in ed7c needs fig4b.
3. [affects a conclusion] Definition M (`summarize`, cell 38) keeps 36 sessions, against the paper's 34. fig5b fails on this alone, and fig5f, fig5e and ed9* run on 36 sessions. Neither reading of "fewer than 10" gives 34, and the cause is not looked into: no list of excluded sessions is printed.
4. [affects a conclusion] suppfig2, `Session.__init__` and cell 31. Amplitude is taken as the mean of the file's `spike_amps` (unit not given). The paper says "mean spike waveform amplitude". This substitution is not stated as an assumption, and the failure of the claim rests on it.
5. [affects a conclusion; the claims file misreads the paper] fig5d and ed7f. The claims file makes these use the Figs. 3 to 5 set (through ed6b). But the Fig. 5d legend gives a neuron range of 130–1534, which matches the Extended Data Table 1 totals for PAG and MOs, i.e. all neurons. ed7f has a tight tolerance (±0.048), so the neuron set could change its outcome. It was not run on all neurons.
6. [affects a conclusion] fig4d-vis-leads, cell 66. The notebook reads the criterion as "at least one uncorrected point". Under that reading the VIS–Midbrain lead is one point at 0.08 s, found only under trials b. With Bonferroni over the 5 points near 0.1 s, baseline a survives (p = 0.003) and baseline b does not (p = 0.025).
7. [does not affect a conclusion] fig4d-no-lag, cell 68. The point at t = 0 is NaN, because the movement window ends at +0.05 s, so 25 points are tested, not 26. The uncorrected criterion comes from the claims file, which itself flags it as likely to give a false positive.
8. [does not affect a conclusion, unverified] `MIN_TRIALS_TYPE = 12` (steinmetz.py:30) is defined but never used. The definition-T rule of 12 Left, 12 Right and 12 NoGo trials per session is never applied.
9. [does not affect a conclusion] fig1c reading b, and `classify_trials`, use the dataset's `included` flag rather than the Methods' disengagement rule (the two agree on 98.3% of trials). The notebook says so, and the 9,538 count matches the paper.
10. [does not affect a conclusion] task-modulated-fraction, cell 29. It uses neurons N, which include the 13-per-session rule (22,273), instead of the criterion's set: the 42 regions at ≥ 0.1 Hz (22,434).
11. [does not affect a conclusion] edtable1 and supptable2 depend on `REGION_PARENT`, which maps subdivisions to their parent: SCig to SCm, COA, TT, PIR and DP to OLF, and so on. The mapping is stated, and it is consistent with the Allen hierarchy. With labels as given, supptable2 drops to 25 of 39 matching sessions. edtable1 was not run with labels as given, and it sits exactly at the 38-region threshold.
12. [does not affect a conclusion] ed9cf, cell 56, z-scores the index within session. The criterion uses the fig5f index as it is.
13. [does not affect a conclusion] The `inf` readings in cells 36 and 38 count every neuron with zero baseline s.d. and any post-stimulus spike as significant (about 21% of neurons), so those readings carry no information.
14. [does not affect a conclusion] The clock check fails for Tatum_2017-12-09 (cell 4). The session is not followed up and stays in every analysis.
15. Synthetic tests I ran on the helper functions all behaved as specified: `zscores`, `combined_cp`, `causal_smooth` (causal, sums to 1), `matched_contrast`, `classify_trials`, and the sign of `asymmetry` and `jpecc` for a known lead under both PCA modes. The Extended Data Table 1 values in the helper sum to 22,458 and 13,467, as the claims file says.

**C. What I could not check, and the output that would settle it**

- **The "1 h" limit behind the kernel block.** docs/protocol.md is not in my materials. The block needs a sourced limit, or the kernel test run on a subset of sessions.
- **Why M keeps 36 sessions.** I would need per-session counts of matched Go, NoGo and passive trials at each contrast, and the list of sessions dropped.
- **The 12-trial rule.** I would need per-session counts of Left, Right and NoGo trials under definition T.
- **Whether `spike_amps` is the paper's waveform amplitude.** I would need the units-table columns of one file, for example whether it has `waveform_mean`.
- **A fair fig2fg comparison.** I would need fig2fg rerun with the ipsilateral Miss fraction on the same 19 sessions and matched trial counts, and its values printed unrounded.
- **edtable1 with labels as given.** I would need edtable1 run without the parent mapping.
- **fig5d and ed7f on all neurons.** I would need both rerun on all neurons of each region.
- **ed7c's testable part.** I would need the Left-against-Right `combined_cp` per region and the number of sessions with fewer than 10 includable trials.
