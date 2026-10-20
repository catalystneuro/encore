The repeat attempt on the 001754 draft is done. `entry.py all` passes (0 errors, the notebook runs in 318 s), the handover is in `executed/001754-knierim-2000/handover/`, and nothing is committed. The draft was last modified 2026-10-14T21:55:09Z. All eight files were replaced by a new conversion (`mcnaughton2000-to-nwb` at commit `7346882`); the dandiset's description was not changed. I kept the claims file unchanged, since no claim was wrong about the paper.

**(1) Outcome per claim** (earlier outcome in brackets)
- `flight-spatial-code`: not reproduced [not reproduced]. On flight day 9, 10 of 25 Rat1 units are significant (0.40; 10 or 11 in the repeats) and 2 of 28 Rat2 units. The real spikes are the same as before. The draft's position trace also has samples at the other rat's spike times, so the shuffles change and Rat1 drops from 12 to 10. The earlier gap in dropped shuffle spikes between the rats is gone (0.058 against 0.060).
- `three-orthogonal-surfaces`: blocked, metadata insufficient [same]. The draft now states that the camera view and pixel size are not recorded.
- `si-comparable-to-preflight`: reproduced [reproduced]. The main test's maps and numbers are unchanged (1.385 against 1.448 bits/spike, p = 0.45).
- `fd4-abnormal-selectivity`: reproduced [not reproduced]. One-sided p is 0.024, against 0.055 before. This is the one change of outcome, and it rests on three rate maps:
  - The draft leaves out every copy in each group of identical maps, which removes three Rat2 flight-day-4 maps (7.583 bits/spike each, near-zero rate) that the first attempt counted once each.
  - A new notebook cell runs the same test on the earlier version's maps: p = 0.055 with them and 0.024 without them.
- `fig3-stability-across-sessions`: reproduced [reproduced]. Median correlation 0.537, as before.
- `theta-normal`, `ripples-normal`: blocked, data missing [same].

**(2) Earlier findings**
- **Fixed:**
  - Rate maps are now linked to their units; the linked map is the best match for 201 of 211 unit-epochs.
  - The -999 bins and lost positions are now NaN and documented.
  - Duplicate maps are gone, but every copy was removed, so six maps are no longer in the dandiset.
  - Units now list their spike files and windows, and the description says a unit is one sorted cluster across epochs.
  - The spike-time resolution is documented, and the zero intervals follow it.
  - The overlapping baseline epochs are gone.
- **Partly fixed:**
  - Shared position trace: each file now holds the trace only in its own rat's task epochs, with a stated assumption that it is that rat's position. But Rat2's units are still not selective in any window, and Rat1's units are selective in Rat2's flight-day-4 window (10 of 15).
  - Smoothing kernel: the description now says the maps are smoothed, but the kernel is not recorded.
  - EEG: the files now say no EEG was archived, but the dandiset description still reports theta and ripples.
  - Age, pixel scale and camera view: the files now say these are not recorded, but the values are still missing.
- **Still present:**
  - Position is given only at spike times.
  - The dandiset description still says preflight was on a flat rectangular track, while the files label those epochs Escher staircase and Magic Carpet.

**(3) New finding**
- Rat2's preflight file shares no tetrode with its flight files (TT0 to TT10 against TT12 to TT22). The conversion notes list the assignment of preflight recordings to rats as an open question.

**(4) Where the protocol did not fit a repeat attempt**
- The attempt schema has no field for the status of an earlier finding. I listed the fixed ones in the record's opening comment, and started each remaining finding's statement with "Still present", "Partly fixed" or "New". Fixed findings therefore appear only in that comment.
- The protocol says to pin a version, while the repeat rule allows the draft. The notebook prints the draft's modification time but does not stop if the draft changes later.
- A data-owner fix (dropping all copies of duplicate maps) changed an outcome without any change to the analysis. The protocol has no rule for that case.
- Untracked dotfiles (`.bashrc`, `.mcp.json`, `.idea` and others) were in the working tree before I started, and the workflow may commit them with my changes.
- The repository README's table of outcome counts for 001754 still shows the first attempt's numbers. I did not edit it.
