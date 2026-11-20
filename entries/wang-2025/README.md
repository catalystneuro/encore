# Wang, Kurgyis, Chen et al. (2025) from dandiset 000363

Tests the findings of [Wang et al. (2025)](https://doi.org/10.1038/s41593-025-02114-x) that can be
tested on [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.230822.0128) (Mesoscale Activity
Map), version 0.230822.0128, the one the paper cites. It holds 174 Neuropixels sessions of 28 mice
with three DeepLabCut markers (jaw, nose, tongue) from the side camera. It has no video and no
autoencoder embedding; the later version 0.231012.2129 adds the raw video, which would take about
100 hours to read for the paper's sessions before any network is trained.

| Claim | Outcome |
|---|---|
| The authors' deposit links to the dataset (area names, the 106 sessions of Figs. 6 and 7) | Reproduced |
| More than 50,000 neurons in more than a dozen structures | Reproduced |
| Marker-based choice predictability clusters by mouse (Fig. 6e) | Partially reproduced |
| Claims on the embedding, the end-to-end networks or the embedding decoder (25 claims) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In five sessions (SC011 and SC022, February 2019) the marker timestamps advance 3.4 ms per frame
where the frames are 6.8 ms apart, so their markers do not line up with the lick events unless the
timestamps are stretched by 2. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/wang-2025-01.yaml`](../../attempts/wang-2025-01.yaml).
