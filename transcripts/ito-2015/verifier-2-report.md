**Verifier report, round 2: Ito & Doya (2015) on DANDI:001642 (0.260205.0153)**

The claims file has 32 claims, and the attempt record gives an outcome for all 32: 11 reproduced, 9 not reproduced, 12 blocked.

### 1. Outcomes and assumptions

I agree with 31 of the 32 outcomes. Each one matches the printed outputs under the claims file's every-reading rule, with both unit sets counted as readings and the Panzeri-Treves correction kept as a variant that decides nothing.

**I still disagree on neuron-counts.** The record says not_reproduced; I would block it as data_missing. The record's reason, that every count that can be computed misses, does not hold up, because none of those counts limits the paper's counts:
- **The all-unit counts are only upper limits.** They are 297, 255 and 215, all above tolerance, and exclusions can only lower them.
- **The missing conditions can only remove more units.** Conditions 1, 2 and 5 cannot be applied, and DMS after the computable exclusions (204, against a limit of 195.8) could still drop into tolerance.
- **The VS count of 142 is not an upper limit either.** The paper removes a pair as duplicates only if the cross-correlogram test passes "and their PETHs had similar shapes" (Methods, paragraph after the five conditions). The notebook's check omits the PETH-similarity part, so its 90 removals may include units the paper kept.
- **What would settle it.** If VS after conditions (3) and (4i), with no duplicate removal, fell below 161.1, that would justify not_reproduced under reading 4i. That count is not printed. Under reading 4ii every count is far below the paper (47, 57, 21), so the condition-4 readings disagree too.

The author's other argument is about the protocol: blocking would cascade to the dependent claims (Author step 1.5). That is a consequence of the outcome, not evidence about it.

**Assumptions.**
- **fig2g-fq-variable-best** is the only outcome marked `assumed: true`. The assumption is stated: the model equations follow O8, and initial values, bounds, particle-filter priors and the drift-SD grid are in the deviations. It is reasonable, and the added seeds and the finer grid show the result is stable.
- **Two other outcomes also rest on the assumed FQ model** but are not marked. fig8f-state-value-vs (not reproduced) and no-policy-coding (reproduced) both use QL and QR from that model, which is fitted with the assumed priors. The deviations say so, but neither outcome has `assumed: true`, and the Summary table (cell 103) marks both "no". They should be marked as fig2g is.

### 2. Sentences the printed numbers do not support

- **Cell 102 (fig10d).** The text says "DLS shows no difference (p 0.18 and 0.94 at E3 and E4 with the last 20 trials, 0.18 and 0.76 with all)". With the last 20 trials the printed values are 0.937 at E3 and 0.868 at E4, so that pair should read 0.94 and 0.87. The pair for all trials is correct. The attempt record's range, 0.18 to 0.94, is correct.
- **Cell 43 (fig4c).** The text reads "The claim holds in 4 of the 12 readings (mean activity ratio, deposited PANs, 30 ms, no extinction trials: VS 0.216, DMS 0.130, DLS 0.117)". The reading in brackets is one that fails (DLS against DMS, p = 0.065). All four readings that hold are on the Methods-rule set.
- **Cell 68 and the attempt record's notes (fig6-event-coding-proportions).** "No state pair differs significantly (p 0.15 to 0.80)": the largest printed value is 0.8168, so the range is 0.15 to 0.82.
- **Cell 61 (fig5d).** At the DMS peak, DLS is "0.27 to 0.28", but the printed values go down to 0.265 (O1 b, with extinction trials), so the range is 0.26 to 0.28.
- **Cell 94 (fig10a).** "Fixed above free in both windows holds only under O1 (b)": it also holds under the Panzeri-Treves variant with the Wilcoxon test (four rows). This is minor because the variant decides nothing.

I checked every other "**Result:**" conclusion, the Summary section, the README and the attempt record's notes against the outputs, and they are supported. The Summary's count (11 / 9 / 12) agrees with the record.

**My round-1 reasons in the attempt record.** They are stated faithfully, mostly in my own words. Where the author merged in points from my section B (fig2g, actor-critic, fig4b-vs-phase7, fig5g, fig8a-d, no-policy-coding, fig9-dms-never-above-dls, fig10a), the merged text matches what I said. The remaining round-1 points are summarised correctly in `reviewed`.

### 3. Round-1 points

**Resolved:**
- **1:** the adopted reading is dropped, and every claim now gets its outcome from the every-reading rule.
- **2:** both unit sets are readings, and the regression now runs on the Methods-rule set too.
- **3:** the Panzeri-Treves correction is a variant only, and fig5e-action-info-cue-offset-dls is now not reproduced.
- **4:** fig5g part (1) is tested over the whole trial.
- **5:** a threshold variant with labels permuted within blocks was added. It leaves fig5e-action-info-rises-dls, fig9 and fig5g part (1) unchanged.
- **6:** further particle-filter seeds and a finer grid were run.
- **7:** fig10a uses first crossings.
- **8:** the conclusion now states how little the actor-critic test can show.
- **9 to 11:** the comment is fixed, and the bins that straddle events and the partial duplicate check are both stated.
- **All of section C:** the units-table printout, the regression on the Methods-rule set, the seeds, and the within-block threshold.

**Remaining, bearing on a conclusion:**
1. **neuron-counts:** blocked (data_missing) against not reproduced, as argued in part 1.
2. **fig5g-reward-info, a claims-file reading to report.** Part (1) requires each region's first threshold crossing over the whole trial to fall in Phase 6. The paper says reward information "started rising simultaneously in all subareas after the start of L/R poking". The claims file reads "started rising" as the sustained rise for fig9, but not here. The crossings before the reward are small: VS averages 0.013 bits/s over Phases 1–5 against 0.083 in Phase 6. The outcome turns on this reading. Part (2) holds in only 4 of 24 rows, so if part (1) held, the claim would be blocked rather than not reproduced. I raised this point myself in round 1 and accept the outcome under the claims file as worded.
3. **fig4b-vs-phase7 and fig9-dms-never-above-dls** are blocked only by the claims-file readings I reported in round 1:
   - the first-crossing reading of Fig. 4B;
   - for fig9-dms, a single uncorrected p < 0.05 among eight tests.

   Both are with a reader (questions/001642.yaml), so they are pending, not the author's to fix.
4. **fig8f-state-value-vs and no-policy-coding** should carry `assumed: true`, as in part 1.
5. **fig10c-vs-no-fixed-free-difference, a minor claims-file point.** The claim's statement includes a transient VS peak only in single fixed-choice blocks, but the criterion only reports that peak and does not test it. The data do not show such a peak: per block, the VS average passes its threshold in Phase 3 in 12 to 17 windows for double fixed-choice blocks and in 0 to 1 for single fixed-choice blocks (cell 97).
