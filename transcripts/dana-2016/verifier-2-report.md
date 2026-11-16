**Verifier report, round 2: Dana et al. 2016 (eLife 12727) on CRCNS cai-2**

The claims file has 35 claims, and the attempt record has 35 outcomes for the same IDs: 8 reproduced, 3 not_reproduced and 24 blocked (data_missing). One outcome, `fig4e-jrcamp1a-detection`, is marked `assumed: true`. Cell indices below refer to the re-executed notebook; a script cell was added, so the numbering differs from round 1.

### 1. Outcomes

| Claim | Agree | Note |
|---|---|---|
| screen-single-mutations-improved | yes | Cell 12: 230 and 58 improved, against 353 and 187. |
| culture-jrgeco1a-sensitivity | yes | Cell 15: ratio 8.57; decay 1.053 and 160 AP 1.098, both with p ≥ 0.01. |
| culture-jrcamp1-sensitivity | yes | Cell 18: 24.02 and 12.96; jRCaMP1a decays more slowly (3.13 against 1.15). |
| fig4-recorded-cells | yes | Cell 21: 11/6 and 10/5. |
| fig4d-event-counts | yes, now not_reproduced | Cell 26: isolation (a) is the main reading, as the claims-file header requires. The best reading of the claim gives 6 of 18, below the 10 needed for partial. Treating the script's noise rule as a "reading of the claim" stretches the criterion, which names only (i) and (ii), but nothing depends on it: a/i and a/ii give 5 each. |
| fig4e-jrgeco1a-1ap-detection | yes | Cell 33: 84.3% of 191. It no longer depends on the script segment: under "one reading", the claim's named readings alone also pass (a/ii/b, 76.3%, a clean combination). |
| fig4e-jrgeco1a-2ap-detection | yes | Cell 37: 100% of 62. 10 of the 36 named-reading combinations also pass. |
| fig4e-jrcamp1a-detection | yes, as recorded (reproduced, assumed) | Cells 41 and 43: 63.3% and 80.7%. This rests on **two** choices, and each one moves the rate into tolerance. (i) The jRGECO1a script's frame window is applied at 15 Hz. This is stated as the assumption and is weakly supported, because the script's rules do not give the paper's jRCaMP1a counts. Under the named readings no 1 AP rate passes (at most 41.6%), so the result would be partially_reproduced. (ii) `data_20150707_cell1_001.mat` is kept. Without it the 1 AP rate is 71.7 to 75.4% under every isolation reading, which also gives partially_reproduced. Choice (ii) is stated as a deviation but not marked as an assumption. Its justification is weak (see §2), and the event counts point the other way: 130 and 71 without the recording are nearer the paper's 135 and 65 than 158 and 83 with it. |
| fig4df-jrgeco1a-better-than-jrcamp1a | yes | Cell 46: 8 of 8 under the main reading. Clean named-only readings (a/ii/c) also give 8. |
| fig4g-jrgeco1a-faster | yes | Cell 50: 15 against 47 ms, 225 against 2300 ms, 155 against 312 ms under isolation (a); the script isolation gives the same direction. |
| fig4g-kinetics-like-gcamp6 | yes, now not_reproduced | Cell 54: 0 of 4 times pass under the main reading, and at most 2 of 4 in any of the 24 combinations. The Chen Table 3 values (142/45 and 550/179 ms) match the published table as I recall it. |
| 24 data_missing claims | yes | No change; the questions about the eLife source-data files are passed to a reader. |

### 2. Sentences the printed numbers do not support

- **Cell 44:** "…without it 9 cells remain where the paper reports 10, **so the paper's analysis included it**." The cell count does not show that this recording's events were used, and the event counts in cell 43 point against it. The attempt record's own methods_unavailable finding asks exactly this question ("Was data_20150707_cell1_001.mat … included?").
- **Cell 13:** "No variant rule printed above reaches the paper's counts." The record's notes ("Other rules do not reach them either") and the paper_inconsistency finding say the same. Cell 12 shows that RCaMP1h 334 (ratio > 1 with p < 0.05, and also over all rows) lies within 353 ± 35.3. The statement holds only for both counts together; for R-GECO1 no rule passes (207 is just above 205.7).
- **Record, fig4d notes:** "no noise rule tried gives 274." In cell 28, the 4 s bin gives 296, which is within 274 ± 27.4, though 4 s is not the legend's jRCaMP1a bin. Counting the duplicate file gives 258, also within.
- **Cells 53 and 55:** "the claim's half rise is compared with their time to peak, **as the criterion directs**." The criterion only says to compare with the values Chen et al. report; it does not name time to peak.
- **README:** "It takes about four minutes." Cell 57 prints 2.1 min.
- **Record, code_mismatch finding** (outside the required scope): "With the script's own threshold the jRGECO1a single-spike rate is 60.8%." No cell prints 60.8%. Cell 33 prints 60.7%, and that is under isolation (a), not the script's isolation.

All other sentences in the conclusions, the Summary, the README and the record notes match the printed outputs. The verifications block gives my round-1 reasons in my own words, and the sentences added to some reasons come from my problems 1, 3 and 7 and section C.

### 3. Round-1 points

**Resolved:**
- 1: isolation (a) is now the main reading.
- 2: resolved for the jRGECO1a and fig4df claims, which pass under the claim's named readings; it remains only as the stated jRCaMP1a assumption.
- 4: clean tallies are now given.
- 5 and 6: the limits are stated in the conclusions.
- 7: passed to a reader.
- 8: the scripts are printed (cell 24). I checked the "script" rules against them: 1 s before and 0.8 s after, a spike on each side, the 3.15e6 cutoff, 10 frames before to 20 after taken from the 70-frame window with tenfold interpolation, F0 from samples 1 to 100, the |dF/F0| 0.3 noise limit, the 99th percentile, and d′ reading (i). All match.

**Remaining, bearing on a conclusion:**
- **fig4e-jrcamp1a-detection** depends on both the assumed frame window and keeping `20150707_cell1_001`. Either change alone makes it partially_reproduced. The second choice should be marked as assumed, and the cell 44 sentence corrected.
- **New: the event alignment in the "script" segment differs from the script, and this is not stated.** `cai2.segment_traces` aligns on the ephys time stamps. The script uses sample index / fs + the first frame time, which places events about 16 ms later for jRGECO1a and about 33 ms (half a frame) later for jRCaMP1a, and 0.286 s later in `data_20150804_cell5_002.mat`. The clock check (cell 8, lag 0) supports the notebook's choice. Still, the main reading is not exactly the script's segment, and its effect on the jRCaMP1a 1 AP rate (63.3%, against a lower bound of 58.5) is not shown.
