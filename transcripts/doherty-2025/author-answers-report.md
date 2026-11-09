The reader's one answer adds a third way of counting rates, R3. Under it, seven rate claims that were not reproduced are now reproduced and two are partially reproduced. All nine rest on R3 as an assumption, because the paper does not say which cells it averaged over.

I re-ran the claims, updated the notebook, the conclusions, the README and the attempt record, and wrote in each claim's notes what the answer changed. `lock` and `all` passed (0 errors, notebook ran in 279 s), and `handover` wrote `executed/001444-doherty-2025/handover/`. I did not verify my own work, and nothing is committed or pushed.

## The question

**fig2c-control-it23-rate-activated, and ten other rate claims.** I asked whether the paper also allows a third reading of a population's mean rate, R3. R3 takes the cells that fired at least once in the 4.3 s simulation, with rates over the last 2.3 s and cells silent in that window counted at 0. The other two readings are R1 (all cells of the population) and R2 (only cells with a spike in the last 2.3 s).

**The answer: changed.** The legends fix the time window the spikes are counted in, but not which cells are averaged over. The reader added R3 to the claims file:
- Every rate criterion that read "R1 and R2" now reads "R1, R2 and R3".
- control-it5-silenced-activated (and so pd-it5-silenced-activated) now uses R1 and R3.
- pt5b-highest-rate now accepts R1, R2 or R3.
- Expected values, tolerances and tests are unchanged.

The files hold exactly the cells that fired, so R3 is the set of cells each file holds. In the notebook, R3 is now one of the claims file's readings, no longer a side variant.

## Outcomes per affected claim (new, with the earlier one in brackets)

| Claim | Now | Before | Basis |
|---|---|---|---|
| fig2c-control-pt5b-rate-activated | reproduced | reproduced | R3 is the same as R1, since all 1,435 PT5B cells fire |
| fig2c-control-it23-rate-activated | partially reproduced (rests on R3) | not reproduced | All four values within tolerance; unpaired tests p < 0.001; paired tests 0.016 and 0.011 |
| fig2c-control-it6-rate-activated | reproduced (rests on R3) | not reproduced | 5.82 ± 5.78 and 3.47 ± 5.19; every test p < 1e-10 |
| control-it5-silenced-activated | reproduced (rests on R3) | not reproduced | 3.25, 3.08, 0, 0 |
| control-it4-rate-activated | reproduced (rests on R3) | not reproduced | 2.57 and 4.74 |
| pt5b-highest-rate | blocked, methods_underspecified | blocked | PV5A (an interneuron population) still fires faster than PT5B under R3, so the two readings of "any population" still disagree |
| fig5c-pd-pt5b-rate-activated | reproduced | reproduced | R3 is the same as R1 |
| fig5c-pd-it23-rate-activated | partially reproduced (rests on R3) | not reproduced | Values within tolerance; only the Welch test is below 0.001 (Mann-Whitney 0.0018, paired tests 0.60 and 0.21) |
| pd-it5-silenced-activated | reproduced (rests on R3) | not reproduced | 2.17, 1.25, 0, 0 |
| pd-it6-rate-unchanged | reproduced (rests on R3) | not reproduced | 6.00 and 5.99; no test below 0.05 |
| rest-pt5b-rate-pd-vs-control | reproduced | reproduced | R3 is the same as R1 |
| rest-it4-rate-pd-vs-control | not reproduced | not reproduced | Values within tolerance under R3 (2.57 and 14.13), but the parkinsonian mean rests on 2 cells and no test reaches p < 0.05 (smallest 0.077) under any reading |
| rest-it5a-rate-pd-vs-control | reproduced (rests on R3) | not reproduced | 3.25 and 2.16; every test p < 0.01 |
| activated-pt5b-rate-pd-vs-control | partially reproduced | partially reproduced | R3 is the same as R1; the Mann-Whitney test gives 0.0052, above 0.001 |
| activated-it6-rate-pd-vs-control | reproduced (rests on R3) | not reproduced | 3.47 and 5.99; every test p < 1e-07 |

The nine outcomes that rest on R3 carry `assumed: true` and a deviation saying so. Their question for the paper's authors stays in the record, now noting that nine outcomes depend on it.

I chose "partially reproduced" for the two IT2 claims, where the values match but some tests miss p < 0.001. That follows the earlier treatment of activated-pt5b-rate-pd-vs-control. For rest-it4-rate-pd-vs-control I kept "not reproduced", because no test finds the increase even at p < 0.05.
