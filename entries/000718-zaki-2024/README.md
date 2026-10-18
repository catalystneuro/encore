# Zaki et al. (2024) from dandiset 000718

Tests the findings of [Zaki et al. (2024)](https://doi.org/10.1038/s41586-024-08168-4) that can be
tested on [DANDI:000718](https://dandiarchive.org/dandiset/000718/0.260825.1902). The dandiset holds
two of the nine mice of the paper's calcium imaging and EEG/EMG experiment (Figure 5), Ca_EEG2-1
(high shock) and Ca_EEG3-4 (low shock), with their encoding and recall sessions, the first 10 min
offline recording after encoding, and cell registration for Ca_EEG2-1 only. The mice of the one-hour
offline, behaviour-only, inhibitory tagging and no-shock experiments are not in it.

| Claim | Outcome |
|---|---|
| The deposited mice match the paper's per-mouse freezing (source data) | Reproduced |
| The high-shock mouse freezes more than the low-shock mouse in aversive recall | Reproduced |
| Offline bursts are more frequent than in shuffled activity | Blocked: methods underspecified |
| Offline population activity is more skewed than shuffled activity | Reproduced |
| Movement pauses around offline bursts | Not reproduced |
| Overlap-neutral exceeds overlap-aversive co-bursting in wake after a high shock | Partially reproduced |
| Behaviour-only experiments (five claims) | Blocked: data missing |
| One-hour offline and single-experience experiments (nine claims) | Blocked: data missing |
| Inhibitory tagging and no-shock experiments (two claims) | Blocked: data missing |
| EEG cohort claims needing missing mice, sessions or registration (four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000718-zaki-2024-01.yaml`](../../attempts/000718-zaki-2024-01.yaml).

- `reproduce_zaki_2024.ipynb`: the analysis. It takes about two minutes, most of it streaming the
  files.
- `memlink.py`: loading the session, Week and registration data, freezing, burst detection,
  ensembles, co-participation, circular-shift surrogates and time-shift decoding. Other notebooks
  on this dandiset can import it.
