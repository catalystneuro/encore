## Check of `claims/001950/10.64898-2026.04.10.717727.yaml`

**Checker result:** `44 claims, 44 quotes, 40 statistical values, 3 problems`

The 3 problems are all VALUE NOT FOUND, for p = 3.0e-4 (fig5g, fig6a) and 3.40e-5 (figs12h). All three are in the paper text, printed as "3.0 × 10 −4" and "3.40 × 10 −5", so the fault is in how the checker matches these numbers, not in the file. The statistical value count went from 41 to 40 because I removed one threshold entry from fig4g.

**Changes, by claim:**
- **fig4g-go-cue-excitation:** removed the `statistics` entry (p < 0.05 per neuron). It is the threshold used to count neurons, not a result, and the paper does not print it.
- **task-iti:** the criterion stated as fact that the interval excludes the trial. The Methods say both "after the 3.0 or 3.1 s trial" and "the times between consecutive cue onsets", so it is now named as open, with both readings kept.
- **Header, plus fig5c, fig5g, fig6a and figs14:** "positive DV coefficient" was used to mean dorsal, but in Allen CCFv3 the DV coordinate grows ventrally. Directions are now stated anatomically, and a header note on coordinate conventions also covers the code's axis vectors used in fig5d, fig5h and figs18d.
- **fig6a-reward-dorsal-anterior:** the legend describes groups of neurons, so I added readings that use the group label (excited by reward or by no reward) as the spatial feature.
- **fig6c-rpe-choice-change:** the criterion gave "minus" as the Methods' operator, but that equation was lost from the text. It now says the difference is read from the word "change".
- **figs17-respond-ignore-axons:**
  - The statement said axons and single neurons differ "in sign". Both have higher activity before ignored trials, and the paper reports only that the fraction of positive t-statistics differs. The statement now says that.
  - The comparison group for cortex-projecting neurons is now the legend's "population of single neurons". The Methods' comparison with non-projecting neurons is kept as a variant.
- **fig6jk-pl-axons-more-rpe:** the Results compare both cortex-projecting neurons and axonal dF/F with the single-neuron population. The statement now names both, and the criterion has a reading that includes cortex-projecting neurons.
- **figs16-pupil-autocorrelation:** the paper gives τ no unit. "s" is removed from the statement, and the criterion reads τ either as seconds or as lags of the 0.5 s window.

**Still open:**
- The checker's three p-value misses, described above.
- I did not check the code details the criteria cite (windows, permutation counts, k = 30, populations, axis vectors) against the code repositories, because they are not in this checkout. They stand as the claims author recorded them.
- Two minor anatomical results have no claim: cortical co-projection to nearby regions (Figures S4d to S4g) and dendrite orientation (Figure S6). They are not main findings, and this dandiset cannot test them.

All other quotes, sources, statistics and expected values matched the paper. Each main finding of the abstract and Results has a claim.

**Ready:** yes. The `checks` entry at the end of the file has `ready: true`. Nothing is committed.
