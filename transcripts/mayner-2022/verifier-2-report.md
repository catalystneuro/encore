# Round 2 verifier report: attempt 000036-mayner-2022-01

## 1. Stated outcomes

The claims file has 27 claims. The author's link claim, session-link, is now inside the file. The attempt record gives an outcome for all 27. I agree with all 27 outcomes, with these remarks:

- **session-link, ext1-2-cell-counts, fig3a, fig3b, ext3-1, table1-permutation, fig4-locomotion-effect-size, fig5-multivariate-layer, fig5-multivariate-area, fig6-category-decoding, ext6-1-identity-decoding, fig7-stimulus-effect, fig7-snake-highest, fig8-nd-sd-correlation, fig8-no-sd-relation-controlled (reproduced):** I agree. The printed values are the same as in round 1. The new checks of the statistics code on the paper's own data (cell 26) back these outcomes further.
- **design-sessions (now reproduced):** I agree. This was my round-1 outcome. The criterion asks for the paper's 45 sessions with its counts, and cell 29 prints them. The 12 extra sessions are rightly recorded as a finding.
- **ext3-2-sensitivity (not_reproduced):** I agree under the claims file's rule: 36 of 108 sets agree (cell 46). The outcome reflects the rule as much as the data (see section 3).
- **discussion-session-effect-sizes (partially_reproduced):** I agree on the Methods formula. Cell 53 now prints the failed check: the largest d is 1.111, and the check "within 1.25 +/- 0.125" prints False.
- **fig4-pupil-effect-size (blocked: data_missing):** I agree. The reason is now the same in the header, the conclusion, both summaries, the README and the record.
- **ext3-5-arousal-covariates and ext7-1-arousal-mediation (blocked: data_missing):** I agree. Arousal cell 4 now lists `data/eye/`: 45 `<id>_area.npy` files and one yaml, with no ellipse fit.
- **The five L0-event claims (blocked: not_runnable):** I agree they are blocked. I accept not_runnable in place of my round-1 "other", since the record says the protocol uses that reason for software that cannot be installed. Section 3 has one open point on this.
- **ext8-1-no-low-level-relation (blocked: methods_underspecified):** I agree.

## 2. Sentences the printed outputs do not support

- **Main cell 21:** "falls below chance (about 0.04) when the windows are moved one presentation back". Cell 20 prints a mean of **0.085** at −34 s, which is chance (1/12 = 0.083), not below it. The point that the windows share a clock with the dF/F still holds. No conclusion depends on this.
- **Main cell 79:** "its FitSegmentModel.cpp uses std::numeric_limits without including <limits>, which a current compiler rejects". Cell 78 shows only that the header is missing. No compile attempt is printed.
- **Main cell 79** also says: "a build with those patches was made outside the notebook". The attempt record's notes on the L0 claims do not mention this build. They say only that running the detector "would mean patching the package".
- **Attempt record, last code_mismatch finding:** "AL alone in 50 and AM alone in 24, while L2/3 is the only significant layer in all of them". For the paper's stats.parquet, cell 46 prints only "28 of 108 sets agree (25.9%); looser rule 28". The 50, the 24 and the claim about L2/3 are not in any output.
- **Attempt record, fig3b notes, and main cell 40:** "the code's printed Figure 3 output 0.128". No such output is printed. What is printed is 0.128 from the code-SD variant on the paper's data (cell 39). That is consistent with the sentence but is not the same evidence.
- **Attempt record, fig4-locomotion notes and response:** "reached all required members after 210 s" and "arrives in about 210 s". Arousal cell 2 prints **217 s**.
- Every other "**Result:**" sentence, the three Summary sections, the README and the other notes match the printed outputs. That includes all counts, χ², p, d, r and range values, the run times, and the 2/3/1 males.

**Round-1 reasons in the record.** The record states my round-1 reasons faithfully and in my terms. That covers my outcomes, the "other" reason for the L0 claims, problems 1–3 and 5–8, and the requests in my section C. There is one small gap. My problem 3 also bore on the effect size in fig4, and the fig4-locomotion reason does not mention it, though the response does address it.

## 3. Round-1 points

**Resolved:**
- **Problem 2 (d(AM) = 0.268):** recorded as a code_mismatch finding, with a question to a reader.
- **Problem 3, the formula part:** the code's SD is now found. It reproduces effect_size.parquet to 4e-15 in all 44 sessions (cell 53). The extremes are now tested.
- **Problem 4 (trial timing):** disclosed, and the drift is now quantified against the sync files (arousal cell 6).
- **Problem 5 (session-link criterion written after the offset was found):** kept as a deviation.
- **Problem 6 (inconsistent blocked reason for fig4-pupil):** fixed.
- **Problem 8 (code's pupil reading as a variant):** not run, with a reason. It would not decide either claim.
- **All my section C requests:**
  - Fig. 7 likelihood-ratio and Tukey tests on the paper's data: they give χ²(4) = 32.115 and z of 3.229, 3.928, 5.249 and 3.396 (cell 26).
  - Sensitivity spectra: they match the paper's per-trial ND to 1e-14 for six sets, and r = 0.993–0.9999 over all 108 (cell 47).
  - The code's effect size: found (cell 53).
  - The Zenodo `data/eye/` listing (arousal cell 4).
  - The NWB group listing: none of the 57 files has a path naming events, eye, pupil or ellipse (cell 5).
  - The detector sources (cell 78).

**What remains that bears on a conclusion:**
1. **ext3-2-sensitivity (problem 1, unresolved).** The claims file's rule gives 28 of 108 on the paper's own outputs. So the not_reproduced outcome reflects the claims file's reading of "nearly all … specifically in L2/3 of AL and AM" more than the data. That reading may be a misread of the paper. A question to a reader is filed. The outcome should be read with that caveat.
2. **discussion-session-effect-sizes (problem 3, the criterion part).** The outcome depends on which pooled SD the criterion means:
   - With the Methods formula: partially reproduced.
   - With the code's SD: reproduced, at 0.584–1.194 with a pooled 0.343.

   The claims file is itself inconsistent here. Its opening comment says Cohen's d is from "analysis.py, cohens_d", and the criterion cites "pooled SD (code fig_4.ipynb)". Both point to the code's swapped-weight SD, while the Methods state the standard formula. I report this, not correct it. The attempt's choice of the Methods formula is defensible. The paper's printed AL (0.200) and PM (−0.122) values in Fig. 3 also match the code's SD.
3. **The L0 claims (problem 7, partly open).** The outcome is blocked either way. But cell 79 says a patched build of the detector was made outside the notebook, and the record does not say so. The compiler-rejection sentence is also not shown. If the patched detector runs, the reason for blocking (software that cannot be installed) is weaker than the record states. The record should either show the build or say what it found.
