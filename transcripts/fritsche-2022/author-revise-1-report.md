I've worked through every point in the round-1 report. One outcome changed: fig5-repeat-suppression went from partially reproduced to not reproduced. The entry was re-run with `python tools/entry.py all entries/fritsche-2022` (0 check errors, notebook passes in 367 s), and the notes, results and summary now match the new numbers. Nothing is committed.

**Outcome change**
- **fig5-repeat-suppression: now not reproduced, as the verifier gave.** The criterion has no partial rule. The part that fails is the claim's main contrast: orthogonal over blank stays below 1 at 2-back. That holds under every reading and seed, and in the session-level bootstrap the verifier asked for (0.949 to 0.994, and 0.961 to 0.996 over 100 draws). The other failing part, repeat at 8-back, is also not significant in that bootstrap.

**Kept, with what was added**
- **fig3b (reproduced, resting on an assumption).** I added a two-sided table for all 12 readings and the LGN 9-back values (ratio 1.024, corrected p = 0.049). Counted two-sided, no reading meets the criterion and the outcome would be partial; the record now says so, and that RL sits exactly at the threshold of 6. I kept the assumption that only ratios below 1 count, because the paper speaks of significant *adaptation* in thalamus limited to 1- or 2-back.
- **fig8 (not reproduced).** The verifier also gave not reproduced but said it comes from a claims-file misreading. I ran 200 more Poisson seeds: the criterion is met in 38% of them under reading (a, c), and intervals exclude 1 at about the rate chance predicts (0.36 and 0.47 per set over 2 to 10, against 0.45). The partial rule holds under seeds +1000 and +4000. The misreading is now a question for a reader in the new file `questions/fritsche-2022.yaml`; the claim is unchanged.
- **fig1e, fig6d, fig7c (partially reproduced).** The output now lists the mice that fail reading (a). In thalamus they have 2 to 4 units each.
- **Fig. 2 (all reproduced).** I added which units are dropped per tertile and orientation: 77 of the 78 are in the high-OSI tertile. Forming tertiles after the drop gives the same conclusions. The high-OSI 90° test on the ratio scale, with zero-count units kept, gives p = 0.17.
- **Invalid intervals (new variant).** Leaving out the presentations inside them (375 drifting, 7001 static) keeps unit counts and 1-back ratios within tolerance, ratios moving by at most 0.014. fig3b's passing reading still passes, though under the main reading LGN gains a significant 7-back. This variant drops the presentations for all units of a session, not only the probe each interval names.
- **Helper fix.** `adaptation._boot_task` now passes `sign`. No number changed.

**Record**
- The round is recorded under `verifications` in `attempts/fritsche-2022-01.yaml`, with all 31 claims; the verifier disagreed only on fig5.
- I also updated the invalid-intervals finding, the fig2 deviation, and the README row for fig5.
- There is no `findings` entry for this round: that is for round 2, and no finding is rated critical.

**Not done**
- **Problem 4** (fig7a and fig7b-static: the 1-to-20 test family partly meets the 18-to-22 test by construction): left as is. The verifier itself called this the claims file's reading, reported and not to be corrected, so I added no question.
- **Problem 6** (the `noise`-unit filter): the verifier found it reasonable and asked for nothing, so it is unchanged.
