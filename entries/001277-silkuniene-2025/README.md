# Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) from dandiset 001277

Tests the findings of [Silkuniene et al. (2025)](https://doi.org/10.1016/j.bioelechem.2025.109016)
that can be tested on [DANDI:001277](https://dandiarchive.org/dandiset/001277/0.250701.1610). The
dandiset holds the pulse-duration experiment of Figure 6: whole-well YO-PRO-1, Hoechst and propidium
images of 18 CT26 monolayers exposed to packets of 300-, 600- or 900-ns pulses from a four-electrode
array. The packet-rate, raised-electrode, burst-number and thermometry experiments are not in it.

| Claim | Outcome |
|---|---|
| The central YP peak is highest at 900 ns, without a significant difference | Reproduced (assumption on the wells) |
| Normalized YP declines similarly for the three pulse durations | Not reproduced |
| FWHM falls with pulse duration (p = 0.003) | Blocked: methods underspecified |
| FWHM at 600 and 900 ns each smaller than at 300 ns | Blocked: methods underspecified |
| FWHM at 900 ns is 1.7 mm, 11.1% of the gap | Blocked: methods underspecified (depends on the claim above) |
| Pr fits a Gaussian and YP a Lorentzian better | Not reproduced (assumption on the wells) |
| The YP spot is slightly larger than the Pr spot | Not reproduced (assumption on the wells) |
| Figures 2, 3, 4, 7 and the raised electrodes of Figure 5 (ten claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper analysed five wells per pulse duration; the dandiset has seven at 600 ns, with nothing to
say which five. The notebook takes the five plate rows that each hold one well of every duration,
and shows all seven and every choice of five. With those rows the FWHM trend is close to the paper's
under most readings; with all seven it disappears, because two wells on plate P1 take up dye over
the whole array. The ROI spacing along the diagonals is not given in the paper, and the significance
of the Figure 6D tests depends on it, so those claims are blocked as the claims file's criteria
require. The Figure 5 claims assume that the 600-ns wells with propidium images are the 0-mm group
of Figure 5; their propidium staining is broad, not a small central spot.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001277-silkuniene-2025-01.yaml`](../../attempts/001277-silkuniene-2025-01.yaml).

- `reproduce_silkuniene_2025.ipynb`: the analysis. It takes about ten minutes, most of it streaming
  the images (about 13 GB read, reduced to 40.6-um block means as they load).
- `cancan.py`: loading the files, finding the electrode footprints, the ROI profiles along the
  diagonals, and the Lorentzian and Gaussian fits of the Methods. Other notebooks on this dandiset
  can import it.
