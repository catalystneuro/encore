# Padilla-Coreano, Batra, Patarino et al. (2022) from dandiset 001749

Tests the findings of [Padilla-Coreano et al. (2022)](https://doi.org/10.1038/s41586-022-04507-5)
that can be tested on [DANDI:001749](https://dandiarchive.org/dandiset/001749/0.260311.1727). The
dandiset holds the wireless mPFC recordings of 20 mice in 53 reward competitions, with the tone
schedule, port entries, AlphaTracker poses and the nine hand-scored behaviour labels of Figure 1f.

| Claim | Outcome |
|---|---|
| Rank 1 mice win the highest percentage of competitions (ED Fig. 5b) | Reproduced |
| Dominants and subordinates obtain similar numbers of rewards, and body weight difference correlates with rewards won (ED Fig. 5c) | Partially reproduced (rewards part; no body weights in the files) |
| Subordinates take longer to pick up the reward in win trials (ED Fig. 5d) | Not reproduced (rests on an assumption about trial alignment) |
| Port occupancy during the tone does not differ by rank (ED Fig. 5e) | Reproduced |
| Dominants are more successful at displacing subordinates (ED Fig. 5f) | Reproduced |
| Time displaced does not differ by rank (ED Fig. 5g) | Reproduced |
| A 6-state HMM-GLM decodes behaviour from multi-unit activity better than static models (Figure 1i) | Reproduced, on 17 of the 34 labelled files |
| Held-out likelihood plateaus at 6 states (ED Fig. 5j) | Not reproduced (6 states on the paper's own input) |
| The HMM-GLM generalizes across relative rank (ED Fig. 5k) | Reproduced, with threshold crossings in either direction (an assumption; negative crossings fail one combination) |
| Single-unit findings of Figures 2 and 3 and ED Figures 6 to 9 (22 claims), distance to port (ED Fig. 7b) | Blocked: metadata insufficient |
| Unimplanted cohort, AlphaTracker evaluation, alone sessions, ex vivo, phototagging and optogenetics (14 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The files do not mark which of their 5,879 Klusta clusters are the paper's 998 curated cells, so
no single-unit finding can be tested. The stored spike times are two thirds of their time in the
recording, and the offset between the neural recording and the behaviour clock, which the
description places in a `video_gap` variable, is in no file. The notebook shows both from the data,
estimates the offset from the units' responses to port entries, and checks it against the paper's
own processed HMM-GLM input. The HMM-GLM claims use the 17 labelled files where the offset can be
placed. With each file's tones placed by its best shift, the latency difference of ED Fig. 5d is
significant only when files whose labels and port entries disagree are kept; on the files aligned
without a shift it is significant at most cut-offs, so that outcome rests on the choice of reading. The attempt record, with the reasons and the differences from the
paper's method, is
[`attempts/padilla-coreano-2022-01.yaml`](../../attempts/padilla-coreano-2022-01.yaml).

- `reproduce_padilla_coreano_2022.ipynb`: the data check, the behavioural claims and the HMM-GLM
  claims. It takes about fifty minutes: streaming the trial windows of the raw recordings and the
  clock checks, and the HMM-GLM fits.
- `competition.py`: loading the files, the trial outcomes, latencies and pushing success from the
  labels, the clock checks and the multi-unit counts. Other notebooks on this dandiset can import it.
- `hmmglm.py`: the paper's HMM-GLM (github.com/Tyelab/HMMGLM at commit 3fc3567), ported from
  MATLAB, and the static decoders of Methods 17.
