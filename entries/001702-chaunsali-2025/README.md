# Chaunsali, Li, Fleischel et al. (2025) from dandiset 001702

Tests the findings of [Chaunsali et al. (2025)](https://doi.org/10.1002/alz.70813) on
[DANDI:001702](https://dandiarchive.org/dandiset/001702/0.260216.2323). The dandiset's 481 NWB files
hold only metadata, with no images or measurements, and its 175 behaviour videos carry no subject,
group or trial labels, so the immunohistochemistry and behaviour claims cannot be tested. The bulk
RNA-seq claims of Figure 4 are tested on the counts the authors deposited in GEO
([GSE317499](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE317499)), which the dandiset does
not hold.

| Claim | Outcome |
|---|---|
| 3 M 5XFAD against control, 98 up and 133 down DEGs | Blocked: methods underspecified |
| 7 M 5XFAD against control, 314 up and 6 down DEGs | Partially reproduced |
| 3 M top GO terms include learning, memory and cognition, down | Blocked: methods underspecified |
| 7 M top GO terms are immune responses, up | Reproduced |
| ECM GO terms change at 7 M but not at 3 M | Blocked: methods underspecified |
| PNN synthesis genes: Vcan, Cspg5, Tnr, Hapln1 down at 3 M; Vcan, Bgn up at 7 M | Reproduced |
| MMP, TIMP and ADAM genes up at 3 M, at 7 M, and at 7 M against 3 M | Reproduced (three claims) |
| Immunohistochemistry, Figures 1, 3, 5 and S1 to S6, S9 (22 claims) | Blocked: data missing |
| Social memory and object recognition, Figures 2, 3, 5, S7, S8 (19 claims) | Blocked: metadata insufficient |
| Social memory of the RNA-seq cohort | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The paper does not say which DESeq2 design or GO enrichment method it used. Every reading the
claims file names is run (one model per age or one on all 16 samples, unshrunken or shrunken fold
changes, two GO backgrounds), with two GO term-size limits, and a claim whose readings give
different outcomes is blocked as methods underspecified. With one model per age and unshrunken
fold changes the 3 M DEG counts are 95 and 136, both within tolerance; with one model on all
samples they are 51 and 141. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001702-chaunsali-2025-01.yaml`](../../attempts/001702-chaunsali-2025-01.yaml).

- `reproduce_chaunsali_2025.ipynb`: the data check of the dandiset and the RNA-seq analysis. It
  takes about ten minutes, most of it the six DESeq2 fits.
- `ca2pnn.py`: listing and scanning the dandiset's files, probing its videos, loading the GEO
  counts and the GO release, DESeq2 through pydeseq2, and GO over-representation with the GOplot
  z-score.
