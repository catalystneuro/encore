**Round 2 verification: Rodgers & DeWeese 2014 on CRCNS pfc-1**

Cell indices are those of the current notebook. They have shifted since round 1; for example, the fig8 conclusion is now cell 123.

**1. Outcomes**

The claims file has 35 claims and the attempt record gives 35 outcomes, all reproduced. Only fig8-model is marked `assumed: true`.

- **34 outcomes: I agree.** Each one meets its criterion in the printed outputs.
- **fig8-model (reproduced, assumed): I agree, and the assumption is stated and reasonable.** It reads "most positive task signals" over Figure 8B's plotted range. Two outputs support that reading:
  - On the plotted axis, x ≥ 0.316 reaches at least 99% (90% of the symlog axis).
  - On the code's linear sweep, 38 of 40 positive gains reach at least 99%.
  - The other reading, counting each log-spaced gain (25%), is shown and disclosed.
- **fig5ab-single-unit-onset (reproduced): I agree only under a reading the record does not mark as assumed.**
  - The criterion defines the interval as the run "that contains the bin just before stimulus onset". Seven mPFC and two A1 units have no such interval.
  - With those units left out, cell 64 gives 0.650 s in A1, outside 0.55 ± 0.05.
  - The pass comes from keeping those units, as `main4.py` does. The notes say this follows the criterion ("main4.py keeps them, as the criterion does"), but the criterion's wording points the other way.
  - The outcome should carry `assumed: true` with this reading stated, or the claims file should settle the point.

**2. Sentences the numbers do not support**

- **Cell 33, and the fig3c-pfc-rule-encoding notes in the record.** They say "Under reading (b) the counts are 81, 37 and 44, the first outside the tolerance of 7.6, so the claim holds under reading (a) only." In fact |81 − 76| = 5 ≤ 7.6, 37 is within 36 ± 3.6, and 44 sits on the edge of 40 ± 4. Reading (b) also passes (cell 30, binomial p = 0.51). My round-1 reason made the same mistake. The outcome itself is unaffected.
- **Cell 19.** "The data set holds 55 sessions, all of which pass." Only 54 were tested (cell 17); the catch-trial session was excluded.
- **Cell 123 and the fig8-model notes.** "below 99% only for the smallest task signals (about 0.63 to 0.77)." These numbers are performance values, but the sentence reads as if they were task-signal values. They also leave out the 0.988 at gain 1.194 (x = 0.30) printed in cell 122.
- **Cell 111.** "a reduction of up to about half the magnitude is not excluded." That holds for mPFC (−0.237 against 0.418). In A1 the interval reaches −0.442 against a magnitude of 0.401, so even a complete loss is not excluded.
- **Summary (cell 124), "because the table applies rules the paper does not state".** This is only partly supported. Cell 74 also shows 6 "nothing" units becoming responsive under reading (b), and 13 units that the table counts as responsive (5 A1, 8 mPFC) losing their responsiveness. So the threshold and trial choices also contribute.
- **README, "Four outcomes rest on the code's choices".** The four named are correct. The list leaves out fig5ab's dependence on keeping the units whose bin just before onset is not significant.

Everything else checks against the outputs: the other "Result" cells, the README counts per row (they sum to 35), and the record's notes and findings.

The record's `verifications` restate my round-1 reasons faithfully and close to my wording, including the problem numbers.

**3. Round-1 points**

Resolved:
- **Problem 1 (audresp/S5E):** reading (b) is now reported in cells 78 and 84, the README, the summary and the record.
- **Problem 2 (fig8):** marked assumed, and the narrow linear sweep is now shown.
- **Problem 3 (evoked-beyond-baseline-rare):** three seeds give the same 6 units after BH, and the unit ranked 7 has adjusted p = 0.063. The record states that the outcome rests on BH, which the claims file names as its main reading.
- **Problem 4 (fig5d):** disclosed.
- **Problem 5 (claims of absence):** confidence intervals and power are now given.
- **Problem 7 (fold alignment):** the crosstab in cell 24 is clean.
- **Problem 8 (conclusions left in markdown cells):** the section headers (cells 32, 34, 50, 52) are now clean.
- **Section C items:** all the outputs I asked for have been added.

Remaining points that bear on a conclusion:
- **fig5ab (my problem 6, now upgraded).** The new output shows that excluding the units whose interval does not contain the bin before onset puts A1 outside tolerance. The pass therefore rests on an unmarked reading of the criterion; see section 1.
- **Not checked:** I still have not read the code's scripts beyond the four from round 1, and nothing was re-run.
