# Le Merre, Heining et al. (2026) from dandiset 001260

Tests the findings of [Le Merre, Heining et al. (2026)](https://doi.org/10.1038/s41593-025-02190-z)
on [DANDI:001260](https://dandiarchive.org/dandiset/001260/0.250911.0744). The dandiset holds 74
of the 99 Neuropixels and Neuronexus recordings of the paper's dataset KI (41 of 66 mice, 20,374
units). The other 25 recordings are in dandiset 000473, which is read here for the counts, the
number of dataROIs and one variant. Each unit's flatmap position, the Harris and Gao hierarchy
tables and the flatmap polygons come from the paper's Zenodo record 10.5281/zenodo.14205018, as
do, for variants only, the paper's own sleep-like detection and trained SOMs.

| Claim | Outcome |
|---|---|
| Unit and recording counts of dataset KI | Reproduced (with 000473) |
| Waveform classes, ww and nw counts and fractions | Reproduced (with 000473) |
| nw units have higher rate, burstiness and memory | Reproduced |
| Sleep-like epochs differ from active epochs | Partially reproduced |
| Sleep-like time and epoch counts | Not reproduced |
| No linear dependence of burstiness on memory | Not reproduced |
| SOM gradients; high memory excludes high burstiness | Partially reproduced |
| PFC units occupy regular, low anti-memory territory | Reproduced |
| Block-to-block category stability 57% against 18% | Reproduced |
| Low-rate categories less stable | Partially reproduced |
| Layer enrichment of bursty and regular categories | Partially reproduced |
| PFC subregions enriched in low-rate regular categories | Reproduced |
| Enrichment and hierarchy claims that change with the category numbering (Figs. 2g, 3a, 3c, 4g, Extended Data Fig. 7n) | Blocked: methods underspecified (category numbering) |
| Within-PFC absence of a hierarchy relation (Supplementary Table 5) | Blocked: depends on a blocked claim |
| nw enrichment in ILA, PL, ACAd/v and ORBl | Partially reproduced |
| ww and nw enrichment correspondence | Not reproduced |
| Zenodo metrics files match the dataset's units (link) | Reproduced |
| 42 dataROIs | Reproduced (with 000473) |
| dataROI enrichment in ILA, PL, MOs, ORBl | Reproduced |
| Activity modules, ILA-specific module | Blocked: methods underspecified (the claim's two readings) |
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
detection of the Methods, applied per session, marks a median 9.9% of each recording, against 6%
in the paper; the paper's own detection files on Zenodo show that it did not use the detection in
19 recordings, a step the Methods do not describe. Which retrained cluster is which of the
paper's numbered categories is not settled by the paper, and eight enrichment and hierarchy
claims change outcome with it; on the paper's own trained SOM the categories match the text. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001260-le-merre-2026-01.yaml`](../../attempts/001260-le-merre-2026-01.yaml).
