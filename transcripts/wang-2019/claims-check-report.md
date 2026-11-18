I've reviewed `claims/wang-2019.yaml` against the paper and the file is ready for an attempt (`ready: true`).

**Checker result:** `claims/wang-2019.yaml: 25 claims, 25 quotes, 12 statistical values, 0 problems`. That was the result both before and after my edits.

The quotes, sources, p-values, n's and the expected values (APD80 of 50.9±5.1, 60.6±4.1 and 46.5±9.1 ms; 8 of 9 rabbit hearts; 7 of 8 mouse hearts) all match the paper. Each main finding has a claim, from the abstract through Figs. 1 to 9, and every claim comes from this paper. No claim ids were changed.

**Changes, by claim:**
- **fig1a-rabbit-hr-increase:** the criterion said the Methods call for a two-sided t-test. The Methods don't say, so two-sided is now marked as this file's reading.
- **fig1bc-rabbit-ap-cat-response, fig4ab-rabbit-paced-shortening, fig6ab-mouse-paced-apd-prolong:** the "majority of hearts" rule was made up; the paper shows one example heart and no test. It is now one of two named readings, with a paired t-test across hearts as the other. For fig4ab, the paper doesn't say what "to a lesser degree" is compared against, so that is now named as open (read as the free-rate hearts of Fig. 1).
- **fig2a-rabbit-monotonic:** requiring significance at 60 s is not in the paper, so it is now labelled as this file's reading.
- **fig2d-mouse-biphasic-apd:** the file now says n=5 comes from the Fig. 2D legend, since the abstract gives no n. I also added a test that APD peaks near 15 s, which the statement claimed but the criterion never checked.
- **fig3f-constant-pacing-sns-prolongs:** the statement had settled "prolonged compared to baseline" as "longer than without SNS", which is one of two possible readings. It now uses the paper's wording, and the criterion keeps both readings. The criterion now also tests that APD tends to shorten in both conditions (it only checked without SNS) and that the biphasic response is gone.
- **fig4cd-activation-unchanged:** I removed the made-up 10% threshold and the base-apex test. The claim is now reported descriptively, and the "in phase" part has a named reading.
- **fig4g-5f-rabbit-base-apex:** the criterion now says which hearts: the free-rate rabbit hearts of Fig. 5 (n=4).
- **fig5c-rabbit-free-rate-reversal:** the paper gives no count of hearts, so that is named as open and read as a majority.
- **fig6e-mouse-repolarization-unchanged:** the count is now tied to the paced mouse hearts of Fig. 6.

**What remains open:**
- No PDF was supplied, so I couldn't see the figures. That leaves unknown which time points were sampled, where the base and apex regions are drawn (Figs. 5E and 7E), and which points carry the asterisks.
- Several method details are this file's readings because the paper doesn't fix them: the window for "during SNS", what counts as "monotonic" or "similar", how the direction of repolarization is measured, the base and apex regions, and the "majority" counts. Each criterion now says so, and any result that depends on one should be marked that way.

All changes, with reasons, are logged under `checks` at the end of the file. Nothing was committed or pushed.
