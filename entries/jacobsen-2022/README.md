# Jacobsen, Nair, Obenhaus, Donato, Slettmoen, Moser & Moser (2022) from dandiset 000230

Tests the findings of [Jacobsen et al. (2022)](https://doi.org/10.1016/j.crmeth.2022.100221) that can
be tested on [DANDI:000230](https://dandiarchive.org/dandiset/000230/0.220506.1516), the version the
paper cites. It holds nine optrode sessions in the MEC of two mice, with only the 12 curated units shown
in Figures 5C, S3 and S4. The histology of the single-cell tracing and the two-photon imaging are not in
it.

| Claim | Outcome |
|---|---|
| Grid, head direction and border cells are found in the MEC recordings | Reproduced (resting on an assumption) |
| Laser-responsive cells (2 to 4 ms latency) include grid cells | Reproduced |
| Rates, latencies and fidelities of the three example cells of Figure 5C | Reproduced (resting on an assumption) |
| One input cell stays stable and responsive over six sessions (Figure S3) | Partially reproduced (resting on an assumption) |
| Non-responsive head direction, border and grid cells (Figure S4) | Partially reproduced (resting on an assumption) |
| Responsive cells with spatial firing at 19 days | Reproduced |
| Input cells detected in the MEC from about 2 weeks | Reproduced |
| Histology of single-cell tracing, controls and population labelling (19 claims) | Blocked: data missing |
| Two-photon imaging (2 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper publishes no code. Cell classes follow Rowland et al. (2018), which the paper cites for its
analysis, with details from the code that paper links. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/jacobsen-2022-01.yaml`](../../attempts/jacobsen-2022-01.yaml).

- `reproduce_jacobsen_2022.ipynb`: the analysis. It takes about three minutes, most of it the shuffles.
- `mec_units.py`: loading the files, latency and fidelity, and the spatial scores and shuffles used to
  classify cells. Other notebooks on this dandiset can import it.
