**Verifier report: Churchland et al. 2010 on DANDI:000128 (round 1)**

**A. Outcomes**

The claims file has 22 claims. My outcomes: 11 reproduced, 1 partially reproduced, 3 not reproduced, 7 blocked.

| claim id | outcome | reason |
|---|---|---|
| recordings-jarray | partially_reproduced | Conditions are 108 (exact), and trials are 2295 under reading (a), within 2166 ± 216.6 (cell 12). The unit count is 182, outside 146 ± 14.6. The 137 "held-in" units that fall within tolerance are a Neural Latents Benchmark split, not a reading the claims file names, so the three counts do not all match under one reading. |
| recordings-single-electrode | blocked: data_missing | The archive holds one subject (Jenkins), two files and one array session; there are no single-electrode data for A, B or J. |
| fig2b-example-concordant-tuning | blocked: data_missing | Speed task (monkeys A and B) is not in the archive. |
| fig2ce-example-opposing-tuning | blocked: data_missing | Speed task is not in the archive. |
| fig3-maze-most-not-maintained | reproduced | Of 17 neurons, 1 has r ≥ 0.72 (0.765) and 94% have r < 0.72 (cell 17). This rests on a single neuron. |
| fig4d-mean-correlation-jarray | not_reproduced | Mean r = 0.051 and mean Spearman = 0.072, against 0.13 ± 0.013 and 0.11 ± 0.011. p = 0.42 to 0.61 under P1, P2 and P3 (cell 14, n = 17), so even the "partially reproduced" rule (positive mean with p < 0.05) fails. |
| fig4abc-mean-correlation-single-electrode | blocked: data_missing | No data from monkeys A, B or J (single electrode). |
| fig4-no-separate-populations | reproduced | Dip test p = 0.683 (U1 holds); 16 of 17 neurons have \|r\| < 0.5 (U2 holds); no neuron has \|r\| ≥ 0.8 (cell 19). |
| fig4e-correlation-time-course | reproduced | Under both A1 and A2, r falls from about 0.74 (−400 ms) to 0.61 (−200 ms) to 0.012 at onset. Smallest p at onset is 0.854, so (i) holds; 80 to 82% of the drop comes after −200 ms, so (ii) holds (cell 21). |
| suppfig1-population-averages | reproduced | Preparatory separation is positive (0.220 or 0.346). The ratio at onset is 0.240 (a) and 0.274 (b), so R1 holds under both readings and R2 under (a) (cell 24). |
| fig6-peri-movement-space-best | reproduced | Best peri-movement performance is 0.518 (K1) or 0.505 (K2). The best kinematic space reaches 0.424 and the best task space 0.412. The peri-movement space wins 24 of 24 combinations under each K (cell 31). J-array is the only dataset. |
| fig6-each-dimensionality | reproduced | Peri-movement wins 21 of 22 (K1) and 19 of 20 (K2) comparisons, so L1 and L2 both hold. Endpoints + max speed scores 0.168, below the 3-D peri-movement space at 0.271 (cell 33). |
| fig6-performance-vs-dimensionality | not_reproduced | Performance rises almost monotonically to the edge of the range: best k = 14 (0.518), with no decline after k = 10 (cell 35). |
| prep-dimensionality | not_reproduced | 15 components (N1) and 18 (N2) are needed for 90% of variance, outside 7 to 11 (cell 26). See problem 2 about how the claim was read. |
| fig6e-summary-across-datasets | blocked: data_missing | Needs A, B, J and EMG; the archive's assets summary lists Units and ProcessingModule only, with no EMG. |
| fig7a-shuffled-space-poor | reproduced | Shuffled space is below the unshuffled one at every k (best 0.227 vs 0.518) and below the worst kinematic variant (0.414 to 0.421), so H1 and H2 hold (cell 37). |
| fig7b-window-start-slide | reproduced | J-array ratio is 0.959 (K1) or 0.957 (K2), within 0.97 ± 0.097 under reading J2 (cell 39). The 0.94 value for monkeys A and B cannot be tested. |
| ap-location-no-effect-on-correlation | blocked: metadata_insufficient | I confirmed this in the archive: asset and version metadata have no anatomical coordinates. The notebook reports x, y, z as all NaN and every unit pointing to PMd electrode rows (cell 4). A two-level variant is possible only if the unit-id leading digit means the array; under that assumption p = 0.084 (cell 43), which would meet the criterion (p ≥ 0.05). |
| fig7c-anterior-posterior-performance | blocked: metadata_insufficient | Same missing location data. A split by the id digit is not testable either, because the criterion needs to know which half is anterior. |
| fig7d-pd-consistency | reproduced | Peri-movement consistency is higher in 11 of 11 comparisons (cell 41). J-array only. |
| fig8-model-weak-correlation | reproduced | 0.08 lies inside the central 95% (about −0.40 to 0.40) under all 8 readings (cell 45). The criterion is weak: almost any small value would pass. |
| fig8-model-pd-perfect | reproduced | Smallest R² and smallest leave-one-out performance are both 1.0 under all readings (cell 47). |

**B. Problems**

1. **[affects a conclusion] recordings-jarray, cell 12.** The table prints "within" for "units (held in only)" = 137 and for trials = 2295 (train file only). Neither is a reading in the claims file:
   - The held-in subset is a benchmark split.
   - Reading (a), "all successful trials", arguably includes the 574 test-file trials (2869 in total, outside tolerance).
   - The dataset's own unit count, 182, is outside tolerance under every reading.
2. **[affects a conclusion] prep-dimensionality: possible misreading in the claims file (reported, not corrected).** The main text says "at least 7-10 dimensions" (Results, PD performance, paragraph 2). The claim's statement and its 7 to 11 window treat 7 to 10 as a two-sided range. The notebook's 15 would agree with "at least". The supplement quote also says "This T-matrix", which may mean a conditions × (neurons × times) matrix rather than the c × n epoch means the claims file uses.
3. **[does not affect a conclusion] fig4d / M6, cell 10.** The selection leaves only 17 of 182 units, because tuning is measured as a range over 108 noisy condition means and the 1.5× peri/prep ratio applies on top. The code follows the claims file (S1 range, > 5 spikes/s, ≥ 1.5×, which matches the Methods wording). But n = 17 gives the dip test (fig4-no-separate) and the fig3 count little power, and fig3 rests on one neuron.
4. **[does not affect a conclusion] fig6-performance-vs-dimensionality, fig7b and fig7d (cells 35, 39, 41).** The best k sits at the upper limit of the tested range (14, or 12 under K2). The "best k" in fig7b and in the fig7d kinematic comparisons is therefore an edge value, not a true peak.
5. **[does not affect a conclusion] suppfig1, cell 24.** The preparatory separation is positive by construction, because conditions are ranked on the same preparatory rates. The claims file asks for this, so the outcome is unaffected.
6. **[does not affect a conclusion] fig6-each-dimensionality, cell 33.** The one lost comparison is not printed. It must be initial velocity (2-D: 0.238 vs peri-movement 0.223; my inference from cell 28). Peri-movement beats kinematic at k = 1 by only 0.002 to 0.004.
7. **[does not affect a conclusion] ap-location variant, cell 43.** It reports r = −0.43 on the id digit. The digit-to-array mapping is unverified, so the variant decides nothing, as the notebook says.
8. **[does not affect a conclusion] Helper functions (`mcmaze.py`).** I tested these on synthetic inputs and all are correct:
   - `loo_performance` matches brute-force leave-one-out.
   - `gram_leave_one_out_scores` matches direct PCA without the left-out neuron.
   - `condition_rates` has unit area, the correct peak height (19.95 spikes/s for one spike) and no time shift.
   - `proto_trial_keep` behaves as the claims file says: T1 drops trials with a flat component and T2 keeps them.
   - `task_features` gives a positive (counterclockwise) excursion for a leftward bulge.
   
   All numbers derive from the loaded data, and no method choice outside the claims file was found. Training/test leakage: the PCA spaces use all conditions, including the left-out one, but never the target neuron. This follows the paper's method and is not target leakage.
9. **[does not affect a conclusion] Chance levels.** The paper states none for any selection. The notebook's decoding sanity check (cell 8; chance 0.22, shuffled labels 0.15 to 0.18) is not tied to any claim.

**C. What I could not check**

- **Figures.** I did not view the plotted images. Printed ranges were given and I relied on them.
- **Per-neuron correlations.** I could not see the 17 r and Spearman values, or each neuron's array digit, with prep and peri tuning. Printing them in cell 14 would let fig3, fig4 and the AP variant be checked directly.
- **The lost comparison** in fig6-each-dimensionality: printing the failing items in cell 33 would confirm it.
- **Test-file trials.** Their delay and success status are unknown, so reading (a) of recordings-jarray cannot be settled. A count of how many session trials the NLB packaging dropped (if the NWB file records it) would help.
- **Supplement definition of the dimensionality T-matrix.** The supplement PDF could not be text-extracted here. A notebook variant computing 90% dimensionality on the conditions × (neurons × times) preparatory T-matrix would cover the other reading.
- **Array identity of the unit-id digit.** Nothing in the archive metadata identifies it. If the NWB electrode-group descriptions or any unit-level field mapped ids to arrays, printing it would make the two-level AP variant and a digit-based fig7c split testable.
