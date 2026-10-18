# Randi, Sharma, Dvali & Leifer (2023) from dandiset 001075

Tests the findings of [Randi et al. (2023)](https://doi.org/10.1038/s41586-023-06683-4) that can be
tested on [DANDI:001075](https://dandiarchive.org/dandiset/001075/0.240930.1859), which holds the
113 wild-type-background recordings of whole-brain calcium imaging during single-neuron optogenetic
stimulation, 110 of them with extracted traces. The unc-31 recordings, the spontaneous recordings
of Fig. 6 and the unstimulated control recordings behind every q value are not in it.

| Claim | Outcome |
|---|---|
| 113 WT animals, up to 40 min, a stimulation every 30 s | Partially reproduced |
| 23,433 pairs measured, from 186 of 188 head neurons, up to 59 observations | Partially reproduced |
| AVJR stimulation evokes AVDR activity (Fig. 1e) | Reproduced |
| AVER stimulation evokes AVAR activity (Fig. 1f) | Reproduced |
| SAADL stimulation inhibits OLLR (Fig. 1g) | Reproduced |
| Most neighbours of the target do not respond (Extended Data Fig. 2i,j) | Reproduced |
| Per-pair counts and means agree with the paper's Source Data | Partially reproduced |
| Recordings and stimulated neurons link to the paper's OSF export | Partially reproduced |
| 11% of q < 0.05 connections are inhibitory | Not reproduced |
| q-value results (Fig. 2c, 2e-g), unc-31 comparisons, extrasynaptic screen | Blocked: data missing |
| Anatomy-model predictions (Fig. 3) | Blocked: data missing |
| Kernel stereotypy (Extended Data Fig. 6) | Blocked: not runnable |
| URX, ADL and AWB respond to RID stimulation in WT (Fig. 4) | Partially reproduced |
| These RID responses are reduced in unc-31 (Fig. 4, OSF export) | Reproduced |
| Spontaneous activity predictions (Fig. 6) | Blocked: not runnable (needs the kernels) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not say which neuron was stimulated for about half of the stimulations; they give a
target position, and the nearest ROI is used. The q values come from the paper's Source Data for
one claim, the paper's OSF export is used to check the recordings and the stimulated neurons, and
its unc-31 export supplies the unc-31 recordings for one claim.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001075-randi-2023-01.yaml`](../../attempts/001075-randi-2023-01.yaml).

- `reproduce_randi_2023.ipynb`: the analysis. It takes about twelve minutes, most of it streaming
  the segmentation files and processing the traces in four worker processes.
- `sigprop.py`: loading the segmentation files, the pre-processing of the Methods, the paper's
  response classifier, the identification of the stimulated ROI and the per-pair tables. Other
  notebooks on this dandiset can import it.
