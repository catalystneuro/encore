# Hasnain, Han & Economo (2025) from dandiset 000363

Tests the findings of [Hasnain, Han and Economo (2025)](https://doi.org/10.1101/2025.10.17.682917)
that can be tested on [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the
Mesoscale Activity Map recordings (Chen et al. 2024) that the paper reuses for its Figure 4. The
paper's own cell-type-specific recordings (Figures 1 to 3) are not public.

| Claim | Outcome |
|---|---|
| The paper's selection gives 20 bilateral ALM and 16 (or 11) ALM and medulla sessions | Not reproduced |
| Medullary units are selective, most in the response epoch (7, 21, 49%) | Partially reproduced |
| In ALM, null and potent subspaces explain comparable variance | Partially reproduced, resting on one reading of 'good' |
| In the medulla, the null subspace explains less variance than the potent | Reproduced, resting on one reading and sensitive to the seed |
| ALM predicts medullary null activity nearly as well as the other ALM | Not reproduced |
| Medulla predicts ALM less well than ALM predicts the medulla | Not reproduced |
| The medullary null subspace has lower dimensionality than ALM's | Not reproduced, resting on one reading of 'good' |
| Medullary units do not span ALM's null activity patterns (UMAP) | Partially reproduced |
| Eleven claims on the paper's own recordings | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper selects sessions with at least 30 units "classified as 'good'". With the `classification`
column, whose units carry the dataset's CCF labels, this gives 5 ALM and medulla sessions, not 16 or
11, so the Figure 4 tests run on fewer sessions and units than the paper's. With the `unit_quality`
column, and CCF labels transferred from the nearest classified unit, it gives 19 sessions with about
2.5 times the paper's units; the second notebook repeats the tests there. Every outcome holds the
unit selection at the `classification` reading while the other readings of the claims file are
searched. Read the same way under the `unit_quality` reading, the ALM claim of Figure 4c would be
reproduced (33.9 against 42.7%, p = 0.251) and the Figure 4e claim reproduced with the participation
ratio (p = 0.027). The `classification` reading is kept because its bilateral unit counts are near
the paper's and its CCF labels are the dataset's own. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/hasnain-2025-01.yaml`](../../attempts/hasnain-2025-01.yaml).

- `reproduce_hasnain_2025.ipynb`: the analysis, under the `classification` reading. It takes about
  40 minutes, most of it streaming the units tables of all 174 files and fitting subspaces.
- `reproduce_hasnain_2025_g2.ipynb`: the Figure 4 tests on the ALM and medulla sessions under the
  `unit_quality` reading. About 50 minutes.
- `map_subspace.py`: loading, label transfer, firing rates, movement masks, subspace identification,
  dimensionality, variance explained, cross-region decoding and selectivity, with where each
  parameter comes from. Other notebooks on this dandiset can import it.

The numbers depend slightly on the processor, since the linear algebra library picks its kernels by
processor. Most move only in the third or fourth digit; the decoding R2, the UMAP embedding and a
few shuffle dimensions under the `unit_quality` reading move more. Two executions on different
runners gave the same outcomes.
