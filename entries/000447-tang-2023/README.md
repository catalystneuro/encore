# Tang, Shin & Jadhav (2023) from dandiset 000447

Tests the findings of [Tang, Shin and Jadhav (2023)](https://doi.org/10.1016/j.celrep.2023.112246)
that can be tested on [DANDI:000447](https://dandiarchive.org/dandiset/000447/0.250724.2224), which
holds CA1 and prefrontal units, position and trial tables of five rats running a W-maze in a novel
(N), a familiar (F) and again the novel room (N'). The de novo learning sessions and the second group
of rats behind Figure 1 are not in it.

| Claim | Outcome |
|---|---|
| Cells per session (30.5 CA1, 37.4 PFC) | Reproduced |
| PV similarity: CA1 remaps across rooms, PFC does not (Figure 2D) | Reproduced |
| CA1 single-cell similarity across rooms is at shuffle level (Figure S3A) | Reproduced |
| PFC single cells similar across rooms, CA1 lower (Figure S3A) | Partially reproduced |
| PFC similarity grows with experience, CA1 does not (Figure S3C) | Reproduced |
| PFC similarity to F rises over novel trials (Figure S3D) | Reproduced, on an assumption |
| Reward wells no different from other locations (Figure S4D) | Reproduced |
| Decoding: CA1 error higher in F and at chance (Figure 2E) | Partially reproduced |
| Decoding: PFC error similar in N and F, above chance (Figure 2E) | Partially reproduced |
| CA1 error rises at the switch, PFC stable (Figure 2F) | Reproduced, on an assumption |
| Ramping cells are 16.4% (CA1) and 18.1% (PFC) of cell samples | Not reproduced |
| Ramping cells generalize like other cells (Figure S4C) | Blocked: too few ramping cells |
| Path equivalence stronger in PFC (Figure S5D) | Reproduced |
| Path equivalence stable across rooms in PFC (Figure S5E) | Partially reproduced, on an assumption |
| Path equivalence and selectivity uncorrelated (Figure S5F) | Blocked: methods underspecified |
| Selectivity indices: PFC r = -0.5, CA1 r = 0.56 (Figure 3D) | Not reproduced, on an assumption |
| Selectivity stable across rooms in PFC only (Figure 3E) | Not reproduced, on an assumption |
| Pseudo-populations of 98 CA1 and 171 PFC cells | Reproduced |
| Manifold shapes (Figure 3F, 3G) | Reproduced |
| InSeq and OutSeq distances (Figure 3H) | Reproduced |
| Phase and location distances (Figure 3I) | Reproduced |
| F against N' manifolds: PFC preserved, CA1 at shuffle level (Figure 3J) | Partially reproduced |
| The same in the neural space (Figure S6) | Partially reproduced |
| PFC CCGP above shuffles for every decoder (Figure 4D) | Partially reproduced |
| CA1 CCGP at chance (Figure 4D) | Not reproduced |
| CCGP against the geometric random model (Figure S7B) | Not reproduced |
| Most dichotomies decodable, similarly in both regions (Figure S7D) | Partially reproduced |
| Performance higher in F than in N (Figure 1C, N-F-N' rats only) | Not reproduced |
| Figure 1B, 1C sessions and S1B, which need the de novo sessions (four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset has no linearized positions, ripple or theta times, or cell labels, and its units
table stores tetrode numbers where the format expects electrode rows. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000447-tang-2023-01.yaml`](../../attempts/000447-tang-2023-01.yaml).

- `reproduce_tang_2023.ipynb`: the analysis. It takes about 20 minutes, most of it in the
  permutation tests of the decoders.
- `nfn.py`: loading the files, the linearization, rate maps, the decoder, selectivity, path
  equivalence, ramping, single-trial maps and the CCGP decoders. Other notebooks on this dandiset
  can import it.
