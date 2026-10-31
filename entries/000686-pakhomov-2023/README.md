# Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023) from dandiset 000686

Tests the findings of [Pakhomov et al. (2023)](https://doi.org/10.1016/j.bioelechem.2023.108437) that
can be tested on [DANDI:000686](https://dandiarchive.org/dandiset/000686/0.240515.1909), which holds
the 18 stitched YO-PRO-1 images of CHO cell monolayers behind Fig. 5: 40 Packet 2 packets or 40
control trains from e1, and the same with electrode rotation (1P x 40, 1T x 40), at 6.4 kV. No ROI
measurements are deposited, so the profiles along the array diagonals are measured from the images.

| Claim | Outcome |
|---|---|
| 40 trains give much stronger uptake than 40 packets throughout the array (Fig. 5A) | Not reproduced |
| Packets enhance the centre; uptake near e1 stays stronger than in the centre (Fig. 5A) | Not reproduced |
| With rotation, packets peak in the centre and trains leave a central void (Fig. 5B) | Not reproduced |
| Normalized, the rotated packet centre is high and the train centre low (Fig. 5C) | Blocked: methods underspecified (depends on the ROI width, which the paper does not give); not reproduced is proposed, with ROIs one step wide as the most direct reading of the paper's layout |
| Field simulations (Fig. 3) | Blocked: data missing |
| Single-cell uptake and bipolar cancellation (Fig. 4, four claims) | Blocked: data missing |
| Packet number, voltage, packet type and electrode height (Figs. 6 to 9, eleven claims) | Blocked: data missing (not in this dandiset; apparently in DANDI:000875, 001025, 001027, 001028) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data of Figs. 6 to 9 appear, from their titles and descriptions, to be in four other dandisets
that name the paper (not opened here); the claims file does not
mark them as data elsewhere, and a question asks a reader whether it should. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/000686-pakhomov-2023-01.yaml`](../../attempts/000686-pakhomov-2023-01.yaml).

- `reproduce_pakhomov_2023.ipynb`: the analysis. It takes about eight minutes, nearly all of it
  streaming the 18 images (about 600 MB each).
- `cancan.py`: streaming the images (parallel range requests on the HDF5 chunks), finding the
  electrode footprints, placing the ROIs of Methods 2.4, and the readings and tests of the claims
  file. Other notebooks on the CANCAN dandisets can import it.
