**Round-2 verifier report: 001544-kim-2024-01 (Kim et al. 2024, DANDI:001544 v0.260827.1410)**

Counts are taken from the claims file and the attempt record. There are 31 claims; 7 are tested and 24 are blocked as `data_missing`. The record has 31 outcomes: 3 reproduced, 4 not_reproduced and 24 blocked. Two outcomes are marked `assumed: true`: figs12a-sag-higher and figs12-app-differs-from-all.

## 1. Outcomes

| Claim | Record | Agree? | Basis (notebook cell) |
|---|---|---|---|
| fig6f-max-firing-rate | reproduced | Yes | Cell 21. APP and AV are above ALL in every cell set, under both readings and with t on the mice df. Kruskal-Wallis and Mann-Whitney agree. |
| figs12a-sag-higher | not_reproduced, assumed | Yes | Cells 25–28. AV is not above ALL in the main set: (a) p = 0.087, (b) p = 0.24. |
| figs12-other-features-shared | reproduced | Yes | Cell 41. 9, 7 and 10 of 10 features show no difference by ANOVA and by the mixed model; Kruskal-Wallis gives 7, 6 and 9 of 10. Every count is 6 or more. |
| figs12-app-differs-from-all | reproduced, assumed | Yes | Cell 45. All four features differ under (a) and (b) in `all` and `no_FL`. |
| fig6g-av-more-hyperpolarized | not_reproduced | Yes | Cell 31. APP against AV p ≥ 0.34 in every set; reading (b) cannot be run. |
| fig6h-av-smaller-ahp | not_reproduced | Yes | Cells 34–35. |
| fig6-app-less-excitable | not_reproduced | Yes | Cell 38. |
| 24 blocked claims | blocked: data_missing | Yes | Unchanged from round 1. |

**The two assumptions.** Both are stated and reasonable. Each rests on using all 24 ALL cells, because the paper's 21 cannot be identified (cell 5).
- **figs12a:** without the `_FL` cells, reading (a) gives both pairs but reading (b) misses AV (p = 0.12). Under the claims file's rule, that set would make the claim blocked as `methods_underspecified`.
- **figs12-app-differs:** in `change20`, 3 of 4 features differ by (a) and 2 of 4 by (b). That would make it partially reproduced, or blocked if the readings are judged to disagree.

None of the unmarked outcomes changes with the cell set.

**Where the claims file misreads or under-specifies the paper.** I report these and have not corrected them.
- **Normality rule (still open from round 1).** The STAR Methods say "Non-parametric tests were conducted if the data failed these tests". The claims file's opening comment repeats this, but no criterion uses it. A question to a reader is pending.
- **Figure S13 (new).** figs13-other-morphometrics says the S13 features are "not known here … needs the supplement". The supplement now in `paper/` names them: dendrite orders, branching angle, convex hull volume, dendrite length, branch points, terminal points and maximum segment length.
- **Convex hull volume (new).** fig6j-convex-hull-area says APP has a smaller convex hull area "(and volume)". The S13 legend reports no significant difference in convex hull volume (S13C), which contradicts the Results sentence. Both claims are blocked, so neither point affects an outcome.

## 2. Statements the printed numbers do not support

- **Cell 23 (fig6f conclusion):** "3 of 6 APP mice … are above every ALL mouse." The per-mouse table shows the highest ALL mouse mean is 29.00 (CG355). APP mice CC328 (87), CC330 (85), CC396 (65) and CC356 (29.33) are all above it, so the count is 4 of 6. This does not affect the outcome.
- **Attempt record, `findings`, `methods_unavailable`:** "The sag and shared-feature outcomes here change with the cell set." This is out of date. Since the amendment, figs12-other-features-shared holds in every set (cell 41), and its own notes say so. The outcomes that change with the cell set are sag and figs12-app-differs-from-all.
- **Attempt record, `findings` ("One other file has a single sample at -112.9 mV") and the figs12a response ("in one sample"):** the notebook prints only the global minimum, -112.88 mV (cell 26). No cell prints how many samples lie at that value. Cell 26 does print that the same file, 20221214_001, has 7 samples at -105.62 mV, which the record does not mention.
- **Entry README:** "It takes about four minutes." Cell 49 prints 302 s, about five minutes.
- **Summary (cell 50):** the rank tests "change no outcome" is literally true. However, the sag conclusion (cell 29) and the record use the rank tests to choose not_reproduced over partially_reproduced, while the deviations say the outcome follows readings (a) and (b) only. The outcome stands without that argument, because the claim needs both groups and AV fails both readings. The wording is inconsistent and does not affect the outcome.

Everything else checks against the printed outputs. That covers every other sentence of the seven "Result:" cells, the rest of the Summary, the README, and the record's notes and responses. Some examples:
- sag: 45–463 ms at the floor (451 to 4632 samples at 10 kHz), and the intended saturation test fires in 6 cells, 3 of them unsaturated, and misses 2 of the 5;
- 30 of 44 cells under the largest-departure reading of the 20% rule;
- p from 9.1e-05 to 0.041 without the `_FL` cells;
- p ≥ 0.34 for fig6g;
- rheobase 36 against 35 pA, p = 0.92.

**My round-1 reasons in the record.** They are stated faithfully, in my own words, almost verbatim from my report. Where problems 2, 3, 4 and 7 have been folded into the reasons for figs12a, figs12-app, fig6g and fig6h, each still matches what I said. "30 of 31 agree" is correct.

## 3. Round-1 points

**Resolved:**
- **2 (saturated sag):** the notebook now has the floor check, a plot, the code's saturation test on every cell, and a variant without the five saturated cells. The sag outcome no longer hinges on these cells, because AV fails anyway.
- **3 (Wald z):** the t-on-mice-df p-values are added, and the downstroke is reported as marginal.
- **4 (membrane potential under holding current):** the notebook discusses it and adds a check of the 0 pA sweep and of the stimulus before the step.
- **5 (20% rule):** a per-sweep table and both readings of the rule are shown.
- **6 (cell counts):** the 8-of-11-mice check is shown.
- **7 (AHP window):** the truncated windows are printed and their minima fall inside them.
- **Section C, partly:** Mann-Whitney p is now printed, along with the holding-current check and the floor plot.

**Remaining that bears on a conclusion:**
- **Normality rule.** It is a gap in the claims file and awaits the reader. The rank tests would remove the APP half of the sag claim (Kruskal-Wallis p = 0.12) but would change no stated outcome.
- **Which 21 ALL cells the paper used.** Only the authors can answer this. It decides whether figs12a stays not_reproduced or becomes blocked, and whether figs12-app-differs stays reproduced or becomes partially reproduced or blocked. Both are correctly marked assumed.
- **fig6g measure.** The only reading that could be run is measured under the holding current, so the not_reproduced outcome says little about the paper's resting potential. The record now says this.
- **Still unverifiable:** the MATLAB code paths, the v1.0.0 parameters and series resistance.
