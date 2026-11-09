The claims file for DANDI:000351 is ready for an attempt. I made six corrections, recorded under `checks`, and nothing was committed.

**Checker result:** `38 claims, 36 quotes, 62 statistical values, 1 problems`. The one problem is a false alarm. The checker could not find p = 3.4e-05 in `fig6i-learning-despite-inhibition`, but Table S1 prints "3.40×10-5", which YAML stores as 3.4e-05. I left it as it is.

I read the paper's code (github.com/namboodirilab/ANCCR at commit cff4414). The code details the criteria cite for Figs 4I, 6D, 6G, 6I, S8E, S8L and S12F match it.

**Changes, by claim:**
- **`fig4hi-delay-change-behavior-changes`:** the criterion now says the changing and constant models are fitted to the per-trial values, not the cumulative sums, as the code does. It was unstated.
- **`fig4hi-delay-change-dopamine-unchanged`:** the same per-trial fitting is now stated. A mean ΔAIC below 0 (the constant model fits better) now counts as "no change found"; that case had no outcome before.
- **`fig6b-no-backpropagation`:** the statement now says the late response "does not differ from" the early one, where it said "does not exceed". The paper's test is two-tailed.
- **`fig6g-inhibition-magnitude`:** the criterion now names three readings for the expected −0.6.
  - The code divides a 0.5 s inhibition window by a 0.5 s reward window. The Methods' 1 s reward window gives about half that ratio.
  - Supplementary Note 10 describes the −0.6 as a dopamine level, not an area ratio.
  - The value holds if it matches under any of the three readings.
- **`figs12f-pre-cs2-licking`:** the statement now says the increase is a main effect of session. It said the increase holds "in both groups", which the two-way ANOVA does not test.
- **`fig5b-simulated-intermediate-cue`:** I added the Fig 5B reward-ratio tests (against a null of one) to the statement, quote, statistics and criterion. The legend reports them and the claim had left them out.

**Still open (recorded in the file):**
- **`fig4ef-dopamine-leads-behavior`:** the signs of the two paired t-values imply opposite subtraction orders. The criterion takes the direction from the Results text.
- **Tests set by the reader:** five claims (`fig4jl`, `fig4p`, `fig6d-cs2-below-cs1-late`, `figs5`, `figs6`) use a test the paper does not give. Each says so, and the paper offers no alternative.
- **Minor findings without a claim:** Figs S11B-C, S9, 2A-C, 2G and S13E. None has a test.

All eleven tests in the paper have claims, and every claim comes from this paper.
