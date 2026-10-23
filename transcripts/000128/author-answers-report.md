I took up all three answers and re-ran every claim that used T1 or S2. The notebook now runs reading T2 for trial selection and S1 for tuning. It still prints T1's trial count once, for the record. The entry locks, passes `check`, and runs in 81 s; the handover is in `executed/000128-churchland-2010/handover/`. I changed the notebook, `mcmaze.py` (docstrings only), `README.md`, `entry.yaml` (runtime 2 min) and `attempts/000128-churchland-2010-01.yaml`. Nothing is committed and I did not verify my own work.

## Q1. Proto-trial selection (M1): T1 or T2

**Answer:** T1 is set aside and T2 alone stands. T2 keeps 1786 of 1967 trials (90.8%) and leaves every condition with at least 10 trials.

| Claim | Earlier | Now |
|---|---|---|
| fig3-maze-most-not-maintained | blocked, methods_underspecified | reproduced: 1 of 17 neurons has r ≥ 0.72 (0.765), and 94.1% are below it |
| fig6-peri-movement-space-best | blocked, methods_underspecified | reproduced: wins 24 of 24 combinations; best 0.518 against 0.424 (kinematic) and 0.412 (kitchen sink) |
| fig6-each-dimensionality | blocked, methods_underspecified | reproduced: wins 21 of 22 comparisons (K1) and 19 of 20 (K2); endpoints + max speed scores 0.168 against 0.271 |
| fig6-performance-vs-dimensionality | blocked, methods_underspecified | not reproduced: performance rises from 0.140 to 0.518 but its best k is 14 and it never declines |
| fig7a-shuffled-space-poor | blocked, methods_underspecified | reproduced: H1 and H2 hold; shuffled best 0.227 against kinematic 0.414 or more |
| recordings-jarray | partially reproduced | partially reproduced: unchanged; reading (b) is now T2 only (1786 trials) |

## Q2. Tuning measure (M6): can S2 stand

**Answer:** S2 is dropped throughout and S1 alone stands. S2 had given no neurons for the correlation claims and 6 for the PD claims, so dropping it changes no outcome. It does change several recorded values, because they previously came from T1.

| Claim | Earlier | Now |
|---|---|---|
| fig4d-mean-correlation-jarray | not reproduced, measured 0.025 / 0.054 (T1) | not reproduced, measured 0.051 / 0.072, p 0.42 to 0.61 |
| fig4-no-separate-populations | reproduced | reproduced: dip p 0.683; 16 of 17 neurons have \|r\| < 0.5 |
| fig4e-correlation-time-course | reproduced | reproduced: mean r 0.012 at onset (p ≥ 0.854); 80 to 82% of the drop comes after -200 ms |
| prep-dimensionality | not reproduced, measured 18 (T1) | not reproduced, measured 15 (all 182 units: 18); the target is 7 to 11 |
| fig7b-window-start-slide | reproduced, measured 0.918 (T1) | reproduced, measured 0.959 (K2: 0.957) |
| fig7d-pd-consistency | reproduced | reproduced: wins 11 of 11 comparisons. Values moved slightly (0.742 → 0.752) because removing readings changed the random draws |
| ap-location-no-effect-on-correlation | blocked, metadata_insufficient | blocked, metadata_insufficient: unchanged; the unit-id digit check is now T2 only (r -0.432, p 0.084) |

## Q3. suppfig1 normalising maximum

**Answer:** the paper does not say, so the criterion now names both readings: (a) the maximum over all conditions and times, and (b) the maximum over the four plotted conditions. The attempt already ran both, so the method is unchanged.

- **suppfig1-population-averages:** reproduced before, reproduced now. Under T2 with S1 the ratios are 0.240 (a) and 0.274 (b). R1 holds under both, and R2 holds under (a) only.

Each affected claim's notes in the attempt record say what the answer changed. The notebook conclusions, summary, header and README are updated to match. Every number they cite appears in the final executed outputs.

The outcome counts are now 11 reproduced, 1 partially reproduced, 3 not reproduced and 7 blocked: 5 for data_missing and 2 for metadata_insufficient. Before the answers they were 7, 1, 2 and 12.
