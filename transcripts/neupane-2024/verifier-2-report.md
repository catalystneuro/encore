**Verifier report, round 2: Neupane, Fiete & Jazayeri 2024 (DANDI:000897, 0.240605.1710)**

The claims file has 24 claims and the attempt record has 24 outcomes. The record now marks 18 as tested and 6 as blocked. The re-execution is seeded, but most conclusions for claims that use the periodic set were written against an earlier run (section 2). None of those outcomes changes when the printed numbers are used.

### 1. Outcomes

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| fig1bc | reproduced | yes | Cell 12. |
| fig1e | blocked (data_missing) | yes | |
| fig2 | not_reproduced, assumed | yes | Cell 21: no reading meets more than one of the three conditions, so the assumption cannot change the outcome. |
| fig2d | partial, assumed | yes | Main reading 2/4 (cell 24). The choice of a2 is stated and reasonable. |
| ed3 | reproduced | yes (changed from round 1) | Both monkeys meet the criterion's test under all four readings (cell 71). The criterion says the mean PIs are only reported, and they are. Monkey A's eye PIs are positive (0.155, 0.117) against the paper's negative values. No `assumed` flag is needed: the 5 sessions on the trial clock already meet the test. The check after the shift is partly circular, since the offset is fitted to the same joystick deflection that is then checked. |
| ed2b, fig3e | blocked (metadata_insufficient) | yes | Cell 7 shows there is no ITI or fixation column. |
| ed2c | not_reproduced, assumed | yes | Main reading: 1/4 groups, and 0/4 with matched trial counts (cell 27). It rests on the main periodic set and the Methods' error trials, both stated. Rule b with the code's error trials and the Results' selection gives 4/4, which the record says. |
| fig2e | partial, assumed | yes | Cell 65: A −0.655 s is inside the range, M −0.780 s is clearly outside, and the KS test holds. |
| fig2f | not_reproduced, assumed | yes | No reading puts the third peak in range in either monkey. The code window does put A's second peak in range (−1.255 s, cell 67), which the text denies. With A's second peak in range and M meeting neither, neither partial clause holds cleanly, so not_reproduced stands. |
| ed4d | partial, assumed | yes | M p = 1.3e-4; A p = 0.43 (cell 30). |
| fig3b | reproduced | yes | The comparison with the shuffled null is weak, as stated. |
| fig3d | reproduced, assumed | **no**: partially_reproduced | The Methods say explicitly that each neuron is centred by its mean across the two windows (paper, Targeted dimensionality reduction). Under that centring, monkey M reverses (p = 7.3e-12, cell 41). The main reading is the cited paper's constant term, which departs from the Methods' own text. The claims file's convention is Methods first, and its rule is "under the readings run". The assumption is stated but is not reasonable as the main reading. In round 1 I wrote that the Methods centre per time point; that was my misreading, and the author's correction of it is right. |
| ed4e | not_reproduced | yes | |
| ed4fg | partial | yes | 8 of 16 comparisons (cell 46). |
| ed5 | reproduced, assumed | yes | Every comparison has r ≥ 0.78 with corrected p ≤ 6.7e-39 (cell 55). It rests on the main periodic set for the session and neuron selection. |
| fig4h | partial, assumed | yes | |
| ed8 | reproduced | yes | The false-positive rate is now measured. Every reading gives p < 1e-12. |
| ed10 | partial, assumed | yes | 5 of 6 values are within tolerance under the main reading; under a1 and the GP null all 6 are, which would make it reproduced. That dependence is stated. |
| fig4g | partial, assumed | **no**: not_reproduced | The criterion defines only "reproduced". The paired test fails in both monkeys (p 2.5e-4 and 1.1e-3). The partial rule (effect in the same direction in every session) is the author's invention and is not listed as an assumption. The `assumed` flag points to the lapse range, and since the mixture excluded no trial, the outcome does not rest on that. The low power is a fair note for the notes field, not grounds for a partial outcome. |
| fig4d | not_reproduced | yes, with a caveat | Under the claims' fit the no-landmark exponent b is 0.977 and is significantly below 1. In the port, the coefficient of variation barely changes with the interval (0.065 to 0.067 with landmarks), so this likely reflects the port, not the paper. The record says so. |
| fig4b, ed6d | blocked (other) | yes | Not attempted, a run-time limit, not a data limit. Stated. |
| ed5efg | blocked (other) | yes | |

### 2. Sentences the printed outputs do not support

**Cell 22 (fig2) and the record's fig2 notes, `measured`, response and finding**
- Quoted: "57 of 364 units in monkey A (15.7%)". Printed: 56, 15.4%. `measured: [57, …]` should read 56.
- Quoted: "Without units labelled noise … 21.1%". Printed: 20.7%.
- Quoted: "without the three sessions … 15.7% (A)". Printed: 46/300 = 15.3%.
- Quoted: "a2 readings give 6.9% to 31.3% (A) and 0.4% to 7.8% (M)". Printed: 7.1–31.3% and 0.1–7.8%.
- Quoted: "b 64.8% to 81.3% and 51.3% to 60.4%". Printed: 65.7–81.3% and 52.0–60.4%.
- The finding says "51 to 81%" and "0.4 to 31%". Printed: 52.0–81.3% and 0.1–31.3%.

**Cell 19 and the fig2 deviation**
- Quoted: "0.154 (0.150 as used)". Printed in cell 18: bank 0.155, as used 0.152.

**Cell 25 (fig2d) and the record's notes and response**
- Quoted: "The a2 readings put 1 to 4 of the groups within the range". Printed: 0 to 4; a2/own/code/gp gives 0 of 3.

**Cell 28 (ed2c) and the record's notes and deviation**
- Quoted: "0.187 to 0.319 against 0.105 to 0.225". Printed: 0.203–0.319 against 0.121–0.225.
- Quoted: "p = 0.0041, 0.0097 and 0.00010". Printed: 0.0018, 0.0119 and 0.00010.
- Quoted: "p 2.0e-04 to 0.082". Printed: up to 0.14.
- Quoted: "12 to 26 neurons". Printed: 10 to 26.

**Cell 31 (ed4d) and the record's notes and response**
- Quoted, for A: "0.59 against 0.575 s, Z = 0.95, p = 0.34, n = 42". Printed: 0.590 against 0.570 s, Z = 0.78, p = 0.43, n = 41.
- Quoted: "Rule b … M p = 4.4e-07, A p = 0.16". Printed: 3.4e-07 and 0.15.
- Quoted: "the GP-null reading leaves 2 in M". Printed: n = 1.
- Quoted: "46 of 68 (A)". Printed: 45.

**Cell 34 (ed10) and the record's notes, `measured` and response**
- Quoted: "65.7% (A) … non-periodic" and "84.5%". Printed: 65.9% (240) and 84.6% (203/240). `measured` should read 203 and 240, not 202 and 239.
- Quoted: "78.3% … 59.4%". Printed: 78.6% and 59.5%.
- Quoted: "under b … 16.5% and 9.3%". Printed: 15.7% and 8.6%.

**Cell 62 (ed8) and the record's notes**
- Quoted: "192 of 307 (A)". Printed: 193 of 308.
- Quoted: "p 2.2e-146". Printed: 1.0e-147.
- Quoted: "1.9e-144". Printed: 1.95e-145.
- Quoted: "p 1.2e-06 or below". The largest printed is 1.4e-06.
- Quoted: "Every … reading gives p < 1e-14 against 5% of all units". Rule b, sel_a, A prints 3.95e-13.

**Cell 66 (fig2e) and the record's notes, `measured` and response**
- Quoted: "-0.645 s in monkey A (44 units) … -0.705 s in monkey M (29 units), just outside it". Printed: −0.655 (45) and −0.780 (30). M is 0.08 s outside the range, not just outside it.
- Quoted: "37 of 56 … 26 of 34". Printed: 36 of 55.
- Quoted: pooled "3.8e-66 and 3.5e-47". Printed: 1.7e-71 and 1.6e-40.
- Quoted: code window "-0.690 (A) and -0.715 s (M)". Printed: −0.675 and −0.825.
- Quoted: "Rule b gives -0.610 … -0.575". Printed: −0.625 and −0.595.
- Quoted: "rule a1 -0.595 s". Printed: −0.645.
- Quoted, by direction: "-0.665 and -0.525 … -0.555". Printed: −0.685, −0.520 and −0.575.
- Quoted: "the same (-0.645 and -0.705 s)". Printed: −0.655 and −0.780.
- `measured: -0.645` is described as "median over both monkeys". The printed pooled value is −0.695.

**Cell 68 (fig2f) and the record's notes, `measured` and response**
- Quoted: second peak "-1.195 … -1.025". Printed: −1.245 and −1.070.
- Quoted: third peak "-1.400 and -1.785". Printed: −1.445 and −1.745.
- Quoted: intervals "0.543 … 0.368 … 0.423 and 0.442". Printed: 0.550, 0.344, 0.407 and 0.394.
- Quoted: "only in monkey A under rule a1 (-1.305 s, 12 units) and the GP-null reading (-1.305 s, 27 units)". Printed: −1.310 and −1.285 (28 units). The main reading with the code window also puts A in range (−1.255 s).
- Quoted: "Leaving out A 09172019 gives -1.215 s". Printed: −1.24.
- `measured: [-1.145, -1.575]`. Printed pooled values: −1.205 and −1.495.

Everything else checks against the outputs: fig1bc, fig3b, fig3d (numbers), ed4e, ed4fg, ed5, fig4h, ed3, fig4g, fig4d, ed2b, the data-check cells, the Summary, the README and the remaining findings. The README and the Summary agree with the record's 24 outcomes.

**My round-1 reasons in the record.** They are in my own words and accurate, including the fig3d reason, which repeats my misreading of the Methods. "21 of 24 agree" is correct: ed3, fig2f and ed5 disagree.

### 3. Round-1 points

**Resolved**
- Problem 1 (bank null): the bank threshold is now about 0.4 SD conservative, against about 2 SD before.
- Problem 2 (downstream claims run only on the main reading).
- Problem 4 (GP variant not run).
- Problem 6 (monkey M clock).
- Problem 7 (pseudo-replicated bootstrap t-test; a paired variant is now shown).
- Problem 8 (Fano false-positive rate).
- Problem 9 (trial-count control for ed2c).
- Problem 10 (own null not matched to k).
- Problem 11 (sessions without a clock check; enough breakdowns are now shown).
- Every item in round-1 section C.
- Problem 5, for ed5, fig4g and fig4d.

**Remaining, bearing on a conclusion**
1. Most conclusions and record entries for the claims that use the periodic set (fig2, fig2d, ed2c, ed4d, ed10, ed8, fig2e, fig2f) quote numbers from an earlier run. Three `measured` fields are wrong (fig2, fig2e, fig2f), one is off by one count (ed10), and the fig2e and fig2f texts state things that are no longer true: "just outside", and "only a1 and GP-null". Every outcome survives with the printed numbers, but the text must be regenerated from this execution.
2. fig3d (problem 3): the main reading departs from the Methods' explicit centring. I would record partially_reproduced, with the per-bin centring as a variant that gives reproduced.
3. fig4g: "partially_reproduced" applies a rule the criterion does not define. I would record not_reproduced.
4. Problem 5, still open for fig4b and ed6d: both are simulations that need no data, blocked only for run time. ed5efg's monkey side remains computable.
