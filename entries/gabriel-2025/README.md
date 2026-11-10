# Gabriel, Gupta, Sanchez-Fuentes, Zeidler, Wilke & DeNardo (2025) from dandiset 001887

Tests the findings of [Gabriel et al. (2025)](https://doi.org/10.1016/j.cub.2025.01.010) on
[DANDI:001887](https://dandiarchive.org/dandiset/001887/0.260902.1724) and on the paper's Zenodo record
of analyzed datasets ([doi:10.5281/zenodo.13381210](https://doi.org/10.5281/zenodo.13381210)). The
dandiset holds trial tables and behaviour videos for 16 mice and no calcium imaging; its BehaviorDEPOT
labels cover 2 of 30 sessions. The Zenodo record holds the Minian traces, BehaviorDEPOT output and
timestamps of all 30 imaged sessions, so every claim is tested there and counted apart from the dandiset.

| Claim | Outcome |
|---|---|
| The Zenodo sessions are the dandiset's sessions (link) | Partially reproduced (25 of 30) |
| Cell counts (1394, 847, 1031, 967) | Reproduced |
| Platform time and successful trials (Figure 1E, 1F) | Reproduced |
| Freezing and latency (Figure 1G, 1H) | Blocked: methods underspecified (Sidak family) |
| Day 1 encoding categories similar between groups | Not reproduced |
| More mixed-selective cells in shocked mice on day 2 (51% against 25%) | Not reproduced |
| Overall encoding similar; tone cells greatest at baseline | Blocked: methods underspecified |
| Platform-exit and freezing activity on day 2 (Figure 1P, 1Q, S1H) | Reproduced, except 1P partially; 1P and S1H sit near p = 0.05 |
| Excited mixed cells at platform exits on day 1 (Figure 1R) | Partially reproduced (assumed reading) |
| Tone strengthens entry and exit encoding (Figure 2) | Day 1 and exits reproduced; day 2 entries partially or not reproduced |
| Decoding better in shocked mice (Figure 3A) | Reproduced (assumed readings; a change to partially reproduced is proposed, as the pre-shock part does not exceed shuffled-label decoders); peak before the shock not reproduced |
| Feature-encoding cells enhance decoding (Figure 3B) | Not reproduced (assumed readings); 3C blocked |
| Hybrid Rescorla-Wagner model fits best (Figure 4B) | Reproduced (assumed tone windows) |
| Cell registration (Figure 1N, 1O) | Blocked: not runnable (no registration deposited; CellReg is MATLAB) |
| CILDS latent trajectories (Figure 4E to 4L, S3, S4; 13 claims) | Blocked: not runnable (MATLAB) |
| Innate behaviours (Figure S2) | Blocked: not runnable (no jumping or rearing labels); the escape part fails, so not reproduced is proposed |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In six sessions the camera ran near 30 frames/s while the paper's code placed the tones at 25 frames/s,
so its tone windows drift from the real tones; the notebook places them by the camera timestamps and
shows every result on the paper's windows too (the Figure 3B and 3C cell sets for one period reading
only), the mean-activity and Figure 2 results with four shuffle seeds of the ROC, and the Figure 3A
decoders beside decoders trained on shuffled trial outcomes. The attempt record, with the reasons and the differences from
the paper's method, is [`attempts/gabriel-2025-01.yaml`](../../attempts/gabriel-2025-01.yaml).

- `reproduce_gabriel_2025.ipynb`: the analysis. It takes about 41 minutes: 9 to stream about 10 GB
  from Zenodo, 7 for the ROC calls and 25 for the 342 decoders of Figure 3, run in four processes.
- `pma.py`: streaming the dandiset and the Zenodo zip members, the tone windows on both readings, trial
  measures, ROC calls, event-aligned activity, the decoder and the Rescorla-Wagner model. Other notebooks
  on this dataset can import it.
