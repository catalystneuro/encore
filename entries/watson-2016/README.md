# Watson et al. (2016) on DANDI:000041 and CRCNS:fcx-1

Tests the claims in `claims/watson-2016.yaml` for Watson, Levenstein, Greene, Gelinas and Buzsáki (2016),
"Network homeostasis and state dynamics of neocortical sleep", Neuron 90, 839-852
(doi:10.1016/j.neuron.2016.03.036), on both of the paper's datasets:

- DANDI:000041 version 0.261104.0300, 22 NWB files, streamed with remfile and h5py;
- CRCNS:fcx-1 (doi:10.6080/K02N506Q, unversioned), 27 session tar.gz files streamed from the public bucket
  `crcnsarchive` and decompressed as they arrive.

`watson.py` holds the loaders, the derivation of the paper's state intervals from the DANDI states, the UP/DOWN and
spindle detection used on DANDI, and the shared measures (per-second grids, time-normalized correlations, slopes,
sextiles, ISI counts from spike times). `reproduce_watson_2016.ipynb` has one section per claim; each prints the result on
both datasets. Outcomes are judged on CRCNS:fcx-1, which holds the paper's whole data set with the lab's own intervals and
detections; the DANDI result is stated beside it.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences
from the paper's method.

The notebook streams the 27 CRCNS tar.gz files in full (88.9 GB) and reads one or two LFP channels of each DANDI file
(149.5 GB in all, read in part). It takes about 25 minutes on 4 CPUs; the notebook process peaks near 2.6 GB and the
largest of the loading workers, which run two at a time on DANDI and three on CRCNS, about 5 GB (4.9 to 5.3 GB
in this attempt's runs). The cell before the summary prints the bytes, the time and the memory of the run.
