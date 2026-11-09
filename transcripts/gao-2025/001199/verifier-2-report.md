**Round 2 verification: 001199-gao-2025-01**

I counted from the claims file and the attempt record. There are 35 claims and 35 outcomes: 4 are not_reproduced (subjects, fig4-unit-counts, fig5-unit-counts, fig11b-ac-responses) and 31 are blocked, all as data_missing. No outcome carries `assumed: true`.

### 1. Outcomes

| Claim | Agree? | Comment |
|---|---|---|
| subjects | Yes | Cell 17 gives 6 and 6 rats under every reading, and 2 and 0 without the 2025 cohort. The "none extra" evidence now prints: 138 of 138 S1 files list an A1x64-Edge probe or H9; BH648 and BH658 are in both groups; none of the 10 rats is in 000946. |
| fig4-unit-counts | Yes | Cell 20: at most 4 of 8 counts can be within 10%, and a partial result needs 6. The bound is valid because keeping all 2025 files and the S1-6 sessions can only raise it. |
| fig5-unit-counts | **No longer** (I am revising my round-1 view) | The sham half fails only the 2 POm counts (37 units, cell 23). The other failures all come from CG1 sessions at 300 and 4,500 Hz. The paper's control, and the claims-file header, is CG1 at 3,000 Hz, and the dandiset has none. Counting other-PRF CG1 sessions does not bound units in sessions that are not deposited. The deviation's "can only raise the bounds" does not hold for that reason. fig7-9-unit-counts and fig5b treat an absent condition as data_missing. Treated the same way here, at most 2 of 8 counts are ruled out and a partial result (6 of 8) stays possible. So the outcome should be blocked (data_missing), or else carry `assumed: true` with the assumption stated: that the dandiset's CG1 sessions are the paper's control. |
| fig6-unit-counts | Yes (blocked) | Cell 26: at most 2 of 4 totals can be within 10%, which leaves a partial result open. I accept data_missing over my metadata_insufficient: the paper types units from waveforms, which are absent, and the label column is recorded as a metadata_error. |
| fig7-9-unit-counts and the 11 duty-cycle claims | Yes (blocked) | Cell 6: every stimulated file is PD 200, and the 26 files with no PD are the 26 sham files. |
| fig2-target-artifact, fig5b, and the 16 other type-dependent claims | Yes (blocked, data_missing) | Cell 4: 0 of 96 files hold a 1 or 2 in `celltype_label`. |
| fig11b-ac-responses | Yes, not_reproduced | 194 units against 453 ± 45.3. 3,000 Hz is never significant and nothing is significant after sonication (cells 28–29). The fallback reading of the assumptions does not apply, because the count and pattern fail under every variant. |

**Assumptions.** fig11b rests on two assumptions that are stated only as deviations, not as `assumed: true`: that the 2025 files were recorded at 5 V, and that the 2025 trial starts are sonication onsets. Both should be flagged. Both are reasonable:
- Nothing in the files states another voltage.
- Several printed outputs support the onset assumption more than the record admits (see item 2b).

### 2. Sentences not supported by the printed outputs

a. **Attempt record, format_error finding:** "Left unsorted they gave one AC unit a normalized rate of 4,224%". No output shows this. Cell 9 and the same finding also say "(one to seven places per unit)"; cell 8 prints only unit counts per rat.

b. **Cell 13, and the fig11b notes:** "untyped S1 units do not give a positive control that could separate the two explanations". The statement that T1 is not significant in 2025 is literally true. But in cell 12, T2 gives the following for 2025 S1 units:

| PRF | Window | p |
|---|---|---|
| 30 Hz | 0–67 ms | 7e-07 |
| 30 Hz | 201–268 ms | 1.6e-12 |
| 1,500 Hz | 0–67 ms | 2.7e-12 |
| 1,500 Hz | 201–268 ms | 8.1e-10 |

The sham AC units give T2 p = 0.57 (cell 29), so the test is not biased. A consistent rise right after the trial starts is locking to those starts. The notebook dismisses these results because the means are only 107–109%. Yet fig11b counts 1,500 Hz in AC as significant at a mean of 105.1% under the same T2 test. The inconsistency affects the stated "low confidence": it weakens the claim that the AC null "may come from the trial tables".

c. **Cell 30 and fig11b notes:** "with BH654 left out the R2 tests give 0.0095 and 0.006, with every R2 mean below 100%". The R2 means of that variant are not printed; cell 29 prints only KW_p, sig and lowest for it.

d. **Cell 13:** "Other files show the paper's delayed increase, from about 125 to 200 ms." The printed PSTHs (cell 11) show rises from about 200–300 ms: BH648 S1 reaches 118% at 225 ms and BH615 300 Hz reaches 110% at 300 ms. Nothing rises at 125 ms, and the BH594 files show no clear rise.

e. **Cell 15:** "as the 64-channel probes of BH594 give many units at 10 and 15 V". Per-rat counts are printed only for the 5 V set.

f. **Cell 9:** "one 2024 baseline has 400 and two 2025 sham files 149". The output gives the counts of files with each trial number, not which files they are.

g. **README:** the fig11b row says only "Not reproduced". It does not carry the low-confidence qualifier that the Summary (cell 31) and the record give.

Everything else checks against the outputs, including the Summary, the subjects, fig4 and fig5 results (cells 18, 21, 24), the counts, bounds, p-values, correlogram figures and per-rat ranges.

**My round-1 reasons in the record:** they are stated faithfully, nearly in my words, including the metadata_insufficient remark. One small misattribution: under subjects, the record appends my problem 7, which I had marked "does not affect a conclusion".

### 3. Round-1 points

**Resolved:**
- 1: fig4 and fig5 bounds, and the fig6 bound.
- 2: the main set is now 5 V, and the 2025 voltage assumption is stated in the sections and the Summary.
- 3: the "none extra" evidence is printed.
- 5: the R2 bias is accepted as not a misreading, and the outcome does not change.
- 6: PD parsing is checked in cell 6.
- 7: the more-than-2,000-spikes rule is applied, with a variant.
- 8: the variants are shown.
- All of my section C requests: per-file label counts, 2025 voltage, subject variants, trial-time span, correlogram and positive control.
- Blocked_by: I withdraw my metadata_insufficient. data_missing is reasonable.

**Partly resolved:**
- 4: the requested outputs now exist, but the notebook reads them selectively (item 2b).

**Remaining issues that bear on a conclusion:**
1. **fig5-unit-counts:** handling the absent CG1 sessions at 3,000 Hz as bounded by CG1 at other PRFs is inconsistent with fig7-9 and fig5b. On consistent treatment the outcome should be blocked, or the substitution should be marked `assumed: true`.
2. **fig11b:** the outcome should carry `assumed: true` for the 2025 trial starts being onsets and the 2025 voltage being 5 V. The conclusion about the positive control (cell 13 and the record's notes) should state the T2 results. Those results support locking in at least the 30 and 1,500 Hz sessions. The outcome itself does not change.
