# Clark, Abbott & Sompolinsky (2026) on dandiset 000939

Tests the findings of [Clark, Abbott & Sompolinsky (2026)](https://doi.org/10.1038/s41593-026-02452-4)
on [DANDI:000939](https://dandiarchive.org/dandiset/000939/0.240528.1542), the postsubiculum
recordings of Duszkiewicz et al. (2024) that the paper reuses, at the version the paper cites. The
1,533 head-direction tuning curves are rebuilt from the NWB files with the paper's procedure; they
match the paper's cached curves on Zenodo to 1e-14 Hz.

| Claim | Outcome |
|---|---|
| Session, unit and head-direction cell counts (link) | Reproduced |
| Tuning curves match the paper's cache (link, with the Zenodo input) | Reproduced |
| Heterogeneous, irregularly spaced peaks (Fig. 1e) | Reproduced |
| Peak numbers, data and generative process (Fig. 5d legend) | Reproduced |
| Mean and fluctuation profiles (Fig. 1f,g) | Reproduced |
| Centers of mass uniform, Kuiper test (Fig. 3a,b) | Reproduced |
| Correlation function approaches circulant form (Fig. 3c, S13) | Reproduced |
| Generative fit (sigma, beta, b) of about (1.42, 2.77, 1.73) (Fig. 4) | Partially reproduced |
| Generative profiles, peak counts, peak heights, flip symmetry, information (Fig. 5a to f) | Reproduced (5 claims) |
| Recorded bump tracks head direction (Fig. 2l) | Reproduced |
| Sorted weights show a Mexican hat (Fig. 2b) | Reproduced |
| Data network is quasi-continuous (Fig. 2e,f) | Reproduced |
| Circulant plus noise collapses (Fig. 2g to i) | Partially reproduced |
| Velocity integration (Fig. 2j,k) | Reproduced |
| Lambda and c grid (Supplementary Figs. 8, 9) | Partially reproduced |
| Global stability of the data network (Supplementary Fig. 11b) | Reproduced (assumed) |
| Spectrum doublets of the data network (Supplementary Fig. 14) | Reproduced |
| Mean-field theory: Mexican hat and stability (Fig. 7) | Reproduced |
| Mean-field timescales (Fig. 7d,e) | Not reproduced |
| Mean-field bump integrates behaviour (Fig. 7c) | Reproduced |
| Large-N eigenvalues and eigenvectors (Fig. 6c,d,f,g) | Reproduced (2 claims) |
| Weight-noise robustness, disordered and circulant (Supplementary Fig. 10) | Reproduced (assumed) |
| Global and finite-N stability of the generative network (Supplementary Figs. 11a, 12) | Reproduced (assumed, seed sensitive) |
| Spectrum does not fix the symmetry, rank-four ensembles (Supplementary Figs. 1, 2) | Partially reproduced (seed sensitive) |
| Grid cells and the toroidal network (Fig. 8) | Blocked: too large for the run's time |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/clark-2026-01.yaml`](../../attempts/clark-2026-01.yaml).

- `tuning_curves.ipynb`: the files, the tuning curves and their statistics, and the generative
  process (about 19 minutes, most of it the generative fit).
- `network.ipynb`: the data-derived network, its weights, dynamics and spectrum (about 38 minutes).
- `network_grid.ipynb`: the lambda and c grid (about 10 minutes).
- `theory.ipynb`: the mean-field theory and the large-N spectra (about 3 minutes).
- `model_sims.ipynb`: the simulations of the generative-process and rank-four networks (about
  51 minutes).
- `hdring.py`: streaming the files, the paper's tuning-curve procedure, the statistics, the
  generative process and the network, in numpy, each function naming the function of the paper's
  code it repeats. Other notebooks on this dandiset can import it.
- `ring_dmft.py`: a copy of the paper's `ring/dmft.py` (MIT licence) without its torch imports.
