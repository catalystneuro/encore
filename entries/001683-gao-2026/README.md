# Gao, Frake, Durand & He (2026) from dandiset 001683

Tests the findings of [Gao et al. (2026)](https://doi.org/10.1109/tnsre.2025.3644273) on
[DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), which holds the EEG and
seizure labels of 16 rats with 4-AP seizures (10 given focused ultrasound to the corpus callosum,
6 sham), and the evoked-potential and EEG recordings of the wild-type phase of 23 rats.

| Claim | Outcome |
|---|---|
| Sham seizure duration does not change across blocks (Fig. 2C) | Not reproduced |
| Most sham seizures last under 2 minutes (Fig. 2D) | Reproduced |
| Sham seizure count does not change (Fig. 2E) | Reproduced |
| Sham percent time in seizure differs at post 3 (Fig. 2F) | Reproduced, on assumptions |
| tFUS reduces seizure count by 9 to 42% (Fig. 3A) | Reproduced |
| Seizure count differs between sham and tFUS at post 1 and 2 (Fig. 3A) | Partially reproduced |
| tFUS reduces percent time in seizure by 33 to 55% (Fig. 3B) | Reproduced |
| Sham percent time does not change (Fig. 3B) | Not reproduced, on an assumption |
| Percent time differs between sham and tFUS (Fig. 3B) | Not reproduced |
| tFUS lengthens the inter-seizure interval by 27 to 52% (Fig. 3C) | Reproduced, on an assumption |
| Interval differs between sham and tFUS at post 1 (Fig. 3C) | Partially reproduced |
| Seizure duration falls significantly only at tFUS post 2 (Fig. 3D) | Not reproduced |
| No change in theta, alpha, gamma power (Fig. 4) | Not reproduced, on an assumption |
| Beta power falls during and after tFUS (Fig. 4C) | Partially reproduced |
| Sham band power does not change (Fig. S4) | Not reproduced, on an assumption |
| Normalized AI rises with tFUS and differs from sham (Fig. 4E-H) | Partially reproduced |
| Seizures lower the AI (Fig. S5) | Reproduced, on assumptions |
| Seizure PLI of S1 falls with tFUS (Fig. 6) | Not reproduced |
| Seizure PLI change, S1 against non-S1 (Fig. S7) | Partially reproduced, on an assumption |
| tFUS evokes potentials in S1 (Fig. 5B) | Blocked: methods underspecified |
| Wild-type gamma PLI falls with tFUS (Fig. 5C-F, J) | Blocked: data missing |
| Wild-type low-band PLI falls only in S1 (Fig. 5G-I) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The seizure labels in the dandiset give the paper's percent changes of Fig. 3 to within one point.
Their times are in minutes, not seconds. The significance pattern of Fig. 3 appears only under a
repeated-measures reading of the paper's "two-way ANOVA", which this attempt adopts as an
assumption. The EEG before the first 4-AP injection is there for 13 of the 16 rats, as recordings
with tFUS pulses (the PLV files), and is read between the pulses. The resting EEG of the wild-type
phase is not in the dandiset.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001683-gao-2026-01.yaml`](../../attempts/001683-gao-2026-01.yaml).

- `seizure_metrics.ipynb`: seizure count, percent time, interval and duration from the labels (about
  a minute).
- `eeg_blocks.ipynb`: band power, asymmetry index and seizure PLI; streams all 70 EEG blocks
  (205 GB) once, in about 25 minutes with four processes.
- `wild_type.ipynb`: the evoked potentials of the target confirmation and the PLI of the wild-type
  EEG (about 12 minutes).
- `tfus.py`: loading (parallel range reads of the unchunked NWB arrays), block assignment, seizure
  metrics, spectra, PLI and the two-way ANOVA readings. Other notebooks on this dandiset can import
  it.
