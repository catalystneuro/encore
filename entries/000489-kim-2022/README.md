# Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022) from dandiset 000489

Tests the findings of [Kim et al. (2022)](https://doi.org/10.1016/j.bioelechem.2022.108319) that
can be tested on [DANDI:000489](https://dandiarchive.org/dandiset/000489/0.230518.1811). The
dandiset holds stitched MemBrite and YO-PRO-1 images of the 17 dishes of Fig. 2: unipolar or
bipolar 600 ns pulses with a second phase of 25 to 100%. The experiments of Figs. 3 to 7 and
the thermometry of Fig. 1E are not in it. Those of Figs. 3 to 7 are in dandisets 000548, 000549,
000550 and 000448, which name the same paper and are not used here.

| Claim | Outcome |
|---|---|
| YP uptake rises with field for every second phase amplitude | Partially reproduced (assumed) |
| Fig. 2A vertical scales, 1200 a.u. unipolar to 250 a.u. at 75% | Not reproduced (assumed) |
| Exponential rise with the same slope for every amplitude | Not reproduced (assumed) |
| Strongest inhibition, to about 20%, at 50 to 75% (p < 0.01) | Not reproduced (assumed) |
| Inhibition does not depend on field from 8.7 to 15.1 kV/cm | Not reproduced |
| Inhibition weaker at 6.7 kV/cm | Blocked: the unipolar mean there is at background |
| Figs. 3, 4, 5, 6 and 7 (15 claims) | Blocked: data in other dandisets of the paper |
| Fig. 1E heating | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold only the images. The ROI, the electrode footprints and the field of each ROI are
measured or recomputed here from the paper's description, and the outcomes marked assumed depend
on how the ROI and footprints are read. The YP image of one unipolar dish is a copy of a 25%
dish's, so unipolar pulses have 2 dishes; dandiset 000548 holds the right image, which is checked
but not used. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000489-kim-2022-01.yaml`](../../attempts/000489-kim-2022-01.yaml).
