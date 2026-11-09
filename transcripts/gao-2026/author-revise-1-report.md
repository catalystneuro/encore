I've revised the attempt for every point in the round-1 report. `python tools/entry.py all` passes all three notebooks (seizure_metrics 61 s, eeg_blocks 26 min, wild_type 12 min), and the check reports 0 errors. Every conclusion matches the new outputs. Nothing is committed.

**Outcome changes (5 of 22)**
- **fig3a-count-sham-vs-tfus**: reproduced → partially reproduced, as the verifier gave it. With the corrected repeated-measures test, post 2 is not significant (p = 0.064 and 0.076); post 1 is, in both hemispheres.
- **fig3c-interval-sham-vs-tfus**: reproduced → partially reproduced, as the verifier gave it. Only the contralateral side is significant at post 1 (ipsilateral p = 0.061).
- **fig6-epileptic-pli-s1-decrease**: partially → not reproduced, as the verifier gave it. The non-S1 part fails too, and the criterion's partial clause does not cover that.
- **figs5-seizures-lower-ai**: blocked → reproduced, resting on assumptions. As the verifier said, 13 of 16 rats have EEG from before the first 4-AP injection; it ends 64 to 176 min before the baseline block. Read between its tFUS pulses, the seizure AI is below that pre-4-AP AI in every band. This holds only with AI on band power, which the paper's wording supports ("relative difference in PSD"). With AI on band-to-total ratios the claim fails, and the notebook shows that.
- **figs7-seizure-pli-s1-vs-non-s1**: blocked → partially reproduced, resting on an assumption. The S1 change is significantly larger than the non-S1 change in theta only (and gamma under one reading), not in all four bands.

**Fixes for each point**
1. **Repeated-measures test**: it now uses t and F with Satterthwaite degrees of freedom, not the normal reference. I checked it against the classical split-plot ANOVA on synthetic data. The first two outcome changes come from this. fig2f and fig3b-sham-percent-time-no-change now also depend on which Bonferroni family is used. I adopted one family per set of comparisons and recorded it as an assumption.
2. **PLI window-length bias**: the 20–200 ms window is now averaged over nine 20 ms sub-windows, so it matches the pre window, and every PLI gets a trial-shuffled noise floor. The earlier tFUS-part decrease for fig5cdj is gone; the notes say so.
3. **EP alignment**: the intervals do start at the burst onsets. Power at 1.4–1.5 kHz (the burst pulse rate) peaks 10–60 ms after the interval start in 13 of 23 CENTER recordings and in none of the 23 resting ones. The LFP shows no clear response at any point in the 2 s cycle, so the missing EP is not a misalignment.
4. **Pre-4-AP EEG**: added a timing table and the figs5/figs7 analyses (see above).
5. **AI on ratios**: tests added. The ratio AI is near 0 at baseline, which means the strongly negative raw AI reflects a difference in total power between the two channels.
6. **Sign under division**: an increase is now shown both ways (the normalized value rising and the AI rising). fig4ef stays partial.
7. **fig5b test**: the paired t is replaced by the repeated-measures two-way ANOVA, and a split-half position reading is added. Now 2 of 18 combinations find significant time points. The outcome stays blocked.
8. **Block-end cut-offs**: six seizures end 1–1.4 s before a block end. Treating them as cut off changes neither fig2c nor fig3d.
9. **BH635**: the label-following variant is now also shown under the ordinary ANOVA.

I also made the helper's range reads retry dropped connections, after a transient network error failed the first full run. In the record, I updated the findings, added two (no clear EP in the LFP; the pre-4-AP recordings are not described as such), and recorded round 1 under `verifications` with the verifier's reasons and my responses.

**Not done**: I added nothing to `questions/001683.yaml`, because the report names no place where the claims file misreads the paper. Two of the verifier's unanswerable items stay open: Satterthwaite is not Prism's exact method, and the borderline cases (fig2f p = 0.040, fig3b-sham-percent-time-no-change p = 0.034) remain sensitive to it.
