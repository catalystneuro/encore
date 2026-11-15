Round 1 is answered and no outcome changed. All 19 outcomes match the verifier's, so every claim is recorded as `agrees: true`. The entry re-ran cleanly with `python tools/entry.py all entries/martinez-conde-2019` (0 check errors, notebook passed in 103 s), and every conclusion and note matches the new numbers.

**Three outcomes now marked as resting on an assumption**
- **table1-edge and table1-s90:** I added a second placement of the baseline squares, centred on the corners and clipped to the ROI (region of interest). With it, table1-edge reaches 3 of 5 values within tolerance and table1-s90 reaches 3 of 5, which would make both partially reproduced. I kept not reproduced, using the squares inside the corners: the Methods say the baseline was measured within the ROI, and centred squares cross its border.
- **fig7c-fold-edge-equivalence:** If "one step" means one level of the grid (from 0.906) instead of 0.037 from 0.90, reading (b) passes. I kept not reproduced, following the criterion's wording, and the notes add the verifier's point that under (b) "nearest" just picks the two ends of the range.

**What I added or corrected for each point in the report**
- **Baseline (B1):** the centred placement now runs through every claim, with a per-file table of the three baselines. The centred squares also find a baseline difference across stimuli (Kruskal-Wallis p = 0.0055). On the same 38 files the Methods' squares find it (p = 0.0245) and the files' own `BaseActivity` does not (p = 0.114). So the two disagree in how they measure, not in which neurons they cover. s4-baseline-no-difference stays not reproduced, marked as an assumption.
- **Star neurons (B2):** the 16 Star files that cannot be placed on the stimulus do not differ detectably from the 12 that can, in peak rate (p = 0.49) or median rate (p = 0.75) of their raw maps.
- **Square and Edge values below the paper (B3):** a per-neuron table shows the paper's means would need a mean baseline of 5.49, 6.30 and 7.79 spikes/s for Edge, S90 and P180, against 8.78 here. No single lower baseline explains the gap.
- **RMS contrast (B4):** I ran the verifier's suggested variant on physical luminance with black levels from 0 to 10 cd/m². None gives the paper's curve. I added a question to `questions/martinez-conde-2019.yaml`, since the verifier reported a gap in the claims file's readings. fig7a stays not reproduced.
- **Undocumented fields (B6):** `norm` is always 0. `smoothed_image_norm` is the map normalised by `BaseActivity` in 17 of its 38 files and something undocumented in the other 21; it is never an eye time or a count. spikes-per-condition stays blocked, and the finding on undocumented fields now covers both.
- **Smaller points:**
  - B7: the statement that every fold runs from 0% to 100% no longer covers the Edge.
  - B8: the refit variant cannot place the contrast levels.
  - B9: the two Corners map sizes are shown to share a centre.
  - The question to the authors now also asks whether the paper's baseline was `BaseActivity`.
- The summary, README, helper docstring and `verifications` block are updated, with the verifier's reasons in its words and my replies under `response`.

**Not done**
- No other baseline placement for Corners: the paper gives only one 0% region inside that ROI.
- B10 (smoothing kernel) and B11 (registration from the authors' maps) were already stated in the notebook and needed no change.
- Nothing is committed, as instructed.
