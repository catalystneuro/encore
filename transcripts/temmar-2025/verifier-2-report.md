**Round-2 verifier report: temmar-2025-01 (LINK, DANDI:001201 0.261026.1912)**

The claims file has 24 claims and the attempt record has 24 outcomes, one per claim. No outcome is marked `assumed: true`.

### 1. Outcomes

I agree with all 24 stated outcomes. Some come with caveats, listed below.

- **Reproduced (16), agreed:**
  - Agreed without caveat: dataset-sessions, figs2-throughput-improves, fig2a-sbp-decline (unit reading b), fig2b-active-channels-decrease, fig2c-pr-decline, fig2c-ten-dimensions (reading a), figs4-bank-slopes, fig2e-trajectories-separable, fig3b-two-channels, fig3cd-tuning-stable (90° reading), fig3d-weak-channels-low-tcr, fig4a-sameday-stable, fig4bc-dof-accuracy.
  - fig4a-lstm-beats-rr: agreed. It is now stronger, because the LSTM also won on the 12 sessions with the highest RR R2 (32 of 32 in all). 280 sessions are still untested.
  - fig4d-cross-day-decay: agreed. It holds under one pair of readings, with margins of 0.017 and 0.003.
  - fig5a-multiday-short-term: agreed. It now holds under both normalisations (multiday [8]), but on only 12 of the 283 day-0 sessions.
- **Partially reproduced (4), agreed:**
  - dataset-contents: agreed on the criterion's literal wording.
  - fig2d-population-drift: agreed; the failure is marginal.
  - suppc1-shuffle-baseline: agreed.
  - fig2a-irregular-shifts: agreed, but fragile. The LSTM part fails by 0.001 on 3 sessions. Taking the percentiles over all 32 sessions with an LSTM (0.560 to 0.693, decoding [27]) would pass it.
- **Not reproduced (3), agreed:**
  - figs5-active-inactive-slopes: agreed under the criterion. The claims file probably misreads a dropped minus sign; this is with a reader.
  - fig3e-array-tuning: agreed under the criterion. The claims file follows Section 4.2 against Figures 3C and 3E; this is with a reader.
  - fig5a-long-term-decay: agreed under the criterion's starting values. The legend-start "pass" rests only on point estimates. The 95% intervals of the initial rates include zero in all four legend fits and overlap widely: training-day normalisation −2.09…0.28 against −0.62…0.25; test-day −1.53…0.33 against −1.91…0.84 (multiday [11]).
  - The criterion's starting values (0.374, 0.00365, 0.134, 0.140) have positive rates and look like the 5-session legend values reordered with their signs dropped. This may be another claims-file misreading; it is with a reader.
- **Blocked, too_large (1), agreed:**
  - fig5b-finetune: agreed. The run in the notes is not in the entry, so I cannot check it. The cost the notes give is understated (see 2).
- **Assumptions:** none is flagged. Choices that decide an outcome are disclosed as deviations or as readings the criterion names, and they are reasonable. Examples are Medial 1 and 2 taken as banks B and C, the 30-day baseline needing at least 3 earlier days, and the 12-of-283 day-0 subset.

### 2. Sentences the printed numbers do not support

The timing figures are wrong throughout. This run printed 207–223 s per LSTM fit, median 210 s, and estimated "4.5 h of fitting alone" for all 312 sessions (decoding [7]). It printed 207–215 s for the extra fits (decoding [9]) and 202–210 s for the multi-day fits (multiday [6]).

- **decoding [0]:** "takes 77 s (round 1) to 148 s (this run) … 312 of them … take 1.7 to 3.2 hours".
  - The same sentence is repeated in every LSTM deviation in the attempt record ("one fit takes 77 s (round 1) to 148 s (round 2) … 1.7 to 3.2 hours"). The record's fig4a-sameday-stable response says the same.
- **decoding [0]:** "An LSTM on every session from July to November 2022 (42 more fits, about 14 minutes)".
  - At the printed 210 s, four at a time, 42 fits take about 37 minutes.
  - This is the time argument for not running the test that would settle fig2a-irregular-shifts.
- **multiday [0]:** "75 s (round 1) to 150 s (this run) … 1415 fits, 7 to 15 hours".
  - At the printed 202–210 s, 1415 fits take about 20 hours.
- **Attempt record, fig5b-finetune:** "about twice that at round 2's fit times (148 s per 2000 iterations)".
  - The printed fit times are about 2.8 times round 1's 0.037 s per iteration, which puts the full run at about 18 hours.
  - "had not finished after 52 minutes" has no output in the materials, so I cannot check it.
- **decoding [22], and the record's fig4d notes:** "RR's mean R2 is -13.4 to -17.9 at the offsets past day 0".
  - These are the means over the 1–5 and 90–100 day windows only. The per-offset means reach −436.6 (decoding [21]).
  - My own round-1 "about −13" had the same flaw. This does not bear on the outcome.
- **README:** "on the 12 other sessions … for one claim".
  - The 12 sessions also enter the fig4a-sameday-stable correlation variant, the by-year LSTM medians and the fig2a-irregular-shifts window median. This is minor.

Everything else checks against the printed outputs: all "**Result:**" cells, the three Summary sections, the README, and the attempt record's notes and responses.

**Round-1 reasons:** the verification block states them accurately, mostly as close paraphrase. It leaves out my B12 (two-session days dropped from the test sets), my B14 (helper tests and leakage check) and the "195 s" point from B5. None of these affects a conclusion.

### 3. Round-1 points

**Resolved:**
- B3: Figure 5A under test-day normalisation is now run (multiday [8], [11]).
- B4: fits started from the legend's values are now run. The outcome still rests on the criterion's starting values.
- B2 / C: channel 47 is printed as Medial, B, row 5, col 5, which agrees with Figure S1.
- C, suppc1: per-session tolerance counts are now printed.
- C, fig4a: the LSTM is now run on the 12 sessions with the highest RR R2.
- B6 / C: baseline rates and the variant counting recording days are now printed. They confirm the shift rule does not single out the July–November 2022 period.
- B7, B8: the margins are now stated in the notes.
- B9–B11 and B13: recorded; none needed action.
- B1 and B2's claims-file questions: correctly passed to a reader.

**Remaining issues that bear on a conclusion:**
1. **fig2a-irregular-shifts:** the LSTM part is still decided by 3 sessions and 0.001. The 42 window fits were not run, and the stated cost of about 14 minutes is wrong against this run's times (about 37 minutes).
2. **B5, timing:** the subset justifications cite fit times (148 and 150 s) that this run's outputs contradict. The conclusion that a full run does not fit still holds, and more strongly, but the stated numbers need correcting in the notebooks and the record.
3. **fig5a-long-term-decay:** the outcome depends on the starting values. The criterion's values may misread the source, and the legend-start fits leave the initial rates undetermined (intervals include zero). It is fit on 12 day-0 sessions only.
4. **fig5b-finetune:** no part was tested. The 30 s arm is now about 2.8 times costlier than I estimated in round 1, so the block is reasonable.
5. **fig4d-cross-day-decay:** the narrow, single-reading pass is unchanged. It is disclosed.
6. **fig4a-lstm-beats-rr:** 280 of 312 sessions are still untested with the LSTM. The adversarial selection of the 12 makes this acceptable.
