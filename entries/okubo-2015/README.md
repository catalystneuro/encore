# Okubo, Mackevicius, Payne, Lynch & Fee (2015) from CRCNS am-3

Tests the findings of [Okubo et al. (2015)](https://doi.org/10.1038/nature15741), "Growth and splitting of neural
sequences in songbird vocal development", on [CRCNS am-3](https://doi.org/10.6080/K01N7Z2Z), which holds the spike
times and syllable segments of 1,125 HVC projection neurons recorded in 32 juvenile zebra finches during singing.
The adult neurons the paper adds from earlier recordings are not in it. The model claims run a Python port of the
paper's own model code.

| Claims | Outcome |
|---|---|
| Neuron counts, stages and ages; protosyllable participation; latency shift from subsong to later stages; bird 1's protosequence; the decrease of shared neurons across birds; B/D sharing in bird 1; HVCRA and HVCX alike; most-probable IBI of shared and specific neurons | Reproduced (12) |
| Shared and specific neurons of bird 1 (62 to 72 dph) | Reproduced, resting on a rule standing in for the paper's visual window adjustment |
| Locking and rhythm rising through development; rhythmic protosyllable-stage neurons; protosequence latencies; coverage; simultaneous pairs; latency correlations of bird 1; shared fractions in birds 1 and 2; totals over all pairs; skipping cycles; bird 2 before beta; bias | Partially reproduced (14) |
| Subsong locking (19 of 39); bout-related counts; latency correlations of the other pairs; bird 4's protosyllable-stage rhythms | Not reproduced (4) |
| Burst width against adults (adult neurons missing); bird 3's phase analysis and the motif strategy (bird 3's labels missing); acoustic differences (Sound Analysis Pro) | Blocked (4) |
| Model (8 claims) | 7 reproduced, 1 partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons, readings and differences from the paper's method, is
[`attempts/okubo-2015-01.yaml`](../../attempts/okubo-2015-01.yaml).

- `reproduce_okubo_2015.ipynb`: the analysis, about 16 minutes; most of it is the surrogate tests of rhythmicity
  for every neuron, run in 4 processes.
- `hvc.py`: loading the analysis files and the neuron list from the public bucket, and the measures of the
  Methods (syllable and bout locking, rhythmicity, shared and specific neurons, protosyllables, coverage).
- `hvcmodel.py`: the network model of the paper's Supplementary Information, ported from MATLAB.
