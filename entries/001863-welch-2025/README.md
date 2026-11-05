# Welch, Gonzales-Hess, Tarvin, Connor & Smear (2025) from dandiset 001863

Tests the findings of [Welch et al. (2025)](https://doi.org/10.1101/2025.07.09.663970) on
[DANDI:001863](https://dandiarchive.org/dandiset/001863/0.260806.2109), which holds one DOI and
one saline session of the olfactory search task for each of 22 mice: trial tables, DeepLabCut
tracking, thermistor sniff cycles and head-twitch (HTR) times.

| Claims | Outcome |
|---|---|
| Accuracy, trial counts, repokes and false reports (Figure 1, six claims) | Reproduced |
| Reward-port duration (Figure 2, nine claims) | Blocked: data missing |
| Trial and ITI duration (Figure 3A, 3B, three claims) | Reproduced |
| Speed: lower within trials and in the ITI on DOI (Figure 3C, 3D) | Partially reproduced |
| Speed by trial type (Figure 3 supplement, five claims) | Four reproduced, one partially |
| Sniff frequency (Figure 4, four claims) | Reproduced |
| Occupancy (Figure 5A, 5B) | Reproduced |
| The event series is the HTR times (link claim) | Reproduced |
| HTR location, timing and sex (Figure 5, five claims) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The tracking has no frame times, and the paper's code places frame i at i / 80 s, which does not
line the frames up with the trial table; a clock fitted to each session does. The claims are
tested with the code's clock, as the claims file fixes it, and the notebook shows the fitted clock
as a variant: with it the within-trial speed difference and the within-trial HTR preference vanish,
and HTRs are rarer within trials than in the ITI. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001863-welch-2025-01.yaml`](../../attempts/001863-welch-2025-01.yaml).

- `reproduce_welch_2025.ipynb`: the analysis. It takes about six minutes, one of them streaming the
  files and most of the rest the permutation tests.
- `doi_search.py`: loading the files, the measures of the paper's code (tracking cleaning, speed,
  rolling accuracy, sniff frequency, HTR maps), R-style tests and the clock check. Other notebooks
  on this dandiset can import it.
