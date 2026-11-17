# Verifier report, round 3: Rich, Liaw & Lee (2014) on CRCNS hc-31

I agree with the one proposed change: fig4c-active-subsets moves from not reproduced to reproduced, still resting on an assumption.

The claims file has 27 claims and the attempt record has 27 outcomes. Only fig4c-active-subsets has a `proposed` entry (attempt record, line 405), so it is the only claim reviewed.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig4c-active-subsets | reproduced (resting on the assumption G-b, linear spacing) | Yes | — | See below. |

**Why I agree (cell 98, conclusion in cell 99)**

1. **The spacing reading.** I couldn't render the supplement PDF, so I pulled Fig. S18 out of the PDF as its embedded JPEG and looked at it.
   * Its gamma-Poisson panels are labelled "environment size (m)", with ticks marked 0 and 50 at the ends of both axes. A logarithmic axis cannot start at 0.
   * The arrows sit at about 10 m and 30 m.
   * In the equal-rate panels, the dense black (inactive) region covers only the left part of the width and thins out across it. In the high-rate panels, the bright strip and the black dots stay within about the first 10% of the width.
   * Cell 98 shows how that strip would look under each spacing. For twice the fitted rate, the exclusive-OR with the 50 m environment is above 0.5 over 0.100 of the width under linear spacing, against 0.627 under logarithmic. Under logarithmic spacing, 10% of the width is only 0.18 m.

   So the figure supports G-b. The evidence comes from the paper, not from the result, and it corrects an assumption that went against the result. I see no sign the choice was made to reach the outcome.

2. **The numbers derive from the data.** The gamma rates are drawn as `gamma(r, (1-p)/p/48)`, using the negative binomial fit (r, p) from the data. That gives a mean of r(1−p)/p per 48 m, about 3.5. The equal rate is the observed mean count, 3.368 per 48 m under P-a, divided by 48. `xor_matrix` is the share of cells active in exactly one environment of each pair, the diagonal is excluded, and each of the 300 environments is drawn independently. This matches the Methods.

3. **The criterion as written.** Under G-b, the gamma-Poisson share beats the fitted equal-rate share at both levels:

   | Level | Gamma-Poisson | Fitted equal rate | Difference over 10 seeds |
   |---|---|---|---|
   | K-a (0.1) | 1.000 | 0.952 | +0.045 to +0.050 |
   | K-b (0.2) | 0.923 | 0.780 | +0.108 to +0.190 |

   Pass reading P-b and the data set's own fields give the same signs. The two spacings give opposite results, so the outcome must still be marked as resting on G-b, as the proposed reason says. Under G-b the criterion counts this as reproduced.

   One more check: for twice the fitted rate, the exclusive-OR between environments both over 20 m is 0.028. That fits the Fig. S18 legend's statement that the high-rate condition is almost zero between larger environments.

**Minor points, outcome unchanged**

* The criterion says "the full matrices are shown". The only matrix plot in cell 98 is drawn under G-a. The proposed outcome rests on G-b, so the G-b matrices should be shown too.
* I raised this in round 2 and it still stands; I am reporting it, not correcting it. The criterion itself says the fitted equal rate "does not recruit all cells by 50 m, so it does not test the paper's statement". The share-of-pairs-above-a-level measure is the reader's own construction, since Fig. 4C is missing from the text read. The mean exclusive-OR over pairs both larger than 10 m is reported, not judged. It is lower for the gamma-Poisson under both spacings: 0.247 against 0.274 under G-b. The attempt record has put this question to a reader.
