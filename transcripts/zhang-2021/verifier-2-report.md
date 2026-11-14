**Verifier report, round 2: zhang-2021-01**

The claims file has 11 claims and the attempt record has 11 outcomes, one per claim.

**1. Outcomes**

| claim | record | agree | assumption (`assumed: true`) |
|---|---|---|---|
| fig1-csi-s2 | reproduced | yes. Cell 17 prints R3 0.739, 0.717 and 0.676, all within tolerance and above every null value under both readings. R2 also passes. | Stated and reasonable. It does not decide the outcome, since R2 passes too. |
| att-csi-group | reproduced | yes. Cell 21 prints R3 means of 0.663, 0.730 and 0.525, and group reading (b) passes. | Stated and reasonable. |
| supp-csi-per-subject | reproduced | yes. Cell 24: 10 of 12 values within tolerance, and 12 of 12 have p < 0.01 under null (a). | Stated and reasonable. |
| att-passive-lower | not_reproduced | yes. Cell 27 counts 2 of 5 at the bound under every R3 combination, and at most 3 at p < 0.05. | none |
| att-classification | reproduced | yes. Cell 30: 43.7, 53.3 and 46.6% are within tolerance, and all four readings are above every null mean. | none |
| att-weights-cortex | reproduced | yes under the criterion: cell 34 gives 4 of 5 subjects under threshold (ii) for B, B_L and Q_S, and 3 of 5 under (i). The margin is thin; see 3. | Stated: atlas regions, a ridge parameter chosen per subject, a t test of r. Reasonable as a stand-in. The t test treats 5400 autocorrelated TRs as independent, which is liberal: 57 to 71% of region voxels pass (cell 33). |
| game-csi | reproduced | yes. Under reading (b), cell 38 gives 0.702 and 0.581. | none (lag +1 also passes, cell 39) |
| game-mutual-negative-projection | reproduced | yes under the dataset column order (cell 42). | Stated, and the reasoning is sound. The Table 1 order would give partially_reproduced, and the record says so. |
| fig3b-state-relations | reproduced | yes (cell 45). | none |
| game-classification | partially_reproduced | yes. Cell 48: S1 is above tolerance under every reading, and every reading is significant. | none |
| game-weights-two-groups | not_reproduced | I agree only conditionally. The outcome rests on S7 alone (cell 53). | The atlas assumption is stated. One assumption that bears on the outcome is not stated: S7's BOLD goes into the analysis without z-scoring (see 3). |

**2. Text against the printed outputs**

This notebook's outputs come from a later execution than the one the conclusions and the record were written from. The R3 values and everything derived from them differ from the text:

- Cell 19 says "0.743 (attend-humans), 0.721 (attend-vehicles) and 0.675 (passive)". Cell 17 prints 0.739, 0.717 and 0.676. The record's measured values (0.743, 0.721, 0.675) and its response to round 1 ("This run gives 0.743, 0.721 and 0.675") are wrong in the same way.
- Cell 13 says "S2 attend-humans 0.740 in the first run, 0.743 in this one". Cell 15 prints 0.739.
- Cell 22 says "0.665 +/- 0.104 ..., 0.731 +/- 0.023 ... and 0.524 +/- 0.260" and "S3's CSI (0.061)". Cell 21 prints 0.663, 0.730 and 0.525, and cell 15 prints 0.062. The record's measured values (0.665, 0.731, 0.524) are wrong in the same way.
- Cell 25 says "S3 passive (0.061 ...)", "S5 attend-humans (0.767 ...)" and "Under reading (b) S3 passive has p = 0.045". Cell 24 prints 0.062, 0.763 and p_b = 0.039. Eleven of the twelve values in the record's measured list for supp-csi-per-subject differ from cell 24's R3 column (for example S1 attend-humans 0.515 against 0.512); only S6 attend-vehicles (0.700) matches.
- Cell 28 says "in 2 or 3 of the 5 subjects under every combination of reading and null run with the code's positions". Cell 27 prints 2 under every R3 combination, for both reading (a) and reading (b), so "or 3" has no support. The same applies to the Summary row in cell 55 ("2 or 3 of 5 subjects at the bound reached") and to the record's "2 or 3 under reading (b)".
- Further stale values in cell 28 and the record's notes for att-passive-lower:
  - "S1 0.515 against 0.620": printed 0.512 and 0.621.
  - "S6 0.605 against 0.651": printed 0.606 and 0.652.
  - "mean differences 0.668 and 0.135": printed 0.665 and 0.134.
  - "S2's mean difference, 0.057": printed 0.0525.
  - "99th percentile (0.042 to 0.055)": printed 0.0416 to 0.0562.
  - "maximum (0.052 to 0.084)": printed 0.0526 to 0.0840. S2's 0.0525 now sits just below the 0.0526 maximum (matched, null ii).
  - "p = 0.001 to 0.010": the printed p_mean ranges from 0.002 to 0.015.
  - "p 0.30 to 0.51": the printed R3 values range from 0.34 to 0.51.
- Cell 31 says "53.8% (contiguous, density)" and "Per subject the accuracy is 39.9 to 60.6%". Cell 30 prints 53.3 and a per-subject range of 40.4 to 60.6. The record's notes also give 53.8. The statement that the first run gave 53.4% "with the same code and seeds" now differs from this run by only 0.1.
- The README says the notebook "runs in about 55 minutes". The last printed elapsed time is 1430 s (cell 48), and the remaining cells are short, so nothing printed supports 55 minutes.
- Everything else I checked matches the printed numbers: cells 35, 40, 43, 46, 50 and 54, the rest of the Summary, the record's notes for att-weights-cortex, game-csi, game-mutual-negative-projection, fig3b-state-relations, game-classification and game-weights-two-groups, and the record's findings.
- The record states my round-1 reasons accurately, and mostly in my words. Several are verbatim (att-csi-group, supp-csi-per-subject, game-mutual-negative-projection). Problem 9, the permutation bound, is not attributed to a claim, but it does not affect a conclusion.

**3. Round-1 points**

Resolved:

- **Problem 1:** cell 7 prints the norm of the code's attention coefficients, about 1e-13.
- **Problem 2:** cell 26 states the mismatch, and cell 27 prints the null quantiles.
- **Problem 3:** both claims are now tested with atlas regions, and the superseded mappers are checked (cell 10).
- **Problem 4:** cell 11 shows the run structure, and the game-classification notes now draw on it.
- **Problem 5:** cells 39 and 49 add the lag +1 variants.
- **Problem 7:** the scoring is fixed.
- **Problem 8:** the centred test is added.
- **Problem 6:** stated, but folds with a gap at their edges were not run. That does not affect a conclusion.
- **Problem 9:** accepted as before.

All of the "Not checked" items have been addressed.

Remaining points that bear on a conclusion:

1. **Stale numbers.** The numbers listed in section 2 need to be updated from this notebook. This includes the measured values for three claims and the "2 or 3" count. The outcomes do not change.
2. **S7 game data are not normalized (new).** The paper says responses were "normalized to zero mean and unit variance". `load_game` uses S7's BOLD as stored (voxel SDs 0.094 to 1.009), with no z-scoring before the PCA, the OLS or the region means. The record reports this as a data finding but does not list it as a deviation. game-weights-two-groups is decided by S7 alone, so its not_reproduced outcome rests on this unstated choice. It also affects the S7 values in game-csi, game-mutual-negative-projection, fig3b-state-relations and game-classification.
3. **att-weights-cortex has a thin margin.** The 4 of 5 count holds only under threshold (ii). Under (i), the B and B_L readings fail in S3 by a near-tie in EBA (human 0.313, vehicle 0.314, cell 34). The values under (ii) are not printed, so the margin there cannot be judged. Threshold (ii) relies on a t test that assumes independent TRs. The conclusion should say the outcome hinges on this.
4. **game-weights-two-groups regions (minor).** The "prefrontal" region covers 57,895 vertices, which is most of the frontal lobe, so the S7 failure also depends on how coarsely the regions are drawn.
