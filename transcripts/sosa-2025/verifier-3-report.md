# Round 3 verifier report: 001361-sosa-2025-01

The claims file has 50 claims and the attempt record has 50 outcomes. Only one outcome has a `proposed` change: ed4l-disappearing-decrease, from partially_reproduced to not_reproduced. I agree with it.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| ed4l-disappearing-decrease | not_reproduced | Yes | — | The criterion is applied as written, the numbers come from the data, and only the reading of the criterion changed. Details below. |

**The criterion as written.**
- It says only: "Reproduced when the disappearing slope is negative at p < 0.05 in both windows and the non-RR remapping and appearing slopes have p of 0.05 or more in both".
- It has no partial clause. Neighbouring criteria spell one out, for example fig1h, ed2m and ed2i.
- An outcome that does not meet the single reproduced condition is therefore not_reproduced. The record treats fig4j the same way.

**The numbers derive from the data (cell 86).**
- Each fraction is a per-mouse, per-switch-day count of disappearing, appearing and non-RR cells, divided by that session's number of place cells.
- Each fit is the shared `mixed` function (cell 9): fraction ~ 1 + switch, a random intercept per mouse, REML and a Wald test. This is the fig4m model the criterion names.
- Disappearing near reward: slope −0.0021, p = 0.020. Disappearing far from reward: slope −0.0048, p = 0.069, so the "both windows" condition fails.
- The parts about absence of change hold: appearing p = 0.14 and 0.39, non-RR p = 0.23 and 0.11.
- The record's notes and the result text in cell 87 match these printed values.

**The choice was not made to reach the result.**
- The analysis is unchanged from round 2. Only the reading of the criterion changed, and it is the reading I asked for in round 2.
- The mouse-clustered OLS printed in cell 86 does not rescue the claim either. It gives the opposite pattern: far p = 0.030, near p = 0.083. Under that fit too, the slope is not significant in both windows.
- The near/far split (|peak − zone start| ≤ 50 cm against > 50 cm, with the same tolerance on both sides) leaves no cell out and puts none in both windows.
- One assumption is stated in the deviations: disappearing cells are placed by their pre-switch peak, the others by their post-switch peak. It is unchanged from earlier rounds and was not tuned.

**A caveat that does not change my outcome.**
- The criterion cites "the mixed model of fig4m-rr-density-near-reward-grows". That criterion defines two readings, (a) raw fraction and (b) logit fraction.
- Cell 86 fits only the raw fraction. The logit fit for ed4l is not shown, so it is not known whether the logit far-window p would fall below 0.05.
- It is not clear whether fig4m's readings carry over to ed4l. I missed this in rounds 1 and 2.
- On the analysis as run, not_reproduced is the correct outcome. A logit fit would settle the question fully.

**About the claims file (reported, not corrected).**
- The ed4l criterion leaves the logit question open, as described above.
- The paper's legend for Extended Data Fig. 4l gives no statistics. The mixed-model test and the p < 0.05 threshold in both windows are the claims reader's choices, not figures stated in the paper. This does not misread the paper's claim, which says "decreases across experience" both near and far.
