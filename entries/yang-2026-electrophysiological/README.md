# Yang & Xiao (2026) from dandiset 000020

Tests the findings of [Yang and Xiao (2026)](https://doi.org/10.64898/2026.01.08.698522) on
[DANDI:000020](https://dandiarchive.org/dandiset/000020/0.210913.1639), the Allen Institute
Patch-seq recordings from mouse visual cortex (4435 cells), the dataset the paper analysed. The
paper builds PCA response geometries from long-pulse, ramp and brief-pulse current-clamp sweeps,
orders driver lines along their axes, and compares driver-line distances across protocols.

| Claim | Outcome |
|---|---|
| Cells per geometry (about 2270, 3220, 2154) | Partially reproduced (ramp and brief pulse match; long pulse does not) |
| 9, 9 and 11 driver lines, 7 shared | Reproduced (8 shared) |
| Long-pulse variance explained (39, 15, 76%) | Not reproduced |
| Long-pulse continuum with biased line occupancy | Reproduced |
| Long-pulse PC1 and PC2 loadings | Reproduced |
| Pvalb centroid farthest from Vip and Sncg | Reproduced |
| Pvalb high and Vip low on long-pulse PC2 | Reproduced |
| Ramp variance explained (33, 21, 87%) | Reproduced |
| Ramp continuum with biased line occupancy | Reproduced |
| Ramp PC1 recruitment, PC2 output loadings | Reproduced |
| Pvalb highest, Vip and Sncg lowest ramp recruitment current | Reproduced |
| Brief-pulse response variance explained (47, 19, 95%) | Reproduced |
| Brief-pulse continuum with biased line occupancy | Reproduced |
| Brief-pulse PC1 dominated by amplitude features | Reproduced |
| Brief response PC1 aligned with base PC2 (r 0.875, 0.900) | Reproduced |
| Vip and Cck highest gain, Pvalb not at the top | Reproduced |
| Cck and Sncg also high gain | Reproduced |
| Long-pulse PC2 and ramp PC1 centroids aligned (r 0.883) | Reproduced |
| Long-pulse and ramp distance alignment (r 0.707) | Partially reproduced (r 0.88) |
| Balanced correlations positive (medians 0.61 to 0.79) | Partially reproduced (all positive, 2 of 6 within tolerance) |
| True alignments above the label-shuffle null | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper gives no thresholds, spike criterion, response windows, feature lists or resampling
settings, and its code is not public, so most outcomes rest on stated assumptions; every reading
the claims name is run and shown. One recording is deposited twice, under two subjects with
different genotypes. The attempt record, with the reasons and the differences from the paper's
method, is
[`attempts/yang-2026-electrophysiological-01.yaml`](../../attempts/yang-2026-electrophysiological-01.yaml).

- `reproduce_yang_2026.ipynb`: the analysis. It takes about 25 minutes, 15 of them streaming the
  4435 files in 40 processes.
- `geometry.py`: streaming the files, per-sweep features of the three protocols, cell-level
  features after Supplementary Table 1, PCA geometries, centroid distances and balanced
  resampling. Other notebooks on this dandiset can import it.
