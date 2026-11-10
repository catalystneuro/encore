## Verifier report: Okuno et al. 2025 on DANDI:000727, round 1

The claims file has 30 claims. The notebook tests 11 against the dandiset (8 have outcome cells, 3 more give a verdict only in the status table) and 5 against the paper's own deposited tables. It marks 14 blocked.

The main result: the analysis leaves out the motion and slice-timing correction that the paper and the claims file require (M1), and never says so. Its FC-SC correlations come out well below both the paper's values and the paper's own deposited result for the same SC matrix, and the transmitter claim fails because of this.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| fig1-poltcomp-optimal | blocked (data_missing) | Neither the code repository at 4b92add nor Zenodo 15532272 holds the SCKm/DistKm atlases (checked). The repository has `hemiFlyem52atlasCal`, but that covers only one of the three ROI types the criterion needs. |
| fig2b-distkm-smoothing-optimum | blocked (data_missing) | Atlas missing. Zenodo has the SC lists (`hemidistkm*_connectlist`) and the paper's own AUC outputs, but no atlases. |
| figs2-1b-sckm-smoothing | blocked (data_missing) | Same as above. |
| fig2c-smoothing-plus-poltcomp | blocked (data_missing) | Same as above. |
| figs2-1d-highpass-degrades | blocked (data_missing) | Same as above. |
| fig2d-log-decline | blocked (data_missing) | Same as above. |
| fig2d-fly-values | blocked (data_missing) | Same as above. |
| fig2d-ten-thousand-rois | blocked (data_missing) | Same as above. |
| discussion-twenty-rois | blocked (data_missing) | Same as above. |
| fig3d-confidence-threshold | blocked (data_missing) | Only the FlyEM cf0.8 SC is deposited (repository `results/sc/hemiroi_connectlist.mat`). `hemiroi_postsyncount` holds counts per ROI, not connectivity. |
| fig3d-flyem-vs-flywire | partially_reproduced | Cell 18: FlyEM r = 0.5999 against a tolerance of 0.657–0.803, FlyWire 0.5640 against 0.612–0.748. FlyEM is higher. Both values are outside tolerance under every variant. The paper's own deposited R(7) is 0.6835 for the same FlyWire SC, so the shortfall is in this attempt's FC. |
| fig3e-flyem-higher-most-regions | reproduced | Cell 21: 54 of 63, inside 52.2–63.8. The margin is small: with left and right swapped the count is 44. The per-region values correlate only r = 0.653 with the paper's deposited values. |
| fig3g-transmitter-correlation | not_reproduced | Cell 23: ACh r = −0.044 (p = 0.73), GABA r = −0.076 (p = 0.55). The paper's deposited per-region values, run through the notebook's own share table, give 0.395 (p = 0.00136) and −0.252 (p = 0.0465). So the inputs are right and the attempt's FC is what fails. |
| fig3a-postsynapse-counts | partially_reproduced | Cell 35: FlyWire sc50 gives 18.83 M (expected 18.8) and sc140 gives 11.24 M (expected 11.4 ± 1.14). The FlyEM confidence-0 count (21.4 M) is not in the deposit, whose thresholds run 50–90, so it is untested. |
| fig3c-regional-detection | reproduced | Cell 36: FlyEM is higher in EB, FB, NO, PB, in aL/bL and in every mushroom-body ROI. FlyWire is higher in LO, ME, CAN, FLA. This is a check on the paper's deposited counts. |
| figs3-1a-regional-count-similarity | reproduced | Cell 37: 0.7778, 0.9001 and 0.9187, all within tolerance (from the deposited table). |
| fig3f-output-transmitters | reproduced | Cell 38: ACh 62.8 %, GLUT 15.5 %, GABA 11.4 %, exact (from the deposited table). |
| figs3-2cd-apl-similarity | blocked (data_missing) | FlyWire synapse locations are deposited, but no FlyEM synapse data is. |
| fig4b-ppssi-distribution | partially_reproduced | Mean PPSSI is 0.471, inside 0.4–0.6. The table covers 139,255 neurons, but only 138,144 have a value, against an expected 139,255 with tolerance 0. See problem 6. |
| fig4a-unsegregated-ranking | blocked (data_missing for FlyEM) | The FlyWire half looks testable and was not tried (problem 5). |
| fig4c-segregated-ranking | blocked (data_missing for FlyEM) | Same as fig4a. |
| figs4-1ij-segregation-index-biased | blocked (data_missing for FlyEM) | The FlyWire half may be testable from `wire0sr140_neuralDBScan3000mi1.mat`. |
| fig4e-unsegregated-higher | reproduced | Cell 26: neuron SC z = +23.5, p = 1.9e‑122; synapse SC z = +6.6, p = 3.8e‑11; both below 0.05/6. Total 2,373,104; the null-totals check gives p = 0.832, as in the paper. Without nuisance removal the direction reverses (z = −6.4 and −9.0). |
| fig4f-segregated-lower | reproduced (reading a) | Cell 27: neuron z = −5.4, p = 8.5e‑8; synapse z = −10.2. Reading (b) was not run. |
| fig4i-reciprocal-higher | reproduced | Cell 28: neuron p = 3.7e‑128; synapse p = 7.7e‑4, below 8.3e‑3. |
| figs4-1-flyem-permutation | blocked (data_missing) | No FlyEM selected-synapse or null SC matrices are in either deposit (checked). |
| fig4h-reciprocal-distances | blocked in the notebook, without justification | `results/neuralsc/wire0sr140_reciprocalDistances.mat` is deposited, and the claim is FlyWire-only. Untested. |
| fig5b-walking-activation | reproduced | Cell 31: under the hemibrain atlas, LAL, FB, IPS and GNG all pass readings (a) and (b) with the graded regressor. |
| fig5b-walking-suppression | not_reproduced | Cell 33: no voxel is below −3.24 (minimum t = −1.01). WED(R) and AVLP(R) are 100 % and 95 % positive-significant. At the README's negative peaks the notebook finds t = +3.01 and +4.03. |
| fig5-wagn | blocked in the notebook, partly testable | I looked up the WAGN neuron (id 720575940644632087) in the already-loaded deposited PPSSI table: 0.1332, matching 0.133 ± 0.0133. The connectivity counts need codex sc50. |

### B. Problems

1. **[affects a conclusion] Motion and slice-timing correction are missing** (`process_fly`, `glm_betas`; cells 7 and 30). The Methods and M1 require SPM12 motion and slice-timing correction, and the code's prefix "ar" marks it. The notebook streams the raw green series with only one registration of the mean image. This deviation is stated nowhere; the `flyfc` docstring lists only the registration and tCompCor choices.
   - It is the most likely cause of r = 0.600/0.564 against the paper's 0.73/0.68 and of the per-region values correlating only r = 0.653 with the paper's deposited values.
   - It also likely causes the fig3g failure.
   - In this pipeline Poly-tCompCor *lowers* the FC-SC r (0.638 → 0.600, cell 18), the opposite of the paper's direction.
   - fig3d, fig3g and fig5b-suppression should be rerun with this step before their outcomes are trusted.
2. **[affects a conclusion] Left-right orientation is not settled** (`choose_flip`, cells 5 and 6). Cell 6 says the flipped and unflipped correlations are "nearly equal", but cell 5 prints 0.73 for the x-flip against 0.44 unflipped. The left-right swap moves fig3e to 44 of 63 (outside tolerance) and fig4e's synapse result to p = 0.83. The NWB file's processed series, already in FDA space, could have settled the orientation.
3. **[affects a conclusion] The permutation outcomes are fragile** (cells 26–28). They hold only with Poly-tCompCor. With no nuisance removal, fig4e reverses, fig4f's neuron result vanishes (p = 0.73) and fig4i's synapse result reverses. Since the Poly-tCompCor here sits on uncorrected data (problem 1), the passing outcomes are not robust.
4. **[affects a conclusion] The GLM departs from the code in ways never checked** (`glm_betas`, `second_level`):
   - no Tukey-8 pre-whitening at the first or second level;
   - tCompCor taken from unsmoothed native voxels, where `glmFlyMB1st.m` takes it from smoothed data;
   - no motion correction.

   These are stated as assumptions, but whether they matter was never tested, and the README's negative peaks come out positive here. The paper's own second level (`results/glm/s80poltcomparfly-all-Tukey8full.mat` on Zenodo) was not loaded for comparison.
5. **[affects a conclusion] Connectome claims marked blocked without a reason** (cell 0 table: fig4h, fig5-wagn, fig4a, fig4c, figs4-1ij). Zenodo 15532272 holds `wire0sr140_reciprocalDistances.mat`, `wire0sr140_neuralDBScan3000mi1.mat` and the per-neuron PPSSI table (`flywire783_neuron*.mat`). `plotNeuralFC.m` names the FlyWire ids of CT1-R, APL-R and WAGN.
6. **[affects a conclusion] Possible claims-file misreading in fig4b.** The claims file's quantity is "neurons with a PPSSI = 139,255". The paper's 139,255 is the number of neurons the index was *applied to*; the code README itself uses 138,144 as the count with a value.
7. **[affects a conclusion] fig3a is printed as if complete** (cell 35). The FlyEM confidence-0 value is not in the deposit, and the notebook does not say so.
8. **[does not affect a conclusion] The connectome-only "reproduced" outcomes rest on the paper's own deposited tables** (fig3c, figs3-1a, fig3f, fig4b; stated in cell 34). They show the paper's text agrees with its deposit, not that the counts come out of the raw connectomes.
9. **[does not affect a conclusion] Claims-file header error about the atlases.** The header says the SCKm and DistKm atlases come from Zenodo 15532271; the deposit holds their SC lists and outputs, not the atlases. `makeVoxelROIatlas.m` could rebuild DistKm from repository inputs, but the new k-means labels would need SC recounted from FlyEM synapses, so the blocked status stands.
10. **[does not affect a conclusion] Fixed voxel spacing.** `NATIVE_SPACING_MM` is fixed at fly-087's grid, while six flies differ (cell 3). The affine stage absorbs this.
11. **[does not affect a conclusion] Smoothing padding.** `glm_smooth` pads with zeros, while MATLAB's `imgaussfilt3` default is replicate. This matters only at the volume border.
12. **[does not affect a conclusion] Helper functions check out on synthetic inputs.** `second_level` equals an explicit stacked-identity OLS (df 56). `mean_zfc` sets the diagonal to the largest finite value. `fcsc_r`, `interp_matrix` (identity and half-voxel shift), `normal_p` (ddof = 1) and `glm_smooth`'s kernel radii (7, 7, 5, as MATLAB's) are all correct. `poly_regressors` matches `getNuisancePolynomial.m`, and the GLM keeps the same columns as `glmFlyMB2nd.m` (`[1 9:end]`). The walking regressor matches the code's `behavior.mat` to 7e‑6, and fly-100 is correctly identified as the one left out.

### C. What I could not check, and the output that would settle it

- **Whether the raw NWB green series is already motion-corrected.** Per-volume displacement from rigid realignment, or each volume's correlation with the mean, would show it.
- **Orientation.** The correlation of each fly's registered mean image with the Brezovec processed (FDA-space) mean, under both x-orientations, would settle left and right.
- **How much ANTs run-to-run variation moves the results.** fig3e's 54 is within 2 of its bound. fig3d r and the fig3e count from two or three repeated registrations would show it.
- **The suppression result.** The paper's deposited second-level t map, read from `Tukey8full.mat` and printed at the README peaks and over WED/AVLP, would separate a pipeline effect from a data effect.
- **The permutation tests.** The paper's own deposited target and null R values (`poltcomparhemiroi_fw0sr140_{sp10…, sp90…, rc20…, rd*}-fcauc.mat`) set beside the notebook's z values.
- **fig4b's histogram.** It was shown only as an image; whether its shape is "normal" rests on the printed bins: unimodal around 0.45, with 6,154 neurons at exactly 1.
