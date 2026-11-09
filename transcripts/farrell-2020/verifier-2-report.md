**Verifier report, round 2: Farrell et al. 2020 (doi:10.1085/jgp.201912447) on CRCNS ear-1**

The claims file has 48 claims, and the attempt record gives an outcome for each: 23 reproduced, 7 partially reproduced, 11 not reproduced and 7 blocked. The README states the same counts. Four outcomes changed after round 1, all because of a new assumed reading, y-1. Under y-1, bins and groups whose mean dVmin is outside (0, 0.4] V are left out:
- fig3a-xe991-fit went from not reproduced to reproduced.
- fig4d-cleq-two-limits went from reproduced to not reproduced.
- table3-pathway-energies went from partial to reproduced.
- low-chloride-similar went from not reproduced to partial.

Three more changed to match my round-1 outcomes: xe991-voltage-clamp, capacitance-asymmetry and fig4a-vh-rises-vd-constant.

### 1. Outcomes and assumptions

I agree with all 48 stated outcomes. The ones with a caveat:

- **Every outcome that uses CLW, dVmin or C_Leq** still rests on the Corbitt et al. (2012) CSB rule. It is stated as an assumption and flagged `assumed: true`. It passes the claims file's Fig. S1 check (CLW 18.30 pF against 18.56 ± 1.856 pF). I still cannot check the rule's constants against the source.
- **y-1, the new reading:**
  - It is stated, flagged `assumed: true` wherever it applies, and run alongside y-0 (all bins) and y-2 (cells outside the range dropped before binning).
  - It is reasonable. It is what I asked for in round 1, and the Fig. S4 legend and the Discussion support it.
  - It is not in the claims file, though, and it now decides four outcomes.
  - The cell-level limit y-2 fails fig3a-eq3a-fit (Vd 0.0299 V against 0.034 ± 0.0034 V, cell 57). So choosing y-1 over y-2 matters for that claim too, and the record does not say so.
- **fig3a-xe991-fit (reproduced):** under y-1 with 5 pF bin edges all four values pass: 0.0505 V, 0.847, −0.377 and 0.921 (cell 57). Under y-0 every value fails. The outcome rests entirely on y-1.
- **fig4d-cleq-two-limits (not reproduced):** the lower limit misses by 0.0006 aF (0.6496 against 0.584 ± 0.065). This is a knife-edge in the other direction from round 1. Two of the three groups behind the upper limit are single cells, at 1.29 and 1.02 aF (cell 85).
- **mean-slope-half (not reproduced):** the outcome depends on which reading counts as "first".
  - The notebook takes edges at multiples of 5 pF (reading e-a) for all three fits, giving −0.407.
  - But fig3a-eq3a-fit is reproduced only with edges from the smallest CLW (reading e-b).
  - With e-b used throughout (weighted fits, the `first2` CLn rule, dC > 5 pF kept), the mean is −0.432, within −0.48 ± 0.048 (cell 79, row 8).
  - The literal criterion ("the slopes found in the claims it depends on") gives −0.402, so I accept not reproduced. The conclusion should still say that the reading under which Fig. 3a passes also passes this claim. The assumption is flagged.
- **two-hyperpolarized-states (partial):** I agree, as a judgement. The criterion defines partial as "slope and Vh conditions hold but C_Leq does not". Under y-1 all three now fail: the mean slope is −0.407, Vh rises 2.67-fold, and the lower C_Leq limit misses by 0.0006 aF. So no tier of the criterion fits. The record cites my round-1 judgement, but that was made when the C_Leq limits passed.
- **Assumptions:** they are stated and reasonable elsewhere. figs1-example-cell lists an "Assumed:" CLn rule but has no `assumed` flag. Its outcome does not depend on the rule, since both CLn readings pass (cell 8).

### 2. Sentences the printed outputs do not support

- **Cell 59, and the attempt record (fig3a-xe991-fit):** "With all 20 cells, edges e-b give 0.0476 V, 0.745, -0.355 and 0.788". Those values are under y-1, which leaves 18 of the 20 cells in the fitted bins (cell 57, "XE991 all 20", row 4).
- **Cell 86, and the attempt record (fig4d):** "The upper limit of 1.048 aF includes a group of one cell (1.29 aF)" and "3 groups, one of them a single cell". Two of the three groups are single cells, at 1.29 and 1.02 aF (cell 85).
- **Cell 105 (Summary):** "the Eq. 3a fit without XE991, the Eq. 6b R2 of Fig. 1 and the Fig. S4 fit come within tolerance". The XE991 Fig. S4 R2 fails (0.605 against 0.737 ± 0.074, cell 64), which is why figs4-fine-bins is partial.
- **Cell 105 (Summary):** "17 against 15 or 16 pigmented XE991 cells". Table 1 row (a) has 15 XE991 cells. The 16 is the pooled basal count (4 + 12), a different quantity.
- **README:** the partial row reads "Counts of Table 1". But table1-pigmented-no-xe991 is partial because p = 0.0010 is not < 0.0001 (cell 25), not because of its counts.
- **Cell 59:** "Under L-c with y-1, Vd is 0.0432 V, outside". That holds for edges at multiples of 5 pF only. With edges from the smallest CLW, Vd is 0.0538 V, and 0.0498 V for all XE991 cells, both within tolerance (cell 57). This comparison decides nothing.

Every other "**Result:**" sentence, the rest of the Summary, the README and the record's notes match the printed outputs.

**My round-1 reasons in the attempt record:** they are stated faithfully and in substance in my own words. Each B-point is attached to the claim it concerned, with the outcome I gave. The `agrees: false` entries match the three outcomes where my round-1 outcome differed from the attempt's at the time. One small paraphrase: the mean-slope-half reason ("inherits the XE991 bin and the Fig. 3b outlier") combines my points B1 and B2, and that is fair.

### 3. Round-1 points

**Resolved:**
- **B1 (one 2-cell XE991 bin):** y-1 is now applied to every fit and grouping, with y-0 and y-2 shown and the fits without the bin printed.
- **B2 (Fig. 3b):** the bins and every cell's dC are printed, and the second CLn reading (C at or below −0.15 V) is now run. The cause is one cell, file 18, with dC −5.0 pF and a negative CLWn. The claim still fails under every reading.
- **B3 (length gradient):** the end-to-end gradient is run, giving 0.95–1.43 µm/mV, also outside.
- **B4 (CLn rule), in part:** the transient check shows the first two ramp points are lower than the next six, not raised.
- **B6–B9:**
  - B6 (degrees of freedom in the uncentred R2): the explanation, n degrees of freedom for an uncentred total, is correct.
  - B7 (area wording): corrected.
  - B8 (imputed CSB): the root without the six imputed cells is 5.137 pF.
  - B9 (conductance units): the I-V units are printed, about 37 nS between neighbouring steps.

**B5** needed no change.

**What remains that bears on a conclusion:**
1. y-1 is an assumption outside the claims file, and it decides fig3a-xe991-fit, fig4d-cleq-two-limits, table3-pathway-energies and low-chloride-similar. The cell-level alternative y-2 would fail fig3a-eq3a-fit.
2. mean-slope-half passes (−0.432) under the reading that reproduces fig3a-eq3a-fit (e-b), and the conclusion does not say so.
3. fig4d-cleq-two-limits fails by 0.0006 aF, and its upper limit rests on two single-cell groups.
4. two-hyperpolarized-states is now outside every tier of its criterion.
5. B4: the CLn plateau fraction was chosen to give 62 cells, and the SD of dC is 2.42 pF against the paper's 1.32 pF. Both remain.
6. The Corbitt et al. (2012) CSB rule still cannot be checked against its source.
