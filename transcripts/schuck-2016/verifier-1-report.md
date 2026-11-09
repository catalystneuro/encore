**A. Outcomes**

The claims file has 29 claims. The notebook tests 22 and blocks 7.

| Claim | Outcome | Reason |
|---|---|---|
| behavior-error-rate | blocked: metadata_insufficient | The 'err' events are multi-trial blocks (cell 9), so the error count cannot be read from the files. Counting one error per block gives 1.98% (reading b; 1.92% under a), below 2.3 ± 0.23. Counting every designed trial inside a block gives an upper bound of 3.10% (cell 14). The bounds bracket the paper's value. |
| supp-errors-by-trial-class | partially_reproduced | The class effect has p ≈ 1e-14, and Enter is the highest class in 24 of 24 participants. Enter is 4.79% against 3.4 ± 0.34. Exit and Internal stay below tolerance however the 44 unknown-class errors are split (Exit at most 1.18%, Internal at most 1.20%), and their order cannot be determined (cell 16). |
| supp-errors-stable-over-blocks | reproduced | LMM χ²(1) = 1.44, p = 0.23; logit p = 0.22 (cell 18). |
| supp-errors-not-by-age-category | reproduced | All three terms p > 0.4 under (a) and (b), and category alone p = 0.23 (cell 20). The age terms rest on 98 of 225 errors. |
| supp-training-errors-higher | blocked: data_missing | The zip listing has no training-session files. |
| supp-training-rt-unchanged | blocked: data_missing | Same reason. |
| supp-rt-stable-over-blocks | reproduced | χ²(1) = 1.74, p = 0.187; the paper reports 1.7, p = 0.18 (cell 22). Only the correct-trials reading could be run. |
| supp-rt-faces-faster | reproduced | Category p = 1.8e-14 with faces faster; age p = 0.72; interaction p = 0.61. Faces 945.8 ms and houses 1012.5 ms are both within tolerance (cell 23). See problem 9. |
| supp-rt-by-trial-class | reproduced | χ²(2) = 116.6, p ≈ 5e-26. Internal is 883 ms against Enter 1021 ms and Exit 1023 ms (cell 24). |
| fig2a-16way-decoding | partially_reproduced | 8.93% (voxel) and 8.92% (map) against 12.2 ± 1.22. Chance is 6.25%, as in the paper. Above chance with one-sided p = 0.002 and 0.0004 (t23) (cell 31). |
| fig2-two-back-state-space | partially_reproduced | No reading meets both conditions. Under voxel z-scoring the two-back accuracy is 5.96%, which is chance and outside tolerance, but lower than the hypothesized space at p = 0.001. Under map z-scoring it is 7.88%, within tolerance, but not lower (p = 0.13) (cell 33). |
| fig2b-hidden-components | partially_reproduced | Only previous category is above 50% (p = 0.048 voxel, 0.038 map). Previous age is at p = 0.77 and 0.16, current category at p = 0.42 and 0.10 (cell 35). |
| fig2b-current-age-absent | reproduced | One-sided p = 0.27 (voxel) and 0.95 (map) (cell 35). |
| fig2b-two-back-absent | reproduced | All t-tests p ≥ 0.055 (cell 37). The bootstrap variant reaches 0.042 and 0.0496 for two-back category under map z-scoring. |
| figs2c-8way-decoding | reproduced | Voxel reading: 15.89%, within 16.7 ± 1.67, with p = 0.006 against 12.5%. Previous category is 55.4% (p = 0.002) and current category 54.5% (p = 0.004). Previous age is 49.1% (p = 0.67), against main-text "above baseline" and supplement p = 0.09 (cell 39). |
| figs2a-permutation-control | partially_reproduced | Permuted 16-way accuracy is 5.98%, not above chance. Real 16-way exceeds permuted at p = 0.001 under reading (a). No component reaches p < 0.025: the best are prev_cat 0.031 and 0.033 and cur_cat 0.049 (cell 41). The reading (a) percentiles are near the expected values (7.09 against 7.04). Under reading (b) even the 16-way real mean is below the pooled 95th percentile. |
| synthetic-data-control | blocked: metadata_insufficient | No voxel coordinates, so neither the spherical peak nor the searchlight peak can be placed. Confirmed from the zip listing, which has no mask or coordinate file. Whether the .mat files hold one is not shown (see C). |
| fig2c-enter-cluster | reproduced | Raw maps with the diagonal out: p = 0.0097, 20 of 24 participants. Diagonal in: p = 0.002. Voxel z-scoring with the diagonal out is p = 0.052 (cell 45). |
| fig2d-enter-nonenter-decoding | not_reproduced | Under reading (a) only previous category reaches p < 0.05 (0.048 and 0.038), and reading (a) is identical to the fig2b numbers. Under reading (b) one of six tests passes (cell 47). The claim requires all three components. |
| fig3-searchlight-conjunction | blocked: data_missing | OFC voxels only, no whole-brain data (zip listing). |
| other-rois-incomplete | blocked: data_missing | No other ROIs. |
| fig4a-decoding-error-correlation | partially_reproduced | By the criterion's wording: r = −0.268 lies inside the paper's CI (−0.84 to −0.017) but outside the tolerance. However p = 0.21, and the notebook's bootstrap CI includes 0. Under map z-scoring r = −0.004 (cell 49). |
| fig4b-error-trial-drop | not_reproduced | Voxel: five preceding trials 8.0–9.0%, error trials 1.6–2.1%; both values are outside tolerance and the difference is not significant (p = 0.06–0.18). Map: the direction is reversed. Only 16 or 21 participants enter (cell 53). |
| fig4b-decline-before-errors | not_reproduced | Voxel slopes are negative but p ≥ 0.37. The only significant error slopes (map/nearest, p = 0.014 and 0.019) are positive, so accuracy rises toward the error (cell 55). |
| fig4b-error-vs-matched | reproduced | Voxel z-scoring with matched reading (a): trial 0 is 1.6% against 9.2%, one-sided p = 0.0003 (t20). It fails under matched reading (b) (p = 0.04–0.14) and reverses under map z-scoring (cell 57). See problem 3. |
| fig5-similarity-predicts-errors | not_reproduced | No correlation reading gives a negative regression at p < 0.05: type regressions have p = 0.08–0.37, and the significant ordinal slopes are positive. The 5C means are about 0 (p ≥ 0.46) (cell 59). |
| figs5-euclidean-distance | reproduced | Raw maps, span reading: ordinal slope positive, p = 0.0008; 5C mean r = 0.26, p = 0.003. Voxel maps also pass. Map z-scoring does not (cell 59). See problem 4. |
| fig5-synthetic-control | blocked: metadata_insufficient | Depends on synthetic-data-control. |
| supp-motor-action-not-in-ofc | blocked: data_missing | The data have no response side or per-trial response mapping, and no whole-brain data. |

**B. Problems**

1. [affects a conclusion] Cells 30 and 11, `analyse_subject`. Cell 30 states that post-error trials lie inside the 'err' regressor (reading O3b). Cell 11 shows the opposite: the 'err' column matches a short event at block onset (r 0.83–0.98), not the block. The repeated and post-error trials inside a block are therefore in no regressor, which is neither O3 reading. Reading (b) could have been built as a boxcar over each block's span from the err dur file. It was not run, and it could change the 16-way accuracy and everything that depends on it.
2. [affects a conclusion] Cells 12, 14 and 16, `error_trials`. Errors are counted as one per block, which the notebook itself shows is a lower bound: 353 designed trials sit inside 228 blocks. 181 of 228 blocks (79%) follow an Exit trial, which is far above the Enter share the paper's rates imply (about 48%). That points to Internal and Exit errors being undercounted or merged into blocks. Class rates, the overall rate and fig4a inherit this.
3. [affects a conclusion] Cells 51 and 57, `courses`. Every reconstructed error is an Enter error. Cell 27 shows Enter and Exit trials decode at about 6% at every lag, while all labelled trials together decode at about 9%. The matched comparison at position 0 is therefore confounded by trial class. Matched reading (b), drawn from the same run, is not significant, and there is no class-matched baseline.
4. [affects a conclusion] Cell 59, `transition_table`. A state's error rate and its number of correct trials are coupled: errors remove trials from the state regressor. Fewer trials mean noisier betas and larger Euclidean distances, which produces a positive distance–error relation by construction. The relation is significant only for raw and voxel-z-scored maps and vanishes for norm-equalized ('map') maps. Nothing controls for per-state trial counts.
5. [affects a conclusion] Cells 27 and 28. The 16-way accuracy stays above chance with the regressors shifted by −1, +2 and +6 TRs (t = 2.5, 4.0, 2.2), and single-volume decoding of Enter and Exit trials is at chance at every lag. The decoded signal may be largely slow or sustained, from runs of repeated Internal states. The notebook notes this and draws no consequence for the trial-wise claims.
6. [does not affect a conclusion] `subject_designs`, two-back reading (b). For Enter errors the block is the error and its repetition, so the trial two back "as presented" is the error trial itself. The code uses the trial before the block instead. This affects 39 trials.
7. [does not affect a conclusion] Cell 33. The two-back space uses rebuilt regressors but is compared against the data set's own columns ("16"), not against "16rebuilt" (9.57%). Using "16rebuilt" would be the cleaner pairing.
8. [does not affect a conclusion] The `ofc4.py` docstring follows the Figure 1B legend, where Internal errors repeat the preceding trial. The Methods and the data descriptor both say Internal errors repeat the same trial. The claims file does not note this conflict in the paper.
9. [does not affect a conclusion] Cell 23. A category χ² of 58.7 sits oddly with only 15 of 24 participants being faster for faces. The random-intercept-only model the criterion prescribes ignores by-participant category slopes and is likely anti-conservative. The notebook follows the criterion, so this is a fragility, not an error.
10. [does not affect a conclusion] Cell 0 / cell 4. Cell 0 says the files hold no voxel coordinates, but cell 4 (described as reading "every field of every run file") prints only selected keys, never the full key list. That statement underpins the O1 and synthetic-data blocks.

Helper checks I ran on synthetic inputs all passed: `trial_class`, `volume_index`, `zscore_maps`, the HRF peak at about 5 s, `regressor`, and `error_trials` on a constructed Exit → err → Exit sequence. I found no train/test leakage: z-scoring is within run, folds leave one run out, and trial-wise tests use the held-out run.

**C. What I could not check, and the output that would settle it**

- Whether the .mat files hold a mask or coordinates. Printing `sio.loadmat(...).keys()` for one run would settle the O1, synthetic-data-control and fig5-synthetic-control blocks.
- The O3(b) result for fig2a and its dependents. 16-way accuracy with 'err' modelled as a boxcar over each block's span would give it.
- Whether the error-trial drop survives class matching. Trial-0 accuracy against matched courses whose position 0 is an Enter trial (or Enter accuracy at volume 'after') would show it.
- Whether the Euclidean result is a trial-count artifact. The figs5 tests with per-state correct-trial counts as a covariate, or the correlation of distance with n_ok, would show it.
- How the 'err' blocks are composed: how many repetitions and post-error trials each holds, using the 'err' RT-file durations against the block spans. This would bound the true error count more tightly than the 1.98–3.10% range.
