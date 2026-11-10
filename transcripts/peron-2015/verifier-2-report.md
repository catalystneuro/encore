**Verifier report, round 2: peron-2015-01 (Peron et al. 2015, CRCNS ssc-1)**

**1. Outcomes**

The claims file has 43 claims, and the attempt record has 43 outcomes covering the same IDs. One is reproduced, one is not_reproduced, and 41 are blocked: 22 data_missing, 18 metadata_insufficient and 1 methods_underspecified.

- **results-trials-per-session: reproduced.** I agree. Cell 28 gives 290.2 pooled and 272.5 as the mean of per-mouse means, both inside [174, 316]. It is weak evidence (5 sessions from 3 of 8 mice), and the record now says so.
- **results-whisking-amplitude: not_reproduced.** I now agree; in round 1 I said partially_reproduced. In cell 33 every listed reading is still outside [42.2, 68.8] after removing only the artefacts: (a) 72.4 or 71.9, (b) 28.6 to 29.0, (c) 26.6. The criterion's "within tolerance under one reading" rule therefore gives not_reproduced. The miss is narrow, though:
  - Reading (a) falls steadily as the threshold drops: 74.1 at 88°, 72.4 at 85°, 70.3 at 80°, 67.4 at 70°.
  - The mean of per-mouse medians is 68.6, which is inside.
  - Multi-sample jumps are not removed by either artefact mask (see section 3).
- **The 41 blocked claims:** I agree with each one. Cell 7 now shows that no identifier or description field carries a layer, class or column label, so the M6 blocks stand. For methods-event-detection I accept methods_underspecified over my round-1 data_missing, given the protocol rule the record cites. Either way the outcome is blocked.
- **Assumptions:** the record has no `assumed: true` entries. The choices the whisking outcome rests on are all stated as deviations: the 6–30 Hz band, valid whisker trials only, and the poleInReach epoch. None of them changes the outcome (cell 31 shows all bands; cell 33 shows the artefact variants). They are reasonable.
- **Claims file:** I found no misreading. Its note that the degree values are "garbled in the extraction" is only partly true. Only the degree signs are garbled; the numbers 20, 55.5 and 13.3 are legible in the text (paper line 188). This does not affect the criterion.

**2. Sentences the numbers do not support**

- **"71.7 to 74.1 with other thresholds"** (cell 34; record notes for results-whisking-amplitude; record's response to round 1). Cell 33 prints 70.3 for the |angle| > 80° threshold. That value is outside the stated range, and the sentence hides the steady fall toward the bound described above.
- **"Tracking errors do not explain the miss"** (cell 34; record notes). This holds only for the artefact types that were removed: ±90° samples and 1–2-sample spikes. Cell 33 itself shows 3-sample jumps (−24.1, 72.8, 72.8, 72.1, −23.1) that the spike filter misses. The mouse that drives the miss, an229717 (mean 91.6–92.8 after cleaning, against 70.1 and 54.1 for the other two), has spikes in 152 of its 183 trials.
- **"Most of reading (a) is real whisking"** (cell 34). Only partly supported. The an229717 median of 87.2 does not move when 1–2-sample spikes are removed, but the multi-sample errors are untested.
- **"holds for every full-sweep measure (29.0 to 77.0)"** (cell 34; record notes). Reading (b) without spikes is 28.6 (cell 33). This is minor; the "larger than about 20°" conclusion still holds.
- **Summary, cell 35, last bullet.** It lists ±90° jumps and wraps but not the multi-sample jumps that the record's finding lists. This is an omission, not a wrong number.
- **Record, fig2e-fraction-imaged ("45 TIFFs and nothing else").** No printed output supports this; cell 6 says it was "not run here".

Everything else checks against the printed outputs:
- Cells 29, 34 and 35.
- The README: the 18, 7 and 14 group counts; 74.7, 29.0 and 26.9; 72.4, 29.0 and 26.6; 53.7.
- The record's notes and findings: 26,761 of 108,374; 72%, 20% and 63%; 12.5 min to 2.4 h; 1,443 trials; 21 of 25 subvolumes; 0.0009 against 0.0083; 146 GB; 0.06%; 179.8.

**My round-1 reasons in the record:** they are stated in my own words for every claim. For results-whisking-amplitude the reason is condensed but faithful. The verification block's "42 of 43 agree" is correct: the only outcome disagreement was whisking, and methods-event-detection is counted as agreeing on outcome (blocked), with a different blocked_by.

**3. Round-1 points**

Resolved:
- Problem 1: artefact-only reading (a) is computed, 72.4.
- Problem 2: edge-trimmed (c) is 26.6, and twice it is 53.2.
- Problem 3: the outcome now follows the strict criterion.
- Problem 4: the clock issue is now a finding and a summary bullet.
- Problem 5: cell 0 and the figs3d notes give the raw-TIFF route.
- Problem 7: the representativeness caveat is now in cell 29 and the notes.
- C1: cell 7.
- C2: cell 33.
- C3: cell 33.
- C4: cell 11.

Problem 6 was passed to a reader through the questions file, which I cannot see. C5, the contents of the imaging tar, is still unshown and only bears on the wording of the fig2e note.

What still bears on a conclusion:
1. **results-whisking-amplitude.** Reading (a) with multi-sample jumps removed has not been computed. A wider running-median window would be one way to remove them. The miss is 3.6° above the bound, it moves with the threshold, and it is driven by an229717, so this check could move the outcome.
2. **The "71.7 to 74.1" range** in cell 34 and the record needs correcting to include 70.3. The record should also state that reading (a) falls steadily with the artefact threshold.
