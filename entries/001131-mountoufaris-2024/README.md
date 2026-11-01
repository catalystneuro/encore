# Mountoufaris, Nair et al. (2024) from dandiset 001131

Tests the findings of [Mountoufaris et al. (2024)](https://doi.org/10.1016/j.cell.2024.08.015) that can
be tested on [DANDI:001131](https://dandiarchive.org/dandiset/001131/0.260601.1203), which holds the
z-scored miniscope traces of VMHvl Esr1 neurons and the male-directed behaviour annotations of 4 control
and 6 Oxtr/Avpr1a co-edited male residents during interactions with a male intruder.

| Claim | Outcome |
|---|---|
| Units and mice recorded (585 in 5 control, 546 in 7 experimental) | Not reproduced |
| Unilateral editing leaves sniffing and aggression unchanged | Reproduced (assumption) |
| Activity during male interaction lower in experimental mice | Reproduced (assumption, units pooled) |
| Activity of male-responsive units unchanged | Reproduced (assumption) |
| Fewer sniff- and attack-selective units | Partially reproduced (assumption) |
| Attack against sniff decoding equal in both groups | Not reproduced |
| ACHW of all units reduced by about 51% | Not reproduced |
| rSLDS fit quality, time constants, line attractor score, flow fields, ACHW of first-dimension units (six claims) | Not reproduced |
| Post-intruder persistence of the first dimension | Blocked: metadata insufficient |
| Female-intruder, behaviour-cohort, photometry and slice claims (21 claims) | Blocked: data missing |
| Co-expression in an outside RNA-seq atlas | Blocked: not attempted for time |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The files mark neither the pre-intruder baseline nor the intruder's entry and removal, so the
measures in units of sigma rest on an assumed baseline (the frames before the first annotated
behaviour). The rSLDS fits use the settings the claims file takes from the ssm notebook the paper
points to, with four seeds split over two notebooks; they explain 59% of the variance, against 85% in
the paper, and do not recover the rSLDS weights the authors deposited for two mice. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/001131-mountoufaris-2024-01.yaml`](../../attempts/001131-mountoufaris-2024-01.yaml).
