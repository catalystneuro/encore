I checked `claims/wang-2014.yaml` against the paper and its supplement. After my corrections it is ready for an attempt.

**Checker result**, run before and after my edits: `claims/wang-2014.yaml: 29 claims, 28 quotes, 13 statistical values, 0 problems`

**Changes, by claim**
- **fig1d-theta-power**: The Results report a drop in theta "amplitude", but Figure 1d and the Methods give normalized power. I added amplitude (the square root of normalized power) as a second reading, run alongside power.
- **fig3c-model-theta-builds-fields**: The paper gives no measure of theta sequences or firing fields in the model. The criterion now says its measures, and its reading of "several cycles" as more than three, are fixed here and count as a deviation.
- **fig4b-linear-track-info**: This claim says there is no difference. The old criterion used a one-sided test for muscimol being lower, a direction the paper never gives. Since the muscimol mean is the higher one (0.95 against 0.81 bits), that test could not fail and could not give the paper's P = 0.23. The claim is now decided by a two-sided paired Wilcoxon signed-rank test, and the one-sided p in each direction is reported.
- **fig5c-platform-info**: The threshold was p < 0.001, which the paper never uses. I changed it to p < 0.0001, the bound printed on Figure 5c. I also added readings for which groups go into the Kruskal-Wallis test, since the paper doesn't say: the two novel-platform groups, or the four groups of Supplementary Fig. 12b.
- **figs14-no-stable-fields**: The criterion added conditions beyond the paper's test (segment means below control, a rising trend). The protocol judges a "no difference" claim on the paper's test alone, so I removed them. The segment means are still reported.
- **fig4b-linear-track-theta-modulation**: I noted that which panel its P < 0.0001 belongs to is an assumption (see below).

**Open**
- Figure 4b prints P = 0.022 and P < 0.0001, but the extracted text doesn't show which panel each belongs to. No PDF renderer was available to settle it, so they stay read as firing field information and theta modulation.
- The Methods say "All of our tests were one sided" but never give a direction. The claims take each direction from the statement, which the paper does not confirm.
- The 2D model result (Supplementary Fig. 10a) has no claim. It is a side result, so the file is fit without it.

All other claims, quotes, sources, statistics and tolerances matched the paper. Every main finding has a claim, and none comes from the data description.

The `checks` entry is added with `ready: true`. Nothing was committed or pushed.
