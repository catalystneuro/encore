**Verification report, round 2: Huszár et al. 2022 on DANDI:000552 (0.261113.1035)**

The claims file has 44 claims, and the attempt record gives an outcome for each of them. The record has 17 reproduced, 10 partially reproduced, 7 not reproduced and 10 blocked (5 data_missing, 5 too_large). Twelve outcomes are marked `assumed: true`.

### 1. Outcomes

**I agree with 38 of the 44 outcomes as recorded.** The six I don't fully accept:

- **sessions-durations (not_reproduced):** I still read this as partially reproduced, as in round 1.
  - On the 96 homecage sessions the count, median and range all hold (cell 14).
  - The only failure is "every session holds non-REM", and the criterion has no category for that case.
  - The record states my disagreement and refers the gap to a reader. That is acceptable, but the gap is in the claims file and is still open.
- **ed10-waveform-matched-controls (blocked, data_missing):** I disagree, and this is a claims-file issue.
  - `depends_on` lists ed2-waveform-validation. Yet the criterion computes the waveform distance "on spontaneous spikes", so it needs none of the light-evoked waveforms that block ed2.
  - The claim's own parts were computed (cell 127). Under its criterion they give **not reproduced**: "Not reproduced when an SBD-DBD comparison fails at p < 0.05", and the ratemap comparison at > 60 µm gives p = 0.0779.
  - The block therefore hides a failing result.
- **fig3c, fig3e, ed6, fig4d (blocked, too_large):** I don't accept "too_large".
  - The 9 to 12 GB figure is for a dense double-precision matrix. The record itself says a chunked covariance "was not attempted".
  - fig4d is a simulation, and the record gives no size for it at all.
  - These four, and ed7 through its dependency, are "not attempted", not too large.
- **fig6c-novel-ratemap-corr-higher (not_reproduced, assumed):** the assumption is stated, but it is weakly supported and it decides the outcome.
  - At the assumed 1 cm per unit, p = 0.784. At 2 cm and at 0.5 cm per unit, p = 2.1e-6 and 0.0104, both of which would give partially reproduced (cell 99).
  - The evidence offered for 1 cm per unit is not in any printed output: neither the "116 units for 110 cm" track nor the open-field sizes in lab units. Only the bin counts (1188, 576, 2332/2376; cell 93) hint at the sizes.
  - At 1 cm per unit, openField_coolbox would be 22.5 × 22.5 cm, which is small for an open field.
  - I accept the outcome only as conditional on the scale. The data do not decide it.

**The other assumptions are stated and reasonable:**

- **Theta channel** (fig1f, fig2c, fig2d, fig6c-theta, fig6d-rate, fig7fg): stated, with layer-centre and "rule-only" variants. fig2c's SBD median, 0.0169, misses tolerance by 0.0001 and is within it on the centre channel (cell 55), so "partially" rests on the channel. That is stated.
- **Depth reference** (ed3): stated. Not reproduced follows from the criterion, and it matches the paper's "weakens bursting differences", which this attempt does not find. The fallback depth is used for 376 of 664 cells.
- **Connection detector** (fig7b, fig7ce, fig7d, fig7fg): stated, and every assumed detail is varied (cell 109).
- **fig7d:** the peak bin (0.0269) beats the 20 to 29 ms bin (0.0266, centre 24.5 ms, inside 13.5 to 25.3 ms) by 0.0003, with no uncertainty given (cell 117). Not reproduced is right as a literal reading, but fragile.
- **fig6f (assumed):** the scale variants were not run, as the record says. The interaction is significant (p = 0.0073), SBD is below DBD in the lowest tercile, and the Supplementary Table 5 means that the criterion says to report are not compared (cell 105). None of this changes the outcome.
- **fig6d-info and fig6e:** both carry the open-field-scale deviation without `assumed: true`. That is acceptable, because both outcomes are the same under every scale reading (cells 96, 102).

### 2. Statements the outputs do not support

- **Attempt record, ed5 notes and response:** it says "1.000 … 1.000 … 0.998 for familiar ratemap correlations … and 0.598 for novel". Cell 125 prints familiar 1.000 and novel 0.604.
- **Attempt record, ed10 notes:** it says "0.132 for ratemap correlations". Cell 127 prints "familiar ratemap 0.106".
- **Attempt record, fig6f notes:** it says "the earlier run without them gave p = 0.016 and 0.013". This notebook has no such output.
- **Attempt record, fig6c-novel, fig6d-info, fig6e and fig6f deviations, and the metadata_insufficient finding:** they cite "116 units for 110 cm of linearized track", the open-field sizes in lab units, and "0 to 1 in some". None of these is printed (cells 93 and 94).
- **Cell 132, Summary:**
  - "finds about 60% more connections than the paper under every variant of them": at alpha 1e-5 the count is 38,402, 20% more (cell 109).
  - "Every theta claim is also shown … on the 76 sessions alone": fig6c-theta and fig6d-rate have no 76-session variant, only "6 of 12" is printed (cells 58 and 61), and fig7fg has neither variant.
  - "follows the Methods' rule … in 76 of 104 sessions": see the next point.
- **Cell 47 and its uses (cells 46, 132; record fig2c and fig1f):** the 76 sessions counted as following the rule include 6 whose channel lies *below* the layer centre (`dy_theta` −300, −300, −260, −260, −20, −20 µm). By the notebook's own check, larger rel_y is above (320 of 327 positive channels). At most 70 sessions follow "above the centre".
  - e13_1f1_200305 and _200307 have no non-REM sleep. For them `pick_theta_channel` falls back to all ripples, which is not stated.
- **Cell 121:** it says slopes "0.0040, 0.0029 and 0.0017 for nonresponsive pairs", but the theta slope for reading (a) is 0.0028. "all rise with convergence": for ratemaps the (a) quintile means are 0.0111, 0.0115, 0.0109, 0.0096 and 0.0206, so they rise only in the top quintile.
- **Cell 112:** "medians above the paper's (0.385 to 0.455 against 0.278 to 0.368)". The second range is this attempt's DBD medians across variants, not the paper's values.
- **README:**
  - "Cohort, sessions, units and light-responsive counts (5 claims)": only 4 claims fit that row (cohort-birthdates, st1-animal-sessions, unit-count, ed2-light-responsive-count), and the README's rows sum to 45.
  - "two sessions without sleep states": they have sleep states, one Awake row each; they have no sleep (cells 5 and 14).
- **Cell 76 and the record's fig5b notes:**
  - "no reading brings the medians within tolerance": under reading (b), coverage at E13.5 (34.5) is within tolerance (cell 75).
  - "25 to 40% below": the concatenated-map medians are 29.5 to 40% below.

Everything else in the Result cells, the Summary, the README and the record's notes matches the printed outputs.

**My round-1 reasons** are given faithfully, mostly in my own words, with problem numbers kept and the smaller points folded into the claims they concern. One misstatement: for ed3 the record shows `agrees: true`, but my reason said the claim was testable and that "not reached in time" is not a data limit. I disagreed with the block; that should not read as agreement. The same applies, less strongly, to ed5, ed7 and ed10 (problem 4).

### 3. Round-1 points

**Resolved:**

- **Problem 1 (theta channel):** pre-ripple baseline, µV conversion, positions printed, variants run. A residual remains, below.
- **Problem 2 (novel environments):** open fields included, e16_3m2_211211 explained, units and bin counts printed.
- **Problem 3 (detector):** all assumed details stated and varied.
- **Problem 4 for ed3:** now tested.
- **Problem 5 (maze trials):** the trials table gives the same counts.
- **Problem 6:** ACG rounding fixed.
- **Problem 7:** the two-way model has the same residual mean square, and the Front/Back faces are explained.
- **Problem 8:** tercile edges fixed.
- **Problem 10:** recorded as a finding.
- **Section C:** all items printed.

**What remains that bears on a conclusion:**

1. **ed10** is blocked by a dependency its criterion doesn't use, and its computed parts give not reproduced (p = 0.078). This is a claims-file issue; it is the rest of problem 4.
2. **fig6c-novel** depends on an open-field scale whose evidence is not printed and that both alternative scales contradict.
3. **Theta channel:** 6 sessions use a channel below the centre but are counted as following the rule, and the two sessions without non-REM use wake ripples, unstated. fig2c sits 0.0001 from tolerance, so even this could change its outcome.
4. **Blocked as too_large without an attempt:** fig3c, fig3e, ed6, fig4d, and ed7 through its dependency.
5. **sessions-durations:** the criterion still has no category for this case (problem 11). It is with a reader.
6. **Wrong numbers to correct:** ed5 and ed10 in the record (no outcome changes), the "60% under every variant" sentence in the Summary, and the README's count of 5 claims.

Problem 9 (the paper's pair set of 315,722) is stated but still unexplained. It does not change an outcome, because the counts fail either way.
