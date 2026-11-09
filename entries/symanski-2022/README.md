# Symanski, Bladon, Kullberg, Miller & Jadhav (2022) from dandiset 001539

Tests the findings of [Symanski, Bladon et al. (2022)](https://doi.org/10.7554/eLife.79545) on
[DANDI:001539](https://dandiarchive.org/dandiset/001539/0.250815.1203), which holds 38 recording
days of 8 rats in the odor-place T-maze task: CA1, PFC and OB LFP, CA1 and PFC units, position and
trial times.

| Outcome | Claims |
|---|---|
| Reproduced | 17 |
| Partially reproduced | 6 |
| Not reproduced | 12 |
| Blocked: data missing (thermocouple, air-only sessions, spike widths) | 6 |
| Blocked: methods underspecified (the paper's readings disagree on this data) | 6 |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most outcomes rest on stated assumptions about methods the paper leaves open; the record marks them
and its deviations say which. fig5e-beta-mvl-correct-incorrect and fig5s2-ca1-int-pfc-beta-accuracy
are reproduced by the criterion's method only: a split-half control, which decides locking and
measures it on different trials, does not support them. Three claims are blocked for missing data because
their outcome differs between the two rate-only interneuron rules and the Methods' rule needs the
spike widths the files lack: fig5gh-phase-preference and fig5-rr-more-than-beta (reproduced at
9.5 Hz, partial or failing at 7 Hz) and fig4d-ccg-lags (also open on its window and significance
band). The third verification round agreed with these changes.

The files hold no odor identity, chosen well or spike waveforms: the odor and the choice are read
from the rewarded well and the position, and interneurons are defined by firing rate alone (over 9.5 Hz, the paper code's rate-only rule;
the Methods' 7 Hz is shown beside it). The
units table's `electrodes` column holds tetrode numbers, not electrode-table rows, and is read that
way. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/symanski-2022-01.yaml`](../../attempts/symanski-2022-01.yaml).
