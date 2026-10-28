# Tingley, McClain, Kaya, Carpenter & Buzsáki (2021) from dandiset 000233

Tests the findings of [Tingley et al. (2021)](https://doi.org/10.1038/s41586-021-03811-w) that can
be tested on [DANDI:000233](https://dandiarchive.org/dandiset/000233/0.250624.0414), which holds
CA1 LFP, detected SPW-Rs, the glucose sensor current, a head accelerometer and, for six rats, sleep
states, from 25 rats. It holds no spike units, stimulation times, CNO or vehicle labels, meal times
or cohort labels, so the optogenetic, DREADD, fasting and unit findings cannot be tested.

| Claim | Outcome |
|---|---|
| SPW-R rate predicts later glucose decreases (R -0.21 at 10.7 min) | Reproduced, under 3 of 16 readings, resting on an assumption |
| The correlation at 10 min exceeds circular shuffles | Reproduced |
| Clustered SPW-Rs are followed by a larger glucose decrease | Reproduced |
| Interval, amplitude, duration, frequency rank in that order | Partially reproduced |
| Phase dispersion of glucose drops more after higher SPW-R rates | Not reproduced |
| Power-power and phase-power coupling, SPW-R rhythm faster | Partially reproduced |
| Glucose oscillates at about 60 min | Not reproduced |
| Glucose is circadian and rises after meals | Blocked: data missing |
| The sensor current decays over days, its fluctuations do not | Reproduced |
| 9.5 SPW-Rs per minute, about 14,000 a day | Reproduced |
| SPW-Rs are consistent across days | Reproduced |
| SPW-R rate has 24-h and 4-h rhythms (1,568.5 h, 8 rats) | Partially reproduced |
| A 20-ms refractory period between ripples | Not reproduced |
| The correlation does not differ between NREM and waking | Reproduced |
| No hour of the day differs (smallest P = 0.53) | Not reproduced |
| Ventral SPW-Rs correlate less with glucose than dorsal | Blocked: data missing (glucose in one of three rats) |
| Predictor models (Extended Data Fig. 6, three claims) | Blocked: too large |
| Optogenetic stimulation (Figure 3, Extended Data Fig. 7, seven claims) | Blocked: data missing |
| DREADD inhibition of the septum (Figure 4, Extended Data Fig. 10, six claims) | Blocked: metadata insufficient |
| Units and fasting (Extended Data Figs 3e, 4d-f, 8, three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In twelve subjects the glucose timestamps carry dates with day and month swapped; the notebook
repairs them, which adds about 580 h of glucose overlapping the electrophysiology. 27 recordings
are deposited twice. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000233-tingley-2021-01.yaml`](../../attempts/000233-tingley-2021-01.yaml).

- `reproduce_tingley_2021.ipynb`: the analysis. It takes about seven minutes, most of it reading the
  metadata, SPW-R tables and glucose series of the 345 files and the shuffles of the coupling
  analysis.
- `sprglu.py`: loading the files, the repair of the glucose dates, the 5-min binning of SPW-R rate
  and glucose change, cross-correlograms and circular shuffles. Other notebooks on this dandiset
  can import it.
