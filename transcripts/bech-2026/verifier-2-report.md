**Round-2 verifier report: 001847-bech-2026-01 (doi:10.7554/elife.109717)**

**1. Outcomes**

The claims file and the attempt record both list 40 claims.

I agree with 37 of the 40 stated outcomes:
- **Session lists and expert sessions:**
  - session-list-link is partially reproduced (98.0%, cell 5).
  - expert-sessions is not reproduced: 318 sessions in 49 mice, and neither variant gets all three counts within tolerance (cell 8).
- **Behaviour, reproduced:** fig1c-whisker, fig1c-catch, fig1d, fig1e, fig1g, fig1f, fig1h, fig1i-pupil and fig1i-posture.
- **Behaviour, partially reproduced:** supp1d (the means are about 100 ms high) and fig1j (whisker speed differs by context, corrected p 0.018).
- **Model:** fig1k-model-accuracy is reproduced (0.781, against 0.500 for permuted labels; cell 101). fig1k-context-strongest-feature is reproduced: context is first, then the other three in the stated order (cell 104).
- **fig1l is not reproduced under the criterion's sign rule** (cell 107). The claims file may misread the paper here. The model has context as its own feature, so the trial-in-block feature's SHAP values describe only what is left after context, which is the one-trial lag. The criterion's sign-flip test cannot be met by such a feature. The author has put this question to a reader.
- **Optogenetics (seven claims), blocked as methods_underspecified:** blocked is correct. Leaving aside the Methods' block-label null (null (i)), the trial-shuffle null still gives different outcomes at d' 0.5, 0.8 and 2 (cells 44–62).
- **Muscimol and Figure 3:**
  - supp2 is reproduced. The injection-day check holds: all 26 sessions typed pharma_session are second-date sessions (cell 65).
  - fig3e and fig3-gcamp are partially reproduced; fig3f is reproduced.
  - supp3c is blocked as data_missing.
- **Figure 4:** fig4c, fig4fg and supp4d are reproduced; fig4e is partially reproduced; fig4d is not reproduced.

**fig1c-auditory and supp1c (reproduced, using the code's list):** I now accept these. The criterion takes "either reading of the selection". The claim itself says "over 41 mice", and expert-sessions shows that the Methods' rule does not give the paper's mice. This depends on the protocol clause the author cites ("a match under one suffices"), which I cannot see.

**fig3c (`assumed: true`, the Methods' correct whisker trials):** the assumption is stated and reasonable. The paper's Methods (Figures 3B and 3C) say the onset is computed "from the jaw traces in Figure 3B", which are "correct trials (i.e. licks to whisker in W+ and no licks in W-)". The result holds with the 70% session rule (90.0 ms over 5 mice) and without it (85.8 ms over 6 mice) (cell 110). The claims file misreads the paper slightly: it says the trial set "is open in the text", but the Methods name it.

I disagree with three outcomes:
- **fig3h (`assumed: true`, the 50 ms baseline):** the assumption is stated, but it is not acceptable. The criterion requires agreement "under every baseline … otherwise methods_underspecified", and the claims file sets 50 ms and 250 ms as the readings. With 250 ms the smoothed pixel version gives a tie between RSC and wM1 at 50 ms, which is partially reproduced (cell 76). With 50 ms both versions give reproduced. The criterion therefore gives blocked (methods_underspecified). The paper really is inconsistent: its Methods say 250 ms for Figures 3 and 4, but 50 ms for Figures 3E&F, whose d' Figure 3H uses. So the claims file reads the paper correctly here, and this belongs with the authors as a question.
- **fig4b (all three claims, blocked as too_large):** the record itself says "a separate notebook could hold it, but was not built within this run". The re-executed notebook estimates about 50 minutes of reading (cell 124). That is a limit of this run's time, not of the data's size, so too_large overstates the cause.

**2. Sentences the outputs do not support**

- **fig3h notes, "22.1 GB read in 1.7 min":** cell 76 prints "22.1 GB in 3.0 min, 122 MB/s".
- **fig4b notes (all three) and the three fig4b verification responses, "(22.1 GB in 1.7 min, 218 MB/s) the reads alone take about 28 min":** cell 124 prints "50 min of reading". The text "with the 42 min of the rest of the notebook" is not printed anywhere.
- **Notes for fig2c, fig2d, fig2e, fig2e-rsc, fig2cd, fig2-control and fig2f, "under it no site reaches d' 0.5 in whisker or auditory trials", and the Figure 2 methods_unavailable finding, "finds no affected site at d' 0.5":** under null (i), cell 42 shows wS1 at 0.53 and 0.53 and tjS1 at 0.57 and 0.56 in whisker trials. The record's own fig2e and fig2e-rsc notes give "at most 0.54" and "at most 0.57". No outcome changes.
- **fig3f notes, "|d'| at most 0.94 (wS1)":** cell 73 shows wS1 at 0.97 with the 250 ms baseline.
- **Cell 119, "RSC and tjS1 have the smallest angles in W+":** in cell 118, A1 (22.3°) and RSC_2 (23.7°) are below tjS1 (26.9°) and RSC (33.1°). The sentence holds only against the sites the criterion compares.
- **The format_error finding on DLC timestamp and data lengths (PB177_20240529_121819, PB192_20241121_122848):** no printed output shows this; only a comment in the helper module does (bech.py:397).

I checked every other "**Result:**" sentence, the Summary (cell 126), the README and the remaining notes against the outputs, and they agree. The README's rows add up to 40 claims.

The attempt record states my round-1 reasons faithfully and in my own words, each with its B-point.

**3. Round-1 points**

Resolved:
- B1: kept blocked, with a synthetic check in cell 42 and a question to a reader.
- B2: fig3c is reworked, and the PB177 exclusion is explained.
- B3: the pixel part has been run.
- B4: the model has been run.
- B5, B6, B7, B9, B10, B11 and B12.
- B14: accepted, as described in section 1.
- The fig4d and fig4e loadings are now printed.

Accepted without change: B8 (the peak reading is uninformative) and B13 (the Off-day noise labels).

What remains that bears on a conclusion:
- **fig3h:** should be blocked as methods_underspecified under its own criterion, not reproduced on an assumption.
- **fig4b (all three claims):**
  - The reason should say the analysis was not run in this attempt, not that the data are too large.
  - The read rate and time estimates in the record are out of date (28 min against the printed 50 min), and the "42 min" figure has no printed source.
- **fig4d:** the claims file's mean-squared-distance measure does not fit this case. The inhibited trajectories at wS1, wS2, wM1, wM2 and ALM are far from both control trajectories (17 to 61 against about 1 to 3 for RSC, cell 115). So "closer to lick or to no-lick" is decided by small relative differences, and the not reproduced may reflect the measure rather than the paper's finding.
- **fig1l:** the criterion's sign reading may not fit what the trial-in-block feature can show, as described in section 1. This is with a reader.
