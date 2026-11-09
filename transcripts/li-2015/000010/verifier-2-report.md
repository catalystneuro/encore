**Verifier report, round 2: Li et al. 2015 (doi:10.1038/nature14178) on DANDI:000010 v0.220126.1905**

The claims file lists 27 claims, and the attempt record gives an outcome for each of them. The record's outcomes are 8 reproduced, 4 partially reproduced, 4 not reproduced and 11 blocked. My round-2 outcomes are 8 reproduced, 3 partially reproduced, 5 not reproduced and 11 blocked. We differ on one claim, imaging-selectivity-counts.

### 1. Stated outcomes

I agree with 26 of the 27 outcomes, including the change of ed1-fast-spiking-properties to not_reproduced.

- **imaging-selectivity-counts: I disagree (record: partially_reproduced; mine: not_reproduced).** The claims file sets only a reproduced condition: all values within tolerance under one reading. No reading meets it (0 of 16, cell 60). The author points to units-classification as precedent, but that case is different. There, the failing count is a class the dandiset does not hold. Here, the selective count is measured and misses under every reading. The author's own handling of fig2d shows the inconsistency. That claim has the same kind of criterion, and 2 of 3 counts are within tolerance under three readings (cell 26), yet it is recorded as not_reproduced. "Bracketing" 1,575 between two readings does not put the count within tolerance under any one reading.
- **fig2e-no-contra-bias-spikes: I agree it is reproduced, but it stays fragile.** See point 3 below.

### 2. Statements the printed outputs do not support

1. **"66 extracellular trials" (cell 6; the attempt-record finding that starts "66 extracellular trials"; the fig2-selective-fraction deviation; my own round-1 B8).**
   - Cell 5 prints "66 of 28508". The 28,508 trials are 24,580 extracellular plus 3,928 imaging non-early matched trials, so the count is not limited to extracellular trials.
   - The finding also says these trials have a go cue "less than 2.6 s" after the sample. Cell 5 shows a maximum gap of 2.6778 s, so at least one of the 66 is longer, not shorter.
2. **Finding "4,332 of 18,385 correct trials".** The figure 18,385 is printed nowhere. Cell 54 gives 4,332 of 14,388 correct trials in the 75 sessions with light.
3. **"Most in the first or last tenth of a session" (cell 6; the 1,540-trials finding).** Cell 5 prints 231 + 523 = 754 of 1,540 trials, which is 49%, not most.
4. **"Spikes are stored only within the 5.5 s trial windows" (cell 10; the last finding; the ed1 baseline deviation).** Cell 9 prints a minimum of 0.7019 for the fraction of spikes inside a trial window. So in at least one session, 30% of spikes fall outside every trial window.
5. **fig2e `measured: 8.5`.**
   - This value comes from reading (a)(ii): all neurons, 570 ms window. Under that reading the absence test fails (P = 0.036 with a contralateral excess), and the population is not the "task-selective neurons" of the statement.
   - The reading where both the test and the 8% value agree is (b)(iii)(t2): 7.97%, P = 0.060 (cell 38).
6. **Author's response on imaging: "the 3,403 ROIs touch 0 in single frames, not in the 0.5 s baseline".**
   - Cell 61 shows only "at least one frame". Nothing printed shows the dips are single frames.
   - In 145 ROI-trials the 0.5 s F0 is itself at or below 0.
7. **README: "with the trials pooled there are more of them".** This is offered as the explanation for the PT result, but it is not tested. Cell 54 shows only that each stratum alone gives P ≈ 0.14 and the pooled data give P = 0.010.

Every other "**Result:**" sentence, the Summary, the README table and the notes match the outputs. I checked every range, count and P value against cells 17–72.

**How the record states my round-1 reasons.** They are in my words, with two defects:
- fig2c-selectivity-time-course: "rises from 273 to 326 to 377 to 408" garbles my "rises from 273–326 to 377–408".
- fig2e: my reading (b)(delay)(t2) result (P = 0.060, 7.97%) is left out.

One correction to my own round-1 text: the s.d. across mice of "29 to 51 ms under every reading" holds only for the (z) readings. The (k) readings reach 96 ms (cell 71). This does not change the outcome.

### 3. Round-1 points

**Resolved:**
- **B2 (light balance):** cell 54 shows the light is balanced (0.295 against 0.307 of correct trials), and the light-only and no-light strata point the same way.
- **B3, B5, B6, B7, B8, B10:** the author added the variant or the text I asked for. None of them changes an outcome.
- **C items now checked:**
  - Plane depth: no depth in any of the 58 fields, so fig4h stays blocked.
  - Trials without events, by mouse: 218693 has 7, so ed7 is unaffected.
  - F0 sensitivity: only 145 of 305,349 included ROI-trials have F0 at or below 0.
- **B4 (imaging sensitivities):** the F0 part is resolved.

**Remaining, and bearing on a conclusion:**
- **fig2e-no-contra-bias-spikes (B1).** The author's rule, "the paper's test as written", does not single out reading (a)(i). The paper prints a second P = 0.13 test as well, "for all task-selective neurons (8%…; P = 0.13)". On that test the result depends on the window:
  - 570 ms window: P = 0.050 and 0.038, both with a contralateral excess, which is the criterion's not-reproduced condition.
  - Delay window: P = 0.12 and 0.060, with 7.97% under t2.

  The claims file sets no rule for deciding a claim of absence across readings, so the outcome depends on which reading is chosen.
- **imaging-selectivity-counts.** The outcome disagreement in section 1 stands. Early-lick trials still cannot be excluded, because the imaging files flag no early licks.
- **fig3f-pt-contra-preferring.** The claim holds only under t1, and only with light and no-light trials pooled. The claims file lets t1 decide, so the outcome stands, but it is fragile.

**Remaining, not bearing on a conclusion:** the "66 trials" count and the trial-window statements above; the lick trace is still not documented as the photodiode signal; and the figure-only values have still not been read from the figures.

I found no new place where the claims file misreads the paper.
