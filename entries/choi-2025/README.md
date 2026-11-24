# Choi et al. (2025) from dandiset 002014

Tests the findings of [Choi et al. (2025)](https://doi.org/10.1016/j.jneumeth.2025.110467) on
[DANDI:002014](https://dandiarchive.org/dandiset/002014/0.261120.0528), one session of monkey T
(09/27/2024), the session of the paper's Figures 8 and 9 (`reproduce_choi_2025.ipynb`). The
paper's lists of large and small successful trials, from its Zenodo record
[14825992](https://doi.org/10.5281/zenodo.14825992), are used to check the trial classes.

| Claim | Outcome |
|---|---|
| Single-trial dopamine fluctuates more after the value cue (Fig. 8A) | Reproduced |
| More dopamine for large than small reward between cue and reward (Fig. 8B) | Reproduced |
| Spikes at c5d aligned to the value cue (Fig. 9A) | Reproduced |
| Spike waveform and interspike intervals of a single unit (Fig. 9B, C) | Reproduced |
| Beta power suppressed more after large than small reward cues (Fig. 9D) | Partially reproduced (p = 0.109) |
| Recordings in two monkeys; electrode yields; cultures; drainage; bone growth | Blocked: not in the dandiset |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/choi-2025-02.yaml`](../../attempts/choi-2025-02.yaml).
