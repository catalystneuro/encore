# Steinmetz, Zatka-Haas, Carandini & Harris (2019) from dandiset 000017

Tests the findings of [Steinmetz et al. (2019)](https://doi.org/10.1038/s41586-019-1787-x) on
[DANDI:000017](https://dandiarchive.org/dandiset/000017/0.240329.1926), which holds Neuropixels
recordings from 39 sessions of 10 mice during a visual discrimination task, each followed by a
passive replay of the task stimuli.

| Claims | Outcome |
|---|---|
| Behaviour: error and Miss rates, reaction times, wheel decoding, early turns (6) | Reproduced |
| Passive replay: 94.1% of high-contrast presentations without movement | Not reproduced |
| Counts of sessions, mice, probes, neurons and trials; sessions of Supplementary Table 2 | Reproduced |
| Per-region counts of Extended Data Table 1 | Reproduced |
| 60% of neurons task-modulated, 74% increasing and 20% decreasing | Reproduced |
| Responsive neurons have higher baseline rates, similar amplitudes | Not reproduced |
| Activity spreads from VIS and SCs on contralateral choices | Reproduced |
| Miss trials activate a visual pathway only; Miss above passive | Not reproduced (2 claims) |
| Pre-stimulus task against passive differences and their order; Go-Miss match; detect probability (4) | Reproduced |
| Engagement index and its controls (6) | Reproduced |
| Detect probability around movement is widespread | Reproduced |
| jPECC: VIS leads frontal cortex and midbrain | Reproduced |
| jPECC: no lag between frontal cortex and midbrain | Not reproduced |
| Kernel model: variance explained is small; vision localized; contralateral preference in midbrain (3) | Reproduced |
| Kernel model: action encoded in all regions | Partially reproduced |
| Kernel model: choice-neuron counts, focality, shuffle false positives, opposed activity, ccCP restriction (5) | Not reproduced (a change to reproduced was proposed for the shuffle false positives and not agreed by the verifier) |
| Decoding from kernel-model residuals (2) | Blocked: not written in this attempt |
| Histology alignment error | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/steinmetz-2019-01.yaml`](../../attempts/steinmetz-2019-01.yaml).

- `reproduce_steinmetz_2019.ipynb`: the analysis. It took 2,084 s (about 35 minutes) in the last run,
  650 s of it loading the 39 files.
- `steinmetz.py`: loading the files (trials, wheel movements, passive events, spikes binned around
  events), the trial and neuron definitions of the claims file, the six responsiveness tests, the
  combined-conditions choice probability, jPECC and the kernel model (design, the basis of the code's
  CanonCor2all.m, elastic net on the Gram matrix, cross-validated variance explained, and the code's reading of the fits as a variant). Other notebooks on this dandiset can import it.
