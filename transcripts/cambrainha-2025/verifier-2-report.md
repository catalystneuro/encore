**Verification report, round 2: Cambrainha et al. 2025 on DANDI:000713 (0.240702.1725)**

The claims file has 18 claims and the attempt record has 18 outcomes: 3 reproduced, 2 partially reproduced, 13 not reproduced, none blocked. Nine outcomes are marked `assumed: true`.

### 1. Outcomes

I agree with 17 of the 18 outcomes. I disagree in part with one, figs3-exponents-stable-with-threshold.

- **No assumption needed (9 outcomes).** These give the same verdict under every reading: sessions-selected, fig3d, figs1, fig4-exponents-active, fig4-exponents-passive, fig4-exponents-nni, fig4bc, figs4 and figs5c.
- **Resting on CV reading (a) (all nine assumed outcomes).** The assumption is stated in each and is reasonable. Reading (a) drops 0 of 11,639 active windows, (b) drops 9,702 and (c) drops 209 (cell 7). The paper calls the exclusion a removal of rare artefacts.
  - fig3a: (a) gives partially reproduced, (c) not reproduced (cell 24).
  - fig3c (both claims), fig4a, figs8: the readings disagree only through CV (b). Note that under the claims file's literal rule an empty grid "cannot meet the criterion", so fig3c is not reproduced under CV (a) whatever the start.
  - figs2, figs5a, figs7: CV (b) would give partially reproduced, partially reproduced, and reproduced respectively.
- **figs3-exponents-stable-with-threshold: agree only in part.** The record states the grid start of 7 (M4) as an assumption. The verdict also rests on a second convention, which is listed only as a deviation: "an exponent with no grid point where 10 sessions contribute is counted as not shown stable".
  - The criterion says the condition must hold "at every grid point with at least 10 sessions contributing". With no such point, that is met vacuously.
  - Read literally, the grid from 7 fails only NNI z (0.083 against an SD of 0.058). That gives **partially_reproduced**.
  - Passive and NNI μ are not evaluable because only 1.7% of windows pass the r² rule (cell 66), so μ was never really tested.
  - I would rate it partially_reproduced (assumed). At minimum, the convention should be stated as an assumption the outcome rests on.

### 2. Sentences the outputs do not support

- **Cell 11:** "the hit rate, phase order and exponent results here do not depend on where the threshold or the grid start is put". This is wrong for the exponents. figs3 changes with the start: from 7 and the 99th percentile it is not reproduced, from the 99.9th percentile partially reproduced (cell 81).
- **Cell 11, and finding 4 (`methods_unavailable`, the κ_surr_max finding):** "not by windows with few active units" and "The windows that set it are not windows with few active units." This holds only for the active-phase maximum (34.29, N = 182).
  - The all-phase maximum used for fig4a and figs8 (O6 (b)) is 48.34. It comes from a passive window of sub-545994 with 87 active units, 84 silent, a rate of 0.031 and CV (a) 3.89. The next value, 36.50, comes from a window with 12 active units (cell 15).
  - With N ≥ 128 the all-phase maximum falls to 34.29, as cell 16 itself says.
  - No outcome changes, because every start was run.
- **Attempt record, fig3c-scaling-hit-rate-higher notes:** "Under the adopted CV reading (a), and under (c), kappa_surr_max is 34.29 (O6 (a)) or 48.34 (O6 (b))". Under CV (c), O6 (b) gives 34.29, not 48.34 (cell 10).
- **Summary, cell 83:** "judged with the grid started at every threshold below it, and give the same outcome at every start except figs3…". figs3 was run only at the named starts (7, 6.51, 10.43) and on the 4–12 variant, not at every start (cell 81).
- **Attempt record, figs2 notes:** "across the five seeds of the strict surrogate that reading gives partially reproduced or reproduced". This is the verdict of the fig3c sub-test (cell 43). figs2 itself cannot be reproduced, because no session count is within tolerance. The sentence should say so.

The other result cells (22, 25, 31, 35, 38, 41, 44, 48, 52, 55, 58, 61, 64, 70, 73, 76, 79, 82), the README and the remaining notes match the printed numbers.

The `verifications` section gives my round-1 outcomes and reasons faithfully and in my own words. Each of my nine problems appears under a claim: problem 1 under fig3a and fig3c, 2 under fig3a, 3 under figs7, 4 under fig4-exponents-active, 5 under sessions-selected, 6 under figs3, 7 under figs5c, 8 under fig3d, and 9 under fig4bc.

### 3. Round-1 points

**Resolved:**
- **1, κ_surr_max blocking:** the windows that set it are printed, every start was run, and the four blocked claims are now not reproduced (cells 15, 29, 34, 47, 51).
- **2, inconsistent treatment of the kurtosis claims:** all are now tested.
- **4, μ fit:** fitting ranks 1 to K/2 gives μ = 1.06, still outside tolerance (cell 69).
- **6, `stable_eval`:** every grid point is now evaluated (cell 81).
- **8, few-trial maxima in fig3d:** the largest gain with at least 30 trials on each side is added (cell 37).
- **9, unpaired test:** the paired Wilcoxon test is added (cell 78).
- **7, bootstrap:** stated as a deviation, which is acceptable.

**Remaining, and bearing on conclusions:**
- **Kurtosis scale (problem 2).** The surrogate median is 3.64 and the minimum 2.80, against the paper's ≈6. The correlation-matrix variant overshoots instead (surrogate median 15.88, cell 15). Every kurtosis-threshold claim rests on Eqs. 2–5 as printed being the paper's method. This is stated, and asked of the authors.
- **Trial counting (problem 3; claims file, O5).** O5 has no reading that counts aborted trials. Counting them is the only rule that matches the paper's "three to five" trials per window (median 5, cell 18). Under it the outcomes stay not reproduced (fig3c 47.7% of points from 7; fig3d +11.72% at 8 and −22.40% at 12, cell 30), so this is a claims-file point, not an outcome change.
- **Selection (problem 5).** All analyses run on 97 sessions from 68 mice, not the paper's 62 from 44. This cannot be resolved from the files.
- **figs3 convention:** see section 1.
- **Figures:** I still have not compared the results with Figures 3A, 3C, 4A or S8.

### 4. Critical findings

No finding in the attempt record is rated `critical`. I agree with the ratings that are given:
- **Finding 1, `selection_undocumented`: major.** It changes the analysis set of every claim.
- **Findings 6–8: minor.** These are the block order, the trial density, and the `VIS` label with dropout windows; each is evident from the values.
  - The dropout windows of sub-545994 set the all-phase κ_surr_max (48.34 and 36.50). That is evident from the printed N and rates (cell 15), so minor is still the right rating.
- **Finding 9: severity none.** No session is deposited twice and the clocks agree (cells 3 and 7).
