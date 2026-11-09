**Verifier report, round 1: Neupane, Fiete & Jazayeri 2024 (DANDI:000897, version 0.240605.1710)**

The claims file has 24 claims. The notebook marks 17 as tested and 7 as blocked. The archive API lists 30 files: 15 sessions, each with one `_behavior+ecephys.nwb` file and one `_ecephys.nwb` file. All 15 are recording sessions (A 6, M 9); there are no behaviour-only sessions.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1bc-produced-matches-actual | reproduced | Cell 10: median session slope is 0.872 in A and 0.860 in M, and every slope is positive (lowest 0.687, M 04142021). The criterion's rule is met. The deviation is that only the recorded sessions are in the dataset. |
| fig1e-immediate-generalization | blocked (data_missing) | Confirmed in the archive: the 30 assets are the 15 recording sessions only, and the generalization sessions came before the recordings. |
| fig2-periodic-proportion | not_reproduced | Cell 16: no reading puts either proportion within tolerance (paper 37.6% and 36.0%). The best reading, a2/own/methods, gives A 24.2% and M 17.0%. Rule b gives 78% and 58%, and its session maximum of 87–95% breaks the 49.5% bound. |
| fig2d-periodicity-at-065 | partially_reproduced | Cell 18: the a2 readings put 2–4 of 4 monkey×direction medians in 0.60–0.70 s (main reading 3/4; A dir −1 is 0.59 s). The a1 readings give 0–1 of 3–4, and the b readings 0/4 (medians 0.72–0.95 s). |
| ed3-no-eye-hand-periodicity | partially_reproduced | Cell 50: under every bootstrap and chance reading, all three signals are below chance at p < 1e-4, and none is above. The criterion's test is met, but only in monkey A (5 sessions). All three mean PIs at 650 ms are outside tolerance, and the eye PIs have the opposite sign: eye x 0.148 (paper −0.25), eye y 0.136 (paper −0.44), joystick −0.40 (paper −0.53). |
| ed2b-pi-navigation-above-iti | blocked (metadata_insufficient) | I agree. Cell 38 shows the gap from joystick offset to the next trial is about 0.9–1.3 s, with 0–6 gaps over 4 s per session. The only segments over 4 s are the post-abort gaps in monkey M (about 6.1 s). Using them would rest on an assumption the paper does not make. |
| ed2c-pi-error-below-correct | partially_reproduced | Cell 20: with the Methods' error trials (attempt 2), 3/4 groups meet p < 1e-4 under the code's neuron reading and 1/4 under the Results' reading. With the code's error-trial variant, 4/4 and 1/4. In all 16 rows correct > error, with p ≤ 0.012. |
| fig2e-first-peak-near-065 | partially_reproduced | Cell 46, Methods window: median first-peak mode is −0.645 s in A (within range) and −0.735 s in M (outside). The KS test passes under both readings (pooled p ≤ 1e-60; 66–73% of tested units have p < 1e-4). |
| fig2f-earlier-peaks-multiples | not_reproduced | Cell 47: second peak is −1.315 s in A (within) but −1.07 s in M. Third peak is −1.585 s in A and −1.66 s in M (expected −1.95). Neither partial clause holds cleanly: A meets only the second peak, M neither. My synthetic test shows the peak routine recovers −0.65/−1.30/−1.95 correctly, so this is a property of the data, not a bug. |
| ed4d-overshoot-longer-period | partially_reproduced | Cell 22: M overshoot > undershoot, Z = 3.13, p = 0.0017. A: Z = 1.31, p = 0.19. Same under both lag sets. |
| fig3b-onset-and-offset-coding | reproduced | Cell 28: the rule holds in all four window×monkey cells, against shuffled proportions of 0. It is a weak result: onset-only coding in A is 0.7–1.0% of units. |
| fig3d-offset-coding-stronger | partially_reproduced | Cell 30: in A, offset R2 > onset R2 (p = 2.8e-7 raw; 5e-14 with the 80%-PC denoising). In M the order reverses significantly (onset 0.79, offset 0.68; p = 7e-12). This outcome is subject to problem 3. |
| ed4e-rate-codes-distance-over-slope | not_reproduced | Cell 36: only 1 of 6 window×monkey cells meets the criterion (M, legend window). A never does; in the legend window A's slope F exceeds its rate F. |
| ed4fg-distance-over-landmark | partially_reproduced | Cell 34: 8 of 16 main comparisons reach p < 1e-4. Distance F is larger in every row, and the legend window with the paired test meets in all four. |
| fig3e-xcorr-conserved-iti | blocked (metadata_insufficient) | I agree, for the same reason as ed2b. |
| ed5-xcorr-conserved-other-epochs | blocked (other), but wrongly blocked | Its comparisons are MNAV against the inference epoch, against error trials and between directions. None of these needs the ITI. Only the neuron and session selection comes from fig3e, and that rests on the PI, which the notebook computes. |
| fig4h-periodic-fano-factor | partially_reproduced | Cell 41, reading sel_a: median periodicities are 0.69 s (A) and 0.66 s (M), within range. The proportions are outside tolerance: A 65.4% against 55.5%, M 52.3% against 43.8%. Reading sel_b puts A within tolerance, but not M, and M's median is 0.72 s. |
| ed8-fano-periodic-without-rate-periodicity | reproduced (conditional) | Cell 43: binomial p ≤ 1e-36 in both monkeys under every reading. It rests on a rate-periodic set that did not reproduce (fig2), and the 5% chance level is not validated (problem 8). |
| ed10-motor-preparation-signal | partially_reproduced | Cell 24: motor-responsive units are 75.5% (A) and 67.9% (M), within 10% of the paper's proportions, and so is motor-among-non-periodic (85.6% A, 85.5% M). The non-periodic proportions are outside tolerance (57.1% against 73.6%, 43.6% against 55.7%), inherited from fig2. All four proportions are above 50%. |
| fig4g-reset-model-fits-better | blocked (other: not attempted) | Not a data blocker. The 15 sessions' trial tables are loaded, so the two utilities models could have been fit on them, with the smaller n noted as a deviation. |
| fig4b-learned-landmark-input | blocked (other) | A simulation that needs no data; not attempted. |
| fig4d-model-subscalar-variability | blocked (other) | A simulation; not attempted. |
| ed6d-model-fano-periodic | blocked (other) | A simulation; not attempted. |
| ed5efg-tighter-phase-clustering | blocked (other) | The monkeys' side (peak lags of pairs) is computable from the data. The model side needs the fig4d simulation. |

Chance levels: the paper states no numeric chance level for the PI selection. For ed3 the notebook's GP chance at 650 ms is 0.205 (mean) and 0.25–0.28 (mean + 2 SD); the legend gives no value to compare against.

### B. Problems

1. **[affects a conclusion]** `mnav.null_from_bank`, cell 13 (global null). Every target trial has the same duration, so all picks come from the same 20 bank entries. That fixes the null mean to the mean of those 20 entries.
   - Synthetic test: the null mean varies across banks with SD 0.21, against a within-null SD of 0.09. So the threshold can be off by about 2 null SDs.
   - A freshly generated null (`surrogate_pis`, 106 trials) gives a rule-a2 threshold of about 0.15. The notebook's global thresholds are 0.265 (A) and 0.178 (M).
   - The global readings of fig2 (A 9.1%) are therefore too conservative. The own-duration null is affected less, but its thresholds are never printed.
2. **[affects a conclusion]** Cells 20 onward. Every downstream claim (ed2c, ed4d, ed10, fig2e, fig2f, ed8) is run only with a2/own/methods as the periodic set.
   - That choice is the author's. Reading a1 is arguably the literal reading of the claims file's sentence, and rule b is the Methods' wording; neither is propagated.
   - Fig2d shows the result depends on the reading: b gives medians of 0.72–0.95 s.
3. **[affects a conclusion]** `tdr_once`, cell 30.
   - Each unit is centred by its mean across both windows. The regression r = β·dist then has no intercept and an uncentred distance, so any difference in a unit's mean rate between the two windows loads onto β.
   - The Methods' "centred firing rate" per time point avoids this.
   - Synthetic test: an offset R2 of 0.99 drops to 0.83 when window means differ. This bears on the M reversal in fig3d.
4. **[affects a conclusion]** Cell 13, PI null. The claims file names the code's GP variant (GP mean = the neuron's trial rate, no Poisson step) and it is not run. All units also share one surrogate rate (the median: 1.65 spikes/s in A, 0.51 in M).
   - My test shows the a2 threshold barely depends on rate (0.136–0.160 for 0.5–15 spikes/s), so the shared rate is minor.
   - The unrun variant could still change the fig2 counts.
5. **[affects a conclusion]** Cell 39 and the summary table. ed5 is blocked as "depends on fig3e", but its comparisons do not use the ITI. fig4g, fig4b, fig4d and ed6d are blocked for run time, not for any data limit.
6. **[affects a conclusion]** Cell 49, ed3. Monkey M is dropped because its behaviour clock is offset. The cell-49 joystick-deflection check could have estimated that offset against `joy1onttl`; this was not tried.
7. **[does not affect a conclusion]** Cell 24, ed10. The t-test on 200 bootstrap means is pseudo-replicated: p < 1e-4 corresponds to an honest z of about 0.4.
   - Evidence: sessions where cell 7 finds no modulated unit (A 09172019, M 04132021, M 04142021) still show 76.6%, 64.5% and 47.3% "motor" units.
   - The criterion's test is followed, but the result says little about a motor signal.
8. **[does not affect a conclusion]** Cell 43, ed8. The binomial test against 5% assumes the Fano selection has a 5% false-positive rate. That rate is never measured, and sel_a selects 65% of A units.
9. **[does not affect a conclusion]** Cell 20, ed2c.
   - Correct trials (about 190 per group) outnumber error trials, and a noisier mean ACG lowers the PI. Neurons are also selected on their correct-trial PI.
   - So correct > error is expected even without a real effect. No control matched for trial count is run.
10. **[does not affect a conclusion]** `periodicity_table`/cell 13 ("own" null). Surrogates average over all of the session-direction's trials, not over the k trials each unit keeps. For low-rate units this makes the null too tight.
11. **[does not affect a conclusion]** Cells 7–8. Three sessions with no evidence of a shared spike/trial clock (A 09172019, M 04132021, M 04142021) are kept in every analysis. Per-session breakdowns are shown only for fig2 and ed10.
12. **[does not affect a conclusion]** Stated assumptions that look reasonable:
    - the 0.05 trial-rate threshold read as spikes/s;
    - 20 ms TDR bins;
    - the Fano time course ending at the shortest tp minus 0.5 s;
    - Type II ANOVA;
    - 650 ms read as 660 ms in the Fano PI.

### C. What I could not check, and the output that would have allowed it

- What `start_time` marks, and whether the trial table has a fixation or ITI event. Needed: the full column list of `intervals/trials`, and `start_time` compared against any stimulus column. This decides whether ed2b and fig3e are really blocked.
- Whether `attempt == 2` rows hold the first attempt's `tp`. Needed: the two attempts' `tp` and joystick times on a few multi-attempt trials.
- How biased the own-duration nulls are. Needed: the per-group own-null thresholds, and one group's threshold set beside a freshly generated null.
- Each unit's k against its session-direction trial count, to size problem 10.
- The downstream claims under readings a1 and b, and fig2 under the code's GP variant.
- fig2e/f: per-unit inter-peak intervals, and the peak results excluding A 09172019.
- fig3d with centring per time bin, and fig3d excluding distance 1 (the Methods' own control).
- The monkey M behaviour-clock offset, estimated from joystick deflection against `joy1onttl`.
