**Round 2 verification report: Randi et al. 2023 on DANDI:001075 (attempt 001075-randi-2023-01)**

The claims file has 19 claims and the attempt record has 19 outcomes.

## 1. Stated outcomes

| Claim | Recorded | Do I agree? |
|---|---|---|
| recordings-protocol | partially_reproduced | Yes |
| pairs-measured | partially_reproduced | Yes |
| fig1e-avjr-avdr | reproduced | Yes |
| fig1f-aver-avar | reproduced | Yes. The evidence is weak (7 trials, p = 0.22) and the notes say so. |
| fig1g-saadl-ollr | reproduced | Yes. The evidence is weak and the notes say so. |
| edfig2ij-spatial-specificity | reproduced | Yes |
| sourcedata-link | partially_reproduced | Yes |
| osf-link | partially_reproduced | Yes. It is now judged on the 0.660 position-found agreement, as I asked. |
| fig2d-inhibitory-fraction | not_reproduced | Yes. All variants run 13.4 to 15.8% (cell 53). |
| fig2c-1310-connected, fig2c-bilateral, fig2efg-path-length | blocked: data_missing | Yes |
| fig3-anatomy-predictions | blocked: data_missing | Yes. The model predictions are not public, so data_missing is defensible. |
| edfig6-kernel-stereotypy | blocked: not_runnable | I accept it with a reservation. I cannot check the protocol's definition here. The failed install is described only in the notes; no cell shows it. The data are in the archive and no reimplementation was tried. |
| edfig7b-unc31-fewer | blocked: data_missing | Yes |
| fig4-rid-wt | partially_reproduced | Yes (cell 56). AWB meets the criterion. URX has 1 trial with no detected response. ADL never appears with a side label. |
| fig4-rid-unc31 | reproduced | Yes, as the criterion is worded, but it is met barely. Reading (a) rests on URX 0.031 in unc-31 against 0.032 from a single WT trial. All Mann-Whitney p values are 0.31 or higher. Against the WT export, ADL goes the other way. |
| fig5-extrasynaptic-screen | blocked: data_missing | Yes |
| fig6-spontaneous | blocked: not_runnable | I accept it, since it now depends on edfig6 in the claims file. |

## 2. Text the printed numbers do not support

**Cell 38 "Result":**
- "Every variant falls in the partial band." This is false for the detected-responses-only variant printed in cell 36: 0.360 / 0.471 / 0.458. That is below every partial threshold. The sentence holds for the filter and exported-assignment variants only.
- "With the code's correction of decaying traces the correlation of means is 0.617." Cell 36 prints 0.616. The attempt record's sourcedata-link notes repeat 0.617.
- "the correlations are 0.820 and 0.676" for the exported-assignment variant. Cell 33 prints 0.675. The attempt record's sourcedata-link notes also say 0.676.

**Attempt record, edfig2ij deviation:** "reading (a) matches, (b) and (c) do not." Cell 49 prints 0.817 for 10–16 µm, which is reading (c) and lies inside 0.675–0.825. Reading (c) also satisfies the criterion, which is what I said in round 1.

**Rows with F0 ≤ 0:** the attempt record findings ("3,173 of 433,216"), the sourcedata-link response ("3,173") and the Summary in cell 62 ("the 3,173 rows") all say 3,173. Cell 21 prints 3172.

**Attempt record, osf-link notes:** "the 3 unmatched exported recordings are the 3 subjects with only imaging files." Cell 32 prints the three exported session keys but never links them to subjects 20, 23 and 33, so the outputs do not show this.

**README:**
- "It takes about twelve minutes." Cell 63 prints a total run time of 919 s, about 15 min.
- The row "q-value results …, unc-31 comparisons, extrasynaptic screen | Blocked: data missing" conflicts with the fig4-rid-unc31 row, an unc-31 comparison listed as Reproduced. The blocked row presumably means edfig7b.

**Cell 12 (not a Result cell):** it says the shortened fit fails on 58 traces and the full fit on 53, with 10,160 responses detected. Cell 11 prints 59, 54 and 10161.

**Smaller inconsistency:** for subject 11, cell 32 prints 200 exported labels in one line and 201 exported ROIs in another. The record and Summary use 200.

All other sentences I checked match the outputs. That covers the Result cells 24, 27, 34, 41, 44, 47, 51, 54, 57 and 61, the Summary, the README and the attempt record's notes.

**My round-1 reasons in the attempt record:** all 19 restate my round-1 reasons faithfully and in substance. For fig1f, fig1g and fig3, my qualifiers ("weak", and the split category for fig3) are kept in the reason text.

## 3. Round-1 points

**Resolved:**
- **B1, sign of F0:** 3,172 rows are counted. With F0 > 0 only, fig2d stays at 15.1% and Pearson at 0.552.
- **B2, photobleaching:** variants without uncorrected traces were added, and 12 recordings were rerun with the full fit. Median Pearson is 0.997 and 99.5% of classifier calls agree (cell 11).
- **B3, osf-link inflated by manual targets:** the outcome now rests on 0.660, and there are variants without the nine poorly linked recordings.
- **B4, excluded stimulations:** sourcedata-link and fig2d now have variants without the 950 excluded stimulations (Pearson 0.601, fraction 15.2%), plus the exported-assignment variant.
- **B5, label mismatches:** shown to have three causes, and the finding is updated.
- **B7, text at odds with outputs:** corrected in cells 6 and 8 and in the docstring.
- **B8, z slope:** my reading was wrong. Only 3 recordings have a slope of exactly 0. Agreement correlates with the absolute slope (Spearman 0.478).
- **Section C, RID check:** done. AIAR and I5 are printed as the two head neurons never labelled.

**Partly resolved:**
- **B6, blocking categories:** fig4-rid-unc31 is now tested. The not_runnable category for edfig6 and fig6 stays, as noted in section 1.

**Remaining points that bear on a conclusion:**
- The cell 38 statement that every variant is in the partial band. It does not change the outcome.
- The edfig2ij deviation that says reading (c) does not match. It does not change the outcome, since reading (a) already meets the criterion.
- fig4-rid-unc31 is reproduced on differences no test detects. The reading (a) comparison uses one WT trial for URX.
- The edfig6 install failure is not shown in the notebook, so its blocking reason cannot be checked from the outputs. It bears on fig6 as well.
