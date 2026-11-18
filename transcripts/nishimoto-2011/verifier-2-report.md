**Verifier report, round 2: Nishimoto & Gallant (2011) on CRCNS mt-2**

The claims file has 20 claims. The attempt record gives 20 outcomes: 14 reproduced, 3 partially reproduced, 2 not reproduced and 1 blocked (data_missing). Cell indices below are positions in each notebook's cell list, counting markdown cells, so they differ from round 1. "Main" is `reproduce_nishimoto_2011.ipynb` and "finer" is `finer_pooling.ipynb`. I found no new place where the claims file misreads the paper.

### 1. Outcomes

| Claim | Record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig3b-mean-prediction | reproduced | Yes | Stated. The 3×3 model (finer, cell 5: 0.518) is closer to the paper's model than the 2×2 one. Its offset was chosen on training data only, and no validation data is used for selection. It is still a reduced model (see 3). |
| fig3b-explainable-variance | blocked | Yes | Main cells 5–6: only `psths`, and `trange` is empty in all 45 files. |
| fig3a-example-neuron | reproduced | Yes | Stated. |
| fig2b-contrast-normalization-no-effect | reproduced | Yes | Stated. |
| fig2b-compressive-improves | partially_reproduced | Yes | Stated. Rests on the 2×2 model. |
| fig2b-expansive-decreases | partially_reproduced | Yes | Stated. Rests on the 2×2 model. |
| fig2b-divisive-improves | not_reproduced | Yes, on the 2×2 model | Stated. ×11 p = 0.056 is close to the bound, and the finer pooling was not run for this pair of models (see 3). |
| fig2b-compressive-divisive-best | reproduced | Yes | Stated. |
| fig2b-no-interaction | reproduced | Yes | Stated. |
| complex-cells-dominate | reproduced | Yes | Stated. Now also holds with every simple channel (finer, cell 11). |
| fig6a-null-on-plane | reproduced | Yes | Stated. Under all-(a) readings the value is 0.396, at the edge of the band. |
| fig6a-excitatory-on-plane | reproduced | Yes | Stated. |
| fig6b-suppressive-off-plane | reproduced | Yes, but fragile | Stated. 6 of 40 combinations pass. |
| fig7a-partial-ring | reproduced | Yes | Stated. |
| fig7a-no-corr-prediction-hv | partially_reproduced | Yes | Stated. |
| fig7b-pattern-index | reproduced | Yes, conditionally | The assumption is stated, with the passages quoted (I checked the quote against the paper). It is defensible: firing rates cannot be negative, the prediction includes the intercept b0 (`mt2.py:755`), and the paper says nothing either way. It was adopted after the unrectified reading failed, and the claims file does not list it. Rectifying clips tuning curves, which by itself pulls \|Z\| toward 0. The notebook does not show how much of each tuning curve is clipped, so I cannot tell whether the model reproduces the continuum or only loses the structure of its tuning curves. |
| fig7c-hv-pattern-correlation | not_reproduced | Yes | Fails under every index reading. |
| fig7c-no-corr-prediction-pattern | reproduced | Yes | Holds under every index reading. |
| natural-movie-control | reproduced | Yes | Stated (3×3 pooling, `nrange` read as the natural movie). The direction flips between models: natural is higher in 10 of 14 neurons with 2×2 pooling (main cell 67) and in 5 of 14 with 3×3 (finer cell 14). This does not affect the criterion. |
| fig8-recovery-simulated | reproduced | Yes | Stated. |

### 2. Sentences the numbers do not support

- **Finer cell 6:** "so the finer pooling does not raise it further on these three." In cell 5, ct0006 rises from 0.322 to 0.347. The attempt record's response on fig3b-mean-prediction says the same thing ("does not raise it further on the three neurons"). The 4×4 changes are −0.022, −0.046 and +0.025.
- **Main cell 72 (Summary):** "fig2b-expansive-decreases | partially reproduced (significant, one size outside)." This holds only under reading (b). Under reading (a), which is the value given as measured, both sizes are outside tolerance: −15.1 against −36 and −13.5 against −24 (cell 26).
- **Attempt record, fig3b-mean-prediction deviation:** "every other analysis uses 763 regressors." natural-movie-control is judged on the 1465-regressor model.
- **Attempt record, fig3a-example-neuron and complex-cells-dominate deviations:** these copy the text "could be run for the main model only, so the effect sizes here may differ". These claims are on the main model, and both were rerun with 3×3 pooling.
- **README vs attempt record:** the README says fig3a-example-neuron and complex-cells-dominate are judged in `finer_pooling.ipynb`. The attempt record points both outcomes to the main notebook, and fig3a has measured = 0.71 from the 2×2 model. The outcome is the same either way.
- **Attempt record, fig7c-hv-pattern-correlation and fig7c-no-corr-prediction-pattern notes:** "with the noisy indices … r is 0.177 or less" and "p of 0.32 or more" come from the first of 20 draws only (main cells 61 and 64), and the record does not say so.

Every other "**Result:**" sentence, both Summary sections, the README table and the attempt record notes match the printed outputs.

The attempt record's `verifications` block states my round-1 reasons accurately and in close paraphrase, for every claim. Problems 4, 9 and 10 are not attached to any claim there, but they appear as deviations or findings, which is adequate.

### 3. Round-1 points

**Resolved:**
- 3 (iteration counts): none of 2700 folds hit the cap, and patience 500 gives 0.449 (main cell 12).
- 8: complex-cells-dominate was rerun with every simple channel.
- 9: the strict estimator also gives 10–33 repeats, now recorded as a finding.
- 10: without ct0133 the mean is 0.450 (2×2) and 0.520 (3×3). The Gram approximation is stated.
- 4, 5, 6: recorded as deviations or notes. They do not affect a conclusion.
- Every item in my round-1 "What I could not check" list: iteration counts, cost of the pooling, HDF5 keys and `trange`, r for ct0028 and ct0030, noise sensitivity of the pattern index, and contiguity of the validation sets.
- The division by zero in `pattern_index` is fixed.

**Not run:**
- 7: null-movie reading (b) under all four rate and delay combinations. This is stated and does not affect a conclusion.

**Remaining, bearing on a conclusion:**
1. **Pooling (point 1, partly resolved).** The 3×3 pooling raises r by 0.070 on average. That is larger than the Fig. 2B differences being judged. fig2b-divisive-improves (×11 p = 0.056), the compressive and expansive effect sizes, and the Fig. 6–7 spectral analyses all still rest on the 2×2 model. Refitting the linear and linear-plus-divisive models with 3×3 pooling would decide fig2b-divisive-improves. Separately, the 4×4 check on three neurons is mixed, so whether 3×3 is close to the paper's model is shown for only three neurons.
2. **fig7b-pattern-index (point 2, partly resolved).** The outcome now rests on rectification, adopted after round 1. Needed: for each neuron, the fraction of grating and plaid directions clipped to zero, and the index against that fraction. This would show whether rectification moves the indices by clipping alone.
