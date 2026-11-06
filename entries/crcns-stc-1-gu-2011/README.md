# Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011) from CRCNS stc-1

Tests the findings of [Gu et al. (2011)](https://doi.org/10.1016/j.neuron.2011.06.015) that can be
tested on [CRCNS stc-1](https://doi.org/10.6080/K07P8WKF). The data set holds derived values: the
noise and signal correlations and preferred headings of the paper's 127 MSTd pairs under 1 mm, and
the tuning curves and choice probabilities of 129 single units of two trained monkeys. It holds no
spike times, distances, training-group labels or naive single units.

| Claim | Outcome |
|---|---|
| The monkeys can be assigned to the naive and trained groups by their pair counts | Reproduced |
| Noise correlation is lower in trained than in naive animals (Figure 2B) | Reproduced |
| The difference holds in each animal (means; Figure S2B) | Reproduced |
| The example pair of Figure 1 | Reproduced |
| Visual and vestibular noise correlations are correlated (Figure 1F) | Partially reproduced |
| Visual and vestibular means do not differ (Figure 1F) | Reproduced |
| Noise correlation rises with signal correlation (Figure 5) | Reproduced |
| Training does not change the slope (Figure 5C) | Reproduced |
| Training lowers the intercept, with non-overlapping intervals (Figure 5D) | Partially reproduced |
| The plane of equation 5 | Partially reproduced |
| Correlations raise the population threshold 5-fold; training has little effect (Figure 6A) | Reproduced |
| Thresholds depend on the slope more than the intercept (Figure 6B) | Reproduced |
| For a pair, reducing correlations helps when rsignal > 0 and hurts when < 0 (Figure 7A) | Partially reproduced |
| At best the trained threshold is about 8% lower (Figure 7C) | Partially reproduced |
| Lateral units are more sensitive around straight ahead (Figures 4D, 4H; trained animals only) | Reproduced |
| Fore-aft units have smaller choice probabilities (Figure 8A, 8B) | Not reproduced |
| Noise correlation does not depend on heading preference (Figure 8C, 8D) | Reproduced |
| Time courses, Fano factors, renormalization, prestimulus correlations | Blocked: data missing |
| Distance groups, single against multiple electrodes | Blocked: data missing, metadata insufficient |
| Training histories, comparisons of naive and trained single units (Figures 2A, 4, S4) | Blocked: data missing |
| Pair tuning curves, task correlations, eye movements (Figures 7B, S5, S6, S8A, S8B) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Seven of the 17 tested outcomes rest on one assumption: the data set holds per-condition noise
correlations, and the paper's pooled value is taken as their mean. Under it the group means of the
main result (0.0241 and 0.1190) lie within the SEMs of the paper's 0.023 and 0.116. Four outcomes
rest on another: the simulations use a tuning amplitude and baseline that the paper does not give.
The Figure 4 test of lateral against fore-aft sensitivity passes under one of the claims file's 8
readings and runs without the paper's selection of significantly tuned units. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-stc-1-gu-2011-01.yaml`](../../attempts/crcns-stc-1-gu-2011-01.yaml).

- `reproduce_gu_2011.ipynb`: the analysis. It runs in about one minute.
- `stc1.py`: loading the data set with its MD5 check, the pairs table, the group assignment, and
  the Fisher information of equations 2 to 5. Other notebooks on this data set can import it.
