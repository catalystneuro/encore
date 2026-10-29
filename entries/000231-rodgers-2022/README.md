# Rodgers (2022) from dandiset 000231

Tests the statements of the data descriptor [Rodgers (2022)](https://doi.org/10.1038/s41597-022-01728-1)
on [DANDI:000231](https://dandiarchive.org/dandiset/000231/0.220904.1554), version 0.220904.1554, the
version the paper cites. The dandiset holds 115 sessions of 15 mice doing whisker-based shape
discrimination or detection, with whisker tracking from 200 frames/s video and, in 44 sessions,
recordings from barrel cortex.

| Claims | Outcome |
|---|---|
| Neural sessions and hours, task rules, "nothing" only in detection, one task per mouse, servo positions, outcome logic, forced alternation, video timebase, blackout gaps, bend on interpolated frames, neural sampling rate, unit depths and layers, electrode order, recording columns, observation intervals, pose structure, C0 contacts, contacts structure, NWB structure, file layout, video format, subjects (23 claims) | Reproduced |
| Dataset size (trials do not match), choice time as the first lick, ignore_trial definition, trials table stop and start times, unit firing-rate criterion, session labeling quality (6 claims) | Not reproduced |
| Reward and timeout, sessions with at least 90 trials (2 claims) | Blocked: methods underspecified (the criterion's readings disagree) |
| Response window timing, neural to video alignment, Arduino clock drift, three tracking-accuracy claims (6 claims) | Blocked: data missing |
| Two findings of earlier papers (2 claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000231-rodgers-2022-01.yaml`](../../attempts/000231-rodgers-2022-01.yaml).

- `reproduce_rodgers_2022.ipynb`: the analysis. It takes about five minutes, most of it streaming
  the 115 NWB files in parallel.
- `rodgers.py`: listing the pinned version, streaming each NWB file and reducing it to per-session
  summaries, reading video headers, and the measures used by the claims. Other notebooks on this
  dandiset can import it.
