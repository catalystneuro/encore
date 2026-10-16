# Even-Chen, Sheffer, Vyas, Ryu & Shenoy (2019) from dandiset 000121

Tests the findings of [Even-Chen et al. (2019)](https://doi.org/10.1371/journal.pcbi.1006808) on
[DANDI:000121](https://dandiarchive.org/dandiset/000121/0.220124.2156), which holds 12 sessions of
delayed center-out reaching recorded with Utah arrays: all 7 sessions of monkey R and 5 of the 16
of monkey J.

| Claim | Outcome |
|---|---|
| Sessions have the configurations the Methods list | Partially reproduced |
| R's trial counts per configuration | Partially reproduced |
| J's 16 sessions | Blocked: data missing |
| Delays, reaction and reach times | Partially reproduced |
| 74 (J) and 80 (R) channels tuned to target position | Reproduced |
| Variance of the top PCs of condition averages | Not reproduced |
| Variance in the spatial plane per task | Not reproduced |
| Time course of the state in the spatial plane | Partially reproduced |
| Single-trial neural deviations predict the hand at maximum speed | Reproduced |
| The speed axis varies with speed within a distance | Partially reproduced |
| Distance information remains after removing speed | Reproduced |
| The distance axis projects half as much as speed onto the top PCs | Not reproduced |
| Single-trial variance of the speed axis and the plane | Not reproduced |
| Condition ellipses point along the condition mean | Reproduced |
| On-axis deviations exceed off-axis ones | Partially reproduced |
| Relative deviations fall with distance | Reproduced |
| SVM accuracy for ring direction and distance | Not reproduced |
| SVM accuracy per ring of the 3-rings task | Partially reproduced |
| Arc-length errors do not depend on ring distance | Not reproduced |
| Distance errors, and their rise after projection to the plane | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The units' `electrode_group` labels are swapped in every file; the analysis takes as PMd the array
the data identify (units 96 to 191). The attempt record, with the reasons and the differences from
the paper's method, is
[`attempts/000121-even-chen-2019-01.yaml`](../../attempts/000121-even-chen-2019-01.yaml).

- `reproduce_even_chen_2019.ipynb`: the analysis. It takes about nine minutes, a third of it
  streaming the files.
- `premotor.py`: loading the sessions, reduced to delay-period counts, a time course around target
  onset and hand kinematics per trial, and the spatial plane, on/off-axis split and SVM used by the
  notebook. Other notebooks on this dandiset can import it.
