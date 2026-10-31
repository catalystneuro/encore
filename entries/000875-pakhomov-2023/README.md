# Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023) from dandiset 000875

Tests the findings of [Pakhomov et al. (2023)](https://doi.org/10.1016/j.bioelechem.2023.108437)
that can be tested on [DANDI:000875](https://dandiarchive.org/dandiset/000875/0.240515.1925),
which holds nine stitched YO-PRO-1 images of CHO monolayers, three dishes each after 4, 20 or 40
rotated Packet 2 packets at 3.2 kV in the small quadrupole array (Fig. 6).

| Claim | Outcome |
|---|---|
| More packets raise dye uptake throughout the array (Fig. 6A) | Reproduced |
| Center about twofold the periphery for 4 packets, about equal for 20 and 40 (Fig. 6B) | Partially reproduced |
| Least affected area about half the center for all packet numbers | Partially reproduced |
| Central peak narrower with more packets | Reproduced |
| Single-cell bipolar cancellation (Fig. 4, two claims) | Blocked: data missing |
| Figs. 5, 7, 8 and 9 (nine claims) | Blocked: data missing |
| Field simulation (Fig. 3) | Blocked: data missing (model not public) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold the images only: no pixel size, electrode positions or ROIs. The ROIs are placed by
code on the detected electrode footprints, under every reading of the ROI layout, background,
center, periphery and normalization that the claims file names. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000875-pakhomov-2023-01.yaml`](../../attempts/000875-pakhomov-2023-01.yaml).

- `reproduce_pakhomov_2023.ipynb`: the analysis. It takes about five minutes, most of it streaming
  the images.
- `cancan.py`: loading, electrode detection, ROI profiles and the readings of the claims file.
  Other notebooks on this dandiset can import it.
