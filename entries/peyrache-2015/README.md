# Peyrache et al. (2015) on DANDI:000056

Tests the claims in `claims/peyrache-2015.yaml` for "Internally organized mechanisms of the head direction
sense" (Peyrache, Lacroix, Petersen and Buzsaki, Nature Neuroscience 2015, doi:10.1038/nn.3968) on dandiset
000056, version 0.261106.1949, streamed from the archive.

- `reproduce_peyrache_2015.ipynb` runs every analysis. It streams the 42 sessions four at a time, and its
  data check comes first, followed by one section per claim.
- `hd.py` holds the loading code and the measures. The docstring of each says where its parameters come from.

Of 35 claims, 32 are tested. The three GLM claims of Fig. 5d,e are blocked as too large for the time limit.
The record is `attempts/peyrache-2015-02.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
