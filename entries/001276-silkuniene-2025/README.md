# Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) from dandiset 001276

Tests the findings of [Silkuniene et al. (2025)](https://doi.org/10.1016/j.bioelechem.2025.109016)
that can be tested on [DANDI:001276](https://dandiarchive.org/dandiset/001276/0.250701.1609), which
holds whole-well YO-PRO-1 and Hoechst images of CT26 and CHO monolayers: the burst-number series of
Figure 7 (0.2 MHz, 1, 2, 4 or 6 bursts (x4)) and CANCAN and control wells at a packet rate of 1 Hz.
The paper's other series (1 kHz and 10 kHz rates, raised electrodes, propidium, 300 and 900 ns
pulses) and its thermometry are not in this dandiset.

| Claim | Outcome |
|---|---|
| Center YP rises linearly with burst number in both cell lines (p < 0.001) | Partially reproduced |
| CT26 center YP saturates at 6 bursts (x4), CHO does not | Partially reproduced |
| FWHM grows with burst number in CT26 but not in CHO | Reproduced |
| 1 burst (x4) in CT26 gives FWHM 1.1 mm, 7.3% of the gap, 2.3% of the array area | Reproduced (assumption) |
| Near-electrode YP 40 to 50 times smaller than at the center after 1 burst (x4) | Not reproduced |
| CHO cells show the same central focusing | Reproduced |
| 40-fold center to near-electrode ratio at 0.2 MHz | Not reproduced |
| CANCAN enhances the center, the control does not | Partially reproduced |
| The profile follows a Lorentzian within 4 mm (R > 0.9) | Reproduced |
| The excess over the Lorentzian beyond 4 mm falls with packet rate | Reproduced |
| Center YP shows no effect of packet rate | Reproduced |
| YP at 6 and 7 mm declines with packet rate | Reproduced |
| FWHM falls from about 4 mm at 1 Hz to about 2 mm at higher rates | Partially reproduced |
| Figures 4C (log fit), 5 and 6 (eight claims) | Blocked: in other dandisets |
| Heating (Figure 2) and field simulation (Figure 1E) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give no pixel size and no electrode positions. The analysis takes 1.625 um per pixel from
the camera and objective named in the Methods, finds the electrode footprints in each image by fitting
a square of the paper's size, and places the paper's ROIs along the diagonals from its center. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001276-silkuniene-2025-01.yaml`](../../attempts/001276-silkuniene-2025-01.yaml).

- `reproduce_silkuniene_2025.ipynb`: the analysis. It takes about 14 minutes, most of it streaming
  the 54 YO-PRO-1 images (19 GB).
- `cancan.py`: streaming and binning the images, locating the electrode array, the ROI profiles and
  the Lorentzian fit. Other notebooks on this dandiset can import it.
