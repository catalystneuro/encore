# Burman, Brodersen, Raimondo, Sen & Akerman (2023) on dandiset 000458

Tests the findings of [Burman et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.005) that can
be tested on [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), the Allen
Institute Neuropixels recordings with cortical electrical stimulation, awake and under isoflurane,
that the paper reuses (Figure 4A to 4D, Figure S6), and runs the paper's network model (Figure 4E
to 4H, Figure S7). The paper's gramicidin patch-clamp recordings (Figures 1 to 3) are not in the
dandiset nor deposited anywhere.

| Claim | Outcome |
|---|---|
| The 17 sessions the paper's code reads are in the dandiset with the fields it uses | Reproduced |
| 662 neurons kept and 203 excluded, from 17 recordings in 16 mice | Partially reproduced |
| Synchrony lower awake (0.325 against 0.393) | Partially reproduced |
| Entropy higher awake (1.347 against 1.111 nats) | Partially reproduced |
| Evoked firing rate higher awake | Reproduced |
| Synchrony and entropy differences remain with firing rate regressed out | Reproduced |
| Model: hyperpolarizing E_GABA gives less activity | Reproduced |
| Model: synchrony lower with shunting E_GABA (0.784 against 0.881) | Partially reproduced |
| Model: entropy higher with shunting E_GABA (0.451 against 0.197 nats) | Partially reproduced |
| Model: shunting networks decoded more accurately | Reproduced |
| Multi-compartment model of Figure S4 | Blocked: methods underspecified |
| Patch-clamp findings of Figures 1 to 3 and S1 to S5 (24 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The three partial outcomes on the dandiset come from the evoked rate used to exclude neurons. The
claims are judged under the Methods' rate, a spike count; under the rate the paper's own code
computes, which sums spike latencies, the dandiset gives the paper's numbers exactly. The two
partial model outcomes are hyperpolarizing means 0.001 to 0.002 outside tolerances narrower than
the spread between runs. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/burman-2023-01.yaml`](../../attempts/burman-2023-01.yaml).

- `reproduce_burman_2023.ipynb`: the Neuropixels claims. About two minutes, most of it streaming the
  units and trials of 24 files.
- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 20 minutes.
- `npx.py`: loading the dandiset and the per-unit measures (rate, entropy, synchrony) of the paper's
  code. Other notebooks on this dandiset can import it.
- `network.py`: the paper's Brian 2 network, transcribed from its simulation code.
