# Nishimoto et al. (2011) from CRCNS vim-2

Tests the findings of [Nishimoto et al. (2011)](https://doi.org/10.1016/j.cub.2011.08.031) that
can be tested on [CRCNS vim-2](https://doi.org/10.6080/K00Z715X), which holds the BOLD responses
of three subjects to 2 hours of training movies and 9 minutes of test movies repeated ten times,
with the movies. The first notebook builds the 6,555-filter motion-energy features from the movies,
fits static, nondirectional and directional models to the voxels of V1 to V3B, maps receptive
fields and speed tuning with simulated probes, and identifies test seconds from the BOLD patterns
of subject S1. The second, `color_no_gain.ipynb`, adds the A* and B* color channels.

| Claim | Outcome |
|---|---|
| Mean prediction accuracy 0.24, 0.39 and 0.40 for the three models | Reproduced, with the penalty chosen by cross-validation (assumed) |
| The directional model's gain over the nondirectional model is small | Reproduced |
| Motion models beat the static model in every area and subject; V1 is best | Reproduced |
| Receptive fields are localized and retinotopic (proxy test without the multifocal maps) | Reproduced |
| Optimal speed rises with eccentricity in V1, V2 and V3 | Reproduced |
| S1 identifies 464 of 486 test seconds within one volume | Partially reproduced (409 of 486) |
| Color information does not improve the models | Reproduced |
| Identification among 1,000,000 clips, and reconstruction from the sampled prior (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The models are fit by ridge regression, not by the paper's L1-regularized regression (an assumption). The
sampled movie prior and the 1,000,000-clip set are not public. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/nishimoto-2011-reconstructing-01.yaml`](../../attempts/nishimoto-2011-reconstructing-01.yaml).
