# Wirtshafter and Wilson (2020) from CRCNS hc-29

Tests the findings of [Wirtshafter and Wilson (2020)](https://doi.org/10.7554/eLife.55252) on
[CRCNS hc-29](https://doi.org/10.6080/K0NG4NV8), which holds the sorted spike times of 452 lateral
septum and 178 CA1 clusters and the time bases of 57 recordings of six rats.

| Claim | Outcome |
|---|---|
| Units recorded, and cells meeting the rate and track coverage criteria | Partially reproduced (units recorded match; cells meeting the criteria blocked: data missing) |
| Spatial information, place fields, skew, field locations and CA1-LS cross-correlations (30 claims) | Blocked: data missing |

The data set holds no position data, and every finding of the paper beyond the count of units
recorded uses the animal's position on the maze. The clusters deposited match the paper's counts of
units recorded (452 LS, 178 CA1) exactly, but the claim also gives the counts of cells that meet the
paper's speed-filtered rate and track coverage criteria, which cannot be computed, so it holds in
part.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The notebook checks the files: two spike trains of rat 7 are deposited under 43 cluster names, on rat 6 one cluster per recording holds the spikes of the others on its tetrode,
and nothing marks the 30 min maze session within recordings of up to 31 h: the time bases have no
change of sampling rate and no gap of 0.1 s, and no recording has a minute without a spike.

The attempt record, with the reasons, is
[`attempts/wirtshafter-2020-01.yaml`](../../attempts/wirtshafter-2020-01.yaml).

- `reproduce_wirtshafter_2020.ipynb`: the data checks and the unit counts. It takes about five
  minutes, most of them streaming Times.mat (2.2 GB) twice, to check its MD5 and to read every
  sample interval.
- `hc29.py`: streaming the three files from the CRCNS bucket, parsing the cluster names, the time
  bases of the recordings, the search for clusters deposited twice, the spike-free stretches of
  each recording and the file list of the paper's code repository. Other notebooks on this
  data set can import it.
