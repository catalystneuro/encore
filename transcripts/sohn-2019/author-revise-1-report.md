No outcome changed, but I changed the blocking reason on two claims. The verifier agreed with all 23 outcomes. The entry passes `python tools/entry.py all` (408 s) and `check` (0 errors). Round 1 is recorded under `verifications` in `attempts/000130-sohn-2019-01.yaml`, and nothing is committed.

**Outcome changes**
- **Two RNN claims** (`rnn-curved-manifold`, `rnn-perturbation`): still blocked, but the reason is now `data_missing` in place of `other`, as the verifier proposed. The trained networks and their code are not in the dandiset and are not public.

**Added or corrected in reply to the report**
- **alt-speed-unmodulated (problem 1):** I added a Poisson null (units firing at constant rates, same trials and Set times) and a variant that keeps a fixed set of trials.
  - The observed slopes are below the null mean in 8 of 8, and only 1 of 8 fixed-trial slopes falls outside the null range.
  - I withdrew "the data show the speed is modulated" and stopped using the bootstrap intervals, which are biased upward.
- **Normalised rates (problem 2):** I added soft-normalised and z-scored variants (new helper `rsg.unit_scale`).
  - With z-scored rates, all 8 PCA counts fall in the paper's ranges, against 1 of 8 in the main analysis. The outcome stays `not_reproduced` because the claims file fixed unnormalised rates before the analysis; the notes state the dependence.
  - For encoding-r2, the encoding axis beats 95% of random axes in only 2 of 8 (soft) and 0 of 8 (z-scored) cases. The notes now say the match to the Bayesian estimate is reproduced but its specificity to the axis is not shown.
- **encoding-bayes-beats-linear (problems 3 and 6):** the notes now say the matched control period shows the same Bayesian advantage. RMSE weighted by trial counts gives the same counts.
- **alt-threshold-monotonic (problem 4):** added variants with at least 2 and 3 components (230 and 70 ms before Go), and noted that in the 1-component datasets the minima are trajectory crossings.
- **speed-vs-projection and speed-predicts-tp (problem 5):** correlations of the residuals after removing ts are near zero, so the pooled correlations come from the shared dependence on ts. The paper's control (z-scoring within ts, trial by trial) still gives r = -0.32 (Short) and -0.20 (Long).
- **gpfa claims (problem 7):** cross-validation prefers 12 latents over 8 in all 4 datasets, and the log-likelihood is still rising slightly after 100 iterations. Both GPFA results are unchanged with 12 latents.
- **glm-prior-ts (problem 9):** chance levels are 0 to 14.6% for the prior test (including shifts that keep the prior blocks) and 0 to 2.1% for the ts test. Each prior's ts test alone gives 31.2% and 33.3%, still above tolerance. The choice of Long time points is now recorded as a deviation.
- **dfr-overlap-support:** a bootstrap puts the peak within 480 to 800 ms in 96% of samples.
- **alt-transient-parallel:** the longest-ts result holds in all variants (p = 0.016 to 0.039) except soft normalisation (p = 0.055).
- I updated the conclusions, summary, README and the helper's docstring to match.

**Not done**
- Problem 8 (`tp` offset, `is_outlier` flags, inverted `iti` description) needed no change; the notebook already documented all three.
- The paper's Tables S1 to S3 and supplementary figures are still unavailable, so the fitted model parameters and the paper's random-axis values are not compared.
- A trial-by-trial GPFA analysis of production speed, which is where the paper applies its control for ts, was not run; it is a new analysis.

The re-downloaded paper text is in `paper/`, which git does not track. The untracked dotfiles and `scripts` at the repo root come from the sandbox, not from me.
