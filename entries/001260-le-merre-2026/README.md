# Le Merre, Heining et al. (2026) from dandiset 001260

Tests the findings of [Le Merre, Heining et al. (2026)](https://doi.org/10.1038/s41593-025-02190-z)
on [DANDI:001260](https://dandiarchive.org/dandiset/001260/0.250911.0744). The dandiset holds 74
of the 99 Neuropixels and Neuronexus recordings of the paper's dataset KI (41 of 66 mice, 20,374
units). The other 25 recordings are in dandiset 000473, which is read here for the counts only.
Each unit's flatmap position, the Harris and Gao hierarchy tables and the flatmap polygons come
from the paper's Zenodo record 10.5281/zenodo.14205018.

| Claim | Outcome |
|---|---|
| Unit and recording counts of dataset KI | Partially reproduced |
| Waveform classes, ww and nw counts and fractions | Partially reproduced |
| nw units have higher rate, burstiness and memory | Reproduced |
| Sleep-like epochs differ from active epochs | Reproduced |
| Sleep-like time and epoch counts | Not reproduced |
| No linear dependence of burstiness on memory | Not reproduced |
| SOM gradients; high memory excludes high burstiness | Partially reproduced |
| PFC units occupy regular, low anti-memory territory | Reproduced |
| Block-to-block category stability 57% against 18% | Reproduced |
| Category stability and enrichment claims that change with the category numbering (Figs. 2f, 2g, 3c, 4g, Extended Data Figs. 3f, 7n) | Blocked: methods underspecified (category numbering) |
| TH and HPF enriched in bursty categories | Blocked: methods underspecified (the claim's two readings) |
| nw enrichment in ILA, PL, ACAd/v and ORBl | Not reproduced |
| ww and nw enrichment correspondence | Partially reproduced |
| Harris hierarchy correlations (Fig. 3a, Supplementary Table 5) | Blocked: depend on a blocked claim |
| Zenodo metrics files match the dataset's units (link) | Reproduced |
| 42 dataROIs | Reproduced (with 000473) |
| dataROI enrichment in ILA, PL, MOs, ORBl | Reproduced |
| Activity modules, ILA-specific module | Partially reproduced |
| Category 1 enrichment correlates with Gao hierarchy | Not reproduced |
| Tone response categories | Reproduced |
| Tone maps cross subregions | Partially reproduced |
| Tone-responsive patches; no correlation with Gao hierarchy | Reproduced |
| Tone-responsive units have high spontaneous rates | Not reproduced |
| Claims on the IBL data (Figs. 2i, 3b, 5g, 5h, 5i, 5k) | Blocked: too large |
| Firing metrics do not differ across settings | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold every sorted unit of the 99 recordings (with 000473, the 29,782 units the paper
had before its quality control) and no label of which units the paper kept. The sleep-like
detection of the Methods flags a median 20% of each recording, against 6% in the paper, which
leaves fewer active epochs and units for every analysis. Which retrained cluster is which of the
paper's numbered categories is not settled by the paper, and many enrichment claims change
outcome with it. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001260-le-merre-2026-01.yaml`](../../attempts/001260-le-merre-2026-01.yaml).
