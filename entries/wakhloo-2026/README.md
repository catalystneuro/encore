# Wakhloo, Slatton & Chung (2026) from dandiset 000978

Tests the rat findings of [Wakhloo, Slatton and Chung (2026)](https://doi.org/10.1038/s41593-025-02183-y)
on [DANDI:000978](https://dandiarchive.org/dandiset/000978/0.240511.0307), the W-track learning data
of Tang, Shin and Jadhav (2023): spikes from PFC and CA1, position and trials of 8 rats over 8
sessions in one day. The paper's theory, its network simulations and its macaque and pose network
analyses are not about this dataset and are blocked.

| Claim | Outcome |
|---|---|
| Behavioural error falls over sessions 1 to 4, then plateaus | Reproduced |
| Readout error falls over learning in PFC and CA1, then plateaus | Reproduced |
| Readout error correlates with behaviour, R2 0.48 (CA1) and 0.51 (PFC) | Reproduced |
| Theory agrees well with the empirical readout error | Reproduced (criterion amended after a question; not reproduced before) |
| Total dimension drops over sessions 1 to 4 | Reproduced |
| Task-relevant dimension (GLM) increases over learning | Reproduced |
| Nearly every geometric measure increases over sessions 1 to 4 | Reproduced |
| After session 4 dimension rises and correlation falls | Reproduced |
| Quadratic mixed models of dimension, correlation, SNF significant (P < 1e-5) | Reproduced |
| No non-monotonic trend in SSF | Reproduced |
| Quadratic model of task dimension significant (P < 0.01) | Reproduced |
| Linear models of SSF (P < 1e-3) and task dimension (P < 1e-5) | Partially reproduced |
| Late trends match the optimal codes | Partially reproduced (PFC only) |
| GLM cross-validated D2 and its spread across rats | Partially reproduced |
| Hebbian and SVC errors strongly correlated (rat part) | Reproduced |
| Theory, MLP, pose network and macaque claims (12) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The analysis follows the paper's code (github.com/awakhloo/population_geometry_optimal_coding at
commit 9674a6c) where the Methods leave details open. Its per-session measures agree with the
paper's own results files to within a fraction of a percent. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/wakhloo-2026-01.yaml`](../../attempts/wakhloo-2026-01.yaml).

- `reproduce_wakhloo_2026.ipynb`: the analysis. It takes about 33 minutes on 4 cores, most of it the
  5684 per-unit GLM fits.
- `wtrack.py`: streaming and binning the files, the readout measures (Eqs. 3 and 5 to 9), the GLMs
  and the mixed models, each with the source of its parameters. Other notebooks on this dandiset can
  import it.
