# Payne, Wiedmann, Eiber, Wong, Senn, Osborne, Keast & Fallon (2020) from SPARC:206

Tests the findings of [Payne et al. (2020)](https://doi.org/10.3389/fnins.2020.619275) that can be
tested on [SPARC:206](https://sparc.science/datasets/206), version 1
([10.26275/kkmb-vun5](https://doi.org/10.26275/kkmb-vun5)), which holds the acute and awake
ECAPs recorded with a pelvic nerve array, colonic pressure during stimulation, cystometry with a
derivative table of void parameters, and electrode impedances. The histology, the c-Fos counts,
the observation notes and the urine-release annotations of the stimulation trials are not in it.

| Claim | Outcome |
|---|---|
| ECAPs recorded in all five anaesthetised rats | Reproduced |
| Anaesthetised peak latencies 1.80, 3.48 and 3.77 ms | Not reproduced |
| Anaesthetised conduction velocities 1.60, 0.82 and 0.78 m/s | Not reproduced |
| Thresholds rise from P1 to P3 (Friedman P = 0.039) | Not reproduced |
| P3 threshold above P1 (Dunn P = 0.034) | Reproduced, under one reading |
| P1 lowest in four of five rats, above P2 in one | Not reproduced |
| Awake peak latencies and velocities | Not reproduced |
| Awake thresholds rise from week 0 to week 1 | Blocked: metadata insufficient |
| Electrode impedance rises after implantation | Partially reproduced |
| 2 of 40 electrodes open | Blocked: data missing |
| Colonic pressure rises in 1 of 3 rats by 2.6 mmHg | Not reproduced |
| No faecal expulsion or erection | Blocked: data missing |
| Table 1 void parameters (six claims) | Reproduced |
| Table 1 comparable to Wiedmann et al. (2020) | Reproduced |
| Stimulus-evoked voiding and non-voiding responses (six claims) | Blocked: data missing |
| Histology, c-Fos and post-mortem (six claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper does not say how its ECAP peaks were found, so every ECAP outcome rests on peak
rules assumed here (four are run; the outcomes are the same under each). The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/payne-2020-01.yaml`](../../attempts/payne-2020-01.yaml).
