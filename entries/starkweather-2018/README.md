# Starkweather, Gershman & Uchida (2018) from CRCNS vta-1

Tests the findings of [Starkweather et al. (2018)](https://doi.org/10.1016/j.neuron.2018.03.036)
that can be tested on [CRCNS vta-1](http://dx.doi.org/10.6080/K01J97X6), which holds the spike
times of 172 light-identified VTA dopamine neurons, with odor and reward times and trial types, in
two classical conditioning tasks after saline or SalB injection. The licks, free water deliveries,
mPFC recordings and other VTA neurons the paper also analyses are not in it.

| Claim | Outcome |
|---|---|
| Post-reward responses fall with ISI in task 1 and rise in task 2 under saline (Figure 4A, 4B) | Reproduced |
| Odor C responses are below odor A responses at the same 2.8 s ISI (Figure 4B) | Reproduced |
| Pre-reward responses fall with time in both tasks, under saline and SalB | Reproduced |
| SalB spares the task 1 pattern and flattens the task 2 pattern (Figure 4C, 4D) | Reproduced |
| Slopes of single neurons: signs, significant slopes, distributions, variances (Figures 4E, 5) | Reproduced; two rest on an assumption about baseline subtraction |
| Odor B and C responses and omission dips are spared by SalB (Figures 6, S5D) | Reproduced |
| Belief state TD model, intact, belief impaired and timing impaired (Figure 7) | Reproduced, with the code ported to Python; under the timing impairment the omission dips are reduced, not removed, which the criterion allows (asked of a reader) |
| mPFC recordings, licks, unidentified VTA neurons, free water responses, no-KORD controls (12 claims) | Blocked: data missing |

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/starkweather-2018-01.yaml`](../../attempts/starkweather-2018-01.yaml).

- `reproduce_starkweather_2018.ipynb`: the analysis. The last run took 267 s (printed at its end);
  the data are one zip, and most of the time is the model.
- `vta.py`: loading the zip from the CRCNS bucket, the trial table and the response measures of the
  paper's Methods. Other notebooks on this data set can import it.
- `belief_td.py`: a Python port of the paper's belief state TD model code (commit d667730).
