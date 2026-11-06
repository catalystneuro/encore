# Nair, Klaassen, Arato, Vyssotski, Harvey & Rainer (2018) from CRCNS bf-1

Tests the findings of [Nair et al. (2018)](https://doi.org/10.1073/pnas.1712431115) that can be
tested on CRCNS data set [bf-1](https://doi.org/10.6080/K0MK6B2Q), which holds basal forebrain (BF)
LFP from six rats, two home-cage and two arena sessions each, in 2-s segments at 400 Hz with one
movement-sensor value per segment. The ACC and VC recordings, single units, object sessions and
behaviour scoring of the paper are not in it.

| Claim | Outcome |
|---|---|
| BF gamma reduced by 35% in the arena (Fig. 3A) | Partially reproduced (48%) |
| Reduction significant in each recording | Reproduced |
| Arena gamma unrelated to movement (Fig. 3B) | Reproduced |
| Home-cage gamma increases with movement (Fig. 3B) | Not reproduced |
| Suppression holds for movement-matched epochs (Fig. 3B) | Not reproduced |
| Home cage above both arena sessions, second session 5.6% above the first (Fig. 3C) | Partially reproduced (by paired t tests, not Tukey; session order not in the data set) |
| Arena gamma rises with time in the arena, r = 0.72 (Fig. 3D) | Partially reproduced |
| Delta, beta higher and theta lower in the home cage (Fig. S2) | Reproduced |
| Theta and gamma power unimodal within each condition (Fig. S3) | Reproduced |
| Gamma excursions during arena exploration (Fig. S5) | Partially reproduced |
| Bipolar recordings; consistency over days | Blocked: metadata insufficient |
| Rapid switch on transfer, behaviour, objects, units, ACC and VC (16 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Rat 3's home-cage session 2 is a second deposit of most of its session 1 and is counted once. The
data set gives one BF signal per rat, so tests run over six rats where the paper used 22
hemispheres. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-bf-1-nair-2018-01.yaml`](../../attempts/crcns-bf-1-nair-2018-01.yaml).

- `reproduce_nair_2018.ipynb`: the analysis. It streams the 22 MB archive from the CRCNS bucket.
- `bflfp.py`: streaming the archive from the CRCNS bucket, band powers per segment, the SI's
  artifact rule, 10-s epochs and the excursion detection. Other notebooks on this data set can
  import it.
