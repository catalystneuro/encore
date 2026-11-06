# Qi, Parot, Wang, Pomeroy, Lavis & Cohen (2026) from dandiset 001960

Tests the findings of [Qi et al. (2026)](https://doi.org/10.64898/2026.10.05.756595) on
[DANDI:001960](https://dandiarchive.org/dandiset/001960/0.261013.2016), which holds, for two
NDNF-Cre::NPY-GFP mice, a spontaneous session, an intrinsic-excitability session and a
connectivity-mapping session of about 320 layer 1 interneurons imaged at 787 Hz, and a raw-movie
excerpt. Of the 56 claims, 45 are tested and 11 blocked.

| Claims | Outcome |
|---|---|
| Intrinsic properties and their three clusters (Figure 2, four claims) | Reproduced |
| Synaptic and gap-junction connection counts, IPSP and spikelet amplitudes, Hadamard rates, distance decay, conduction speed (Figure 3) | Reproduced (six claims) |
| Presynaptic identity sets IPSP amplitude, postsynaptic sets decay, mixed-model variances (Figure 3J to O) | Reproduced (three claims) |
| Connection structure with distance; log-normal amplitudes | Partially reproduced |
| Population interaction kernel; gap-junction strength without identity effect | Not reproduced |
| Spontaneous correlations, dimensionality, oscillations, voltage-to-spike curves, private depolarizations (Figure 4, six claims) | Reproduced |
| Spike-synchrony length constants and widths | Partially reproduced |
| SNR decay over an hour | Reproduced |
| Single-spike SNR and detection errors | Not reproduced |
| Intrinsic properties shape spontaneous firing (Figure 5A to C, Supplementary Figure 22, four claims) | Reproduced |
| Inhibition in spontaneous voltage | Reproduced |
| Inhibition in spontaneous rate; gap-junction synchrony | Partially reproduced |
| NPY subtypes: counts, intrinsic differences, classifier, connectivity, UMAP groups, whisking and state effects (Figure 6, eleven claims) | Reproduced |
| NPY subtypes do not differ in gap-junction connectivity | Not reproduced |
| Figure 1 tool experiments (six claims) | Blocked: data missing |
| Scatter control from the raw movie | Blocked: too large |
| Detection limits, lasso correction, traveling waves, inhibition-gap balance | Blocked: methods underspecified |

Three reproduced outcomes rest on an assumption about a method the paper leaves open
(hadamard-stimulation-rates, voltage-to-spike-sigmoid, npy-oscillation-peak-rates).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Unit ids do not refer to the same cells across the sessions of a mouse, and nothing in the files
links them; every claim is tested within one session. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001960-qi-2026-01.yaml`](../../attempts/001960-qi-2026-01.yaml).

- `qi2026_excitability_connectivity.ipynb`: the data check, Figures 2 and 3, Figure 5D to G and the
  Figure 6 excitability and connectivity claims (about 16 minutes).
- `qi2026_spontaneous.ipynb`: the spontaneous sessions, for the SNR claims, Figure 4 and the Figure 6
  behaviour claims (about 11 minutes; it holds one session's voltage, 3 GB, in memory at a time).
- `qi2026_excitability_spontaneous.ipynb`: Figure 5A to C and Supplementary Figure 22 (about 10 minutes).
- `l1opto.py`: streaming the files, the masks and measures of the paper's code, and the crossed
  random-effects model. Other notebooks on this dandiset can import it.
