# Nishimoto et al. (2011) from CRCNS vim-2

Tests the findings of [Nishimoto et al. (2011)](https://doi.org/10.1016/j.cub.2011.08.031) that
can be tested on [CRCNS vim-2](https://doi.org/10.6080/K00Z715X), which holds the BOLD responses
of three subjects to 2 hours of training movies and 9 minutes of test movies repeated ten times,
with the movies. The notebook builds the 6,555-filter motion-energy features from the movies, fits
static, nondirectional and directional models to the voxels of V1 to V3B, and identifies test
seconds from the BOLD patterns of subject S1.

| Claim | Outcome |
|---|---|
| Mean prediction accuracy 0.24, 0.39 and 0.40 for the three models | Reproduced |
| The directional model's gain over the nondirectional model is small | Reproduced |
| Motion models beat the static model in every area and subject; V1 is best | Reproduced |
| S1 identifies 464 of 486 test seconds within one volume | Reproduced |
| Receptive fields, and speed tuning against eccentricity | Blocked: too large for the run's time |
| Color information does not improve the models | Blocked: too large for the run's time |
| Identification among 1,000,000 clips, and reconstruction from the sampled prior (three claims) | Blocked: data missing |

The models are fit by ridge regression, not by the paper's L1-regularized regression. The
sampled movie prior and the 1,000,000-clip set are not public. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/nishimoto-2011-reconstructing-01.yaml`](../../attempts/nishimoto-2011-reconstructing-01.yaml).
