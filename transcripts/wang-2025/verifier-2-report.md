**Round 2 verifier report: wang-2025-01**

The claims file has 30 claims and the attempt record has 30 outcomes, one for each claim. 2 are reproduced, 1 is partially reproduced and 27 are blocked as data_missing.

**1. Outcomes and assumptions**

| Claim | Record | I agree? |
|---|---|---|
| link-authors-deposit | reproduced | Yes. Cell 18: 16 of 16 areas found; 162 of 294 dataset annotations are in the map; 106 of 106 sessions match; the 5 SC038 days with two sessions each have 2 files. |
| data-scale | reproduced | Yes, which changes my round-1 rating of partially_reproduced. Cell 22: 13 non-nested structures, each with at least 100 units, in all 8 combinations of label, rate filter and session set. Cell 21: 154,948 `unit_quality` good units, 69,453 `classification` good. The count is one above the threshold and depends on splitting ALM from other isocortex. The criterion lists those two as separate areas, so the split is allowed. |
| fig6e-marker-clustering | partially_reproduced | Yes, with the same caveat as round 1. Cells 25–28: CH 6.83 against a null of 1.03 ± 0.42; p < 0.001; 4 nose-type and 5 jaw-type mice. Across all 72 variants CH runs from 3.52 to 7.91, and none is within 11.31–13.83. The criterion has no partial rule, so read literally the outcome is not_reproduced. "Partial" relies on the protocol's general meaning of an effect that is present but weaker. |
| The other 27 | blocked, data_missing | Yes. Cell 14: 34 of the authors' 106 sessions have video and 72 have none in any version. For the 34 with video, the too_large reason is given in the notes. |

No outcome carries `assumed: true`. The assumptions the outcomes rest on are written as text in the deviations, and all are reasonable:
- the session AUC is the mean of the test-fold AUCs, with the pooled AUC run as a variant;
- the AUC is computed in 68 ms bins;
- ALM is split from other isocortex by probe target;
- the 2 Hz filter uses the whole-session `avg_firing_rate`.

**2. Sentences the printed numbers do not support**

- **Attempt record notes (all 27 blocked outcomes):** "reading the side view alone takes more than an hour a session (1.4 h at the rate of the final run, 49 h for the 34)". The final run prints **1.3 h** per session (cell 13) and **44 h** for the 34 sessions (cell 14). The 1.4 h and 49 h figures come from some other run. The conclusion does not change.
- **Summary (cell 34) and the fig6e notes:** these say "the 167 sessions that pass the clock check" form the variant. The variant actually decodes 166 sessions (cell 27, `n_sessions_decoded` = 166), because SC032_121719 is not decoded (cell 25). This is minor.
- **Finding 7:** it says "The Methods … give 105 and 106 sessions". The 105 is in the Results (Fig. 2c–e), not the Methods. This is trivial.

All other sentences check out against the printed outputs:
- **"Result:" cells 19, 23 and 29:** the per-mouse nose/jaw split (4 nose / 5 jaw / 2 even) in cell 26, the seed range 6.68–7.82, the variant range 3.52–7.91 with p at most 0.003, and the 35 sessions kept under both AUC readings.
- **Cell 33:** the pooled AUCs are within 0.007 of the fold-mean ones.
- **The rest of the Summary and the README:** 34/72 sessions with and without video, 71 files from 16 mice, the ×2 stretch, 92,769 good units with no location, and "27 claims".
- **The remaining record notes.**

**The record states my round-1 reasons faithfully, in my words.** This covers:
- data-scale points 1 and 2;
- point 3 on the block reason;
- points 4–6 on fig6e and fig6-marker;
- points 7–10, which are summarised in `reviewed`.

**3. Round-1 points**

| Point | Status |
|---|---|
| 1. Nested structure count | Resolved: each unit is counted once in its major Allen division, giving 13 (cell 22). The nested map gives 10 (cell 22). |
| 2. Good units with no location | Resolved: stated in cells 12 and 23 and in the notes. |
| 3. Block reason and the 106 × video cross-tab | Resolved: 34 with video, 72 without (cell 14). My estimate of 35–40 was slightly high. |
| 4. Marker-only parts of blocked claims | Resolved. The marker half of fig6-marker-vs-embedding-decoding is now computed (cell 32). The marker arm of fig2-ordering-across-methods is stated as computable but not run. The Google Drive embeddings are now excluded under a protocol rule, stated as such. |
| 5. Pooled vs fold-mean AUC | Resolved: both are run, with fold-mean as the main reading. |
| 6. Main session set | Resolved: the authors' 106 sessions are now the main set. |
| 7. Docstring stride | Resolved: the docstring now says every 20th frame (68 ms). |
| 8. Marker cleaning | Resolved: velocity is no longer taken across gaps between trial videos (`clean_marker`). The second flagged frame is kept, and that is stated. |
| 9. Synthetic checks | Nothing was needed. |
| 10. Wording in cell 0 | Resolved. |
| C. Zenodo member list | Resolved: every member and its size is printed (cell 15). |

What remains that bears on a conclusion:
- **fig6e may reflect the decoder, not the data.** The same marker decoder gives a response-epoch AUC of 0.754 ± 0.006 for the better of jaw and nose, against the paper's 0.88 ± 0.01 (cell 32). Mean delay-epoch AUCs are only 0.61 for the jaw and 0.59 for the nose (cell 25). So this decoder is weaker than the paper's, and the CH score of about half the paper's may come from that. Cell 29's "weaker than the paper reports" should be read as "weaker under this decoder". The question to the authors (finding 8) covers this.
- **data-scale is one structure above the threshold.** The margin depends on the ALM split. "ALM" here means isocortex units on probes targeted to ALM, so it may include neighbouring motor cortex. This is acceptable under the criterion but fragile.

**4. Findings rated critical**

Only finding **1** is rated critical. It concerns SC011 on 24–26 February 2019 and SC022 on 27–28 February 2019, where the marker timestamps advance 3.4 ms per frame but the frames are 6.8 ms apart.

- **The printed outputs show it.**
  - Cell 8: the tongue-after-go-cue contrast is negative in 5 sessions.
  - Cell 10: as deposited, the tongue is visible at 0.063–0.132 of lick events. The best fraction at any shift within 1 s is 0.484. Stretching the timestamps by 2 gives 0.999–1.0. These sessions have 934–946 frames per trial video, against a median of 1904.
  - Cell 11 states the conclusion.
- **Caveat:** "6.8 ms apart" is inferred from the ×2 stretch, not measured. These sessions have video in 0.231012.2129 (cell 14), which could confirm it directly.
- **The rating is right.** It is signals on different clocks: the marker time base is half as long as the trial table's, and nothing in the files labels it. The short videos are visible in the data but do not reveal the timing error. Any marker-to-event analysis of these sessions would come out wrong, although none of them is in the authors' 106.

A rating I would consider raising: finding 2 (SC026_080719, rated major). 117 trial videos do not match the licks, and there are 539 videos for 630 trials (cell 10). That looks like markers filed under the wrong trials, which would be critical by the definition. Since the cause is not established and the count mismatch is visible in the files, major is defensible. I would make it critical if the misassignment were confirmed.
