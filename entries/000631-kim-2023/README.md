# Kim et al. (2023) from dandiset 000631

Tests the findings of [Kim et al. (2023)](https://doi.org/10.3390/ijms241310921) that can be tested
on [DANDI:000631](https://dandiarchive.org/dandiset/000631/0.231012.1508), which holds stitched
YO-PRO-1 and MemBrite images of BPAE monolayers after paired-pulse and single-pulse trains in a
triangular electrode array at 1 Hz and 833 kHz (Figures 2 and 4). The square-array data of Figure 3
and the strobe imaging of Figure 5 are not in it.

| Claim | Outcome |
|---|---|
| At 180 degrees paired trains give 2-fold (1 Hz) and 20-fold (833 kHz) less uptake than single trains | Partially reproduced |
| Paired and single trains are equal at about 160 (1 Hz) and 130 degrees (833 kHz) | Reproduced |
| Three-fold facilitation at 90 to 100 degrees, then a plateau to 0 degrees | Partially reproduced |
| Enhancement at small angles and inhibition at large angles depend on frequency | Reproduced |
| 60-fold difference between co- and counter-directional pairs at 833 kHz | Reproduced |
| Paired pulses at 833 kHz electroporate near the apex, single pulses follow the field | Reproduced |
| Figure 3: square array, co- and cross-directional pulses (four claims) | Blocked: data missing |
| Figure 5: FluoVolt strobe imaging (two claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold only the images: no pixel size, electrode positions, ROIs or angles. The helper
`swing.py` finds the electrode footprints in each image, places the ROIs and computes the angle
of field direction change from field models. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000631-kim-2023-01.yaml`](../../attempts/000631-kim-2023-01.yaml).
