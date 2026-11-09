**Verifier report, round 1: Churchland et al. 2010 (doi:10.1016/j.neuron.2010.09.015) on DANDI:000138 v0.220113.0407**

**A. Outcomes** (15 claims, from the claims file)

| Claim id | My outcome | Reason |
|---|---|---|
| fig4abc-tuning-correlation-single-electrode | blocked (data_missing) | The archive lists 2 assets, both from one subject (sub-Jenkins, array data). The single-electrode recordings of monkeys A, B and J are not there, so no part can be tested. |
| fig4d-tuning-correlation-j-array | partially_reproduced | Main reading (cell 23): mean r 0.195 and Spearman 0.212, both outside 0.13±0.013 and 0.11±0.011. Mean r is above zero at p = 0.023 (t-test). No reading puts both means within tolerance. Spearman is never within tolerance (0.146 to 0.212). |
| fig4e-correlation-time-course | not_reproduced | The mean correlation at movement onset is 0.13 to 0.22 under all 8 readings, above the 0.1 bound (cell 26). The other two conditions hold: the decline begins about −250 to −200 ms, and the curve only nears zero by about +200 ms. |
| results-ap-location-no-effect | reproduced (J-array only) | p = 0.43 to 0.84 under all 8 readings (cell 29), using array membership as AP location. A, B and J are data_missing. This is a claim of absence tested on 20 units, so power is low. |
| supp-preparatory-dimensionality | reproduced (assumption) | k90 = 11 with all units and 10 to 11 with included units (range reading), inside 6.3–11 (cell 31). The value sits at the upper edge: all units under `each` give 12. |
| fig6-peri-movement-space-best | reproduced (J-array only) | Main reading: peri-movement 0.351 at k = 10, against kitchen sink 0.250 and kinematic 0.103 (cell 36). The peri-movement space is best in 1468 of 2048 combinations. |
| fig6-each-dimensionality | reproduced (assumption) | Main reading wins 20 of 22 comparisons (0.909) and beats endpoints + max speed at k = 3 (0.126 vs 0.000). Only 1074 of 2048 combinations meet the criterion, mostly failing under fold=once with combine=each (cell 38). |
| fig6-dimensionality-trend | reproduced (assumption, depends on fold reading) | fold=once: best k = 10, then a fall to −0.456 at k = 14. fold=refit: performance rises steadily to 0.461 at k = 14, and only 6% of combinations meet the criterion (cell 40). See problem 1. |
| fig6-pd-adequate-all-spaces | reproduced | Peri-movement 0.351 and kinematic 0.103 are above zero, and 7 of 8 task spaces are above zero. Holds in 1936 of 2048 combinations (cell 42). |
| fig6e-summary-rank | blocked (data_missing) | Needs A, B and J single-electrode data plus EMG. The archive has neither. |
| fig7a-shuffled-space-poor | reproduced (assumption) | Main reading: shuffled best 0.014, below peri-movement at every k and below kinematic best 0.103 (cell 44). Fails under fold=refit (0.178 > 0.160) and under combine=each. |
| fig7b-window-start-onset | reproduced | Main-reading ratio 0.908, within 0.873–1.067. Median ratio over all combinations 0.917 (cell 46). Only reading (a) of the claims file, J-array against 0.97, is possible here. |
| fig7c-anterior-posterior | not_reproduced | Main reading: posterior/random 0.62 to 0.94 and anterior/random 0.67 to 0.97, outside the 10% bound (cell 48). Only 2 of 16 rows pass, both using fold=refit with the neuron's own rate in the upper-limit space (see problem 2). |
| fig7d-pd-consistency | reproduced | Peri-movement consistency is higher in every comparison, for all 8 variants and both axis scalings (cell 50). |
| fig8-oscillator-model | reproduced | 0.08 lies inside the central 95% of r (about −0.40 to 0.39) under all 4 readings; median r is about 0. PD leave-one-out performance is 1.0 (cell 52). |

**B. Problems**

1. [affects a conclusion] Cells 35 and 40, `loo_pca_space` fold reading: fig6-dimensionality-trend passes only under fold=once (91% of combinations vs 6% under refit). I checked both fold implementations against brute-force PCA and regression on synthetic data, and they are correct to 1e-14. On this dataset the fall at k ≥ 12 under once comes from leverage: k = 14 PCs from a 27-row matrix. The paper's J-array had 108 conditions. "Once" is the more natural reading of the Methods (leave out a condition, refit the PD), so I keep reproduced, but the result rests on that reading. Fig7a and fig6-each also flip under refit.
2. [does not affect a conclusion] Cell 48 `subset_scores`, `self_in_upper=True`: the Supplemental Procedures justify the upper limit with "whatever one neuron is tuned for, it ought to be shared with at least some of the other neurons". That implies leaving out the neuron being fit. Putting its own preparatory rate into the space it is regressed on is not a reading the paper allows. The only 2 rows that meet the fig7c criterion use it. With it excluded, fig7c fails under every variant.
3. [does not affect a conclusion] Cells 44 and 48: refit variants use 5 shuffle draws and 4 random-half draws, not the 20 the claims file sets.
4. [does not affect a conclusion] The data are probably not the paper's J-array session. The dandiset has 27 conditions and about 14 trials per condition after selection, while the paper's J-array had 108 conditions and about 2166 trials per neuron. The notebook says this (cell 0), but every tolerance is judged against a different dataset. It also bears on fig7d: drawing 25 of 27 conditions with replacement gives heavily overlapping draws.
5. [does not affect a conclusion] Cells 7, 28 and 47: every unit's electrode reference points to PMd, and the electrode coordinates are NaN. Mapping id prefix 1 to PMd is an assumption, supported only by stronger preparatory tuning in that prefix. The AP regression p-value and the fig7c criterion are symmetric in the labelling. Only the "anterior better" direction depends on it.
6. [does not affect a conclusion] Cell 26 uses only the movement-locked trace, not the spliced trace. All time points in the criterion (−400 to 0 ms) lie inside `MOVE_TRACE`, so the result is unaffected.
7. [does not affect a conclusion] Cell 31: k90 = 11 sits at the bound, and split-half k90 is 13 to 14, so trial noise inflates the count. supp-preparatory-dimensionality is fragile.
8. [does not affect a conclusion] Cell 23: fig4d's mean r depends on the 1.5× peri-movement criterion (0.106 to 0.202 for ratios 1.0 to 2.0, cell 24) and rests on 20 units.

Checked with no problem found: the helper functions (`loo_errors_fixed`, `loo_errors_refit_gram`, `_scores_from_gram`, `peri_errors` leaving out the fitted neuron, `smoothed_rate` normalisation) against brute force; the analysis windows, inclusion thresholds and task-space definitions against the Methods; units (mm, mm/s, spikes/s); the oscillator's mean-over-cycle map, which is ≈[[0, .009], [−.009, 0]], so r is the sampling correlation of the two initial coordinates, consistent with r = 0.08 from a single draw. The test file is not used, and none of the analyses train and test on different trial sets, so there is no leakage to check. Leave-one-condition-out is applied correctly.

**C. What I could not check**

- Whether this session is the paper's J-array session. Nothing in the files or the paper identifies it.
- Which id prefix is which array. NLB documentation of the unit-id scheme, or the archive's per-unit array labels, would settle it.
- Whether the fig7c differences are within noise. The spread (SD) of normalised performance across random-half draws is not printed, so the 10% bound cannot be judged against sampling noise.
- Whether fig6-each and fig6-trend fail under fold=refit for a real reason or a degenerate one. Printing the refit curves and the number of comparisons won under the main reading with refit would show this.
- Per-condition trial counts after selection for each reading. Only the min and max are printed (cell 15).

Cell 0 still contains the author's outcome table. I did not use it.
