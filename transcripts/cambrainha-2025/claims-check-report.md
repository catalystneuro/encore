I made six changes to `claims/cambrainha-2025.yaml` and think it is ready for an attempt. Nothing was committed or pushed.

**Checker result** (it passed before my edits and again after): `claims/cambrainha-2025.yaml: 18 claims, 18 quotes, 12 statistical values, 0 problems`

**Changes, by claim**
- **fig3a-kurtosis-broader-than-surrogate**: the criterion tested the most common surrogate kurtosis against 6. Appendix 3 says the *lowest* surrogate kurtoses are around 6, so it now uses the minimum, with the 5th percentile as a named variant.
- **figs1-other-window-lengths**: the statement says the relative gain departs from zero around kappa of 7 (Figure S1 legend), but the criterion never tested that. I added an onset test within 0.7 of 7 (the 10% default) and marked the 8 to 12 range as the file's own choice.
- **figs5a-firing-rate-order**: the text says only that the firing rate "varies almost monotonically"; the legend is what expects a decrease. I reworded the statement to match. The criterion now needs a negative Spearman correlation of size at least 0.8 (named as the file's measure); before, any negative value passed.
- **figs5c-hit-rate-firing-rate-nonmonotonic**: the paper says only "not monotonic", but the criterion required an interior maximum. Any change of direction larger than one bootstrap SE now counts.
- **figs7-fatigue-halves**: the 8 to 12 threshold range is now marked as the file's choice.
- **fig4-exponents-passive** and **fig4-exponents-nni**: the paper never states n for its tests. Each `n` of 62 sessions per phase now says it is the file's reading (O11 (a)).

All the quotes, p-values, exponent means and SDs, and the 62, 44, 43 and 24% ± 3% figures match the text. Each main finding has a claim, and every claim comes from this paper.

**Still open** (recorded in the `checks` entry)
- I couldn't check the values the file reads from figures, because no PDF renderer is installed here. These are kappa_surr_max near 7, the plotted ranges ending at 12.5 and 15, the Figure S5A firing rates of 0.09 to 0.16, and the firing-rate threshold range of 0.05 to 0.20. They only set the grids the criteria are judged on; none is an expected value.
- The paper drops windows where the mu fit has r² < 0.85, so the mu tests may have fewer than 62 sessions per phase.
- The last p-value in Supplement V is printed as μ1 vs μ2 and is read as μ1 vs μ3, as the file already notes.

**Ready:** true.
