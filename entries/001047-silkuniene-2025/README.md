# Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) from dandiset 001047

Tests the findings of [Silkuniene et al. (2025)](https://doi.org/10.1016/j.bioelechem.2025.109016)
that can be tested on [DANDI:001047](https://dandiarchive.org/dandiset/001047/0.250701.1609), which
holds stitched YO-PRO-1, Hoechst and propidium images of CT26 monolayers exposed to CANCAN and
control packets at 1 Hz and 0.2 MHz, and images of CHO monolayers. The paper's 1 kHz and 10 kHz
rates, pulse durations, film thermometry and CHO burst series are not in it, and no file gives the
electrode elevation.

| Claim | Outcome |
|---|---|
| Heating stays below 44 C (Figure 2) | Blocked: data missing |
| CANCAN enhances the centre, control does not (Figure 3A) | Not reproduced |
| 0.2 MHz suppresses near-electrode and perimeter uptake (Figure 3B, C) | Not reproduced |
| YP profile is Lorentzian, R > 0.9 (Figure 3) | Not reproduced |
| Deviation from the fit beyond 4 mm falls with rate (Figure 3) | Not reproduced |
| No rate effect at the centre (Figure 4B) | Partially reproduced |
| Near-electrode uptake falls with rate (Figure 4B) | Not reproduced |
| 40-fold centre to near-electrode ratio at 0.2 MHz (Figure 4B) | Not reproduced |
| FWHM falls with rate, and its log trend (Figure 4C) | Blocked: data missing |
| Raised electrodes weaken the centre (Figure 5) | Blocked: metadata insufficient |
| YP spot slightly larger than Pr spot (Figure 5A, B) | Not reproduced |
| Pr Gaussian, YP Lorentzian (Figure 5B) | Not reproduced |
| Nuclear YP in the central spot (Figure 5C) | Blocked: data missing |
| Pulse duration (Figure 6, three claims) | Blocked: data missing |
| Burst number, CT26 and CHO series (Figure 7B, C, E, F) | Blocked: data missing |
| Sharpest peak with 1 burst (Figure 7) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset gives the burst number only as a subject label. The attempt reads the label as the
number of repeats after the first burst, so that x1 is the paper's 2 bursts (x4) at both rates, an
assumption; the other reading (the label is the total) is shown. The paper's error-bar rule is read
as a gap beyond the longer error bar, with the other readings shown. The protocol text (3.8-mm
spacing, 3.2 kV) does not describe the paper's array, which the images show, and the voltage cannot
be checked from the images. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001047-silkuniene-2025-01.yaml`](../../attempts/001047-silkuniene-2025-01.yaml).

- `reproduce_silkuniene_2025.ipynb`: the analysis. It takes six to ten minutes, most of it
  streaming 42 images (11.5 GB).
- `cancan.py`: listing and streaming the files, parsing their conditions, locating the electrode
  array, ROI profiles along the diagonals and the fits of the Methods. Other notebooks on this
  dandiset can import it.
