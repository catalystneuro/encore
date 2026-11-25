# Allen, Yan, Kuan et al. (2026) from Dryad rjdfn2zqz

Tests the findings of [Allen et al. (2026)](https://doi.org/10.1038/s42003-025-09506-6) on
[Dryad rjdfn2zqz](https://doi.org/10.5061/dryad.rjdfn2zqz), version id 439366. The dataset holds
per-squid values for metabolism, ammonia excretion, hemolymph acid-base state, exploration,
predation and critical flicker fusion, group means of the ERG response ratio, and the authors' RSEM
count matrix and R workspace with their DESeq2, sva and GSEA results for the optic lobes.

| Claim | Outcome |
|---|---|
| Metabolic rate, ammonia excretion, blood pH, PCO2 and bicarbonate (Fig. 1B to 1F) | Reproduced |
| Distance, velocity, time in upper, left and front zones (Fig. 2C to 2F, Supplementary Fig. 2) | Reproduced |
| Attack willingness, logistic regression (Fig. 2G) | Not reproduced |
| Hunt duration and strike attempts (Fig. 2H, 2I); prey shrimp velocity (Supplementary Fig. 3) | Reproduced |
| ERG ratio declines above 40 Hz (Fig. 3C) | Not reproduced |
| CFF unchanged, CFF variance (Fig. 3D) | Reproduced |
| Assembly statistics, sample distances, GSEA families, nAChR subunits | Reproduced |
| PCA (Fig. 4A), shared down-regulated sets (Fig. 4B), chronic up-regulated counts (Fig. 4F to 4H) | Partially reproduced |
| No change in acid-base or ion regulatory transcripts | Not reproduced |
| Body size, seawater chemistry, mean depth, ERG amplitude | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/allen-2026-01.yaml`](../../attempts/allen-2026-01.yaml). It reports, among other
things, that the deposited count matrix has lost a column and is mislabelled when read as the
authors' script reads it, that the prey shrimp table repeats the control column for the CO2 group,
and that the prey capture file lacks 11 chronic-OA squid.

- `reproduce_allen_2026.ipynb`: the analysis. It takes about a minute and about 4 GB of memory,
  most of it reading the R workspace.
- `squidoa.py`: reading the staged files, a streaming reader for R's serialization format that
  builds only the workspace objects asked for, and the tests the paper names (Welch's ANOVA,
  Dunnett's T3, one-way ANOVA with Tukey's test, DESeq2's PCA, limma's removeBatchEffect).
