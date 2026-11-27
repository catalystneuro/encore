None of the 25 outcomes changed: 20 reproduced, 1 partially reproduced, 4 blocked. The verifier agreed with every outcome, no finding is rated critical, and none of the fixes gave a reason to propose a change. The clean re-run passed (`python tools/entry.py all entries/schapiro-2024`, 0 errors). Only the timing cells differ from my test run, and every conclusion was checked against the new numbers.

**Outputs the verifier asked for (all now in the notebook):**
- **Slopes fitted to the authors' own per-experiment phases** (SummaryStatistics.mat), tested the way their deposited script does. LP ON in Cs+ advances 0.054 ± 0.055 per 10 C with adjusted p = 0.0004, and LP OFF in Cs+ 0.140 with p < 0.0001. That matches what leaving the gap cycles out gives, which supports the assumption behind fig6a-lp-advances-cs. The PD and PY slopes are not significant (adjusted p ≥ 0.056).
- **The outlier-removal lines of the deposited extractBurstFrequency_Final.m**, with a note on how the port follows them line by line.
- **Gap-cycles-kept variants for matched-period-lp-earlier and fig2c.** For matched-period, reading (b) still matches, but reading (a) fails with the gap cycles kept (LP advance 39 ms, below the 51 ms PD shortening). The summary now says the claim then holds under reading (b) only. For fig2c, reading (a) shares change by at most 0.015, and reading (b) gives 16 of 20 experiments instead of 17 of 20.
- **969_152 under Cs+ + PTX:** no LP spike falls within 30 s of the step onset, which is now printed.
- **981_007:** the real reason it cannot serve fig2c is now printed. Its temperature stays between 9.6 and 11.7 C over 187 min, so it has no warming step; "no spike file" was not the limit.

**Corrections:**
- **The holding-period end (O4 reading (b)) was cut short**, as the verifier suspected. The warming-onset detection in `pyloric.py` took a brief rise during the hold for the warming. It now ignores rises that fall back, and reading (b) ends the hold at the last exit from the 11 C band. 969_088 saline now holds 301 cycles (was 34) and 969_068 Cs+ 269 (was 20). Where reading (b) still has fewer cycles than reading (a), the gap is exactly (a)'s cycles in the first part of the warming (3 to 23 per experiment), printed per experiment.
- **The reading (b) numbers moved slightly** for fig5b, Table 1, PY, fig5d and LP duty cycle, and the notes now carry the new values. The old "19 experiments" for LP ON was wrong; it is 20.
- **The same onset fix moved two fig2c onsets** (969_068, 969_070), where the old rule had caught an excursion at the start of the window. The counts are unchanged.
- **Text fixes:**
  - The stale text in cell 8, including the missing cell reference, is rewritten.
  - The voltage-clamp trial count now reads "5 to 22 trials, 2 to 8 of them Cs+", in both the notebook and finding 1.
  - The fig6a reading (b) p is now the t-test's 0.0020, not the Wilcoxon 0.0005.
  - The summary's statement about the gap cycles now matches what is printed.
- **Record:** round 2 is added under `verifications`, with the verifier's reasons and my responses. The round-1 problem 3 (`extract_bursts`) is now in the verifier's own words in the fig5b round-1 reason.

**Not done:**
- The two unexplained differences from the deposited summary at 969_147, 21 C, are still unexplained.
- The fig4c open points (the 0.5 C margin and which post hoc test) stay a question for the authors; they are why that outcome is partial.
- No new reader question was needed, since the verifier reported no misreading of the paper by the claims file.
- `tools/publish_site.py` was already modified before this run, and I left it alone.

Nothing is committed.
