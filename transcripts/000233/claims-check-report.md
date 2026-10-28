The claims file for DANDI:000233 is ready for an attempt after my corrections. Nothing was committed or pushed.

**Checker result:** before my edits it read `34 claims, 34 quotes, 6 statistical values, 0 problems`. After them it reads `35 claims, 35 quotes, 6 statistical values, 0 problems`.

**Changes, by claim**
- **Opening comment:** the Fig. 3f legend says "100 iterations", not 100 per rat. Reworded.
- **fig2h-phase-reset:** the test could not work. It asked for a Spearman correlation across single peaks of a measure (circular s.d.) that only exists over groups of peaks, and the 4 quartiles it grouped them into are too few for p < 0.05. It now uses 10 deciles of peak rate. The baseline, the peak definition and the pooling across rats are now marked as choices, with two baselines named as readings.
- **edfig5-cross-frequency-coupling:** the t-test pairing and the Rayleigh setup are now marked as choices.
- **edfig1-glucose-rhythm:** the legend says "linear best fit", not a 1/f fit. Statement fixed, and log-log axes marked as a standard choice.
- **edfig2-refractory-period:** measuring intervals between ripple peaks is now marked as a choice. The legend doesn't say which time point is used.
- **Source corrections:** four claims cited the wrong Supplementary Discussion paragraph:
  - edfig3e: 5 → 6
  - edfig6: 3 → 4
  - edfig6d: 4 → 5
  - fig4c-medial-septum: 6 → 7
- **edfig3e-ca1-firing-decrease:** the test is now marked as a choice.
- **edfig4-fasting-fed and edfig4-nrem-wake:** each statement includes transitions (fasting to fed, wake to NREM and back) that the criterion never judged. I added a test for each, labelled as made here.
- **edfig6d-pairwise-predictors:** the +10-min offset was credited to the Methods, which give no offset for these models. Now OPEN, with +10 and 0 min as readings.
- **edfig6ef-latent-variables:** the criterion allowed a component to beat SPW-R rate in one rat. The paper allows none and says PC1 is similar in all rats, so the criterion now follows the legends.
- **fig3d-induced-ripples-lower-glucose:** the shuffle test is marked as a choice. The per-rat P values in Extended Data Fig. 7c-d are now shown.
- **fig3-induced-effect-size:** which natural ripples give the 0.094 nA is not stated. The optogenetic rats' own natural ripples are added as a reading.
- **fig3ef-stimulation-dose-response:** added "rat counts when R < 0 with P < 0.05" (Extended Data Fig. 7d) as a reading of the 7-of-8 count. Added a t-test of the per-rat R values as a reading of P < 0.01.
- **fig3f-stimulation-vs-shuffle:** n now says "100 iterations", as in the legend.
- **edfig7-ppc-stimulation-no-effect:** the PPC shuffle bound is marked as a choice.
- **fig4-cno-controls-no-change:** the 2-h window is cited from the Results and the Fig. 4b legend, not the Methods. Removed a reason given for the test's units ("Extended Data Fig. 10d compares days"), which the paper doesn't support.
- **fig4-ls-dreadd-chance-level (new):** the abstract's finding that the correlation drops to chance levels had no claim. The test is a choice, since the paper gives none.
- **fig4e-dreadd-time-course:** the legend doesn't say which groups are compared. Both comparisons from Extended Data Fig. 10d are now readings, and the 5-min step is marked as a choice.
- **edfig10-expression-correlates-effect:** the effect measure is now OPEN. Legend 10e says "the effect of CNO", but panels 10f-g plot the correlation after CNO.

**Still open** (also recorded in the checks entry)
- The buzcode commit and the ripple detector defaults described in the opening comment were not checked.
- The Results paragraph numbers can't be checked: the text has no paragraph breaks and no PDF of the main article was supplied.
- Extended Data Fig. 5a-c has no claim, because no sentence states its result.
- The edfig10 claim depends on scores printed only in the figure table, which the file notes no reader has seen.

**Ready:** `true`.
