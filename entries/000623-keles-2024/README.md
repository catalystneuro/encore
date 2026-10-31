# Keles et al. (2024) from dandiset 000623

Tests the findings of the data descriptor of [Keles et al. (2024)](https://doi.org/10.1038/s41597-024-03029-1)
on [DANDI:000623](https://dandiarchive.org/dandiset/000623/0.240130.2108), the version the paper
cites. The dandiset holds the 29 EMU runs of 16 patients: spike-sorted units, microwire LFP,
macro iEEG, eye tracking and the recognition test. The fMRI data are on OpenNeuro (ds004798).

| Claim | Outcome |
|---|---|
| 29 runs from 16 participants, as Table 1 | Reproduced |
| Demographics of the 20 participants (Table 1) | Reproduced |
| 1450 units, per-area counts | Reproduced |
| Units per wire, firing rate, ISI, SNR, projection and isolation distances | Reproduced |
| Missing gaze for P53CS; gaze similarity and missing gaze | Reproduced |
| Recognition AUC; run 1 against run 2; confidence and accuracy | Reproduced |
| 1266 units in the memory analysis | Reproduced |
| Memory-selective cells, significant and not significant areas | Reproduced |
| Memory-selective LFP and iEEG channels | Reproduced |
| Memory selectivity differs by modality | Reproduced |
| Scene-cut labels (link) and event-selective cells, LFP and iEEG channels | Reproduced |
| Example cells and channels of Figs. 6 and 7 | Reproduced |
| Contents of the NWB files | Reproduced |
| In-scanner questions (code repository's copy of the answers) | Reproduced |
| fMRI motion, tSNR and inter-subject correlation | Blocked: not runnable |

The LFP series store a starting time near 0 s, although their samples begin 10 s before the
movie; the paper's code corrects for this, and the notebook shows the correction is needed.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000623-keles-2024-01.yaml`](../../attempts/000623-keles-2024-01.yaml).

- `reproduce_keles_2024.ipynb`: cohort, unit quality metrics, gaze, behaviour and single-neuron
  selectivity. About 4 minutes.
- `hfb_keles_2024.ipynb`: high-frequency broadband power of every LFP and iEEG channel, and the
  claims that use it. About 25 minutes, most of it streaming and filtering the LFP.
- `bmovie.py`: loading, the paper's measures and tests, and the HFB pipeline, ported from the
  paper's code. Other notebooks on this dandiset can import it.
