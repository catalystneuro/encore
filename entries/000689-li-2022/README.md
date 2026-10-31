# Li, Namburi, Olson et al. (2022) from dandiset 000689

Tests the findings of [Li et al. (2022)](https://doi.org/10.1038/s41586-022-04964-y),
"Neurotensin orchestrates valence assignment in the amygdala", that can be tested on
[DANDI:000689](https://dandiarchive.org/dandiset/000689/0.240530.1923). The dandiset holds 31 BLA
recording sessions during the three-cue discrimination task (spike times, trial events,
DeepLabCut pose) and the GRAB-NTS1.0 photometry of 5 mice in early and late reward and punishment
learning.

| Claim | Outcome |
|---|---|
| NT sensor response to sucrose increases after learning (Figure 3k) | Not reproduced |
| NT sensor response to airpuff decreases after learning (Figure 3l) | Not reproduced |
| NT sensor dips after both outcomes early in learning (Figure 3, text) | Not reproduced |
| 685 BLA neurons from 30 mice (Figure 4) | Not reproduced |
| Seven functional clusters of BLA responses (Figure 4d) | Blocked: methods underspecified |
| Behavior clusters from pose (Figure 5d-h) | Blocked: metadata insufficient |
| 13 claims comparing CRISPR and control mice, or tagged projectors | Blocked: metadata insufficient |
| 20 claims on experiments not in the dandiset | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The NT sensor effects go in the paper's direction under the per-trial z-score, with sizes near the
paper's, but none reaches p < 0.05 with five mice. No file says which recorded mice are CRISPR and
which control, the units are not sorted single units, and the pose is not on the trial clock. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000689-li-2022-01.yaml`](../../attempts/000689-li-2022-01.yaml).
