**A. Outcomes**

The claims file holds 31 claims. The notebooks test 11 dandiset claims (10 in `reproduce_yemini_2021.ipynb`, plus fig7de in `optimal_coloring.ipynb`) and 5 claims from the Zenodo record (`wholebrain_zenodo.ipynb`). The other 15 are marked "Not tested on the dandiset" and are not attempted. I did not have the attempt record, so these counts come from the claims file and the notebooks.

| Claim | My outcome | Reason |
|---|---|---|
| fig2cd-variability-differs | partially_reproduced | Head only. For neurons named in at least 8 worms, the largest SD over the smallest is 36, 21 and 13 on the three axes; the atlas variants give 33 to 53 on axis 1 (cell 12). The criterion also needs the tail, which the archive does not hold. |
| fig2c-ollr-more-variable-than-olll | reproduced | SD ratio 2.14 and variance ratio 4.6 (cell 14). Every atlas variant has SD ratio ≥ 2.00 (lowest 2.002, initial worm 38_YAaDV) and variance ratio ≥ 4.0. One reading over 2 is enough under the criterion. |
| fig7bc-identification-accuracy | not_reproduced | Head accuracy is 39.0 to 51.8% with the Methods alignment and 55.0 to 63.2% with the CELL_ID alignment, against 77.4 to 94.6% (cell 20). The atlas variants give 38.7 to 67.0% (cell 21) and reading b gives 21 to 31%. Only the oracle, which is not a paper method, gets in (77.7%). Tail data missing. |
| fig7bc-ventral-ganglion-lowest | blocked (data_missing) | The deciding comparison needs the tail ganglia. The API lists 10 assets, all heads. |
| fig7b-eight-labels-above-90 | not_reproduced | After 8 annotations: 43.0% (Methods alignment) and 58.8% (CELL_ID alignment); no worm is above 90% (cell 23). |
| ms1-uncertain-first-faster | partially_reproduced | Head: the uncertain-first curve is above random at 50 of 50 counts, with means 52.2 vs 48.5 and 68.0 vs 62.4 (cell 24). The gain at 8 annotations is only about 1 point. Tail missing. |
| ms1-position-only-accuracy | not_reproduced | Head 20.4 to 27.1% against 45 to 55% (cell 22). Only the oracle (48.7%) is inside. Tail missing. |
| ms1-detection-accuracy | partially_reproduced | Head precision 83.4% and recall 82.5% are inside 81 to 99%. Accuracy is 71.0%, just under the 72% bound (cell 16). Tail missing. |
| ms1-calibration | blocked (methods_underspecified) | The two readings disagree: Spearman rho is 0.51 to 0.70 with p < 1e-13, but the mean absolute difference is 27.8 to 49.2 points. Confidence is 87 to 89% against accuracy of 38 to 62% (cell 26). Tail missing. |
| ms2-neuropal-color-violations | reproduced | Head-atlas adjacency gives 3.64%, inside 3.15 to 3.85; the variants give 3.62 to 3.66%. The data.mat adjacency for head and tail pooled gives 3.47% (cell 28). |
| fig7de-optimal-coloring-violations | partially_reproduced | 39-reporter case matched: best of 10,000 runs is 1.707%, and the best run with exactly 39 reporters is 1.828%. 3-reporter case not matched: best is 6.945%, against 9.45 to 11.55% (`optimal_coloring.ipynb` cells 6 and 8). |
| fig6d-ase-nacl-asymmetry (Zenodo) | reproduced | The left/right t test gives p 0.0005 to 0.002, and ASER rises (mean +0.42, p 0.003 to 0.007), under every duplicate-removal reading (`wholebrain_zenodo.ipynb` cell 8). |
| fig6ef-nacl-novel-interneurons (Zenodo) | reproduced | All six neurons have q ≤ 0.041 under every reading (cell 9). |
| fig6de-asj-ric-stimulus-specific (Zenodo) | blocked (methods_underspecified) | The claim holds with no removal and with one member removed. It fails with both members removed, the helper's main reading: ASJ to pentanedione has q 0.063 and RIC to NaCl has q 0.044 (cell 10). |
| tables6-tail-pvq-and-post-stimulus (Zenodo) | partially_reproduced | PVQ excitation to pentanedione has q ≤ 0.0008 under every reading. Post-stimulus responses to NaCl disappear with both members removed (cell 11). |
| figs1h-avf-cyclic-activity (Zenodo) | not_reproduced | Median peak rate is 0.07 to 0.20 Hz and the median spectral peak is 0.19 Hz. At most 3 of 31 traces fall in 0.27 to 0.33 Hz (cell 12). The peak rule is the notebook's assumption. |

**B. Problems**

1. [affects a conclusion] Identification failures cluster in the DV-named worms, and the notebook does not check whether the files share one orientation.
   - Methods alignment, per-worm accuracy (cell 20): the LR worms get 52.8 to 78.5%; the DV worms (38, 55, 56, 64, 76) get 5.3 to 12.0%.
   - CELL_ID alignment: 38, 56 and 64 get 13.7 to 23.3%.
   - In `code_alignment` the rotation search does nothing. The second `major_axis_align` re-runs PCA, so all 26 theta values give the same output up to axis signs; I tested this on synthetic points.
   - The port is faithful here: CELL_ID `AutoId.local_alignment` (line 280 at d9f5df9) does the same.
   - The low accuracies for fig7bc, ms1-position-only, fig7b and ms1-calibration may therefore reflect how the worms were mounted, not the method. For fig7bc the outcome probably still stands, since the oracle bound is 77.7% and the LR worms average about 69% under both alignments. For position-only the oracle (48.7%) is inside tolerance, so that outcome is less secure.
2. [affects a conclusion] fig7de (`optimal_coloring.ipynb` cell 7). Sparsities 1000, 2000 and 3000 also give 3-reporter solutions, but only 1500 got the full 7,500 runs. The other sparsities had 100 runs, and at 3000 the best 3-reporter value was 15.2%, not 9.9%. This open detail could change the outcome and was not run under every reading.
3. [affects a conclusion] `wholebrain.py` docstring and `wholebrain_zenodo.ipynb` cell 6. The docstring calls removing both members "a choice that removes few traces", but it removes 647 of 3,550 head traces and 161 of 797 tail traces. The outcomes of fig6de and tables6 turn on this reading.
4. [affects a conclusion] ms1-detection-accuracy (`detect`, `fit_gaussian`). fmincon is replaced by SLSQP. Accuracy misses the bound by 1 point, so this deviation could decide that quantity, and its effect is not measured.
5. [does not affect a conclusion] Claims-file misreading, fig7de. Methods S2 Figure 1 legend says panels D to K were chosen "among 7,500 simulations" spread across the 2 or 3 colors, 1 or 3 intensities and 3 or 10 reporters settings. That is not 7,500 runs per setting. Notebook cell 9 shows that the best of about 1,000 runs is still 7.8%, so the outcome does not change.
6. [does not affect a conclusion] Claims file, ms2 and fig7de. The code's shortfall measure is chosen because the Methods share (21.5% here) is "far above 3.5%". The reading is selected by its agreement with the target. Under the Methods share both claims fail (21.5%, and 13.7% for the 39-reporter solution).
7. [does not affect a conclusion] `fit_atlas`. The gauge fix is a stated, reasonable assumption, and its variants are shown. The `direction="forward"` reading (equation 4.11) is implemented but never run.
8. [does not affect a conclusion] fig7bc-ventral-ganglion-lowest. The head part (ventral ganglion's rank among head ganglia, and densities) could be reported from the head runs; the notebook does not.
9. [does not affect a conclusion] `RIDGE` of 0.01 µm² sets the SD floor to 0.1 µm for neurons named in only one worm (the cell 12 "all neurons" table). The ≥8-worm table, which decides the claim, avoids this.
10. [does not affect a conclusion] figs1h. Figure S1H uses five worms, while the notebook pools 31 traces from 18 worms. The median filter is 3 samples (0.75 s), not 0.5 s.
11. [does not affect a conclusion] Data check (cell 5). Only 2 of the 10 volumes are compared voxel by voxel with Zenodo; the other 8 are matched by identifier only. The archive metadata are wrong: strain OH16230, spinning disk, born 2021-01-05.

**C. What I could not check**

- Whether the LR and DV files are stored in different orientations. Per-worm principal-axis extents, and the rotation part of each oracle alignment against the atlas (cell 20), would settle it.
- Whether an orientation-corrected alignment changes fig7bc or position-only. Oracle and CELL_ID accuracies grouped by LR/DV, and under each atlas variant, would show this.
- Detection port fidelity. Optimizer convergence status per fit, or the detections on one worm compared with the CELL_ID GUI output, would show this.
- fig7de at sparsities 1000, 2000 and 3000. The best 3-reporter value from about 1,000 or more runs at each would show this.
- Head ganglion accuracies, with ganglion membership, for fig7bc-ventral-ganglion-lowest.
- The Sinkhorn shortcut's equivalence to CELL_ID `sinkhorn_logspace`. The helper asserts a 0.001 difference on one worm but no output shows it.
- Tail claims. I checked the archive through the API: version 0.241009.1514 has 10 assets, all heads, and the same assets in every version. No tail part of any claim can be tested on the dandiset.
