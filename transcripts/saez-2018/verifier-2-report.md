# Verifier report, round 2: Saez et al. 2018 on CRCNS ofc-3

## 1. Outcomes and assumptions

The claims file has 28 claims, and the attempt record gives 28 outcomes: 9 reproduced, 4 partially reproduced, 9 not reproduced and 6 blocked (data_missing).

The opening line of my round-1 report gave "6 reproduced, 6 partially, 10 not reproduced". That was wrong. My own round-1 table had the same 9 / 4 / 9 / 6 split as the record.

I agree with 27 outcomes. I disagree with one.

**mixed-effects-robust: I disagree with not_reproduced.** The claims file says it is "Reproduced when, under one reading, every regressor has corrected p < 10^-4", and its opening comment lists baseline (a) as an allowed reading. Under baseline (a), one model per window with one regressor and all electrodes makes all 16 significant (cell 90: "one, all 16 … none" at corrected p ≥ 1e-4). The record's own finding says the same ("16 of 16 per window after subtracting each epoch's own 200-ms pre-event baseline").

- The implementation of baseline (a) is exact. Subtracting the window centred at -100 ms removes any constant per-trial offset, so applying it on top of the deposited correction gives the same values as applying it to uncorrected HFA.
- The record treats the deposited baseline as the only primary analysis. For fig4, fig5, figs5d and figs6b that choice gives the best outcome, which is consistent with "under one reading". For this claim it blocks a pass that a claims-file reading gives.
- The outcome should be reproduced, with `assumed: true`, resting on baseline reading (a) and the per-window Bonferroni reading.

**Assumptions (`assumed: true`):**
- **fig3-latency-duration-similar** (buttonpress epoch locked to outcome reveal): stated and reasonable, for the reasons in my round-1 point 3.
- **fig4-past-encoding, fig5-past-sustained, figs5d-sharp-boundary** (deposited HFA as the authors' baseline): stated.
  - It is reasonable for the game epoch, which is corrected over a pre-trial 200 ms.
  - It is weaker for the buttonpress epoch. Its per-trial offset differs from the game epoch's by -4.7 to 3.3 (cell 13), so it is not the same correction.
  - Under both claims-file readings all three outcomes would fall, so the flags are needed.
- **figs6b-stepwise-similar** (stepwise details): stated and reasonable.
- **fig7f-multiplexing, figs7-present-past-overlap**: stated, but neither outcome depends on the stepwise assumption. The 5-window selection fails as well, both the fig7f variant and readings (b) and (c) of figs7 (cells 79 and 82). The flag overstates the dependence; this is harmless.

## 2. Text against the printed outputs

Sentences the outputs do not support:
- **Cell 77 and the record (figs6b):** "the stepwise proportions are 0 for 10 of 16 regressors". Cell 76 shows 9 zeros: 6 current regressors plus past risk, past offer value and past chosen value.
- **README:** "the claims file's two baseline readings … change the outcomes marked as resting on an assumption". They do not change fig3-latency-duration-similar, fig7f-multiplexing or figs7-present-past-overlap, which are also marked (cell 90).
- **Cells 8 and 92 and the reveal.time finding:** "`reveal.time` is 31 to 47 ms after the button press in most rounds". Cell 7 prints only the range, 0.031 to 0.593 s, so the claim about most rounds is not shown.
- **Cell 88 and the record:** the fit "matches statsmodels MixedLM to the printed digits". Cell 85 shows small differences (SE 0.003467 against 0.003468; p 7.145e-20 against 7.271e-20; beta 0.468905 against 0.468908). The agreement is close but not exact to the printed digits.
- **Cell 44 and the record (fig3):** the own-null counts are "mostly below Table S2". All 8 are below (cell 43).
- **Cell 39 and the record:** "0.57 averaged, loss index with RPE". The pair behind the averaged maximum is not printed (cell 38).
- **fig3-latency-duration-similar note:** it reports only reading (a) under the baseline readings. Under baseline (a), reading (b) of the delays gives p = 0.034 (cell 90). The outcome holds because one reading suffices, but the note should say this.
- **fig5 note:** "past durations are about 500 ms shorter". The gaps run from 368 to 671 ms depending on the reading (cell 52).

Every other sentence I checked matches the printed numbers. That covers the Result cells 19 to 83, the baseline summary in cell 91, the Summary, the README table and the record's notes and findings.

**My round-1 reasons in the record:** they are stated faithfully and in my words. The fig5 entry repeats my round-1 statement that "none reaches p < 1e-6". That was my error: 8.0e-07 is below 1e-6, as the author's response says. The outcome is unaffected because the criterion needs all four comparisons.

## 3. Round-1 points

Resolved:
- **1, mixed-effects readings:** every combination is now run with the nested model, which is checked against statsmodels.
- **2, baseline:** both readings are run, and the mean offset between the epochs is printed.
- **4, stepwise:** the formal pass is now stated.
- **5, RT definition and s10:** now stated.
- **6, figs3a confound:** now stated.
- **7, fig2 circularity:** now stated.
- **8, non-timeout R2 variant:** added.
- **9, s03 electrode 42:** stated.
- **11, trial matching:** checked by a reverse match; no matched round is a timeout.
- **Section C items:** the variables in the .mat files, the mean offset between epochs, the unrun mixed-effects readings and the timeout-free HFA trials are all now printed.

Remaining items that bear on a conclusion:
- **mixed-effects-robust** should be reproduced (assumed) under baseline reading (a), as set out in section 1.
- **Baseline reading (b) is not cleanly applied to the buttonpress epoch.** Cell 90 subtracts the game epoch's pre-event window from a buttonpress epoch that carries its own per-trial offset (cell 13: -4.7 to 3.3, measured on 10 trials per subject). The (b) results therefore include that residual offset. No outcome turns on (b) alone: every change also occurs under (a), and (b) does not lift mixed-effects-robust above 15 of 16.

Other remaining items, which do not change a conclusion:
- **Point 3:** the claims file may misread the paper on the buttonpress epoch. Its criteria place outcome reveal at "button press plus 550 ms", while the Figure 3 and Figure 4 legends put t = 0 of that epoch at the gamble outcome. Its text says "buttonpress/reward events". The outcomes are unaffected because the notebook shows both timings.
- **Point 10:** the possible misreading of chance (the paper describes a per-electrode null) is passed to a reader in the questions file. The claim is tested as the claims file has it, with the own-null variant shown.
- I still did not inspect the figure image in cell 43.
