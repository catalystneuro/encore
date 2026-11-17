**Verifier report, round 3: Vinograd et al. 2024 on DANDI:001037 v0.260609.1402**

The attempt record has one proposed change of outcome, on ed3h-decode-engaged-from-observed. No other claim has a `proposed` entry. Only that claim is reviewed here.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| ed3h-decode-engaged-from-observed | reproduced (assumed: seed-0 fits) | Yes, with two changes to the record | — | See below |

**Reasons for ed3h-decode-engaged-from-observed**

The numbers come from the data:
- **Cell 24 (seed 0):** the observation decoder is trained on all observation trials and scored on balanced engaged-attack trials.
  - Observation-weights reading: accuracy 0.82, 0.68, 0.86, 0.60, 0.63 against shuffled 0.49 to 0.52.
  - Own-weights reading: accuracy 0.87, 0.92, 0.67, 0.67, 0.59 against shuffled 0.49 to 0.51.
  - Both give a two-tailed Mann-Whitney p = 0.0079 (`linattr.mwu` uses `alternative="two-sided"`).
- **Shuffle:** the labels within each observation trial are swapped at random, the threshold is refit and scored on the same engaged trials, 1,000 times per mouse. This matches the Methods and the decoder of ed3g.
- **Cell 26:** the four-seed sweep gives the counts in the proposal.
  - Observation-weights reading: p = 0.0079 with seeds 0, 137 and 1337, and 0.15 with seed 1 (3 of 4 seeds).
  - Own-weights reading: p < 0.05 with seed 0 only (1 of 4 seeds).
  - ed3g has the same 3-of-4 pattern under every split.

The choice was not made to reach the result:
- Seed 0 was fixed as the main reading in round 1, for all claims, before the four-seed run existed. It is the default of the sample code's rslds function.
- ed3g is already recorded as reproduced with `assumed: true` on the same fits.
- Treating ed3h the same way removes the inconsistency I raised in round 2. It is not a choice made for this claim alone.

The criterion is applied as written:
- The criterion asks for both readings to be run, and reproduced at p < 0.05.
- It does not say whether one reading or both must pass. With the seed-0 fits both pass, so the ambiguity does not matter here.
- The own-weights reading's weakness across seeds fits ed4c: refits of one session share only 47% of the five strongest x1 neurons (rslds cell for ed4c). The own-weights projection therefore varies with the engaging fit.

Two changes the record needs when the proposal is applied:
1. **Assumed flag.** The `proposed` block says "assumed on the seed-0 fits as ed3g" but sets no `assumed: true` and adds no assumed deviation. The applied entry should have both, worded as ed3g's.
2. **Seed the code keeps.** On this variant ed3h differs from ed3g, and neither the proposal nor the notes say so. In cell 24, the seed the sample code keeps by its R2 gives p = 0.15 for both ed3h readings (M35R at 0.29 on observation weights; one mouse at 0.33 on own weights). In cell 23, ed3g on that seed gives p = 0.0079 for leave-one-out and fivefold, and 0.15 only for training on one trial. The reason's phrase "the same pattern as ed3g" is accurate for the four-seed sweep only. The notes should report the result on the kept seed. The outcome still rests on the seed-0 assumption the record already uses, so this does not change my verdict.

A small point that does not affect the conclusion: the seed-0 own-weights accuracy range is 0.59 to 0.92 in cell 24 and 0.59 to 0.91 in cell 26. The trials are balanced with a different random draw in each cell (rng 4 and rng 5), and both cells give p = 0.0079.

The claims file does not misread the paper for this claim. ED Fig. 3h and the Results support the statement, and the reported test is n = 5 mice, p = 0.0079.
