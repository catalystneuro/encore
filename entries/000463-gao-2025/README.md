# Gao, Ramachandran, Yu & He (2025) from dandiset 000463

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) on
transcranial focused ultrasound of rat S1. [DANDI:000463](https://dandiarchive.org/dandiset/000463/0.250829.1248)
cites the paper but holds only broadband recordings of one S1 probe from four other rats, with no
units, trial times or electrode locations. The paper names its own deposit,
[DANDI:000946](https://dandiarchive.org/dandiset/000946/0.250829.1249), and the claims are tested
there. Its units carry no RSU or FSU type (every `celltype_label` is 0) and no waveforms, so only the
claims on auditory cortex units, which the paper does not type, can be tested.

| Claim | Outcome |
|---|---|
| AC unit counts, 453 over the PRFs (Figure 11) | Not reproduced |
| AC responses to five PRFs (Figure 11) | Partially reproduced (resting on an assumption) |
| S1 and POm responses and correlations by cell type (Figures 4, 6 to 10, 11C and 11D; 31 claims) and the Discussion's synthesis | Blocked: metadata insufficient |
| Sham and CG1 control sessions (Figure 5), hydrophone scans (Figure 1C) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000463-gao-2025-01.yaml`](../../attempts/000463-gao-2025-01.yaml).
