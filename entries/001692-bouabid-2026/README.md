# Bouabid, Vu et al. (2026) from dandiset 001692

Tests the findings of [Bouabid, Vu et al. (2026)](https://doi.org/10.64898/2026.01.20.700614) that
can be tested on [DANDI:001692](https://dandiarchive.org/dandiset/001692/0.260303.1724), which holds
multi-fiber photometry of dopamine (GRAB-rDA3m) and acetylcholine (GRAB-ACh3.0) across the striatum
of 17 head-fixed mice: spontaneous and reward sessions (5 mice), Pavlovian sessions (3), control
mice with non-functional sensors (3) and midbrain DA stimulation (6). The ex vivo slice statistics
of Figure 8 are tested on the paper's source data on Zenodo.

| Claim | Outcome |
|---|---|
| Dominant DA-ACh correlations: 132 negative (DA leading), 42 positive (ACh leading) of 174 | Reproduced |
| A negative correlation hotspot in the anterior dorsolateral striatum | Partially reproduced |
| More negative inside the hotspot; positive correlations posterior; consistent across mice | Reproduced |
| Control mice show only weak correlations and no hotspot | Not reproduced |
| Paired transients: DA leads opposite-sign pairs, ACh same-sign pairs | Reproduced |
| Paired-transient magnitude correlations (counts; stronger inside the hotspot) | Partially reproduced |
| Pairing frequency and transient rates highest in the hotspot | Reproduced |
| Reward: DA peak to ACh correlations (counts and latencies) | Partially reproduced |
| Reward: more negative inside the hotspot; reward hotspot overlaps | Reproduced |
| Pavlovian cue: ACh peak, DA peak, ACh dip at 49 of 75 sites | Not reproduced (58 of 75) |
| Pavlovian cue correlations (counts and latencies) | Partially reproduced |
| Extinction DA dip to ACh correlations; cue and extinction in-out tests | Reproduced |
| Locomotion initiation: counts of DA and ACh responses | Partially reproduced |
| Locomotion: latency order; initiation and invigoration correlations in the hotspot | Reproduced |
| Locomotion: topography of DA dips, DA peaks and ACh dips | Not reproduced |
| Stimulation: DA release at 179 of 180 sites; ACh dips larger inside the cohort hotspot | Reproduced |
| Stimulation: ACh dips at 116 of 180 sites; cohort hotspot replication | Partially reproduced |
| Figure 8 slice ANOVAs (Zenodo source data): quinpirole, D2 block / cocaine / FCV | Reproduced / partially reproduced / blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The photometry series state a sampling rate of 9 Hz; the timestamps, the Methods and the code give
18 Hz, which is used. The files do not say which experiment or Pavlovian phase a session belongs to;
the notebook infers this from subject names, indicators and events. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/001692-bouabid-2026-01.yaml`](../../attempts/001692-bouabid-2026-01.yaml).

- `reproduce_bouabid_2026.ipynb`: the analysis. It takes about ten minutes, a third of it streaming.
- `daach.py`: loading the files, lagged correlations, transient detection and pairing, triggered
  averages with bootstrap significance, the paper's trial-by-trial event correlation, locomotion
  events and the invigoration GLM, and a simplified version of the paper's hotspot procedure.
  Other notebooks on this dandiset can import it.
