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
| 685 BLA neurons from 30 mice (Figure 4) | Partially reproduced |
| Photoidentified BLA-NAc and BLA-CeA neurons (Figure 4c) | Blocked: metadata insufficient |
| Seven functional clusters of BLA responses (Figure 4d) | Blocked: methods underspecified |
| Behavior clusters from pose (Figure 5d-h) | Partially reproduced |
| 13 claims comparing CRISPR and control mice, or tagged projectors | Blocked: metadata insufficient |
| 19 claims on experiments not in the dandiset | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The NT sensor response to sucrose rises after learning in every reading, but reaches p < 0.05
(p = 0.005) only with all trials, each trial z-scored against its own baseline and the regression
fitted on the trial-averaged baseline; with the first 16 trials (p = 0.09), the session baseline
(p = 0.16) or a regression fitted on the pooled baseline bins (p = 0.64) it does not, so it is not
reproduced; the airpuff decrease goes in the paper's direction without reaching
p < 0.05. The units are not sorted single units, so the neuron and tagged-unit counts are far above
the paper's; the light block taken as the "fake" phototagging session evokes responses in most
units, so the tagged count does not test the claim, which is blocked. The pose has no timestamps; a clock fitted to the port entries aligns it in 21 of 29
sessions, and under every reading the behavior clustering gives one of the paper's counts (seven sucrose
and five shock clusters) and not the other; the counts move with numerical detail such as the PCA
solver. No file says which recorded mice are CRISPR and which
control. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000689-li-2022-01.yaml`](../../attempts/000689-li-2022-01.yaml).
