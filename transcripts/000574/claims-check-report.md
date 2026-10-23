I checked the claims file for 000574 against the paper, corrected 14 claims, and recorded the changes under `checks`. I marked it ready.

**Checker:** `35 claims, 34 quotes, 25 statistical values, 1 problems`. The one problem is P = 5.0e-5 in behavior-rt-correct-incorrect. The value is right: the paper prints it as "5.0 × 10 −5", a form the checker doesn't recognise. I left it unchanged.

**Changes, by claim:**
- **behavior-rt-workload:** removed the per-session ANOVA reading. Table S2 says the ANOVA was over trials (n = 1630).
- **behavior-rt-correct-incorrect, spike-sorting-quality, fig3-probe-onset-not-movement:** tolerances changed from 10% to the standard deviations the paper prints. The protocol uses the paper's stated spread, and the file already did this for the IN/OUT accuracy rates.
- **fig3e-probe-neurons-entorhinal:** probe-window reading (c) was wrong. The retrieval decoding window is the 500 ms before the button press, not after the probe. Reading (b) now cites Methods, Task.
- **fig3-probe-neurons-few-task-specific:** the tolerance on the single workload-dependent neuron was 0, but the criterion allowed 0 to 2. It is now 1.
- **fig4b-speed-lowest-maintenance, fig4c-distance-largest-maintenance:** the number of runs is now open: 200 per the Methods, 2000 per table S2. Both are run.
- **figs3d-hippocampus-loadings:** the statement now includes the amygdala comparison and the first-three-ranks exception, as the legend gives them.
- **fig5-subject1-eeg-power-workload:** "at most one other subject" is now "none", which is what the text says. Pz/Fz is added as a variant electrode reading, and table S2's 116 trials are noted beside the legend's 61.
- **fig5-subject1-plv-hippocampus-pz:** the claimed maintenance specificity was never tested. The criterion now requires maintenance PLV above encoding PLV, and depends_on gains fig6-plv-maintenance-over-encoding.
- **fig6i-plv-posterior-gradient:** the criterion now judges the expected R2 and the 34 electrode pairs, which were listed but never used.
- **hfo-rates-unaffected:** the comparison had been made up. It is now open with two readings: task periods against fixation, or set size 8 against 4. The claim is blocked as `methods_underspecified` until the HFO detector of reference 27 is supplied.
- **sfc-maintenance-over-encoding, fig2b-maintenance-neurons-hippocampus:** choices the paper doesn't state are now labelled as readings: the 5% chance rule for iEEG and scalp EEG, and which labels the null permutes.

**Still open:**
- The RT ANOVA's F(2, 2007) fits no design the paper states. It is reported but not judged.
- Tables S1 and S2 were read from the extracted text by column order, because no PDF renderer was available here. The values I read reproduce the medians the paper prints.
- Fig. S5 cites a table S7 that doesn't exist, so the EEG channels for the other subjects are a reading.
- The HFO claim needs reference 27, which isn't under `paper/`.

The paper's main findings each have a claim, and none comes from another source. **Ready: true.** Nothing was committed.
