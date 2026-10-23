# Berg, Sorensen, Ting, Miller et al. (2020) from dandiset 000023

Tests the findings of [Berg et al. (2020)](https://doi.org/10.1101/2020.03.31.018820) that can be
tested on [DANDI:000023](https://dandiarchive.org/dandiset/000023/0.210914.1900), which holds the
whole-cell current-clamp recordings of 318 human L2/3 glutamatergic neurons from 56 neurosurgical
donors. The files carry no t-type, depth or specimen ID: each recording is linked to the paper's
per-cell table, in its code at
[AllenInstitute/patchseq_human_L23@3daf9f0](https://github.com/AllenInstitute/patchseq_human_L23/tree/3daf9f0803ea0c220a040ea523f23af5f93c56ac),
through the file's session id. The link is confirmed by the electrophysiological features, which
equal the code's in most cells, and for the 35 cells without features in the code it is supported by
the sample dates and tube order of the code's table.

| Claim | Outcome |
|---|---|
| The recordings can be linked to the paper's per-cell table | Reproduced through the session id (reading M2); no cell links through a stored specimen ID (M1) |
| 385 cells, 283 with features; 90 donors; cells per t-type | Not reproduced (318 cells, 56 donors) |
| Depth of each t-type | Partially reproduced |
| Homologous t-types differ most in input resistance, f-I slope and rheobase | Partially reproduced |
| GLP2R neurons have sag, LTK neurons do not | Reproduced |
| Classifier accuracy, human 67% | Reproduced |
| FREM3 features change with depth | Partially reproduced |
| Deep L3 t-types differ in 15 of 18 features | Reproduced |
| COL22A1 input resistance, f-I gain and sag | Reproduced |
| CARM1P1 upstroke and input resistance | Blocked: methods underspecified |
| Mouse comparisons (mouse features from the code) | Reproduced (3 claims) |
| Pathology and electrophysiology (scores from the code) | Partially reproduced |
| Claims on the code's pathology, morphology and section data | 10 reproduced, 2 blocked |
| Transcriptomic and histological claims on data not pinned or not public | Blocked (5 claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds every one of the 283 cells that have features in the paper's code, and 35 more
of its 385 cells, but none of the labels the paper's findings rest on. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000023-berg-2020-01.yaml`](../../attempts/000023-berg-2020-01.yaml); the questions to
the readers, and their answers, are in [`questions/000023.yaml`](../../questions/000023.yaml).

- `reproduce_berg_2020.ipynb`: the analysis. It took 14 minutes in its last run (26 in an earlier one,
  at a slower network): about 5 to stream the 12.4 GB of recordings and run IPFX on four processes,
  about 6 for the two electrophysiology classifiers and about 2 for the morpho-electric ones.
- `patchseq_l23.py`: listing and streaming the files, IPFX feature extraction with the paper's
  feature names and the Methods' sweep QC, the statistics of the claims file, and a port of the code's
  R scripts for the NeuN sections. Other notebooks on this dandiset can import it.
