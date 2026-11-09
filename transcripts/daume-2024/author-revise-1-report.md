I've finished the round-1 revision. Five outcomes changed. The entry re-ran cleanly with `python tools/entry.py all` (880 s, 0 check errors), and every number in the conclusions matches the executed copy.

**Outcome changes**
- **fig1d-wm-rt-load: partially reproduced → reproduced.** The verifier pointed out that with 10,000 permutations, whether p falls below 0.0001 depends on the seed. With 2,000,000 permutations p = 6.0e-05 (95% upper bound 7.0e-05), so it is below the bar. Over 100 seeds of 10,000, 63 draws give p below 0.0001. The larger permutation count is recorded as a deviation.
- **fig2c, fig2e, fig2f and fig4f: now blocked (`methods_underspecified`).** For each, the readings the criterion names give different outcomes, and the claims file's shared method blocks such a claim. I agreed with the verifier, dropped the assumed readings, and kept every reading's result in the notes.
- **fig4d-category-no-memory-signal: blocked → reproduced.** I looked at all 600 new LTM images (200 for each of the 3 task variants). In every variant the IDs fall in blocks of 40 per category, in the same order as the old pictures' leading digits, with no exceptions. Two sessions of each variant hold identical images. The notebook now shows contact sheets of every new image so this can be checked. With these labels, no reading reaches p < 0.05. Reading the labels by eye is recorded as a deviation, and the metadata finding stays.

**Added or corrected**
- **Question for a reader** in `questions/001187.yaml`: reading (b) of fig2c/fig2f uses 0/1 coding, so its `acc` and `l1` terms are not main effects. The claims file is unchanged. A variant with centred coding is shown, and its load effect is also not significant.
- **fig3c**: a table of neurons lost at each step and rows per condition. Only 80 neurons have both conditions before any removal, fewer than the paper's 83. Adding incorrect trials as a diagnostic gives p = 0.46 and 0.12, so the outcome stays not reproduced.
- **fig3e**: the time-resolved t curves are now printed. The notes say the criterion's partial grade is met but the data do not show an early effect. They also say windows near 0 s include part of the last encoding picture.
- **fig4e**: per-pair strong minus weak has median -0.044 Hz (37 pairs positive, 47 negative). A pooled median split also puts strong below weak in all 24 readings. The outcome stays not reproduced.
- **Clock check**: per-session peri-onset counts of responding units and PSTHs. Nine of the 12 flagged sessions show responses at the true onsets. The other three hold 10 of the 883 units and are assumed to share the clock.
- **Model fits**: a convergence and missing-SE/p table for every mixed model. None failed to converge and none has a missing SE or p.
- **Record**: round 1 is recorded under `verifications` (the verifier agreed with 25 of the 29 outcomes as they stood). The `methods_unavailable` finding now also asks the paper's authors which model and coding they used for Fig. 2c and 2f. README, notebook summary and `runtime_minutes` (15) are updated.
- **Dependency**: `pillow` was added to the requirements and lock file, for the contact sheets.

**Not done**
- No outcome was changed for problems 5 to 7 (the all-sure session, the windows near 0 s, the 24 uncorrected tests). The verifier marked them as not affecting a conclusion, and each is now noted in the record.
- I did not commit, as instructed.
