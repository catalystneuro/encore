**Round 2 verifier report: schapiro-2024-01 (Schapiro et al. 2024, DRYAD:1rn8pk129 v310115)**

The claims file has 25 claims and the attempt record has 25 outcomes: 20 reproduced, 1 partially reproduced, 4 blocked.

### 1. Outcomes

I agree with all 25 outcomes.

- **Unchanged from round 1 and still right:**
  - figs1-ih-reduced-11c and figs1-ih-reduced-21c: blocked.
  - fig1e-two-saline-q10-same and fig1e-saline-q10-same-across-designs: blocked.
  - fig1f: reproduced on the deposited table.
  - All other "reproduced" outcomes. Every number moved a little once the gap cycles were left out, and none moved enough to change an outcome (cells 26–69).
- **fig4c-ptx-restores-frequency-change: partially_reproduced, `assumed: true`.** The record now gives my reason (cell 49). The assumption is stated in the deviations: 981_035's 21 °C value is taken within 0.5 °C instead of 0.3 °C. It is reasonable, because the paper reports N=6 with F(2,10), and the deposited summary has a 21 °C value at 20.70 °C (cell 9).
- **fig6a-lp-advances-cs: reproduced, `assumed: true`.** It was partially reproduced in round 1. I agree with the change.
  - The assumption is stated in the deviations and the notes: the "gap" cycles are left out. These are cycles that the deposited outlier removal leaves spanning two or more bursts while keeping a single cycle's period.
  - The assumption is reasonable, for two reasons:
    - Leaving them out shrinks the median phase difference from the deposited SummaryStatistics.mat five- to twelvefold, and the largest from 0.85 to 0.11 (cell 15).
    - Without them, the LP ON slope is 0.053 ± 0.052, against the paper's 0.05 ± 0.05. With them it is 0.010 ± 0.202 (cell 69). The paper's own spread matches the reading without them.
  - One direct check is missing. The notebook never fits slopes to the deposited per-experiment phases (TotalLPON_E and TotalLPOFF_E, already loaded in cell 15). That would show whether the authors' own values give adjusted p < 0.01.
- **matched-period-lp-earlier: reproduced.** Both readings now pass (cell 66). Reading (a) passes only because the gap cycles are left out (it failed with them in round 1). Reading (b) does not depend on that, so the outcome does not need the assumption.

### 2. Sentences the outputs do not support

- **Cell 8 still has the round-1 text and contradicts cell 10 and finding 3.** It says "they are two PD spike trains of one preparation and one session", and "the cell `finding-ptx-981-035-twice` shows it". No cell has that tag.
- **Cell 20 and finding 1: "its ConditionsKey lists 3 to 22 trials".** Cell 19 prints 5 to 22 trials. The "3" is a step count (array shape (1, 3, 300000)), not a trial count.
- **Cell 54 and the record's deviations for fig5b, Table 1, fig5d and lp-duty: O4 (b) is described as "every cycle of the first holding period … to the onset of the warming toward 13 C".**
  - The table in cell 54 shows reading (b) holding fewer cycles than reading (a) in many experiments: 969_088 saline 34 against 267, 969_068 Cs+ 20 against 113, 965_106 saline 526 against 543.
  - The likely cause is in `step_onset`: it treats the first cycle above 11.3 °C as the warming, even when that is a brief rise during the hold.
  - So round-1 problem 6 is not fully fixed. No outcome depends on it, because reading (a) decides each claim and reading (b) agrees with it.
- **Cell 44: "In 969_152 under Cs+ + PTX the cycles hold no LP spikes".** Cell 42 prints only NaN shares; the LP spike count is not printed.
- **Cell 44 and the fig2c notes: "981_007 has no spike file" is given as the reason no further Cs+ intracellular PD trace is available.** Cell 43 shows 981_007 has a PD intracellular channel, and the notebook detects spikes on such a trace for 981_037. The condition of 981_007 is not known, so the reason given is not the real limit.
- **Summary (cell 71): "keeping them changes no outcome but fig6a-lp-advances-cs".** The notebook prints no gap-kept variant for matched-period-lp-earlier, and none for fig2c (the response's "shares change by at most 0.02" is not printed). For matched-period, reading (b) passed with the gap cycles kept in round 1, so the statement is probably true, but this notebook does not show it.
- **fig6a-lp-advances-cs notes give the reading (b) LP ON p as "Wilcoxon adjusted p = 0.0005".** The test chosen by Shapiro-Wilk is the t-test, p = 0.0020 (cell 69). Both are below 0.01, so the outcome stands.

Everything else I checked matches the printed outputs: all other Result cells, the Summary, the README (its rows cover all 25 claims) and the record's notes. That includes cells 16, 24, 27, 30, 33, 36, 39, 47, 52, 56, 58, 60, 62, 64, 67 and 70.

**My round-1 reasons in the record:** the `reason` fields give them faithfully, mostly in my words. Problem 3 (`extract_bursts`) is not in any reason; it appears only in the author's responses.

### 3. Round-1 points

**Resolved:**
- 2: the burst-start comparison (cell 9) shows PD and PD2 are two rhythms, and the five-preparation variant is gone. The stale text in cell 8 above is left over.
- 3: the gap cycles are marked and left out, with the deposited code's reading kept as a variant.
- 4: O3 (b) is run, the stable-cycle rule of each reading is stated, and smoothing within the window is a variant.
- 5: the strict bound is stated and a ≤ variant is shown.
- 7: reading (c) is added and the step timing is shown.
- 8: the clock check is called weak, and most outliers are explained. Two (969_147 at 21 °C) are not.
- 10: the channels of all seven raw files are listed, and 981_037 is analysed.
- 9: recorded as a question for a reader.

**Remaining, bearing on a conclusion:**
- **fig6a-lp-advances-cs** rests on leaving out the gap cycles. Two things would settle it:
  - slopes fitted to the deposited TotalLPON_E and TotalLPOFF_E;
  - a printout of the deposited extractBurstFrequency_Final.m (not available to me), to confirm the port's outlier removal really matches it.
- **fig4c:** the 0.5 °C margin and the choice of post hoc test remain open (problem 1). This is the reason the outcome is partial, and it is correct as stated.
- **O4 reading (b) is truncated** in several experiments (section 2). No outcome changes.

### 4. Critical findings

No finding in the record is rated `critical`, and I agree none should be.

The nearest is finding 3: 981_035 holds a second preparation as `PD2`, and nothing in the files describes it. Cell 9 shows what the finding states. I would keep it `minor`: the second train sits under its own variable name, so a user sees it, and the deposited summaries enter it as a separate experiment.
