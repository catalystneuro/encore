**Round-2 verification: Markowitz et al. 2023 on DANDI 000559 (0.260528.0858)**

The claims file has 24 claims, and the attempt record gives an outcome for all 24:
- 12 have an outcome from a test: 7 reproduced, 3 partially reproduced, 2 not reproduced.
- 12 are blocked: 4 metadata_insufficient (fig3l, fig3m, fig3i, fig4f), 1 data_missing (fig2a) and 7 "other: not attempted".

The paper text is saved in `paper/` and was used to check the values the record quotes from it.

**1. Stated outcomes**

I agree with all 24.
- **fig1e-velocity-timescales, partially reproduced.** Cell 12: transient rate is positive at 47 of 100 timescales of 10 s or more; amplitude at 0 of 100.
- **fig1h-syllable-dlight-differs, partially reproduced.** Cell 16: H = 266.40, outside 209.29 ± 20.93.
- **fig1l, fig2b, fig2i: reproduced.**
- **fig2e-dlight-predicts-future-usage, partially reproduced.** This is no longer provisional. Cell 26 shows the same number of groups in the observed value and in every shuffle at every n, and 6 of 10 values of n up to 190 are significant.
- **ed7-dms-fewer-transients: reproduced.**
- **ed7-dms-no-usage-prediction: not reproduced, as the pre-set criterion requires.** Cell 30: significant at 9 of 10 values of n.
- **fig3e-optoda-learning and fig3f-cumulative-counts: reproduced.**
- **fig3e-learner-count: not reproduced.** Cell 36 finds 7 learners against the paper's 9.
- **fig3h-stim-post-correlation: reproduced.** Cell 37: r = 0.891, P = 0.017.
- **fig3l and fig3m: blocked, metadata_insufficient.** Cells 40–42: 9 of 12 controls are significant at 250 ms, and 2 of 2 at 3 s.
- **The other 10 blocked claims:** I agree with each.

**2. Sentences the printed outputs do not support**

Every "**Result:" conclusion (cells 14, 17, 20, 24, 27, 31, 35, 38, 43) matches the printed numbers. I checked the paper values the record cites against the paper text: 75 % of detections stimulated (Methods), 379 experiments (Methods), control P = 0.082 (Fig. 3h legend), 216 experiments (Fig. 1b legend), and U = 97 (Extended Data Fig. 7b legend). All match. The exceptions:

- **README run time.** "It takes about 16 minutes, 6 of them streaming 1,723 files." Cell 45 prints a run time of 13.1 min. Cell 3 prints 67 s plus 133 s of streaming, about 3.3 min. The file count (383 + 1,340) is correct.
- **dLight+ChrimsonR sessions.** The Summary (cell 44) and the record's data_missing finding say "Of the dLight+ChrimsonR mice, only the 250-ms sessions are present." No cell prints the pulse lengths of the dLight+ChrimsonR stimulation files: cell 6 leaves those mice out of `C`.
- **635-nm stimulator.** Cell 9, cell 44 and the record's metadata_error finding say "every closed-loop file states a 635-nm stimulator." Cell 6 prints this only for the 1,340 Opto-DA and control files, not for the dLight+ChrimsonR closed-loop files.
- **Rotated clocks.** The record's format_error finding says "with one backward jump of about a session length." No cell prints this. Cells 5 and 6 print only the counts (28 and 547).
- **Cell 38.** "Ranking by the log2 fold change gives 10." Cell 36 counts mice above the control maximum of log2 fold change; it does not rank them. This is a wording issue only.

The record's verification `reason` fields state my round-1 reasons accurately and in my own words, including the problems I tied to each claim (NaN shuffle, catch fraction, how the block was worded, binning, habituation, RF settings, P reporting). My two "not checked" points that had no claim (rotated-clock alignment and 378 against 177 sessions) do not appear in `reason`. They were addressed in the notebook (cells 8 and 5).

**3. Round-1 points**

Resolved:
- **Problem 1, NaN shuffle:** fixed, and cell 26 prints the group counts.
- **Problem 2, substitute catch set:** cells 40–42 add the stimulated fraction per mouse and per session, and a variant with catch trials at least 2 s from any pulse.
- **Problem 3, how the block is worded:** cells 0 and 43 and the record now give the outcome under the literal criterion and rest the block on the catch fraction and the controls.
- **Problem 4, one-sided P:** fixed in cell 37.
- **Problem 5, binning:** fixed in cell 12.
- **Problem 6, habituation sessions:** now left out (cells 5 and 10).
- **Problem 7, RF settings:** listed as deviations.
- **Problem 8, P reporting:** fixed.
- **Rotated clocks:** cell 8 splits the pulse-alignment check by clock, 0.938 and 0.936.
- **Session counts:** cell 5 tabulates sessions after each filter (177 against the paper's 379).

Remaining points that bear on a conclusion:
- **ed7-dms-no-usage-prediction.** The paper's Extended Data Fig. 7 has no lagged future-usage test. Its support for this claim is the encoding model (7e) and the panel title "does not correlate with syllable usage or entropy". The attempt's own across-syllable count test in DMS is not significant (cell 23: r = 0.026, P = 0.170), which agrees with the paper; the record's notes do not mention it. The fig2e-style test finds DMS stronger than DLS, and DLS is only partially significant. That pattern suggests the attempt's version of the test (equal time segments, no z-scoring to the shuffles) differs from the paper's. The outcome follows the criterion, but the notes should say this.
- **fig1h.** The cause of the H gap (266.40 against 209.29) is still unknown. The variants added in cell 16 rule out the quality filter and the post-session rule.
- **fig3e-learner-count.** The cause of 7 learners against 9 is still unknown. The per-target table in cell 36 shows a spread for 3442 and dls-ai32jr-1 similar to that of the control that sets the threshold, and no single cause.
