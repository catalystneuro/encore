# Fan, Dal Monte, Nair, Fagan & Chang (2024) from dandiset 000959

Tests the findings of [Fan et al. (2024)](https://doi.org/10.1016/j.neuron.2024.05.004) on
[DANDI:000959](https://dandiarchive.org/dandiset/000959/0.261020.0242). The dandiset holds one file
per 300-s run for every day of the paper: 81 Eyes stimulation days (OFC, dmPFC and ACCg; 15 per area
from monkey L, 12 from monkey T) and 15 Mouth stimulation days of monkey T. Each file has the gaze and
pupil of both monkeys at 1 kHz, the stimulation and sham times, the day's ROIs and the fixation events.

| Claim | Outcome |
|---|---|
| Days per area, runs per day | Reproduced; partially reproduced (monkey L has 6.0 control runs per day, not 5) |
| Stimulation and sham counts comparable across areas and monkeys (social, control) | Reproduced |
| More fixations on the Eyes than on the non-eye Face | Reproduced |
| Eyes fixations comparable to RDM fixations | Not reproduced under the Methods' day total; comparable under the code's mean per run |
| OFC density map more clustered around the partner | Reproduced |
| OFC lowers social gaze distance, not dmPFC or ACCg; stronger contralaterally; none in the control condition; longer windows | Reproduced |
| No change in fixation number; longer whole Face looking after OFC stimulation | Reproduced; partially reproduced (tests hold, values in part) |
| No effect of Mouth stimulation | Reproduced (5 days per area cannot reach p < 0.05) |
| Eyes against Mouth bootstrap | Not reproduced |
| Inter-looking interval and reciprocation latency (day and trial level, 41% and 86%) | Reproduced |
| Partner monkey unchanged | Partially reproduced (one reading of M2's reciprocation latency gives dmPFC p = 0.044) |
| 76 of 81 days with at least 90 stimulations | Reproduced, with the five named days |
| Causal decomposition and epoch slopes (six claims) | Blocked: too large |
| Trigger fixation duration unchanged | Not reproduced (dmPFC p = 0.019) |
| Pupil unchanged | Reproduced |
| Saccade counts and kinematics (two claims) | Blocked: not runnable (MATLAB detection, no saccades in the files) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000959-fan-2024-01.yaml`](../../attempts/000959-fan-2024-01.yaml). `microstim.py` reads
each run into small tables (trials, fixation events with positions and hemifields, pupil traces)
and holds the measures.
