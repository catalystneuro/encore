# Kennedy, Kunwar, Li et al. (2020) from dandiset 001182

Tests the findings of [Kennedy et al. (2020)](https://doi.org/10.1038/s41586-020-2728-4) that can be
tested on [DANDI:001182](https://dandiarchive.org/dandiset/001182/0.240827.1656), which holds the
microendoscopic calcium imaging traces of 5 mice over three days, one file per mouse and day.

| Claim | Outcome |
|---|---|
| 187.3 cells imaged per day, 78 tracked across days | Not reproduced as stated (per mouse and day); the per-day total over the 5 mice matches exactly |
| Fiber photometry, behaviour, optogenetics, slice and silicon probe findings (20 claims) | Blocked: data missing |
| Imaging findings that need the stimulus presentations (15 claims) | Blocked: metadata insufficient |
| Network model findings (3 claims) | Blocked: depend on blocked imaging claims |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold the traces and one annotation channel ("Ch1: baseline", empty for 3 of the 5 mice),
but no stimulus onset times, no stimulus names, no cell identifiers and no cross-day registration,
so no stimulus response can be located. The cell counts per day (203, 183 and 176 over the five
mice) match the paper's 187.3 +/- 8.1 to the last digit, which supports that these are the paper's
cells; the claims file reads that number per mouse, and a reader has been asked. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/kennedy-2020-01.yaml`](../../attempts/kennedy-2020-01.yaml).
