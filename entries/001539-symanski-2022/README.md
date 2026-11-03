# Symanski, Bladon, Kullberg, Miller & Jadhav (2022) from dandiset 001539

Tests the findings of [Symanski, Bladon et al. (2022)](https://doi.org/10.7554/eLife.79545) on
[DANDI:001539](https://dandiarchive.org/dandiset/001539/0.250815.1203), which holds 38 recording
days of 8 rats in the odor-place T-maze task: CA1, PFC and OB LFP, CA1 and PFC units, position and
trial times.

| Outcome | Claims |
|---|---|
| Reproduced | 18 |
| Partially reproduced | 11 |
| Not reproduced | 9 |
| Blocked: data missing (thermocouple, air-only sessions) | 3 |
| Blocked: methods underspecified (the paper's readings disagree on this data) | 6 |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no odor identity, chosen well or spike waveforms: the odor and the choice are read
from the rewarded well and the position, and interneurons are defined by firing rate alone. The
units table's `electrodes` column holds tetrode numbers, not electrode-table rows, and is read that
way. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001539-symanski-2022-01.yaml`](../../attempts/001539-symanski-2022-01.yaml).
