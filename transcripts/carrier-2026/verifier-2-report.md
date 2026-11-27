**Verification report, round 2: Carrier et al. 2026 (doi:10.1152/jn.00294.2025)**

The claims file has 29 claims, and the attempt record gives an outcome for each of them: 17 reproduced, 1 partially reproduced, 2 not reproduced and 9 blocked.

### 1. Outcomes

I agree with all 29 outcomes. Notes on the ones that changed since round 1, or that need comment:

- **fig2f-cb-mixed-model, now reproduced (my round-1 outcome was partially reproduced).** I agree. Cell 51 now tests fixed effects only (`m.fe_params`). Under S-c, with frequency as the response and salinity as a number, temperature P = 1.5e-19, the interaction P = 0.00042 and salinity P = 0.158. That meets the criterion's "under one reading" with salinity at 1 df. Satterthwaite tests would raise the P values, which cannot push salinity below 0.05 or plausibly push 0.0004 above it. The criterion lets the reading be chosen after the fact. The notes say openly that the reading whose n matches the paper's (S-b, n = 11) gives salinity P = 0.022.
- **fig2i-cb-neuron-crash-counts, reproduced, `assumed: true`.** The assumption is stated, and it is reasonable. The criterion defines a neuron's crash as the step at which its bursts stop. Cell 39 shows that in all 9 ramps where all three neurons crashed, the spread is at most 1.0 °C, and readings ii and iii both give 9. Reading i, which requires exactly equal temperatures, gives 4, and the record says so.
- **fig8-invivo-rhythm-maintained, now blocked (methods_underspecified; my round-1 outcome was partially reproduced).** I agree.
  - By the letter of the claims file's rule it would be reproduced (58 of 58 exposures). But cell 83 shows shuffled traces pass the same rule in 0.901 to 0.992 of windows, so the rule cannot detect a crash.
  - The three calibrated rules give 53, 58 and 46 of 58.
  - Cell 84's spectrograms show near-flat crab traces, for example crab 10 at 0.25x and crab 19 at 1.25x. Crab 18 at 0.25x has a perfectly steady 2.4 Hz line with no subharmonic, which could be a rhythm or an artifact.
  - Without the paper's visual criterion, none of these can be decided.
- **fig1e-cb-salinity-crash-fractions, blocked: too_large (I had said data_missing).** I accept the change. Cell 5 shows the 21 inner zips hold salinity-series preparations, so the data are deposited. Cell 32's three counts are reported and match the paper.
- **fig5c-ha-mixed-model (partially reproduced), fig5d-ha-q10-salinity-unchanged (not reproduced), fig7e-species-crash-temp-1x (not reproduced).** I agree, from cells 61, 63 and 72. For fig5d, cell 63 shows the miss depends on which point the paper dropped: leaving one point out at a time, P is above 0.05 in only 60 of 214 cases. The notes say this.
- **The remaining reproduced and blocked outcomes** are unchanged from round 1, and I agree with them.

No other outcome rests on an unstated assumption.

### 2. Statements the printed outputs do not support

- **Cell 88 (Summary):** "The deposit holds the authors' analysis tables and Prism files, which reproduce the paper's Q10 statistics exactly." Cell 63 (Fig. 5D: F(1,210), P = 0.046 against the paper's F(1,209), P = 0.063) and cell 58 (PY on Q10 1.160 against 1.233) contradict this. The match is exact only for Figs. 2G, 2H, 3B and 7A to 7C.
- **Cell 88 (Summary):** "the analysis scripts the paper says are deposited are not in either record." Cell 25 and finding 8 say the 21 inner crab zips were read only at their start, so the deposit has not been ruled out.
- **Attempt record, fig5b notes and finding 5 (cell 86); cell 87 and cell 6:** "LP and PY burst files exist for 6 of the 19 preparations." Cell 5 lists `#_PY_bursts.txt` and `#_LP_bursts.txt` in 7 folders, including 061223/1X TEXT FILES, and `ghfhd_LP/PY_bursts.txt` in 021423. So at least 7, possibly 8, preparations have them. Cell 86 counts only the "For Analysis" folders. Cell 87 also calls these "the phase subset", which has 7 preparations (cell 58). The outcome does not change, because 7 or 8 is still below the paper's n of 12 to 18.
- **Finding 1:** "(both name 0.75x_ramp.smr from 329.541 s)". No cell prints this.
- **fig1e notes:** "the measured 1 to 5 MB/s". **fig5b notes:** "33 GB of Spike2 recordings … about 15 min to read". No cell prints either figure. Cell 76 says the in vivo section "takes about five minutes", while cell 77 prints 6.8 min.
- **Cell 55:** "the interval the paper gives for n = 19". The notebook's Wald interval is [1.29, 1.59]; the paper's is [1.30–1.59]. The difference is small, but the wording should not say they are the same.
- **Cell 71:** "the range of the deposited Prism fit". The 1.25x Prism CSV is not printed.
- **fig8 notes and cell 85:** "a harmonic at 2.6 Hz" is visible only in the cell 84 figure. I checked the figure and it does show it.

Everything else agrees with the outputs: every other "**Result:**" cell (29, 31, 36, 38, 40, 42, 45, 47, 49, 52, 57, 59, 62, 64, 67, 69, 73, 75, 85), the rest of the Summary, the entry README and the remaining notes. The README outcomes match the record.

**Round-1 reasons in the record.** The record states my round-1 reasons faithfully, close to my own words, including problems 2, 3, 4, 5, 8 and 9 and the section C requests. One small point: fig2i is recorded `agrees: false` although my round-1 outcome was "reproduced". This depends on the round-1 notebook outcome, which I did not see.

### 3. Round-1 points

Resolved:
1. The fig8 rule. All 58 spectrograms are now shown, calibrated rules were added, crab 18 was checked, and the claim was moved to blocked.
2. The fig2i reading. It was replaced and is computed in code, with a step-binned variant.
3. The mixed models. Failed fits are now listed and the 2 df of the factor reading is printed. A real error was found and fixed: the salinity test had included the salinity random-slope variance.
4. The fig5c Crash-mark subset now runs in cell 61.
5. Fig5d. The extra point was compared against the MATLAB and Prism data (as sorted value sets, not per preparation) and cannot be traced; the leave-one-out run was added.
6. The in vivo duplicates and the 32-min recordings are now findings.
7. The `.mat` statement now has output in cell 15.
8. The fig1e counts are now reported in cell 32.
9. The fig1d 9-animal variant was added in cell 30.
10. The `abf_signal` annotation is fixed (`stns.py:399`), and windows spanning a gap are counted.

All of the section C items were addressed.

What remains bearing on a conclusion: nothing that would change an outcome. Two things are worth recording:
- **fig7df.** The crab 1.25x test was not re-run with the unit-table value for 963_106 (26.0 °C in place of 36.0 °C). It would narrow the difference from 3.0 to 1.9 °C, so P can only rise and the "similar" outcome holds.
- **fig5b.** The count of preparations with LP and PY burst files should be corrected from 6 to 7 or 8.

### 4. Critical findings

- **Finding 1** (lobster 111122's 0.75x ramp is a copy of 120722's; output `finding-lobster-075-duplicate`, cell 15). The output shows it:
  - Identical Sheet4 values from 10 to 28 °C.
  - Identical columns (5, 8) in both `Lobster_Q10s_1x&075x.mat` `low` and the Prism Homam 0.75x sheet.
  - The two burst tables equal in all 4730 numbers.
  - Different recordings (910,496,768 and 703,075,328 bytes, different CRCs).
  - 111122's own 28 °C burst file gives 1.130 Hz where the table has 1.657 Hz.

  The only unsupported part is the "329.541 s" detail. `critical` is right: data are filed under the wrong preparation and one recording is counted twice in Figs. 5D and 7A, with nothing in the tables to show it. No `versions` or `fixed_in` are given.
- **Finding 2** (seven in vivo exposures are duplicates; output `finding-invivo-duplicates`, cell 79). The output shows exactly the seven pairs listed and "Exposures: 59; distinct recordings: 52". `critical` is right: recordings are deposited under two animals or salinities, which changes the per-salinity counts of animals, and the file names give no sign of it. No `versions` or `fixed_in` are given.
