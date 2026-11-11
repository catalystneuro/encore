I wrote `claims/wright-2019.yaml` and did not commit it. It holds 38 claims, every one with a quote. The quote checker passes every quote and the schema. It flags 3 of the 50 p-values as "not found". The paper prints those three with trailing zeros: p = 9.70×10⁻⁵ and 8.90×10⁻⁵ for the Onset tests (fig2b, fig5a) and p = 3.20×10⁻³ for the Ramping test (fig5f). I read all three in the text and they are correct; the checker just doesn't recognise that printed form, so it still exits non-zero.

**Text read.** The version of record (PMC6435320, Europe PMC full text): main text, Methods, all figure legends and all figure-supplement legends, plus the Methods' example regression table. The paper has no other supplement. No PDF was supplied, so numbers printed only inside figures could not be read: the R² and sign-test p-values of Fig 4, the F values of Fig 5–supplement 1, and the values of the tuning curves. Those claims are judged on the tests the legends name.

**Code.** The paper's only code link is the lab website (http://mcdannaldlab.org/resources). It returns 404, and the one archived copy, from 2020, has no files. So no code was read, and every method in the file comes from the paper's text. The data set's description mentions sample MATLAB scripts, but those are data-set files, so I did not open them.

**Contents.**
- **Statistics:** 50 values are recorded, mostly p-values with their F, t and χ² statistics.
- **Expected values:** 19 claims have them. They are suppression ratios, neuron and cluster counts, departure times, tuning-curve peaks, mean Ramping betas and correlation counts. Tolerances are the reported SEM for the betas and 10% elsewhere. The exceptions, each with its reason in the file, are 0.05 for the safety ratio and 0 for the tuning peaks and exact counts.
- **Criteria:** all 38 claims have one. Five are claims of absence, judged on the paper's own test.

**Details the paper leaves open, and the readings named:**
1. **Nose-poke baseline window for the suppression ratio:** the 2 s before cue onset (the firing baseline), or the 10 s before onset (the cue's length).
2. **A ratio with no pokes at all (0/0):** set to 0, or left out.
3. **A session's ratio:** the mean of per-trial ratios, or the ratio of the session's mean rates.
4. **Baseline for per-trial interval firing:** the trial's own 2 s baseline, or the trial type's mean baseline.
5. **K-means:** baseline rate taken from the pre-cue windows or from the whole session, and features raw or Z-scored. Initialisation is a standard choice.
6. **Sign tests:** two-sided, since the paper doesn't say.
7. **Fig 4 shuffle:** cue values permuted within each neuron, or across neurons. "Above chance" means above the 95th percentile, or above the box plot's upper whisker.
8. **Fig 2E sliding window:** firing taken as the mean of the 100 ms Z-scored bins, or re-Z-scored per window. The reported time is the window's start or its end.
9. **Fig 2–supplement 2 (nose-poke cessation):** where the ITI starts and ends, and whether firing is raw or minus a baseline.
10. **Fig 6E/F χ² test:** Pearson χ² × (N−1)/N, plain Pearson, or Yates-corrected. The first reproduces the reported 8.08 and 4.22 from the reported counts.
11. **Smaller ones:** what counts as "weaker" in Fig 5–supplement 1, the rule for "not safety trials" in Fig 2–supplement 1, and that the ANOVAs are uncorrected repeated-measures designs, as the reported degrees of freedom imply.

**Inconsistencies within the paper, noted in the file:**
- The Onset danger vs uncertainty test is p = 9.70×10⁻⁵ in the Results but 9.70×10⁻⁴ in the Fig 2B legend; t(28) = 4.54 fits the Results.
- A Ramping first-interval test is p = 0.81 in the Results and 0.82 in the legend.
- The mean danger suppression ratio is 0.80 in the Results and 0.83 in the Fig 2–supplement 2 legend.

**Missing.** No claim was blocked for missing text. Only the linked code and the in-figure numbers were unavailable.
