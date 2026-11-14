# Danish, Aronov & Fee (2017) from CRCNS aa-3

Tests the findings of [Danish et al. (2017)](https://doi.org/10.1371/journal.pone.0169568) that can
be tested on [CRCNS aa-3](https://doi.org/10.6080/K0GQ6VP4): song from 7 zebra finches before and
after bilateral Uva lesions, with the authors' segmentations, and multiunit recordings in Uva
during singing from 3 of the paper's 5 recorded birds. Control lesions, directed song, sorted
single units and GTE times are not in the data set.

| Claim | Outcome |
|---|---|
| Lesioned birds sing at rates similar to intact birds | Not reproduced |
| Maturity index falls from 0.26 to 0.08 | Reproduced (assumption) |
| Syllable durations closer to exponential (Gamma 16 to 3.7) | Partially reproduced |
| Small syllable-duration peak at 50 to 100 ms in 6 of 7 birds | Partially reproduced |
| Gap durations broader after lesion | Reproduced |
| Song rhythmicity R falls from 3.30 to 1.7 | Partially reproduced |
| Residual 3 to 8 Hz rhythm in 6 of 7 lesioned birds | Partially reproduced |
| Uva activity before calls and introductory notes (Fig 4B, 4C) | Partially reproduced |
| Uva activity elevated during song | Reproduced (assumption) |
| Consistency across renditions and sites (Fig 5) | Partially reproduced |
| Peak before syllable onset (Fig 6) | Partially reproduced |
| Dip before syllable offset (Fig 6) | Reproduced (assumption) |
| Correlation with song amplitude, 42 ms lead (Fig 7A) | Reproduced (assumption) |
| Spectral peaks near 9 Hz (Fig 7B) | Partially reproduced |
| Coherence with amplitude at 8.8 Hz (Fig 7D) | Reproduced (assumption) |
| Fast oscillations in long syllables (Fig 9) | Not reproduced |
| Suppression for about 200 ms after bouts | Not reproduced |
| Little activation at motif and bout boundaries | Not reproduced |
| Directed song, control lesions, single units | Blocked: data missing |
| Antidromic responses, spectral features | Blocked: not attempted in the run's time |
| GTE analysis | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Each recording has three neural channels and the data set does not say which one is the Uva
electrode; the electrophysiology outcomes rest on the channel chosen for each bird. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/danish-2017-01.yaml`](../../attempts/danish-2017-01.yaml).

- `reproduce_danish_2017.ipynb`: the analysis. It takes about half an hour, most of it streaming
  and reducing the two archives (9.4 GB).
- `uva.py`: reading the archives (the .dat format of the recordings, the analysis files and the
  spreadsheets), MUA and sound amplitude, the maturity index, Gamma, the song rhythm spectrum and
  multitaper coherence. Other notebooks on this data set can import it.
