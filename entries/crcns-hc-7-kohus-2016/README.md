# Kohus et al. (2016) on CRCNS hc-7

Tests the paired-recording findings of Kohus, Káli, Rovira-Esteban, Schlingloff, Papp, Freund, Hájos
and Gulyás (2016), J Physiol, [doi:10.1113/jp272231](https://doi.org/10.1113/jp272231), on CRCNS data set
hc-7 ([doi:10.6080/K0MK69T5](https://doi.org/10.6080/K0MK69T5)), streamed from the public S3 bucket
`crcnsarchive` (the data set is not versioned; the notebook prints the MD5 sum of `Data.zip`).

- `reproduce_kohus_2016.ipynb`: the attempt, one section per claim.
- `hc7.py`: reading the zip (`.hda` headers, float32 sweeps, `_EPA` tables), single-AP measures,
  the asynchronous-release reconstruction and the short-term plasticity models.

The data set holds the paired recordings of eight connection types; the paper's current-step,
connectivity, spontaneous IPSC and field potential data are not in it, and the claims on them are
blocked. The record is `attempts/crcns-hc-7-kohus-2016-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.
