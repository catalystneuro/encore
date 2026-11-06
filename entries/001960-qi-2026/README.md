# Qi, Parot, Wang, Pomeroy, Lavis & Cohen (2026) from dandiset 001960

Tests the findings of [Qi et al. (2026)](https://doi.org/10.64898/2026.10.05.756595) on
[DANDI:001960](https://dandiarchive.org/dandiset/001960/0.261013.2016), which holds, for two
NDNF-Cre::NPY-GFP mice, a spontaneous session, an intrinsic-excitability session and a
connectivity-mapping session of about 320 layer 1 interneurons imaged at 787 Hz, and a raw-movie
excerpt. Of the 56 claims, 46 are tested and 10 blocked.

| Claims | Outcome |
|---|---|
| Intrinsic properties and their three clusters, two-mouse comparison (Figure 2, four claims) | Reproduced |
| Synaptic and gap-junction connection counts, Hadamard rates, distance decay, conduction speed, log-normal amplitudes (Figure 3, six claims) | Reproduced |
| IPSP median and size of correlated fluctuations | Partially reproduced |
| Scatter control from the raw movie (first 40,000 frames) | Reproduced |
| Presynaptic identity sets IPSP amplitude, postsynaptic sets decay, mixed-model variances (Figure 3J to O) | Reproduced (three claims) |
| Connection structure with distance | Partially reproduced |
| Population interaction kernel; gap-junction strength without identity effect; lasso off-target correction | Not reproduced |
| Spontaneous correlations, dimensionality, oscillations, private depolarizations (Figure 4, five claims) | Reproduced |
| Traveling waves | Not reproduced |
| Spike-synchrony length constants and widths | Partially reproduced |
| SNR decay over an hour | Reproduced |
| Single-spike SNR and detection errors | Not reproduced |
| Intrinsic properties shape spontaneous firing (Figure 5A to C, Supplementary Figure 22, four claims) | Reproduced |
| Inhibition in spontaneous voltage | Reproduced |
| Inhibition in spontaneous rate; gap-junction synchrony | Partially reproduced |
| NPY subtypes: counts, intrinsic differences, classifier, connectivity, UMAP groups, whisking and state effects (Figure 6, ten claims) | Reproduced |
| NPY subtypes do not differ in gap-junction connectivity | Not reproduced |
| Figure 1 tool experiments, high-magnification footprints (six claims) | Blocked: data missing |
| Detection limits | Blocked: too large |
| Voltage-to-spike curves; inhibition-gap balance; rates at oscillation peaks | Blocked: methods underspecified |

Of the 56 claims, 46 are tested (35 reproduced, 5 partially reproduced, 6 not reproduced) and 10
blocked. Five outcomes rest on an assumption about a method the paper leaves open
(two-mice-intrinsic-distributions, hadamard-stimulation-rates, npy-ipsp-duration,
lasso-off-target-correction, traveling-waves). Voltage-to-spike-sigmoid is blocked (methods
underspecified) after the third verification round, since the readings its criterion names give
different outcomes: 52% of cells pass with V at the spike frame, 42% and 24% with V in the 10 ms
before.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Unit ids do not refer to the same cells across the sessions of a mouse, and nothing in the files
links them; every claim is tested within one session. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001960-qi-2026-01.yaml`](../../attempts/001960-qi-2026-01.yaml).

- `qi2026_excitability_connectivity.ipynb`: the data check, Figures 2 and 3, Figure 5D to G and the
  Figure 6 excitability and connectivity claims, the lasso correction and the scatter control (about 30 to 40 minutes).
- `qi2026_spontaneous.ipynb`: the spontaneous sessions, for the SNR claims, Figure 4 and the Figure 6
  behaviour claims and the wave analysis (about 20 to 30 minutes; it holds one session's voltage, 3 GB, in memory at a time).
- `qi2026_excitability_spontaneous.ipynb`: Figure 5A to C and Supplementary Figure 22 (about 10 to 15 minutes).
- `l1opto.py`: streaming the files, the masks and measures of the paper's code, and the crossed
  random-effects model. Other notebooks on this dandiset can import it.
