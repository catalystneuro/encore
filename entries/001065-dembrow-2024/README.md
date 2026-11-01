# Dembrow, Sawchuk et al. (2024) from dandiset 001065

Tests the findings of [Dembrow, Sawchuk et al. (2024)](https://doi.org/10.1016/j.celrep.2024.114718)
on [DANDI:001065](https://dandiarchive.org/dandiset/001065/0.241028.1559), which holds the current
clamp recordings of 294 deep-layer neurons from macaque motor (MCx) and temporal (TCx) cortex.
Every physiology feature is computed from the traces in `dembrow.py`; area, preparation and
subclass labels come from the per-cell tables of the paper's code on Zenodo, matched by cell name.

| Claim | Outcome |
|---|---|
| The files are the cells of the paper's tables (link) | Reproduced |
| Cohort: 58 macaques; 300 new recordings | Reproduced |
| L5 ET neurons differ from other neurons: higher resonance, lower input resistance, faster spikes | Reproduced |
| Projection type has the largest effects; a classifier predicts subclass from physiology | Reproduced |
| CS neurons lie only among L5 ET neurons in the UMAP | Not reproduced |
| The largest projection effects are subthreshold features; interactions with area are small | Not reproduced |
| No effect of species | Not reproduced |
| MCx and TCx L5 ET neurons differ (resonance, fAHP, symmetry, input resistance, instantaneous FI slopes) | Reproduced |
| MCx L5 ET neurons need more current to fire | Not reproduced |
| Firing to 4 nA: higher MCx spike counts, equal instantaneous rates, upstroke ratio | Reproduced |
| Depolarization block in TCx; spike width ratio | Partially reproduced; not reproduced |
| Irregular firing and subthreshold oscillations (Figure 7, six claims) | Four partially reproduced, one not reproduced, one reproduced |
| Dendritic morphology, on the paper's deposited features | Reproduced or partially reproduced |
| Transcriptomic claims (Patch-seq in SRA, snRNA-seq in NeMO) and dendrite per layer | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001065-dembrow-2024-01.yaml`](../../attempts/001065-dembrow-2024-01.yaml).
