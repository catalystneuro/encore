The claims file is ready for an attempt. Its last check entry has `ready: true`. Nothing is committed or pushed, and only the claims file was changed.

**Checker result:** `42 claims, 41 quotes, 85 statistical values, 0 problems`, both before and after my edits.

I checked every claim against the main text, Methods, figure legends and supplement. The four supplementary tables are images in the PDF, so I rendered them and confirmed that all the numbers the file took from them are right.

**Changes, by claim:**
- **beh-tom-age:** the statement now also covers the DCCS-against-age correlation (tau = .20). The claim already tested it, but the statement left it out.
- **beh-fb-dccs:** the statement now says failers did worse than both other groups, as the paper says. Against inconsistent performers the difference is only marginal (p = .052).
- **irc-williams:** the criterion picked the partial age correlations without saying the paper leaves this open. It now names both readings: correlations with motion as a covariate, and without.
- **irc-3yo-nonbilateral:** the paper does not list its bilateral pairs. I added a second reading that drops only the two pairs it names (TPJ and insula).
- **rc-child-adult-timecourse:** I removed "more so with age" from the statement and the "rises with age" condition from the criterion. The paper does not claim a rise, and the Pain value at 4 years (.56) is below the one at 3 years (.60).
- **supp-table4-other-networks:** 20 of the 25 values sat only inside the text describing other values. Each is now its own expected value, with a 10% tolerance.
- **face-rc:** added the 3-year-olds' face event count (4) as an expected value; the statement already gave it.
- **Header, note P9:** it said every partial correlation against ToM score is Kendall. The one for maturity against ToM score is Spearman, so I corrected it.
- **Header, Rule S (the shared pass/fail rule):** it now says how a test with an exact p is judged: on the same side of .05, or of the claim's corrected threshold, as the paper. Before, a value like p = .049 had no clear rule.

**Open:** the paper's code is only available on request, so these stay as named readings in the criteria:
- the threshold for the reverse-correlation t-tests,
- how the ROI spheres were cut down to the sizes in Supplementary Table 2,
- the scale of the regression coefficients,
- how stimulus times map to TRs for the events.

**Coverage:** the abstract's three main findings and the false-belief result each have a claim. Every claim comes from this paper and its supplement.
