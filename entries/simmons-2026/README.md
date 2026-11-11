# Simmons et al. (2026) from dandiset 001777

Tests the findings of [Simmons et al. (2026)](https://doi.org/10.1126/sciadv.adq8840) that can be
tested on [DANDI:001777](https://dandiarchive.org/dandiset/001777/0.260521.2201), which holds
cell-attached and whole-cell recordings of SNr neurons in brain slices: spiking before and after
bath drugs, and evoked IPSCs. The SNc recordings, imaging, RNAscope and voltammetry of the paper
are not in it.

| Claim | Outcome |
|---|---|
| Quinpirole reduces optogenetic GPe IPSCs by about 30% (Fig. 1C) | Reproduced |
| Quinpirole raises the paired-pulse ratio (Fig. 1E) | Reproduced |
| Quinpirole attenuates the inhibition by a GPe train (Fig. 2C) | Not reproduced |
| The train's inhibition wanes (Fig. 2B) | Reproduced |
| Quinpirole raises SNr rate by about 50% (Fig. 3A) | Not reproduced |
| Gabazine raises SNr rate by about 25% (Fig. 3B) | Partially reproduced (assumed) |
| The gabazine effect correlates with basal rate (Fig. S1) | Not reproduced |
| GPe Gi-DREADD reduces evoked IPSCs (Fig. 4A) | Not reproduced |
| GPe Gi-DREADD does not change SNr rate (Fig. 4B) | Reproduced (assumed) |
| Gabazine has no effect after shRNA, disulfiram, DEAB, rasagiline or NNC-711 (Figs. 5E, 5G, 5H, 6A, 6E) | Reproduced |
| Astrocytic Gi-DREADD raises SNr rate by 28% (Fig. 7D) | Reproduced (assumed) |
| Gabazine occludes the astrocytic Gi-DREADD effect (Fig. 7E) | Reproduced |
| SNAP-5114 lowers SNr rate by 23% (Fig. 7F) | Partially reproduced |
| SNAP-5114 occludes quinpirole (Fig. 7F) | Reproduced |
| NNC-711 raises SNr rate by 36% (Fig. 7H) | Reproduced |
| shRNA SNr neurons and ALDH-inhibited SNr neurons fire faster than controls (Figs. 5D, 5F) | Blocked: the control cells are not labelled |
| Sixteen claims on data not in the dataset, and two on outside data | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The condition of each file is given only in its free-text notes, which the helper `snr.py`
parses. Spikes are detected by a threshold of the helper's own choosing, as the paper gives no
settings; every rate result is shown at three thresholds, and without seven recordings whose
action currents fade into the noise during the experiment. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/simmons-2026-01.yaml`](../../attempts/simmons-2026-01.yaml).
