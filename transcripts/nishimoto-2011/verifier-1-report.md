**Verifier report, round 1: Nishimoto & Gallant (2011) on CRCNS mt-2**

The claims file has 20 claims. The notebook tests 19 and blocks 1. One fact applies to every model-based claim: the notebook does not fit the paper's model. It downsamples the frames from 128 to 32 pixels and pools the bank onto 763 regressors (deviation D in `mt2.py`).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig3b-mean-prediction | not_reproduced | Cell 11: mean r is 0.448. The best reading gives 0.451 (sigma chosen on held-out data), below the 0.468 lower bound. All 45 neurons fall between 0.2 and 0.8, as in Fig. 3B. The model was pooled for compute (problem 1), so this tests a reduced model. |
| fig3b-explainable-variance | blocked: data_missing | `psths` holds only the mean over repeats. The archive listing has only 45 `.mat` files, docs, `checksums.md5` and `filelist.txt`. No trial-level files exist, so no part can be tested as David & Gallant (2005) specify. |
| fig3a-example-neuron | reproduced | Cell 13: 3 neurons fall in 0.648–0.792 (ct0013 0.710, ct0021 0.708, ct0039 0.730). None of them shows 10 repeats. |
| fig2b-contrast-normalization-no-effect | reproduced | Cell 17: change −0.3% (a), Wilcoxon p = 0.41, ×11 = 1. Enhanced-only p = 0.89. |
| fig2b-compressive-improves | partially_reproduced | Cells 15/19: both increases are significant (×11 p ≈ 1e-7 and 2e-8). No single reading puts both values in tolerance: reading (b) gives 9.2% (expected 16 ± 4) and 16.1% (expected 19 ± 4, within). |
| fig2b-expansive-decreases | partially_reproduced | Cell 21: both decreases are significant. Reading (b) gives −26.9% (expected −36 ± 4, outside) and −24.5% (within). With divisive normalization, the expansive model beats the simplest model in 7 of 45 neurons, against the paper's "always". |
| fig2b-divisive-improves | not_reproduced | Cell 23: reading (b) gives 5.1% (within 8 ± 4), but Wilcoxon p = 0.0051, ×11 = 0.056 and ×5 = 0.026. The criterion needs corrected p < 0.01, and its partial grade also needs a significant increase. |
| fig2b-compressive-divisive-best | reproduced | Cell 25: compressive + divisive beats compressive alone (p = 1.6e-4; ×11 = 0.0017, ×12 = 0.0019). No other model is better: the closest, lum compressive + div, differs by −0.0065 (p = 0.36). |
| fig2b-no-interaction | reproduced | Cell 27: under both readings, with and without divisive normalization, compressive is better and expansive worse, all with ×11 p < 1e-7. |
| complex-cells-dominate | reproduced | Cell 29: complex-only gives mean r 0.448, the same as the full model (r² ratio 1.001). Simple-only drops to 0.194. The simple-only arm is weakened (problem 8), but the first condition alone carries the claim. |
| fig6a-null-on-plane | reproduced | Cell 33: 12 of 40 combinations fall in 0.324–0.396. Under the combination that also passes fig6a and fig6b (plane aaa, null aaa) the null mean is 0.3956, at the tolerance edge. A second consistent combination (plane baa, null aaa) gives 0.378. This null is the paper's chance level (0.36). |
| fig6a-excitatory-on-plane | reproduced | Cell 35: 40 of 40 combinations pass. The mean is 0.55–0.60 and the rank-sum against the null is p ≤ 0.01. |
| fig6b-suppressive-off-plane | reproduced (fragile) | Cell 37: 6 of 40 combinations pass, among them plane aaa with null aaa (0.168 against null 0.201, p = 0.0029), the same combination that passes fig6a. With the null's offset rate reading (b), no combination is significant, and quantity reading (b) puts the mean (0.11) outside tolerance. |
| fig7a-partial-ring | reproduced | Cell 39: 25 of 32 combinations pass, including aaa/a: 71% of neurons between the extremes, 6.7% low, 22% ring. |
| fig7a-no-corr-prediction-hv | partially_reproduced | Cell 41: p > 0.10 in 10 of 16 readings and p < 0.05 in 2. The reading that passes fig6a, fig6b and fig7a (aaa/a) gives r = −0.28, p = 0.061, which is in the partial band. r is negative in all 16 readings. |
| fig7b-pattern-index | not_reproduced | Cell 43: 0 of 4 combinations pass. Medians run from −8.6 to −10.7, and only 0–18% of neurons fall in −6.6 to 2.2. The noise-free simulation (problem 2) may cause part of this. |
| fig7c-hv-pattern-correlation | not_reproduced | Cell 45: 0 of 64 combinations pass. r runs from −0.34 to 0.33, and no positive r reaches p < 0.01. It rests on pattern indices that are themselves not reproduced. |
| fig7c-no-corr-prediction-pattern | reproduced | Cell 47: p > 0.10 in 3 of 4 readings, including the primary one (a, 120°: p = 0.13). The fourth gives p = 0.055. It is a weak test, because the pattern indices are far outside the paper's range. |
| natural-movie-control | partially_reproduced | Cell 49: 14 neurons have `nrange`, against the paper's 15. Wilcoxon p = 0.24. The natural mean, 0.493, is within tolerance; the enhanced mean, 0.462, is below 0.483. The identification of `nrange` as the natural movie rests on its lower motion content in 14 of 14 neurons (cell 5), which is convincing. |
| fig8-recovery-simulated | reproduced | Cell 51: under both noise readings each recovered field correlates best with its own true field (diagonals 0.84/0.57/0.50 and 0.79/0.60/0.67; off-diagonals ≤ 0.13). |

### B. Problems

1. **[affects a conclusion]** `mt2.pooling`, `load`, cells 0/11/19/21/23/43. The fitted model is not the paper's model. The paper fits about 5956 filters at every position; here 32×32 frames are pooled onto 4 or 1 regions (763 regressors), and simple cells enter only at SF 0.75 (one position) and SF 0. The deviation is stated, but its effect is never measured, for example by an unpooled fit on a few small neurons. The shortfall in mean r (0.448 against 0.52), the smaller Fig. 2B effect sizes and the extreme pattern indices may all come from this reduction. The not_reproduced and partially_reproduced outcomes above therefore test a reduced model.
2. **[affects a conclusion]** `pattern_index` and `process_neuron` (plaid block), cell 43. The tuning curves are noise-free model outputs. The Smith et al. Z-scores then grow without bound as the partial correlations approach ±1, so their magnitude depends on numerical detail. My synthetic check: a pure component cell plus 5% noise gives −7.5, against the notebook's medians near −9. Whether, and how, the paper added response variability is an open detail that could change fig7b and fig7c, and only one reading was run. Separately, an exactly pure component cell returns 0.0 (divide by zero at line 553). That case did not occur here (maximum −4.4).
3. **[affects a conclusion]** `boost`, `fit_neuron`. Early stopping uses a patience of 50 steps at 0.01 SD, with `maxit` = 20000. The per-fold iteration counts (`its`) are stored but never printed, so stopping too early or hitting the cap could not be ruled out. Either would lower r (fig3b-mean-prediction).
4. **[does not affect a conclusion]** `bank_outputs` (`CENTRED`) and `shift_rows`. The temporal filters are centred, so a feature reads 5 frames ahead of the response frame, and offsets of 3 or 6 frames (chosen for 14 neurons) extend this to 11 frames ahead. The model is acausal, unlike Eq. 5. The offset is chosen on held-out training data, so validation responses do not leak, and offset 0 for every neuron gives the same mean r (0.448, cell 11). The largest weight share sits at delay 10 (0.131, cell 7), which suggests the delay window is truncated.
5. **[does not affect a conclusion]** `optimal_plane`, balance (a). Coverage ties across speeds are broken by the lowest index. In my synthetic test the true plane (azimuth 90°, speed 5 cRF/s) was found at speed 2.55. The on-plane ratio stayed correct (1.0), but `near_col`, and so the HV ratio, depends on the speed picked. The fig7a outcome is robust (25 of 32).
6. **[does not affect a conclusion]** `hv_ratio`. A regressor's quadrant is set by its SF-direction angle, not its position within the tilted plane, which biases the ratio toward horizontal for fast planes. This is stated in the docstring.
7. **[does not affect a conclusion]** Cell 33. Null movie reading (b) was run only with rate and delay readings (a,a). The claims file asks for every combination to be shown.
8. **[does not affect a conclusion]** `pooling`. The simple-only model lacks the SF 1.5 simple cells and every position but one. This makes the second condition of complex-cells-dominate easy to meet, though the first condition carries the outcome.
9. **[does not affect a conclusion]** `_process`, repeats estimate. It reports up to 33 repeats, while the paper says 5–20, so the estimator is unreliable. It only feeds the fig3a listing.
10. **[does not affect a conclusion]** Cell 5. ct0133 keeps 7093 of 19842 training frames (12729 removed) and enters every test without comment. Separately, for neurons with gaps the lag-product Gram in `Fold` is approximate. It changes only the boosting path, since early stopping uses exact held-out predictions.

### C. What I could not check

- Whether fits stopped at `maxit` or too early. Needed: per-neuron, per-fold `its` for the main model.
- Whether pooling or downsampling lowers accuracy. Needed: an unpooled fit, or a finer pooling, on 2–3 of the 22000-frame neurons, compared with the pooled r.
- The full HDF5 contents, to confirm the blocked claim beyond the archive listing. `read_meta` reads `trange` but never reports it. Needed: the key list and the shape and content of `trange` for one file, to confirm no trial-level responses exist.
- The fig3a candidates among neurons with 10 repeats. Needed: r for ct0028 and ct0030.
- The sensitivity of the pattern index to response noise. Needed: indices with Poisson or trial-like noise added to the simulated grating and plaid responses.
- That the validation segments are contiguous and NaN-free, which `val_corr`'s smoothing and trimming assume. Needed: a printed check per set.
