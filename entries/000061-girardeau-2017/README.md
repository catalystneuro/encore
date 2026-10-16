# Girardeau, Inema & Buzsaki (2017) from dandiset 000061

Tests the findings stated in the abstract of [Girardeau et al. (2017)](https://doi.org/10.1038/nn.4637)
on [DANDI:000061](https://dandiarchive.org/dandiset/000061/0.250624.0426), which holds sorted units
of the hippocampus and the amygdala, sleep states and ripple, air-puff and reward events from four
rats. The paper is not open access, so only its abstract was used, and the methods are common
choices fixed before the analysis.

| Claim | Outcome |
|---|---|
| Joint hippocampus and BLA patterns of the run reactivate in post-sleep Non-REM | Reproduced |
| The reactivations peak during sharp wave-ripples | Reproduced |
| A subgroup of BLA cells is positively modulated during ripples | Reproduced |
| The reactivations involve those BLA cells | Reproduced |
| Reactivation is stronger for the air-puff direction than the safe one | Not reproduced |
| Rats learned the location of the air puff | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset has no position tracking, so run direction comes from the reward times. Position
could only come from tracking the raw video frames stored in the files, which would take about
190 hours to stream at the rate measured in the last run. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/000061-girardeau-2017-01.yaml`](../../attempts/000061-girardeau-2017-01.yaml).

- `reproduce_girardeau_2017.ipynb`: the analysis. It takes about 14 minutes (13.9 in the last
  run, as printed at its end), six of them streaming the files.
- `hpcbla.py`: loading the files, sleep epochs, laps, joint patterns and their reactivation, and
  ripple modulation. Other notebooks on this dandiset can import it.
