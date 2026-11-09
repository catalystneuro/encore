# Okubo, Mackevicius, Payne, Lynch & Fee (2015) from CRCNS am-3

Tests the findings of [Okubo et al. (2015)](https://doi.org/10.1038/nature15741), "Growth and splitting of neural
sequences in songbird vocal development", on [CRCNS am-3](https://doi.org/10.6080/K01N7Z2Z), which holds the spike
times and syllable segments of 1,125 HVC projection neurons recorded in 32 juvenile zebra finches during singing.
The adult neurons the paper adds from earlier recordings are not in it. The model claims run a Python port of the
paper's own model code.

| Claims | Outcome |
|---|---|
| Neuron counts, stages and ages; protosyllable participation; latency shift from subsong to later stages; bird 1's protosequence; HVCRA and HVCX alike | Reproduced (7) |
| Shared and specific neurons of bird 1 early and late; shared fraction falling across birds and in bird 2; B/D sharing in bird 1; bias; shared proportions of HVCRA and HVCX; the IBI of shared and specific neurons; bird 2 before beta | Reproduced, resting on a rule standing in for the paper's visual window adjustment or on another stated assumption (9) |
| Locking and rhythm rising through development; protosequence latencies; coverage; simultaneous pairs; latency correlations of bird 1; totals over all pairs; skipping cycles; bird 2 after beta | Partially reproduced (9) |
| Subsong locking (19 of 39); rhythmic neurons in subsong and the protosyllable stage; bout-related counts; latency correlations of the other pairs; bird 4's protosyllable-stage rhythms | Not reproduced (5) |
| Burst width against adults (adult neurons missing); bird 3's phase analysis and the motif strategy (bird 3's labels missing); acoustic differences (Sound Analysis Pro) | Blocked (4) |
| Model (8 claims) | 7 reproduced, 1 not reproduced (three-group motif strategy) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons, readings and differences from the paper's method, is
[`attempts/okubo-2015-01.yaml`](../../attempts/okubo-2015-01.yaml).

- `reproduce_okubo_2015.ipynb`: the analysis, about 16 minutes; most of it is the surrogate tests of rhythmicity
  for every neuron, run in 4 processes.
- `hvc.py`: loading the analysis files and the neuron list from the public bucket, and the measures of the
  Methods (syllable and bout locking, rhythmicity, shared and specific neurons, protosyllables, coverage).
- `hvcmodel.py`: the network model of the paper's Supplementary Information, ported from MATLAB, and the motif-strategy script of the GitHub repository its code names (commit 05dc96b).
