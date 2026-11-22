# Shamugia et al. (2026) from dandiset 000630, with dandisets 000636 and 000020

Tests the findings of [Shamugia et al. (2026)](https://doi.org/10.21203/rs.3.rs-11136357/v1),
"Ion Channels and Morphology Drive Widespread Resonance in Human Cortical Interneurons", on
[DANDI:000630](https://dandiarchive.org/dandiset/000630/0.230915.2257) (210 human layer 1
interneurons, Chartrand et al. 2023), together with two dandisets of the paper's other sources:
[DANDI:000636](https://dandiarchive.org/dandiset/000636/0.241120.0510) (human acute and
slice-culture interneurons, Lee, Dalley et al. 2023) and
[DANDI:000020](https://dandiarchive.org/dandiset/000020/0.210913.1639) (mouse interneurons,
Gouwens et al. 2020, of which 461 are among the paper's mouse cells; the paper's mouse PV and SST
cells are not in it).

| Claims | Outcomes |
|---|---|
| Labels and cell lists link to the dandisets (3 link claims) | 2 reproduced, 1 partially (461 of 628 mouse cells public) |
| Sample size | Not reproduced (440 human acute cells from 76 donors, against 542 from 170) |
| Human against mouse resonance, sag and input resistance (12 claims) | 4 reproduced, 6 partially reproduced, 2 not reproduced |
| Sag ratio and input resistance against resonance (4 claims) | 1 reproduced, 1 partially reproduced, 2 not reproduced |
| Slice culture against acute (4 claims) | 3 partially reproduced, 1 not reproduced |
| Region and disease (1 claim) | Reproduced |
| Ion channel gene expression (3 claims) | 1 reproduced, 2 not reproduced |
| Mouse SST, depth, ZD7288, Allen Brain Map expression and model findings (19 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's analysis code is not public, so impedance, sag ratio and input resistance are
computed as the IPFX package computes them, with the alternatives the claims file names shown
beside them; several outcomes rest on the choice of the lowest chirp frequency (0.4 Hz here).
Labels come from the analysis repositories of Chartrand et al. (2023) and Lee, Dalley et al.
(2023) and from the Allen Institute's mouse metadata, each at a pinned commit, and from the
paper's Tables S1 and S2b; the expression of the human cells comes from the same two analysis
repositories. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/mansvelder-2026-01.yaml`](../../attempts/mansvelder-2026-01.yaml).

- `reproduce_mansvelder_2026.ipynb`: the analysis. It takes about twenty minutes, most of it
  streaming the files.
- `resonance.py`: streaming the files, the chirp impedance profile, resonance measures, sag ratio,
  input resistance, the labels, and mixed models with Satterthwaite tests. Other notebooks on
  these dandisets can import it.
