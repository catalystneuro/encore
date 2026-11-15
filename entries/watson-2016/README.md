# Watson et al. (2016) on DANDI:000041 and CRCNS:fcx-1

Tests the claims in `claims/watson-2016.yaml` for Watson, Levenstein, Greene, Gelinas and Buzsáki (2016),
"Network homeostasis and state dynamics of neocortical sleep", Neuron 90, 839-852
(doi:10.1016/j.neuron.2016.03.036), on both of the paper's datasets:

- DANDI:000041 version 0.261104.0300, 22 NWB files, streamed with remfile and h5py;
- CRCNS:fcx-1 (doi:10.6080/K02N506Q, unversioned), 27 session tar.gz files streamed from the public bucket
  `crcnsarchive` and decompressed as they arrive.

`watson.py` holds the loaders, the derivation of the paper's state intervals from the DANDI states, the UP/DOWN and
spindle detection used on DANDI, and the shared measures (per-second grids, time-normalized correlations, slopes,
sextiles). `reproduce_watson_2016.ipynb` has one section per claim; each prints the result on both datasets.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences
from the paper's method.

The notebook streams about 90 GB from CRCNS and reads one or two LFP channels of each DANDI file; it takes about 30
minutes on 4 CPUs and peaks near 10 GB of memory.
