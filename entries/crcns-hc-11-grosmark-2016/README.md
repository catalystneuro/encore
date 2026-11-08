# Grosmark & Buzsáki (2016) from CRCNS hc-11

Tests the findings of [Grosmark and Buzsáki (2016)](https://doi.org/10.1126/science.aad1935) on
[CRCNS hc-11](https://doi.org/10.6080/K0862DC5), which holds eight CA1 recordings in four rats, each a
PRE sleep, a novel maze and a POST sleep. The analysis reads the sessInfo files (spike times, cell
types, position and state epochs) and, for Figure S11 only, the cluster labels and spike features of the
per-session archives; the LFP and the waveforms are not read.

| Claim | Outcome |
|---|---|
| Place cells, 491 of 562 pyramidal cells by running direction | Partially reproduced |
| Sequence scores above chance, MAZE > POST > PRE (Figure 1C) | Reproduced |
| Observed above shuffled weighted correlations (Figure S5B) | Reproduced |
| Ripple-event duration unchanged from PRE to POST | Reproduced |
| More place cells participate in POST events | Reproduced |
| POST PCC above PRE PCC (Figure S9B medians) | Partially reproduced |
| 216 strongly contributing cells (97 PRE, 190 POST, 71 both) | Partially reproduced |
| 73% of PRE contributors also contribute in POST | Reproduced |
| 105 rigid and 105 plastic cells | Partially reproduced |
| Shuffling or excluding the top 10 to 20% dPCC cells abolishes replay (Figure 2D, S12) | Reproduced (2) |
| Removing plastic cells abolishes replay (Figure 2E) | Partially reproduced |
| Rigid and plastic fields similarly placed along the track | Reproduced |
| Plastic cells more place specific, fewer fields (Figure 3A) | Partially reproduced |
| Plastic cells' specificity rises over laps (Figure 3B) | Not reproduced |
| Plastic cells' out-of-field rate falls over laps (Figure S13) | Reproduced |
| Rigid cells fire faster offline (Figure 4A) | Not reproduced |
| Plastic cells' ripple gain and bursting (Figure S14, two claims) | Not reproduced |
| Ripple-triggered firing and coactivity rise in plastic cells (Figure S16A, B) | Reproduced |
| Low and high rate split, 0.39 and 1.12 Hz | Reproduced |
| Low-rate cells code space better (Figure S16C) | Not reproduced |
| Coactivity by firing rate (Figure 4B, C) | Reproduced (proposed: partially reproduced; the verifier would give not reproduced) |
| Slow-firing cells carry the replay increase (Figure 4D) | Not reproduced |
| High-gain cells carry the replay increase (Figure 4E) | Partially reproduced |
| More ripple events in POST (Figure S16D, E) | Not reproduced |
| Coactivity preservation, all pairs (Figure S17A, C) | Partially reproduced |
| Coactivity preservation, rigid and plastic pairs (Figure S17D) | Not reproduced |
| Temporal bias preservation (Figure S18) | Not reproduced |
| Per-cell PRE against POST PCC, 2.2% and 21.4% (Figure S19C) | Not reproduced |
| Rigid and plastic cluster quality similar (Figure S11) | Reproduced (quality and stability; waveforms not compared) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Five changes of outcome were proposed after verification round 2. The third round agreed with four,
which are applied (Figures S16C, 4D, 2E and S11). It did not agree with the change for Figure 4B and C,
which stays at its verified outcome with the proposal recorded.

Ripple events here lack the paper's condition that each holds an LFP-detected ripple, as the LFP is
only in tar.gz archives of 70 GB in all. Many outcomes rest on choices the paper leaves open (how the
two running directions enter the replay scores, which test marks a strongly contributing cell, how the
PRE and POST epochs are yoked), stated as assumptions in the record,
[`attempts/crcns-hc-11-grosmark-2016-01.yaml`](../../attempts/crcns-hc-11-grosmark-2016-01.yaml).

- `reproduce_grosmark_2016.ipynb`: the analysis. It took 38 to 76 minutes on the runners used, most of it the
  1,000-shuffle replay and per cell contribution analyses; the Figure S11 archives (11.6 GB) stream in a
  background thread.
- `hc11.py`: streaming the sessInfo files, state and yoking intervals, place fields, ripple events,
  Bayesian replay scores, per cell contributions and cluster quality. Other notebooks on this data set can import it.
