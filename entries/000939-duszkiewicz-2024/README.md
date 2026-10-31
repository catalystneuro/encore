# Duszkiewicz et al. (2024) from dandiset 000939

Tests the findings of [Duszkiewicz et al. (2024)](https://doi.org/10.1038/s41593-024-01588-5) on
[DANDI:000939](https://dandiarchive.org/dandiset/000939/0.261016.2310), which holds 31 recordings
of the postsubiculum (PoSub) with H5 probes, one per mouse, during open-field exploration and
sleep, some with a triangular arena or light over the anterodorsal thalamus (ADN). Claims that
need the ADN, cue rotation, ADN optogenetic and Neuropixel recordings use the paper's
[figshare item](https://doi.org/10.6084/m9.figshare.24921252.v3), version 3.

| Claim | Outcome |
|---|---|
| Cell classes and counts | Partially reproduced (17 of 18 parallel sessions in the dandiset) |
| Excitatory and FS cells carry HD information above control | Reproduced |
| HD can be decoded from FS cells | Reproduced |
| FS tuning is stable within the epoch and across arenas | Reproduced |
| FS tuning follows a rotated cue with HD cells (figshare) | Reproduced |
| ADN-HD cells are broader than PoSub-HD cells (figshare) | Reproduced |
| The first ten Fourier components hold 98% of the power | Partially reproduced |
| Fourier signatures of FS, PoSub-HD and ADN-HD cells differ (figshare) | Not reproduced |
| PoSub-HD spectra are closer to the FS signature than ADN-HD spectra (figshare) | Partially reproduced |
| The same under three controls (figshare) | Partially reproduced |
| FS spectra exceed control in components 1 to 3 only | Reproduced |
| Dominant components of FS cells (231, 141, 55) | Partially reproduced |
| FS spectra are heterogeneous; FS phases are independent | Reproduced |
| Auto-correlogram symmetries; Isomap of auto-correlograms (figshare) | Reproduced |
| Putative HD-to-FS synaptic weights are dispersed | Reproduced |
| Thalamic disinhibition: ADN (figshare) and PoSub rates, preserved tuning | Reproduced |
| HD gain multiplicative, FS gain additive | Partially reproduced |
| Gain simulations; ADN-HD mixed gain (figshare) | Reproduced |
| GLM coupling preserved across WAKE and REM; follows tuning | Reproduced |
| Ring manifold: WAKE and REM tuning from the virtual HD, ring radius | Reproduced |
| HD tuning steps up at the PoSub border (figshare Neuropixel) | Reproduced (qualitative) |
| Simulations, model fit and anatomy (three claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset lacks one parallel-probe session and three of the five ArchT mice of the PoSub
optogenetic experiment, which are on figshare only. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000939-duszkiewicz-2024-01.yaml`](../../attempts/000939-duszkiewicz-2024-01.yaml).

- `reproduce_duszkiewicz_2024.ipynb`: the analysis. It takes about 26 minutes, ten of them in the
  GLM fits.
- `posub.py`: streaming the NWB files and the figshare tarballs, tuning curves, HD information,
  Fourier spectra, decoding, GLMs and synapse detection, each parameter with its source. Other
  notebooks on this dandiset can import it.
