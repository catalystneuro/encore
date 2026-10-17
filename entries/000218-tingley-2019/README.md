# Tingley & Buzsaki (2019) from dandiset 000218

Tests the findings of [Tingley and Buzsaki (2019)](https://doi.org/10.1016/j.neuron.2019.10.012) that
can be tested on [DANDI:000218](https://dandiarchive.org/dandiset/000218/0.250624.0439), which holds
the LFP, sorted units, sleep states and trials of simultaneous lateral septum (LS) and hippocampal
recordings in 6 rats. The files hold no detected events, so LS high-frequency oscillations (HFOs)
and CA1 ripples are detected here from the LFP. The optogenetic experiments of Figure 6 are not in
the dandiset.

| Claim | Outcome |
|---|---|
| 6 rats, 1989 LS neurons, 37 CA1+LS and 25 CA3+LS recordings | Partially reproduced |
| HFOs with increased LS firing in each of 6 animals | Not reproduced |
| 29,955 HFOs | Reproduced |
| 16% of LS neurons per HFO, 0.23 spikes per event | Not reproduced |
| 92% of LS neurons phase-locked, at the trough | Partially reproduced |
| LS HFOs shorter than CA1 ripples | Reproduced |
| LS HFOs slower than CA1 ripples | Not reproduced |
| No amplitude-frequency correlation | Not reproduced |
| HFOs confined to LS | Not reproduced |
| HFO excess correlation PRE = POST | Reproduced |
| HFO excess correlation above BEHAV and jitter | Reproduced |
| Compression up to 20-fold | Not reproduced |
| Rates rise in post-behavior NREM in CA1, CA3 and LS | Partially reproduced |
| HFOs mostly in NREM, rarer than ripples | Partially reproduced |
| CA1 leads LS by 6.4 ms | Not reproduced |
| Coupling 0.3 in NREM against 0.15 in WAKE | Not reproduced |
| Ripple-triggered LS firing higher in NREM | Not reproduced |
| CA1-LS phase coherence at chance | Not reproduced |
| Ripple features predict LS firing (CA1 spikes, state, duration) | Partially reproduced (3 claims) |
| Depth profile, travelling waves | Blocked: metadata insufficient |
| Per-session pair results (Figure 4B sessions, 4C) | Blocked: too few recordings after selection |
| Optogenetics; CA1 depth feature | Blocked: data missing |
| Replay and seqNMF features, and the comparison that uses them | Blocked: methods underspecified |
| Network model (Figure 8) | Blocked: other (a simulation) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper does not say which channels it used for detection, and its code repository holds no
analysis of this paper apart from the model of Figure 8, so the detected events are this
attempt's own. LS firing at them exceeds firing at random times, or before and after the events,
by more than 3 SEM in only one animal of six, and a third of the events coupled to CA1 ripples fall on
the same sample as the ripple; most outcomes on HFOs follow from that. Detecting
the events again on the LS channel re-referenced within its shank removes most same-sample events
but changes no outcome. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/000218-tingley-2019-01.yaml`](../../attempts/000218-tingley-2019-01.yaml).

- `reproduce_tingley_2019.ipynb`: the analysis. It takes about 18 minutes, most of it streaming the
  files: each file's chunk index has to be loaded over the network before a channel can be read.
- `ls_hfo.py`: loading, fast parallel reading of single LFP channels, the HFO and ripple detector,
  phase locking and the spike measures. Other notebooks on this dandiset can import it.
