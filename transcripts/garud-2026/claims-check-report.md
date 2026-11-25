Checker result, run before and after my edits: `claims/garud-2026.yaml: 18 claims, 18 quotes, 4 statistical values, 0 problems`

**Changes, by claim**
- **fig4b-long-iti-dip-below-baseline**
  - The source pointed at Discussion paragraph 6. That paragraph is about the recovered value function; the ITI dip is in paragraph 7, so I corrected it.
  - The short-ITI test compared the last bin with the long-ITI dip measure. That measure is below zero, so the test would pass even if the short-ITI trace had returned to baseline. The paper says the reward response "did not resolve before the next trial", so the test is now that the last kept bin is above baseline (ΔF/F of zero).
- **fig2e-velocity-covaries-with-distance**: the statement includes the legend's "average dopamine and velocity covary", but the criterion only tested velocity against distance. I added a matching test for the dopamine and velocity part.

The other 15 claims' statements, quotes, sources, statistics, expected values and tolerances match the paper. No claim draws on anything outside this paper, and every main finding has a claim.

**Still open** (recorded under `checks`)
- **Supplement missing**: the text read has no supplement, and the Methods send "further detailed methods" there. It might settle the open Figure 4 details: how ΔF/F is formed, where the ITI is measured from, the 20-observation rule, how sessions are numbered, and how r is computed. These are named as readings in the criteria. figs2-no-velocity-coupling-without-goal stays blocked until the supplement is read.
- **Code**: the OSF project (https://osf.io/g3e2d/) was not public when the first reader tried it, so no method detail is settled by code.
- **fig4c**: the printed p-value is garbled ("p=so this 1e-4"). The outcome only needs p < 0.05, so this does not change it.
- **fig2c**: the paper names no test for this claim of absence. The criterion borrows the paper's paired t-test and reads ramp amplitude as slope, so the outcome rests on those two choices.
- **fig4b**: the paper reports no test for the long-ITI dip. The criterion uses a one-tailed one-sample t-test, borrowed from the stationary-dip test in the rat data.

**Ready**: yes. The DANDI:001552 claims can be tested from the main Methods with the readings named. I edited only the claims file and did not commit.
