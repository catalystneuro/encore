The claims file has 24 claims and the attempt record has 24 outcomes. Two of them carry a `proposed` change: fig4c-wt-contrast-zx1-effects and fig4-wt-posthoc. I agree with both.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig4c-wt-contrast-zx1-effects | partially_reproduced (from blocked, methods_underspecified), assumed true | yes | — | See (1). |
| fig4-wt-posthoc | not_reproduced (from partially_reproduced), assumed true | yes | — | See (2). |

**(1) fig4c-wt-contrast-zx1-effects**

- **Numbers derive from the data (cell 43).**
  - The analysis uses group C, CTRL and ZX1 DRC trials with baseline PD below 50%: 328 trials and 6888 rows.
  - It fits both model formulas the criterion names, each under reference and sum coding. All fits converged and the subject variance is 28.1, away from 0.
  - The number of terms with p < 0.05 per reading is [5, 5, 4, 3]. The contrast × ZX1 term has p = 3.0e-05 in all four readings.
  - The two failures are under sum coding: the ZX1 intercept (p = 0.72) and, in the full factorial, the contrast slope (p = 0.12).
  - So every reading has the interaction plus at least three main terms significant, which meets the partial condition. Two readings also meet the full condition.
- **The test follows the criterion as written (cell 71).** It computes partial as `c_x_p < 0.05` and at least two of the four main terms below 0.05, and the result is "2 of 4; 4 of 4".
- **How the criterion is applied.**
  - The readings disagree only on whether the full condition is met. They all agree on the partial level.
  - Read with its partial clause applying under every reading, as the full clause does, the criterion gives partially_reproduced. This is how I read it in round 2.
  - fig4f-ko-no-contrast-effect is a different case and correctly stays blocked: there the readings disagree between reproduced and not_reproduced.
- **The choices behind it were not made to reach the result (cell 71).**
  - The partial condition holds in all four readings under three cleanings:
    - the main cleaning;
    - the narrower step rule (0 of 4 full, 4 of 4 partial, interaction p ≤ 0.00093), where the readings disagree on nothing at all;
    - the round-1 cleaning without AA0319 and AA0334 (1 of 4 full, 4 of 4 partial).
  - It fails under two cleanings:
    - the round-1 cleaning (interaction p = 0.25);
    - the single pass (interaction p = 0.56).
  - Both failing cleanings keep the tracking-failure maxima that the cleaning assumption exists to remove.
  - The outcome therefore rests on the cleaning, and `assumed: true` is right.

**(2) fig4-wt-posthoc**

- **Numbers derive from the data (cell 46).**
  - The cell means are taken at tPoly = 0 and compared pairwise with Tukey's test.
  - The four readings give the same cell means and almost identical p-values:
    - HIGH − LOW in CTRL: +2.48, p = 3.9e-08;
    - HIGH − LOW after ZX1: −0.28, p = 0.95;
    - ZX1 on HIGH: −1.51, p = 0.015;
    - ZX1 on LOW: +1.25, p = 0.0496.
  - The test uses df = rows − parameters (about 6880), not Satterthwaite df. The paper's denominator df are about 7920, so this cannot move p = 0.0496 across 0.05.
- **The criterion is applied as written.** It has no partial level and requires that ZX1 does not change LOW at p < 0.05. That part fails, and cell 46 prints "criterion met per reading: [False, False, False, False]".
- **The choice behind it was not made to reach the result.**
  - The main cleaning was fixed before this proposal, and it gives the outcome less favourable to the claim.
  - Under the other cleanings (cell 71):
    - round-1 cleaning: HIGH − LOW in CTRL p = 0.078, ZX1 on HIGH p = 0.83, ZX1 on LOW p = 0.89, so it fails;
    - round-1 cleaning without AA0319 and AA0334: ZX1 on HIGH p = 0.31 and ZX1 on LOW p = 0.00011, the reverse of the paper, so it fails;
    - single pass: HIGH − LOW after ZX1 p = 0.0045, so it fails.
- **Caveat: one variant reproduces the claim.** The narrower step rule meets all four parts (p = 1.7e-05, 0.98, 0.00036 and 0.99). In round 2 I criticised the main rule as reaching too far, and this narrower rule answers that criticism.
  - The not_reproduced outcome therefore rests on a p-value at the threshold (0.0496) and on keeping the broader rule. `assumed: true` is needed, and the notes should keep saying that the narrower rule reproduces the claim, as the proposal does.
  - Four of five cleaning variants fail the criterion, and the main one fails it. On that basis I still give not_reproduced.

**Reading of the paper by the claims file.** I found no misreading in these two criteria.
