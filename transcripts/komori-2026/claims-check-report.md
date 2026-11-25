**Checker:** `claims/komori-2026.yaml: 24 claims, 22 quotes, 31 statistical values, 0 problems`. Before my edits it read 23 claims, 21 quotes, 28 statistical values, 0 problems.

**Changes, by claim**
- **Opening comment, R2:** the file said the paper ran its own processing pipeline on the raw resting frames. The Methods don't say that, so it is now marked as implied but not stated.
- **rest-needs-0-1-hz:** the statement now adds that the 0.1 Hz AUC did not differ significantly from any other cutoff (Supplementary Figure 5E, all n.s.). The file already recorded that test, but the statement left it out.
- **rest-ic-count-and-window:** the Supplementary Figure 5F legend says "initial number of ICs". It's unclear whether that means the ICs kept or the count before ICs were removed to bring VIF under 10. Both readings are now named and run.
- **rest-vif-below-10:** the statement claims the 7, 13 and 15 IC comparisons, but the criterion only reported them. They are now judged on the paper's test (Mann-Whitney U with Holm, Supplementary Figure 6G). It counts as partially reproduced when only the 10-IC maximum of 9.0 holds.
- **rest-shap-medial-anterior-first:** I removed the statistics entry. The paper reports no test for IC7 preceding IC6 and IC4. The test from the Supplementary Figure 9 legend stays in the criterion as a method.
- **fig1-roi-vif-vs-ica:** the 7.8 is the maximum VIF with 10 ICs (Supplementary Figure 6A), not with 20 to 30 ICs. I corrected that and added the Supplementary Figure 6B result: 10 ICs give a lower maximum VIF than 12 or 14 ICs, p < 0.05 with Holm.
- **fig1-somato-exclusion-window:** the expected quantities now say they are validation AUC over the 5 models, reported as median and standard error per the Figure 1F legend.
- **fig1-somato-selection-rates:** added expected values for 34.4%, 48.2% and 34.7%, which the statement reports but the file left out.
- **fig4-shap-somato-ic5:** added the reported statistics: significant by uncorrected paired t-test, not significant after Holm correction.
- **fig4-shap-visual-ics:** extended the quote to cover the visual contextual IC4 result, which the statement includes.
- **supp10-top-shap-ics:** added the expected percentages (43.1, 19.1, 37.1, 23.6). Also added the result that visual models without the 0.0 s frame don't differ from null after Holm correction.
- **New claim, supp2-session-selection-needed:** decoding fails unless sessions with early or absent dilation are excluded (Supplementary Figure 2E and the Discussion). This underlies the abstract's main result and had no claim. Like the file's other own-recording claims, it can't be tested on DANDI:001425.

**Still open** (recorded under `checks`)
- **Resting-state methods:** the paper doesn't fix several details: which mice and sessions, preprocessing, pupil measure, how samples and epochs are built, the hand-picked ICs, fold unit, shuffle scope, and the SHAP background. The criteria name the possible readings (R1 to R10).
- **Values read from bars:** the resting AUC, loss and accuracy values come from Supplementary Figure 5 bar heights, not printed numbers. The 10% tolerances rest on that reading.
- **2 Hz resting model:** the paper reports no test of it against null. The criterion uses the null-model paired t-test from the Supplementary Figure 5D legend.

**Ready:** yes. The last check is marked `ready: true`. Nothing is committed.
