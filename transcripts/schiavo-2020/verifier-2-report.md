I agree with all 44 outcomes in the attempt record. The record now resolves almost all of my round-1 points. What remains is mostly wording that claims more than the printed numbers show, and one check whose result runs against the "no response" summary.

**1. Outcomes (44 claims in the claims file and 44 in the attempt record: 1 partially reproduced, 1 not reproduced, 1 reproduced, 41 blocked)**

The 41 blocked claims are 22 metadata insufficient, 12 data missing, 5 other and 2 methods underspecified.

| Claim | Agree? | Note |
|---|---|---|
| subject-group-link (partially reproduced) | Yes | All 54 subjects now have a group. 7 of the 9 group counts match the paper. The chronic-cohousing group has 14 mice against 13, the paper's 12 naive excitatory mice can't be picked out of 23, and no file says which call was played on each trial (cell 22). |
| fig1g (not reproduced, assumed) | Yes | Both of the claims file's readings find nothing at 175 ms (cell 25). The assumption, a peak 2–30 ms after each pulse against the 5 ms before it, is stated and reasonable. |
| fig1i, ed5b (blocked: methods underspecified) | Yes | The readings disagree (cells 30 and 33). |
| ed6ef, fig2h, fig2i, fig2j, fig2k (blocked: other) | Yes | The inclusion-rule check decides it. 3.9% of call trials pass against 3.7% of pre-call trials, and the rule keeps 1 (or 0) of 39 cell recordings (cell 14). The pre-call window shows the same experienced-versus-naive difference (cell 40). The rule needs its own definition of a significant PSC (k s.d. of the pre-call measure); that is stated and reasonable. |
| ed9b (reproduced, assumed) | Yes, as flagged | The assumption (Dunn's test on the five baseline-vs-post pairs, Bonferroni over five) is stated and fits the legend's one p per stimulus. With all 45 pairs, or with Wilcoxon tests, the outcome would be not reproduced. The record says so. |
| 34 claims blocked for data missing or metadata insufficient | Yes | No misreading of the paper by the claims file found. |

**2. Sentences the numbers do not support**

- **"No current that follows the calls."** Check (3) in cell 14 finds a sweep-locked deflection in 13 of 110 files where 5.5 are expected. That is a binomial p ≈ 0.003, and 9 of the 55 morph-set EPSC files give p ≈ 0.0015. Check (1) also shows one naive EPSC cell responding strongly: 190326_e1, 26.4 pA, 40 of 40 trials in the expected direction. These sentences therefore go too far:
  - Summary (cell 57): "under every check run, about as many cells respond as chance gives".
  - Cell 16, which lists the 13 of 110 against 5.5 among the null results.
  - README: "show no current that follows the played calls".
  - Record notes and the "other" finding ("in the in vivo whole-cell recordings the current does not follow the played calls"), which also cite the 13 of 110 as if it were chance.
  - Response to ed6ef: "None finds call-evoked currents beyond chance".

  The blocked outcomes still stand, because the inclusion-rule check decides them. But the wording should say the currents almost never follow the calls, not never.
- **Out-of-date sentence in the imaging notes.** All 20 imaging notes, ed3e among them, say "The movies show no peak at the 0.1 Hz call rate from which onsets could be recovered". Cells 10–11 now say the 10.24 s trial period is found and "the phase of the trials could be recovered".
- **The "metadata_error" finding on the call rate.** 40 frames (10.24 s) is 0.098 Hz, which is the Methods' "0.1 Hz" rounded. It is also measured on only two call files and one tone file (cell 10). It is not an error.
- **Cell 11, "no clear cycle".** In the three-prototype file, folding at 3 × 40 frames beats the nearby periods by 0.050, against 0.033 at 1×, 0.024 at 2× and 0.026 at 6×. This is one file, and the excess at 3× is the largest seen. "No clear cycle" is a judgement, not a result.
- **Trivial rounding.** Cell 44 says "p >= 0.35"; the smallest printed p is 0.3472.
- **Checked and supported.** Every other sentence of the Result conclusions (cells 23, 28, 31, 34, 38, 41, 44, 47, 50, 54), the Summary, the README and the record notes matches the printed outputs. This includes the README's outcome counts (21 + 1 metadata insufficient, 11 + 1 data missing).
- **My round-1 reasons.** The attempt record states them in my own words, faithfully, for all 44 claims.

**3. Round-1 points**

- **Resolved:**
  - B1: groups are now read from the figshare titles.
  - B2: the onset is corrected, traces are drawn, and four checks plus the inclusion rule were run, giving the blocked outcomes.
  - B3: the expected-direction ranking was run, and the pre-call difference persists.
  - B4: the inclusion rule is applied and the seventh experienced IPSC cell is shown.
  - B5: labels and timing are printed, and the second control-window reading is added.
  - B6: the interval is now a median and the time-dependent gap is stated.
  - B7 and B8.
  - C, slice pulse timing: median offset 0.5 ms, 91.8% of pulses within 1 ms.
- **Remaining, bearing on conclusions:**
  1. **The 13 files of check (3) and cell 190326_e1.** They are neither listed nor drawn, and the latency of their deflections is not shown. A consistent latency after onset would mean a response the evoked window misses. That would not change the blocked outcomes (the inclusion rule decides them), but it is the one open check on the claim that the recordings lack evoked currents.
  2. **Wording.** The over-strong "no response / chance" wording in the Summary, cell 16, the README and the record (section 2) needs correcting, and so does the out-of-date imaging sentence in the 20 imaging notes.
  3. **Imaging call order.** Only one three-call file and one morph file were folded, and the 3 × 40 frame excess in the three-call file was not checked on other files. With no ROIs deposited, this is unlikely to change the 20 imaging outcomes, but the "cannot be recovered" statement rests on two files.
- **Remaining, not bearing on conclusions:**
  - Which 13 of the 14 first-retrieval mice, and which 12 of the 23 naive excitatory mice, are the paper's cannot be determined from the files.
  - 8.2% of slice pulses fall more than 1 ms from the computed time, up to 4.9 ms. That can put a 2 ms peak window over the stimulus artefact on a few pulses. It does not affect the fig1g outcome, where nothing comes near significance.
