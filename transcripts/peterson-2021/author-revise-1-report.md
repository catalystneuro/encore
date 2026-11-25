I've worked through every point in the round-1 report and re-run the entry twice with `python tools/entry.py all entries/peterson-2021`. Both runs passed in about 38 minutes and gave the same numbers. `tools/entry.py check` reports 0 errors and the record validates against the schema. Nothing is committed.

**Outcome changes**

- **fig5-recording-day-effects: partially reproduced → not reproduced.** The verifier's problem 1 was that region power used each file's own good-electrode flags, while the claims file renormalises per subject. The main analysis now uses the electrodes good in every file of the subject, for the segment rejection, the projection and the regression. With that choice 18 of 24 subject and band pairs agree with the paper, below the criterion's 20. The outcome is marked as resting on this assumption. Each file's own flags, the round-1 choice, give 20 of 24 and are shown as a variant.
- The other 24 outcomes are unchanged. Some numbers moved:
  - **table1:** the best reading is now 18 of 24 inside the paper's intervals (21 with each file's flags), still partially reproduced.
  - **fig4:** two of four parts now hold (three with each file's flags), still partially reproduced.
  - **fig3-lfb-more-widespread:** the two readings still disagree (8 against 8 regions; 36.0 against 22.2 bins), so it stays blocked.

**Added or corrected**

- Region power is renormalised over electrodes with finite power in each event; no kept event needed it. The notebook now counts events with exact zeros on good electrodes. In S09 and S10 every analysed event has runs of at least 50 ms of zeros on 1 to 15 good electrodes; this is a new minor finding at the end of the list.
- The one event whose two time stamps disagree (S08 day 4, 40.3 s against 86440.3 s, past the end of the recording) is counted and left out of reading (b).
- The regression variants that were missing are now run: the four other seeds with Delta R² and coefficients refit, log(onset speed + 1), and the code's inclusion of bad electrodes. Day and angle stay on top, and the angle signs hold, in all of them.
- Projection rows: the zero rows of S03 and S12 sit exactly at the electrodes without a position. Shifting the rows by 1 to 3 places lowers the agreement with the nearest region in all 12 subjects.
- New printed outputs:
  - a table of the angle density at ±90, ±75 and 0 degrees per subject;
  - event counts after the Methods' 0.5–4 s filter (fewest 207, still outside the tolerance);
  - the grid-only surface count (63.08, outside the tolerance, so the group-description reading stays).
- The forward-selection leakage is now stated in the notebook and the deviations. The claims file prescribes the method, so it is kept.
- One finding's number was wrong: 1708 of 8088 bimanual overlap values are above 1, not 1661 (that figure came from the analysed subset). The findings that describe the clock check, the segment rejection, the spread measure and the electrode flags now give the new numbers.
- I added three questions for a reader in `questions/peterson-2021.yaml`:
  - the "drop all-zero rows" wording for roi-projection-link;
  - the 15° window on a density with no boundary correction for fig2-reach-shape;
  - the 0.5–4 s filter for fig2-event-counts.

  No claim was changed.
- The round is recorded under `verifications`, with all 25 claims. I also updated the notebook conclusions, the summary, the header, the helper docstring and the README.

**Not done**

- The Benjamini–Hochberg correction still runs over the −1.5 to +1.0 s bins only. The paper does not state the spectrograms' time range, and the verifier found it changes no outcome.
- Under the other seeds, the variants refit only the models with R² above 0.03 under the main fits. The regions of the models that pass 0.05 under those seeds were not recomputed.
