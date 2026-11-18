I checked `claims/shi-2013.yaml` against the paper and made three small fixes. The file is ready for an attempt (`ready: true`).

**Checker result line:** `claims/shi-2013.yaml: 28 claims, 26 quotes, 7 statistical values, 0 problems` (same before and after my edits).

**Changes, by claim:**
- **fig3-example-neuron:** the source said paragraphs 1 and 2. The 225 degree peak and the ANOVA P values are both in paragraph 1 of Results, Neurophysiology, so I changed it to paragraph 1.
- **fig4-indx1-means:** the source said paragraphs 4 and 5. The -13% and -31% sentences end paragraph 4 (it carries on past Fig. 4), so I changed it to paragraph 4.
- **behavior-mean-position-sessions:** the criterion used each trial's mean endpoint over the 800 ms hold without citing it. It now cites the Fig. 2 legend, which defines that unit.
- **Header, no change:** the extracted text replaces some signs with a placeholder. I checked them against the PDF's own font tables, and the header's readings are right: "P = 0.52; P = 0.64", the eye-position "P < 0.05", and the Fig. 4 outliers "> 1.5 times" the interquartile range. I also compared all 96 means and SDs of Table 1, with their signs, against the text. They all match, and the largest difference between the two conditions is 0.11 cm, as the claim states.

Every other statement, quote, source, statistic, expected value and tolerance matches the paper. The P < 0.05 thresholds used to count sessions and cells are correctly left out of `statistics`. Every main finding has a claim: behaviour, the ANOVA counts, the correlation test, the two suppression indexes, rate variance, Fano factor, CV2, decoding, and the Discussion controls. None comes from outside the paper.

**Still open (recorded under `checks`):**
- The paper gives no rule for judging many values at once. Two claims use rules it does not state: the Table 1 claims need 90% of values within tolerance, and hold-subepochs needs five of six, with "partial" at three or four. I left these because they decide how a claim is judged; they do not change the analysis.
- **longer-hold-no-difference:** the paper cites only an abstract and names no measure or test. The criterion picks its own measures and a chi-square test, and marks that as an assumption.
- **aborted-trials-nv and longer-hold-no-difference:** these rest on sessions from that same 2009 abstract. The paper does not say whether they are among the 343 recordings. `data` stays at the default for the author to settle.

Nothing is committed or pushed.
