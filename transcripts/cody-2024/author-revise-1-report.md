The round-1 revision is finished. The entry passes `python tools/entry.py all` (0 errors, notebook runs in 160 s), and the handover package is rebuilt. Nothing is committed.

**Main fix (verifier point 2).** The pupil cleaning now also drops any trial whose raw trace jumps by more than a factor of 2 between consecutive tracked frames. That removes 118 of 2113 trials from 15 mice. It changes the animal maximum of only the two mice the verifier flagged: AA0319 goes from 332.7 to 78.3 and AA0334 from 162.1 to 70.9. No trial maximum is now more than 3.1 times its animal's median. Like the other cleaning steps, this is an assumption, stated in the helper module and the record.

**Outcome changes:**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig4f-ko-zx1-slope | blocked | not reproduced | The verifier was right: its criterion fails under all 4 readings on its own. |
| fig6a-baseline-pd-drift | not reproduced | partially reproduced | Follows the verifier: both drifts are present; only the overlap of the intervals fails. |
| fig4c-wt-contrast-zx1-effects | not reproduced | blocked (methods underspecified) | With the new cleaning, reference coding gives all 5 terms significant (interaction p = 3e-5), sum coding gives 4 and 3. The criterion blocks when readings disagree. |
| fig4-wt-posthoc | not reproduced | partially reproduced | Three of four parts hold; ZX1 also raises LOW at p = 0.0496. |
| fig6c-no-baseline-evoked-correlation | reproduced | blocked (methods underspecified) | No reading the claims file lists matches the count, and they disagree (group D, all trials: p = 0.00025). |
| methods-baseline-evoked-correlation | partially reproduced | blocked (methods underspecified) | No reading matches both counts any more. |

**Disagreement kept:** fig6b-acsf-contrast-effect stays partially reproduced; the verifier would give not reproduced. With the new cleaning, the contrast effect on the intercept holds in every reading, including within ACSF (p = 2.6e-5, where it was p = 0.37 before). The slope effect fails in every reading. The disagreement is recorded in the attempt record.

**Several outcomes depend on the cleaning:**
- Under the first round's cleaning, fig4c and fig4-wt-posthoc go back to not reproduced.
- Under the paper's single cleaning pass, the fig6d genotype effect is not significant (p = 0.20) and the fig1i interaction p is 0.17.

All of this is printed in a new section at the end of the notebook.

**Added or corrected, by verifier point:**
- **Point 2 (output asked for):** a table of each animal's five largest cleaned trial maxima, each with its trial's median.
- **Point 3:** the key number behind each pupil claim is recomputed under five versions of the data: the new cleaning, the first round's cleaning, the single pass, the first round's cleaning without AA0319 and AA0334, and group A without its ZnT3-WT mouse AA0335.
- **Point 4:** the growth curve fits now try several optimizers and keep the best converged fit, and print the optimizer, convergence, subject variance and boundary status. The lbfgs-only fits had stopped at broken points, for example the fig6d genotype intercept of -52.5 with p = 1, now p = 0.39.
- **Points 5 to 7:**
  - Without AA0335, group A's Fig. 2b test becomes significant (p = 0.028). The Fig. 3 baseline term is then not significant for trials below 50% (p = 0.087). Neither changes an outcome; both are in the notes.
  - Group B restricted to its C57BL6/J mice gives the same Fig. 2e result.
  - Fig. 3 now runs all four cell-inclusion readings, 16 fits in all.
- **Point 8:** new tables of DRC trials by sound delay, block order and contrast. The 32 ZX1 trials of AA0327 start the sound 10 s after the first frame, and the pupil dilates after that onset. FRA mapping trials are in 7 of 30 files, not 5 as the first round said; this is corrected.
- **Point 9:** the dead loop is removed, and readings added beyond the claims file's list are marked.

The `verifications` block records all 24 claims with the verifier's reasons in its own words and my responses. The README, the summary, the helper's docstrings and the findings are updated to match the new numbers.

**Not done:**
- No question was added to `questions/001256.yaml`. Point 10 says the discussion claim's criterion is weak, which is not a misreading of the paper, so it does not qualify. The verifier reported no misreading.
- No lmer/Satterthwaite comparison was run: no R in the locked environment. The tests remain Wald z tests, as stated before.
