# Hasnain, Han & Economo (2025) from dandiset 000363

Tests the findings of [Hasnain, Han and Economo (2025)](https://doi.org/10.1101/2025.10.17.682917)
that can be tested on [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the
Mesoscale Activity Map recordings (Chen et al. 2024) that the paper reuses for its Figure 4. The
paper's own cell-type-specific recordings (Figures 1 to 3) are not public.

| Claim | Outcome |
|---|---|
| The paper's selection gives 20 bilateral ALM and 16 (or 11) ALM and medulla sessions | Not reproduced |
| Medullary units are selective, most in the response epoch (7, 21, 49%) | Partially reproduced |
| In ALM, null and potent subspaces explain comparable variance | Partially reproduced |
| In the medulla, the null subspace explains less variance than the potent | Reproduced, resting on one reading |
| ALM predicts medullary null activity nearly as well as the other ALM | Not reproduced |
| Medulla predicts ALM less well than ALM predicts the medulla | Not reproduced |
| The medullary null subspace has lower dimensionality than ALM's | Not reproduced |
| Medullary units do not span ALM's null activity patterns (UMAP) | Partially reproduced |
| Eleven claims on the paper's own recordings | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

With the dataset's CCF labels, which only units classified good carry, the paper's selection gives 5
ALM and medulla sessions, not 16 or 11, so the Figure 4 tests run on fewer sessions and units than
the paper's. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/hasnain-2025-01.yaml`](../../attempts/hasnain-2025-01.yaml).

- `reproduce_hasnain_2025.ipynb`: the analysis. It takes about 35 minutes, most of it streaming the
  units tables of all 174 files and fitting subspaces.
- `map_subspace.py`: loading, firing rates, movement masks, subspace identification, dimensionality,
  variance explained, cross-region decoding and selectivity, with where each parameter comes from.
  Other notebooks on this dandiset can import it.
