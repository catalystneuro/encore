# Du, Lai, Hu & Ye (2026) on LINK, MC_RTT and MC_Maze

Tests the findings of [Du et al. (2026)](https://doi.org/10.64898/2026.08.04.742876), "A
Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding", on
[DANDI:001201](https://dandiarchive.org/dandiset/001201/0.251023.2336) (LINK) and
[DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) (MC_RTT), at the versions the
paper cites, on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze-medium,
data elsewhere, at the version the claims file names), and on the synthetic data its code generates. The estimators in `du2026.py` are ports
of the paper's released code (github.com/gwkuqgfkqe/neural-decoder-context-audit, tag
v1.0-jne-submission, commit b042fbe), reading the NWB files by streaming them.

| Claims | Notebook | Outcome |
|---|---|---|
| Synthetic calibration (3) | `01_synthetic.ipynb` | Reproduced |
| LINK development sessions: sample, neural-only R2, context ladder, task contrast, fully nested gains, replacement and permutation controls, practical magnitude, representative trial, split seeds, nonlinear maps (17) | `02_link_development.ipynb` | Reproduced |
| LINK estimator families (1) | `03_link_estimators.ipynb` | Reproduced |
| LINK temporal offset and context capacity (2) | `04_link_temporal_capacity.ipynb` | Reproduced |
| LINK confirmation sessions (4) | `05_link_confirmation.ipynb` | Reproduced, seed sensitive |
| MC_RTT (4) | `06_mc_rtt.ipynb` | Reproduced |
| MC_Maze (2) | `07_mc_maze.ipynb` | Reproduced, seed sensitive |

Almost every value equals the paper's at its printed precision. The confirmation values hold only
under the paper's split seed; under other split seeds the pattern holds but the values move outside
their 10% tolerances. The MC_Maze gains (about 0.0005 and smaller) likewise match the paper under its
estimator seed and move outside the tolerances under others. `07_mc_maze.ipynb` also runs the
release's own estimator code next to the ports, which give the same values. The attempt record, with the deviations and findings, is
[`attempts/du-2026-01.yaml`](../../attempts/du-2026-01.yaml).
