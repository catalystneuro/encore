# Semenov et al. (2026) from dandiset 001516

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283) on
[DANDI:001516](https://dandiarchive.org/dandiset/001516/0.261006.1833), version 0.261006.1833. The
dandiset holds 72 image sets from 12 fields of view of FluoVolt-stained CHO cells: single 1-us pulses
and pulse pairs with intervals of 1 to 250 us, at 150 to 1570 V/cm, with 1.00-mm electrodes. The
paper does not report this experiment. Its figures rest on Di-8-ANEPPS and FluoVolt escalations, a
Di-8-ANEPPS two-pulse experiment at a 5-us interval, Gd3+ experiments and Fluo-4 calcium imaging,
none of which is in the dandiset.

| Claim | Outcome |
|---|---|
| Eq. (2): a 10-fold rise in effective conductivity reduces IMP by ~2%, a 100-fold rise by 12% | Not reproduced |
| All 31 claims on recordings (Figures 1 to 7) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The notebook also measures the dataset's own sets with the paper's pole method, which decides no
claim. The attempt record, with the reasons and the findings about the dataset, is
[`attempts/001516-semenov-2026-01.yaml`](../../attempts/001516-semenov-2026-01.yaml).
