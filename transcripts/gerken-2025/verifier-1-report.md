A. Outcomes by claim

The claims file holds 20 claims. 16 have a criterion, and 4 (the last four) do not.

| Claim | Outcome | Reason |
|---|---|---|
| dataset-composition | partially_reproduced | Cell 5 gives 29 patients, 2286 units, 17 female and 30 to 137 units per patient, all exact. A (559) and H (846) are within tolerance. EC 493 (allowed 396–484), PHC 293 (336–410) and PIC 68 (89–109) are outside it. |
| fig2b-phc-camera-cuts | blocked (methods_underspecified) | The test as specified flags 72.35% of PHC units (68.33% of all units) at random event times (cell 18, cell 20), so the 75.77% for camera cuts says nothing. The calibrated ZETA variant gives 12.63% / 22.18% against 51.74% (cell 21). With this test Summer comes out at 44% of units where the paper has 2%, so the paper must have used a different, unknown implementation. |
| tables1-camera-cuts-regions | blocked (methods_underspecified) | Same test. A 73.7%, EC 74.0% and H 64.4% (cell 23) are no higher than the 62–73% each region shows at random times (cell 18). |
| fig2b-phc-scene-cuts | blocked (methods_underspecified) | 47.44% at alpha 0.001 against 6.70%, from an uncalibrated test (cell 25). The ZETA variant gives 2.73% / 10.24%, outside 4.16–9.24% at both alphas. The cluster p (1.000, or 0.048 with per-trial z-scoring) rests on the same split. |
| tables1-few-semantic-responses | blocked (methods_underspecified) | Summer 1017 and Tom 1168 against 46 and 216 (cell 27). Camera cuts at 70.7% sit at the random-time level of 68.3%, so the contrast cannot be judged. |
| tables1-no-indoor-response | blocked (methods_underspecified) | 279 units at 0.001 (cell 29). This is literally not_reproduced, but a test that flags 68% of units at random times can neither support nor refute an absence claim. |
| results-cluster-regions | blocked (methods_underspecified) | Only 9/32 and 13/32 cells agree (cell 31), but the responsive/non-responsive split is uninformative. For camera cuts, 548 of the 669 "non-responsive" units are the ones barely spiking (cell 16). |
| fig3b-single-neuron-threshold | reproduced | Median unit kappa 0.0077 < 0.05. Best unit 0.276, and no unit ≥ 0.31 (cell 35). |
| fig3c-logreg-characters-location | reproduced | Summer 0.302 (in 0.225–0.335) and Indoor/Outdoor 0.360 (in 0.25–0.37). Tom 0.217 ≥ 0.17, McKenzie 0.317 ≥ 0.235, Persons 0.418 ≥ 0.312, so 5/5 (cell 37). Tom fold 4 is at chance (kappa 0.0, permutation p 0.52). |
| fig3c-logreg-cuts-lower | reproduced | Scene Cuts 0.0745 (in 0.068–0.132) and Camera Cuts 0.0967 (in 0.095–0.125) (cell 37). Camera Cuts is only 0.002 inside the bound, and Scene Cuts fold 4 is at chance (kappa −0.014, p = 1.0). |
| fig3e-temporal-gap | reproduced | With the logistic regression: random split 0.947 ≥ 0.9 and above the 32 s gap's 0.302. Intermediate gaps are 0.555, 0.524 and 0.450 (cell 40). |
| fig4-patients-below-pooled | reproduced | For all three labels, no patient reaches the pooled value. Best patients: 0.268 vs 0.302, 0.044 vs 0.075, 0.257 vs 0.360 (cell 42). |
| fig4-named-patients | reproduced | 7 of 8 named pairs are above 0.2; patient 15 has 0.197 for Summer (cell 44). This assumes subject ids equal the paper's patient numbers, which nothing confirms. |
| fig5-region-decoding | partially_reproduced | 3 of 4 orderings hold (cell 46). For Indoor/Outdoor the lowest is EC 0.117, not A 0.122; the gap is far smaller than the SEM (about 0.04). |
| fig6-responsive-subsets | blocked (methods_underspecified) | All four conditions hold mechanically (cell 48), but the subsets come from the uncalibrated test. The camera-cut "non-responsive" set is mostly units that barely spike, so condition (c) mainly measures removing every active unit. |
| fig7b-top500-overlap | partially_reproduced | 97 common units against 78 ± 7.8, outside tolerance (cell 50). Chance is 1.12–1.14, matching the paper's "about 1", and 97 is above 10× chance. |
| fig3c-lstm-decoding | blocked (methods_underspecified) | The archive (API, version 0.260702.0824) holds only the 29 `sub-*_ecephys.nwb` files, with no model code. The Methods leave the LSTM hyperparameters open. |
| fig3d-temporal-shuffle | blocked (methods_underspecified) | Needs a sequence model. The logistic regression on window sums cannot respond to the order of bins, so no part can be tested with it. |
| fig5-faces-presence | blocked (methods_underspecified) | LSTM claim. The `summer-presence`, `summer-faces` and `tom-faces` labels are in the files (0/1 only, cell 9), so a logistic regression stand-in for the orderings could have been tested, as was done for fig5-region-decoding. |
| fig7a-500-neurons | blocked (methods_underspecified) | The Results compare the full-population value with the LSTM's 0.31, which suggests an LSTM, but the Methods describe the 20-split logistic regression. The 20 sub-split fits and rankings already exist in cell 50, so a logistic regression stand-in on the top-k units was cheap to run. |

B. Problems

1. [affects a conclusion] `summer.wilcoxon_simes` (cells 16–31, 48). The code follows the paper's Methods text (saved under `paper/`), but the test is badly miscalibrated with many pseudo-trials. I checked this on synthetic data. Under stationary Poisson spiking, bin minus baseline/10 has mean zero but is skewed, so the signed-rank test rejects. With 2 Hz units and 883 events, 100% are flagged; with 113 events, 66%. A t-test on the same differences gives p = 0.76. Every responsive-unit claim and fig6 rest on this.
2. [affects a conclusion] Cell 18 calibrates only with 883 random events. The semantic labels have 39–151 onsets, and their real-unit null rate is never shown; synthetic 2 Hz units with 40 events give 20% at 0.001.
3. [affects a conclusion] Cell 48: for camera cuts, 548 of the 669 "non-responsive" units are the inactive units that get p = 1 (cell 16). Condition (c) is confounded with firing rate.
4. [affects a conclusion] Cell 51: fig7a and fig5-faces-presence are blocked as LSTM-only, although logistic regression stand-ins were feasible with data and fits already in the notebook (see A).
5. [does not affect a conclusion] Cell 21: the ZETA variant uses 100 resamplings (the dataset's code uses 1000) and covers PHC with camera and scene cuts only.
6. [does not affect a conclusion] `summer.onsets` always drops the first segment of a label (`np.r_[False, ...]`), even when it has the required second of absence before it. That costs at most one onset per label.
7. [does not affect a conclusion] `summer.window_sums` truncates windows at the edges of the analysis portion and ignores spikes just outside it, which affects 10 bins at each end.
8. [does not affect a conclusion] `fit_logreg`: C hits the top of the grid (0.03) in many folds. Results land within tolerance anyway. I confirmed L1 is active: `l1_ratio=1.0` with liblinear gives sparse coefficients under sklearn ≥ 1.8, and the notebook's nonzero counts confirm it. On sklearn < 1.8 the same call would silently fit L2.
9. [does not affect a conclusion] Cell 13: the per-patient clock check passes in only 12 of 29 patients. The pooled peri-stimulus histogram (PSTH) and the 300 s label-shift control (kappa 0.016) support the alignment.
10. [does not affect a conclusion] Everything else I checked is correct:
    - `split`: no leakage; at least 33.7 s between all sets with the 32 s gap, and gap + 1.6 s for the others.
    - z-scoring uses training statistics only.
    - `kappa` matches sklearn.
    - `ranking` ordering and `threshold_unit` behave correctly on synthetic inputs.

C. Not checked, and the output that would have allowed it

- Whether the paper's responsive counts come from the Wilcoxon test or from ZETA. Needed: ZETA for all regions and labels with 1000 resamplings, or the Wilcoxon p-value distribution at random times for each label's number of onsets.
- The mapping of subject ids to the paper's patient numbers (fig4-named-patients). Needed: units per patient printed next to the per-patient counts in the paper's Figure 4, if the figure gives them.
- fig7a and fig5-faces-presence with the logistic regression. Needed: kappa on the top-k units (k = 100 to 2286) with nested averaging over the 20 sub-splits, and kappas for Summer Faces, Tom Faces and Summer Presence, pooled and by region.
- Per-fold permutation p-values for fig4 and fig5. They were not printed, so per-patient above-chance cannot be judged.
