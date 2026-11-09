The claims file for 001619 is ready for an attempt (`ready: true`). I corrected 17 claims and the opening comment; three problems remain open.

**Checker:** `48 claims, 46 quotes, 13 statistical values, 0 problems`, both before and after my changes.

All quotes, sources, p-values and expected values match the paper, and every claim comes from this paper. Every main finding has a claim: lick and breath coordination, swallow pauses, the activity maps, the premotor network and rhythm site, the coupled oscillators, and the descending control at lick onset.

**Changes, by claim**
- **Opening comment:** added the protocol's rule for readings. When a method detail can be read more than one way, every reading must give the same outcome, or the claim is blocked as `methods_underspecified`. "Under one reading" is kept only where the doubt is about what a number counts (O4, O5, denominators, the unit of a test).
- **15 claims** used "under one reading" for method readings, which the protocol does not allow. These now say "under every reading": fig2-licking-breathing-tuned-counts, fig2-swallow-modulated-counts, fig2f, fig2h, ed7h, ed8bc, ed8i, fig3b, fig4d, both fig4g claims, ed12c, fig4h, fig5c, fig5f.
- **fig2-licking-breathing-tuned-counts:** the 10% and 25% thresholds for "partially reproduced" were credited to the Methods, which only say the proportions were robust. They are now named as a standard choice. I also added two readings, because the text doesn't say whether 3551 and 1015 include the 182 units tuned to both.
- **ed1-unidirectional-models-fail, fig1k:** the statements said "so" where the paper says "suggest". ed1 now also names the latency, the cycle count and its test as choices, since the paper gives none.
- **ed7-glm-separate-clusters:** the criterion didn't work. It asked whether two sets "overlap" when the way they were built means they can't, and it added a "posterior" position the paper doesn't give. I rewrote it from Extended Data Fig 7c-d.
- **ed1bc, ed6e, ed8e, fig3a, fig3ce:** methods the paper doesn't give (such as expiration onset, the peak window and the overlap rule) are now named as choices.
- **fig2g:** "in XII, V and IRN" now reads "in each of".
- **ed10-site-classes:** noted that the three site classes add up to 33 of the 46 sites, and that the paper doesn't say whether the 4 transient sites are among the 11.
- **fig5e:** "n: 11 mice" was a guess, since the paper gives no n for the paired test. It now says so, and the criterion offers two readings: mice or sessions.
- **fig5f:** the bootstrap was described as "paired", but those trials aren't paired. It now resamples within each condition.

**Still open**
- The cross-correlation analysis (O6) cites a Methods section that doesn't exist, so its readings are reconstructions. fig4g, fig4h and ed12c are likely to be blocked as `methods_underspecified`.
- fig1f-inspiration-between-licks judges "never" with a 5% threshold that the first reader chose; the literal reading is only reported.
- I didn't check the opening comment's details from the analysis code against the repository; they are as the first reader recorded them.

Nothing is committed or pushed. The only file changed is `claims/001619/10.1101-2025.01.27.635041.yaml`.
