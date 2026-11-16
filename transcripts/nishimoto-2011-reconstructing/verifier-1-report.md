**Verifier report, round 1: Nishimoto et al. 2011 on CRCNS vim-2**

The claims file has 10 claims. The notebook tests 4 and treats 6 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig2de-prediction-accuracy | reproduced | Cell 10, reading (a)(i) and (a)(ii): static 0.217, nondirectional 0.375, directional 0.379. All three are within tolerance, in the right order, and both Wilcoxon tests give p ≈ 0 (underflow). The margin is tiny: static 0.217 sits just above the 0.216 lower bound, and the fit is ridge, not the L1 regression the criterion names (problem 1). Reading (b) gives means of 0.12 to 0.21, all outside tolerance. |
| fig2e-directional-gain-small | reproduced | Cell 12: directional minus nondirectional is 0.0042, against a motion gain of 0.158. The ratio of 0.027 is below the claims file's bound of 0.1, and p ≈ 0. This holds under all four readings. |
| figs1a-motion-better-every-area | reproduced | Cell 14: both motion models beat the static model in 15 of 15 cells. V1 has the highest mean in every subject and every model. With V1 against the other four areas pooled (reading b), p ≤ 1e-11 in 3 of 3 subjects for every model. Against each area in turn (reading a), only the static model passes in all 3; the directional model passes in 1 of 3 (S3 V1 vs V3A, p = 0.03). |
| fig2fgh-retinotopic-receptive-fields | blocked (other: not run, though testable) | Cell 17 says "too_large (time)", but the whole run took 30.9 min and 11.7 GB (cell 18), and the probes are cheap. The archive holds everything the claims file's proxy test needs (problem 2). |
| fig2j-speed-eccentricity | blocked (other: not run, though testable) | Same as above. The grating probes need only the fitted weights and the filter bank. |
| fig3ab-identification-s1 | reproduced | Cell 16, model (a) with the repeat-averaged signal (i): 424 of 486 at the Tikhonov penalty 3.0, chosen on the held-out training data. That clears the threshold of 418. Chance is 2.96 of 486, matching the paper's "3 of 486". The margin is 6 volumes, and the fit is ridge (problem 1). Readings (b) and (ii) fall short: 344, 357.4 and 265.9. |
| fig3c-identification-large-set | blocked, data_missing | The archive listing has no candidate clip set: Stimuli, VoxelResponses ×3, anatomy.zip, docs, raw_data, checksums.md5 and filelist.txt only. The paper gives no location. Only a partial test is possible: the ~7,128 training seconds as distractors. That cannot meet the criterion at 1,000,000 clips. |
| fig4-reconstructions | blocked, data_missing | The archive has no sampled prior (listing as above). The training movies (7,200 s) are about 2,500 times smaller than the 18,000,000 s prior, so they are no defensible stand-in. |
| fig4d-reconstruction-accuracy | blocked, data_missing | Same as fig4. |
| discussion-color-no-gain | blocked (other: not run, though testable) | `Stimuli.tar.gz` holds RGB frames, and `vim2.load_stimuli` already supports the a and b channels. The cost is about 2 × 622 s of extra filtering plus one more fit per subject, which fits a run of this length. |

### B. Problems

1. **[affects a conclusion]** Cells 0, 7 and 16 and `vim2.kernel_ridge_path` / `ridge_fit_predict`: every model is fit by ridge, not by the L1-regularized least squares that the criterion and the paper (Model Fitting, refs 15–16) specify.
   - The notebook states this as a deviation "for time", which the 31 min total run does not really support.
   - Two passes sit near their thresholds: static 0.217 against a bound of 0.216 (fig2de), and 424 against 418 (fig3ab). Either could flip under the paper's estimator.
   - Reading (b) of the penalty choice (several CV splits), which the claims file says could change the outcome, was not run either.
2. **[affects a conclusion]** Cell 17: fig2fgh, fig2j and discussion-color are blocked as too_large, which the run's own time and memory figures don't support.
   - The ROI masks are split by hemisphere (lh/rh), which serves the contralateral test.
   - The voxel index in the 64×64×18 volume (plus anatomy.zip) gives the posterior–anterior axis.
   - The stimuli are RGB.
   - All three claims are testable from the data set.
3. **[does not affect a conclusion]** `vim2.model_columns`: the nondirectional model has 4,155 features. Pairing every nonzero-temporal-frequency filter would give 3,990 (1,425 + 5,130/2), so 330 filters are left unpaired, probably among the 570 zero-spatial-frequency, nonzero-temporal-frequency filters. The notebook never shows this.
   - Relatedly, pymoten puts 285 zero-spatial-frequency filters at each temporal frequency, where the paper says zero-spatial-frequency filters "occur only once (no orientation)". The total of 6,555 still matches.
   - Zero-spatial-frequency filters carry no direction, so the effect on the fig2e comparison should be negligible.
4. **[does not affect a conclusion]** Cell 14: the rank-sum tests are one-sided (`alternative="greater"`), which is neither stated nor in the claims file. Doubling the p-values changes no pass/fail under the readings that pass.
5. **[does not affect a conclusion]** Cell 7: the per-voxel ridge penalty hits both ends of the grid (10 and 1e7) for 100–560 voxels per model and subject. The top end is harmless, because correlation saturates as the penalty grows. Voxels at the bottom end may be under-regularized.
6. **[does not affect a conclusion]** Cell 7: the observed test signal is the mean of the ten repeats after each was z-scored, not the stored `rv`. The two differ only by per-repeat scaling, which is reasonable given the paper's per-run z-scoring.
7. **[does not affect a conclusion]** `vim2.load_stimuli`: the frame orientation (the `swapaxes` on the stored w/h axes) is asserted but never checked against an image. A transpose leaves the bank's statistics unchanged for the tested claims, but it would matter for the receptive-field claims.
8. **[does not affect a conclusion]** `vim2.holdout_blocks`: the 50 s blocks are laid out on the concatenated kept samples, so a few cross run boundaries. No test data enters any selection: feature z-scoring, ridge penalties, the 2,000-voxel set and the Tikhonov penalty are all chosen on training data.

On the helpers themselves: on synthetic inputs, `kernel_ridge_path`, `ridge_fit_predict` (predictions and residuals), `identify` (against brute-force Mahalanobis), `delayed`, `keep_mask`, `holdout_blocks` (750 held out), `corr_cols`, `_resample_matrix` and `rgb_to_lab` (red gives L 53.24, a 80.09, b 67.20) are all correct.

The claims file reads the paper faithfully on every point I checked: model definitions, the 486/7,128 sample counts, voxel selection, the Tikhonov inverse, and the Figure S1A legend.

### C. What I could not check

- **pymoten filter bank.** pymoten is not installed here, so I could not inspect the zero-spatial-frequency filters or the 165 extra nondirectional groups. *Output that would settle it:* a table of filter counts per (spatial frequency, temporal frequency, direction), plus the size distribution of the nondirectional groups.
- **Ridge versus L1.** I could not test whether ridge moves the borderline results. *Output that would settle it:* an L1/coordinate-descent fit (all voxels, or a random subsample of about 500 per subject) with the static and directional means beside the ridge values, and the S1 identification count under it.
- **Tikhonov grid.** The penalty grid has half-decade steps, so I could not check how sensitive the 424 count is to it. *Output that would settle it:* held-out and test counts on a finer grid around 3.0.
- **Blocked-for-time claims.** I could not say whether fig2fgh, fig2j and discussion-color reproduce. *Output that would settle it:* their computations, which the archive supports.
