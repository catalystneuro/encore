# Haley, Hampton & Marder (2018) from OSF r7aes

Tests the findings of [Haley, Hampton & Marder (2018)](https://doi.org/10.7554/elife.41877) on
[OSF:r7aes](https://osf.io/r7aes/), which holds the raw Axon recordings of the paper's
stomatogastric (STG), cardiac (CG) and picrotoxin (PTX) experiments: one file per pH step, with a
README per STG and CG experiment. The manual state annotations and the Spike2 burst output behind
the paper's figures are not in the project.

| Claim | Outcome |
|---|---|
| Example STG and CG preparations (Figures 2, 6) | Reproduced (fig2a, fig2bcd, fig6a); not reproduced (fig6) |
| STG burst measures across pH (Figure 3D to F, supplement 2) | Reproduced (3e, 3s2); not reproduced (3d, 3f) |
| STG and CG fraction of time rhythmic (Figures 3C, 7B, 8) | Not reproduced (3c, 7b, 8a, 8b, 8b cross-predictive); reproduced (robust 6.1 to 8.8) |
| Semi-isolated PD and LP with PTX (Figure 4) | Reproduced (4a, 4bc); partially reproduced (4de, 4fg) |
| CG burst measures across pH (Figure 7C to E, supplement 2) | Reproduced (7e, 7s2); not reproduced (7c, 7d) |
| Baseline frequency correlations | Not reproduced |
| Intact PD and LP depolarize in acid | Reproduced |
| State transitions, Figure 3A examples, gastric-like rhythms (Figure 5) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every outcome rests on assumptions the paper leaves open: spike thresholds set automatically where
the authors set them by hand, states read from the spikes in place of the hand-annotated ones (for the STG, PD bursting with LP and PY firing on the lvn; for the CG, LC bursting), and the pH of the PTX files
taken from their recorded bath pH. The attempt record, with the reasons and the differences from
the paper's method, is [`attempts/haley-2018-01.yaml`](../../attempts/haley-2018-01.yaml).

- `reproduce_haley_2018.ipynb`: the analysis. It streams every STG and CG file whole (about
  64 GB, as the notebook prints, checking each SHA-256) and the last minute of each PTX file.
  The revisions' runs took 31 and 40 minutes (the last cell prints the time), reading OSF through
  WaterButler at a throttled request rate, as osf.io answers bursts of requests with 429.
- `crabph.py`: reading the .abf files from OSF, the READMEs, spikes and bursts, the intracellular
  measures, and the ANOVAs. Other notebooks on this project can import it.
- `r7aes_files.py`: the pinned version, size and SHA-256 of every file.
