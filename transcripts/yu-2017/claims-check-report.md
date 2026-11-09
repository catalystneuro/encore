I checked the claims file for hc-13 against the paper and edited it. Its last check now says it is ready for an attempt.

**Checker result:** `claims/crcns-hc-13/10.7554-elife.27621.yaml: 32 claims, 32 quotes, 35 statistical values, 0 problems` (it was 31 statistical values before my additions, also with 0 problems).

**Changes, by claim:**
- **Opening comment, O1 (well entry):** the Methods define well entry for Figure 6 as the infrared beam break, so the reading built from immobility periods no longer applies there.
- **fig1f-iap-smaller-coverage:** added the second per-task bound, p < 0.0005. The legend gives both p < 0.005 and p < 0.0005.
- **fig3s3-iap-same-well-coactivity, fig4s2c-spatial-proximity-control, fig4s3-overlapping-pairs:** added the significance bounds the legends give that the file had left out (p < 0.05, p < 0.0001 and p < 0.0001 respectively). Each entry now says the legend does not state which comparison carries which bound.
- **fig4s1b-offset-matched-coactivity:** full reproduction now needs p < 0.05 in all four bins from 1 to 5 s, as the legend reports. The file had accepted three of four.
- **fig4d-iap-swr-lower-power:** the statement claimed a "slow gamma" increase in every SWR type. The paper says only that IAP-SWRs show the usual gamma (~30 Hz) increase, so the statement and criterion now say that. The 25 to 35 Hz band is named as a choice, and the LFP reference to ground from the Methods is added.
- **fig4s67-matched-subsamples:** the median p-value rule and the 95% bound are now named as choices; the paper shows only boxplots.
- **pfc-unit-selection:** added the Methods reading (units recorded with both CA1 IAPs and MAPs) next to the Results reading (sessions with both SWR types).
- **fig5-pfc-modulated-fraction:** the file presented the PETH window, bin and shift range as given, but the paper does not give them. They are now a choice the outcome rests on.
- **fig5dg-pfc-groups:** the paper does not say whether the binomial test is one- or two-sided, so both are now readings. I computed both on the paper's counts and they give the same outcome.
- **pfc-regression-joint-swr:** `expected` is now written as a list, like the other claims.
- **fig6c-similarity-index:** well entry is the beam break, from the Methods.

**What remains open:**
- **fig5-pfc-modulated-fraction:** the paper takes the PETH settings from Jadhav et al. 2016 without stating them, so the count of modulated units may depend on that choice.
- **fig2c-continuous-transition:** the paper gives no measure for how far the "tail" must extend. The file uses its own rule, labelled as a choice.
- **fig1-iap-map-counts:** the per-task MAP counts add to 679, but the paper reports 659 pooled. The file accepts a match to either, and the paper does not say which is right.

The paper's main findings all have claims, and none comes from any other source.

**Ready:** yes. Nothing was committed or pushed.
