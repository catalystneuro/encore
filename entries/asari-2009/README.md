# asari-2009

Tests the findings of Asari and Zador (2009), "Long-Lasting Context Dependence Constrains Neural Encoding Models in Rodent Auditory Cortex" (J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009), on CRCNS ac-1 (doi:10.6080/K0KW5CXR), streamed from the public bucket `crcnsarchive`.

- `reproduce_asari_2009.ipynb`: every claim except the encoding models; reads all of Asari's recordings once (about 40 minutes).
- `strf_wehr.ipynb`: the STRF and LN encoding models on Wehr's recordings (fig4-strf-performance-low, about 20 minutes).
- `asari.py`, `wehr.py`: loading and measures; the docstrings say where each parameter comes from.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

The record is `attempts/asari-2009-03.yaml`.
