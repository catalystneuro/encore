# Peyrache, Lacroix, Petersen & Buzsaki (2015) from dandiset 000056

Tests the findings of [Peyrache et al. (2015)](https://doi.org/10.1038/nn.3968) that can be tested on
[DANDI:000056](https://dandiarchive.org/dandiset/000056/0.250624.0430), which holds spike times, LED
positions, sleep states and LFP from 40 sessions of 7 mice recorded in the anterior thalamus and the
post-subiculum. The units carry no brain region, so head-direction (HD) cells of the two structures are
pooled, and the claims that compare them are blocked.

| Claim | Outcome |
|---|---|
| 353 of 1077 recorded cells are HD cells | Partially reproduced (378 HD cells, but a fraction of 0.22) |
| HD cell rates are correlated between waking and sleep | Reproduced |
| Pairwise correlations are similar across brain states | Reproduced |
| Zero-lag correlation crosses zero at about 60 degrees | Reproduced |
| The internal HD signal is about tenfold faster in slow-wave sleep | Partially reproduced (8.3-fold) |
| It is similar in REM sleep and waking | Reproduced |
| Noise correlations, excess at 0 degrees and dip at 60 degrees | Reproduced |
| Decoded HD tracks the head in waking | Reproduced |
| Comparisons of the ADn and the PoS (12 claims) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000056-peyrache-2015-01.yaml`](../../attempts/000056-peyrache-2015-01.yaml).

- `reproduce_peyrache_2015.ipynb`: the analysis. It takes about six minutes, three of them streaming the
  files.
- `hd.py`: loading the files, the open-field epoch, HD cell classification, binned activity, the
  cross-correlogram estimate of angular velocity and a Bayesian decoder. Other notebooks on this
  dandiset can import it.
