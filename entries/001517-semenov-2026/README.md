# Semenov et al. (2026) from dandiset 001517

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283) that can be tested
on [DANDI:001517](https://dandiarchive.org/dandiset/001517/0.261006.1856), which holds raw strobe images of CHO
cells loaded with FluoVolt or Di-8-ANEPPS and exposed to 1-us pulses of escalating amplitude. The pole polarization,
the dye calibration and the departure from linear charging are rebuilt from the images by `strobe.py`.

| Claim | Outcome |
|---|---|
| Poles dim at strong fields while regions nearer the equator stay polarized (Fig. 1) | Reproduced |
| FluoVolt saturates at 66% (360 V/cm, cathodic) and -83% (570 V/cm, anodic) | Partially reproduced |
| FluoVolt responses stable within sets and baselines | Not reproduced |
| Di-8-ANEPPS dF climbs up to 570 V/cm at both poles | Reproduced |
| Di-8-ANEPPS bleaching shifts dF by about 5% at 43 V/cm | Reproduced |
| Di-8-ANEPPS responses decline within sets at 780 V/cm and above | Reproduced |
| Dye slopes of 26% and 9.1% per 100 mV against the calculated IMP (Fig. 3) | Not reproduced |
| FluoVolt bends from about 200 mV, Di-8-ANEPPS stays linear | Not reproduced |
| FluoVolt maxima of 71% and -83.5%, matching IMPC only at 43 and 150 V/cm | Not reproduced |
| FluoVolt cathodic dF falls from 71% to 45 to 50% | Not reproduced |
| Di-8-ANEPPS maxima of 57% and -55% at 570 V/cm | Not reproduced |
| Di-8-ANEPPS first-10-pulse maximum of 66% | Not reproduced |
| Above 780 V/cm the poles lose charge, more at the cathode | Partially reproduced |
| Equatorial regions follow the cosine up to 1000 V/cm | Not reproduced |
| Eq. (2) gives 2% and 12% IMP reductions for 10- and 100-fold conductivity rises | Partially reproduced |
| Charging falls 1.5- and 2-fold below linear at 570 and 780 V/cm (Fig. 7B) | Reproduced |
| Fig. 2C/D, 4D, 5A/C, 6 and 7A/C (15 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The shapes of the field-strength series reproduce; most failures are of absolute dF values and slopes, which rest on
details neither the paper nor the files give: the background method, the pixel size, which cells were used, and how
the generator volts in the files map to the paper's V/cm. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/001517-semenov-2026-01.yaml`](../../attempts/001517-semenov-2026-01.yaml).
