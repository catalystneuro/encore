# Dana et al. (2016) from CRCNS cai-2

Tests the findings of [Dana et al. (2016)](https://doi.org/10.7554/eLife.12727) that can be tested
on [CRCNS cai-2](https://doi.org/10.6080/K0W37T87), which holds simultaneous two-photon imaging and
loose-seal cell-attached recordings of 11 jRGECO1a and 10 jRCaMP1a neurons in L2/3 of mouse V1
(Figure 4). Three claims on the neuronal culture screen are tested on the paper's Supplementary
files 1 and 2. The paper's other experiments (cultured neurons, purified protein, V1 grating
responses, Drosophila, zebrafish, C. elegans) are not in the data set.

| Claim | Outcome |
|---|---|
| Improved single mutants in the culture screen (353 of 934, 187 of 689) | Not reproduced |
| jRGECO1a 8.5-fold 1 AP sensitivity over R-GECO1, similar decay and saturation | Reproduced (supplementary table) |
| jRCaMP1a and jRCaMP1b 24- and 13-fold over RCaMP1h | Reproduced (supplementary table) |
| 11 jRGECO1a cells in 6 mice, 10 jRCaMP1a cells in 5 mice | Reproduced |
| Event counts of Figure 4d and 4e | Partially reproduced |
| jRGECO1a single spike detection, 82% at 5% false positives | Reproduced |
| jRGECO1a two spike detection, 96% | Reproduced |
| jRCaMP1a detection, 65% and 80% | Reproduced, resting on an assumption |
| jRGECO1a above jRCaMP1a in amplitude and d-prime for 1 to 8 spikes | Reproduced |
| jRGECO1a faster than jRCaMP1a for 2 spikes | Reproduced |
| Kinetics similar to GCaMP6f and GCaMP6s | Blocked: other |
| Culture, protein, V1 grating, fly, fish and worm claims (24) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set's own MATLAB script for Figure 4 reproduces the paper's jRGECO1a event counts
exactly, and its event isolation, noise traces and frame window are used as the main reading for
the detection claims. It is written for jRGECO1a; the jRCaMP1a counts it gives differ from the
paper's. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/dana-2016-01.yaml`](../../attempts/dana-2016-01.yaml).

- `reproduce_dana_2016.ipynb`: the analysis. It takes about three minutes, almost all of it streaming
  the two 1.1 and 1.3 GB archives.
- `cai2.py`: streaming the archives, the event and noise selection, the traces, projections,
  d-prime and the kinetics fits. Other notebooks on this data set can import it.
