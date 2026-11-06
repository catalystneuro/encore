# Nakagawa et al. (2026) from dandiset 001968

Tests the findings of [Nakagawa et al. (2026)](https://doi.org/10.1038/s41593-026-02260-w) that can
be tested on [DANDI:001968](https://dandiarchive.org/dandiset/001968/0.260914.1316). The dandiset
holds sorted lateral entorhinal cortex units of 27 tetrode mice and 41 dopamine-fiber photometry
sessions of 10 mice. The unit files hold spike times only, with no trial or event times, so the
cue responses, population trajectories and decoding of Figure 2, Extended Data Figs. 5 to 9 and
Figure 6 cannot be tested. Histology, optogenetics and the behaviour of most mice are not in it.

| Claim | Outcome |
|---|---|
| The tetrode mice can be linked to the paper's animal lists | Partially reproduced |
| The photometry mice can be linked to the paper's animal lists | Partially reproduced |
| 479 and 846 units from young WT and APP-KI mice | Partially reproduced |
| Higher firing rates in young APP-KI principal cells and interneurons | Reproduced |
| Young APP-KI mice perform worse on novel associations (10 of 27 mice) | Not reproduced |
| Fewer correct sessions in young APP-KI mice (10 of 27 mice) | Partially reproduced |
| WT dopamine signals to Odor-A, -1 and -2 at T1 | Partially reproduced |
| Delayed Odor-1 dopamine signals in APP-KI mice | Not reproduced |
| Lower Odor-1 dopamine signal at T1 in APP-KI mice, all and correct sessions | Not reproduced |
| No dopamine difference in error sessions | Reproduced |
| The T1 decrease is specific to Odor-1 | Reproduced |
| Dopamine emergence correlates with learning | Blocked: methods underspecified |
| Spike widths and types | Blocked: data missing |
| Cue responses, PCA, similarity and decoding (13 claims) | Blocked: data missing |
| Histology (4 claims) | Blocked: data missing |
| Behaviour of old, prelearning, optogenetic and L-DOPA mice (13 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

No file states genotype, age group or treatment; these come from the paper's Supplementary Table 2
and Supplementary Fig. 2a. The photometry files state no sampling rate or cue time; the notebook
reads them as 1 kHz with the cue at 1 s from their z-scoring, an assumption. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001968-nakagawa-2026-01.yaml`](../../attempts/001968-nakagawa-2026-01.yaml).

- `reproduce_nakagawa_2026.ipynb`: the analysis. It takes about four minutes, most of it reading
  the 3855 files.
- `lecda.py`: loading the unit and photometry files, the paper's animal groups, and the photometry,
  behaviour and rate measures. Other notebooks on this dandiset can import it.
