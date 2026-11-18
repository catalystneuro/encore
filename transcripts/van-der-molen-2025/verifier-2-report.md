**Verifier report, round 2: van der Molen et al. 2025 on DANDI:001603 (0.260923.0623)**

The claims file has 50 claims, and the attempt record has 50 outcomes: 31 reproduced, 11 partially reproduced, 7 not reproduced and 1 blocked. Five outcomes carry `assumed: true`: ed4d, supp8, fig7d-murine-organoids-slices-same-lag, supp10b and supp27. The README's counts match the record.

### 1. Outcomes

I agree with 48 of the 50 outcomes. I disagree with two.

**ed4d-gabazine-rank-order: reproduced (assumed). I disagree.**
- The criterion requires gabazine to be higher "under both readings". Under the ratio reading it is not (−1.15, p 0.6; cell 51).
- The claims file reads the paper correctly here. The Supplementary Methods section "Firing rate peak rank order correlations" names (A−B)/(A+B) for exactly this measure, while the Extended Data Fig. 4D legend says z-scored. The paper contradicts itself; the claims file did not misread it.
- The case for dropping the ratio reading holds only for a mean-based model on ratios computed per burst pair. Cell 51 also prints per-recording medians of the ratio, and these are stable (0.855 to 0.996). They rise in three organoids and fall in one (MO14: 0.959 to 0.953). So the ratio reading has not been shown to carry no information.
- Under the claims file this should be blocked as methods_underspecified, which was my round-1 outcome.
- The record says "As the verifier finds the ratio reading gives no information, the legend's z-score is adopted". I called the ratio reading degenerate, but I concluded blocked. I did not say the z-score should be adopted.

**supp10b-rank-order-by-model: reproduced (assumed). I disagree.** It rests on two assumptions, and neither is consistent with the claims file.
- The ratio reading fails under both recording lengths (p 0.66/0.49 and 0.69/0.38; cell 129).
- The z reading passes under length (a) only (p 0.032/0.031). Under (b) it fails (0.064/0.099).
- The claims file says both lengths "are run where the outcome could depend on it", and that disagreeing readings make a claim methods_underspecified. The outcome should be blocked as methods_underspecified, not reproduced.

**I agree with the other 48.** Points on some of them:
- **fig1e and fig3f (partially reproduced).** I accept the author's argument: the criteria require every reading, so my round-1 "blocked" was wrong.
  - The record's rationale for fig5f is that "the criterion defines no partial outcome".
  - That applies equally to fig1e, fig3f and supp26, which are recorded as partial.
  - The outcomes are defensible on substance, but the record should state one rule and apply it to all four.
- **fig7d-murine-organoids-slices-same-lag (not reproduced, assumed).** The assumption is stated and reasonable: the code's lag table has no zero lags. The outcome does not depend on it. The second contrast, which the criterion "judged the same way", fails under every reading (p 0.008, 0.006, 0.029).
- **supp8 (assumed).** The link by identical ordered positions is stated, reasonable, and shown alongside each recording's own result.
- **supp27 (assumed).** The assumption is stated. The outcome is partial under both readings of the fit check, so it does not change the outcome.
- **supp26 (partially reproduced).** I agree that it is not reproduced in full: PR > MS gives p 0.056, against the paper's P < 0.0001. The label question is the consistency point above.
- **fig5f (not reproduced) and supp5 (blocked, methods_underspecified).** I agree with both. I accept the author's reading of the protocol for supp5.
- **fig7b, fig7e and fig7c-backbone-pairs-above-random (not reproduced).** I agree under the claims file. Each fails in the murine organoids, which rest on 5 of 9 recordings (see section 3).

### 2. Text against the outputs

These sentences are not supported by the printed numbers:

- **Cell 29.** "HO7 has no backbone unit here (no unit fires twice in all 24 bursts)." HO7 has 21 bursts (cells 8 and 12).
- **Cell 10.** "median coarse rate 0.47 to 1.07 against at most 0.6 elsewhere". Pr2's median is 0.685 (cell 9).
- **Cell 130.** "The judged contrasts keep their direction and significance under (b), with these exceptions". The fig7b murine organoid backbone-minus-non-rigid contrast changes sign (0.026 to −0.003; non-significant both times). It is not listed.
- **Cell 142, Summary.** "Every recording the paper analyses is in the dandiset as a sorted file". The next sentence says MO12's baseline and all murine longitudinal recordings are missing.
- **Cell 142 and the fig2 notes.** "the backbone units and burst counts of HO1 to HO4 equal the numbers in the paper's processed tables". The notebook prints the counts but never compares them with any processed table.
- **Record finding identifier_missing, and cell 49.** These say unit positions are identical across conditions for MO10, MO11 and MO14 and differ for MO13. No output shows this; it appears only as a label inside a print statement (cell 48).

Everything else checks against the outputs:
- the other "**Result:**" sentences;
- both Summary tables;
- the README;
- the outcome notes in the record, including numbers, p-values, counts and ranges.

The record states my round-1 reasons faithfully, mostly in my own words with details added from my numbered problems. The one exception is the ed4d inference described in section 1.

### 3. Round-1 points

**Resolved:**
- 1, duplicate bursts. Overlapping bursts are now merged, and the counts at 700, 800 and 2000 ms are printed.
- 2, supp8 is tested.
- 3, the HMM scoring is now symmetric. The smallest margin is 0.015 (HMM notebook, cell 6).
- 4, reading (b) of the recording length is run (cells 128 and 129).
- 7, tests now use Satterthwaite t.
- 8, the 30-spike rule counts spikes over the whole recording.
- 9, the docstring of `burst_segments_compressed` is corrected.
- 10, 12 and 13 are covered in the notes and findings.
- The deviations in 11 are stated.
- Every item in my list C (what I could not check) has been run: shuffle completeness, the cause of the missing murine bursts, supp18, the borderline contrasts, reading (b), supp8, supp27 and fig4f.

**Still bearing on a conclusion:**
1. **ed4d and supp10b.** Both outcomes override the claims-file criterion (section 1). Both should be blocked as methods_underspecified.
2. **The murine organoid outcomes.** The cause of the missing bursts is now shown (peaks reach 3.0 to 3.7 times the RMS) and filed as a finding.
   - Every murine organoid failure (fig7b, fig7e, fig7c-backbone-pairs-above-random) and the partial results (fig7a-primary-higher-rate, fig7d) still rest on 5 of 9 recordings, under detection that the paper evidently did not use for these organoids.
   - MO3 is kept with 4 bursts, and 160 of its 234 units are backbone.
   - No analysis without MO3 is printed.
   - The notes should say that these failures may come from the unstated murine detection parameters. A run without MO3 would show how much it drives them.
3. **The partial-outcome rule.** fig5f says partial is not allowed when the criterion defines none, but fig1e, fig3f and supp26 are recorded as partial. One rule should be stated and applied to all four.
