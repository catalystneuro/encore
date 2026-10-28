# Gillon, Lecoq et al. (2023) from dandisets 000336 and 000037

Tests the findings of the data descriptor by [Gillon, Lecoq et al. (2023)](https://doi.org/10.1038/s41597-023-02214-y),
which [DANDI:000336](https://dandiarchive.org/dandiset/000336/0.260325.1802) lists as a related resource.
DANDI:000336 holds a different OpenScope project (Dendritic Coupling) and none of the paper's sessions.
The paper's data are in [DANDI:000037](https://dandiarchive.org/dandiset/000037/0.230426.0054), version
0.230426.0054, where the other claims are tested: 50 two-photon sessions of 13 mice, imaged at the somata
and distal apical dendrites of L2/3 and L5 pyramidal cells.

| Claim | Outcome |
|---|---|
| DANDI:000336 holds the paper's sessions | Not reproduced |
| 13 mice in four groups, 7 male and 6 female (Table 1) | Reproduced |
| 50 sessions, 2 mice with failed sessions, 33 analysed files (Table 2) | Reproduced |
| Three 70-minute sessions within 3 to 6 days | Reproduced |
| Imaging depths, 30 Hz, 512 x 512 pixels | Partially reproduced |
| 15 to 224 somatic and 159 to 1636 dendritic ROIs per session | Reproduced |
| Tracked ROIs per plane (254, 261, 516, 129), 32 to 75% of the maximum | Reproduced |
| Example matches of Fig. 8 (136 and 47) | Reproduced |
| Matching varies with session order far more for dendrites than somata | Reproduced (resting on an assumption) |
| Stimulus durations (34 and 17 min, 30 s grey) | Reproduced |
| Inconsistent stimuli about 7% and 5%, about 30 blocks | Reproduced |
| Responses differ between consistent and inconsistent stimuli (Fig. 5) | Reproduced |
| Running and pupil recorded in every analysed session (Fig. 6) | Reproduced |
| SNR above 1 and stable over days (Fig. 7a) | Reproduced |
| Signal stable over days (Fig. 7b) | Reproduced |
| Dendritic and somatic correlations similar (Fig. 7c) | Blocked: methods underspecified |
| About 0.01% of L2/3 dendritic pairs correlate above 0.8 | Not reproduced |
| Transients at stimulus onsets and offsets (Fig. 9) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000336-gillon-2023-01.yaml`](../../attempts/000336-gillon-2023-01.yaml).

- `reproduce_gillon_2023.ipynb`: all claims but one. It takes about ten minutes, most of it streaming the
  ROI traces of the 33 analysed sessions.
- `roi_matching_orderings.ipynb`: reruns ROI matching with the Allen Institute's public n-way matching
  package over the six session orderings of each mouse. It takes about nineteen minutes.
- `credassign.py`: listing and streaming the files, the session table of the paper's code, and the
  measures of the paper's code (SNR, correlations, onset and offset responses), with the matching
  driver. Other notebooks on DANDI:000037 can import it.
