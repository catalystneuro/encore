# Round-2 verification: Gillespie et al. 2024 (eLife 90944), attempt gillespie-2024-01

The claims file has 35 claims, and 26 of them are `data: elsewhere`. The attempt record has 35 outcomes: 3 reproduced, 7 partially reproduced, 2 not reproduced and 23 blocked (`too_large`).

- **Claims on 000115 (9):** 5 tested and 4 blocked.
- **Data-elsewhere claims (26):** 7 tested on 000629 (rats 2 to 4 only) and 19 blocked.

The notebook's cell indices have changed since round 1. Every cell number below refers to the re-executed notebook.

## 1. Outcomes and assumptions

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| control-cohort-trial-counts | reproduced | Yes | Cell 21. The assumption is the trial parser written here, and it is stated. Cell 3 now shows only 3 control trials with a withdrawal over 200 ms. |
| control-decode-counts | partially_reproduced | Yes | Cell 24: 3 of 4 rats within tolerance for both 4E and 4G. The assumption is stated. |
| fig2s1h-control-dwell-increases | partially_reproduced | Yes | Cell 27: under leaving reading (a) 3 rats have positive r, under reading (b) 4 do. `assumed` was removed, but the trials still come from the written parser, as in the two claims above that keep `assumed: true`. It should be restored. |
| fig3a-control-speed | reproduced | Yes | Cell 30. The stated assumptions (smoothing, parser) are reasonable. |
| fig5s1-control-search-efficiency-increases | reproduced (assumed) | Yes | Cell 33. The assumption about task-phase rules is stated. |
| blocked: fig2s1c-control-prereward-swr-counts, fig4g-control-replay-glm, fig4s1 control part | blocked | Yes | |
| blocked: fig2s1f-control-rate-increase, fig2b-control-timecourse | blocked | Accept, with a reservation | Now based on a measured rate (cell 19: 180 s of 10 tetrodes in 110 s; two epochs per rat about 1.8 h in four processes). Three gaps: <br>• The "about 1 h for one epoch per rat" figure for fig2s1f is derived and not printed. <br>• The notebook time limit is not in my materials. <br>• "A run of one session … did not finish within 60 min" is shown by no output. |
| fig1s1c-prereward-dwell-matched | partially_reproduced | No; see below | |
| fig2e-postreward-dwell | partially_reproduced | Yes | Cell 39: the NF/control inset ratio is 0.36 to 0.39 under every reading. |
| fig3a-speed-below-immobility | partially_reproduced | Yes | Cell 42. The 0.2 cm/px scale is stated as an assumption, and the margin is given. |
| fig5a-search-efficiency | not_reproduced | Yes | Cell 47: the delay model gives p = 0.60 to 0.80 under reading (a) and 0.062 to 0.14 under (b). |
| fig5b-redundant-search-balanced | not_reproduced | Yes | Accepting the author's rule: the criterion names no partial level. |
| fig5c-repeat-accuracy-unchanged | partially_reproduced | Yes | Cell 53. |
| fig5d-repeat-errors-balanced | partially_reproduced | Yes | Cell 56. |

**fig1s1c and fig5b are judged by opposite rules.** For fig5b the author argues that the criterion "names no partial level", so one rat failing means not_reproduced. The fig1s1c criterion also names no partial level ("Reproduced when … less than 10% in all four rats"), yet the record calls it partially_reproduced with 2 of 3 rats within 10%.

- Applying the author's own fig5b rule, fig1s1c is not_reproduced. That is my outcome.
- The other reading of the claim fails too. With the pre-reward period started after the last withdrawal, bernard moves further out, to 16.1% (cell 36).
- The two claims should be judged by the same rule.

**The "matched" plateau decides fig5b.** fig5b rests on the "matched" plateau reading. For gus that reading is 5 days, below the Methods' 7 to 10. Under last7 and last10 no rat is significant (cell 50). The record says the outcome rests on the epoch selection, but not that the adopted reading falls outside the Methods' range for this rat.

## 2. Sentences the outputs do not support

1. **Cells 14 and 43.** "the x range of the head positions per run epoch is wider in 000629 than in 000115" and "The x range … is wider in 000629 at the assumed scale (median 112.6 cm, largest 158.7) than in 000115 (median 115.7, largest 119.2)". Cell 15 prints 000629 [105.8, 106.9, 112.6, 116.6, 158.7] against 000115 [107.6, 112.8, 115.7, 117.9, 119.2]. The median range in 000629 is smaller; only the spread and the maximum are larger.
2. **Finding 5.** "the scale of DANDI:000115 (0.2 cm per pixel) gives the same maze size". This contradicts cell 15. It also contradicts the record's own fig3a deviation ("the data do not confirm it"). The author said this sentence was corrected; it was corrected in the notebook but not here.
3. **Summary (cell 58).** "about 1 to 9 TB of streaming per cohort". Cell 19 prints 1943 GB for one channel and 16.8 TB for decoding in 000629, so the upper figure for that cohort is about 17 TB.
4. **Cell 34 and the fig5s1 notes.** "too few to move the correlations" / "does not bear on the result". The 39 carried-over search trials are printed, but the correlations are not re-run without those 8 epochs. The statement is plausible but not shown.
5. **fig3a-speed-below-immobility notes and cell 43.** "neurofeedback medians at most 2.17 cm/s" is shown only for the matched plateau (cell 42 prints per-rat medians only for that reading). The text applies it more widely.
6. **Finding 1 and the fig2s1c notes.** The groups are given as "ca1, bad_ca1, reference, dead or lost" and "about 20 of 32". Cell 9 shows ca1 23, bad_ca1 4, empty 3, can1ref 1, lost 1. No "dead" group appears, and ca1 is 23.
7. **fig2e deviation.** It says the leaving time is "adopted (assumption, see fig2s1h-control-dwell-increases)". fig2s1h no longer adopts a reading.

Every other number in the "**Result:" cells, the Summary, the README and the notes matches the printed outputs. I checked trial and epoch counts, percentages, r and p values, ratios, mixed-model coefficients, the withdrawal counts, the carry-over counts and the DIO counts.

**My round-1 reasons are stated faithfully in my own words.** Two things to know when reading them:
- They cite round-1 cell numbers, which no longer match this notebook.
- The fig1s1c reason merges my table entry with problems 1 and 2, which is fair.

## 3. Round-1 points

**Resolved:**
- Problem 2: withdrawals are counted (cell 3, cell 15) and the other start is run (cells 30, 36, 42).
- Problem 3: fig2s1h is now partially_reproduced.
- Problem 5: corrected in the notebook (but see item 2 above).
- Problem 6: the mixed models are now fit by ML (`fit(reml=False)`).
- Problems 7 and 8.
- Section C, all four questions: the withdrawal sizes, the scale distribution, the goal carry-over, and remy's raw DIO. Cell 12 shows repeated zero-length events at 137.074 s.

**Remaining, bearing on a conclusion:**
- **fig1s1c:** the outcome is inconsistent with the fig5b rule (section 1).
- **Problem 4:** the matched plateau is fitted to the paper's counts, and it alone decides fig5b. For gus it covers 5 days, against the Methods' 7 to 10.
- **Problem 9:** fig2s1f and fig2b stay blocked on a time limit I cannot see. One claimed failed run is not in any output.
- **Problem 1:** the protocol justification (Author, step 1.4) is not in my materials. The README and the Summary table list the 000629 claims in the same table as the 000115 claims, with no separate heading or count, so "counted apart" is only partly visible.
- **fig2s1h:** `assumed` should be restored.

I found nothing new in the analysis that misreads the claims file, and no new place where the claims file misreads the paper.

## 4. Critical findings

No finding in the attempt record is rated `critical`, and I would not raise any to critical.

- **Finding 4 (`major`, remy and gus DIO corrupted):** cell 12 shows it, e.g. 20743 home pump onsets in remy's day-33 epoch 04_r2 against 146 and 155 in bernard's run epochs. `major` is the right rating: it removes rat 1 from every analysis and is obvious from the values.
- **Finding 6 (`major`, plateau and NF port not marked):** cells 13, 15 and 17 support it. `major` is right.
- **Findings 1, 2, 3 and 5 (`minor`):** the ratings are right. Finding 5's statement needs the correction in item 2 above.
