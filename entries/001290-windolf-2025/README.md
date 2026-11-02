# Windolf et al. (2025) from dandiset 001290

Tests the findings of [Windolf et al. (2025)](https://doi.org/10.1038/s41592-025-02614-5) that can
be tested on [DANDI:001290](https://dandiarchive.org/dandiset/001290/0.260827.1449), which holds
one 600 s Neuropixels 1.0 recording in an anesthetized macaque, the "fast-motion NHP dataset of
Extended Data Fig. 3". The paper's other findings use human, mouse, rat, simulated and other
macaque data held in other archives and are not tested here.

| Claim | Outcome |
|---|---|
| DREDge's spike-based estimate follows the drift in the unregistered raster (Extended Data Fig. 3a) | Reproduced (assumed) |
| HDBSCAN isolates clusters of high-amplitude registered spikes (Extended Data Fig. 3b) | Reproduced (assumed) |
| A spline fit to the centred clustered spikes captures sub-second displacement (Extended Data Fig. 3c) | Reproduced (assumed) |
| Spline correction gives a more stable raster and tighter localizations (Extended Data Fig. 3d, e) | Partially reproduced (assumed) |
| 30 claims on data outside the dandiset | Blocked: not attempted in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper does not say how spikes were detected and localized for this recording. The claims file
names two readings; only the one from the DREDge repository's demo notebook (SpikeInterface
detection and monopolar triangulation) could be run, as DARTsort was far too slow on a CPU, so every
outcome rests on that reading. The IBL preprocessing of the other reading, run before the same
detection, gives the same outcomes. The claims file's control for the spline (Extended Data Fig. 3c)
passes even on data without motion; the notebook adds a held-out check, on which the penalized
spline still lowers the spread of spikes it was not fit to. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/001290-windolf-2025-01.yaml`](../../attempts/001290-windolf-2025-01.yaml).

- `reproduce_windolf_2025.ipynb`: the analysis. It takes about 25 minutes, a third of it streaming
  the 7.4 GB file and detecting and localizing spikes.
- `ibl_preprocessing_variant.ipynb`: the same tests with the IBL preprocessing (bad channel
  detection, phase shift, interpolation, spatial high-pass) before detection. About 30 minutes.
- `pulsation.py`: streaming the AP band in chunk-aligned blocks, both preprocessings, spike
  detection and localization, DREDge registration, the template correlation metric, HDBSCAN
  clustering, the fast-motion spline and its tests. Other notebooks on this dandiset can import it.
