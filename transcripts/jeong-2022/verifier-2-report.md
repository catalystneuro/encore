**Verifier report, round 2: 000351-jeong-2022-01 (doi:10.1126/science.abq6740, DANDI:000351 v0.260828.1905)**

The claims file has 38 claims and the attempt record has 38 outcomes: 27 reproduced, 1 partially reproduced, 2 not reproduced and 8 blocked (1 methods_underspecified, 7 not_runnable). No outcome in the record carries `assumed: true`.

## 1. Outcomes

I agree with all 38 stated outcomes. Five need comment.

- **fig4hi-delay-change-dopamine-unchanged (reproduced):** I agree under the criterion, which fixes the code's bounds (A −2 to 50, b −10 to 10). The new outputs in cell 67 show that the "no change" result comes from those bounds, not from the data:
  - On the ÷100 scale, b ≤ 10 cannot reach a starting level where 5 of 7 animals have mean responses of 13.2 to 44.6.
  - Three animals have ΔAIC of exactly −6.00, which means the changing model collapsed to the constant one. HJ-FP-M3, at −168.5, fits worse than the constant.
  - On the percent scale, ΔAIC is −272 to −817 in every animal, so the bounded model cannot fit the data at all.
  - Fitted without bounds, the changing model is better in every animal (t = 7.83, p = 2.3e-4).

  The outcome therefore rests on an unverified premise: that the code's bounds were set on a scale where they do not bind. The record should state this as an assumption (`assumed: true`), or say plainly that the test cannot detect a change in this data. This is a gap in the claims file's criterion, which takes the bounds from the code without fixing the dF/F scale. It is not a misreading of the paper. The paper's t of −0.86 is close to this attempt's −0.73, which suggests the paper's fit was bounded the same way.
- **fig4p-background-faster-decay (not reproduced):** I agree. The result is close to the threshold: p = 0.053 under (a) and (c). Leaving out the NaN trials brings (a) and (c) below 0.05, while (b) stays at p = 0.088. HJ-FP-M4's first background session is missing from the data. The record states all of this.
- **fig6i-lower-cs1-asymptote (not reproduced):** I agree on the criterion's measure. Each of the three alternatives in cell 110 would give p < 0.05, and the record states this.
- **figs8e-lick-bout-responses (blocked, methods_underspecified):** I agree.
- **Simulation claims (blocked):** I agree they are blocked. The author keeps the reason "not_runnable" and cites protocol Author step 1.5. The protocol is not among my materials, so I cannot confirm or withdraw my round-1 statement that "other" is the correct reason. This does not affect any conclusion.

## 2. Sentences the printed numbers do not support

- **Cell 119, Summary:** "on the evidence that the files store percent and the code's bounds suit a fraction". Cells 67 and 68 show the bounds bind on the fraction scale as well: b ≤ 10 against mean responses of 13 to 45, and M3's ΔAIC is −168.5.
- **Cell 68:** "the criterion's result does not depend on the scale assumed". On the percent scale the bounded model cannot fit at all (ΔAIC −272 to −817), so that variant does not test the scale. The record's notes repeat this sentence.
- **Cell 102:** "(0.37 to 0.71 per animal)". The no-baseline ratios printed in cell 101 range from 0.303 to 0.705. The record's notes correctly give 0.30 to 0.71.
- **Cell 45:** "The consummatory t values (6.3 to 8.6)". The consummatory one-sample t values are 6.30 to 6.49; 8.58 is the paired t. The record's wording ("about twice the paper's") is correct.
- **Cell 80, and the cell 79 comment:** "as HJ-FP-M6's pre-change sum is near 0". No pre-change sum is printed. The sentence is an inference from bgd_a = 12.154.
- **Record, methods-session-counts notes:** "so the paper's counts include the 7 sessions the dandiset lacks". The outputs only support "suggests", which is what cell 22 says. The record's own session-day-link deviation says integer days without a session "can be days without training". Only M4 Day38 is directly shown to be missing, because it is a listed start day. The data_missing finding, the README ("Seven sessions inside those lists are not in the dandiset") and Summary bullet 2 state the other six as fact.
- **Cell 119, Summary:** "dF/F and the event log are consistent with one clock" drops cell 14's caveat that this is not established for 27 sessions.
- **Cell 6 (data check, minor):** "sessions last 500 to 4200 units". Cell 5 prints 481 to 4810.

Every other Result sentence, the README table and all other record notes match the outputs. I checked the counts (5600/4064/4013, 37 of 8721, 0 to 4 NaN trials), the t and p values, the ranges and the per-animal statements.

The record's round-1 reasons are mine, sometimes merged across claims: problem 1 is placed under fig4ef and figs10b, problem 8 under fig4hi and fig4kl, problem 6 under fig6g, and problem 7 under methods-session-counts. They are faithful. The only omission is my remark on cell 43's "without a dopamine value: 0", which cell 56 now explains.

## 3. Round-1 points

**Resolved:**
- Problem 1, nansum zero-fill: cell 8 is corrected, trials are counted under each claim, and every claim shows its result without them.
- Problem 4, (a) and (c) being one affine function of the other: now printed and stated.
- Problem 5, Methods lick measure for fig4jl reading (b): t = 3.78.
- Problem 6, the baseline scaling choice: stated.
- Problem 7, the Experiment 7 SD swap: stated.
- C1 and C2: cell 17 reads the six scripts at the pinned commit, and all lists match.
- C3: the NaN-trial counts are printed.
- C5: the per-animal variants for fig4p and fig6i-lower are printed.

**Open, does not affect a conclusion:**
- Problem 3: the not_runnable label.
- Problem 8: the abruptness t values still differ from the paper's (15.3 against 22.9; 9.7 against 5.67), cause not found.

**Open, bears on a conclusion:**
- **fig4hi-dopamine-unchanged:** this came out of problem 2 and C4. The variants now show that the outcome holds only because the bounds bind on both scales tested, and an unbounded fit finds a change in every animal. It needs an explicit assumption, or a statement that the test has no power here.
- **Experiment 7 trials without dF/F, which is new:** `auc_python` gives NaN when a window has no samples. HJ-FP-WT-stGtACR-M2 Day6-Pavlovian has no dF/F for its first 1117 s, and Day6 is that control's last conditioning session: it has 5 conditioning sessions and the Day2–Day7 numbering of WT-F3 indicates they are Day2–Day6. My estimate, assuming a mean ITI of about 60 s, is that about a third of its 50 CS1 trials drop out of the last-session value of 0.459 used in fig6i-lower-cs1-asymptote, which is the borderline not-reproduced claim. No Experiment 7 output counts these trials, and none shows the result without that session.
