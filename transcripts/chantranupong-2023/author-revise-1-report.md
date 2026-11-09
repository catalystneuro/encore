Revision for round 1 is finished. I re-ran the entry with `python tools/entry.py all entries/001767-chantranupong-2023`: 0 check errors, and the notebook passed in 45 minutes. I checked every changed conclusion against the executed outputs, and the round is recorded under `verifications` with all 48 claims. Nothing is committed.

**Outcomes that changed**
- **ed5f-leave-out**: blocked → partially reproduced. As the verifier said, the criterion fails under all 12 GLM readings (dropping side entry never raises the DA error beyond the full model's range), so the open readings don't change the outcome. Reward and the centre entry/exit parts mostly hold.
- **fig2h-photometry-glm**: blocked → not reproduced. It is now run. The R2 of Ach predicted from DA alone, and of DA from the history GLM with photometry, are below tolerance under every reading. The DA kernel predicting Ach is most negative at +54 ms.
- **ed11-cko-glm-r2**: blocked → partially reproduced. All six R2 match with one model per genotype (G1, P1), and the cKO Ach kernels are larger before side entry. The DA kernels are not "comparable" under any reading.
- **ed8f-amplitude-no-consistent-effect**: blocked → not reproduced. The Extended Data Fig. 8 legend places panel f with the dLight1.1 cohort, where all 4 mice show the same sign.
- **ed7e-cin-activation-evokes-da**: not reproduced → blocked (data missing). The laser artefact appears in the right (mCherry) fibre's red channel in all 7 sessions and not in the left (Chrimson) fibre. So the control hemisphere was the one illuminated, and its dLight1.1 trace is not stored. I added this as a finding.
- **fig5ef-input-telc-dampens-ach**: blocked → partially reproduced. The cortical half holds; the thalamic half can't be tested.

**Outcomes I kept despite the verifier, with the disagreement recorded**
- **link-manuscript-sessions** stays reproduced. The TelC and control groups are now formed from the table's virus codes, so the size check no longer counts a hand-written list. The groups come out the same.
- **fig1e-reward-outcome-not-pre** and **ed8g-vls-telc-ach-suppressed** stay reproduced, each resting on its stated assumption (window W1 and the dF/F0 reading).
- **fig2a-rdah-smaller-than-dlight** stays partially reproduced: rDAh amplitudes are smaller in rewarded trials in all mice under every reading, including the newly run pre windows.
- **ed3-not-lateralized** stays not reproduced. The new W2 LDA puts Ach at 0.691, so the Ach part also depends on the window, and the DA part fails under both.

**Outputs added or corrected**
- **ed5-history-glm-r2:** the history model's test error is lower than the base model's in 10 of 10 runs under every reading, on the same test trials. The train-vs-test R2 check shows the per-session models overfitting most.
- **ed11j-cko-switching-impaired:** the one-sided bootstrap still finds no history significant against both controls.
- **ed9jm-vls-telc-behaviour-normal:** the two groups ran under different task settings (high-port probability 0.9 or 1.0 against 0.95; blocks of about 46 against 36 trials). I added this to the notes and as a finding.
- **fig1f-cue-omission:** the "no-cue" sessions have LED onsets at the cue times in every trial. The outcome now says it rests on the paper's script.
- **Other checks:**
  - The table rows of each cohort are printed.
  - The thalamic controls carry the same retro mCherry virus as the cortical controls; recorded as a finding.
  - The Drd2 cohort's channel sensors are checked per session.
  - Channels with no named sensor are listed by mouse.
  - The ITI from the trials table equals centre entry minus the previous side exit.
- **Handover fix:** the combined "Result" cell for ed9jm, ed11fh, ed11i and ed13 is split so the handover strips it.
- **Questions:** I created `questions/001767.yaml` with two questions for a reader: the measure for fig4g-cko-ach-suppression-lost, and the sensor for ed8f-amplitude-no-consistent-effect. Neither claim was changed.

**Not done**
- I did not refit reading (b) of ed1hj on all sessions pooled. The verifier judged it would not change the outcome.
- The DA test restricted to the 7 mice of Extended Data Fig. 3 could not be run, because those mice cannot be identified.
- The extra, unidentified Fig. 1 mice remain unidentified.
- I left the existing changes to `tools/build_site.py` and `tools/site_assets/app.css`, and the untracked dotfiles, untouched; they are not mine.
