# Yang (2026) from dandiset 000363

Tests the findings of [Yang (2026)](https://doi.org/10.21203/rs.3.rs-11447300/v1), a reanalysis of
the late-delay bilateral ALM photoinhibition sessions of the Mesoscale Activity Map dataset,
[DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129) (Chen et al. 2024), at the
version the paper cites, 0.231012.2129.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the outcome of each claim, the reasons and the differences from the
paper's method, is [`attempts/yang-2026-01.yaml`](../../attempts/yang-2026-01.yaml).

- `reproduce_yang_2026.ipynb`: the analysis. It surveys the 174 session files, streams the spike
  times, trial events, licks and video keypoints of the 112 late-delay sessions, and tests the 25
  claims. It takes about 40 minutes, about 25 of them streaming.
- `mam.py`: loading of the sessions, trial sets, z-scored window rates, choice and action axes,
  control splits, decoding, matching and distances. Other notebooks on this dandiset can import it.
