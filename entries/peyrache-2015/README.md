# Peyrache et al. (2015) on DANDI:000056

Tests the claims in `claims/peyrache-2015.yaml` for "Internally organized mechanisms of the head direction
sense" (Peyrache, Lacroix, Petersen and Buzsaki, Nature Neuroscience 2015, doi:10.1038/nn.3968) on dandiset
000056, version 0.261106.1949, streamed from the archive.

- `reproduce_peyrache_2015.ipynb` runs every analysis but the GLM. It streams the 42 sessions four at a time, and its
  data check comes first, followed by one section per claim.
- `glm_peyrache_2015.ipynb` runs the GLM prediction between ADn and PoS of Fig. 5d,e, on the sessions of the
  mice with both structures, in a notebook of its own.
- `glm_windows_peyrache_2015.ipynb` runs the same GLM with the dense grid of readout windows that
  fig5e-readout-windows needs, for PoS targets only.
- `hd.py` holds the loading code and the measures. The docstring of each says where its parameters come from.

All 35 claims are tested. fig5e-readout-windows was first recorded as blocked (too large); the round-2
verifier found that the printed timing did not support the block, and it now runs in
`glm_windows_peyrache_2015.ipynb`. The third verification round agreed that it, and fig4d-ole-near-bayesian
from the ensembles of hd-b cells, are partially reproduced.
The record is `attempts/peyrache-2015-02.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
