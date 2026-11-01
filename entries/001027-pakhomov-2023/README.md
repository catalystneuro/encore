# Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023) from dandiset 001027

Tests the findings of [Pakhomov et al. (2023)](https://doi.org/10.1016/j.bioelechem.2023.108437)
that can be tested on [DANDI:001027](https://dandiarchive.org/dandiset/001027/0.240605.1859), which
holds the YO-PRO-1 images of the Figure 8 experiment: ten CHO monolayer dishes, each treated with
one of three packets of unipolar nanosecond pulses in a quadrupole electrode array. The single-cell
time-lapse of Figure 4 and the monolayer experiments of Figures 5, 6, 7 and 9 are not in it.

| Claim | Outcome |
|---|---|
| Packets 1, 2 and 3 give the same uptake in the center, 215 to 235 a.u. (Fig. 8A) | Not reproduced |
| Packets 1 and 3 give more uptake near the electrodes than Packet 2 (Fig. 8A) | Not reproduced |
| Normalized center 183% for Packet 2, 83% and 74% for Packets 3 and 1 (Fig. 8B) | Not reproduced |
| Figures 4, 5, 6, 7 and 9 (fifteen claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files labelled Protocol 3 (8 phases with 5-us delays) show the focusing the paper reports for
Packet 2 (8 phases without delays), and the files labelled Protocol 2 behave as its Packet 3. With
the two labels exchanged, the order of Figure 8B appears. The files give no pixel size and do not
identify the electrodes. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001027-pakhomov-2023-01.yaml`](../../attempts/001027-pakhomov-2023-01.yaml).

- `reproduce_pakhomov_2023.ipynb`: the analysis. It takes about five minutes, most of it streaming
  the ten 350-MB images.
- `cancan.py`: streaming the images (reduced to 8 x 8 pixel means as they are read), finding the
  electrodes, the ROI profiles along the diagonals, and the readings of the open details. Other
  notebooks on this dandiset can import it.
