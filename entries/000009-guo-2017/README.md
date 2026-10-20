# Guo, Inagaki, Daie, Druckmann, Gerfen & Svoboda (2017) from dandiset 000009

Tests the findings of [Guo et al. (2017)](https://doi.org/10.1038/nature22324) that can be tested
on [DANDI:000009](https://dandiarchive.org/dandiset/000009/0.220126.1903): 137 silicon-probe
sessions in ALM, thalamus and SNr during a delayed licking task with optogenetic photoinhibition,
and 36 whole-cell recordings of ALM neurons during thalamus, M1 or contralateral ALM
photoinhibition.

| Claim | Outcome |
|---|---|
| Behaviour: 77.6% correct, 10.3% lick early, 1.1% no response | Partially reproduced |
| ALM photoinhibition biases licking to the ipsilateral side (Fig. 1c) | Reproduced |
| Thalamus photoinhibition in VGAT mice reduces activity 0.5 to 1.1 mm from the fibre to 15.9% | Reproduced |
| ALM and thalamic unit classes by spike width | Partially reproduced (2 claims) |
| 70% of ALM pyramidal neurons selective; selectivity types (Fig. 2e) | Partially reproduced |
| Equal numbers of contra- and ipsi-preferring ALM neurons | Reproduced |
| VM/VAL selectivity like ALM (Fig. 2f) | Partially reproduced |
| Thalamus photoinhibition collapses ALM activity (Fig. 3c) and silences thalamus (Fig. 3f) | Partially reproduced (2 claims) |
| Onsets: thalamus 2.5 ms, ALM 8.2 ms | Reproduced |
| ALM photoinhibition reduces VM/VAL activity to 25% (Fig. 6c) | Not reproduced |
| Unmodulated VM/VAL neurons less selective; localization to VM/VAL | Partially reproduced (2 claims) |
| SNr response to ALM photoinhibition | Partially reproduced |
| Onsets after ALM photoinhibition (Fig. 6e) | Not reproduced |
| Selectivity time course in ALM and VM/VAL | Reproduced |
| ALM Vm 12.7 mV below threshold | Not reproduced |
| ALM Vm hyperpolarized by 18.7 mV under thalamus photoinhibition; small effect of M1 photoinhibition | Partially reproduced (2 claims) |
| Small Vm effect of contralateral ALM photoinhibition; thalamus drives ALM more strongly than cortex | Reproduced (2 claims) |
| Equal inhibition across selectivity types; all cortical layers (3 claims) | Blocked: methods underspecified |
| vM1 photoinhibition | Blocked: metadata insufficient |
| Gad2 optrode reduction | Blocked: metadata insufficient |
| Behaviour under thalamus photoinhibition, muscimol, weak photoinhibition (Fig. 5), current injection, M1 and Olig3 recordings, SNr rates, anatomy (10 claims) | Blocked: data missing |
| Latency and network models (2 claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The dandiset holds 966 of the paper's 1214 ALM units, nearly all its thalamic units and its 181
putative GABAergic SNr units. Its mean waveforms are too short to measure the spike widths the
Methods classify by, so unit classes are run both by computed width and by the files' own labels (and, for the
thalamic claims of Fig. 2 and 6, with all units).
Spikes are stored only in the first 5 s or so of each trial, and most units hold spikes over only
part of their session. The whole-cell files record no photostimulus time; the effect of photoinhibition
starts about 0.19 s after one onset their trial times allow (E) and just before the other (M), and
the whole-cell claims hold under M only. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/000009-guo-2017-01.yaml`](../../attempts/000009-guo-2017-01.yaml).

- `reproduce_guo_2017.ipynb`: the analysis. It takes about ten minutes, most of it streaming the
  whole-cell files (12.7 GB).
- `loop.py`: loading the extracellular sessions and whole-cell recordings, the epoch and
  photostimulus conventions of the claims file, per-unit selectivity and photoinhibition measures,
  onset detection and spike clipping. Other notebooks on this dandiset can import it.
