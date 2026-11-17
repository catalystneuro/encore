**Verifier report, round 2: timme-2016-01**

Counts come from the claims file (14 claims) and the attempt record (14 outcomes).

**1. Outcomes**

I agree with all 14 stated outcomes. Every outcome marked `assumed: true` states its assumptions in the deviations, and each assumption is reasonable.

| Claim | Record | Agree | Assumption |
|---|---|---|---|
| data-recordings | reproduced | yes | none needed |
| fig4ac-te-lognormal | partially_reproduced | yes | Tie rule and bins t-2, t-3: stated and reasonable. The criterion has no partial grade. Partial is justified: the spread passes (353 to 1160×), and three of eight averaged R² values fall just under 0.9 (0.882, 0.895, 0.899; cell 18). With bins t-1, t-2 the claim would be reproduced; under the strict rule it would not. Both are stated. |
| fig4bd-heavy-tailed-degree | reproduced | yes | Holds under every variant (cell 22), so it needs no assumption. |
| fig4bd-out-tail-longer | reproduced | yes | Tie rule: stated. It fails only under strict (f) (cell 26). |
| fig5a-in-degree-uncorrelated | partially_reproduced | yes | (s), Pearson and the tie rule are all stated. The result is borderline: binomial p = 0.043. Under (s, Spearman) and under bins t-1, t-2 the grade would be reproduced (cell 29). The record says so. |
| fig5b-out-degree-positive | reproduced | yes | Stated. It holds under every reading of the main analysis. |
| fig5ab-correlations-beyond-null | partially_reproduced | yes, with a caveat | Stated. The criterion defines only "reproduced", and its letter is not met. The in-degree panel fails under all four main readings (63 to 88%). The out-degree panel passes under three of four (cell 34). "Partial, one panel of two" is a judgment the criterion does not grade. I accept it. |
| fig5cd-pooled-trends | not_reproduced | yes | Fails under every variant (cell 37). |
| fig6-information-gain-not-rising | reproduced | yes | The normalized gain is a stated, reasonable reading (the paper normalizes the PID terms). In bits the grade is partial under (f). With bits and bins t-1, t-2 it would be not reproduced. Both are stated. |
| table1-pid-examples | reproduced | yes | none needed |
| fig7b-connectivity-patterns | reproduced | yes | none needed |
| fig7c-degree-modified-rule-matches | partially_reproduced | yes | Stated. The whole criterion holds only under (s, Spearman) (cell 47). |
| fig7d-degree-rule-highest-conditioned-mi | not_reproduced | yes | none needed |
| figs1-larger-model | not_reproduced | yes | Fails under every reading and both α/β choices (cell 53). |

**Places where the claims file misreads the paper (reported, not corrected):**
- **M-PID redundancy.** The claims file takes the minimum over sources within each (i_F, i_P), weighted by p(i_F, i_P). Eq 8 of the version of record, as transcribed in cell 45, takes the minimum once per i_F, weighted by p(i_F). The claims file was written without the equations. The notebook follows the claims file and runs Eq 8 as a variant; no verdict changes (cells 29, 34, 37, 43, 47).
- **M-SIG "larger".** This one is not a misreading: the paper's text does say "larger than ... (i.e. p < 0.001)". How ties are counted is open in the paper itself.

**2. Text against the printed outputs**

Every "**Result:**" sentence, the Summary, the README and the record's notes match the outputs, except for these:
- **README:** "It takes about 52 minutes on four cores". Cell 57 prints "Notebook ran in 63.3 min".
- **Cell 45:** "the mean and standard deviation of the 50 per-recording correlations (25 recordings, two time scales) of the main analysis, reading (s), Pearson". Under (s) there are 49, since DataSet5 has none at 1.6 to 6.4 ms (cell 29, n = 49).
- **Cell 14 and cell 16** cite [44]: "effective N of 241 +- 103 and effective k of 22 +- 30", and "Degree rises with firing rate ... as [44] reports for its networks". Neither can be checked against any output or my materials. The notebook's own figures (245/277, 8.8/19.5, ρ 0.75/0.81) do match cells 10 and 13.

The record states my round-1 reasons in my own words for all 14 claims, and the "12 of 14 agree" count is correct (fig4ac and fig4bd-out-tail-longer disagreed). One small compression: for fig7d, "At 50,000 runs the ranking holds" leaves out that I reran only a few models.

**3. Round-1 points**

Resolved:
- **1, the tie rule.** Ties now count as exceeding, the strict rule is run as a variant, and the size of the problem is measured: zero-exceedance pairs and pairs with no movable spike (cell 10), false-positive rate on shifted trains (cell 12), degree against firing rate (cell 13). What is left of it is listed below.
- **2, past bins.** Both readings are run, and the choice is stated as an assumption.
- **3, PID form.** The claims-file form is now the main analysis and Eq 8 the variant.
- **4, sub-networks.** Short draws are redrawn, reading (b) is run, and edge counts are printed (cell 15).
- **5, undefined model correlations.** The NaN-as-0 check is added; no verdict changes.
- **6, `deg_beats`.** It now checks direction.
- **7, fig6.** Reading (s) is added, with 100 combinations per n. Receivers are still sampled (30), which is stated.
- **8, figs1.** The verdict is printed for every reading.
- **9, model MI bias.** The plug-in bias is printed.
- **My round-1 section C requests:** the equations, [44]'s Table 1 row (in the `hdn.py` docstring), edge counts, and the approximation check at 3.5 ms are now all present.

Remaining points that bear on a conclusion:
- **The tie-counting test is still too liberal.**
  - Pooled false-positive rate is 0.32% against the nominal 0.1%, and up to 1.28% for DataSet11 at 3.5 to 14 ms (cell 12).
  - Multiplying each rate by the number of pairs gives the connections expected by chance in the five tested recordings: about 8 to 30% of the significant connections. For example, DataSet16 at 3.5 to 14 ms expects about 1885 of its 6364 (0.00535 × 352242 pairs); DataSet1 at 3.5 to 14 ms about 96 of 428.
  - The record gives the rate but not this share. It affects fig4bd, fig5, fig5ab and fig7c's real-data reference; the direction of the effect is unknown.
- **The normal approximation matches the full jitter less well under the tie rule.** It shares 83 to 89% of the connections either method finds, and finds 0.1 to 8.2% more (cell 9). This is stated, but it adds to the excess above.
- **Several outcomes hinge on which reading is taken:**
  - fig5a sits at p = 0.043, and the alternatives (Spearman, or bins t-1, t-2) give reproduced.
  - fig4ac turns on three R² values between 0.882 and 0.899.
  - fig7c holds in full only under (s, Spearman).
  - All of this is disclosed. These outcomes rest on the stated readings and are not robust results.
- **fig5ab's partial grade** is not defined by the criterion (see section 1).
- **Degree mostly tracks firing rate** under the tie rule (median Spearman 0.75 and 0.81, cell 13). This is consistent with the test's power rising with rate. It changes no verdict, but it qualifies what "high-degree" means in fig4bd and fig5b.
