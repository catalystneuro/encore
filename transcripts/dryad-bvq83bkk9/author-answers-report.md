I re-ran the two claims the answer bears on, updated the notebooks, conclusions and attempt record, and ran lock, `all` (all five notebooks pass), `check` (0 errors) and `handover`. Nothing is committed or pushed, and I did not verify my own work.

**The question.** It asked how to judge a 95% bound that lies within Monte Carlo error of 0, given that the paper's code sets no seed. The reader answered that the paper gives no rule, and that its tables judge each bound by its unrounded sign. Both criteria now name two seed readings: (1) one run with a recorded seed, and (2) a set of seeds, where a term counts as excluding 0 only if it does so in most of them. When the two readings disagree, the claim is blocked as `methods_underspecified`.

**What I changed.** Before, I had used ten other seed sets only for the single term at the line. Now all ten are run for every preliminary model under filtering readings (a), (c) and (d). "Most" means more than 5 of 10; the criterion does not fix the number of sets, and the record lists that as a deviation. The notebook gained about 5 minutes and runs in 380 s.

| Claim | Earlier | Now |
|---|---|---|
| s4-s6-spring-migration-temperature-none | not reproduced | blocked, `methods_underspecified` |
| s6-autumn-ahy-recent-wintering-prebreeding-precipitation-none | not reproduced | blocked, `methods_underspecified` |

- **Spring migration temperature.** With the recorded seed it is not reproduced, as before: the chain-4 HPD interval of MinTempNextSpringMig in the spring AHY model ends at -0.0002 under (a) and -0.0005 under (c). Over the ten seed sets no term excludes 0 in most of them. The most is that same HPD interval, in 1, 0 and 2 of 10 sets under (a), (c) and (d), and the pooled intervals never exclude 0. So that reading gives reproduced, and the claim is blocked.
- **Recent wintering and pre-breeding precipitation.** With the recorded seed it is not reproduced: under (d) the HPD interval of the tarsus by PrevPrecipWinMo interaction ends at -0.0003. Over the ten seed sets that interval excludes 0 in 1 of 10, and no other term ever does. So that reading gives reproduced, and the claim is blocked.

**A problem the final run exposed.** The Table 3 Stan fits came out different from the recorded run, with the same seeds. The cause is the `-march=native` compile flag, which comes from the paper's Script01: the draws depend on the machine's CPU. On this machine, three further runs gave identical draws. I kept the flag. Each autumn notebook now prints the CPU and shows pd to two decimals. I rewrote the stale conclusions and record numbers from this run's outputs, and added the CPU dependence to the convergence finding. The four Table 3 outcomes are unchanged:
- **table3-autumn-ahy-prior-breeding-temperature:** reproduced, as before.
- **table3-autumn-ahy-prior-autumn-temperature:** reproduced, as before.
- **table3-autumn-ahy-recent-autumn-temperature:** partially reproduced, as before. The slope pd is now 89.98% under (a), 90.01% under (c) and 85.10% under (d).
- **table3-autumn-ahy-prior-wintering-precipitation:** partially reproduced, as before, but please check this one. Under (d), both effects now fall on the wrong side of 90%: intercept pd 89.39%, slope pd 93.60%. The criterion's partial case names only one effect. I kept partially reproduced because signs and means hold under all three readings, and the record says so.

The timing estimates also changed, to 55 minutes for HY and 71 for spring AHY (93 and 77 before). Both are still over the 30-minute notebook limit, so the 16 `too_large` blocks stand. The timing conclusion now points to the printed estimates without restating them, since they change between runs, and the record and README carry this run's values.
