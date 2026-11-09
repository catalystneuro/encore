**Verifier report, round 1: Farrell et al. 2020 (doi:10.1085/jgp.201912447) on CRCNS ear-1**

The claims file has 48 claims. The notebook tests 41 and treats 7 as blocked. Every outcome that uses CLW, dVmin or C_Leq rests on the notebook's reading L-b. Under L-b, the stereocilia capacitance CSB comes from the Corbitt et al. (2012) rule, which the notebook states as an assumption. That rule passes the Fig. S1 admissibility test: CLW 18.30 pF against 18.56 ± 1.856 pF.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| cohort | reproduced | All 8 group counts match. Totals 89, 42 albino and 47 pigmented. Also 3 cells at 10 mM chloride, 81 with Rs < 10 MOhm, recording times 47–182 min (cell 5). |
| figs1-example-cell | reproduced | All 6 recomputed values are within tolerance, and so are the stored ones (cell 7). |
| nlw-capacitance | reproduced | Root 5.104 pF is within 4.82 ± 0.482 (reading n-ii). Pigmented/albino and adult/juvenile 95% intervals overlap (cell 9). This holds only with the Corbitt CSB assumption: with CSB = 0 (n-c) the root is 5.44 pF and fails. |
| clw-by-turn | reproduced | Turn 1: 5.04 pF (SD 2.34). Turn 4: 17.79 pF (SD 2.74). Both means and both SDs within tolerance (cell 11). |
| fig1-charge-not-linear | reproduced | Fit through the origin, centred R2: 0.539, within 0.516 ± 0.052. CLW < 10 pF slope is 2.0× the other, with disjoint intervals (cell 13). Only 1 of 6 R2 readings passes. |
| fig1-two-state-bounds | not_reproduced | Reading b-a: 86% of cells in the band, below the 90% needed. Reading b-b: the CLW ≥ 10 pF median is 0.167 V against 0.129 ± 0.013 V (cell 55). |
| alpha-pigmented-vs-albino | reproduced | Means 9.00 and 7.81 V⁻¹, ANOVA p = 0.00008 (cell 15). |
| alpha-gradient-pigmented | reproduced | Region reading r-a: all four means within tolerance. Pigmented p = 0.00097; albino p = 0.586 (cell 17). |
| table1-pigmented-xe991 | partially_reproduced | Means and z within tolerance, p = 0.0027. But the counts are 5/12, not 4/11; reading r-b gives 1/10 and fails the means. |
| table1-pigmented-no-xe991 | partially_reproduced | Means within tolerance, but p = 0.0010, not < 0.0001 (cell 17). |
| table1-albino-no-gradient | reproduced | Counts 11/30, means within tolerance, p = 0.586. |
| table1-xe991-no-effect-alpha | partially_reproduced | XE991 effect p ≥ 0.47 under all three models, and the pooled means are within tolerance. But the counts are 17/27, and the criterion requires 16/27 (cell 19). |
| figs2-alphab-vs-clw | reproduced | Pigmented ρ = −0.85, p < 0.0001; albino p = 0.29 (cell 21). Rests on a test the paper does not name. |
| splice-isoform-x1 | blocked (data_missing) | Confirmed from the zip's file list (120 members): only MATLAB, HDF5, scripts and an ontology; no sequencing data. |
| v05-by-turn | reproduced | Reading v-a: all four means within the SD and within 10%. Turn 1 is more negative than turn 4 in both colonies (cell 23). |
| fig2b-v05-vs-clw | partially_reproduced | Both slopes positive with p < 0.01. Pigmented R2 0.613 passes; albino R2 0.175 falls outside 0.2 ± 0.02 (cell 25). |
| fig2b-no-phenotype-difference | not_reproduced | The interaction test (g-a) gives p = 0.0385, so the slopes do differ (cell 25). |
| v05-gradient-length | not_reproduced | The regression readings give 0.45–0.50 µm/mV (l-a) or 1.37–1.58 µm/mV (l-b); none within 0.63–0.77 (cell 27). See B3. |
| xe991-voltage-clamp | not_reproduced | Every XE991 cell's drop is under 13%. But the ratio of medians is 1.5, not ≥ 2. The largest conductance at V0.5 is 8.53 nS against 0.335 nS (cell 29). |
| table2-pigmented-xe991 | reproduced | Means −0.062 and −0.036 V, p = 0.021. |
| table2-pigmented-no-xe991 | reproduced | Means within tolerance, p = 0.0005 (< 0.001). |
| table2-albino | reproduced | Counts 11/30, means within tolerance, p = 0.0697, the same as the paper's. |
| table2-xe991-v05-shift | reproduced | Shift 0.024 V (reading h-a) or 0.0225 V (h-b), p = 0.0019. QTm, CLW and alphaB all have p ≥ 0.27 (cell 31). |
| v05-not-correlated-voltage-drop | reproduced | All four Pearson tests p ≥ 0.065 (cell 33). One Spearman variant gives p = 0.038. |
| fig3a-eq3a-fit | reproduced | Bin edges from the smallest CLW (e-b), weighted unconstrained fit (u-a): Vd 0.0311, R2 0.931, slope −0.4245, R2 0.948 — all four pass (cell 35). Under edges at multiples of 5 pF (e-a), the slope misses by 0.0001. |
| fig3a-xe991-fit | not_reproduced | Under L-b, no reading passes any value: Vd 0.077–0.085 V and R2 around −43 (cell 35). See B1: one 2-cell bin causes this. |
| fig3a-high-density-deviation | reproduced | On the 0.01 V bins all three conditions hold: t-test p = 0.042, F-test p = 0.021, and the mean residual below 0.25 V is smaller (cell 37). |
| figs4-fine-bins | partially_reproduced | Weighted (w-1): both Vd within tolerance (0.0299 and 0.0522 V). The XE991 R2 of 0.605 is outside 0.737 ± 0.074 (cell 39). |
| tables3-by-region | reproduced | In every group and region reading, the region with the higher dVmin has the more negative V0.5 (cell 41). Table S3's numbers are not available to compare. |
| fig3a-other-rodents | blocked (data_missing) | Needs rat and mouse V0.5 and QTm from other papers; not in the archive. |
| fig3c-engineered-mice | blocked (data_missing) | Rests only on values from other papers. |
| capacitance-asymmetry | not_reproduced | The two dC/CLW percentages fail: reading m-a gives apical 0.154 and basal 0.361; reading m-b gives basal 0.299 (cell 43). |
| figs5-specific-capacitance | reproduced | With the stored area: all five values within tolerance (cell 45). |
| fig3b-negative-clw-fit | not_reproduced | Every reading fails, with slopes of +0.03 (cell 47). See B2. |
| mean-slope-half | not_reproduced | Mean slope −0.15 to −0.22 against −0.48 ± 0.048 (cell 49). |
| fig4a-vh-rises-vd-constant | not_reproduced | Without XE991 (o-a), Vh is monotonic and Vd constant, but \|Vh\| max/min is 2.67, just under the 2.7 bound. Pooled bins (o-b) give 5.6 with 3 inversions (cell 51). |
| fig4d-cleq-two-limits | reproduced (fragile) | 5 pF CLW groups (j-a): 0.560 and 1.048 aF, Spearman p = 0.001 (cell 53). The lower limit passes only because of the 0.20 aF outlier bin; without it the limit is 0.6496, outside by 0.0006 (B1). |
| fig4c-sensor-area | not_reproduced | Area range 21–136 nm² under j-a, outside 45.9–133.1 nm². Under j-a the exponent (−1.60) matches −1.5 but the coefficient (64.8) does not match 38.5 (cell 57). |
| fig4e-sensor-charge | reproduced | Under j-b: z values 0.929, 0.814 and 0.885, Welch p = 0.12. |
| table3-pathway-energies | partially_reproduced | Under j-a both V0.5 values are within tolerance, but lambda for pathway 1 is 4.40 kB T against 3.97 ± 0.40. No grouping passes all six. The rebuilt equations do give Table 3's values from Table 3's inputs. |
| alternative-limit | not_reproduced | δ mean 0.65–0.69 against 0.535 ± 0.054, and the ranges fall outside (cell 57). |
| fig4f-all-rodents | blocked (data_missing) | Needs values from other papers. |
| low-chloride-similar | not_reproduced | C_Leq and z pass for all 3 cells, but no cell is within 0.02 V of the XE991 line, whose Vd is 0.0847 (cell 59). See B1. |
| molecular-model | blocked (data_missing) | The zip holds no structural model. |
| figs7-hearing-loss | blocked (data_missing) | Values from other papers only. |
| v05-temperature-corrected | blocked (data_missing) | The temperature coefficient is an outside input the paper does not give. The uncorrected basal V0.5 could be computed from the archive, but it decides nothing without that coefficient. |
| recording-time | reproduced | Means 124.7 and 112.0 min; none of the 10 correlations is significant (cell 61). |
| two-hyperpolarized-states | partially_reproduced | The Fig. 3a slope is near −½ (−0.42), Vd is constant, Vh is monotonic, and the two C_Leq limits pass. The mean slope and the threefold fail. The criterion defines no outcome for this mix; I judged it partial. |

Tally (my outcomes): 22 reproduced, 9 partially reproduced, 10 not reproduced, 7 blocked.

### B. Problems

1. **[affects a conclusion] One 2-cell XE991 bin decides several outcomes** (cells 35, 53, 59, `ear1.groups`). The 0–5 pF XE991 bin holds file 57 (CL 5.93 pF, CLW 0.475 pF, dVmin 1.33 V) and has a mean dVmin of 0.80 V.
   - I refitted the printed XE991 bin table (cell 35) with the notebook's own `fit_eq3a` and `ols`, leaving that bin out:

     | value | without the bin | paper |
     |---|---|---|
     | Vd | 0.0505 V | 0.0499 |
     | R2 of the Eq. 3a fit | 0.844 | 0.793 |
     | slope, weighted unconstrained fit | −0.376 | −0.37 |
     | R2 of that fit | 0.920 | 0.87 |

     All four are within tolerance, so the paper's Fig. 3a evidently did not include this bin. Its Fig. S4 fit also restricts dVmin to < 0.4 V.
   - The notebook keeps the bin for fig3a-xe991-fit (fails), mean-slope-half and low-chloride-similar. With the bin removed, low-chloride-similar would have 2 of 3 cells pass, a partial result.
   - It also keeps the bin for fig4d, where the bin is what makes the lower limit pass. Removing it gives 0.6496, which fails. The notebook flags this, but only for fig4d.
   - The notebook needed to run a "bins with dVmin ≤ 0.4 V" reading consistently across all of these claims.
2. **[affects a conclusion] fig3b rests on one CLn reading and its bins are not shown** (cell 47, `ear1.cln_readings`). Only the `first2` reading of CLn is used (mean C of the first two ramp points, right after the step from −0.06 to −0.18 V). The `below_m015` reading is never run for Fig. 3b. A positive slope and R2 down to −400 point to outlier bins, probably cells with negative dC, but the per-bin table is not printed. Mean-slope-half inherits this.
3. **[affects a conclusion] v05-gradient-length was run under regression readings only** (cell 27). The paper's comparison value, the mouse 1.6 µm/mV "across the cochlea", reads as an end-to-end gradient: the difference in mean length between turns 1 and 4 divided by the difference in mean V0.5. That reading was not run, and the claims file omits it; I report this as a gap in the claims file, not a correction. The paper also gives no citation for the 0.7 µm/mV, so it may not even come from this data set.
4. **[affects a conclusion] The CLn readings were chosen to match the paper's own numbers** (cells 43, 45; capacitance-asymmetry, figs5, fig3b). The plateau threshold was picked so the cell count is 62, and `first2` was picked because it reproduces the Fig. S1 legend's CLn. Both are stated as assumptions. Whether the first two ramp points carry settling transients was never checked. The SD of dC is 2.42 pF against the paper's 1.32.
5. **[does not affect a conclusion] Cell counts differ from Table 1** (cells 15, 17, 19). The data set has 17 pigmented XE991 cells at 144 mM chloride (Table 1: 15) and 27 without XE991 (paper: 28). This is shown openly. It turns the table1-xe991 claim and the no-effect claim into partial results, but it is not a code error.
6. **[does not affect a conclusion] Inconsistent degrees of freedom** in the uncentred R2 of `r2_origin` (cell 13): it divides the total sum of squares by n but the residual sum by n−1. That reading fails either way.
7. **[does not affect a conclusion] One cell-description statement is inaccurate** (cell 3). It says the stored area formula 2πr·l, with l the whole cell length, is "of the form" 2πr(L + r). It is not, unless l = L + r. The recomputed-area reading gives the same root (5.100 against 5.104 pF).
8. **[does not affect a conclusion] Six cells have an imputed CSB** (`ear1.csb`), the median of their turn. CSB only ranges from 0.35 to 1.05 pF, so the effect is small.
9. **[does not affect a conclusion] Conductance cannot be resolved.** Every conductance in the data set is in the nS range (the largest Rm, 375 MOhm, is about 2.7 nS), so the paper's 335 pS cannot be matched by any reading. xe991-voltage-clamp fails on the twofold criterion anyway.

The helpers check out on synthetic inputs:
- `ols` (weighted) matches statsmodels' WLS in slope, standard error, p-value and adjusted R2.
- `fit_eq3a` gives the correct closed-form Vd.
- `nlw_fit` recovers a planted root of 4.80.
- `bin_cells` handles negative values.
- The constants give kT/e0 = 0.02561 V, and alphaB 37.3 converts to z = 0.955.
- The unit conversion in `groups` is right (aF divided by 0.0095 pF/µm² gives nm²).

### C. What I could not check

- **The cause of the fig3b failure.** Printing the CLWn bin table (n, CLWn, dVmin, V0.5 per bin) and the per-cell dC distribution, including negative values, would have settled it.
- **Whether `first2` is a settling artefact.** A plot or table of C over the first 5 ramp points for a few cells would have shown this.
- **The XE991 fits without the 2-cell bin.** I recomputed these by hand from cell 35's printed table. The notebook should report them, along with fig4d, low-chloride and fig4c under the same exclusion.
- **The end-to-end length gradient.** Printing the mean lateral-wall length and cell length per turn and colony would have allowed it.
- **The units of the I-V steps** (the `IV_steps` values for one cell). Printing them would confirm the nS scale of the DC conductance.
- **The Corbitt et al. (2012) CSB rule** (0.07 µm² of bundle per µm², 140 µm² cap, 0.0075 pF/µm²) and the claim that the stored values follow the data set's analysis script. Neither source was available to me.
