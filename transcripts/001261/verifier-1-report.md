**Verifier report, round 1: Luo et al. 2024 (doi:10.1002/cne.70001) on DANDI:001261 v0.250917.2023**

The claims file has 29 claims. The notebook tests 18 and treats 11 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| sample-sizes | partially_reproduced | Cell 3 matches on files: 48 mouse C, 46 mouse NC, 46 macaque C, 27 mice, 9 macaques, and the sexes match Table 1. Cell 5 shows one of the 46 NC files is the same trace, sample for sample, as a C file (CG608_FL_S4C7). That leaves 45 distinct NC recordings, and the criterion's tolerance is 0. Slices are not recorded in the files. |
| fig2-mouse-c-nc-15-of-18 | not_reproduced | F1 can't be computed, so the range is 13 to 15 of 17. Cell 21 gives 11 or 12 under every reading (and with the last sweep of a repeat). Sag, AHP latency and, under reading a, adaptation also fail to differ. |
| fig2d-mouse-max-firing-rate | partially_reproduced | p = 1.1e-12 with NC higher. Both means fall just outside tolerance: C 6.33 against 6.57 to 8.03, NC 34.8 against 35.1 to 42.9 (cell 23). |
| fig2d-mouse-threshold-rheobase | partially_reproduced | Threshold holds: p = 6.4e-4, means -33.2 and -36.8 within tolerance. Rheobase has both means within tolerance (59.6, 42.0), but p = 2.3e-3 does not reach p < 0.001 (cell 25). Tie correction does not change this; I checked it at 2.1e-3. |
| fig2d-mouse-ahp | not_reproduced | AHP amplitude has p = 3.7e-12, but the NC mean is 16.35 against 12.4 ± 1.24. AHP width under the Methods window is reversed: C 158.9, NC 226.3, p = 0.02 (the window-only reading is also reversed, p = 2.6e-5). The tests do not hold, so this is not even partial. The code's window does reproduce it: 29.7 / 12.1 mV and 180.8 / 77.4 ms (cell 27). |
| fig2d-mouse-adaptation | reproduced | Under reading b (step with the most spikes): p = 0.011, C higher, means 0.884 and 0.606, both within tolerance. Reading a gives p = 0.68 (cell 29). |
| fig2d-mouse-passive | not_reproduced | F1 can't be computed (file names give it for only 8 of 48 C neurons, p = 0.35). Tau has p = 6.7e-5 in the right direction, but the means are far outside tolerance: C 60.95 against 34.6 ± 3.46, NC 28.6 against 22.3 ± 2.23 (cell 31). |
| figs2-2-mouse-amplitude-cv-sag | partially_reproduced | Amplitude: p = 1.6e-4, C larger. CV: p = 2.6e-3 under the most-spikes reading, C lower. Sag: p = 0.21, does not differ (cell 33). |
| fig2c-mouse-umap-separation | not_reproduced | The median count of misclassified neurons is 6 (drop) and 9.5 (impute), against at most 2, under both missing-value readings. It does beat every permutation (cell 35). |
| fig5a-mouse-lda-electrophysiology | reproduced | Accuracy is 1.00 (drop) and 0.936 (impute). That beats the 95th percentile of both shuffle types (about 0.75 to 0.78) and their maximum (at most 0.84), under both scalings (cell 37). |
| fig5b-mouse-lda-ahp-amplitude-top | reproduced | AHP amplitude ranks first under weight readings a and b and under both missing-value readings (cell 39). |
| fig7d-macaque-more-excitable | partially_reproduced | All three tests reach p < 1e-4 in the stated directions. Rheobase (22.5) and both f-I slopes (0.124 and 0.056) are within tolerance. Macaque maximum rate is 21.2 against 26.3 ± 2.63, outside tolerance (cell 41). |
| fig7d-macaque-threshold-ahp | partially_reproduced | Threshold (p = 3.5e-7, -39.6) and AHP amplitude (p = 5e-8, 20.5) hold. AHP width under the Methods window is 190.7 against 158.9, p = 0.27: wrong direction, not significant (cell 43). Two of three tests hold. |
| fig7-macaque-spike-width | not_reproduced | Means match (1.32 and 1.18), but p = 0.025 does not reach the criterion's p < 0.01 (cell 45). |
| figs7-1-macaque-amplitude-cv-sag-upstroke | partially_reproduced | Amplitude (p = 2.3e-3), CV (p = 3.2e-5 and 2.1e-6) and upstroke (p = 1.3e-5) hold, each larger in macaque. Sag gives p = 0.31. Downstroke differs (p = 0.015 under both F11 readings), which caps the claim at partial (cell 47). |
| fig7-macaque-mouse-feature-count | not_reproduced | 12 or 13 of 17 differ (cell 49). That is below the criterion's 14. The criterion does not lower the range when F1 is missing; if it were lowered as in the fig2 claim, 13 would sit on the edge. |
| fig7d-macaque-input-resistance | reproduced | Input resistance at -20 pA: macaque 584 against mouse 318 MΩ, p = 2.2e-5. Rheobase is lower in macaque, p = 8.6e-10 (cell 51). The code's slope variant gives p = 0.18, but it does not decide. |
| fig7c-macaque-mouse-umap-separation | blocked (methods_underspecified) | Reading b holds: every seed beats every permutation. Reading a fails: the median misclassified count is 9 and 10 (cell 53). The criterion assigns methods_underspecified to this case. |
| fig4d, figs4-1a, fig4c, fig5c, fig9-convex-hull, fig9-feature-count, fig9-branch-points, fig9c, fig10, fig10c, figs9-1a (11 claims) | blocked (data_missing) | I checked the archive: version 0.250917.2023 has 152 assets, all `.nwb`. The assets summary lists only CurrentClampSeries and CurrentClampStimulusSeries, and there are no related resources. A DANDI search (DOI, PMID, "NBM/SI", "BLA-projecting") finds only 001261. No part of these 11 claims can be tested. |

### B. Problems

1. [affects a conclusion, unverified] `nbmsi.load_file`: each sweep's onset is taken as `nz[0]`, the first non-zero stimulus sample. The -20 pA test pulse sits in the same sweep as the step. That is why the steps have 550 and 600 ms of non-zero samples (cell 7). Wherever the test pulse comes before the step, the 500 ms window is placed on the test pulse and the step is missed. I confirmed on a synthetic sweep that the amplitude (median) and the 550 ms duration still look normal in that case. This would explain the 8 "non-responsive" neurons in cells 9 and 10:
   - their steady state barely changes from the most negative to the largest step (-5 to 8 mV);
   - they fire no spikes;
   - the mouse C tau values are very large (CG250 401 ms, CG269 153 ms);
   - input resistance goes as low as -61 MΩ (cell 14).

   All 6 mouse neurons among them are cholinergic and come from one recording period, so the error is not random by group. They pull down the mouse C maximum rate (6.33, or 7.24 without them, which is within tolerance), inflate C tau, and leave 7 C neurons without spike features. They likely also change the fig2 and fig7 feature counts. The file-level onset `out["onset_s"]` (the largest step's first sample) is computed but never compared with the per-sweep onsets.
2. [affects a conclusion] Claims file, F12 to F14: the claims file makes the "Methods" AHP (rheobase step, 100 ms window) the deciding reading. Methods (12) only says "after the first action potential". The code's window reproduces the paper's numbers almost exactly: mouse 29.7 / 12.1 mV and 180.8 / 77.4 ms against 28.9 / 12.4 and 177.9 / 85.0; macaque 19.3 mV and 116 ms against 19.1 and 106.6. The Methods window reverses the AHP width direction. This is a likely misreading of what the paper computed. It decides fig2d-mouse-ahp and fig7d-macaque-threshold-ahp, and it affects the counts.
3. [affects a conclusion] `nbmsi._ahp_methods`: the main F14 searches for the half-level crossings to the end of the step. The claims file says "Window as in F12", which is closer to the `ahp_width_window` variant. The notebook states this as its own assumption, which is acceptable, and both readings give the same reversed direction. So this does not change an outcome, but the deciding reading is not the claims file's.
4. [affects a conclusion] Cell 14 drops the macaque file with the wrong scale (factor of 20) rather than rescaling it, and drops one NC copy of CG608. That gives 45 macaque C and 45 mouse NC against the paper's 46 and 46. The CG608 choice rests on "G+" in the file name, which is reasonable. Both are stated.
5. [does not affect a conclusion] `nbmsi.features`: F16 is capped at 200 pA, as Methods say. The code variant (macaque 23.8 ± 22.8) is closer to the paper's 26.3 ± 23.1 but still just outside tolerance.
6. [does not affect a conclusion] `ranksum_table` uses `scipy.stats.ranksums`, which has no tie correction, while MATLAB's ranksum has one. I checked rheobase: 2.34e-3 without the correction against 2.14e-3 with it.
7. [does not affect a conclusion] `lda_separation`: the 10-fold CV variant z-scores on all neurons before splitting, which leaks a little between training and test folds. It is a variant only.
8. [does not affect a conclusion] Sag: the claims file's rule for a saturated -60 pA step ("the next step up") is not implemented.
9. [does not affect a conclusion] Cell 21 `count()` counts a feature as differing without checking direction. AHP width is counted as differing at p = 0.02, but in the opposite direction to the paper.
10. [does not affect a conclusion] sample-sizes: the NC reading with ChAT-unknown neurons added is not addressed. The dataset has no such label, and the notebook does not say so.

### C. What I could not check

- Problem 1. I did not download the data. A per-sweep table of `onset_s` against the file onset (and against the stimulus's last non-zero run) for the 8 non-responsive neurons, plus a plot of one of their +200 pA sweeps showing both voltage and stimulus over the whole sweep, would settle it. If the onset is wrong, the feature table needs recomputing with the onset taken from the longest non-zero run.
- The tau fits. A plot or a fit-quality metric (R²) for the tau outliers above 150 ms would show whether these are failed fits or bad windows.
- `general/notes` and other per-file fields that might carry QC or slice information. The notebook prints `notes` into `info` but never displays it.
- UMAP parity with Meehan's run_umap. Only umap-learn with n_neighbors 15 and min_dist 0.3 was run, with no output showing that the outcome is insensitive to these parameters.
