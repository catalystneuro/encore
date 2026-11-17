# van der Molen, Spaeth, Chini et al. (2025) from dandiset 001603

Tests the findings of [van der Molen et al. (2025)](https://doi.org/10.1038/s41593-025-02111-0)
on [DANDI:001603](https://dandiarchive.org/dandiset/001603/0.260923.0623), which holds the sorted
spike trains of 8 human organoids, 9 murine organoids, 6 neonatal mouse cortical slices and 8
primary cultures, murine organoids recorded with gabazine and with NBQX and R-CPP, and longitudinal
recordings of two human organoids.

Of the 50 claims, 29 are reproduced, 11 partially reproduced, 5 not reproduced and 5 blocked. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/van-der-molen-2025-01.yaml`](../../attempts/van-der-molen-2025-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Burst detection as the Methods state it reproduces the paper's burst counts and backbone units for
HO1 to HO4 exactly, but finds no burst in four of the nine murine organoids, so claims on murine
organoids rest on the five that have bursts. The baseline sorted file of MO12 and the longitudinal
murine organoid recordings are not in the dandiset.

- `reproduce_van_der_molen_2025.ipynb`: bursts, backbone units, burst-to-burst and pairwise
  correlations, burst similarity, PCA and the comparisons across model types (about 23 minutes,
  most of it the shuffles).
- `hmm_van_der_molen_2025.ipynb`: the hidden Markov model claims (about 22 minutes).
- `sequences.py`: loading the spike matrices and the paper's measures, with the source of each
  parameter. Other notebooks on this dandiset can import it.
- `hmm.py`: a Poisson HMM fitted by EM, in place of the SSM package the paper used.
