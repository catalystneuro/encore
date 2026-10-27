# Dias, Lemoine, Yanco, Zimova, Bay & Weeks (2025) from Dryad dataset bvq83bkk9

Tests the findings of [Dias et al. (2025)](https://doi.org/10.1098/rspb.2024.2556) on
[DRYAD:bvq83bkk9](https://doi.org/10.5061/dryad.bvq83bkk9), version id 333377, which holds the wing
and tarsus lengths of 27 486 Field Museum specimens of five migratory passerines, the climate of each
species and year, and the phylogeny. The paper's code is on Zenodo
([doi:10.5281/zenodo.14226724](https://doi.org/10.5281/zenodo.14226724)).

| Claims | Outcome |
|---|---|
| Sample sizes of the main and preliminary models | Reproduced |
| Preliminary models (Tables S4 to S8): seven claims of absence, interactions, variable selection, phylogenetic signal, collinearity, climate trends | Reproduced (8), blocked (2, methods underspecified: one interval bound lies within Monte Carlo error of 0, and the recorded seed and the majority of ten seed sets give different outcomes) |
| Autumn AHY main model (Table 3): four claims | Reproduced (2), partially reproduced (2) |
| HY and spring AHY main models (Tables 1, 2, S1), expanded ranges (Tables S9 to S11) and the claims built on them: 16 claims | Blocked: too large (estimated at 90 and 74 minutes per fit, about 58 and 47 when scaled by the autumn AHY fits, against a 30-minute notebook limit; three filtering readings each) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The deposited specimens give every sample size of the paper exactly without the outlier filter the
Methods describe, and the README's statement that the filtering is in the code does not hold. The
specimen measurements carry no identifier, so they cannot be linked to the catalogue numbers.
MCMCglmm (R) cannot be installed in the entry's Python environment, so the preliminary models are
sampled by a Gibbs sampler of the same model; the Stan model runs with CmdStan in place of rstan. The Stan fits converge poorly with the code's settings, and the notebooks print the Monte Carlo error and the per-chain value of every probability of direction.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/dryad-bvq83bkk9-dias-2025-01.yaml`](../../attempts/dryad-bvq83bkk9-dias-2025-01.yaml).
