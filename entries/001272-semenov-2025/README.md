# Semenov, Kim, Silkuniene & Pakhomov (2025) from dandiset 001272 and the paper's other deposits

Tests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660) on
[DANDI:001272](https://dandiarchive.org/dandiset/001272/0.250805.1358), which holds the Di-8-ANEPPS
control recordings of Figure S1: 3 neurons stimulated with 250-ms, 2-kHz sine waves, where the paper
reports 8. The paper's FluoVolt findings are tested on its other deposits, DANDI:001032, 001033 and
001035 (Figures 1 and 2), 001030 (Figure 3C) and 001271 (Figure S2). The 2-kHz unmodulated files of
DANDI:001034 duplicate those of 001032. The strobe images of DANDI:001273 (Figure 4) are fitted without the debris ROI the paper
scaled them to, which is not deposited, as the claims file allows.

| Claim | Data | Outcome |
|---|---|---|
| Di-8-ANEPPS experiments on eight neurons | 001272 | Not reproduced (3 neurons) |
| Di-8-ANEPPS APs are reductions of emission | 001272 | Reproduced |
| Near threshold, one or a few delayed APs | 001272 | Partially reproduced (assumption); not reproduced proposed |
| Stronger fields shorten the delay and induce sustained firing | 001272 | Reproduced (assumption) |
| The strongest fields give sustained depolarization | 001272 | Not reproduced |
| Di-8-ANEPPS traces are noisier than FluoVolt | 001272 with FluoVolt neurons | Not reproduced |
| Effects do not differ from FluoVolt | 001272 with FluoVolt neurons | Partially reproduced (assumption) |
| Pure sine waves excite all neurons, ceiling 60 to 90 Hz, delay 100 to 200 ms | 001032, 001033, 001035 | Not reproduced |
| 20 kHz needs about twice the field of 2 kHz | 001032, 001033, 001035 | Not reproduced |
| Modulated thresholds are higher | 001032, 001033, 001035 | Not reproduced |
| Modulated waves lock firing to the beats | 001032, 001033, 001035 | Partially reproduced (assumption) |
| Pure sine waves evoke more APs than modulated ones | 001032, 001033, 001035 | Reproduced |
| Low conductivity halves thresholds | none | Blocked: not deposited |
| 2-s sine waves evoke sustained firing, then a block | 001030 | Partially reproduced (assumption) |
| Tetrodotoxin abolishes APs and sustained depolarization | 001271 | Reproduced (assumption) |
| Pooled membrane charging time constants (Figure 4) | 001273 | Not reproduced (unscaled fits) |
| Orientation, pole and discharge effects on the time constants (Figure 4) | 001273 | Blocked: cell shapes not deposited |
| Sine wave against pulse sensitivity (Figure 6) and the threshold estimate | 001274 | Blocked: not attempted in this attempt |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The soma outline, the stimulus onset in the 2024 files and the scale of the stated amplitudes are not
deposited, so several outcomes rest on stated assumptions. APs are detected with a width at half
height of 1 to 20 ms, as the claims file gives it after a reader answered a question on it
([`questions/001272.yaml`](../../questions/001272.yaml)); no outcome differs from those with the
2 to 20 ms first tested. For the Di-8-ANEPPS traces the AP height is read as the peak's prominence,
since read as the dF value it counts noise on the bleaching-raised inverted trace (a null test of the
detector after the stimulus shows it). Thresholds in V/cm, from the files' nominal
volts and 36 V/cm per volt, are about 150 V/cm at 2 kHz, against the paper's 57.7 V/cm; the files say
the delivered amplitude is smaller by a calibration that is not deposited. For the near-threshold claim the
second verification round found that only 1 of 3 neurons passes the claim's per-neuron test under the
adopted readings, and a change to not reproduced is proposed for a third round. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001272-semenov-2025-01.yaml`](../../attempts/001272-semenov-2025-01.yaml).
