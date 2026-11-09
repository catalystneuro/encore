**Verifier report, round 1: Li et al. 2016 (doi:10.1038/nature17643) on CRCNS alm-3**

The claims file has 29 claims and the notebook covers all 29. My outcomes: 9 reproduced, 7 partially reproduced, 8 not reproduced, 5 blocked.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| units-and-sessions | not_reproduced | Cell 12: units 1012, sessions 20 + 38, mice 12 and pyramidal 890 match exactly. FS is 89 by label, 98 by width and 104 upsampled, against 72; intermediate is 33 or 24 against 50. The criterion only allows partial if class counts are within 10%, and they are not. |
| ed1-selective-fraction | reproduced | Cell 14, correct trials, lick-early excluded: 633, 176, 336, 493 (1.3 s response) and 635, 176, 336, 490 (1.5 s, reading b). All four counts are within 10%. |
| fig1d-late-delay-ipsilateral-bias | blocked (data_missing) | Cell 7: no recorded condition ends at the cue (latest offset is −0.31 s). The FAQ and the archive listing confirm that behaviour-only sessions are not deposited. |
| fig1d-earlier-photoinhibition-minimal | reproduced | Cell 37: early delay p = 0.23 and middle delay p = 0.22 (paired, pooled); every reading gives p ≥ 0.18, so none reaches p < 0.05. Performance drops 4.6 to 5.4 points over only 4 mice, and these are recording sessions, not the paper's behaviour sessions. Power is low. |
| ed3-recovery-interval | blocked (data_missing) | See item 4 below. |
| ed2b-silencing | reproduced | Cell 26, window (a): ipsilateral and bilateral reductions are 0.885 to 0.962 in every experiment. Exp 2 ipsilateral by line: VGAT 0.845, PV 0.951. Contralateral normalized rate 0.945, 0.986 and 1.152, all within 0.8 to 1.2. Under window (b) Exp 3 contralateral is 1.222 and fails. VGAT exp2b is 0.75 (item 8 below). |
| ed2d-spatial-extent | blocked (data_missing) | There are no recordings from untrained mice in the archive listing. |
| ed2e-no-rebound | not_reproduced | Cell 28: the population mean is not above control (p = 0.57 and 0.62). In the first 400 ms, though, 24 neurons are significantly excited against 9 suppressed, and the criterion needs fewer excited than suppressed. See item 13(i) on how the criterion reads the paper. |
| fig1f-rate-recovery | partially_reproduced | Cell 18: neuron counts are exactly 168, 168, 175. The fraction is 0.18, 0.20, 0.11 under reading (a) and 0.13, 0.14, 0.09 under reading (b), with means 0.161 and 0.122. Neither is within 0.10 ± 0.01; all are below 0.2. |
| fig1g-selectivity-recovery | partially_reproduced | Cell 20: with 200 ms windows stamped at their centre, all three recovery times are within tolerance in all four readings (e.g. 347, 420, 236 ms), and nearly every resample recovers. But the neuron count is 70 to 87 against 55 ± 5.5 in every reading, so this is not the paper's neuron set. |
| ed4-return-to-trajectory | not_reproduced | Cell 30, decreasing neurons, early delay: the RMS to time-matched control (0.526) is larger than the RMS to the end point (0.463), p = 0.019, the opposite direction, with 14 of 47 favouring time-matched. Pooled conditions: p = 0.18. n = 55 against 27. The window may be biased (item 2). |
| ed5-photoactivation | blocked (data_missing) | The FAQ says the photoactivation data were not published, and no such files are in the listing. |
| fig2b-bilateral-behaviour | partially_reproduced | Cell 39: ipsilateral 1 spot 69.3% is within tolerance. Ipsilateral 4 spots 75.6%, bilateral 1 spot 65.8% and bilateral 4 spots 58.1% are outside. Ipsi 4 spots against control p = 0.15, and bilateral 1 spot against ipsi 4 spots p = 0.12, with only 3 mice. The order control > unilateral > bilateral 1 spot > bilateral 4 spots holds. |
| ed6-bilateral-bias-inconsistent | reproduced | Cell 58: 8 sessions are biased, 6 towards lick right and 2 towards lick left. The sign agrees with the nearer control mean (reading b) in 0.88 with pyramidal neurons; it is 0.75 with all units and 0.62 under reading (a). This passes on one reading only, with n = 8. |
| fig2-bilateral-recovery | not_reproduced | Cell 22: ipsilateral rate recovers (ratio 0.958, 9.4% of neurons still changed). But ipsilateral selectivity reaches 80% before the cue in only 1 to 30% of resamples, and the deficit at −0.2 s is 0.48 to 0.58 in every reading. The rows flagged "within tolerance" are misleading (item 1). Contralateral (240 ms) and bilateral (no recovery) agree with the paper. Bilateral rate is 1.114 at the cue, outside 10%. |
| ed7-unilateral-4-spots-bilateral-1-spot | not_reproduced | Cell 24: bilateral 1 spot reaches 80% of control before the cue in 51 to 80% of resamples (335 to 557 ms), and the claim needs it not to. Neurons: 32 or 29 against 40 ± 4. Bilateral delta selectivity is larger than ipsi 4 spots, but p = 0.53. |
| ed7e-size-and-roc | not_reproduced | Cell 48: bilateral 1-spot ROC is 0.598 to 0.642, above the 0.594 limit (0.54 ± 0.054), in every reading. It passes only with the 0.08 variant tolerance. Ipsi 4 spots (0.62) is below Exp 2 ipsi 1 spot (0.71). Only 4 or 5 sessions. |
| fig3-cd-roc | reproduced | Cell 44: 16 sessions. Pyramidal neurons, leave-one-out split: 0.731, 0.713, 0.742, 0.592, all within tolerance but at the edges. Only 2 of 16 readings pass. |
| ed8-roc-during-photoinhibition | reproduced | Cell 46, reading (b), all units, code split: 0.703, 0.534, 0.642, 0.539, all within tolerance. Only 3 of 32 readings pass. |
| ed9b-cd-stability | reproduced | Cell 50: 0.590 ± 0.075 (pyramidal) and 0.622 (all units), both within 0.61 ± 0.05. |
| ed8a-mode-variance | partially_reproduced | Cell 52: the two cd values are within tolerance in several readings (e.g. pyramidal, random-half split, squared norms: 67.1 and 39.9). No reading has modes 1 to 5 at ≥ 98.0 variance and ≥ 94.6 selectivity together. |
| fig3-cd-predicts-movement | reproduced | Cell 54: in all four conditions accuracy is 0.67 to 0.73, binomial p ≤ 7e-12 and logistic p ≤ 2.5e-10. |
| fig3-other-modes | not_reproduced | Cell 56: the persistent and ramping modes predict control behaviour (binomial p = 0.003 and 0.002, pyramidal, code split). The ipsilateral persistent-mode shift (−2.09) lies inside the control s.e.m. band (2.17). No reading meets every condition. |
| ed9f-reaction-time | blocked (data_missing) | Cells 9 and 62: all 26 Exp 2 lick traces are noise-like (range 0.0018, against 0.05 in sessions that show licks). Part could be tested (item 4). |
| fig5b-callosotomy-behaviour | partially_reproduced | Cell 41: after the cut, unilateral photoinhibition lowers performance with p = 0.0033 (paired; 0.0071 using the mean over sessions), to 59.1%, within 58.0 ± 5.8. The before/after test and the interaction are blocked, as there are no sessions before the cut in the archive. |
| fig5-callosotomy-recovery | reproduced | Cells 34 and 60: ipsilateral rate is back within 10% (1.05 to 1.08), ipsilateral selectivity does not recover (0.3% of resamples), contralateral recovers in 297 ms (also 260 to 278), bilateral does not. Ipsilateral cd ROC 0.566 is reduced against both references (p = 0.006 and 0.003). 125 neurons against 129; 16 sessions. |
| ed10e-callosotomy-preparatory-activity | not_reproduced | Cell 32: 519 callosotomy pyramidal neurons against 496 (tolerance 0). The selective fraction is 12.7 to 14.3 points below control mice, more than the 10 allowed. The selective count (259 with all trials) is within tolerance. |
| models-monolithic-fail | partially_reproduced | Cell 64: the simple integrator (0.212, just over the 0.2 threshold), the monolithic attractor and the FORCE network all fail to recover in 3 of 3 draws. The corrective-feedback integrator and the tamed-chaos network were not simulated (methods_underspecified). |
| fig6-modular-models-robust | not_reproduced | Cell 66: the modular integrator does not recover on left trials (−7.2 against −14.4); the printed matrix causes this (item 5). The attractor's step-noise result passes, but the bilateral "random fixed point" check rests on states that have not settled. |

**B. Problems**

1. [affects a conclusion] Cells 16 and 22, `recovery_readings`. `within_tol` compares `recovery_ms` with the paper and ignores `frac_boot_recovered`. `recovery_ms` is the mean over only those resamples that recover. The two fig2 ipsilateral rows marked within tolerance (637 and 533 ms) come from 30% and 16% of resamples; the mean that counts non-recovering resamples is 821 to 840 ms. The same applies to fig5 contralateral (81% of resamples) and ed7.
2. [affects a conclusion] Cell 30, `ed4_rows`. The RMS window starts just after photoinhibition offset, but it uses 200 ms windows centred on each time, so the first 100 ms still includes photoinhibition and the ramp. For decreasing neurons this inflates the time-matched RMS and favours the end point; for increasing neurons it does the reverse. That may explain why the two directions come out opposite. Also, the end point is the window from −0.3 to −0.1 s, not the last 400 ms of the delay as the criterion says.
3. [affects a conclusion] Cell 15, `selection`. It counts a neuron as selective on the sample or delay epoch only, following the authors' code, and adds a filter |preference| > 1. The claims file (M3) defines selective as any of sample, delay or response. The counts for fig1g (70 to 87 against 55) and ed7 (32 against 40) are not explained.
4. [affects a conclusion] Cells 10, 16 and 20, the selectivity-trace method (M4). Each experiment runs only one screening rule: 5 trials per type for Exp 1, 10 per type elsewhere. The other screening reading, and setting the preference from the epoch where the neuron is most selective, were never run, although the claims file asks for "M4 with all readings". So the not_reproduced outcomes for fig2 and ed7 have not been checked under every reading.
5. [affects a conclusion] Cell 66 and `models.py`.
   - After bilateral silencing, 80 to 83% of attractor runs have not settled by 2 s. The sign of an unsettled state is close to a coin flip, so the 25 to 75% "wrong fixed point" test passes trivially.
   - The integrator's failure on left trials comes from the printed matrix itself: the recovery neuron only ever receives R − L, which is clipped at zero. I confirmed this by simulation. The Fig. 6c gating neurons do not appear in the 8 × 8 matrix, so the Methods may be underspecified here.
   - Under the per-unit-time noise reading, even unperturbed runs end on the wrong side 45 to 49% of the time, so that reading tells us nothing about recovery.
6. [could affect a conclusion] Cell 52, `modes_for`. Modes 2 and 3 and the lick right and lick left mean responses use correct and error trials; the claims file says correct trials. Modes 1 to 5 fall short by small margins (97.6 against ≥ 98.0, 94.3 against ≥ 94.6), so this could move ed8a.
7. [does not affect a conclusion] `alm3.population_session` drops a session only when a trial group has fewer than 5 trials, so it keeps groups of exactly 5. M6 says more than 5. The session count still matches (16).
8. [does not affect a conclusion] Cell 8. In four sessions the pyramidal rate after laser onset is 0.71 to 2.18 times the rate before, i.e. no silencing. These sessions are flagged but kept in every analysis without investigation, and probably drive the low VGAT exp2b reduction (0.75).
9. [does not affect a conclusion] Cell 62. The exp3 and exp2b sessions have lick traces that show licks, but ed9f was not run on them. It was run on callosotomy sessions instead, which are outside the claim; there it gives r = −0.025, p = 0.66, no relationship.
10. [does not affect a conclusion] fig3-cd-roc and ed8 pass on 2 of 16 and 3 of 32 readings, at the edges of tolerance. These are fragile passes, not robust agreement.
11. [does not affect a conclusion] I tested `recovery_time`, `boundary`, `auc`, `binned_window` and `lda_direction` on synthetic inputs, and all behave correctly. Laser timings in cell 7 match the onsets and offsets the notebook uses.
12. [does not affect a conclusion] The notebook takes method details from the authors' MATLAB scripts in the archive (e.g. the 1.3 s response epoch, the 5 or 10 screening trials). It says so, and each one sits within, or is shown alongside, the claims file's readings.
13. Possible misreadings in the claims file (reported, not corrected):
    - (i) ed2e: the criterion turns "a low level of sustained inhibition in a larger proportion" into a count of neurons suppressed at p < 0.01. Low-level inhibition need not reach per-neuron significance, and this decides the outcome.
    - (ii) The ED Fig. 2b legend gives Exp 3 n = 52, 52, 102. The 102 suggests the bilateral 1-spot neurons from the exp2b sessions were pooled into the paper's Exp 3. The claims file and the notebook use the exp3 sessions only, which bears on ed7 and ed7e.
    - (iii) ED Fig. 2b and ED Fig. 4 say Exp 1 used 6 mice. The data hold 4 unilateral mice, and neither the claims file nor the notebook mentions this.

**C. Blocked claims and what I could not check**

Blocked claims, checked against the archive's file list (224 keys) and the FAQ:
- **fig1d-late-delay, ed2d, ed5:** nothing in the archive can test them.
- **ed3:** the part on 0.5 s photoinhibition ending 0.8 s and 1.6 s before the cue can be tested with the recording sessions. Cell 37 already has it: p = 0.23 and 0.81, no significant effect. The 1.3 s photoinhibition and the condition ending at the cue are missing.
- **ed9f:** the 4 exp3 population sessions (and the exp2b sessions) have lick traces that show licks, so part could be tested.

What I could not check, and the output that would settle it:
- **ed10e:** whether 496 follows from a width-based class, because cell 12's width counts were not printed for the callosotomy units.
- **fig1g and ed7 neuron counts:** where the extra neurons come from. A count of neurons removed at each selection step would show it.
- **ed4:** whether the result is caused by the window problem (item 2). Re-running with the window starting at offset + 0.1 s, or with 400 ms end-stamped windows, would settle it.
- **fig2:** the control and ipsilateral selectivity traces at a few time points, and the two M4 readings that were never run.
- **ed2b:** the result with the four non-silenced sessions excluded, and the neuron counts against the legend's (117, 110, 109; 300, 294, 301; 52, 52, 102).
- **ed9f:** the `ts_channels` of the Exp 2 sessions, to confirm no other lick channel exists, and the test run on the exp3 sessions.
- **fig6:** the bilateral attractor run long enough to settle (e.g. 4 s), and the share of runs ending at each fixed point.
