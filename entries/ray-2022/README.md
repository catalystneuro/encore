# Ray, Moaddab & McDannald (2022) from CRCNS nac-1

Tests the findings of [Ray et al. (2022)](https://doi.org/10.1523/JNEUROSCI.1107-21.2021) on
CRCNS data set [nac-1](https://doi.org/10.6080/K0M906VB), which holds 368 nucleus accumbens core
single units recorded from seven female rats during Pavlovian fear discrimination. The
pre-surgery sessions (Figure 1C) and the paper's population labels are not in it.

| Claim | Outcome |
|---|---|
| Units, sessions and rats recorded | Not reproduced (90 sessions, not 95) |
| Cue-responsive screen (193 units) | Reproduced |
| Acquisition before surgery (Figure 1C) | Blocked: data missing |
| Discrimination and behavior correlations (Figure 1G, 1H) | Reproduced (3) |
| K-means populations (Figure 2) | Partially reproduced |
| Populations by rat | Not reproduced |
| Most units signal threat | Reproduced |
| Firing and waveform characteristics (Figure 3) | Reproduced (2) |
| Cue firing by population (Figures 4 and 5) | 2 reproduced, 3 partially, 2 not |
| Firing similarity (Figure 6) | 4 reproduced, 1 not |
| Tuning curves (Figure 7) | Reproduced |
| Fear output and exaggerated threat (Figure 8) | 1 reproduced, 2 partially |
| Reward firing (Figure 9) | 1 partially, 3 not |
| Nose poke cessation firing (Figure 10) | 1 reproduced, 2 not |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The population findings rest on a reproduced k-means partition, chosen as an assumption among
the claims file's readings, since the paper's labels are not deposited and its clustering cannot
be repeated. The data set includes the authors' MATLAB scripts, which give the event channel map
and settle several details the Methods leave open. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/ray-2022-01.yaml`](../../attempts/ray-2022-01.yaml).

- `reproduce_ray_2022.ipynb`: the analysis. It takes about five minutes, most of it the CI checks.
- `nac.py`: loading the unit files from the zip in place, the event channel map, and the
  measures (suppression ratio, screen, normalizations, ITI events inside the recorded segments,
  ANOVAs, bootstrap in both interval forms, dip test).
