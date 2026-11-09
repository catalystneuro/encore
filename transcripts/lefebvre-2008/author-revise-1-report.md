I've worked through all of the verifier's round-1 points. One outcome changed: fig9d (receptive-field size similar) went from not_reproduced to blocked (methods_underspecified). The entry re-runs cleanly with `tools/entry.py all` in about 8 minutes, `check` reports 0 errors, and nothing is committed.

**Why fig9d changed.** The verifier asked for the alignment search on 20080702_R4 to be run in the notebook. It showed that the old text was wrong: the stated frame lengths of the vertical-bar recordings of 20080702_R4 and 20080702_R1 (16.6653 and 16.6691 ms) are not those of the stimulus.
- Rebuilt with 16.6718 ms, the frame of the other 22 bar recordings and half the checkerboard frame of the same retinas, 10 of the 12 units of 20080702_R4 give clear STAs. The median peak ratio over the null is 2.57, against 0.96 with the stated frame.
- Following the protocol's "trust the data", the main analysis now uses the corrected frame, and a variant keeps the deposited frames.
- With the correction, the DKW band under reading B (svd separation) overlaps. So fig9d separates in 17 of 18 combinations, and the criterion gives blocked.
- With the deposited frames all 18 still separate, so this one combination is close to the line. The verifier agreed with not_reproduced, so round 2 needs to review this change.

**Other outcomes** stay as verified: counts not reproduced, surrounds reproduced, slower time course reproduced, lower firing rate reproduced, threshold not reproduced, gain blocked.

**Output added for the verifier's points and requests:**
- **Alignment search (B4):** the frame scan for both 20080702 recordings and an onset search of ±2 s. The weak 20080606 retinas peak at the stated onset, so their weak STAs are weak responses, not misalignment.
- **Null calibration of the bands (B1):** shuffling the group labels 200 times per measure, the binomial band separates in 35% of shuffles, the bootstrap band in 37%, and DKW in 0 of 1600. Each conclusion now says whether its result holds under DKW.
- **Cells behind each separating value:** shown for fig9e and for the continuous-form gains of fig9h. After the frame correction, fig9e no longer separates the other way anywhere, so I removed that deviation.
- **LN fits at the grid edge (B7):** under reading A, 107 of 200 mutant and 39 of 122 control binned/printed fits stop at the top of the θ grid. Without them those medians are equal (−0.03 and −0.03). The frame/continuous fit has 1 edge fit per group and still separates, DKW included.
- **Synthetic check of the LN fit (B6):** it confirms the printed-form bias. For a true θ of 0.5 and gain of 20, the printed fit returns 0.75 and 13.4.
- **Other additions:**
  - a per-retina count table
  - example b(x) and a(t) for strong and weak cells in each group
  - a reading-B check with the deposited frames

**Corrections from the new numbers:**
- **Cell counts:** no mutant count is now inside the tolerance (138 above a ratio of 1.5, 103 above 2), where before 126 was in range. The outcome stays not_reproduced.
- **Findings:** the `metadata_error` finding now records the wrong frame lengths, in place of "cannot be rebuilt".
- **Text:** I updated every conclusion, the summary, the README, the runtime in `entry.yaml`, and the notes and deviations in the attempt record. I added a round-1 `verifications` block, with the verifier's reasons in its own words and my changes under `response`.

**Not done:**
- **Group definition (B2):** I kept the data set's labels for the groups, as the claims file requires. The variant with only the Pax6-het controls is shown.
- **Responsive subset (B3):** I did not judge fig9d on a subset of responsive cells, since the criterion uses all units. That variant is reported.
- **Matching the paper's 115 and 143 cells:** this can't be done, because the files give no recorded region for the Pax6-Cre retinas.
- **Untracked files:** some dotfiles and folders I didn't create (`.bashrc`, `.idea`, `scripts` and others) showed up untracked at the repo root. I left them alone.
