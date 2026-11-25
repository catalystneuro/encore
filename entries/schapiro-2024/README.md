# Schapiro, Rittenberg, Kenngott & Marder (2024) from Dryad dataset 1rn8pk129

Tests the findings of [Schapiro et al. (2024)](https://doi.org/10.7554/elife.98844) on
[DRYAD:1rn8pk129](https://doi.org/10.5061/dryad.1rn8pk129), version 310115, which holds the PD, LP
and PY spike times and the temperature of 25 *Cancer borealis* preparations (24 files, one holding two) recorded over
temperature steps in saline, 5 mM Cs+ and Cs+ with picrotoxin, with the authors' summary values,
code, voltage-clamp files and seven raw recordings.

| Claim | Outcome |
|---|---|
| Ih is reduced by Cs+ at 11 and 21 C (two claims) | Blocked: data missing |
| Pyloric frequency at 11 C is lower in Cs+ | Reproduced |
| The saline minus Cs+ difference grows with temperature | Reproduced |
| Q10 is lower in Cs+ (1.3 against 1.7) | Reproduced |
| Two saline protocols give the same 11 to 21 C frequency change | Reproduced, on the deposited per-experiment values |
| Two saline protocols give the same Q10; saline Q10 is the same across designs | Blocked: data missing |
| The frequency drop on warming in Cs+ is carried by the depolarizing phase | Reproduced (the Cs+ + PTX example agrees) |
| In Cs+, frequency falls more often while warming and rises more often when stable | Reproduced (two claims) |
| Picrotoxin restores the frequency change | Partially reproduced, resting on an assumption |
| Picrotoxin keeps the jags; stable-temperature increases order saline < Cs+ < Cs+ + PTX | Reproduced (two claims) |
| PD burst shorter, PD OFF, LP ON and LP OFF advanced, PY unchanged, PD-LP delay shorter, LP duty cycle kept, at 11 C | Reproduced (seven claims) |
| In period-matched cycles LP fires earlier than PD shortening explains | Reproduced |
| LP OFF advances with temperature in saline; PD and PY phases stay constant | Reproduced (two claims) |
| LP ON and LP OFF advance with temperature in Cs+ | Reproduced, resting on an assumption |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The Dryad files need a token to download, so they are staged and checked against their SHA-256
before the notebook runs (`pyloric.DATA_DIR`). The voltage-clamp file of this version holds no Cs+
trial, five of the six two-saline control experiments are deposited only as summary values, and the
picrotoxin summaries enter the two preparations of one file, which the dataset's README does not describe. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/schapiro-2024-01.yaml`](../../attempts/schapiro-2024-01.yaml).
