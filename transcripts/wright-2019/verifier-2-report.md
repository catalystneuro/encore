**Round 2 verification: Wright & McDannald 2019 (eLife 45013), CRCNS pag-1, attempt wright-2019-01**

Counts come from the claims file and the attempt record. The claims file has 39 claims and the record has 39 outcomes: 32 reproduced and 7 partially reproduced. Nine outcomes carry `assumed: true`: fig1d, fig1s1a, fig5bc, fig5d, fig5s1, fig5e, fig5gh, fig5s1-ramping and fig6ef. Cell numbers below refer to the re-executed notebook.

**1. Outcomes and assumptions**

I agree with all 39 stated outcomes.

All nine assumptions are stated, and each comes with a deviation entry. I find all nine reasonable:
- **The primary reading is justified by the data check.** Cell 13 matches the paper's printed regression table on one Onset unit (rf03092316 SPK12a). The match is within 0.004 for Z firing with the trial's own baseline, within 0.003 for interval fear with a 2 s window and 0/0 = 1, and within 0.004 for total fear with a 20 s window.
- **fig1d** rests on 0/0 = 1. The table gives 1.0 on all 10 of the unit's 0/0 trials, which supports that rule.
- **fig1s1a** takes the 20 s window. That is the primary reading's total-fear window, and it is the one of the two windows that fails the baseline test (p = 0.017), so it was not chosen because it passes.
- **fig5d, fig5s1 and fig5s1-ramping** depend on detail 4 (which firing baseline is subtracted). The table fixes it as the trial's own baseline.
- **fig5bc, fig5e, fig5gh and fig6ef** depend on the poke windows and the 0/0 rule, which the table fixes.
- **fig5gh** holds on the primary reading, but the probability vs interval-fear correlation that it needs is only p = 0.035 (cell 115).

Two outcomes are "partial" by the author's judgement, not by a branch of the criterion:
- **fig2s1:** the criterion defines only "reproduced", with no partial branch.
- **fig3:** the criterion covers neither 3 pairs nor 0 negative betas. The record says so.

Both judgements are disclosed and reasonable.

**2. Text against printed outputs**

Nearly every number in the "**Result:" cells, the Summary, the README and the record notes matches the printed output. These do not:

- **fig2e, attempt record note and finding.** The note says: "Under no reading is the danger time at p < 0.00025 within 5.8 +- 0.58." This is false. With window ends, cell 62 prints 5.5 s (measure a) and 5.7 s (measure b), and both are within 5.22–6.38 s. The finding's wording "No reading gives the Bonferroni danger time of 5.8 s (4.5 to 4.7 s by window start)" is misleading for the same reason. The outcome still stands, because with window ends the danger time at p < 0.05 is 3.7 s, outside 2.8 ± 0.28. My own round-1 reason, as recorded, has the same error: "the danger Bonferroni time is 4.5–4.7 s" is true only for window starts.
- **Summary (cell 139).** "With the paper's methods they reproduce … most reported statistics to their printed precision." The printed outputs do not support this. Exact matches to printed precision are few: F = 7.16 (cell 100), F = 3.14 (cell 127) and the fig5i means (cell 118). Many values are close but not exact:
  - F = 595 against 592.00, and t = 12.3 against 12.36 (cell 18)
  - t = 5.05 against 4.54 (cell 47)
  - 1.89 against 1.94 (cell 44)
  - 7.00 against 5.20 (cell 134)
  - 0.51 against 1.02 (cell 131)

  Others miss widely: 3/20 against 13/20 (cell 137), and the fig2e times.
- **Summary (cell 139) and the record's code_mismatch finding.** "The cube's interval suppression ratios (cubeScript.m) use the 20 s baseline." Cell 13 prints only the 20 s baseline line and the NaN→1 line. Nothing printed shows that the interval ratios use that baseline.
- **fig6ef, record note.** "Earlier one reading differed in outcome, now two." I count the earlier readings the same way as the record's other "earlier" counts, which agree with the notebook for fig5d, fig5gh and fig5e: the 12 former readings plus the six with 2 s interval fear and 20 s total fear. On that count, two earlier readings had Ramping above Onset in cell 137, not one: former 2/2 with 0/0 left out and type baseline, and 2 s/20 s with 0/0 left out and type baseline.
- **fig5s1-ramping (cell 122).** "Under the former 2 s readings … the claim held in full in 6 of 12." It held in all 6 of the former 2 s readings; 6 of 12 is the count over all former readings. The wording is ambiguous.

The README's outcome groups add up to 8 + 11 + 13 = 32 reproduced and 7 partial, which matches the record. The record's `verifications` entries give my round-1 reasons and problem numbers faithfully, close to my own wording, including the fig2e error noted above.

**3. Round-1 points**

All eleven are resolved:
- **1 (fig6ef counts):** the outcome is kept as partial under the criterion's partial branch. The fourfold miss in the counts is now stated in cell 138 and in the record.
- **2 (fig1s1a window):** the outcome rests on the 20 s window, where the baseline test fails.
- **3 (fig3 near-threshold units):** cell 74 now prints them. Nine units with screen p from 0.025 to 0.046 could each supply a fourth pair.
- **4 (fig2s1):** cell 68 now prints the verdict "not met in full".
- **5 (Z-scoring forces negative correlations):** a within-neuron shuffle null was added (cells 77 and 83). The observed r values lie inside the shuffled range, and this is disclosed.
- **6 (gaps in the spike trains):** checked in cell 9. Spikes are stored only from 20 s before to 31–34 s after each cue onset. The session-rate reading was recomputed over those windows, and the cluster sizes are unchanged.
- **7 and 8 (reading sensitivity):** both are disclosed and need nothing more.
- **9 (waveform features):** the Onset neurons' features are now printed (cell 36). They can only be compared with the paper's figure, which was not supplied as a PDF.
- **10 (mixed ANOVA):** the A×B and A×B×G terms now match a sums-of-squares model comparison (cell 128).
- **11 (inter-trial interval):** recorded as a finding.

One item from my round-1 "could not check" list remains open: no second paper value tests the primary reading's poke windows. The author found none. It does not change a conclusion.

What remains that bears on a conclusion:
- **fig2e:** the record note and the finding should say that window ends put the danger Bonferroni time within tolerance. The outcome is unchanged.
- **fig4abc and fig4efg:** the correlations the criterion asks for are no stronger than the Z-scoring alone produces. The outcomes follow the criterion, which only asks for p < 0.05, so they stay as they are. A reader should take that part of the claim as not tested beyond what the procedure forces, and the Summary says so.
