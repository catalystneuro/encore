# Neupane, Fiete & Jazayeri (2024) from dandiset 000897

Tests the findings of [Neupane et al. (2024)](https://doi.org/10.1038/s41586-024-07557-z) that can
be tested on [DANDI:000897](https://dandiarchive.org/dandiset/000897/0.240605.1710), which holds 15
of the paper's 32 entorhinal recording sessions (monkey A 6 of 17, monkey M 9 of 15) during the
mental navigation task.

| Claim | Outcome |
|---|---|
| Produced vectors match actual vectors (regression slope) | Reproduced |
| Generalization from the first session | Blocked: data missing |
| 37% and 36% of neurons periodic | Not reproduced |
| Periodicity at or near 0.65 s | Partially reproduced |
| No periodicity in eye and joystick | Reproduced |
| PI higher in navigation than in the ITI | Blocked: metadata insufficient |
| PI lower on error trials | Not reproduced |
| First peak before joystick offset near -0.65 s | Partially reproduced |
| Earlier peaks near multiples of 0.65 s | Not reproduced |
| Longer periodicity on overshoot trials | Partially reproduced |
| Single neurons code distance at onset, offset or both | Reproduced |
| Population coding stronger at offset | Reproduced |
| Rate codes distance more than slope | Not reproduced |
| Distance explains more variance than landmarks | Partially reproduced |
| Cross-correlations conserved in the ITI | Blocked: metadata insufficient |
| Cross-correlations conserved in other epochs | Reproduced |
| Periodic Fano factor in 55% and 43% of neurons | Partially reproduced |
| Periodic Fano factor in non-periodic neurons | Reproduced |
| Motor-related response before offset | Partially reproduced |
| Reset model fits behaviour better | Partially reproduced |
| Model without landmarks scalar, with landmarks subscalar | Not reproduced |
| Other model simulations (two claims), and phase clustering against the model | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000897-neupane-2024-01.yaml`](../../attempts/000897-neupane-2024-01.yaml).

- `reproduce_neupane_2024.ipynb`: the analysis. It takes about 26 minutes.
- `mnav.py`: loading the sessions, smoothed rates, the periodicity index with its Gaussian
  process null, the clock offset of the behaviour traces, the Bayesian observer models and the CAN model. Other notebooks on this dandiset can import it.
