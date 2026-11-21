**Verifier report, round 2: Jarzebowski & Bendor (2026) on DANDI:000713 0.240702.1725**

The claims file has 31 claims, and the attempt record has 31 outcomes: 22 reproduced, 4 partially reproduced and 5 not reproduced. Five outcomes carry `assumed: true`: fig2d, fig4b, fig6b, fig6c and fig7c.

### 1. Outcomes

I agree with all 31 outcomes. Notes on the outcomes that rest on an assumption or are fragile:

- **fig2d (assumed), reproduced.** I now agree. The new test resamples the steepest interval at 1 nS with 4000 runs, and no single 1 nS step carries more than 0.43 of the change. About 0.40 of first spikes fall at intermediate latencies of 8–12 ms (cell 28). The coarse steps of 5.25–6.28 ms come from noise in the 80-run means. For example, under seed 4 the step is 6.28 ms but the fine-grid change over that interval is 3.03 ms. The assumption is stated and reasonable.
- **fig4b (assumed), reproduced.** The assumption is stated and reasonable (cells 43–44).
- **fig5c-fsb-highest-on-first-repetition, reproduced.** This meets the criterion's "under one reading", but only just:
  - Under O9 (b), one analysis reading (O8 a, O4 a, square root, coding k) on 2 of 16 cell selections falls inside the tolerance, by 0.0002–0.0003 (cell 63).
  - That reading uses coding k. Its intercept extrapolates to repetition 0, and coding k against k−2 moves the L5 intercept by about 0.0018 (−0.0574 against −0.0592, cell 66). That shift is six times the margin.
  - The recorded `measured` values come from O9 (a), which fails cell-counts. The O9 (b) values (−0.0524, −0.0548) would be the consistent choice.
- **fig6b and fig6c (assumed), partially reproduced.** The assumption is stated. It is defensible, but no better supported than reading block 1 alone, and the outcome depends on it:
  - "Both blocks" is in effect block 3: the median cell has 1155 block-3 windows against 40 in block 1 (cell 87).
  - The deviation argues against block 1 because "the paper's n is every cell". That argument applies only to O5 (b). Under O5 (a), block 1 drops only 4 and 15 cells under O9 (a), and 1 and 9 under O9 (b) (cell 87).
  - Against block 1 alone, fig6b is not reproduced (L2/3 p = 0.87), and fig6c is not reproduced either (+0.0073; cells 87 and 90).
- **fig7c (assumed), reproduced.** The assumption is stated and reasonable. Under O9 (b), no reading under either selection gives p < 0.05 (lowest 0.059, cell 105). No selection reaches the paper's 47/35 and 658/94.
- **figs1-novel-firing-rate-unchanged, not reproduced.** I agree. After the refits, all 32 combinations of selection and O9 reading give p ≤ 0.017 (cells 63 and 84).

### 2. Text against the printed outputs

These sentences are not supported by the printed numbers:

- **Cell 79, and the record's figs1-post-omission-bursting notes:** "L2/3 ... p 0.006 to 0.032 under O9 a". The printed range is 0.0026 to 0.032 (cell 78, all L2/3, O4 a diff p = 0.002603).
- **Cell 85, the record's figs1-novel-firing-rate-unchanged notes, and cell 64 ("p at most 0.017" is fine; the lower bound is not):** "p from 0.00025 to 0.017". The smallest printed p is 0.00027 (cell 63).
- **Summary (cell 110):** "within tolerance only on 2 of the 16 selections under O9 (b) (8 under O9 a), by 0.0003 at most". Under O9 (a), the readings fall inside by up to 0.0012 (cell 63, a aa b a: −0.0012).
- **Record's fig5c-fsb-highest-on-first-repetition notes:** "The outcome rests on intercepts within 0.0003 of the tolerance edge". The record's own `measured` values (L2/3 −0.0505, L5 −0.0473) sit 0.0005 and 0.0013 inside the edge.
- **README:** "six to run the claims on all 16 cell selections". Cell 63 prints 230 s, about 4 minutes. Streaming took 376 s (cell 3), which is consistent with the README's "four to nine".
- **Cell 0:** "the draft has the same asset count and size". No output shows this.

Every other "**Result:**" conclusion, the Summary, the README table (11/1/2, 6/1, 2 partial, 1/1, 2/1/1, summing to 31) and the record's notes match the outputs.

The record's `verifications` block restates my round-1 reasons faithfully and in my own words, including problems 1–12 and the items in section C. The agree/disagree flags are correct: false for fig2d, fig3b, fig6b and fig6c.

### 3. Round-1 points

**Resolved:**

| Point | How it was resolved | Cells |
|---|---|---|
| 1 | All 16 cell selections are run under both O9 readings | 63 |
| 3 | The fits now converge, with Powell's method where needed | 63 onward |
| 4 | The fig2d test is refined | 28 |
| 6 | Explained | 108 |
| 7 | Late spikes are counted at every L4 | 12 |
| 8 | The notes now say how much of fig4d comes from L5 IT alone | 50 |
| 9 | 800 omission runs per gain | 34, 37 |
| 10 | Rerun without the low-AUC sessions; no outcome changes | 63 |
| 11 | Optotagging table printed | 8 |

The block timing, the repetition ordinals and the per-session running fractions are now printed (cell 8).

**Remaining, and bearing on a conclusion:**

- **Point 2.** The timing is now explained: block 1 starts 18–29 s after the task in 152 sessions, and one session is an outlier. The fig6b and fig6c outcomes still rest on the block assumption, and the literal reading reverses both.
- **fig5c-fsb-highest.** The outcome rests on a 0.0002–0.0003 margin under O9 (b), with one reading on 2 of 16 selections, and that reading is coding k. The record should take its `measured` values from O9 (b).
- **Point 5.** Figures 7A and 7B cannot include every cell under D7: 26 of 104 sessions have no stationary Repetition 1 presentation (cell 8). The paper's running definition probably differs from this one, which may bear on the L5 magnitude in fig7b. This is open as a question.
- **Point 12.** The claims-file readings I reported in round 1 still stand. O5 still assumes a single spontaneous block. One more for the claims file: coding k in fig5c makes the intercept an extrapolation to repetition 0, not the drop from Repetition 1 to 2 that the claim states.
- **Still unavailable:** the paper's model code, and the legends of Figures S1 and S2.

### 4. Critical findings

No finding is rated `critical`.

The rated findings are:

| # | Finding | Rating | My view |
|---|---|---|---|
| 1 | 351 units have coordinates (0, 0, 0) | minor | Agree: the zeros show in the values |
| 2 | No column descriptions | minor | Agree |
| 3 | Block 1 starts 3277 s after the task in one session | minor | Agree: it shows in the timestamps |
| 4 | Checks that passed | none | Agree |

The weak clock checks in 10 sessions are not established as errors, and leaving those sessions out changes no outcome (cell 63), so nothing needs a `critical` rating.
