**1. Outcomes**

The claims file has 22 claims and the attempt record has 22 outcomes:
- 9 reproduced: hd-cell-rate, fig1c-speed, fig1c-firing-rate, fig1c-directionality, fig2-decoding, figs2, figs3, fig3, fig5c.
- 5 partially reproduced: cell-counts, fig1d-preference-change, fig1d-instability, fig2c, fig5.
- 3 not reproduced: no-angular-velocity-tuning, fig4, fig4c.
- 5 blocked (data missing): fig1a, fig1c-lfp-power, figs4, figs5, figs6.
- 6 marked `assumed: true`: fig1c-directionality, fig2, figs2, figs3, no-angular-velocity-tuning, fig5c.

I agree with 19 outcomes as they stand. Three need more:

- **fig4c (not reproduced).** The outcome depends on how "beyond 10 s" is read, and the record does not state that as an assumption. The partial clause reads "the arena frame falls below the others beyond 10 s and not before, but the room-frame order at long intervals is not found". The before-side, code-normalisation reading (b) meets that clause word for word (cell 63):
  - no differences up to 10 s (p = 0.096 to 0.50);
  - p < 0.05 at every later interval;
  - arena below all three others at 60, 300 and 600 s;
  - room not below stable2 at 600 s.

  The record rejects this because the arena frame "falls only from 50 or 60 s, after the room frame". Both 50 and 60 s are beyond 10 s, and "after the room frame" is not a condition in the criterion. Not reproduced is defensible if "beyond 10 s" is read as "from 20 s", which fits the paper's "abruptly decreased after 10 s" and its legend's 20–60 s order. My round-1 outcome made the same reading. Either mark this outcome `assumed: true` and state that reading, or change it to partially reproduced.
- **fig1d-instability (partially reproduced).** The criterion has no partial form, and the record says so. Partial is therefore a judgement outside the criterion (I made the same one in round 1). Either mark it `assumed: true` with that reason, or give not reproduced.
- **figs3 (reproduced, assumed).** The n = sum-of-weights assumption is stated and is reasonable (CircStat convention). Not stated: the Idir reading used here (10° bins) is not the only reading under which figs2 reproduces (45° bins, rotating trial, ΔIdir SD, both below 0.05). Under the figs2 reading, figs3 has 1 of 14 tests significant even with n = sum of weights (min p 0.039, cell 48), so it would not reproduce. The record should say so.

The other assumptions are stated and reasonable:
- **fig1c-directionality:** the repeated-measures error term for Tukey. The Bonferroni paired t-test gives 0.0048 for the deciding pair, so the outcome does not depend on `tukey_rm` assuming sphericity while Mauchly's test is significant.
- **fig2:** the claims file's majority rule.
- **figs2:** 1 of 16 readings, two labels on 0.02–0.03 differences.
- **no-angular-velocity-tuning:** the claims file's test, now with shift controls.
- **fig5c:** pooled readings. I agree it is reproduced as the criterion is written, but the support is weak:
  - It is 1 match in 32 combinations at 0.0063 per combination by chance. At least one match is expected about 18% of the time, and the record gives only the 0.20 expected count.
  - The pooled error-by-direction curve is nearly flat (r = 0.029, cell 66).

  The note should say both.

**2. Text against outputs**

These numbers are not supported by the printed output:
- **Cell 43, and the figs2 notes in the record:** "0.605, 0.291, 0.199 and 0.054 … 1023R029 (0.000 against 0.367)". Cell 42 prints 0.606, 0.292, 0.200 and 0.368.
- **Cell 46:** "(-0.062 to 0.113)". Cell 45 prints a maximum of 0.114 (1026R157, angle, room).
- **fig2c notes in the record:** "(first reading -0.071)" and `measured: -0.071`. Cell 45 prints -0.0704.
- **Cell 67, and the fig5 notes in the record:**
  - "the arena-frame r … is 0.484, 0.543": cell 66 prints 0.542.
  - "reach at most 0.343 in the room frame": cell 66 prints 0.345 (4 samples, (ii) ≤15).
  - "Reading (i) gives error r of 0.030 to 0.426 at 20 samples": the lowest printed value is 0.0284 (1121R157).
- **Cell 64, and the fig4c notes in the record:** "at 20 to 50 s the room frame falls as far as or further than the arena frame". This holds only with the Methods' normalisation. With the code's normalisation the arena frame is lower at 40 s (0.180 against 0.204 before, 0.181 against 0.208 after) and at 50 s (0.142 against 0.199; Tukey significant, after side), as cell 63 prints.
- **README:** "about seven minutes, four and a half of them for the internally referenced tuning". Cell 59 prints 306 s (5.1 min), and the notebook prints no total runtime.

Everything else in the Result cells, the Summary, the README table and the record's notes matches the outputs.

The record's verification block gives my round-1 reasons faithfully and in my own words. It folds the problem-list items into the claims they affect, and `agrees: false` appears only on fig4c, which is correct.

**3. Round-1 points**

Resolved:
1. Tukey error term: `tukey_rm` added (formula checked by reading), outcome changed and the assumption recorded.
2. fig4c after side: now run at every interval.
3. KLD +0.5: rescaled variant added; the fig4 (b) reading still passes, instability p = 0.052.
4. fig2c distance: edge and angle distances added; the outcome holds under all 24 readings.
5. R523 outlier: dropped as a variant, p = 0.275.
6. Angular velocity: the shift tests keep the excess, so it does not come from treating samples as independent.
7. cell-counts: now uses the Rayleigh vector of the tuning curve.
8. fig3 timestamps: the offset unit forms no pair.
9. Bin-start convention: kept and stated as a deviation.
10. fig5c `near`: now matches by bin centre only.
11. Leftover result cell: split.
12. The two .xls lists: now read.

All the outputs listed in my section C are now printed.

Point 13 (the fig1d legend order) is passed to a reader; the claim is tested as written, which is acceptable.

Remaining points that bear on a conclusion:
- fig4c: the reading of "beyond 10 s" against the before-side, code-normalisation result, as in section 1.
- fig1d-instability: partial is given although the criterion has no partial form.
- figs3: the outcome holds only under an Idir reading that differs from the one that reproduces figs2.
- fig5c: the note should state how weak a single chance-level match on a nearly flat curve is.
