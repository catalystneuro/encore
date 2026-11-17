# Hunt, Malalasekera et al. (2018) from CRCNS pfc-7

Tests the findings of [Hunt, Malalasekera et al. (2018)](https://doi.org/10.1038/s41593-018-0239-5)
on CRCNS data set [pfc-7](https://doi.org/10.6080/K0PZ5712): the behaviour of two macaques in an
information sampling task (25 and 32 sessions) and 549 single units from ACC, DLPFC and OFC. All 40
claims of the claims file are tested: 37 are reproduced, 2 partially reproduced and 1 not
reproduced.

| Claim | Outcome |
|---|---|
| Sessions and trial counts | Reproduced |
| Neuron counts after the 1 Hz exclusion | Reproduced |
| Choice accuracy, on expected value and on the pictures seen; early choices | Reproduced (assumed) |
| Logistic regressions of choice (Supplementary Figure 1a/b) | Partially reproduced |
| More accurate on 2-picture trials (Supplementary Figure 1c/d) | Reproduced |
| Information sampling (Figure 2a/b) | Reproduced |
| RSA templates at cue 1 (Figure 4d-h, Supplementary Figures 2, 4, 11) | Reproduced |
| t75 latencies (Figure 4) | Reproduced |
| Latency order from simulations (Supplementary Figure 5c) | Not reproduced |
| OFC value comparison subspaces (Figure 5a-k, Supplementary Figures 6, 7) | Reproduced |
| ACC belief confirmation and action subspaces (Figure 6) | Reproduced; Figure 6e under 12 of 72 readings |
| Single-neuron value difference in OFC at each test (Figure 7a) | Reproduced, under 4 of 12 readings |
| Single-neuron value difference collapsed, belief confirmation (Figure 7b/c) | Reproduced |
| Cue 1 single-neuron coding (Figure 8): value, spatial value, attribute value | Reproduced; spatial value under 2 of 26 readings |
| Cue 1 action value in about 18% of ACC and DLPFC neurons (Figure 8) | Partially reproduced |
| EV 16 correlation (Supplementary Figure 9) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's MATLAB scripts are files of the data set; where the claims file leaves a detail open
and a script settles it, the analysis follows the script and says so. The GLM written here gives the
T-statistics the authors stored in the data set to within 1.6e-06, the cue 1 regression its
stored T-statistics to within 3.3e-07, and the Figure 6 weights, on the random halves the scripts
stored, the stored weights to within 2.6e-07; the data the Figure 6 projections use match the
scripts' stored data. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/hunt-2018-01.yaml`](../../attempts/hunt-2018-01.yaml).

- `reproduce_hunt_2018.ipynb`: the analysis. It takes 9 to 16 minutes, about three of them streaming
  the files (about 3 GB, read into memory one file at a time).
- `pfc7.py`: loading the behavioural files and the preprocessed units, and the GLM, RSA and
  regression measures of the paper's scripts. Other notebooks on this data set can import it.
