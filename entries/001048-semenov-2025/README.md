# Semenov, Kim, Silkuniene & Pakhomov (2025) from the dandisets it names

Tests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660).
[DANDI:001048](https://dandiarchive.org/dandiset/001048/0.250701.1624) names the paper but holds
HEK-cell recordings of another study, so the claims are tested on the dandisets the paper's Data and
code availability lists (001030 and 001032 to 001035, 001271 to 001274; 001031 holds a stimulus the
paper does not describe and is not used, and 001034, a copy of 001032, serves only to show that it is
a copy): optical recordings of rat
hippocampal neurons stimulated by 2- and 20-kHz sine waves, unmodulated or modulated at 20 Hz, with
TTX and Di-8-ANEPPS controls, and strobe images of membrane charging by pulses and sine waves.

| Claim | Outcome |
|---|---|
| APs above 5% dF, typically 11.3% high and 8 ms long | Partially reproduced |
| Pure 2- and 20-kHz waves excite every neuron, with latencies of 100 to 200 ms and rates up to 60 to 90 Hz | Partially reproduced |
| Excitation block at the highest fields | Not reproduced |
| 20-kHz thresholds about twice the 2-kHz ones | Blocked: metadata insufficient (voltages not calibrated per frequency) |
| 5-AP thresholds above 1-AP thresholds | Reproduced |
| Modulated thresholds higher than pure ones; 57.7 V/cm at 2 kHz | Partially reproduced (rests on the crop ROI) |
| Modulated waves lock firing to the beats, no sustained depolarization | Reproduced |
| Pure waves give more APs than modulated ones in the same neuron | Reproduced |
| Low conductivity halves thresholds; extrapolation to 7 V/cm | Blocked: data not deposited |
| Heating calculation | Blocked: methods underspecified |
| 2-s ramped waves: firing for the whole wave, then block | Partially reproduced |
| Di-8-ANEPPS gives the same responses | Partially reproduced (3 of 8 neurons deposited) |
| TTX abolishes APs and depolarization | Partially reproduced |
| Charging time constants of 0.65 to 0.91 us | Blocked: metadata insufficient (no ROIs, experiments not identifiable) |
| Orientation and pole effects on charging | Blocked: metadata insufficient |
| Figure 5 and S3 cells (asymmetry, whole-cell depolarization) | Blocked: metadata insufficient |
| Sine sensitivity below pulse sensitivity, 42% of it | Partially reproduced (a change to blocked, metadata insufficient, is proposed) |
| Threshold depolarization of 6.8 mV | Blocked: metadata insufficient (voltages not calibrated) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The dandisets hold generator voltages, not calibrated fields, no ROIs and no stimulus waveforms, and
001034 is a copy of 001032. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001048-semenov-2025-01.yaml`](../../attempts/001048-semenov-2025-01.yaml).

- `reproduce_semenov_2025.ipynb`: the analysis. It takes about 40 minutes, most of it streaming the
  strobe images of 001273 and 001274.
- `tisine.py`: loading the dandisets, the soma traces, AP detection, thresholds, and the strobe ROIs
  and fits. Other notebooks on these dandisets can import it.
