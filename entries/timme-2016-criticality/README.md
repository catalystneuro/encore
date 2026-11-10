# Timme et al. (2016) on CRCNS hc-8

Tests the findings of Timme, Marshall, Bennett, Ripp, Lautzenhiser and Beggs (2016), "Criticality
Maximizes Complexity in Neural Tissue", Front. Physiol. 7:425 (doi:10.3389/fphys.2016.00425), on
CRCNS data set hc-8 (doi:10.6080/K0PC308P), the spike-sorted spontaneous activity of 435 recordings
from 28 dissociated rat hippocampal cultures. The files are read in place from the public bucket
`crcnsarchive/hc-8/live/Data.zip`; CRCNS data sets are not versioned, so the zip's MD5 from the
data set's `checksums.md5` pins it.

- `culture_criticality.ipynb`: counts, network ISI, avalanches, critical exponents with and without
  sub-sampling, branching ratios, susceptibility, shape collapse curvature and fit ranges, and how
  they change under randomization (all 435 recordings, about 42 min with 4 processes).
- `complexity_culture.ipynb`: neural complexity of the real and randomized data (40 recordings,
  100 subsets per size, about 38 min).
- `models.ipynb`: the chain model, the Bethe lattice and the cortical branching model (about 11 min).
- `hc8.py`: loading, and a Python port of the NCC MATLAB toolbox functions the paper used
  (`plparams`, `plmle`, `pvcalc`, `avprops`, `rebin`, `avgshapes`, `avshapecollapse`,
  `sizegivdurwls`, `complexity`, `randomizeasdf2`, `brestimate`). `models.py`: the models.

The counts of recordings and neurons match the paper exactly, and the exponents, branching ratios,
susceptibility, curvature and fit ranges behave as the paper reports, with some exceptions under
the weakest randomization. The number of avalanches per recording is about eight times the stated
10,000. The complexity results depend on the toolbox's cut of the integration curve, which keeps
about a tenth of the subset sizes in the real data even with the paper's 100 subsets per size:
with it, shuffling raises complexity, against the paper, while spike swapping leaves it unchanged,
as the paper says. In the cortical branching model the susceptibility rises to the end of the
p_trans range with no peak. Two model claims are blocked for time.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Run with `python tools/entry.py all entries/timme-2016-criticality`.
