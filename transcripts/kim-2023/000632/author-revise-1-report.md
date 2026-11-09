I've addressed every point in the round-1 report, and no outcome changed. The entry re-ran cleanly (`tools/entry.py all`: 0 errors, notebook passes in 289 s), and every number in the conclusions, notes and README matches the new run.

**Outcomes**
- **Figure 3 claims:** the five outcomes are unchanged. Three are reproduced and two are not. The verifier agreed with all of them.
- **Seven blocked claims (Figures 2, 4, 5):** they stay blocked, but the reason changes from `data_missing` to `other`. The verifier was right that these data are public: DANDI:000631, 000633 and 000634 each name the paper as IsPublishedIn. The protocol reserves `data_missing` for data that are not public anywhere. The claims file scopes every claim to 000632, so I did not test them on those dandisets. The verifier had accepted `data_missing` within that scope, so this disagreement on the reason is recorded in `verifications`.

**Added or corrected**
- **Other dandisets:** the false statement that the data are "not public elsewhere" is gone. A new notebook cell lists 000631, 000633 and 000634 from the archive with their link to the paper. The header, summary, README, `entry.yaml`, the blocked claims' notes and the finding now point to them.
- **Question for a reader:** `questions/000632.yaml` is new. It has three questions asking whether to mark the Figure 2, 4 and 5 claims as data held elsewhere, naming the dandiset and version for each. The claims file is unchanged.
- **Centre ROI check (asked for in the report):** `epimg.refine_footprints` finds the footprints again on a finer image (5.2 µm blocks).
  - The refined array centre is a median 54 µm from the one used (range 6 to 193 µm; 4 dishes are more than 100 µm off).
  - A new figure shows every array with the centre ROI and the refined footprint outlines.
  - Putting the ROIs at the refined centres was run as a variant for all four tests; no outcome changes.
- **Pixel size:** the 0.5 mm lumen can't be seen in the images (YP inside it is 0.97 to 1.13 times the YP around it), so it gives no second check of the 0.65 µm/px scale. The refined footprints measure a median 1.66 mm across, against 1.5 mm needles. The deviation now says this.
- **Low power:** each test now prints the 95% interval of the difference and the smallest difference it would detect with 80% power. That is 81% to 199% of the reference group's mean. The conclusions and notes now say the two "no difference" claims mean only that no difference was found, not that the groups are equal. The two not-reproduced differences (1.96-fold and 1.59-fold) are smaller than their tests could detect.
- **Group sizes:** the notebook and the group-size finding now discuss the extra cross-directional and the missing co-directional dish at 770 kHz. The labels are kept as deposited. The four cross-directional 770 kHz dishes of 2022-12-04 have anisotropy 0.06 to 0.18, below every co-directional dish (0.31 to 0.75).
- **Round record:** round 1 is recorded under `verifications`, with the verifier's reasons in its own words and a response for each claim.

**Not done, and why**
- I did not test the Figure 2, 4 or 5 claims on 000631, 000633 or 000634. The claims file scopes them to 000632, so results there would be counted towards the wrong dataset. That waits for the reader's answer.
- I did not compare effect sizes with the paper's Figure 3 bar heights and p-values. The paper text doesn't contain them.
- Nothing is committed. The untracked files at the repository root (`.bashrc`, `.idea`, `scripts` and others) are not mine and should stay out of the commit.
