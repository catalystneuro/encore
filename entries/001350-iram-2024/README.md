# Iram, Garcia et al. (2024) from dandiset 001350 and GEO GSE241561

Tests the findings of [Iram, Garcia et al. (2024)](https://doi.org/10.1073/pnas.2307250121) that can
be tested on [DANDI:001350](https://dandiarchive.org/dandiset/001350/0.250511.1527), which holds the
adult corpus callosum TEM images of Figure 2A to 2E and Fig. S3, and on the paper's ChIP-seq and bulk
RNA-seq in NCBI GEO (GSE241561).

| Claim | Data | Outcome |
|---|---|---|
| Fewer myelinated axons in cKO corpus callosum (Fig. 2C) | dandiset | Blocked: data missing (masks for one SRF-Flox mouse) |
| Fewer myelinated axons per area (Fig. 2D) | dandiset | Blocked: data missing (masks for one SRF-Flox mouse) |
| Higher g-ratio in cKO (Fig. 2E) | dandiset | Blocked: data missing (masks for one SRF-Flox mouse) |
| Myelin thickness unchanged (Fig. S3C) | dandiset | Blocked: data missing (masks for one SRF-Flox mouse) |
| Larger myelinated axons in cKO (Fig. S3D) | dandiset | Blocked: data missing (masks for one SRF-Flox mouse) |
| Optic nerve TEM, staining, RNAscope, culture imaging (14 claims) | dandiset | Blocked: data missing |
| 848 SRF peaks, 329 high-confidence (Fig. 3A) | GEO | Partially reproduced |
| Peaks near TSS and enriched for CArG (Fig. 3B, 3C) | GEO | Reproduced, on an assumption |
| About half (60) of CArG targets shared (Fig. 3D) | GEO | Partially reproduced |
| No myelin genes among SRF targets | GEO | Reproduced, on an assumption |
| 157 and 264 differentially expressed genes (Fig. 4A, 4B) | GEO | Reproduced, on an assumption |
| Srf and Actb down in KO cells (Fig. 4C, 4D) | GEO | Reproduced, on an assumption |
| Assembly genes regulated, disassembly genes largely unchanged, Cfl1 lower in KO oligodendrocytes (Fig. S4E, S4F) | GEO | Partially reproduced, on an assumption |
| GSEA and single-nucleus RNA-seq (4 claims) | GEO | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds the raw images of all ten mice, but the paper's hand scoring is not deposited,
and the segmentation masks, made later for a segmentation project, cover one of the five SRF-Flox
mice. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001350-iram-2024-01.yaml`](../../attempts/001350-iram-2024-01.yaml).

- `reproduce_iram_2024.ipynb`: the TEM claims, from the dandiset's masks. About two minutes.
- `geo_sequencing_claims.ipynb`: the ChIP-seq and RNA-seq claims, from GEO's processed files. Fifteen
  to twenty-five minutes, most of it the DESeq2 fits; NCBI's server refuses some requests, which are retried.
- `srf_tem.py`: loading the images and masks, and the axon measures.
- `srf_geo.py`: loading the GEO files and the paper's Datasets S1 to S3 (for comparison only), DESeq2 through pydeseq2 (with tximport's length offsets put into its fits), rn6 sequence by range requests,
  and CArG motif matching.
