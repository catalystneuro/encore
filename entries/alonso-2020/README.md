# Alonso and Marder (2020) from Dryad m31b1h7

Tests the findings of [Alonso and Marder (2020)](https://doi.org/10.7554/eLife.55470) on
[Dryad m31b1h7](https://doi.org/10.5061/dryad.m31b1h7) (version id 94811), which holds the
authors' Java model of a three-cell pyloric network, their Python scripts and the parameters of
38 temperature-compensated models. The paper has no recordings: every claim is tested by
simulating the deposited models with a port of the deposited Java (`pyloric.py`), which matches the
Java to 3e-9 mV over 3 s at 18 C and to 0.06 mV over 3 s at 25 C.

| Claim | Outcome |
|---|---|
| The deposit holds the paper's models, which give a 1 Hz rhythm at 10 C | Not reproduced |
| Figure 1: frequency Q10 near 2, duty cycles and phases constant | Partially reproduced |
| Figure 1, supplement 1: three more models | Not reproduced |
| All 36 models compensated over 10 to 25 C | Partially reproduced |
| 2 in 40 solutions failed between control temperatures | Blocked: data missing |
| Figure 1, supplement 2: largest ISI falls along a ramp | Reproduced |
| Figure 1, supplement 3: LP duty-cycle distributions differ across models | Reproduced, on the variant reading (fixed temperatures) |
| Figure 2: LP spike amplitude falls and threshold depolarizes | Reproduced, resting on an assumed rule for reading the threshold |
| Figure 2, supplement 1: peak voltage falls, rises or stays | Reproduced |
| Figure 3: current amplitudes at two temperatures | Partially reproduced |
| Figure 4: currentscapes reorganize | Not reproduced |
| Na and Kd drive spikes; H and synaptic currents dominate at the trough | Reproduced |
| Figure 5: A to KCa trade-off after the PD burst | Reproduced |
| Figure 6: two models crash with loss of PD activity | Not reproduced |
| Figure 6, supplement 1: crashes by different mechanisms | Not reproduced; blocked (data missing) proposed, as the missing model could make it partial |
| Figure 7: slow time scales at high temperature | Blocked: data missing |
| Figure 8A: hysteresis of PD quiescence | Reproduced |
| 34 of 36 models similar on up and down ramps | Blocked: too large |
| Figure 8B: pathological attractor | Not reproduced |
| Figure 9A: removing IA at 10 and 25 C | Partially reproduced |
| Figure 9B: removing IKCa at 10 and 25 C | Reproduced |
| Figure 10A: graded removal in one model | Partially reproduced |
| Figure 10B: complete removal across models | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The deposit holds 38 models where the paper says 36; four models the Methods name are absent and
three are filed under other spellings, and one is matched at the character the paper's text cannot
render. The attempt record, with the reasons and the differences from
the paper's method, is [`attempts/alonso-2020-01.yaml`](../../attempts/alonso-2020-01.yaml).

- `reproduce_alonso_2020.ipynb`: the data check and most claims, at fixed temperatures (about 30
  min).
- `ramps.ipynb`: the claims on temperature ramps (about 50 min).
- `voltage_distributions.ipynb`: the membrane potential distributions of Figure 2 (about 20 min).
- `pyloric.py`: loading the deposit, the port of the model, the classification scheme of the
  Methods and the current shares. Other notebooks on this dataset can import it.
