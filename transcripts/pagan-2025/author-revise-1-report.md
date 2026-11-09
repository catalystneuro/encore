I've addressed every point in the round-1 report. No outcome changed, and the entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passed in 419 s). The conclusions match the new numbers. Nothing is committed.

**Outcomes:** all 23 stay as they were, and the verifier agreed with every one. Round 1 is recorded under `verifications` in `attempts/001550-pagan-2025-01.yaml`, with the verifier's reasons in its own words and my response for each claim.

**What changed in the results**
- **choice-axes-parallel (point 1):** the verifier was right that I had ported only the first angle in `ExtDataFigure5ag.m`; the code overwrites it and plots a second one. I ported that second angle and made it the main value: 1.12 to 8.00 degrees per rat, mean 4.73, against the paper's 1.6. That matches the verifier's own recomputation. It is still outside the tolerance, so the outcome stays not reproduced. The old full-space angle (mean 40.3) is kept as a variant. I also corrected the claims file's wrong description of the code, with a note that the correction came after this round. The measured value and the code-mismatch finding now say 4.7 degrees.
- **fig5d-behaviour-neural (point 2):** I kept it reproduced but recorded that it is fragile. If P049 and P059 come from the code's looser selection, r is -0.834; the code's selection with the cross-validated penalty gives -0.830. Both fall outside the tolerance (-0.803 to -0.657) on the more negative side. Leaving out one rat at a time gives -0.655 to -0.895, inside the tolerance for 4 of 7. All five 14-point correlations are negative with p < 0.01.
- **neural-link (point 3):** I added P100's 13 unsearched TaskSwitch4repeat sessions and every other TaskSwitch protocol. Cells matched with gaps rise to 0.958, but they still come from only 115 sessions against 199. I added a per-rat table with trial counts and dates. The 146 cells still unmatched overlap partly with sessions that are already matched, so they do not point to missing sessions.
- **ed4-bilateral-fof-impairs (point 4):** the laser was connected on every trial that has an epoch. With laser-connected trials only, the result is unchanged, and P124 is still not impaired.

**Outputs added for the remaining points**
- **session-link (point 5):** of the 1,553 sessions whose relative weights differ from the paper's, 861 agree once capped at 1 (the paper's table caps them) and 632 have a missing value. I extended the per-trial check from the 20-session sample to every matched session. 627 have an empty per-trial record in the paper's tables. In the other 14,650, all 7,447,692 valid trials agree, and 0.99996 of the pulse bins agree.
- **ed1e-switch-four-trials (point 7):** the 30-trial minimum drops nothing (every fit has at least 103 trials). I added per-rat values for positions 1 to 5 and a bootstrap over rats. The position 4 reading is thin: 0.874 to 0.946, and 0.68 of resamples reach 0.9. The position 5 reading, which the criterion also allows, is firm.
- **subjects (point 8):** the dates of birth put 25 rats at 1.6 to 2.7 months at their first session, so the young ages look real. P189's date of birth (2018-02-21) looks a year early: it puts the rat at 14.1 months on its first day, which is also P187's first day, and P187 was born 2019-02-21. This is added to the age finding.
- **Smaller fixes (points 6 and 9):** removed the unused variable, showed the trial readings with the 13 unreadable sessions included, and explained in the notebook why the cross-validation folds are random over trials.

**Not done**
- I did not switch the cross-validation folds to whole sessions, because the claims file fixed the folds before the analysis; the fixed-penalty variant already shows the effect.
- I kept `not_runnable` as the block reason for fig1f, fig3a and fig5c, where the verifier wrote "other". The outcome is blocked either way, and the reason is recorded.
- No paper text was downloaded.
