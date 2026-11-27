## Round 3 verifier report: mansvelder-2026-01

The attempt record has one proposed change of outcome, for fig2d-subclass-proportion. No other claim has a `proposed` entry.

| Claim id | Current outcome | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|---|
| fig2d-subclass-proportion | partially_reproduced | not_reproduced | yes | — | See below. |

### Why I agree

**The criterion.** The claims file passes this claim only when three conditions hold:
- Human LAMP5, VIP and PV resonant fractions are all within tolerance: 31.25 ± 3.125%, 25.0 ± 2.5% and 43.6 ± 4.36%.
- Each per-subclass goodness-of-fit chi-square gives p < 0.001.
- The human fraction is higher in each subclass.

There is no partial rule for this claim. Unlike other claims, the criterion does not define "partially reproduced", so a failed condition means not reproduced.

**The numbers derive from the data (cell 37).** A cell counts as resonant when fres > 1 Hz and Q > 1.05 (`resonance.py:284`), which is the fig2c definition. The test is `R.chi2_gof`, the reading the claims file names. I recomputed both chi-squares from the counts printed in cell 37 and they match:
- LAMP5: 17 of 87 human cells against a mouse fraction of 10/100 gives chi2 = 8.80.
- VIP: 6 of 49 human cells against a mouse fraction of 1/39 gives chi2 = 18.38.

**The criterion is not met under the main chirp reading (b), cell 37:**

| Subclass | Human fraction | Tolerance | Test |
|---|---|---|---|
| LAMP5 | 19.5% | fails | p = 0.003, fails the p < 0.001 bar |
| VIP | 12.2% | fails | p = 1.8e-5, passes |
| PV | 43.1% | passes | cannot be run: the mouse PV cells are not in DANDI:000020 |

**The outcome does not depend on the choices it rests on.** The choices that move the result fail the criterion either way:
- **Chirp reading (a), cell 37:** VIP is 16.3%, still below tolerance.
- **Sncg counted as LAMP5, cell 37:** the VIP test cannot be computed.
- **LOWESS fraction 0.02, cell 106:** VIP is 20.4%, below tolerance, and PV is 49.2%, above it.
- **LOWESS fraction 0.08, cell 106:** every fraction is far below tolerance.

So nothing was chosen to reach not_reproduced. Even without these checks, the untestable PV comparison alone rules out "reproduced".

**Records are consistent.** The result cell (cell 38) and the notes in the attempt record agree with these numbers.

I found no place in this claim's criterion that misreads the paper.
