# Girardeau, Inema & Buzsaki (2017) from dandiset 000061

Tests the claims of [Girardeau et al. (2017)](https://doi.org/10.1038/nn.4637), written by a reader
from the full text, the supplement and the paper's code
(`claims/000061/10.1038-nn.4637.yaml`), on
[DANDI:000061](https://dandiarchive.org/dandiset/000061/0.250624.0426) version 0.250624.0426,
which holds sorted units of the hippocampus and the amygdala, sleep states and ripple, air puff and
reward events from four rats. The attempt record is
[`attempts/000061-girardeau-2017-02.yaml`](../../attempts/000061-girardeau-2017-02.yaml); it
replaces [`000061-girardeau-2017-01`](../../attempts/000061-girardeau-2017-01.yaml), whose claims
were written from the abstract alone.

Of 32 claims, 10 are tested: 6 reproduced, 1 partially reproduced, 3 not reproduced. The other
22 are blocked: 18 because the dandiset has no putative cell types (pyramidal cell or interneuron),
on which most of the paper's reactivation analyses rest, and 4 because it has no position tracking.
Two claims with a pyramidal test and an all-cell test are judged on the all-cell test alone, as
their criteria allow when the pyramidal test cannot be run.

| Claim | Outcome |
|---|---|
| `unit-counts` | Not reproduced: 40 of 61 sessions, 4702 of 7,390 units |
| `habituation-over-days` | Reproduced (laps from reward times) |
| `bla-pyr-sleep-firing-increase` | Reproduced (identified cells of five Rat08 files) |
| `bla-int-sleep-firing` | Not reproduced (REM/wake change p = 0.020) |
| `reactivation-all-cell-pairs` | Reproduced |
| `cen-no-reactivation` | Reproduced |
| `ripple-rate-unchanged` | Reproduced |
| `reactivation-peaks-at-ripples` | Partially reproduced (all-cell test alone, p = 0.0042) |
| `direction-all-cell-pairs` | Reproduced (laps from reward times) |
| `ripple-modulated-cells-larger-reactivation` | Not reproduced (all-cell test alone, p = 0.27) |
| 18 claims on putative pyramidal cells or interneurons | Blocked: metadata insufficient |
| `rats-learn-puff-location` and the three behaviour claims that depend on it | Blocked: too large (position only in raw video frames) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Position could only come from tracking the raw video frames stored in the files, which would take
about 234 hours to stream at the rate measured in the final run (the rate varies between runs). Five Rat08 files have a `cell_type` column, which marks
only cells identified as excitatory or inhibitory.

- `reproduce_girardeau_2017.ipynb`: the analysis. It takes about 8 minutes (7.6 in the final run), six of
  them streaming the files; the notebook prints its run time at the end.
- `hpcbla.py`: loading the files, sleep epochs, laps, EV and REV, ripple modulation, reactivation
  strength around ripples, firing rates by state. Other notebooks on this dandiset can import it.
