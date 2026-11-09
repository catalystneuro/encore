**Checker result:** `claims/000036/10.1523-eneuro.0280-21.2021.yaml: 26 claims, 25 quotes, 82 statistical values, 0 problems`. I got the same line before and after my edits.

I checked the file against the paper and against the paper's code (wmayner/openscope-differentiation at the cited commit 2d959bd). The code's printed outputs agree with what the file says about cell counts, the 108 sensitivity sets, the Fig. 3-1 area test (chi2(4) = 22.213), the mediation subset and results, the Fig. 4 and Fig. 8 correlations, the Table 1 counts and the UMAP parameters.

**Changes, by claim**
- **design-sessions:** a dataset holding only the 44 analysed sessions, with the missing one in L5 AL, now counts as reproduced. Before, it was only partial, even though the paper itself excluded that session.
- **ext3-8-events-spectral:** the criterion said the code drops trials with zero event ND. It doesn't: the stats code checks that all 2200 trials go into the models, and only the plotting notebook drops them. Any dropped trial is now reported as a deviation.
- **mediation-event-magnitude:** the direct-effect tolerance was 0.0551 and is now 0.0549, the distance to the nearer bound of the CI (0.15). The criterion had two conflicting pass rules; it now has one, "within tolerance". I also added `robustSE = TRUE`, which the code passes to `mediate`.
- **fig6-category-decoding:** the statement says decoding shows no layer or area specificity, but the paper gives no test for that. The criterion now shows accuracies by layer and area without judging them.
- **fig7-snake-highest:** the rule that the other six pairs are not significant cited the wrong legend. It now cites the Extended Data Fig. 7-1 legend, which says four pairs were significant.
- **ext7-1-arousal-mediation:** the statement now says arousal *alone* does not account for the differences, with a mix of direct and mediated effects, as the legend says.

**Still open** (all recorded in the `checks` entry)
- **mediation-event-magnitude:** the paper prints the direct effect as p = 0.002, while the code's output gives p < 2e-16. Both are below 0.05, so the outcome doesn't change.
- **ext3-2, ext3-5, fig6, ext6-1:** the paper never puts numbers on "nearly all", "high" or "most". The thresholds in these criteria are readings, not the paper's, and each claim is blocked if the readings disagree.
- **ext8-1:** the paper names no test for luminance, contrast or spectral energy, so the Pearson tests in the criterion are readings too.
- **Coverage:** Extended Data Fig. 7-2 has no claim, because the paper states no finding from it.

**Ready:** yes. The `checks` entry is added with `ready: true`. Nothing is committed or pushed.
