**Verifier report, round 2: Geiller, Vancura et al. 2020 (doi:10.1016/j.neuron.2020.09.013) on DANDI 000625 v0.231114.0019**

The paper text is the PMC7736348 author manuscript, saved as `paper/PMC7736348_bioc.json` and `paper/PMC7736348.txt`. The paper checks out on these points:
- TG19 is a strategy 1 mouse.
- The negative-field rule is below the 5th percentile, with no peak threshold.
- The paper counts 44 CCKC and 119 IvC/NGFC from 7 mice.
- Correlations are averaged over sessions.
- Mice were 3 to 5 months old.

### 1. Outcomes

I agree with all 28 stated outcomes.

- **fig4e-bic-recurrence:** in round 1 I would have recorded "blocked (data_missing)". The record keeps "blocked_by: other" and cites the protocol's example of too few units under the claim's own rule. `docs/protocol.md` is not among my materials, so I could not check that citation. The outcome itself is not in question.
- **fig2c-most-positive and fig4f-selectivity-no-difference:** I agree that both pass their stated criteria. Both are fragile, for the reasons in sections 2 and 3.

### 2. Statements the numbers do not support or only partly support

- **Cell 42, and the fig4-fraction-negative notes**
  - Quoted: "Under the paper's rule the two kinds of field are coupled … 55.8% of ROIs have both kinds … Counting only ROIs with a negative field and no positive field gives 10.6%, inside the paper's range".
  - The 55.8% and 10.6% use the positive set without the peak rule. With the paper's positive rule (peak above 100%), the same variant gives 0.653 (cell 41, last column). The text does not say which positive rule it uses.
  - Cell 41 also prints "negative among ROIs not positive" = 0.377 (0.268, 0.407, 0.457 by session), against 0.108 on the surrogate. So ROIs with no positive field still have negative fields at about 3.5 times the surrogate rate. The coupling explains part of the 66.4%, not all of it, and the notes present it as the explanation.
  - The notebook never shows the coupling itself. It rests on my round-1 synthetic test, which the record does not cite.
  - The outcome (not_reproduced) is unaffected.
- **Cell 22, and the fig2c-most-positive notes**
  - Quoted: "averaging over sessions lowers the negative fraction, and the all-ROI reading fails because of it."
  - Per session, the all-ROI fraction is 0.065, 0.111 and 0.089 (cell 19). Only 0.089 is inside 0.088 to 0.108, so the all-ROI reading would fail in two of three sessions even without averaging.
  - Neither text says the converse. The six-subtype reading, which passes, is 0.055, 0.143 and 0.164 per session. All three are outside the range, so it passes only because of averaging.
  - Cell 20's smoothing and clock variants are printed only for the all-ROI denominator. "Change no fraction shown by more than 0.005" is true of what is shown, but it says nothing about the six-subtype reading that carries the outcome.
- **Cell 48, and the fig4f notes**
  - Quoted: "The indices are small because dF/F here has a baseline near 0.12 in every bin."
  - The median dF/F (0.11 to 0.13, cell 5) is consistent with this. No output shows the per-bin baseline of the tuning curves or that it causes the small indices.
- **README:** "Depth, SWR, novel-context, goal-oriented learning, VIP and classifier findings (12 claims) | Blocked".
  - The count of 12 includes fig4e-bic-recurrence, which none of those headings covers (it is blocked by having only 3 BiC).
- **Everything else checks:** every other "**Result:" sentence, the Summary table and lists, and the numbers in the record's notes and findings match the printed outputs (cells 5, 8 to 10, 13 to 14, 16, 19 to 57).
  - Minor: the record's s2-lags reason gives "p of at least 0.82" where cell 33 shows 0.816. It rounds to 0.82.
- **My round-1 reasons:** the attempt record restates them faithfully in its own words, including the [affects a conclusion] markings for problems 1, 3, 5 and 6, and my data_missing view on fig4e. Two parts of my evidence are left out:
  - the AR-noise false-positive rates (0.22 positive, 0.20 negative) under fig4-fraction-spatial;
  - the synthetic demonstration under fig4-fraction-negative that a cell with only a negative field is flagged positive under the rule without the peak. This bears on the "negative only" variant, because it means that variant excludes some real negative cells.

### 3. Round-1 points

**Resolved**
- **Depth and coordinates (C).** Cell 5 prints the PlaneSegmentation columns, the pixel_mask fields (no z), the mask ranges and the placeholder ImagingPlane fields. Blocked is confirmed for fig1-depth, fig2d and s3.
- **Behavioural series (C).** Only reward and water intervals exist, and there is no lick record. Blocked is confirmed for fig6.
- **Frame-rate uniqueness (problem 2, C).** The best score more than 0.1 Hz from the fit is 0.51, 0.39 and 0.52, against 0.80, 0.72 and 0.87 at the fit (cell 8). The fitted rate is unique within the range searched.
- **Run-stop per session (C).** CCKC give −0.005, 0.024 and −0.023 per session (cell 36). The partially_reproduced outcome stands.
- **Per-ROI r table (C).** Cell 21 shows 17 of 74 subtyped ROIs changing sign between sessions, 7 of them CCKC.
- **Session order (problem 6).** The conflict is now documented in cells 6 and 55, the s6 deviation and a finding. Nothing in the files resolves it.
- **Problems 4, 7, 8 and 9:** these did not affect a conclusion, and their caveats are now acknowledged.

**Partly resolved: placed-field overlap (problem 1)**
- The overlap is now counted (cell 41). The interpretation needs the qualifiers in section 2.

**Remaining issues that bear on a conclusion**
1. **fig2c-most-positive.** It is reproduced only under the six-subtype reading after averaging over sessions. No single session is in range under that reading. Under the all-ROI reading the result is in range only in session 21322, and it is 0.088 if the per-session fractions are averaged. One of 74 ROIs flipping sign would end the match. The notes should say that averaging is what makes the six-subtype reading pass.
2. **fig4-fraction-negative.** The coupling explanation is overstated: the negative-field rate is 0.377 even among ROIs with no positive field. The 10.6% variant also depends on the positive rule without the peak. The outcome is unchanged.
3. **ROI identity across sessions (problem 5).** This is unresolvable from the data. It bears on every claim that averages over sessions (fig2c, s2-lags, fig4f, fig4h, s6) and on whether s6-later's "above chance" fails because of drift or because of a mismatched mapping. It is disclosed.
4. **Session order (problem 6).** This is unresolvable and determines which pairs stand in for 1 h and 24 h in s6-later-lower-above-chance. It is disclosed.
