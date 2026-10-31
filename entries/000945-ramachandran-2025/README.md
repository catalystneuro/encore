# Ramachandran, Gao, Yttri, Yu & He (2025) from dandiset 000945

Tests the findings of [Ramachandran et al. (2025)](https://doi.org/10.1088/1741-2552/adbb1f) on
[DANDI:000945](https://dandiarchive.org/dandiset/000945/0.250213.2212), the version the paper
cites. The dandiset holds the sorted units and trial times of awake and anesthetized recordings in
rat S1 during transcranial focused ultrasound at five pulse repetition frequencies (PRF) and three
duty cycles (DC), with a cell-type label (RSU or FSU) in most files.

| Claim | Outcome |
|---|---|
| Units sort into 28 FSU and 32 RSU in one animal (Figure 3B) | Blocked: data missing (no waveforms) |
| RSU respond during stimulation in both states, against sham (Figure 4) | Blocked: data missing |
| FSU delayed onsets are later awake than anesthetized (Figure 4H, 4I) | Not reproduced |
| Awake onset latencies are more spread (Figure 4H) | Blocked: methods underspecified |
| Awake RSU time-locked responses by PRF (Figure 5A) | Not reproduced |
| Anesthetized RSU time-locked responses by PRF (Figure 5C) | Not reproduced |
| Anesthesia lowers RSU time-locked responses (two-way ANOVA) | Not reproduced |
| FSU time-locked responses do not depend on PRF (Figure 5B, 5D) | Not reproduced |
| Awake RSU delayed responses peak at 1500 and 3000 Hz (Figure 5E) | Blocked: data missing (no sham) |
| Awake FSU delayed responses peak at 4500 Hz (Figure 5F) | Not reproduced |
| Anesthetized delayed responses depend on PRF (Figure 5G, 5H) | Not reproduced |
| Anesthesia lowers delayed responses (two-way ANOVA) | Reproduced, on an assumption |
| Time-adjacent second batch (Figure 6A to 6D) | Blocked: data missing |
| RSU responses rise with ISPTA, then fall (Figure 6E, 6G) | Blocked: methods underspecified |
| FSU delayed responses rise linearly with ISPTA (Figure 6F, 6H) | Not reproduced |
| 1500 Hz gives the highest RSU time-locked mean (Figure 5A) | Not reproduced |
| RSU time-locked responses by DC (Figure 7A) | Blocked: data missing (no 30% DC recordings, no sham) |
| 60% DC gives the highest RSU time-locked mean (Figure 7A) | Not reproduced |
| FSU show no time-locked response across DC (Figure 7B) | Not reproduced |
| RSU delayed responses prefer 30% DC (Figure 7C) | Blocked: data missing (no 30% DC recordings) |
| FSU delayed responses higher at 60% than 6% DC (Figure 7D) | Partially reproduced (sham part untested) |
| The off-target sham gives no response | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds part of the paper's data: the awake PRF series of seven rats, labelled
anesthetized recordings of two, and 6% and 60% DC recordings of three; no sham, no second batch,
no 30% DC recordings and no waveforms. Eleven files are second copies of other recordings, and
the `_2` suffix of the repeat recordings does not always mark the later one. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000945-ramachandran-2025-01.yaml`](../../attempts/000945-ramachandran-2025-01.yaml).

- `reproduce_ramachandran_2025.ipynb`: the analysis. It takes about two minutes, most of it
  streaming the files.
- `tfus.py`: loading the files, parsing the condition from the identifier, finding duplicate
  deposits, and the paper's response, group-test and latency measures. Other notebooks on this
  dandiset can import it.
