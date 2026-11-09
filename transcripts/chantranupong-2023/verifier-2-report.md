**Round 2 verification: Chantranupong et al. 2023 on DANDI:001767 (0.260318.1448)**

**1. Outcomes**

The claims file has 48 claims, including the author's link claim, and the attempt record has 48 outcomes for the same IDs: 16 reproduced, 7 partially reproduced, 16 not reproduced and 9 blocked (7 data_missing, 2 methods_underspecified). The record marks three outcomes `assumed: true`: fig1e-reward-outcome-not-pre, ed8g-vls-telc-ach-suppressed and ed11j-cko-switching-impaired.

I agree with 42 of the 48 outcomes. I disagree with these six:

- **fig1e-reward-outcome-not-pre: reproduced (assumed W1). I find it not reproduced.**
  - The criterion judges both W1 and W2, and the claims-file checks say claims need "both window readings, as the other claims do". W2 gives 7 of 14 DA mice, which is not fewer than half (cell 16). Choosing a window is not left open to the author.
  - The assumption is stated, but its basis is weak. The claims-file header gives the Fig. 1 scripts (`_Fig1_AllDA.m`, `_Fig1_Ach_Words.m`) a pre window of −18 to 0, which includes the side-entry sample. The startDrop = −1 scripts the record cites are for other figures.
  - The result is borderline: it depends on one extra DA mouse that cannot be identified.
- **ed8g-vls-telc-ach-suppressed: reproduced (assumed ΔF/F0). I find it not reproduced.**
  - The criterion says "Reproduced when, under each reading, Ach is lower … in every one of the 4 mice". Reading (a) fails: S952 is significantly higher under W1 and W2, S950 is not lower under W1, and S1143 has p = 0.073 under W1 (cell 78).
  - The argument that z-scoring hides an amplitude loss questions the claims file. It does not let the author pick one reading.
- **fig2a-rdah-smaller-than-dlight: partially reproduced. I find it not reproduced (same as round 1).** In unrewarded trials rDAh is significantly larger than dLight1.1 in 2 of 3 mice, against "consistently smaller". The correlation of WT65's rewarded traces is 0.788, below 0.8 (cell 66). Only the rewarded half of the amplitude part holds.
- **ed11-cko-glm-r2: partially reproduced. I find it not reproduced.** The criterion requires every part under every reading. No part does (cell 104):
  - The R2 part holds only under one model per genotype (G1).
  - The Ach-kernel part holds only under the author's "mean over shifts" reading. Shift by shift it fails under every reading.
  - The DA "comparable" part fails under every reading.
- **ed7e-cin-activation-evokes-da: blocked, data_missing. I agree.** The laser artefact is in the right red channel in all 7 sessions and absent on the left (cell 81). This is an inference from the data, and it fits the Methods' one-hemisphere illumination. The dip in the left dLight1.1 during the laser (−0.44 z) is left unexplained.
- **ed11j-cko-switching-impaired: not reproduced. I agree with the outcome, but the assumption is not needed.** The criterion requires a significant history under each resampling unit, and session resampling gives none. The outcome therefore follows from the criterion without assuming session resampling.

Two unflagged assumptions:
- fig1f-cue-omission rests entirely on the session list in the paper's script. The LED channels show cue onsets in every trial of the "no-cue" sessions (cell 28). The deviation says this, but the outcome is not marked `assumed`.
- "Under every GLM reading" covers the six P×G readings only. Y = 3 is not run for ed5f, fig2h or ed11 (cells 98, 101, 104). It is unlikely to change anything, since Y = 3 and Y = 10 agree to within 0.002 in cell 97.

Claims-file issues (reported, not corrected):
- **fig2h-photometry-glm:** the criterion requires the predicted signal to follow the predictor in both models. When Ach predicts DA, the DA-leads-Ach lag implies a minimum at a negative shift, which is what was found (−54 ms, cell 101). The outcome does not change, because the R2 values fail anyway.
- **fig4g-cko-ach-suppression-lost:** delta-Ach versus mean Ach (my round-1 point B16) is still open.
- **ed8f-amplitude-no-consistent-effect:** the criterion still names no sensor.

**2. Text against the printed outputs**

Every "**Result:**" line, the Summary, the README counts and the record notes match the outputs, except these:

- **Cell 32 and the ed4bc record notes:** "After side entry DA is lower in unrewarded trials in 7 (W1) and 8 (W2) of 14 DA mice … reaching more than half only under W2; before side entry DA is higher in 5 of 14."
  - Cell 31 prints `mice 12` for DA (and 15 for Ach). 7 of 12 is more than half, so "only under W2" is wrong.
  - The outcome is unaffected, because the Ach part fails.
- **Cell 99 and the ed5f notes:** "Leaving out reward raises the DA validation MSE beyond the full model's range under all 12 readings." Cell 98 prints 6 DA readings, and Y was not varied.
- **Findings, data_missing:** "no raw trace in 193 channel-sessions (23 mice)". Cell 5 gives 23 mice for the 163 channels that have a z-scored trace only. Adding the 30 channels with no traces at all brings in S1233, S1451 and WT55–WT59, so the total is 30 mice.
- **Cell 107 (Summary):** "every reading named is shown, and the outcomes resting on one are marked". For fig1e-not-pre and ed8g the claims file did not leave the reading open (see section 1).

My round-1 reasons are given in my own words in `verifications`. Where they changed, it is only by folding in my linked B points (fig4g, fig5b) or dropping cell references.

**3. Round-1 points**

Resolved:
- **B1:** the fig2h and ed11 GLMs were run.
- **B2:** ed5f is now partially reproduced.
- **B3:** the history-versus-base MSE is computed.
- **B4:** the ed7e laser artefact and illuminated hemisphere were checked.
- **B5:** the one-sided ed11j interval was added.
- **B6:** the ed3 LDA under W2 was added. The 7-mouse restriction cannot be run, and the outcome holds anyway.
- **B7:** the ed9jm task parameters are printed, and the confound is recorded.
- **B9:** cohorts now come from the table's virus codes.
- **B12:** not done; it does not change the outcome.
- **B14:** ITI checked: the trials-table and photometry-sample ITIs agree exactly (cell 34).
- **B15:** fig2a pre-window readings were added.
- **B17:** the ed8f sensor is now taken from the legend.
- **B20:** the stray "Result:" lines were removed.
- **B21 and all of section C:** printed, apart from the archive-contents limitation.

Remaining points that bear on a conclusion:
1. **fig1e-reward-outcome-not-pre:** W1 is assumed against a criterion that needs both windows, and the deciding DA count depends on an unidentified extra mouse (B8). Not reproduced, in my view.
2. **ed8g-vls-telc-ach-suppressed:** ΔF/F0 is assumed against "under each reading". Not reproduced, in my view.
3. **fig2a-rdah-smaller-than-dlight and ed11-cko-glm-r2:** partially reproduced is recorded, but the criterion fails as a whole under every reading.
4. **B10:** the thalamic control's virus (349, "retro mCherry") is recorded as a finding but not reconciled. It bears on ed13 and fig5ef.
5. **B11:** for fig1f, the files contradict cue omission. The outcome rests on the script's session list and should be marked as assumed.
6. **B16:** the fig4g measure, delta-Ach or mean Ach, is a claims-file question still open with a reader. It decides the outcome.
