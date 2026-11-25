**Round 2 verification: Shamugia et al. 2026, attempt mansvelder-2026-01**

## 1. Outcomes

The claims file has 47 claims: the 45 from round 1 plus two link claims the author added (`lee-label-link`, `mouse-specimen-link`). The attempt record gives all 47 an outcome: 8 reproduced, 11 partially reproduced, 9 not reproduced and 19 blocked (10 data_missing, 5 other, 4 methods_underspecified).

**Outcomes I agree with:**
- **Reproduced:** chartrand-label-link, lee-label-link, fig2d-pv-highest, figs2a, fig3jl, fig6b.
- **Partially reproduced:** mouse-specimen-link, fig5g, fig5jk.
- **Not reproduced:** sample-size, fig2ab, fig2g, fig3eg, fig3fh, fig5l, fig6c, figs4.
- **Blocked:** fig2d-sst-similar, fig5be, figs3 and fig4b (data_missing); fig7-model-ca and the three fig8 claims (methods_underspecified).

**Outcomes I agree with, with a caveat:**
- **fig2b (reproduced).** The criterion is met under both chirp readings (cell 28). The Q difference disappears when both species are limited to LAMP5 and VIP (p = 0.25, equal medians). So it rests on the human PV and SST cells, which have no mouse counterpart here.
- **fig2e-fres (partially reproduced).** The PV test cannot be run. The VIP "human higher" result has both medians at the 0.40 Hz floor.
- **fig2f, fig3c and fig3d (partially reproduced).** The criterion's partial rule ("two of the three lower subclasses" for fig2f, "three subclasses" for fig3c) cannot be met with only LAMP5 and VIP testable. "Partially reproduced" holds only if untestable parts count as missing rather than failed. The author applies that convention consistently.
- **fig2e-lamp5 (partially reproduced).** This absence claim holds under reading (b) only, with medians of 0.40 against 1.15 Hz (cell 49).
- **fig3ik (partially reproduced).** It is fragile: it fails under sag/Rin reading (b) and under chirp reading (a), and GEE gives sag p = 0.17 (cell 69).
- **figs1 (reproduced).** Weak: only 3 lobes have chirp cells (173/34/2), and Q against disease gives p = 0.052 (cell 101).
- **Depth claims (fig4c, fig4df, fig4g, figs2-l23, fig4i, fig4km), blocked data_missing.** Cell 106 confirms the 000630 depth is 0 and cell 6 confirms the mouse depth is empty. But "no depth column in the Lee table" is a fixed string in cell 6's print statement, not a check of the table.
- **fig6a and the four model claims, blocked other under the Time rule.** I accept this; their data remain public and untested.

**Outcome I disagree with:**
- **fig2d-subclass-proportion.** I would rate it not_reproduced under the main reading (b). The criterion has no partial rule. LAMP5 fails both its test (p = 0.003, needs < 0.001) and its tolerance, VIP fails tolerance, and PV is untestable (cell 37). It is only partially met under chirp reading (a).

**Assumptions (`assumed: true`):** fig2c, fig2e-fres, fig2e-lamp5, fig3ik, fig5i and figs1.
- Each assumption is stated, and each is reasonable:
  - Chirp reading (b) is supported by the 0.40 Hz medians, the mouse LAMP5 match and the Allen features (cell 20).
  - Counting Sncg as VIP is supported by the even coverage of the paper's counts.
  - Acute-only for figs1 is supported by the U-pairs argument (cell 101).
- One choice the record does not tie to these outcomes is the LOWESS fraction of 0.04. Cell 22 shows it moves the resonant fractions as much as the chirp reading does: human LAMP5 is 31.0% at 0.02 against 19.5% at 0.04. fig2c, fig2d-subclass and fig5i rest on it as much as on reading (b). The value comes from the claims file's O1, but these outcomes should say they depend on it.

## 2. Sentences the outputs do not support

- **README results table.** The row "Human against mouse… (12 claims): 4 reproduced, 6 partially, 2 not reproduced" disagrees with the record, which gives those 12 claims 3, 6 and 3. The README total is 9 reproduced and 8 not reproduced, against the record's 8 and 9.
- **Cell 107 (Summary):** "Four cells are deposited in both dandisets with identical traces." Cell 6 compares four measures, not traces.
- **Cell 107:** "None of the three dandisets carries subclass, donor name, layer or depth in its files." No output shows this.
- **Cells 15, and the mouse-specimen-link notes:** "(Pvalb-Cre and Sst-Cre cells with specimen ids above 1.2e9 are from later releases)." Cell 14 prints only id ranges, not Cre lines.
- **Record, fig3eg notes:** "All fits converged (conv_a, conv_b)." Cell 66 shows VIP `conv_b: False` under chirp (a) with sag/Rin (a).
- **Record, chartrand-label-link notes:** "of the 31 donors of chirp cells, 28 and 3" and "3 of the LAMP5/PAX6/Other cells have the t-type SST CHRNA4." Neither is printed (cell 8).
- **Record, finding 5:** "or their first second of chirp response." Cell 6 compares measures only.
- **Record, depth notes:** "the Lee, Dalley et al. table gives a layer but no distance" is a fixed string, not a check (cell 6). "Morphological features for 140 cells" is not printed.
- **Cells 29 and 107:** fig2b is labelled "under the assumed chirp reading (b)", but reading (a) gives the same outcome and the record does not mark it assumed. This is an inconsistency, not a wrong number.

Every other number in the Result cells, the Summary and the outcome notes matches the printed outputs.

The record's `verifications` block gives my round-1 reasons in my own words, nearly verbatim, for all 45 claims I reviewed. For fig3eg the reason also takes in problem 4.

## 3. Round-1 points

**Resolved:**
- 1: DANDI:000020 and 000636 are now used, through checked link claims.
- 4: reading (b) is now the main reading, with its reasons in cell 23.
- 5: Satterthwaite tests are implemented in the helper. I read the code and it is standard REML with Fai-Cornelius F df. It was checked against synthetic designs outside the notebook only.
- 6: convergence of every fit is printed, apart from the one non-converged fit in section 2.
- 7: reading (a) is kept as IPFX computes it, and reading (b) is shown.
- 9: my point was wrong. The column is filled but 0 for every cell (cell 106).
- Not-checked items: stimulus names, dropped-sweep table, histograms and Satterthwaite tests are now printed (cells 6, 20, 66).

**Partly resolved:**
- 2: fig6a and the model claims now give a stated reason (Time rule), but they remain untested.
- 3: the readings are now compared with Table S3 (cell 20). Neither gives the human LAMP5 median (0.40 or 0.20 against 1.09 Hz). fres is still censored at the floor (47 of 87 LAMP5 cells) inside linear models for fig3eg, fig2e and fig3fh. Cell 19 acknowledges this but does not handle it.
- 8: sensitivity to the LOWESS fraction is shown in cell 22, but not carried into the outcomes (section 1).
- 10: the misreadings are said to be asked in questions/mansvelder-2026.yaml, which I cannot see. The sample-size criterion still says the dandiset holds the Table S1 "Chartrand" donors; in fact 43 of its 53 donors are listed under "AcuteLDPublished" (cell 8).

**Still bearing on a conclusion:**
- The LOWESS fraction and floor censoring, for fig2c, fig2d-subclass, fig5i, fig2e and fig3eg.
- The fig2d-subclass rating.
- The fragility of fig3ik.
- The depth-blocked claims rest on an unshown check of the Lee table.
- Cultured analyses include 20 cells from donor H19.03.002, who is not in Table S1 (cells 11 and 101), so possibly not in the paper's sample.

## 4. Critical findings

No finding in the attempt record is rated `critical`.

Finding 8 (four cells deposited in both 000630 and 000636) is the nearest case, since it is one recording deposited as two. `minor` is right: both copies carry the same session id, and cell 6 shows the measures are identical. I would not raise any other finding to critical.

Two data oddities have no finding, and I would add both as `minor`:
- A mouse cell with Q = 16.8 (cell 75).
- A 000636 donor age of 0.0 years (cell 11).
