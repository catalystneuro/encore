# Nishimoto and Gallant (2011) from CRCNS mt-2

Tests the findings of [Nishimoto and Gallant (2011)](https://doi.org/10.1523/jneurosci.6801-10.2011)
on [CRCNS mt-2](https://doi.org/10.6080/K0DN4374), which holds, for 45 of the paper's 52 MT neurons,
the movie patch around the receptive field and the response averaged over repeats, at the 83 Hz
frame rate.

| Claim | Outcome |
|---|---|
| Compressive and divisive model predicts with mean r = 0.52 | Not reproduced (0.448) |
| The model accounts for 35% of the explainable variance | Blocked: data missing (no single repeats) |
| An example neuron is predicted with r = 0.72 | Reproduced |
| Luminance and contrast normalization has no significant effect | Reproduced |
| A compressive nonlinearity improves predictions (16% and 19%) | Partially reproduced |
| An expansive nonlinearity worsens predictions (-36% and -24%) | Partially reproduced |
| Divisive normalization improves predictions (8%) | Not reproduced |
| Compressive and divisive model is best | Reproduced |
| The nonlinearity effects do not depend on divisive normalization | Reproduced |
| Complex cells carry most of the prediction | Reproduced |
| Null model on-plane ratio 0.36 | Reproduced |
| Excitatory on-plane ratio 0.59, above the null | Reproduced |
| Suppressive on-plane ratio 0.18, below the null | Reproduced |
| Most neurons form a partial ring | Reproduced |
| No correlation of prediction with the horizontal-vertical ratio | Partially reproduced |
| Pattern indices mostly from -6 to 2 | Not reproduced |
| Horizontal-vertical ratio correlates with the pattern index (r = 0.46) | Not reproduced |
| No correlation of prediction with the pattern index | Reproduced |
| Natural movies predicted as well as motion-enhanced ones | Partially reproduced |
| Simulated receptive fields are recovered | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The model is fitted at a reduced size: the filter bank follows the paper's rules, but the
regression weights are pooled over space onto 763 regressors so that 12 models for 45 neurons fit
in an hour. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/nishimoto-2011-01.yaml`](../../attempts/nishimoto-2011-01.yaml).

- `reproduce_nishimoto_2011.ipynb`: the analysis. It takes about 55 minutes, two neurons at a time.
- `mt2.py`: streaming the files, the filter bank, boosting with early stopping, the null and
  simulated neurons, gratings and plaids, and the spectral measures. Other notebooks on this data
  set can import it.
