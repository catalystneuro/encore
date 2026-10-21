# Scala, Kobak et al. (2021) from dandiset 000008

Tests the findings of [Scala, Kobak et al. (2021)](https://doi.org/10.1038/s41586-020-2907-3) on
[DANDI:000008](https://dandiarchive.org/dandiset/000008/0.211014.0809), which holds the current-clamp
recordings of 1,328 Patch-seq neurons of mouse primary motor cortex, one NWB file per cell, with each
cell's t-type, family, layer and read counts. The paper's gene counts, morphology and reference data are
not in the dandiset; the claims that need them are tested with the paper's own deposits (its code
repository and a Zenodo record) and counted apart.

| Claim | Outcome |
|---|---|
| The dandiset's cells match the paper's metadata table (link) | Reproduced |
| Features extracted from the files match the paper's feature table (link) | Reproduced |
| 1,329 cells from 266 mice | Reproduced |
| Ages of the mice | Reproduced |
| Mice per genotype | Partially reproduced |
| Stimulus protocol | Partially reproduced |
| 1,284 cells with a soma depth | Reproduced |
| Features of the example cell (Extended Data Fig. 4) | Reproduced |
| 1,320 cells with all 17 features, 1,219 with a t-type | Reproduced |
| Pvalb fire fastest, Sst have the highest sag and rebound | Reproduced |
| Families are separable from electrophysiology except IT and ET | Reproduced |
| Features that differ most between L5 IT and ET | Reproduced |
| 1,227 cells with a t-type, 77 t-types | Partially reproduced |
| Soma depths agree with the layer names of excitatory t-types | Partially reproduced |
| L4/5 IT_1 lies on the L2/3 to L5 boundary | Reproduced |
| Many t-types are more variable than k-means clusters | Reproduced |
| Leiden entropies highlight the same variable t-types | Not reproduced |
| Some t-types lie between two families | Reproduced |
| Morphology separates families less well, combined best (with the paper's morphology) | Reproduced |
| cDNA yield does not depend on hold time (with the paper's table) | Reproduced |
| Reduced-rank regression, full and ion-channel genes (with gene counts) | Reproduced (2) |
| Transcriptomic and electrophysiological distances correlate (with the reference) | Reproduced (2) |
| IT depth follows transcriptomic distance; L5 Sst rebound (with the reference) | Reproduced (2) |
| Vip tau, Vip Mybpc1_2 rebound on the t-SNE | Blocked: methods underspecified (2) |
| High-firing Sst Pvalb Calb2 cells group on the t-SNE (with the reference) | Reproduced, at the threshold of its permutation test |
| Sequencing depth, quality control, reference agreement (paper's deposits) | Reproduced (3) |
| 34 °C follow-up; Pvalb axon shape | Blocked: methods underspecified (2) |
| Number of reconstructions (Brain Image Library) | Blocked: data unreadable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

What the attempt found about the dandiset: three pairs of cells share identical voltage recordings (1,325
recordings for 1,328 cells), three
files hold other traces than the ones the paper's features came from, the fields named
`cortical_thickness_4x` and `cortical_thickness_um` hold a soma depth and a cortical thickness in 4x image
units, the units of voltage and current are mislabelled, no sweep has a start time, and the five cells the
paper excludes are not marked. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000008-scala-2021-01.yaml`](../../attempts/000008-scala-2021-01.yaml).

- `scala_2021_ephys.ipynb`: the data check, the link claims and the claims on the recordings and metadata
  (about 18 minutes, most of it streaming the files and running the paper's feature extraction).
- `scala_2021_transcriptomics.ipynb`: the claims that combine the recordings with the paper's gene counts
  and 10x reference (about 18 minutes).
- `scala_2021_sequencing.ipynb`: the sequencing claims on the paper's count tables (about 4 minutes).
- `scala.py`: loading the files, the paper's feature extraction fetched from its repository at a pinned
  commit, the cell table, and the measures of the claims. Other notebooks on this dandiset can import it.
