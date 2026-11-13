I revised the attempt for every point in the round-1 report. The entry was re-run with `python tools/entry.py all entries/laboy-juarez-2019`: `check` reports 0 errors and the notebook runs in 46 minutes. Nothing is committed.

## Outcomes now
29 reproduced, 13 partially reproduced, 7 not reproduced, 1 blocked (it was 28 / 14 / 7 / 1).

| Claim | Before → now | Why |
|---|---|---|
| fig1e-best-combination-includes-cw | partial → reproduced | Sequences now use same-direction trials only (B5). The Methods list 252 two-whisker sequences and no opposite-direction pairs. The fractions are 0.694, 0.851 and 0.456. Pooling the opposite-direction trials back in is kept as a variant. |
| fig3g-binary-decoder | not → partial | I now average three refits of 10,000 ensembles each, and handle constant-curve sets as described below. N = 10 gives 0.633, inside the band but only 0.003 from its edge, so the result is fragile. N = 100 gives 0.857, above 0.81 but not above 0.9. |
| fig7a-dt-half-width | reproduced → partial | I took the verifier's reason: the suboptimal half-width is undefined, so the two half-widths cannot be compared. |
| fig8c-awake-cw-stronger | partial → not | The criterion's partial rule needs the t-test to hold, and it does not (p = 0.0021). |

I kept three outcomes the verifier would rate not reproduced, and recorded the disagreement:
- **exp1-cw-sw-comparable-firing**: partial. The spontaneous rates match; the maximal evoked firing fails only in the claims file's unit.
- **supp4-selectivity-at-high-rates**: partial. The peak test holds; the group counts fail.
- **fig4c-sw-tuned-decoding**: partial. SW-tuned decoders beat CW-tuned at every ensemble size, but CW-tuned decoding is not clearly above chance.

## What I added or corrected
- **B1, the shuffle test.** I added a calibration on a null built from the real data. It gives p < 0.05 for 24.6% of sets, though FDR control then selects none of them. The cell prints histograms of the measured and null p-values. Calibrated on that null, the measured p-values give 162 selective sets, against the paper's 187.
  - A new section re-runs all 20 selective-group claims on the 187 sets with the smallest p.
  - The outcome changes for four claims (supp4, fig7a, fig3g, supp8) and, under one reading, for fig6b-enhancement-not-different. These five are marked `assumed: true`, keeping the Methods' procedure as the main reading.
  - supp8 stays not reproduced at 0.584 against a bound of 0.585, a fragile miss. On the 187-set group it reaches 0.595, inside the band.
- **B2, sets whose best curve is constant across dt.** Their responses are now taken over all dt and their decoders use all their trials. This is recorded as an assumption. The fig7f notes now say that readings (a) and (b) count these sets as inbound only because of the tie at −50 ms.
- **B3, dt smoothing.** I ran two more ways of scoring held-out trials. Neither produces any unsmoothed curve, so the claim stays not reproduced. The notebook also prints where the likelihood peaks. I removed the unused `dt_smooth` and the other unused helpers.
- **B4, Hz reading.** Read as a rate in Hz, the best single-whisker responses (4.64 and 4.80 Hz) fall within both tolerances. I added this as a variant and put the question in `questions/laboy-juarez-2019.yaml`. The claim is unchanged.
- **Smaller points:**
  - B6: refits, more ensembles, and the Monte Carlo errors are now printed.
  - B8: a variant with positive dt ranges that mirror the negative ones.
  - B9: supp4 is now also run under O3 (b).
  - The section C outputs: the experiment 3 field names, the raw direction fields of the 20170510 trials, and the experiment 1 measures under sham reading (b).
  - The finding on the 20170510 recordings is corrected. About half the trials of each pair with whisker 3 or 8 have opposite directions, and the pair 3-8 has only opposite-direction trials.

All notebook conclusions, the summary, the README, the record's notes, and a `verifications` round-1 block for all 50 claims now match the final numbers.

## Not done
- I did not make the calibrated or 187-set group the main reading. The Methods describe the test as run here, so it stays the main one, and the dependence is shown and marked as an assumption.
