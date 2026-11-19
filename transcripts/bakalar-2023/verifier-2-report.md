**Verifier report, round 2: Bakalar et al. (2023), DANDI:001362 version 0.260923.2152**

**1. Outcomes**

The claims file has 27 claims and the attempt record has 27 outcomes. All 27 are blocked: 24 for data_missing and 3 for methods_underspecified.

| Claim | Record | Agree? |
|---|---|---|
| fig5-dg-fos | blocked: methods_underspecified | Yes. On 22 hemispheres the 20 readings give 12 with both regions, 3 with one and 5 with neither (main notebook, cell 15). The higher thresholds and the other variants add more disagreement (cells 22 and 23; threshold notebook, cell 8). The dataset marks no threshold, so no reading can be picked over the others. This outcome is robust. |
| table4-lenient-regions | blocked (depends on fig5-dg-fos) | Yes, which changes my round-1 answer of partial. Its own test is partial in all 20 readings at 4000 to 12000 (cell 25), but not reproduced in 54 of 56 analyses at 14000 to 26000 (threshold notebook, cell 11). It is also not reproduced in 6 of 20 for the 18-hemisphere variant and 29 of 220 for the finer series (cell 27). The readings disagree, so fig5's blocking rule applies through "same readings", as well as through depends_on. |
| table4-region-values | blocked (depends on fig5-dg-fos) | Yes, which also changes my round-1 answer. No reading is reproduced. Most are partial, but a few are not reproduced: 2 of 112 at 26000 (LRN, ratio of medians; threshold notebook, cell 14), 6 of 440 in the finer series and 24 of 1920 subset analyses (cells 32 and 33). The readings disagree. Note that this claim's own criterion ("under one reading") does not itself say to block, so the block rests on depends_on and fig5's rule. |
| 24 data_missing claims | blocked: data_missing | Yes. Unchanged from round 1. |

**Assumptions.** No outcome in the record is marked `assumed: true`. The assumptions are given as deviations instead:
- 26-connectivity
- 9 to 900 voxels with majority-label assignment
- masked labels with a fallback to unmasked
- 438 regions
- linear-interpolation quartiles
- no artifact exclusion

Each is stated and reasonable, and each is shown as a variant or checked against the count tables (cell 9). None of the three blocked outcomes depends on them, because every variant also disagrees across readings.

**Claims file.** I again found no misreading of the paper.

**2. Text against printed outputs**

Almost every sentence checks out, including cells 23, 28 and 34, the threshold notebook's cells 9, 12 and 15, the Summary and the README. These do not:

- **Attempt record, fig5-dg-fos notes:** "Raw p is … 6.8e-06 to 3.7e-03 for DG-po". Cell 15, row 1 (4000, density, pooled) gives DG-po p = 3.093e-06, so the range should start at 3.1e-06.
- **Attempt record, fig5-dg-fos notes:** "Over the 20 readings the criterion names (thresholds 4000 to 12000…)". Reading (1) of the criterion names every threshold the derivatives hold. The 20 readings are the shared subset, not what the criterion names.
- **Attempt record, last metadata_insufficient finding:** "the masked labels hold 74% to 100% of the unmasked labelled voxels". Cell 21 prints 74.13% to 93.66% over all 16 hemispheres that have both.
- **Summary (cell 35) and README:** "the recount cell alone took 52 minutes", and cell 0 says "took 52 minutes in the last run". Cell 8 prints "recount took 50.5 min". The 66-minute total is consistent with the cell timestamps (04:16:54 to 05:22:05).
- **Summary (cell 35), fig5 row, and README:** "both significant in 12 of 20 at 4000 to 12000, in none at 14000 to 26000". The two counts are on different hemisphere sets (22 against 18), and the sentence doesn't say so. On the same 18 hemispheres, 4000 to 12000 already gives only 5 of 20 (cell 22). The drop is partly the loss of 4 hemispheres, not the threshold alone. The same applies to "So the claim's own test also depends on the threshold" (cell 28), since the 18-hemisphere variant at 4000 to 12000 is already not reproduced in 6 of 20.
- **Attempt record, fig5-dg-fos notes:** "The readings differ in outcome mainly through the outlier rule and the region size at thresholds of 8000 and above." This holds for the 20 main readings. It understates the threshold and hemisphere-set readings, which change the outcome more (cells 20 and 22, threshold notebook).

**My round-1 reasons in the record.** They are stated faithfully in my own words, including the problems behind the fig5-dg-fos outcome. The two disagreements (table4-lenient-regions, table4-region-values) are recorded as `agrees: false` with a response. "25 of 27 agree" matches.

**3. Round-1 points**

1. **Thresholds:** mostly resolved. 14000 to 26000 were run on the 18 hemispheres, and the 4 finer-series hemispheres were run at each threshold of their own series. 28000 to 40000 were not run. This does not bear on a conclusion: p rises with threshold, and the claims are blocked already.
2. **Artifact mask:** resolved as far as the data allow. The corrected heatmaps were compared (cell 5), a variant leaves out the two hemispheres (7, 6 and 7 readings), and the gap is recorded as a finding.
3. **Region set:** resolved. The 438 regions and the 59 extra exclusions are printed (cell 4). The 438 against 431 gap remains, with no effect on a conclusion.
4. **Masked against unmasked labels:** resolved (cells 21 and 22). DG cell counts are the same on both, DG densities are 0% to 17% lower on unmasked labels, and that variant gives 14, 3 and 3 readings.
5. **U comparability at 22 hemispheres:** resolved. It is stated in the notes and in cell 34.
6. **Slab edge:** resolved. The synthetic check was added (cell 6: 1228 short components plus 4 of 5 tall ones counted, 1 piece dropped), and the dropped number is now reported as an upper bound.
7. **Low power of the count-table variant:** resolved. It is stated in the notes.
8. **Claims file:** still no misreading found.

**Still open, bearing on a conclusion.** Nothing could change the three blocked outcomes. What remains are the text corrections in section 2: the DG-po p range, the 74% to 100% finding, and the confounding of threshold with hemisphere set in the Summary, the README and cell 28.
