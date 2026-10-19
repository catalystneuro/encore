# Pagan, Tang, Aoi, Pillow, Mante, Sussillo & Brody (2025) from dandiset 001550

Tests the findings of [Pagan et al. (2025)](https://doi.org/10.1038/s41586-024-08433-6) on
[DANDI:001550](https://dandiarchive.org/dandiset/001550/0.260916.0811), which holds the
behaviour of 26 rats in a task that switches between accumulating location and frequency
evidence. The electrophysiology is not in the dandiset; the neural claims use the paper's own
data repository on GitHub, at a pinned commit.

| Claim | Outcome |
|---|---|
| The dandiset links to the paper's per-session behavioural tables | Reproduced |
| 26 male Long-Evans rats aged 6 to 24 months | Partially reproduced |
| 542 trials per session on average | Reproduced |
| 14.6 context blocks per session on average | Reproduced |
| Sessions lasted 2 to 4 hours | Reproduced |
| Blocks of at least 30 trials | Reproduced |
| 20 rats with more than 120,000 trials | Reproduced |
| Choices follow the relevant feature in each context | Reproduced |
| Rats switch within about four trials of a new block | Reproduced |
| Most rats learned the task in 2 to 5 months | Reproduced |
| Differential behavioural kernels converge (Figure 4) | Reproduced |
| Location and frequency slope indices uncorrelated across rats | Reproduced |
| Half-split slope indices correlate (r = 0.58) | Reproduced |
| Bilateral FOF silencing impairs performance | Partially reproduced |
| Neural cells link to 199 dandiset sessions | Not reproduced |
| 3,495 units, per-rat counts (paper's GitHub data) | Reproduced |
| Neural location and frequency slope indices uncorrelated (paper's GitHub data) | Reproduced |
| Choice axes parallel across contexts, 1.6 degrees (paper's GitHub data) | Not reproduced |
| Behavioural and neural slope indices anti-correlated (r = -0.73) | Reproduced |
| Variance of the choice axis (Figure 1e) | Blocked: methods underspecified |
| mTDR trajectories (Figure 1f) and the RNN results (Figures 3a, 5c) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001550-pagan-2025-01.yaml`](../../attempts/001550-pagan-2025-01.yaml).

- `reproduce_pagan_2025.ipynb`: the analysis. It takes about 7 minutes: 2 to read the 15,853
  TaskSwitch sessions, 2 to read the paper's neural files from GitHub, and 3 to fit the kernels.
- `taskswitch.py`: loading the sessions (each file is read whole into memory), the session
  selection, the behavioural kernels and slope indices, and ports of the paper's neural slope and
  choice-axis code. Other notebooks on this dandiset can import it.
