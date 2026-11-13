I've worked through the round-2 report and re-run the entry twice with `python tools/entry.py all entries/kim-2022`. Both runs passed (755 s for the second), and the checks report 0 errors. All conclusions now match the new numbers.

**Outcomes:** none changed and none proposed. The verifier agreed with all 25 (12 tested, 13 blocked), and the new outputs gave no reason to propose a change.

**fig2c-weaker-at-6-7 (the verifier's main point):**
- The record and notebook now say plainly that the criterion's literal wording, pooling every dish and ROI value, would give reproduced. That holds under every variant (50% p = 1.5e-09, 100% p = 2.6e-09), and the notebook now prints it. The per-dish averaging used here is recorded as a departure from the criterion's letter.
- The notes now say the 100% pass rests on a near-background unipolar mean (19 a.u.) from only 2 dishes. I kept it counted, because the criterion counts it.
- The verifier's two caveats point in opposite directions: the literal wording gives reproduced, while discounting the 100% pass would give not reproduced. So partially reproduced, which the verifier agreed with, stays.

**Pole regions in groups of touching cells:**
- All 9 recordings in 000448 turned out to be groups of 2 or more cells, so restricting to single cells wasn't possible.
- Instead I added a variant to the helper (`facing_out`) that keeps only pole pixels facing no other cell along the field axis. It keeps 61 to 100% of pole pixels per file.
- It changes nothing: pole ratio 0.92, charging amplitude still 23.2%, time constants 191 and 614 ns. The record's assumption and the question for the paper's authors now mention the groups.

**Outputs the verifier could not find, now printed:**
- conversion, offset, resolution and unit for every 000489 file;
- series names and descriptions ("Channel1", 144 images in a 12 x 12 grid, "Fig2_25");
- both dandiset descriptions, including FluoVolt's sensitivity of about 10% dF/F per 100 mV;
- the darkest frame of each 000448 file;
- the draft against the published versions of both dandisets;
- channel ratio ranges, the per-field means for 25% and 100%, and the build-up as a percent of the first peak.

**Text corrected:**
- The channel brightness ratio is now 1.28 to 6.54 (below 3 in 10 of 17 dishes), replacing "three to six times".
- The two unipolar dishes analysed have YP0 of 236 and 292 a.u., not the day mean of 273.
- Fig2_25_04 is dated 2021-07-26, and the metadata finding now notes that the two files sharing one YP image give different dates.
- The reverse-trial lag is 74 frames in 8 cells and 75 in cell24.
- The dark-frame finding now uses the printed counts: the darkest frame is the first in 10 of 18 files, and 5 files have frames below half their median.
- The build-up is 7.8 to 10.1% for pulses 2 to 4, with pulse 5 separately at 6.1% (p = 0.089).
- 25% and 100% pulses do not inhibit on average (110.0% and 118.1% of unipolar).

**Differences from the report:**
- The verifier counted 25% below 100% at 6 of 10 fields; the printed table gives 7, and I used 7.
- The notebook header said the drafts were modified before publication. That was wrong: they were modified on 2023-06-20, after it, but hold the same assets. The header now says so.
- The re-run showed that the two channels of the Fig1F sample image are the same image. I added this as a new finding.

**Not done:**
- The imaging-day confound (amplitudes imaged on different days) can't be separated with these dishes, so it stays disclosed only.
- The Fig. 3 to 6 claims are listed under the wrong dandiset in the claims file. That is a matter of how the claims file and the registry's dataset list are set up, not a misreading of the paper, so I added no reader question and `questions/kim-2022.yaml` was not created.
- Nothing was committed, as instructed.

The round-2 review is recorded under `verifications` in `attempts/kim-2022-02.yaml`.
