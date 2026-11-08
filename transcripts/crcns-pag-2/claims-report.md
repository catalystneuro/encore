I wrote the claims file at `claims/crcns-pag-2/10.1038-s41598-020-74457-3.yaml` and nothing is committed. `tools/claims_check.py` passes every quote. It flags 3 p-values only because the text prints them as "3.00 × 10 –6" and "9.00 × 10 –6", a form it doesn't parse; I confirmed those against the text by reading.

**Text read:** the version of record, PMC7582948 (Europe PMC JATS XML, flattened). It has the full main text, Methods, all figure legends and the Discussion.
- **Supplement:** Figs. S1 to S6 and a Supplementary Information file are listed but their content isn't in the text, and no PDF was supplied. The main results and their statistics are stated in the main text, so I went ahead. The three claims that only Figs. S4 to S6 show are written from the Results sentences that cite them, with no expected values.
- **Code:** none was read. The only link is https://mcdannaldlab.org/resources (behavioral programs only), and it returned a 404 on 2026-11-06, so no repository or commit is recorded.

**Counts:** 20 claims, all 20 with quotes and none inferred. 17 have statistics (49 statistical values), 4 have expected values, and all 20 have criteria. Some claims need data the dataset's description doesn't list (body weights, the eight pre-surgery sessions); they're kept as the paper's findings.

**Settled from the paper's own numbers:**
- **Fig. 2D chi-square:** χ² = 5.68 comes out only without the Yates correction.
- **Fisher r-to-z p-values:** they are one-tailed for Z = 3.80, 3.05, 1.04 and 1.43, and two-tailed for Z = 0.60. The criteria show both where it matters.

**Details left open, with the readings named:**
- **Selection epochs:** the Methods give first 1 s and last 5 s for both cell types; the Results give first 5 s and last 5 s for inhibited cells. A third reading uses all three epochs.
- **Trial-wise normalized firing for the regression:** (a) subtract the trial type's 2 s baseline and use the neuron's normalization mean and SD; (b) subtract the trial's own 2 s baseline instead; (c) Z score each trial's binned firing over all its trials and bins.
- **Suppression ratio of 0/0** (no pokes in baseline and cue): set to 0, or drop the trial.
- **Beta for a multi-second window:** the mean of the 1 s interval betas, or one regression on the window's averaged firing.
- **Baseline window:**
  - Fig. 2B nose poke rate: the 20 s before the cue, or the dataset's own baseline poke field.
  - Fig. 2E,F firing rate: 10 s or 2 s before the cue.
- **Fig. 2C rat means:** the mean of session means, or all trials pooled.
- **Bonferroni divisor for Fig. 4F's within-group test:** 2 or 3.
- **Degrees of freedom:** several tests report fewer than the neuron counts imply (t 66 and F 1,65 for 81 cells; F 1,78; F 110,8360; F 2,346 for 354 cells). The paper doesn't say which neurons were dropped, so a mismatch counts as a deviation, not a failure of the claim.
- **ANOVA software and sphericity correction:** not named. The criteria assume uncorrected repeated-measures ANOVA.

**Missing from the paper that claims needed:**
- The supplement's content, so the statistics behind the S4 to S6 claims are unknown.
- The lab's analysis code, which is unreachable, and no neural analysis code is linked at all.
