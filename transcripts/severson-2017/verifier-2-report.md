**1. Outcomes**

The claims file has 28 claims. The attempt record gives 28 outcomes: 14 reproduced, 3 partially reproduced and 11 blocked. I agree with all 28.

- **fig7d-cut-emg:** In round 1 I gave the block as metadata_insufficient. The record keeps data_missing and gives the missing cut condition in its notes. Both blockers apply, so I accept this.
- **fig5e-phase-span:** I agree with partially reproduced. The criterion fixes the estimator (highest of 30 bins), which gives p = 0.047 (cell 50). The record discloses that the circular-mean variant gives p = 0.062.
- **fig3d-gam-best-pair:** I agree with partially reproduced. M0+M0' ranks 2nd in all three variants (cell 40).

**2. Sentence check against printed outputs**

Every "**Result:" cell (19, 23, 26, 29, 30, 32, 35, 41–43, 46, 49, 51, 53, 56, 59, 62, 65, 68, 71) matches the printed numbers. So do the README and nearly all the record notes and findings. The exceptions:

- **Record, verifications, fig3d-gam-full response:** "The held-out variant … gives pair values within 0.003 of the in-sample ones." Cell 40 prints only the top five pairs for each variant. The statement is supported for those five (differences 0.002–0.003) and not shown for the other 40 pairs. The held-out r of the full model was not computed.
- **Record, fig5e-phase-span notes:** "At the preferred phase the whisker is retracting for 11 of 15, which fits the paper's remark of a slight abundance in retraction." Cell 50 gives 11 of 15 (73%), which is not "slight". The record's own finding says the stored phase is negated. If the paper's Figure 7G used the stored phase under the usual convention, these 11 would be labelled protraction. "Fits" is not established. This does not affect an outcome.
- **Record, fig5e notes:** "with the highest of 20 or 60 bins p = 0.023 and 0.046". In cell 50 these two variants also use a different frame set (the outlier-free frames kept for figs6). The note does not say so.
- **Record, fig7d-cut-emg and figs4-intrinsic-protractor notes:** "hold the whisker video series". Cell 61 shows tracked kinematic series (position, velocity, Mi, dMi, and so on), not video.
- **Summary, cell 73:** "the values reproduce the paper's frame counts, rates and model performance closely". This is broadly true. Against it: the non-preferred rate is 16% above the paper's (cell 48), sigma-kappa is 28% above (cell 70), and direction selectivity reaches 65% against the criterion's 80% (cell 34).
- **Cell 11 (data check, not a conclusion):** the velocity column is labelled "(degrees/s)", but the notebook's own ratio check says the stored values are per millisecond.
- **Record, inputs:** "The transcription was checked against the supplement (mmc1.pdf) … all 60 rows agree". No notebook output shows this check. I tried again to get the supplement and could not: PMC returns a reCAPTCHA page and Europe PMC reports the article is not open access. The manuscript text is saved at `paper/PMC5528144.txt`.

**My round-1 reasons in the record:** they are stated faithfully. All ten B points and all five "not checked" items appear under the right claims. The "reviewed" summary correctly says I listed 10 problems, 3 affecting a conclusion, and agreed on all 28. One gap: the reasons cite round-1 cell numbers ("Cell 36", "Cell 34", "Cell 37"), which no longer match this notebook (now cells 48, 45, 50). The record should say they refer to the round-1 notebook.

**3. Round-1 points**

Resolved:

- **B1:** cells 28 and 48 now print the claim's tolerance check and label the 10% check as not the criterion.
- **B2:** estimator variants were run and disclosed. The outcome is kept per the criterion.
- **B3:** the 45-pair ranking was rerun with lambda 100 and with held-out frames. The rank is 2 in both and the same five pairs lead.
- **B4:** position by phase is finite and peaks next to 0 in 60 of 60 files. Sine −0.9999 and cosine +0.9999 show the stored phase is negated, not shifted by pi.
- **B5:** `fit_visco` now flags bounds on the fitted scale (merkel.py:508–520). It reports 7 of 25 fits at a bound, and the parameter values are no longer interpreted.
- **B8:** recorded as a finding.
- **B10:** cell 61 shows what the archive holds.
- **B6, B7, B9:** acknowledged; none needed a change.
- **"Not checked" items:** the EMG and progressive file contents are now printed (cell 61), and the fig7f lower bound was computed (cell 64; it is uninformative).

Remaining that bears on a conclusion:

- **The Table S1 transcription has still not been checked by a verifier.** The record says the author checked it, but I could not get the supplement and the notebook does not show the check. The type, Merkel and viscoelastic-fit columns drive merkel-minutes, fig3a-direction-selective and fig4c-viscoelastic. The class column drives fig2c-wt-star's agreement count.

A minor residual, unlikely to change an outcome: the EMG files 7A, 8A and 9A hold unexplained `Mi` and `dMi` series (cell 61). Their values were never compared with positive velocity. Doing so would fully rule out that one of them is the intrinsic protractor EMG, which is the basis for blocking figs4-intrinsic-protractor.
