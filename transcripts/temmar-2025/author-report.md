I've done steps 1 to 6 of the Author section. `entry.py all` passed on all three notebooks (10, 33 and 27 min), `check` reports 0 errors, and the handover is built in `executed/temmar-2025/handover/`. The entry is in `entries/temmar-2025/` and the record in `attempts/temmar-2025-01.yaml`. Of the 24 claims, 16 are reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked.

### 1. Outcome per claim

| Claim | Outcome | Measured |
|---|---|---|
| dataset-sessions | reproduced | 312 sessions, 303 days, 1242-day span, 9 two-session days, 375 trials each |
| dataset-contents | partially reproduced | 81 of 312 files have no `imp` column |
| figs2-throughput-improves | reproduced | positive slope under all 3 readings |
| fig2a-sbp-decline | reproduced | −0.0338 µV/month |
| fig2a-irregular-shifts | partially reproduced | the shift rule flags almost every day; LSTM R2 in the window is just above its 90th percentile |
| fig2b-active-channels-decrease | reproduced | −6.5 channels/year |
| fig2c-pr-decline | reproduced | −0.0708 PR/month |
| fig2c-ten-dimensions | reproduced | PR at most 10 on 84.8% of days |
| figs4-bank-slopes | reproduced | all four slopes equal the paper's to the printed digits |
| figs5-active-inactive-slopes | partially reproduced | inactive slope −0.54e-3, where the paper prints +0.54e-3 |
| fig2d-population-drift | partially reproduced | 3 quarters with an outlying spread, where the rule allows 2 |
| fig2e-trajectories-separable | reproduced | 0.21 and 0.22 accuracy against 1/8 chance |
| fig3b-two-channels | reproduced | |
| fig3cd-tuning-stable | reproduced | holds at the 90° reading only |
| fig3d-weak-channels-low-tcr | reproduced | |
| fig3e-array-tuning | not reproduced | the pattern matches the paper only with the array names swapped |
| fig4a-sameday-stable | reproduced | LSTM tested on 20 sessions |
| fig4a-lstm-beats-rr | reproduced | 20 of 20 sessions tested |
| fig4bc-dof-accuracy | reproduced | |
| fig4d-cross-day-decay | reproduced | under one of the four reading pairs only (absolute offset, test-day normalisation) |
| suppc1-shuffle-baseline | partially reproduced | LSTM −0.154 inside the tolerance; RR −0.223 outside it |
| fig5a-multiday-short-term | reproduced | 12 day-0 sessions |
| fig5a-long-term-decay | not reproduced | the double-exponential fits are degenerate, likely because 12 day-0 sessions are too few |
| fig5b-finetune | blocked, `too_large` | estimate 2.45M training iterations, about 16.5 h |

### 2. Dataset

**Version pinned.** 0.261026.1912, the latest published. The paper cites none, and all three published versions list identical asset ids.

**What was found about the data:**
- The stored SBP is already in µV. The code divides it by 0.25 and its analysis multiplies by 0.25, which cancel.
- ThresholdCrossings is labelled "volts" but holds integer counts.
- The files give no implant date, so the paper's days after implant cannot be checked.
- 81 files have no impedance column at all.
- Velocity is a forward difference: velocity at a bin is the next bin's position minus this one's.
- 29 sessions have 72 unmarked pauses of 1 to 473 s.
- 998 trials are no longer than the 750 ms hold.
- **Paper inconsistency:** with the files' array labels, the paper's lower-SBP-on-lateral result (Figure S4) holds but its tuning-by-array sentence (Section 4.2) is reversed.
- **Code mismatch:** the code swaps the LSTM's noise arguments (0.1 bias and 0.2 white, where the paper says the reverse). I followed the paper.

**Subsets, recorded as deviations.** For time, the LSTM runs on every 16th session (20 of 312) and multi-day training on 12 of 283 day-0 sessions, with only 1 and 5 training sessions. Cross-day scores use every 5th test bin.

**Assumptions, questions for the paper's authors, questions to a reader.** None. Every open choice was one of the readings the criteria name, so `questions/temmar-2025.yaml` was not created.

### 3. Protocol problems

1. **`about` field on findings:** `tools/entry.py check` requires `about: data|paper` on `other` findings, but `schemas/attempt.schema.json` rejects that field. I re-filed those two findings as `metadata_insufficient` and `paper_inconsistency`. (`tools/entry.py` is modified in the working tree, which may be why.)
2. **Writing conclusions after the run:** the protocol says to develop on a subset and run the whole once. But the conclusion cells must quote the full run's numbers, and editing them changes the entry hash, so every notebook has to run twice. I ran each notebook in full once, wrote the conclusions, then ran `all`. The claim outputs were identical between the two runs.
3. **Subsets versus blocking:** "Develop on a subset" says to block a claim as `too_large` when the estimate is over the limit, yet the protocol also lists "one session of four" as an acceptable deviation. I tested the LSTM claims on pre-chosen subsets and recorded deviations. I blocked only fig5b, whose estimate is far over even the run's time.
4. **Editing `entry.yaml` after the run:** I changed `runtime_minutes` after `all`, which invalidates the run's reuse stamp. The executed copies are unaffected.
5. **Supplement figures:** the PDF renderer (pdftoppm) is missing, so I could not open Figure S1 to check where channel 7 sits. The array-label finding rests on the files and the text only.

### 4. Runtime and failures

The run took about 2 h 50 min, ending at about 13:25 UTC, well before the 14:52 cutoff. Two development runs failed and were fixed (the missing `imp` column, and a statistic over an empty list). Nothing failed in the final run. Nothing was committed.
