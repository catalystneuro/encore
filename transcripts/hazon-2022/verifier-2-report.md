**Verifier report, round 2: Hazon et al. 2022 on CRCNS hc-30**

The claims file has 29 claims and the attempt record has 29 outcomes, one for each claim. They are 23 reproduced, 2 partially reproduced, 3 not reproduced and 1 blocked. Six outcomes rest on an assumption (`assumed: true`).

### 1. Outcomes and assumptions

I agree with all 29 stated outcomes. Each assumption is stated, and I find each one reasonable:

- **suppl-table1 (not_reproduced):** the assumption is the 1180 cm cap on fitted widths. Without the cap the mean width is 37.6 cm (NB1 cell 16), which is within tolerance and would make the outcome partial. The record says this. Treating the 195 fits wider than ten times the track as failed fits is reasonable, since the median width is 11.5 cm. The paper's SD of 48.5 cm points to a long tail, so whether the paper kept such fits cannot be known.
- **fig3f (reproduced):** the assumption is the code's test direction, which the criterion's last clause allows. The statement's "decreasing over the run" is contradicted: the legend's direction gives p = 1.00 (NB1 cell 35). Reproduced on the code's direction follows the criterion. Partially reproduced would also have been a defensible reading.
- **pf-width-variance-not-predictive (reproduced):** the assumption is the Supplementary Table 2 filter. It is shown at interval widths of 1 to 3 SE, giving p = 0.056 to 0.139 across sessions. The four sessions it drops are misaligned sessions. Reasonable.
- **fig5cd (reproduced):** the assumption is the legend's width distributions, as the criterion provides. Fine.
- **fig2d (reproduced):** the assumption is the SVM with C = 1. The change between C variants (at most 0.34 cm, NB2 cell 10) is well inside the margin to tolerance. The same decoder underlies the other eight decoding outcomes, but only fig2d is flagged as assumed. That labelling is inconsistent but does not change any outcome.
- **suppl11b (partially_reproduced):** the assumption is leaving out failed fits and misaligned sessions. It is reasonable and stated. fig4c and fig5f match the code's printed values when the misaligned sessions are included, so the paper probably fitted those sessions too. That suggests the paper's fit behaved differently on flat IMSE curves, and the exclusion stands in for that difference.

### 2. Sentences the printed numbers do not support

- **NB2 cell 41 (Summary):** "The reduced repetitions are therefore not the likeliest reason the claims built on I0 and N fall short; the misaligned sessions and near-linear curves are." This holds for suppl11b. For saturation (cell 22: 717 to 2,487 without those sessions) and suppl8 (cell 33, same variant) the claims still fail without the misaligned sessions and degenerate fits, so those sessions are not shown to be the reason.
- **NB2 cell 23, and the saturation notes in the record:** "the reduced repetitions do not explain the failure." The fit check (fitcheck cells 8 and 12) covers only Mouse2011, Mouse2012 and one Mouse2028 session. The cleaned variant's bounds, geometric-mean N of 207 and 716, equal reading (a)'s Mouse2022 and Mouse2023 (Mouse2023 has a single session), and neither animal was checked. The per-animal values of the cleaned variant are not printed. The suppl8 note "the I0 and N fits change little with the paper's 80 subsets" has the same limited basis.
- **Record finding (misaligned sessions):** "Mouse2011 105556 and 104511 give I0 about 240 … with 80 subsets as with 4." With 4 subsets, 104511 gives I0 = -3.7e-5 and N = -8.95 (fitcheck cell 8). "Their IMSE curves are flat" is shown for only four of the six sessions (51, 83, 84, 92). The IMSE of sessions 73 and 97 is not printed.
- **Record finding (joined sessions):** "with the rate rising about 2.5 times in its second part" is not in any output. NB1 cell 5 prints only 77.6 against 12.0 events per neuron per minute.
- **Record finding (positions):** "the first valid trial of Mouse2022 093722 includes such frames" is not printed. "Far outside the track" overstates the Mouse2028 case, which is -23 px (NB1 cell 5).
- **Record finding (questions for the authors), point 4:** "None of the readings tried gives more than two of the seven values" contradicts the record's own suppl-table1 notes and NB1 cell 16: without the cap there are three.
- **Record fig4a notes:** "A preparatory run with 20 splits peaked at the 6th" has no output behind it. The record says so, but it should not be used as evidence.
- **NB2 cell 41:** the decoding error "up to 51.9 cm" is attributed to misaligned sessions, but no output names the session with 51.88 cm.

All other "**Result:**" sentences, the NB1 Summary, the README and the remaining notes match the printed outputs. I checked them number by number against NB1 cells 10 to 66, NB2 cells 8 to 40 and fitcheck cells 8 to 13.

The verification block gives my round-1 reasons in my own words, lightly condensed. It maps all nine problems and my request for a fit table onto the right claims and keeps their substance. The `agrees: false` entries (fig3f, pf-width, suppl11b) correctly record that I disagreed with the round-1 outcomes, which have since been changed to mine.

### 3. Round-1 points

Resolved:
- **Point 2:** the suppl8 variant was run. It is still not reproduced.
- **Point 3:** the filter's sensitivity is shown and the outcome is recorded as resting on the filter.
- **Point 4:** the docstring and the defaults now give C = 1 (`hc30.py:174`, `hc30.py:180`).
- **Point 5:** the modulation rule is explained; it removes only silent cells. The cap is recorded as an assumption.
- **Points 6 to 9:** each is now recorded as a deviation or in the notes.
- **Fit tables:** these were requested in section C and are now printed (NB2 cell 16, fitcheck cell 10).

Partly resolved, and bearing on a conclusion:
- **Point 1 (saturation, suppl8, suppl11b), repetitions.** On 13 sessions with usable fits, N changes by a median factor of 1.09 (0.67 to 2.02), and the failed fits are the misaligned sessions under both settings. This settles suppl11b and makes a repetitions-only explanation unlikely for the lower saturation bound: moving 717 down to 346 ± 10% would need about half the current N across Mouse2022's sessions. Two things are still open:
  - The upper bound in the cleaned variant comes from a single Mouse2023 session that was not checked, and per-session factors reach 0.67.
  - How N depends on the decoder (C, voting against loss-weighted decoding) was never tested, although both cleaned bounds are about twice the paper's. Reading (a)'s Mouse2028 value of 886 also includes the degenerate N = 1.0e9 of session 19, which inflates that bound; this is not stated.

  The not_reproduced outcomes stand, but they may reflect this attempt's decoder rather than the data.
- **suppl11b exclusion.** See section 1: the partial outcome rests on excluding sessions that the paper evidently fitted.
