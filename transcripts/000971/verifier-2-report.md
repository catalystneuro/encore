## Round 2 verifier report: Seiler et al. (2022), dandiset 000971 v0.261013.1707

Counts are taken from the claims file (38 claims) and from the attempt record's outcomes: 18 reproduced, 9 partially reproduced, 6 not reproduced, 5 blocked. Since round 1, two outcomes have changed: fig6-nphr-learning-dropout is now blocked, as I recommended, and fig2n-rewards-per-session went from reproduced to partially reproduced. I did not re-download the paper. The checks below use the claims file, the notebook outputs and my round-1 reading.

### 1. Outcomes

I agree with all 38 stated outcomes. Three need a note:

- **fig2n-rewards-per-session (partially_reproduced).** I accept this outcome, but it sits on the threshold, and which result you get depends on a rule chosen after round 1.
  - The claims file defines sessions as the files described as RI60 training. Under that definition the 170 s file of 140.306 is included and Tukey PS vs DPR gives p = 0.048 (cell 53), which would be reproduced.
  - Leaving out that one file gives p = 0.059. Keeping one file per mouse-day gives p = 0.044.
  - The stated reason for leaving it out is "a false start followed by a full session the same day". That reason applies just as well to files the analysis keeps: 271.396 (2 rewards, 720 s), 88.239 (1 reward on two days), 92.246 (4 rewards), 348.393 and 115.273 (3 rewards). Removing all of those is what the one-file-per-mouse-day variant does, and it gives 0.044.
  - Partially reproduced is the conservative choice and every variant is reported, so I accept it. The claim should still be read as borderline.
- **fig6-nphr-learning-dropout (blocked).** I agree. Cell 105 shows the shortfall against Figure 6F is 3, 2 and 0 mice, the "Did Not Learn" flag also marks an EYFP mouse, and no file says which group a mouse was in.
- **fig5f and fig7f (not_reproduced).** I agree, because the criterion fixed the pooled least-squares fit before the analysis. In both, a mixed model with a per-mouse slope reverses the result (cells 90 and 117).

### 2. Sentences the numbers do not support

**Result conclusions, Summary, README and notes**

- **Cell 73:** "The dropout step leaves out more than 1% of samples in only one DMS session of the 51 behind these pairs (1.61%)."
  - The count is correct, but the sentence suggests the step has little effect. Cell 72's table shows it changes DMS scores a lot in sessions where it leaves out 1.61% or less: 88.239 goes from 0.09 to 1.92, 048.392 from 0.02 to 1.81, 346.394 from 0.00 to 1.10, and 92.246 from 0.04 to 0.30.
  - The fig3g response in the attempt record ("one DMS session above 1%") carries the same implication.
- **Summary (cell 133) and the fig2c and fig2n deviations:** "Training files with no nosepoke and no reward are left out."
  - The 140.306 file holds `left_nose_poke_times` (30 events in the file, cell 20). It has no active nosepoke, which is what cell 21 says correctly.
- **Cell 60, and the figs1i notes:** "With the 20 RR20 files that hold port entries only counted as sessions of 0 rewards…"
  - That variant also keeps the RI60 false start (RI60 mean 41.89 instead of 41.97, cell 59). This is minor and does not change the result.
- **Cell 91, and the fig5f notes:** "A mixed model … agrees with the per-mouse slopes."
  - The fit converged only after a retry with lbfgs and warns that "the MLE may be on the boundary" (cell 90).
- **Cell 118, and the fig7f notes:** the mixed-model p values (0.43 to 0.96) are reported with no caveat.
  - Cell 117 prints repeated "Random effects covariance is singular" warnings, so those p values are weak evidence that the result rests on the pooled fit.

Every other "**Result:" sentence, the Summary, the README and the outcome notes match the printed outputs. That includes the counts (33/39, 42/47, 6/9 mice), the p values, the means, the 2336/2337 and 10892/10916 event counts, and the runtime of about 25 minutes (1407 s).

**My round-1 reasons in the attempt record**

These are stated accurately and in my wording, each with its B point. Two small things:

- The fig6 reason leaves out my note that applying the criterion literally would have given not_reproduced. That point no longer matters now that the claim is blocked.
- The fig2n entry correctly records my round-1 outcome as reproduced.

### 3. Round-1 points

**Resolved (fixed in the notebook, or disclosed in the conclusion and notes):**

- B1: dropout step dependence stated, with variants.
- B2: Bonferroni p = 0.13 and the no-dropout-step readings added.
- B3: mixed-model variant added.
- B4: fig6 changed to blocked.
- B5: variance ratio of 251 reported.
- B6: table of the empty files and variants added.
- B7: per-stage mouse counts against Figure 3E given.
- B8: per-mouse wait table added.
- B9: counts said to match by construction.
- B10: events kept now printed.
- B11: 95% intervals of r added.
- B12: RI60 part of fig3e shown.
- C: Zenodo blocks printed, fig3g without the dropout step shown, per-session dropout fractions shown.

**Still open, and bearing on a conclusion:**

- **fig4g (and fig3f, fig3g).** The outcome still depends on the dropout step, which was chosen after seeing the data and is in neither the Methods nor the authors' code. This is now disclosed. In the sessions with large dropouts the authors' processing gives scores near 0 (cell 72), which supports the step but cannot prove it is right.
- **fig2n.** The outcome changes with the session-exclusion rule (p = 0.048, 0.059 or 0.044). The rule used is the only one of the three above 0.05 and is narrower than the false-start reason given for it.
- **fig5f and fig7f.** Both outcomes rest on a pooled fit with no mouse term. The mixed models that reverse them have convergence or singularity warnings that the conclusions do not mention.
- **Not resolved: Figure S1 to S7 legends.** figs1i, figs2b, figs5f and figs3ab are still judged on the main text alone.
