# Guan, Aflalo et al. (2022) from dandiset 000147

Tests the findings of [Guan, Aflalo et al. (2022)](https://doi.org/10.7554/eLife.74478) that can
be tested on [DANDI:000147](https://dandiarchive.org/dandiset/000147/0.221122.2256), which holds the
main finger task of all ten sessions of the paper's participant.

| Claim | Outcome |
|---|---|
| Recording counts: 95.8 units and 408 trials per session | Reproduced |
| Online decoding accuracy of 86% | Reproduced |
| 70% of online errors are middle-ring or ring-pinky confusions | Reproduced |
| Offline cross-validated accuracy of 92% | Reproduced |
| 89% of neurons tuned to a finger | Reproduced |
| Cue location cannot be classified from the movement window | Not reproduced |
| Thumb distinct; middle, ring and pinky close | Reproduced |
| RDMs match the able-bodied fMRI model better than the unstructured model | Reproduced |
| RDMs match the MC fMRI model better than the PC-IP model, near the noise ceiling | Reproduced |
| Session RDMs correlate at r = 0.90 | Reproduced |
| No trend toward the unstructured model over sessions | Reproduced |
| Confused-pair distances do not increase | Reproduced |
| All distances decrease slightly | Reproduced |
| Calibration task, control task, cue coordinates, individual fMRI RDMs, component models, well-isolated units (seven claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The fMRI model RDMs are not in the dandiset; they are read from the authors' code repository at
the commit the paper archived. The attempt record, with the reasons and the differences from the
paper's method, is
[`attempts/000147-guan-2022-01.yaml`](../../attempts/000147-guan-2022-01.yaml).

- `reproduce_guan_2022.ipynb`: the analysis. A run takes about 90 s, streaming the data from the archive.
- `ppcfingers.py`: loading the sessions, the crossnobis RDM, diagonal LDA and the other measures.
  Other notebooks on this dandiset can import it.
