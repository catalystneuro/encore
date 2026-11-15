No outcome changed in this round. I proposed two changes for round 3, and the entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passes in 56 s).

**Proposed outcome changes (in `proposed` on the record; the verified outcomes stay as they are)**
- **table1-edge and table1-s90: from not reproduced to partially reproduced.** The verifier said the two ways of placing the baseline squares (inside the corners, or centred on them) were equally defensible. To decide, I compared each placement with the files' own `BaseActivity`, the authors' undocumented baseline. For Square and Edge, the centred squares are closer to it in 7 of 9 files (median absolute difference 0.67 against 1.51 spikes/s, signed rank p = 0.027). With the centred squares both claims reach 3 of 5 values within tolerance. I also removed the weak argument that centred squares cross the ROI border from the helper, the notebook and the record.

**Added outputs**
- A data-check cell comparing each placement with `BaseActivity`. For Star the result is the reverse: the inside placement is closer in 8 of 10 files.
- Two new baseline readings, run through every claim in a new section "Baseline readings compared":
  - "nearest": for each stimulus, the placement closer to `BaseActivity`.
  - "corners_quarter": the two Corners squares moved to the quarter points of the ROI's bottom edge.
- **table1-s40 depends on the Corners placement after all.** With the quarter-point squares it gets only 2 of 5, which would be not reproduced. Its outcome stays reproduced, now marked assumed. I kept the bottom corners because they are closer to `BaseActivity` (median difference 0.72 against 2.88 spikes/s).
- Cell 41 now prints the range of a single mean baseline that puts all three Square and Edge midpoints within the paper's SEM: 6.64 to 8.24 spikes/s. The squares give 8.78, which is 0.54 above that range.

**Corrections**
- **Fig 4B text:** fixed the wrong conclusion in that notebook conclusion and the fig4b notes, and dropped "not baseline-related".
- **Summary table:** the assumed flags now match the record.
  - s4's assumption is now "the Methods' squares, not `BaseActivity`".
  - fig4b no longer carries an assumption, since it is partial under every baseline.
  - table1-s52 now carries its assumption.
- **Data check and record:**
  - The helper now also reads `norm` from the one MATLAB v7.3 file; it is 0 there too, so 74 of 74.
  - `BaseActivity` is in 38 files, not 40 (finding and docstring).
  - The `smoothed_image_norm` wording now says two relations plus "neither".
- **README:** the sentence that said the baseline comparison depends on placement is fixed.
- **Unverifiable claim removed:** the "(not run here)" sentence in cell 26 is gone.
- **Verification record:** round 2 is recorded under `verifications` with the verifier's reasons and my responses.

**Not done**
- No new question for a reader: the report found no new place where the claims file misreads the paper, and the RMS-contrast question is already filed.
- Nothing was committed.
