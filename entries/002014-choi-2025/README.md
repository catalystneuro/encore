# Choi et al. (2025) from dandiset 002014

Tests the findings of [Choi et al. (2025)](https://doi.org/10.1016/j.jneumeth.2025.110467) that can be tested on
[DANDI:002014](https://dandiarchive.org/dandiset/002014/0.261012.0921), which holds one session of monkey T
recorded through the paper's semi-sealed chamber (Figures 8 and 9). The surgical, culture, drainage and
electrode-yield results, and monkey J, are not in it.

| Claim | Outcome |
|---|---|
| A single trial's dopamine fluctuates more after the value cue (Figure 8A) | Reproduced (weak test) |
| Dopamine rises more for large than small reward trials (Figure 8B) | Reproduced |
| Spikes at c5d aligned to the value cue (Figure 9A) | Reproduced, after correcting the spike clock |
| Waveform and interspike intervals of the c5d unit (Figure 9B, C) | Reproduced by the criterion (weak evidence for a single unit) |
| Beta power is suppressed more after large reward cues (Figure 9D) | Partially reproduced |
| Recordings in two monkeys; electrode yields; cultures; drainage; bone growth (eight claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The raw ephys and the spike times in the file are not on the clock of the trials and events: they start at 0 s,
and the data put them 11812.11 s later. The notebook measures the offset from the data and corrects for it.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/002014-choi-2025-01.yaml`](../../attempts/002014-choi-2025-01.yaml).

- `reproduce_choi_2025.ipynb`: the analysis. It takes about two minutes, most of it streaming the file.
- `chamber.py`: loading the file, the trial classes, the clock checks and the measures. Other notebooks on this
  dandiset can import it.
