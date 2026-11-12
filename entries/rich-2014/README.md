# Rich, Liaw & Lee (2014) from CRCNS hc-31

Tests the findings of [Rich, Liaw & Lee (2014)](https://doi.org/10.1126/science.1255635) on
[CRCNS hc-31](https://doi.org/10.6080/K0BV7DT2), which holds the spikes, positions, PRE sleep periods
and the paper's own place fields for the 253 CA1 cells of five rats that explored a novel 48 m track
and an open field. Place fields are recomputed from spikes and position by the paper's method; the
data set's own fields are shown as a variant.

| Claim | Outcome |
|---|---|
| 253 cells, 63, 58, 24, 57 and 51 per animal | Reproduced |
| Field number uncorrelated with cluster quality (Fig. S3) | Blocked: data missing |
| New sections add fields to place cells and recruit silent cells | Reproduced |
| Single cells with six or more fields are Poisson (Fig. 2A) | Reproduced |
| No population bias in location or interval (Fig. 2B, C) | Reproduced |
| Cells with fewer than six fields uniform (Fig. S6) | Reproduced (assumption) |
| Field counts overdispersed against equal-rate Poisson | Reproduced |
| Mean fields per cell per animal (Fig. S7A) | Partially reproduced |
| Negative binomial r 0.57, p 0.14 | Reproduced |
| Recruitment about 65% at 48 m | Reproduced |
| Recruitment follows the Lomax curve (KS 0.05) | Partially reproduced (assumption) |
| 90% recruitment at about 500 m | Reproduced |
| Uniform field density (KS 0.03) | Partially reproduced |
| No influence of track features or speed (Fig. S10) | Not reproduced (assumption) |
| Field propensity stationary along the track (Fig. S11) | Reproduced |
| No change of propensity at section boundaries (Fig. S11) | Not reproduced (assumption) |
| Field locations uncorrelated between cells (Fig. S12) | Not reproduced |
| Memoryless recruitment (Fig. 3E, S13) | Reproduced |
| Field size and rate uncorrelated with location and field number (Fig. S14) | Not reproduced |
| Higher detection threshold (Fig. S15) | Partially reproduced |
| Weak relation to anatomical position (Fig. S16) | Reproduced |
| PRE sleep rate predicts field number (Fig. 4A) | Reproduced |
| 5 to 10% single-field cells over a wide range of sizes (Fig. 4B) | Not reproduced |
| Active subsets distinguish environments (Fig. 4C) | Not reproduced |
| Silent cells fire very little (Fig. S5) | Partially reproduced |
| Some silent cells form fields in the open field (Fig. S8) | Reproduced |
| Propensities correlated across environments (Fig. S17) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

"Assumption" marks outcomes that rest on the reading of a "pass" through a field, which the paper
leaves open; under the other reading those four claims would be reproduced. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/rich-2014-01.yaml`](../../attempts/rich-2014-01.yaml).
