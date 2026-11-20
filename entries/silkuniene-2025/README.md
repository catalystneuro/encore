# Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) from dandisets 001047, 001276, 001277 and 001284

Tests the findings of [Silkuniene et al. (2025)](https://doi.org/10.1016/j.bioelechem.2025.109016) on
[DANDI:001047](https://dandiarchive.org/dandiset/001047/0.250701.1609),
[DANDI:001276](https://dandiarchive.org/dandiset/001276/0.250701.1609),
[DANDI:001277](https://dandiarchive.org/dandiset/001277/0.250701.1610) and
[DANDI:001284](https://dandiarchive.org/dandiset/001284/0.250701.1610). Each file is a whole-well image of a
cell monolayer stained with YO-PRO-1, propidium or Hoechst after CANCAN pulse exposures from a
four-electrode array. Dye uptake is measured in ROIs along the diagonals of the array, and for one claim along lines parallel to its sides.

| Claim | Outcome |
|---|---|
| Field simulation, heating (Figs. 1 and 2) | Blocked: data missing |
| Centre enhanced by CANCAN, dip in the control (Fig. 3A) | Partially reproduced on 001276 (two rates held; the control dip fails) |
| 0.2 MHz suppresses off-target uptake (Fig. 3B, C) | Blocked: data missing (verified before the reader's answer); reproduced on 001276 on an assumption about the pooling was proposed, and the verifier did not agree (it would block the claim as methods underspecified) |
| Lorentzian profile, R > 0.9 (Fig. 3) | Partially reproduced on 001276 (two rates held) |
| 40-fold centre to near-electrode ratio (Fig. 4B) | Reproduced on 001276 (on an assumption about the background footprint, which alone moves the ratio across the band) |
| Rest of the packet-rate series (Figs. 3 and 4, five claims) | Blocked: data missing (001047 holds a smaller array; no dandiset holds the 1-kHz and 10-kHz wells) |
| Raising the electrodes weakens the central spot | Not reproduced |
| Cell killing focused at the centre | Reproduced |
| YP spot slightly larger than the Pr spot | Not reproduced |
| Pr Gaussian, YP Lorentzian, with the reported R2 | Reproduced |
| Reversible electroporation from about 2 mm | Reproduced |
| Zones of Fig. 5C | Partially reproduced (high-resolution images not deposited) |
| 900-ns peak highest, not significantly | Reproduced |
| Normalized decline similar across durations | Not reproduced |
| FWHM falls with pulse duration | Not reproduced (it holds only when a 600-ns well whose only difference is its broad profile is left out) |
| 600 and 900 ns each narrower than 300 ns | Blocked: methods underspecified (the outcome depends on the background footprint) |
| 900-ns FWHM 1.7 mm | Reproduced |
| Centre YP linear in burst number | Partially reproduced |
| CT26 saturation at 6 bursts | Partially reproduced |
| FWHM grows with bursts in CT26, not CHO | Blocked: methods underspecified (the outcome depends on the background footprint) |
| Sharpest peak, 1 burst in CT26, 1.1 mm | Reproduced |
| Off-target 40 to 50 times smaller (Fig. 7 series) | Reproduced (on an assumption about the background footprint) |
| CHO cells replicate the focusing | Reproduced |

After the first verification rounds a reader answered two questions on the claims file (questions/silkuniene-2025.yaml): four packet-rate claims now list DANDI:001276, and the electrode footprint that gives the background is an open reading that every claim citing it is run under. The changes the answers bring were proposed and reviewed in a third verification round, which agreed with all but one: the change of the Fig. 3B, C claim to reproduced, whose outcome stays as verified. Two further questions from that round are with a reader.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/silkuniene-2025-04.yaml`](../../attempts/silkuniene-2025-04.yaml).

- `reproduce_silkuniene_2025.ipynb`: the analysis. It takes about 27 minutes (printed at its end), most of it
  streaming the 121 image files it reads (46.7 GB, printed in the notebook).
- `cancan.py`: listing and reading the files, locating the electrode array, ROI profiles and the
  Lorentzian and Gaussian fits. Other notebooks on these dandisets can import it.
