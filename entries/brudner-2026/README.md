# Brudner, Zhou et al. (2026) from dandiset 001871

Tests the findings of [Brudner, Zhou et al. (2026)](https://doi.org/10.1073/pnas.2608896123) that can
be tested on [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657). It holds the
walking trajectories and turn events of flies navigating a projected smooth plume (83 trials) and a
complex smoke plume (48 trials, in two sets named smoke-1a and smoke-2a), a 1500-frame window of the
complex plume movie, and three freestream plume windows. The smooth plume movie is not in it.

| Claim | Outcome |
|---|---|
| Fig. 5E, gradient predicts turns in the smooth plume, motion in the complex plume | Not reproduced |
| Fig. 5F, cue dominance positive (smooth) and negative (complex) | Partially reproduced, resting on assumptions (file set and turn onset) |
| Fig. S5C, turns of about -34 and +34 degrees | Not reproduced |
| Fig. 2C, motion predicts the centerline side better than the gradient (complex plume) | Partially reproduced, resting on an assumption |
| Fig. 2E, motion weighted above the gradient (complex plume) | Partially reproduced |
| Fig. S1F-G, cue maps robust to sensor spacing and delay | Not reproduced |
| Rightward turning bias with light intensity | Blocked: metadata insufficient |
| 15 claims on the smooth plume, the trained networks and the agents | Blocked: the smooth plume (Dryad) could not be read |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The Fig. 5 outcomes take the smoke-1a files as the paper's complex plume, as the dandiset's description
says, and the SI's definition of turn onset, as the claims file asks. Under these, Fig. 5E fails in
every reading (and no file set or onset gives it in every reading): as stored or pooled the complex motion cue has p 0.046 and 0.090, above the criterion's
0.01, and with per-trajectory z-scoring, where it passes at 160 to 200 degrees (p 0.0046), the smooth
motion cue becomes significant (p 0.0079). Fig. 5F would be reproduced with the files' own turn start
in place of the SI's onset, which a reader has been asked about. The paper's code names other files
(smoke-2a), and its published Fig. 5 tables are matched most closely by the smoke-1a files with the
files' own turn start, and closely by the smoke-1a files with the SI's onset. Fig. S5C is not
reproduced: over the files' turn events, as the claims file reads it, the medians are about 21 degrees.
They match the paper only when the turn is bounded by the 20% crossings of its peak, a bound the paper
does not state, and whether the files' events are the paper's turn bounds has been asked of a reader.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/brudner-2026-01.yaml`](../../attempts/brudner-2026-01.yaml).

- `reproduce_brudner_2026.ipynb`: the analysis. It takes about 15 minutes: streaming the behavior
  files, two passes over the 1 GB complex movie, samples of the three freestream windows, and the Fig. 2
  model fits.
- `plumes.py`: loading the files, the Fig. 5 turn analysis of the paper's code (ported, with the SI's
  readings), and the complex-movie measures of Figs. 2 and S1. Other notebooks on this dandiset can
  import it.
