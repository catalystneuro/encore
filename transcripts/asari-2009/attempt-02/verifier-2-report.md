**Verifier report, round 2: Asari & Zador 2009 (doi:10.1152/jn.00577.2009) on CRCNS ac-1**

The claims file has 21 claims. The attempt record has 21 outcomes: 8 reproduced, 6 partially reproduced, 4 not reproduced and 3 blocked. Nine outcomes are marked `assumed: true`.

### 1. Outcomes

I agree with 19 of the 21 outcomes. I disagree with fig8a-proportion-by-property, and fig8c-relative-effects stands only with a caveat.

- **methods-recording-counts, partially reproduced: agree.** The record writes 0 as the "measured" value for the two voltage-clamp counts. Those quantities were not measured, so they should be left empty.
- **a1-mgb-firing-rates, partially reproduced, assumed: agree.** The assumption is stated: the outcome rests on the robust-threshold detectors, since the authors' detector gives 4.992 Hz.
- **fig2-example-reliability, reproduced: agree.**
- **fig2-example-long-context, reproduced, assumed: agree.** The assumption (match on the two mean correlations, not the SDs) is stated and reasonable. Under the stricter reading the claim would be not testable, not failed, and the record says so.
- **fig3a-proportion-significant, not reproduced: agree.**
- **fig3a-significance-decay, partially reproduced, assumed: agree.** The assumption (non-negative sizes) is stated and reasonable.
- **fig3b-fractional-power-decay, reproduced, assumed: agree.** The assumption (silence counts as a context, as in CxtDep.m) is stated and reasonable.
- **timescale-longer-than-membrane, reproduced: agree.**
- **fig4-predictability-upper-bound, not reproduced: agree under the criterion as written.** The 1 − Q reading is still open (point 3 in part 3).
- **fig4-strf-performance-low, not reproduced, assumed: agree, with a caveat.**
  - The outcome rests on computing validation performance over the pooled folds. The authors' STRFanalysis.m averages over folds, and elsewhere this attempt takes open details from the authors' scripts.
  - The only combination that meets the criterion is folds by stimulus (a reading the claims file names) with the fold average (strf cell 7: STRF at most 0.129, p = 0.202). With the code's own contiguous folds the fold average fails (means up to 0.83 and 0.86).
  - That combination gives negative LN performance (−0.11 to −0.20, strf cell 6), which does not fit Figure 4. That is a reasonable ground for rejecting it, but the record does not give it. The record should say the main reading departs from STRFanalysis.m in two places (pooling over folds, and which samples are scored) and give this reason.
- **fig5-example-conductances and fig6-conductance-decay, blocked (data_missing): agree.** Cell 5 now covers the experiment-3 files and the tuning curves.
- **fig8a-proportion-by-property, partially reproduced, assumed: I now disagree.**
  - The new Table 1 rebuild (cell 43) changes my round-1 view. The per-property reading (count probes for amplitude, frequency and higher-order; count probe x ensemble entries for AM and FM) reproduces 4 of the 5 Table 1 denominators exactly. It also reproduces the MHT sub-rows exactly: 71 and 57 (cell 43 output). The claims file says the populations follow the Table 1 columns.
  - Under that reading the order fails: AM 41/96 (0.427) and FM 29/82 (0.354) both fall below higher-order 64/131 (0.489), from cell 42. Only the higher-order count is within tolerance, so the outcome is not reproduced.
  - The partial outcome holds only under the uniform readings, whose AM and FM denominators (39 and 25) or amplitude, frequency and higher-order denominators (104, 120, 336) do not match Table 1.
  - The Table 1 legend says each row is a probe type. Counting further ensembles of natural probes as the MHT row conflicts with that, so the question to the authors stands. The record should report this reading.
- **fig8b-decay-by-property, partially reproduced, assumed: agree.** The partial rule holds under every reading, the mixed reading included (1.350, 0.784, 0.109, 0.278, 0.176 s).
- **fig8a-significance-fits, not reproduced: agree.**
- **fig8c-relative-effects, partially reproduced, assumed: agree with a caveat.** Under the Table-1 reading the higher-order interval [0.637, 0.826] overlaps the frequency lower bound of 0.792. The frequency point estimate is 0.907, so the partial rule holds only if "include 1" is read loosely for a point estimate. The record states this.
- **fig8-natural-synthetic-probes-alike, reproduced, assumed: agree.** The test is the claims file's.
- **fig9-mgb-fast-decay, reproduced: agree.**
- **fig9-example-first-bin, reproduced: agree.**
- **fig7-example-frequency-context, blocked (data_missing): agree.** Cell 64 prints every fragment. The (625, 2500, 10000, 40000) vector is the single split-band fragment DMR4, in recordings with no natural fragment. The Figure 7 legend itself does not say DMR, but the Methods do ("Figure 7A ... DMR frequency variants"), so the claims file is supported.
- **figs1-silence-probe, reproduced: agree.**

Every assumed outcome states its assumption in the record, the notebook Summary and the README, with one exception. The README row for fig2-example-long-context says "Reproduced" with no assumption, while the record and the cell 69 Summary give one.

### 2. Sentences the outputs do not support

- **Record, fig3b notes:** "Before the swapped fragment lists of 20051108-ha1-001 were corrected (data check), the same fit gave 0.46 and 1.7 s." The same figures appear in the metadata_error finding. No cell prints the uncorrected fit; cell 6 prints only the mismatch.
- **Deviation text in fig8a, fig8b, fig8a-significance-fits, fig8c and fig8-natural-synthetic:** "it is supported by Table 1, whose denominators it reproduces exactly for amplitude (95) and frequency (110) counting probes and for AM (96) and FM (82) counting probe x ensemble entries." This is support for the mixed reading, which the record says it dropped. Higher-order matches under neither count (131 or 336 against 137), and cell 43 shows the split by probe type does not match.
- **Record, fig3a-significance-decay:** "a negative fast component (-0.17 to -0.20 with 0.015 to 0.022 s) ... with a slow constant of 0.42 s." The range −0.17 to −0.20 includes the silence-left-out fits, while 0.42 s holds only with silence counted; without silence it is 0.22 s (cell 27).
- **Record, fig9-mgb-fast-decay:** "Size 5.3 (bin start)". Cell 58 gives 5.273 and 5.571.
- **Record, fig9-example-first-bin:** "the same 4 of 12" under robust thresholds. Cell 61 prints only the count, not which probes.
- **Record and cell 67, figs1:** "most within 0.1 s". Cell 66 prints only the first 12 of the 22 periods.
- **Cell 28:** "the fitted constant at the mean noise floor". The constant is fixed in the fit, not fitted.

All other numbers in the Result cells, the Summaries, the README and the notes match the printed outputs. That includes all of strf cell 9 and the strf notes.

The record states my round-1 reasons accurately and mostly in my words. Problems 6, 7, 8, 10 and 11 are folded into the right claims. The note in problem 1 that the families in cell 11 point the same way is left out, which is acceptable.

### 3. Round-1 points

**Resolved:**
- 2 (fig7): every fragment is now printed.
- 4 (fig4-strf not run): it has been run.
- 6 (tie handling): the CxtDep.m ranking code and the int16 scale are printed, and ties are rare.
- 7 (bounds on the fit sizes): stated.
- 8 (fig9 plateau check is nearly circular): the record now says so.
- 9 (helper details): stated, with the CxtDep.m psth code printed.
- 10 (the 9 extra A1 cells): resolved as far as the data allow.
- 11 (voltage-clamp check of the other files): checked.

**Remaining, bearing on a conclusion:**
- **1, now reversed, fig8a and fig8c:** as set out in part 1, the reading that follows Table 1 makes fig8a not reproduced. The record should report it and the deviation text should be corrected.
- **3, fig4-predictability:** whether 1 − Q is an allowed reading is for the claims file to decide. If it is allowed, the outcome becomes reproduced.
- **New, fig4-strf:** the outcome rests on pooling over folds, against the authors' STRFanalysis.m. The record should state the departure and its reason.
- **5, fig8c:** the trial-resampling reading has still not been run. With n-sized resampling neither reading meets the interval criterion, so this matters only if the entry reading were accepted.

**Not bearing on a conclusion:**
- Remove the measured 0s for the voltage-clamp counts.
- Fix the README fig2-example-long-context row.
- The claims file I was given already holds the amended fig2-example-long-context criterion, but its `checks` section does not record the amendment.
