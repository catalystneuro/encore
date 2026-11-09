I've worked through every point in the round-2 report. No outcome changed, and none needed a `proposed` change. The final run of `python tools/entry.py all entries/001868-kim-2026` passed: 0 errors, about 25 minutes, and it repeats the earlier numbers. Round 2 is recorded under `verifications` in `attempts/001868-kim-2026-01.yaml`. Nothing is committed.

**Outcomes:** all 43 stay as the verifier agreed them: 16 reproduced, 4 partially reproduced, 4 not reproduced, 19 blocked. Two of them now rest on weaker ground than before:

- **figs7-control-no-change (still reproduced).** The verifier was right that the 700 ms baseline usually contains the previous burst (5863 of 8795 bursts). I added a variant that takes each baseline from before the trial's first burst. Under it, NPL modulation in the controls rises (p = 0.0059), so the "no change" result holds only with the baseline the paper's code uses. I kept the outcome because the protocol says a claim of absence is judged on the paper's own test, with a cleaner test shown as a variant. The notes, conclusion and deviations now say so. I also added which baseline the paper's missing timing file sets to the question for the paper's authors. A third round could reasonably take this up.
- **figs9-coupling-window-and-control (still reproduced).** Checking the verifier's point turned up a bug: the stored `trial_index` restarts in each recording block, so my trial segments had joined trials from different blocks. Trials are now numbered from `burst_index_in_trial` (new helper `icms.control_trial_ids`). After the fix:
  - The early and late tests still find no difference (FDR p = 0.431 and 0.134), so the outcome holds.
  - The sample sizes are now closer to the paper's than the burst reading's in absolute numbers as well (45/48 and 31/90, against 41/18 and 28/46 for bursts).
  - The reason for using whole trials is now three things: the criterion's "the full train", the dataset's own trials table (one row per 3-burst trial), and these sample sizes.

  The restarting index is recorded as a new `metadata_error` finding.

**Outputs added to the notebook**
- A data-check cell for the behavioural imaging files. It prints per-session planar ROI counts, the segmentation descriptions and columns (including `voxel_mask`), that `roi_id_source` is just the row index in every session, and that no reference images are stored. These back the blocked notes, which also misquoted the ROI description and are corrected.
- Control files: burst and trial spacing, plane counts (51 to 171, replacing the unprinted "136 planes"), the trials-table rows and the `trial_index` description.
- **figs4b:** modulated fraction by distance for each mouse, the fit without Mouse 5, and the fit leaving out each mouse in turn. At 4 uA the velocity is still below 0.18 m/s without Mouse 5 (0.179), so the outcome is unchanged.
- **figs5c:** the 568 hit trials with no onset are exactly the ones with no stored wheel trace.
- **fig4:** counts per possible trough-to-peak value, which show the "dip" comes from the binning.

**Text corrected**
- The fig4 outcome now rests on the counts (4 of 6 outside tolerance), not on the "no partial clause" wording.
- The bimodality claim is removed.
- The Fig. 6D finding now gives 75 ms (10 ms bins) and 87.5 ms (5 ms bins) instead of 105 ms.
- The channel-mapping statements now say the check holds when mice are pooled, but not in the nearest bin or in Mice 5 and 6.
- figs7 and figs9 now have `notebook` and `output` fields.
- The summary, README and `entry.yaml` runtime are updated.

**Not done**
- I did not investigate the sign flipping of the Fig. 6D PL clusters or the week-4 KL value under the second Fig. 6C reading. The verifier says neither affects an outcome.
- I added no reader questions, because the verifier reported no place where the claims file misreads the paper.
