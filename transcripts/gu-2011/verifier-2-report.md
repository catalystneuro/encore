**Verifier report, round 2: Gu et al. (2011) on CRCNS stc-1**

**1. Outcomes**

The claims file has 35 claims and the attempt record has 35 outcomes: 17 tested and 18 blocked.

I agree with all 35 outcomes. Three need comment:

- **fig7c-narrow-preferences, now partially_reproduced.** I agree. This is the change I asked for in round 1.
- **fig4dh-lateral-more-sensitive, now reproduced (it was blocked).** I agree that it meets the criterion as written: lateral thresholds are lower with p < 0.001 under at least one reading. The result is fragile, though, and the record does not say so in full:
  - Only 1 of the 8 claims-file readings passes (cell 57: weighted vector sum, spline, log10, two-factor ANOVA, p = 1.9e-07).
  - In that reading the preference × condition interaction is significant (p = 0.026). Neither the conclusion (cell 58) nor the notes report this.
  - The two-factor ANOVA counts each of the 129 units twice, once per condition.
  - With spline-peak preferences, no reading reaches p < 0.05.
  - See section 3 for a deviation the record leaves out.
- **fig8ab-choice-probability-lateral, not_reproduced.** I agree. It holds under every preference reading, including the corrected vector sum (p = 0.80). It also holds under the distance-from-0.5 variant (p = 0.10 to 0.17), so it does not depend on how the CPs are signed.

There are 11 outcomes marked `assumed: true`. Each assumption is stated and reasonable:

- **Pooled rnoise taken as the mean of the two per-condition values:** fig2b, figs2b, the four fig5 claims and fig8cd.
- **Tuning amplitude 30 and baseline 10 spikes/s over 1 s:** fig6a, fig6b, fig7a and fig7c. fig6a is sensitive to this choice: in cell 44, baseline 2 gives 4.32 and baseline 20 gives 5.90, both outside 4.5–5.5. The record states this.

Points where the claims file misreads or leaves out part of the paper (reported, not corrected):

- **fig4dh-lateral-more-sensitive:** The criterion leaves out the Figure 4 legend's selection: "Only neurons with significant heading tuning (p < 0.05, ANOVA) were included." This bears on the outcome (section 3).
- **fig8ab-choice-probability-lateral:** The criterion tests raw CP. The Figure 8A legend describes CP "more deviated away from the chance level of 0.5." The notebook runs this as a variant, and the outcome is unchanged.
- **fig8ab and fig4dh, any reading:** The rule "reproduced under one reading" is permissive when there are 8 or more readings. This is a design point, not a misreading.

**2. Text checked against the printed outputs**

Every "**Result:**" conclusion (cells 14 to 64) matches the printed numbers. That includes the new fig4dh conclusion in cell 58 (p-value ranges 0.013–0.77, every median lower, 2 values left out) and the fig8ab conclusion in cell 61.

Statements the numbers do not support:

- **"the main result matches the paper to the third decimal"**
  - Where: Summary, cell 65; README line 37; attempt-record finding (methods_unavailable, "matching 0.023 and 0.116 to the third decimal").
  - Cell 16 prints 0.0241 and 0.1190 against the paper's 0.023 and 0.116. At three decimals that is 0.024 against 0.023 and 0.119 against 0.116. Both are within the paper's SEMs, but they do not match to the third decimal.
- **"Most outcomes rest on one assumption: ... the paper's pooled value is taken as their mean"** (README line 36)
  - Only 7 of the 17 tested outcomes rest on the pooled-rnoise assumption.
  - Another 4 rest on the tuning amplitude and baseline instead.
- **Attempt record, methods-single-vs-multiple-electrodes notes and a metadata_insufficient finding:** "Ten file_ids of monkey 17 end in 's'". No cell prints this.
- **Attempt record, fig7b-msdt-pairs notes:** "Seven pair recordings share a cell id with experiment 1 units". No cell prints this.
- **README line 42, "It takes about two minutes":** No output gives a run time. Cell 1 prints only the load time.
- **fig4dh deviation, "a different window scales all thresholds alike":** This is not exact. In `stc1.neuron_threshold`, the trace term 0.5(f'/f)² does not scale with the counting window. The effect is small and does not change the outcome.

The attempt record states my round-1 reasons accurately for every claim, including problems 1 to 8, which it places under the matching claims. It mostly uses my own wording. For fig4dh it records `agrees: false` with no outcome, which matches my round-1 report: I asked for the claim to be tested and did not propose an outcome.

**3. Round-1 points**

Resolved:

- **Problem 1:** The vector sum is now weighted for the uneven heading spacing. Cell 56 checks it on synthetic curves, and fig8ab is rerun with it.
- **Problem 2:** fig4dh is now tested.
- **Problem 3:** The conflict with the claims-file point-count rule is stated in cells 62 and 64 and in the notes. The claims-file readings support the argument made there.
- **Problem 4:** Fixed in cell 0.
- **Problem 6:** Cell 43 prints the rsignal difference (5.6e-07).
- **Problem 7:** Fixed in cell 11.
- **Problem 8:** Recorded as a finding.
- **From "Not checked":**
  - fig5: bootstrap intercept intervals added (cell 37); they overlap.
  - fig7a: crossover reported, rsignal = −0.0216 (cell 50).
  - fig8ab: CP sign check added (71.7% of CPs above 0.5).

Cannot be resolved from this data set, and stated as such: problem 5 (renormalization or outlier removal), and whether the 258 CPs are among the paper's 311.

What remains that bears on a conclusion:

1. **fig4dh-lateral-more-sensitive.**
   - The analysis applies no tuning-significance selection, which the Figure 4 legend uses. The record does not list this as a deviation.
   - Without it, poorly tuned units enter the test. Their thresholds are huge (spline maximum 2760°; linear reading up to 1e17°) and their preferred headings are arbitrary. This may explain why the vector-sum and spline-peak readings agree on only 71.7% of group labels, and why no spline-peak reading passes.
   - The selection cannot be applied exactly to trial-averaged curves. It should be listed as a deviation, together with the interaction (p = 0.026) and the double counting of units, so a reader can see how much the "reproduced" outcome depends on one reading.
2. **The "third decimal" statement** in the Summary (cell 65), the README and the attempt-record finding should be changed. It overstates the support for the pooled-rnoise assumption.
