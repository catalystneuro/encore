# Natraj et al. (2025) from dandiset 001535

Tests the findings of [Natraj et al. (2025)](https://doi.org/10.1016/j.cell.2025.02.001) that can
be tested on [DANDI:001535](https://dandiarchive.org/dandiset/001535/0.260608.0617), which holds
one NWB file for participant B1: 9737 trials of the high-gamma and low-frequency features (100 Hz,
128 channels) used to train the paper's biLSTM decoder, each with a target id and a virtual or
robot flag.

| Claim | Outcome |
|---|---|
| The biLSTM was trained on about 14 h 48 min of data | Reproduced (resting on an assumption) |
| The other 51 claims (Figures 1 to 7 and S2 to S8) | Blocked: data missing (48), metadata insufficient (3) |

The stored trials last 13 h 57 min in total. This matches if the robot trials are the real-world
practice the paper counts, which the file does not say; without them the total is 540 min, outside
the tolerance. The spatial pooling claim of Figure S3 is blocked because the file does not place
the channels on the grid; the notebook shows a variant under assumed layouts, where pooling lowers
the variance under every layout, random ones included.

The file has no participant B3, no Figure 1 task, no band-power features of the MLP decoders, no
day, session or open-loop and closed-loop labels, no online decoder outputs and no robot
kinematics, so the other findings cannot be tested. The target ids carry no names.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001535-natraj-2025-01.yaml`](../../attempts/001535-natraj-2025-01.yaml).

- `reproduce_natraj_2025.ipynb`: the data check and the analysis. It takes about ten minutes,
  most of it streaming the file.
- `bci.py`: streaming the file and per-trial summaries. Other notebooks on this dandiset can
  import it.
