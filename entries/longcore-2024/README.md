# Longcore, Villanueva, Nguyen-Ngo, Ghiani, Harrison & Colwell (2024) from Dryad t1g1jwtb0

Tests the findings of [Longcore et al. (2024)](https://doi.org/10.1242/jeb.247235) on
[DRYAD:t1g1jwtb0](https://doi.org/10.5061/dryad.t1g1jwtb0), version id 300765, which holds the percent
suppression of wheel running of 16 mice under four illuminances and three color temperatures, the
per-animal cFos counts in the SCN after 50 lx light at 1950 and 3000 K, and the lamps' spectra.

| Claim | Outcome |
|---|---|
| Light of 0.5 lx and brighter reduced activity, except 0.5 lx at 1750 K | Reproduced |
| All 0.01 lx treatments and 0.5 lx at 1750 K increased activity | Reproduced |
| Within color temperatures, only 50 lx at 1750 K differed (Tukey-Kramer) | Not reproduced |
| At 0.01 lx, CCT had no significant effect | Reproduced |
| Illuminance, CCT and their interaction each significant in the GLM | Partially reproduced |
| Illuminance effect several times the CCT effect | Reproduced |
| CCT effect smallest at the lowest illuminance, growing with illuminance | Partially reproduced |
| Lower CCT suppressed activity less at equal lux | Reproduced |
| AICc order: mouse identity, then sex, then neither | Reproduced |
| Males suppressed less than females | Reproduced |
| Predicted suppression by sex at the extreme treatments | Reproduced |
| Individual mouse effects from -27.9 to +21.5 points | Reproduced |
| No difference in SCN cFos between 1950 and 3000 K | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The Methods give the GLM a log link, but the paper's AICc differences, predictions and mouse effects
are matched by an identity link with illuminance in lux. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/longcore-2024-01.yaml`](../../attempts/longcore-2024-01.yaml).

- `reproduce_longcore_2024.ipynb`: the analysis. It takes a few seconds.
- `alan.py`: reading the staged files, the GLM design and fits (log or identity link, likelihood-ratio
  and Wald tests, AICc, JMP-style scaled estimates). Other notebooks on this dataset can import it.
