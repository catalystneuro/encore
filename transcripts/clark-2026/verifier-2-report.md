**Verifier report, round 2: Clark, Abbott & Sompolinsky (2026) on DANDI:000939 (0.240528.1542)**

The claims file has 30 claims. The attempt record has 30 outcomes: 21 reproduced, 4 partially_reproduced, 1 not_reproduced, 1 blocked (fig8), and 3 reproduced resting on an assumption (figs11b, figs10, figs11-s12). Five notebooks are present now; in round 1 there were four. `model_sims.ipynb` is new.

### 1. Outcomes and assumptions

**Outcomes I agree with, unchanged since round 1.** I agree with all 26 outcomes I gave in round 1, except figs11b, which is discussed below. Checked against the claims file again, the outcomes for fig4, fig2gi, figs8-s9 and fig7de follow from the printed values.
- **No partial rule.** The criteria for fig4, figs8-s9 and figs1-s2 contain no "partially" rule. Read strictly, they give `not_reproduced`. I accept `partially_reproduced` as the fair description in each case, but it comes from the protocol's general reading, not from the criterion.

**Changed or new outcomes:**
- **figs11b, `reproduced`, `assumed: true`.** I agree.
  - The assumption is stated: the threshold comes from the fig2ef protocol run with the same 5-ms step. It is reasonable, and it is the reference on the same footing that I asked for in round 1.
  - Any threshold here sits at the noise floor. The real evidence is that final distances are about 1e-3 against median starting distances of 1.6 to 700 (cell 22).
- **figs10, `reproduced`, `assumed`.** I agree.
  - The continuum rule (at least 31 of 34 states) is stated and reasonable. It does not decide the outcome: both networks keep 34 states at noise 0, against 8 and 9 at 0.4 (cell 11).
- **figs11-s12, `reproduced`, `assumed`, `seed_sensitive`.** I agree.
  - The threshold assumption (the network's own fig2ef-protocol run) is stated and reasonable.
  - Part of the assumption is stated only in notebook cell 6, not in the record's deviations: it reads the criterion's "every final state" and "all … converge" as "at least 95%, as in figs11b". Under a strict "every", the claim seed fails at standard deviation 10: 0.97 within, with one state at 0.01146 against 0.01121 (cell 7).
- **figs1-s2, `partially_reproduced`, `seed_sensitive`.** I agree, with two reservations.
  - The criterion has no partial rule (see above).
  - The criterion's 5% test on two finite matrices measures sampling noise: the population eigenvalues are identical by construction (100, 100, 25, 25; cell 4). I report this as a weakness in the claims file's chosen threshold.
- **fig8, `blocked` (`too_large`).** I agree.

### 2. Statements the printed outputs do not support

- **theory cell 9 and the fig7de notes:** "reaches 20.5 tau at beta 1.1 and sigma 100". Cell 8 prints 19.513 at sigma 100. The maximum of 20.521 is at some other sigma.
  - The notes also say "the failures come from the grid's large sigma" and "Over sigma 1 to 10 the timescales stay within a few tau". The divergence time's "decreasing" test fails at small sigma (11 and 10 increases), and only sigma 1 and 100 are printed.
- **theory cell 6, fig7 notes and finding 4:** "mostly at small beta and large sigma" (finding 4: "mostly beta below 0.1 or sigma near 100"). Cell 5 lists only 8 of the 293 points.
- **network_grid cell 5 and figs8-s9 notes:** "1 to 4 of 100" diverge and "96 to 100 of 100" collapse "at every lambda". At lambda 1e-10 and 1e-6, n is 20 (4 and 16, 3 and 17; cell 4).
- **figs14 notes:** "Without setting one aside, two of the four pairs pass." The variant in network cell 19 prints within [0.027 0 0 0.0359] against next [0.1389 0.183 0.0002 0], which gives 3 of 4.
- **network cell 23:** "Every final state is on the manifold at the resolution of the reference (largest final distance 0.0015…)". Final maxima reach 0.00153 and 0.00154, above the 5-ms reference of 0.00141 (cell 22); only 97–100% are within it.
- **model_sims cell 12 and figs10 notes:** "The two fragment alike over the whole range."
  - At noise 0.4 the disordered network ends in fewer states under every seed: 4–8 against 9–12.
  - Under the claim seed it has fewer states at every level from 0.4 on, and about twice the median drift (cell 11).
  - The criterion is met, but "alike" overstates it.
- **Finding 3:** the two minima's errors "differ by less than the sampling noise of 500,000 samples". In float64 the ranges do not overlap: 0.00853–0.00894 for the chosen point against 0.00907–0.01006 for the paper's (tuning_curves cell 33). The ranking flips only with float32 under one seed and in the paper's cached grid.
- **Run times:**
  - The fig8 notes say the five notebooks take "77 minutes per run", and the README gives per-notebook times of 15, 22, 8, 2 and 31 minutes.
  - The printed totals are 1139, 2254, 611, 154 and 3042 s, which make 7,200 s (120 min).
- **tuning_curves cell 0:** later files have "sizes of about 24 GB". Cell 3 prints 12.7 to 30.2 GB.

Every other "**Result:**" sentence, Summary section, README row and note I checked matches the printed values.

**My round-1 reasons in the record:** the attempt record states them faithfully and in substance in my own words, for all 30 claims.

### 3. Round-1 points

| point | status |
|---|---|
| 1. fig4 | Resolved: all the outputs I asked for are printed, plus the paper's cached grid. `partial` stands on the tolerance. |
| 2. widths compared with `==` | Resolved. |
| 3. fig2gi | Resolved as far as the attempt can go: seeds, the angle-shift test and the wrap-mode variant are all added. **Remains, and bears on the outcome:** the criterion's 50 states cannot be reached; this is a claims-file defect, now sent to a reader. |
| 4. figs8-s9 | The paper's err_grid has been added and agrees. The grid still uses 20 initial conditions at most points (the 8 points the criterion reads use 100). **Remains, and bears on the outcome:** the claims file reads err(1e-8) < err(1e-12) more strictly than the supplement, and λ 1e-2 at c 1 does not collapse (radius 4.6 against 3.9). |
| 5. figs11b | Resolved by the 5-ms reference; the outcome now rests on a stated assumption. |
| 6. figs14 | Resolved: documented (but see the miscount in section 2). |
| 7. fig7 | Resolved: the bump amplitude is printed. **Remains:** the criterion tests only eigenvalue 2. The output contradicts the statement's "except the symmetry-induced zero" at 293 of 800 points, where the bump is not flat (median amplitude 0.95). That gap in the claims file bears on how much the `reproduced` covers. |
| 8. minor points | Resolved. |
| 9. untested claims | Resolved: three are tested and fig8 is blocked with a stated reason. |

**Other points that bear on a conclusion:**
- figs1-s2's 5% threshold sits at the level of sampling noise.
- figs11-s12 reads "every" as 95% without saying so in the record.
- Three outcomes are `partial` under criteria that have no partial rule.

### 4. Critical findings

None of the four findings in the attempt record is rated `critical`.
- **Findings 1 and 2** are rated `none`. They are supported by tuning_curves cells 3, 6, 8 and 10, and `none` is right.
- **Findings 3 and 4** concern the paper and carry no severity.
