# Padilla-Coreano, Batra, Patarino et al. (2022) from dandiset 001749

Tests the findings of [Padilla-Coreano et al. (2022)](https://doi.org/10.1038/s41586-022-04507-5)
that can be tested on [DANDI:001749](https://dandiarchive.org/dandiset/001749/0.260311.1727). The
dandiset holds the wireless mPFC recordings of 20 mice in 53 reward competitions, with the tone
schedule, port entries, AlphaTracker poses and the nine hand-scored behaviour labels of Figure 1f.

| Claim | Outcome |
|---|---|
| Rank 1 mice win the highest percentage of competitions (ED Fig. 5b) | Reproduced |
| Dominants and subordinates obtain similar numbers of rewards (ED Fig. 5c; the body weight part is not testable) | Reproduced |
| Subordinates take longer to pick up the reward in win trials (ED Fig. 5d) | Reproduced |
| Port occupancy during the tone does not differ by rank (ED Fig. 5e) | Reproduced |
| Dominants are more successful at displacing subordinates (ED Fig. 5f) | Reproduced |
| Time displaced does not differ by rank (ED Fig. 5g) | Reproduced |
| HMM-GLM decoding of behaviour (Figure 1i, ED Fig. 5j-k; three claims) | Blocked: metadata insufficient |
| Single-unit findings of Figures 2 and 3 and ED Figures 6 to 9 (21 claims), distance to port (ED Fig. 7b) | Blocked: metadata insufficient |
| Unimplanted cohort, AlphaTracker evaluation, alone sessions, ex vivo, phototagging and optogenetics (14 claims) | Blocked: data missing |

The files do not mark which of their 5,879 Klusta clusters are the paper's 998 curated cells, so
no single-unit finding can be tested. The stored spike times are two thirds of their time in the
recording, and the offset between the neural recording and the behaviour clock, which the
description places in a `video_gap` variable, is in no file. The notebook shows both from the data.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001749-padilla-coreano-2022-01.yaml`](../../attempts/001749-padilla-coreano-2022-01.yaml).

- `reproduce_padilla_coreano_2022.ipynb`: the data check and the behavioural claims. It takes
  about eight minutes, most of it streaming parts of the raw recordings for the clock checks.
- `competition.py`: loading the files, the trial outcomes, latencies and pushing success from the
  labels, and the clock checks. Other notebooks on this dandiset can import it.
