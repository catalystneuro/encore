# Verifier report, round 2: Sennesh et al. 2025 on DANDI:000253 (0.240923.1441)

The claims file has 37 claims. The attempt record has 37 outcomes: 16 reproduced, 10 partially reproduced and 11 not reproduced. Thirteen of them carry `assumed: true`: fig2ab, fig2e, fig2g, fig2h, fig2i, fig3d, fig3g, fig3h, fig3i, fig4def, fig4g, fig4h and fig4i.

## 1. Outcomes

I agree with 34 of the 37 outcomes. I disagree with three: fig3d, fig3h and fig3i.

**I agree, and the stated assumption is reasonable:**
- **fig2ab (partially reproduced):** the code's condition-panel reading (dB of the trial-mean power) is stated and settled from the code, and the per-trial dB reading is shown beside it.
- **fig2e (partially reproduced):** the code's 5–150 Hz fitting range (S3 reading a) is the conservative choice here; reading b would give reproduced. The L1 value changes with which L1 row is kept (0.74 against 2.30 dB), and the record says so.
- **fig4def (partially reproduced):** partial under three of the four readings.
- **fig2g, fig3g, fig4g (reproduced) and fig2h, fig2i, fig4i (not reproduced):** in the gamma CSDs, the L4 sink starts several samples before the L2/3 sink, so the tie-break works there.
- **fig4h (not reproduced):** this follows from the tie-break, but it is fragile. In reading a, L1 and L5/6 are already sinks at the first lag while L4 is a source (v1 cell 103), so a by-eye reading could give the opposite result. The S7 rule fails in both readings.

**I disagree:**
- **fig3h (record: reproduced; my rating: not reproduced).** Cell 85, reading a: the L1 "sink onset" at −32.0 ms is one sample (`.......S......`), and that sample is not displayed (the shown row has no x there). L1's displayed sinks begin at +28.0 ms, after L2/3 and L4. Under reading b, L1 is not first either, and S7's rule fails in both readings.
- **fig3i (record: reproduced; my rating: not reproduced).** Cell 88, reading a: L2/3 and L4 are both sinks from the first lag (−124.8 ms) through most of the window. The −120.8 against −84.0 ms ordering comes from brief sign flips, so a by-eye reading gives a tie, which is what S7's own rule gives. Reading b fails, and there are 685 and 575 windows against 335.
- **fig3d (record: reproduced, assumed; my rating: partially reproduced).** The adopted combination takes the code's fitting range together with the Methods' 30–90 Hz band, and it is the only one of the four readings that reproduces (cell 73):
  - 30–50 Hz band: partial (late value 0.94 dB).
  - Under the 5–90 Hz fitting range (S3 reading b), with either band: L5/6 has no onset increase (0 points), so not reproduced.

  The stated reason for preferring the code's range is arguable. The Methods sentence "2 to 90 Hz" sits in the paragraph about removing the aperiodic component from spectrograms (paper line 174). The onset values (0.57–0.75 dB) are also above the paper's 0.2–0.4 dB; the criterion does not test them.

**The 2-to-10 Hz edge window (fig2f, fig3e, fig3f):** the caveat is now stated, and the outcomes do not depend on it.

## 2. Sentences the numbers do not support

**Attempt record notes:**
- **trial-counts:** "A likely cause is the handling of the 0 to 2 main-block sequences per mouse…". Those sequences can only affect the main-block counts (xxxX, xxxY). The differences in XXXY (random block, −3), xxxx (−4) and yyyy (−1) come from other blocks (v1 cells 5 and 25).
- **fig2ab** (also v1 cell 33, "the gamma does not last"): "…and the gamma does not last past 250 ms". Under the per-trial dB reading, the largest gamma value after 250 ms equals the overall maximum (1.58 / 0.72 dB, cell 32). The gamma does last; what fails is the 2.25 dB level.

**Findings list:**
- **Finding 12 (code_mismatch):** "4 of 13 within tolerance against 0". Areas cell 36 shows at most 3 of 13 under 30–50 Hz, and up to 2 of 13 under 30–90 Hz (S3 reading b, significant-points average). The 4 is the round-1 number.

**Notebooks:**
- **v1 cell 104:** "the margins are under 1 ms in reading b". Only the L1 margin is (0.8 ms); L5/6 trails L4 by 4.8 ms.
- **areas cell 37 and the record's fig5 note:** "its unfiltered variant reproduces the areas notebook's V1 values". The values match, but the GO point count differs by one (1307 against 1308, v1 cell 23 against areas cell 36). This is trivial.

**README:**
- "six Neuropixels probes each in V1, LM, RL, AL, PM and AM": v1 cell 7 shows three mice with no AL probe and one probe with no area label.
- "About 17 minutes" and "About 35 minutes": the notebooks report 13.0 minutes (v1 cell 113) and 26.7 minutes (areas cell 45).

Everything else in the Result cells, both Summary sections, the README outcome table (all 37 claims, counted against the record) and the record's notes matches the printed outputs.

**Round-1 reasons:** the attempt record reproduces my round-1 reasons word for word, in my own words.

## 3. Round-1 points

**Resolved:**
- **1 (condition panels):** the code's reading is run, and the extra "peak above 0 dB" requirement in the rise test is gone.
- **3 (areas pipeline):** the V1 values move by at most 0.09 dB without the median filter, and the masks share 70–88% of their points. The fig5-hierarchy outcome holds even if the small counts (GO-AL 4 points, GO-AM 2) flip.
- **4 (downsampling start):** the kept rows now follow the code, and the shifted variants are printed.
- **5 (edge-of-window caveat):** stated.
- **6 (frequency labels):** the true bin frequencies are printed.
- **7 (habituation block):** the interval tables are printed.
- **8 (pupil):** a check of the eye clock and a time-in-session variant were added, and the sign of the difference reverses. The clock check shows a stimulus-locked response; it does not show a zero offset.
- **9, 10, 11:** stated or answered.

**Remaining, and bearing on a conclusion:**
- **Point 2, partly:** the CSD tie-break is now stated, but it has no minimum duration or display requirement. Single-sample or undisplayed sign flips decide fig3h and fig3i, and they set the direction of fig4h. I would require a sustained, displayed sink before counting an onset, or grade these claims as not reproduced.
- **The S3 fitting range:** adopting the code's range lifts fig3d to reproduced and lowers fig2e. The record should give the outcomes by reading, as asked above, and not rest on one adopted reading.

## 4. Critical findings

**Finding 1** (LFP timestamps 0, 24, 48 … in 7 mice of the cited version 0.240503.0152):
- **What the outputs show:** v1 cell 11 shows it for the V1 files of the 7 mice, and that 42 files of those 7 mice differ between the versions. The timestamps of the other probe files ("every probe file") are not printed.
- **Rating:** I would rate it major, not critical. The defect is plain from the values (a 24 s step at 1250 Hz, end times near 2.4e8), and it blocks the analysis for half the mice.

**Finding 2** (in the cited version, near-identical LFP in sub-645495/sub-645322 and sub-645324/sub-647836 while their stimulus tables differ):
- **What the outputs show:** v1 cell 11 shows r = 0.999–1.0 and 0.9985–1.0 on all six probes. Cell 10 shows that no two sessions share a stimulus sequence, and that in the pinned version the largest correlation between different mice is 0.844.
- **Rating:** critical is right. One recording is deposited under two subjects, nothing in the files shows it, and an analysis that takes the files as given would count it twice against the wrong stimulus tables.

No other finding is rated critical.
