The file is ready for an attempt: the last check says `ready: true`.

**Checker:** `claims/001340/10.1371-journal.pcbi.1013226.yaml: 39 claims, 39 quotes, 63 statistical values, 0 problems`. Before my edits it gave the same result with 38 claims.

I read the paper's code (github.com/Wilbrecht-Lab/cogmodels at commit 589555c). Every code choice the opening comment cites matches the code. The quotes, p-values, confidence intervals and tolerances are correct. The tolerances follow the file's own rule: the larger distance from the value to a bound of the interval, the paper's ± where it gives one, otherwise 10%.

**Changes, by claim**
- **fig2c-no-bayes-vs-complex-rl:** the paper does not say whether its t-tests are one- or two-sided. The one-sided tests are now shown as a variant of this absence test.
- **figs8-brlwrp-no-difference:** the Methods cite S8 Fig for BRLfwr against the unrestricted BRL (BRLfw), but the legend names BRLwrp. I named the conflict and added BRLfw against BRLfwr as a variant.
- **figs7-no-change-across-sessions:** "model fitness" is not defined. The criterion now has two readings: AIC relative to RL4p, and AIC per trial. I also cited the Discussion, which says these fits are to behaviour.
- **fig4f-bayesian-rpe-fit** and **fig4h-rpe-only-llk:** the expected values were listed but never used in the verdict. They now decide it. If only the ordering of the models holds, the claim is partially reproduced.
- **fig4h-nonnegative-rpe-aaa:** the statement said "the RL models" drive the RPE toward zero. The paper says this only of RL_meta and PearceHall, so the statement now names them.
- **fig4j-lmer-stay:** added fig4i-model-runchosen to `depends_on`, because the criterion uses its model regressions.
- **figs4-lmer-feature-sets:** new claim, because S4 Fig had none. The readings the legend leaves open are named in it.

**What remains open**
- Several qualitative claims depend on thresholds or tests the paper does not give: fig2b, figs2, fig4de, fig4g, fig4-consistent-after-reward, fig4i-model-runchosen and figs4. Each one is named as a reading in its criterion, and the outcomes depend on these readings.
- Reading (b) in rl4p-learning-rates (fits per session) is a guess based on the narrow interval, not something the text says. I kept it as a reading.

Only the claims file changed; nothing was committed.
