# Powell, Haddad, Gorur-Shandilya & Marder (2021) from Zenodo record 3924718

Tests the findings of [Powell et al. (2021)](https://doi.org/10.7554/elife.60454) that can be tested
on [ZENODO:3924718](https://zenodo.org/records/3924718), which holds `evoked_data.mat` (spike times of
PD, LG and DG, saline temperature and a stimulation mask for the ten preparations in which gastric
mill rhythms were evoked) and zips of raw recordings. The spontaneous recordings (Figure 2) and the
recordings with the pyloric pacemaker hyperpolarized (Figure 4, figure supplement 2) are not in the
record.

| Claim | Outcome |
|---|---|
| Spontaneous gastric mill activity from 11 to 30 C in nine preparations | Blocked: data missing |
| Spontaneous rhythms less regular at high temperature (Figure 2a) | Blocked: data missing |
| Rhythms evoked from 7 to 21 C in 9 of 10 preparations | Reproduced (9 of 10; 8 if 21 C is required) |
| Spontaneous and evoked rhythms similar in three of four preparations | Not reproduced (1 of 3 testable) |
| PD and LG periods decrease with temperature in all 10 preparations | Reproduced |
| Q10 of about 2 for both rhythms in 8 of 10 preparations | Not reproduced |
| PD and LG Q10s do not differ (paired t-test) | Reproduced |
| The evoked rhythm slows with time since stimulation | Reproduced |
| Gastric mill period falls with temperature with the pacemaker hyperpolarized | Blocked: data missing |
| Rhythm counts with the pacemaker active and hyperpolarized | Blocked: data missing |
| Example LG/PD period ratios of about 10 and 11 (Figure 5a) | Reproduced |
| LG and PD integer-coupled from 7 to 21 C | Reproduced |
| DG and PD not integer-coupled | Reproduced |
| Integer-coupling area larger for LG than DG; DG overlaps shuffled | Partially reproduced |
| LG/PD ratio independent of temperature | Reproduced |
| LG/PD ratios from about 5 to 25 at low temperature | Not reproduced |
| LG burst starts phase-locked to PD (Rayleigh test) | Partially reproduced |
| Counts of LG and DG burst starts in the phase analysis | Partially reproduced |
| LG starts at a PD phase of about 0.5, without trend | Partially reproduced |
| LG spiking drops near the end of the PD burst at high temperature | Not reproduced |
| DG burst starts not phase-locked to PD | Reproduced |
| DG spiking does not drop near the end of the PD burst | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Bursts follow the Methods (at least 5 spikes for LG and DG, 2 for PD). The paper's code counts
inter-spike intervals, one spike more, and is shown as a variant throughout; with it and the code's
computations, several reported numbers are matched exactly (the Q10 t-test, the 3799 cycles and
Spearman p of Figure 5f, the phase trend of Figure 6b, the 3816 LG burst starts). The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/powell-2021-01.yaml`](../../attempts/powell-2021-01.yaml).

- `reproduce_powell_2021.ipynb`: the analysis. It runs in one to two minutes (the time is printed at the end);
  fetching and reading `evoked_data.mat` (73 MB) from Zenodo took 14 to 61 s in five runs (printed
  in the first cell).
- `stg.py`: loading `evoked_data.mat` (including its MATLAB categorical fields), burst detection as
  crabsort's `computePeriods`, and the paper's measures of Q10, integer coupling, PD phase, the
  Rayleigh test and the slowing after stimulation. Other notebooks on this record can import it.
