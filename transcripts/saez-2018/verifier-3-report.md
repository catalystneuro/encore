# Verifier report, round 3: Saez et al. 2018 on CRCNS ofc-3

The attempt record proposes a change of outcome for one claim, mixed-effects-robust (`saez-2018-01.yaml`, under `proposed`). No other claim has a `proposed` entry.

| claim id | proposed outcome | agree | my outcome if different | reason |
|---|---|---|---|---|
| mixed-effects-robust | reproduced (assumed: baseline reading (a), per-window time-point reading) | yes | — | See below. |

**Why I agree with mixed-effects-robust**

1. **The numbers come from the data.**
   - Cell 90 builds baseline reading (a) for each trial and electrode by subtracting that epoch's window centred at -100 ms (the mean of [-200, 0] ms) from the epoch. It then reruns `me_fits` over all 114 windows with the same nested REML fit (`saez.nested_lmm`) used for the deposited data.
   - Cell 85 checks that fit against statsmodels MixedLM on three fits. The slopes and SEs agree to four or more significant digits and p agrees within 2%.
   - Cell 90's output for "one, all" under (a) shows 16 of 16 regressors below the threshold, with "corrected p >= 1e-4: none". The largest corrected p is 3.3e-05 (gamble_ind_1). The other three regressor and electrode combinations under (a) give 10, 9 and 8, so only this one passes.
   - Under the deposited HFA the same model gives 14 of 16 (cell 87; risk_1 3.0e-03, exputil_1 1.7e-03). Under (b) it gives 15 of 16 (risk_1 2.9e-02).

2. **The choice it rests on was not made to reach the result.**
   - Baseline reading (a) comes from the claims file's opening comment, which was written before the data were seen. It was not invented by the author.
   - The author kept the deposited HFA as the primary analysis even though that gives not_reproduced here. The proposal follows my round-2 argument.
   - Applying (a) on top of the deposited values is equivalent to applying it to uncorrected HFA, provided the deposited correction was a subtraction. The data are consistent with a subtraction: the game epoch's first window has SD 0.000 over trials and the values take negative values (cell 11: range -96.3 to 311.9, mean -0.133).
   - Under (a), the window that becomes constant is skipped in both epochs (`me_fits`), leaving 112 fitted windows. Bonferroni is still taken over 16 × 114, so the correction is slightly conservative.
   - The pass has a margin of about 3× below the threshold (3.3e-05 against 1e-4).

3. **The criterion is applied as written.**
   - The criterion says "Reproduced when, under one reading, every regressor has corrected p < 10^-4."
   - The readings used are time point (a) (one model per window, a regressor counted in any window, correction over windows and regressors), regressors (a), electrodes (a) and baseline (a). All four are readings the claims file names.
   - The count is taken in `me_count(pwb, 16 * 114)`, which keeps each regressor's smallest corrected p over windows and epochs.

**Caveats for the record (no change of outcome)**
- This pass is the best of the 24 combinations of baseline, time-point, regressor and electrode readings that were run. The claims file's "under one reading" permits that. The `assumed: true` flag should stay, citing both baseline (a) and the per-window reading, as the proposal says.
- My round-2 point still stands: reading (b) is applied to the buttonpress epoch with an estimated offset, measured on 1,572 of 1,753 trials, with the electrode's median used elsewhere (cell 90). The proposal does not rest on (b).
