# Vijayan, Wang, Chandra, Chakravorty, Li, Sarbanes, Akhlaghpour & Maimon (2022) from dandiset 000212

Tests the findings of [Vijayan et al. (2022)](https://doi.org/10.1126/sciadv.abn3852) that can be
tested on [DANDI:000212](https://dandiarchive.org/dandiset/000212/draft), which holds the tracking
of 1013 flies in egg-laying chambers: position, island, sucrose under the fly and egg times at 2
frames per second. The dandiset has no published version, so the draft is used.

| Claims | Outcome |
|---|---|
| Two-choice search behaviour; larger chambers; three-choice inhibition and recovery; earlier merge in three-choice chambers (6 claims) | Reproduced |
| Faster egg laying with a 2-mm tunnel, after long absences, with the preferred substrate in the middle; anomalous eggs on 200 mM; inter-egg intervals; motor program in middle chambers (6 claims) | Reproduced |
| Strains release inhibition faster; D. suzukii egg and time fractions; egg numbers; pause differences between strains (4 claims) | Reproduced |
| Longer pauses on harder agarose; DDC>Kir choice falls with temperature; receptor mutants' flat rate curves; long searches; kernel model fails (5 claims) | Reproduced |
| Bounce chamber faster; dwell before fast eggs; transit times; DDC>Kir merge points; overall rate drop; mutants' speed rise (6 claims) | Partially reproduced |
| Fast eggs' pause; D. suzukii has no preference; DDC>Kir egg number and pause unchanged; robustness to search definitions (4 claims) | Not reproduced |
| Agarose choice, merge and time on the softer side (3 claims) | Blocked: metadata insufficient |
| Movable boundaries, glued flies, screen, feeding latency, Gal80 rescues, other receptor mutants and their other chambers (11 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The paper's analysis code is not public, so the search periods, rate functions and bin tests are
rebuilt from its Methods in `egglay.py`. The files agree with the paper's egg counts. Several
experiments are not in the dandiset, and the agarose chambers do not record which side held which
agarose. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/vijayan-2022-01.yaml`](../../attempts/vijayan-2022-01.yaml).
