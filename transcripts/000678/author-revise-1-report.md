I've addressed every point in the round-1 report. Two outcomes changed, both to reproduced, and none went the other way. The entry was re-run with `python tools/entry.py all`: 0 errors, and the notebook passed in 1550 s (about 26 minutes). That is close to the 30-minute CI limit. The numbers matched my separate development run exactly, and the record, notebook conclusions, summary and README now use them. Nothing is committed.

**Outcome changes**
- **fig2b-optimal-occupancy**: partially reproduced → reproduced. The indeterminate share is now 13.1% ± 1.6% (expected 13.1 ± 1.6), and the optimal state beats each other state at p = 0.00024.
- **fig3f-movement-index-inverted-u**: partially reproduced → reproduced. r² is now 0.574, just inside the 0.57 lower bound; the shape holds, and pupil vs movement is not different (p = 0.22). It is borderline, and the notes say so.

Both changes come from two fixes that re-fit every state model:
- **Cross-validation initialisations:** raised from 3 to 10 per fold, as the paper does and as the verifier asked (point 1).
- **Visual stimulus values:** the verifier flagged this as something it could not check. The paper's `get_stim_vals` takes them from the `visual_gabor_angle` column where a file has one, and 123 of the 141 visual sessions do. Those sessions use 1, 0.6 and 0.2 in most cases, not the fixed 1, 0.8 and 0.6 the first version used. `hulsey.py` now follows the code.

The other outcomes stayed the same, but some numbers under them moved:
- **figs2-n-states:** every mouse now has 3 or 4 states, so no mouse has 5. The criterion only asks that counts fall within 3 to 5, so it stays reproduced, and the notes say the largest count is 4.
- **fig2c-dwell-times:** the indeterminate dwell is now in tolerance (3.31), but the optimal dwell (42.8 to 43.8) is above the paper's 37 under every reading.
- **fig3d-optimal-pupil-modality:** p is now 0.013.
- **fig4b-variability-at-transitions:** 3 of the 4 marked tests now pass.
- **fig5c-movement-index-best:** the movement index is now lower than pupil but not significantly (p = 0.086), so it stays not reproduced.

**Other changes for the report's points**
- **Point 2:** the notebook and notes now say the condition 5 and condition 1 variants keep pupil information, so they cannot test the movement-index claim.
- **Point 3:** stationary reading (b) now uses absolute speed below 0.02 m/s. The old rule is shown as a variant; it added 214 backward-moving trials and does not change the result.
- **Point 4:** the notebook prints each state's psychometric and its distance to all six templates for BW061 and BW048. With the new fits, every state of both mice is nearest the template of its label. The text now says that under the claims file's labelling rule this matching cannot fail.
- **Point 5:** the extra zero-length epochs from `get_dwell_times` are explained, and a variant without them is shown. There are 3 such epochs, and no number changes.
- **Point 6:** a variant gives the mean r² over 10 shuffled splits per mouse. BW051's pupil r² ranges from 0.001 to 0.562 across splits. The criterion fixes the paper's single split, so that stays the main result.
- **Data check:** it now prints the trial-table columns and the visual stimulus values per session.
- **Record:** I wrote the round-1 `verifications` block, with the verifier's reasons in its own words and my response for each claim. `runtime_minutes` is now 26 and the README is updated.

**Not done**
- No question added to `questions/000678.yaml`, because the report did not say the claims file misreads the paper.
- Points 7 and 8 (the session counts and the decoder run counts) needed no change; the verifier said neither affects a conclusion.
- Which 381 sessions the paper used is still unknown, as before.
