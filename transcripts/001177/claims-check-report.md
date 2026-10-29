The checker now passes: `claims/001177/10.1093-brain-awaf312.yaml: 44 claims, 43 quotes, 92 statistical values, 0 problems`. Before my changes it also passed, with 43 claims and 0 problems.

**Changes, by claim:**
- **fig1b-th-loss:** n is now 44 animals, as Table 1 gives it. It had read "sections or mice".
- **figs1d-snc-cells, fig1c-rotarod, figs6-dreadd-validation:** none of these had expected values or a criterion. I added criteria taken from the Supplementary methods and Table 1. For the rotarod, the Methods name Mann-Whitney and Wilcoxon tests while Table 1 uses Kruskal-Wallis, so the Methods' tests are named as a variant.
- **figs1ef-ppx-locomotion and fig2bc-a77636-locomotion:** the paper never gives the baseline window for these. The file had fixed it at -20 to 0 min. It is now marked open, with two readings: -20 to 0 min (the window stated for CNO) and -30 to 0 min (the electrophysiology baseline).
- **figs1-instrumental-learning:** the statement mentions slower latencies, but the criterion never tested them. I added the Figure S1I latency results and latency conditions from Figure S1I and S1L.
- **fig1fg-baseline-similar:** "use the last three baseline sessions" was not in the paper. It is replaced by two readings: every baseline session (as the analysis code averages them), or the stable sessions under the paper's coefficient-of-variation rule.
- **fig1fg-delay-discounting (new claim):** both groups chose the large reward less often as the delay grew (delay effect F(3, 180) = 38.53). This Results finding had no claim.
- **figs2de-omissions-low:** the statement said PPX did not change centre omissions. Table 1 shows a significant PPX main effect on centre omissions in parkinsonian mice. The statement now refers to the per-delay comparisons, and the main effect is recorded.
- **figs2ijk-ppx-washout:** the test name was credited to the figure legend, which names no test; it comes from the Supplementary methods. I also added Table 1's comparisons of PPX on against PPX off, reported without entering the outcome.
- **figs3-a77636-washout-latency:**
  - The omission condition from Figure S3A–B is now in the criterion.
  - "Differs from baseline" had no test, and the paper reports none, so it now asks only that the values sit on the same side of baseline.
  - I added the baseline reward-size effect and noted that Table 1 gives N = 10 where the legend gives 16.
- **fig5cf-cno-locomotion:** noted that the paper states the time windows only for the inhibition experiment; they are applied to all groups.
- **figs8-session-trend:** the statement said the counts of "increase"-type cells rose, but they fall from 41 to 32 between sessions 3 and 4. It now compares sessions 3 and 4 with sessions 1 and 2. The invented "six of eight counts" rule is replaced by "all counts within tolerance", with a partial outcome otherwise.
- **Header:** the file had counted units significant in only one post-drug window as "no change", without support from the paper. This is now open, with two readings: count them as "no change", or leave them out.

**Still open:**
- **Unit pools in Figure S5 and Figure 4:** the paper does not say which sessions these come from. The counts it gives for the first session (105 units) and for all four sessions together (113 increase, 116 decrease) don't match Figure S5's totals (214 parkinsonian and 117 control units). The figs5 and fig4 electrophysiology claims depend on this.
- **Pie-chart percentages (Figures S5D, S8A–B):** I couldn't check these against the figures because no PDF renderer was available. They do agree with the stated unit counts.
- **Table 1 typos:** it gives N = 15 for two of the chemogenetic groups (the legend says 12) and swaps their labels on the area-under-curve row. Both values are p < 0.001, so the outcome is unaffected.

The file is ready, and the check entry records `ready: true`. Nothing was committed.
