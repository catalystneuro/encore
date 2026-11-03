# Tian et al. (2025), Figure 4, from dandiset 001559

Tests the findings of [Tian et al. (2025)](https://doi.org/10.1021/acssensors.5c01093) that can be
tested on [DANDI:001559](https://dandiarchive.org/dandiset/001559/0.250902.2058), which holds the
raw data of Figure 4 for one mouse: two-photon stacks of eBRIC expression, laser speckle movies,
and PMT recordings of bioluminescence during whisker pad stimulation. The other figures are not in
it.

| Claim | Outcome |
|---|---|
| Two-photon images show labelled neuronal somata and processes (Figure 4B) | Reproduced |
| Speckle imaging shows the expressing region responds to stimulation (Figure 4C) | Blocked: metadata insufficient |
| DTZ infusion gives a steady baseline (Figure 4D) | Partially reproduced (assumed) |
| Clear increases at both currents and both electrodes (Figure 4D) | Blocked: methods underspecified |
| 4 mA responses detectable in single trials (Figure 4D) | Blocked: methods underspecified (depends on the claim above) |
| The two electrodes differ in response timing (Figure 4D) | Blocked: methods underspecified (depends on the claim above) |
| Figures 1, 2, 3, 5, S2, S3 and Table S1 (fifteen claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no stimulus table. The stimulus times come from a marker recorded as image
channel 1 of the PMT acquisitions, and nothing records which electrode or current each session
used, so the four stimulated sessions are taken as the four conditions and the two with the larger
responses as the 4 mA ones. The speckle movies carry no stimulus times. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/001559-tian-2025-01.yaml`](../../attempts/001559-tian-2025-01.yaml).

- `reproduce_tian_2025.ipynb`: the analysis. It takes about eight minutes, most of it streaming
  the files.
- `ebric.py`: loading the files, the stimulus marker, trial responses, averages, peak and rise
  times, and image projections. Other notebooks on this dandiset can import it.
