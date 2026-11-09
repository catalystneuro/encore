**Round-2 verification: Siegle, Jia et al. 2021 (attempt 000253-siegle-2021-01)**

The claims file has 36 claims and the attempt record has 36 outcomes: 21 reproduced, 7 partially reproduced, 6 not reproduced, 2 blocked. Four outcomes are marked `assumed: true`: fig3i, ed9e, fig2f and ed7fg.

**1. Outcomes and assumptions**

I agree with all 36 outcomes. Three of them come with qualifications.

- **fig2f-directionality-vs-anatomy (partially_reproduced, assumed).**
  - Under the judged reading r = 0.827 with p < 1e-5. That is above the tolerance of 0.666 to 0.814 (CCG cell 21).
  - The criterion defines no partial outcome. Read literally, it would give not_reproduced. "Partial" fits how fig1g was handled, but the record should say the criterion names no partial outcome, as it does for fig1g.
  - The assumption (2 s window, all units) is stated and reasonable. But the outcome also depends on which mouse is left out (point 3, item i).
- **ed7fg-absent-in-spontaneous (not_reproduced, assumed).** The assumption is stated and its consequence is shown: with the Extended Data Fig. 1j filters the outcome flips (p = 0.54 and 0.46). The result is borderline:
  - p = 0.022 and 0.026 with DS averaged across mice;
  - p = 0.049 and 0.043 with pooled DS;
  - it is measured under a reading that gives 36% more sharp peaks than the paper (21,962 against 16,119).

  I accept the outcome as conditional, not firm.
- **fig3i and ed9e (assumed).** The preferred-condition assumption is stated and reasonable.
- **firing_rate_dg.** The main notebook's Summary calls its definition an assumption, but no outcome flags it. It enters every Figure 3 selection only as a > 0.1 Hz cut, so I expect little effect.
- **All other outcomes** are supported by the printed values and the criteria. This includes the round-2 changes: fig2-sharp-peak-pairs is now not_reproduced (cell 9), and fig3-unit-counts and ed10b are not_reproduced (main cells 58 and 67).

**2. Text the numbers do not support**

- **CCG Summary (cell 36) and the record's `selection_undocumented` finding.** Both say that no single mouse left out changes the outcome of fig2f. Cell 21 prints a leave-one-out range of r = 0.8024 to 0.8394. The low end is inside the tolerance (≤ 0.814), so leaving out at least one mouse would make fig2f reproduced. This bears on the conclusion, because the paper used 25 of the 26 mice.
- **Stale numbers in the record.**
  - The `code_mismatch` finding says "13,347 against 17,167". Main cell 58 prints 13,344 and 17,163.
  - The ed9bc notes say "157 of 13,347 units". Cell 61 prints 156 of 13,344.
  - The ed9a notes say "corrected p 0.45 to 0.93". The p_bh values in cell 34 are 0.444 to 0.902.
  - The ed9e notes give PM-AM 0.13, LM-LP 0.87 and RL-LP 0.53. Cell 46 prints p_bh 0.120, 0.879 and 0.537.

  None of these changes an outcome.
- **The record's "other" finding** says "the receptive field, latency and modulation results match the paper's". This overstates:
  - the hippocampal receptive-field fraction is outside tolerance (main cell 21);
  - per-unit latencies match the paper's table for only 16% of units (cell 24);
  - ed9e, the modulation-index pairs, is not reproduced (cell 46).
- **README.** "the scripts' windows give the paper's counts" should say counts within tolerance: 17,163 against 15,713 (cell 58).
- **Main cell 9** prints "fewer than 10 spikes … 0 of 65945". That is computed only over units that already have a p-value, so it is vacuous. The correct count, 4,267 visual and 3,352 hippocampal units, is in cell 21.
- **Everything else checks out.** All other "Result:" sentences, both Summary sections, the README and the outcome notes agree with the printed outputs.
- **My round-1 reasons in the record.** They are stated faithfully, mostly in my own words. Two things are off:
  - The `reviewed` text says "the nine CCG outcomes marked provisional". I marked eight; ed7e was blocked and not marked.
  - The count of 34 of 36 agreeing is correct: fig3-unit-counts and ed10b disagreed.

**3. Round-1 points**

Resolved:
- **B1, the jitter expectation at negative lags.** `ccg_group` now sets `G[-k] = G[k].T`. A brute-force check passes at 5e-9 for both lag signs (CCG cell 6). The outcomes were rerun, and fig2-sharp-peak-pairs and fig2f changed.
- **B2.** Each within-area pair now enters the reference once. File-order and doubled variants give the same 4 of 5 (cell 15).
- **B3.** One judged reading is used throughout, and the others are shown as variants.
- **B6.** 8,834 of the 15,958 kept units sit at the 1 ms bound; without them p = 0.85. The text now calls the test weak.
- **B8 and the claims-file note.** The 10-spike rule is applied, and the raw-MI variant gives 0.587.
- **D, ed7e.** All 325 probe files have y equal to z, so the claim stays blocked.
- **C items.** The AllenSDK's use of spike counts is reported from the AllenSDK source, which I could not check myself. The per-unit latency comparison has been added.
- **B7.** No change was made. That is acceptable, since the code it follows reproduces the paper's table.

Remaining points that bear on a conclusion:
- i. **fig2f and the 25 mice.** Some single-mouse exclusions put r inside the tolerance. The record should report how many do, and mark the outcome as also resting on which 25 mice are used. The contrary sentences in CCG cell 36 and in the finding should be corrected.
- ii. **B4, the latency table.** It is still unexplained (at most 16% of units within 1 ms). fig3-unit-counts and ed10b are not reproduced under the Methods' windows. Both reach tolerance under the scripts' windows or the paper's own tables (3 of 4 parts for ed10b). These two outcomes therefore may reflect a difference in procedure more than a difference in the data. That is stated, and the question is put to the authors.
- iii. **All CCG claims.** No reading reproduces the parent peak count, and the code's random-resample jitter variant was not run. The dependent outcomes rest on a reading with 36% excess peaks. This matters most for ed7fg, which is borderline and changes with the unit set.
- iv. **B5.** The mouse the paper left out is still not identified. This feeds item i.
