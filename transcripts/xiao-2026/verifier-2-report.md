**Round-2 verification: 001687-xiao-2026-01 (doi:10.1016/j.neuron.2026.05.027, DANDI:001687 0.260821.2126)**

The claims file has 41 claims, and the attempt record has one outcome for each. The record has 13 reproduced, 3 partially reproduced, 3 not reproduced and 22 blocked (16 data_missing, 6 metadata_insufficient). Cell numbers below are this notebook's; the cells moved since round 1.

## 1. Outcomes

I agree with all 41 stated outcomes. The record now carries my three round-1 disagreements: fig2-distance-tuned-counts, figs4ef-crossvalidated-stability and figs5de-svm-robust are not_reproduced, because their criteria have no partial clause.

- **Partially reproduced outcomes.** Each fits its criterion's partial clause.
  - figs4b-activated-increase-suppressed-decrease: the activated baseline is out under readings (a) and (b) (cell 33).
  - figs4l-temporal-windows-map: the offset count is 68 or 42, against 34 ± 3.4 (cell 45).
  - fig3c-decoding-by-distance: (a) fails only at 9 mm and (b) holds at 7/7 (cell 59).
- **Cutting claims.** Keeping fig4-cut-baseline-unchanged, fig4b-cut-wall-firing-reduced and fig4b-cut-per-unit-changes blocked is defensible.
  - The baseline result depends on the stability threshold: p = 0.0141, 0.29 and 0.251 (cell 75).
  - The fall in wall firing holds on every subset (cell 78). On the 79-unit subset (unstable sessions dropped, r ≥ 0.9) the n, both means and the test all meet the criterion (79, 12.70 → 8.88 sp/s, p = 1.25e-8).
  - The blocks therefore rest only on the undefined selection, not on the data.
  - The record files this as `blocked_by: metadata_insufficient`, but its finding is of kind `selection_undocumented`.
- **Assumptions.** No outcome carries `assumed: true`.
  - figs4j-ventral-location rests on an assumption that is stated but not flagged: that probe_site 1 is the tip. Cell 10 prints "(tip)" from its own format string. The electrodes-table column description that supports it is not printed.
  - The cut split (the longest gap between passes, `prv.split_cut`) is an assumption too, but it feeds only the blocked claims.
  - The SNR definition is stated as an assumption, and it affects only a variant.

## 2. Sentences the printed numbers do not support

- **Cell 49 and the figs4j notes:** "rank-sum p = 3.85e-25". Cell 48 prints p=3.48e-25.
- **Cell 57 and the fig3-overall notes:** "With window (ii) 4.5 to 9.5 s the map value is above its tolerance (78.62 and 78.79%, against 71.53 +/- 7.15)." The upper bound is 78.68, so 78.62 is within. Under 10-fold (ii) the value out of tolerance is the combined group, 67.77 against at most 64.41. Under 15 splits (ii) both map (78.79) and combined (69.61) are out (cell 56). This does not change the outcome, which is judged on reading (i).
- **Cell 72:** dropping the post-gap trials "changes the counts by at most 2 units (pass-set variant (ii))". That holds for BH-FDR, but the uncorrected variant's untuned count goes from 403 to 406 (cell 18).
- **Cell 72 and the record's metadata_error finding:**
  - "matching raw passes 21 to 220 and 51 to 250" and "realigning to raw passes 1 to 200 abolishes the tuning" appear in no output.
  - Cell 71 prints only pre = 180/150 and 20/50 trials after the gap.
- **All six cutting-claim notes:** "Recomputing waveform stability from the raw voltage of 25 sessions was not attempted." This is stale. Cells 73–81 compute exactly that, and later in the same notes the record reports it.
- **figs4l deviation:** "181, 103 and 84 of them … are also responsive over the full period." These are the uncorrected variant's numbers. Under the main BH-FDR reading they are 127, 82 and 39 (cell 45).
- **fig4c-map-units-after-cut, fig4jk-proximity-units-after-cut and figs5fg-cut-decoding notes, the metadata_insufficient finding, and cell 88:** "a fresh random permutation in every block of 10 passes". The output shows only that the 67 first blocks are distinct and that no second block repeats the first (cell 87). No block is shown to be a permutation.
- **Cell 8 and the fig2-wall-responsive-counts notes:** the deposit labels are "reproduced unit for unit … except for about 40 units". That count is right (41 deposit-unresponsive units). The crosstab also shows 12 other disagreements (2+2+1, 3+1, 1+1, 1) that go unmentioned (cell 7).
- **si-unit-yield notes and the isolation-metrics finding:** the low SNR of the 18 extra responsive units is "consistent with the deposit's labels applying an SNR criterion". This is overstated: by the same approximation, 75 of the 768 deposit-labelled responsive units also have SNR < 5 (cell 10). A sentence should say so.
- **Minor wording:** the SNR deviation still gives "as the processed files hold no waveforms" as the reason SNR is not applied. SNR is now computed; the reason it is not applied is that it is an approximation.

All other "**Result:**" sentences (cells 15–85), the Summary (cell 89), the README and the remaining notes match the outputs.

**My round-1 reasons in the record.** The record states them faithfully, close to my own words, with the relevant B and C points attached. The verifications entry correctly says that round 1 disagreed with three outcomes.

## 3. Round-1 points

**Resolved:**
- **B3:** SNR approximation and the duplicate rule added. The count is 1,034 / 1,030, within tolerance; the lower bound is 1,026.9.
- **B4 and B6:** both pass-set variants were run. Counts change by at most 3 units.
- **B7 and C3:** the model's four output lines are now labelled.
- **B10 and C4:** the cutting claims were tried on session-note and waveform-proxy subsets.
- **C2:** pass-epoch columns, DigitalInputEvents and the order of distances were checked.
- **C5:** other baselines were tried. None of them is a reading the criterion names.
- **C6:** SNR counts are reported.
- **B8, B9 and B11** need no action.

**Largely resolved:** B5 / C1, the orientation of rel_y. rel_y rises with probe_site (Spearman 1.000 / 0.996). That site 1 is the tip is still asserted, not printed.

**Remaining, bearing on a conclusion:**
1. **B2:** the claims file has the reader still to resolve this. fig2-distance-tuned-counts fails only on "both" = 92 against 29 ± 2.9. The paper's own Fig. 2F implies 94, so the outcome rests on a number the paper contradicts. The question is pending in questions/001687.yaml, which I did not see.
2. **B1:** the claims file's opening comment and criteria now consistently make BH-FDR the main reading. Its only `checks` entry (2026-10-21) still says the uncorrected test was made main, and no entry records the reader's 2026-11-03 change. Every judged outcome depends on that reading, so the log should record it.
3. **The fig4b-cut-wall-firing-reduced block** rests only on the undefined selection (see section 1).
4. **figs4j-ventral-location:** printing the description of the electrodes table's probe_site column would close C1.

**Claims-file misreadings to report, not correct.** Neither changes a conclusion.
- In fig4b-cut-wall-firing-reduced, the `expected` tolerance is 1.338, but the criterion says the larger spread (2.986) is used.
- In fig6-model-telc-loses-map, the criterion names the nine-bin classification. The paper's 590 and 636 equal the code's 99-point fine-grid counts exactly (cell 84). Both grids pass.
