# Shamugia et al. (2026) from dandiset 000630

Tests the findings of [Shamugia et al. (2026)](https://doi.org/10.21203/rs.3.rs-11136357/v1),
"Ion Channels and Morphology Drive Widespread Resonance in Human Cortical Interneurons", that can
be tested on [DANDI:000630](https://dandiarchive.org/dandiset/000630/0.230915.2257). The dandiset
holds the electrophysiology of 210 human layer 1 interneurons (Chartrand et al. 2023), a part of
the paper's human acute sample; 85 of them have a usable chirp recording.

| Claim | Outcome |
|---|---|
| Labels of the Chartrand et al. repository match the dandiset's cells (link) | Reproduced |
| Sample size (542 human acute cells from 170 donors) | Not reproduced: the dandiset holds 210 from 53 |
| Sag ratio and input resistance predict resonance frequency in human cells | Partially reproduced (LAMP5 and VIP only) |
| Sag ratio predicts resonance strength, input resistance relates negatively | Not reproduced |
| Resonance does not differ by region or disease | Reproduced |
| Mouse, cultured, ZD7288, depth, gene expression and model findings (40 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's analysis code is not public, so impedance, sag ratio and input resistance are
computed as the IPFX package computes them, with the alternatives the claims file names shown
beside them. Subclass and donor labels come from the analysis repository of Chartrand et al.
(2023) at a pinned commit; region and disease come from the paper's Table S1. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/mansvelder-2026-01.yaml`](../../attempts/mansvelder-2026-01.yaml).

- `reproduce_mansvelder_2026.ipynb`: the analysis. It takes about five minutes, most of it
  streaming the files.
- `resonance.py`: streaming the files, the chirp impedance profile, resonance measures, sag ratio
  and input resistance. Other notebooks on this dandiset can import it.
