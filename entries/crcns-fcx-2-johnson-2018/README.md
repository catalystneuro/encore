# Johnson et al. (2018) from CRCNS fcx-2

Tests the findings of [Johnson et al. (2018)](https://doi.org/10.1371/journal.pbio.2004274) on
CRCNS [fcx-2](https://doi.org/10.6080/K0VX0DQD), which holds the preprocessed intracranial EEG of
the paper's 10 subjects (254 bipolar MTL, PFC and OFC electrodes) in the visuospatial working memory
task, with trial tables and the paper's MATLAB analysis scripts.

| Claim | Outcome |
|---|---|
| All subjects proficient (accuracy 0.79 to 0.97) | Reproduced |
| Accuracy and response time do not differ by condition | Not reproduced |
| 254 electrodes, 36 MTL, 116 PFC, 102 OFC | Reproduced |
| About 100 correct trials per subject | Reproduced |
| ERPs do not differ by condition | Not reproduced |
| Sustained theta power in all regions | Not reproduced |
| 8 electrodes with power condition effects | Not reproduced |
| PLV peaks in theta | Reproduced |
| Theta PSI shifts from frontal to MTL leads | Not reproduced |
| Cross-spectral PSI shifts after the test cue | Not reproduced |
| Counts of theta phase-directing electrodes and pairs | Not reproduced |
| Equal cross-spectral strength across frequencies and directions | Not reproduced |
| Individual theta peak bands | Not reproduced |
| Theta PAC by condition (eight claims) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The trial table and the descriptor place the task events 1.5 s earlier than the time axes of the
derived data, which the paper's code follows, and the data show no task-locked response that
settles it. The PSI of the paper's Methods selects no phase-directing units; the PAC claims use the
units of the deposited code's own form of PSI. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/crcns-fcx-2-johnson-2018-01.yaml`](../../attempts/crcns-fcx-2-johnson-2018-01.yaml).
