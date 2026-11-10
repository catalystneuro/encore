# Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022) from dandisets 000489 and 000448

Tests the findings of [Kim et al. (2022)](https://doi.org/10.1016/j.bioelechem.2022.108319) that can be
tested on [DANDI:000489](https://dandiarchive.org/dandiset/000489/0.230518.1811), the dish images of the
Fig. 2 experiment (YO-PRO-1 uptake after uni- and bipolar 600 ns pulses), and
[DANDI:000448](https://dandiarchive.org/dandiset/000448/0.230421.1844), strobe images of the membrane
potential of 9 CHO cells during 833 kHz pulse trains (Fig. 7). The experiments of Figs. 3 to 6 and the
thermometry of Fig. 1E are in neither. Dandisets 000548, 000549 and 000550 name the paper and match
Figs. 3, 4 and 6 by title, but are not among the paper's datasets this attempt tested.

| Claim | Outcome |
|---|---|
| YP uptake rises with field for every second phase amplitude (Fig. 2A) | Reproduced (assumed) |
| Vertical scales of Fig. 2A, 1200 to 250 a.u. | Not reproduced |
| Exponential rise with the same slope for every amplitude (Fig. 2B) | Partially reproduced |
| Strongest inhibition, to about 20%, at 50 to 75% (Fig. 2C) | Partially reproduced |
| Inhibition flat between 8.7 and 15.1 kV/cm | Reproduced |
| Weaker inhibition at 6.7 kV/cm | Reproduced (assumed) |
| Unipolar pulses polarize the two poles in mirror image (Fig. 7) | Reproduced (assumed) |
| Charging 200 ns and discharging 520 ns time constants | Not reproduced |
| Later pulses show the same difference of time constants | Partially reproduced |
| Bipolar pulses: same first-phase polarization, faster discharge, overshoot | Reproduced |
| Bipolar trains alternate the membrane potential | Reproduced |
| Unipolar trains: same peak each pulse, continuous polarization | Reproduced |
| Figs. 3 to 6 (12 claims) | Blocked: dataset missing (likely in 000548, 000549, 000550) |
| Heating (Fig. 1E) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The YO-PRO-1 channel of two dishes of different conditions is the same image, and 000448 holds 5 of
the paper's 18 unipolar and 4 of its 17 bipolar cells. The attempt record, with the reasons and the
differences from the paper's method, is [`attempts/kim-2022-02.yaml`](../../attempts/kim-2022-02.yaml).
