**Round 2 verification: 000579-tseng-2022-01 (Tseng et al. 2022, DANDI:000579)**

The claims file has 43 claims, and the attempt record has 43 outcomes, one for each claim. They break down as 9 reproduced, 5 partially reproduced, 1 not reproduced and 28 blocked (3 for missing data, 25 as too large). Five outcomes rest on an assumption (`assumed: true`): neuron-counts, lstm-choice-accuracy, visually-guided-rule-update, fig2f-latency-strategy and fig8cd-position-specific-decoders. Cell numbers below are positions in the re-executed notebook, not the round-1 numbering.

## 1. Outcomes

| Claim | Record | Agree? | Note |
|---|---|---|---|
| neuron-counts | reproduced, assumed | yes | Under reading b (sessions selected on fraction correct over all trials), all 9 counts are within tolerance (cell 16). The assumption is stated and reasonable: the cut that keeps 141 sessions is 0.659 (cell 14). |
| fig1d-switch-performance | reproduced | yes | Initial 0.226, end 0.727; 15% of bootstrap samples are at or below 0.7 (cell 20). The record says plainly how close the end value is to 0.7. |
| lstm-choice-accuracy | reproduced, assumed | yes | Every reading gives 0.766–0.792 (cell 23). The assumption that the stored predictions are held out is stated and cannot be checked from the files. |
| figs1h-lstm-beats-rl | reproduced | yes | p = 4.65e-22 and 1.42e-17; the LSTM leads in all 8 mice (cell 26). The inverse temperature sits at its cap of 50 in 50 folds, which could slightly handicap RL; this is minor. |
| fig1i-strategy-after-switch | reproduced | yes | Holds in all four readings (cell 31). |
| visually-guided-rule-update | not_reproduced, assumed | yes | The adopted forward reading gives p < 0.0001 and p = 0.0022 (cell 34). The record no longer treats the backward reading as support. The assumption is stated and argued from the Methods. |
| fig1l, fig1m, figs1m (photoinhibition) | blocked, data_missing | yes | — |
| fig2c-running-variability-after-switch | reproduced | yes | Cell 39. |
| fig2f-latency-strategy | reproduced, assumed (session selection) | yes | Every test passes under reading b. The p = 0.058 under reading a is stated as fragile (cell 43). |
| fig2g-choice-commitment | reproduced | yes | The variant without the current trial agrees (cell 47). |
| cue-biased-running-uncorrelated | partially_reproduced | yes | The two readings disagree: pooled r = 0.224, p = 0.0005; per-mouse slopes p = 0.35. |
| fig4h-activity-by-epoch | partially_reproduced | yes, changed from round 1 | The criterion's comparisons split. RSC is below A in feedback/ITI, and feedback/ITI is RSC's lowest epoch (both hold). RSC stem > arm and RSC stem > AM fail (cell 53). The claim file's rule for mixed results allows "partially". The part that fails is the claim's lead ("most active in the stem"), and only the all-neuron reading was run. |
| fig3q-cue-decoding | partially_reproduced | yes, with a caveat | V1 is highest in only 2 of 12 readings. But PM leads V1 by only 0.001–0.027, on 12–14 PM decoders from a subsample of 18 sessions. The subsample cannot decide V1 against PM, so the "partial" may be an artefact of subsampling (see 3). |
| figs5f-dynamic-choice-decoding | partially_reproduced | yes | Both values are 3–9 SEM outside the paper's, under every reading (cell 61). |
| fig4d-partial-correlation | partially_reproduced | yes | No reading has all three values within tolerance (cell 64). |
| fig8cd-position-specific-decoders | reproduced, assumed | yes | Every decoder drops with distance, p < 0.001 in every area (cell 67). The assumption is stated and reasonable: the paper has 698 of its 974 decoders at cue offset 0.76, but the files give that offset for only 6 of 142 sessions, so the files' cue delay is probably not the paper's offset. The 6 sessions that do match (in RSC, A, PM and MM) could have been decoded to test the claim file's own reading for those four areas. |
| 23 GLM claims, plus figs5l | blocked, too_large | yes | The lower bounds printed in cell 70 exceed the stated 30-minute limit even for 200 neurons (0.6 h). The design matrix is not public. figs5l is blocked because it depends on well-fit-neurons. |
| fig8g-shattering-dimensionality | blocked, too_large | yes | The estimate is now given: 3.9 CPU-h for one conjunction, a lower bound. |

## 2. Statements the printed outputs do not support

- **GLM and shattering costs.** The record's notes for all 23 GLM claims and figs5l, the "other" finding, and the responses to round 1 cite figures from a different run:
  - The record has 0.3 s per fit, "about 730 CPU hours", 2,000 neurons at 15 CPU-h (3.7 h), 200 at 1.5 CPU-h (0.4 h), and a "19-minute notebook".
  - Cell 70 prints 0.4 s per fit, 1,191 CPU-h, 24.3 CPU-h (6.1 h) and 2.4 CPU-h (0.6 h). Cell 72 prints 15.9 min.
  - For fig8g the record has "about 1 ms … about 5 CPU hours (1.3 h on 4 cores)"; cell 70 prints 0.81 ms and 3.9 CPU-h.
  - The conclusions do not change.
- **Decoder cost.** Cell 55 and the record's decoder deviations say all decoders take "about 2.7 CPU hours", with "a single session of about 650 neurons [taking] about 2 to 3 minutes".
  - Cell 56 prints 382 s on 4 processes for 18 sessions and 11,564 neurons. That is about 85 CPU-s, or 1.4 min, per session.
  - Scaled up, that is about 3.3–3.6 CPU-h, about 55 min on 4 cores.
- **Cue offset 0.76.** Cell 66 says the files mark "only 8 layer 2/3 sessions with that offset … none … in V1 or AM (printed with the decoder sessions)". The record's metadata_insufficient finding says the same ("8 of the 184 layer 2/3 sessions").
  - What cell 56 prints is 6 of the 142 sessions in the pool (RSC 2, visA 2, PM 1, MM 1).
  - The Summary (cell 71) correctly says 6 of 142.
- **"The 12 single-plane sessions".** This appears in the record's decoder deviations, its fig4h deviation and cell 55.
  - Cell 5 prints 13 single-plane sessions over both layers.
  - Cell 53 prints 8 such planes in reading b, which is also the 150 − 142 left out of the decoder pool.
  - The number 12 is never printed.
- **Cell 35 and the record's notes:** "under every reading both values are 2 to 5 times the paper's".
  - This holds for the all-trial readings (2.3–4.5×).
  - In the correct-only rows of cell 34, the normal-trial update is 0.076–0.080, about 10× the paper's 0.008. The correct-only rows have no paper values to compare, so "every reading" should say "all-trial readings".
- **Cell 51:** choice decoding in the second quadrant "rises with cue decoding". The printed values rise up to bin 3 and then flatten (−0.726, then −0.768 to −0.776). This part is reported, not judged.
- **README:** "about 20 minutes" against the printed 15.9 min. This is minor.
- Every other "**Result:**" sentence (cells 17, 21, 24, 27, 32, 40, 44, 48, 54, 59, 62, 65, 68), the outcome table in the Summary, the README table and the record's outcome notes match the outputs.
- **My round-1 reasons** are stated faithfully and in my own words in the record's verifications section. Its count of 38 agreeing and 5 disagreeing outcomes is correct.

## 3. Round-1 points

**Resolved:**
- **1 (decoders blocked as too large):** the four decoder claims are now tested, on a subsample.
- **2 (GLM subsample):** too_large is defensible under the stated 30-minute limit, but the cited numbers must be corrected (see 2).
- **3 (session selection):** reading b is adopted and stated as the assumption.
- **4 (visually guided update):** the forward reading decides the outcome, and the split by trial type and outcome is shown.
- **5 (fig4h epochs):** no frame of the feedback delay has a position, and the frame counts are printed.
- **6 (hboot is liberal near 0.05):** acknowledged in fig2f.
- **7 (sigmoid fit bias):** acknowledged.
- **9 (sign of stored rule_belief):** recorded as a finding.
- **10 (p = 0 printing):** p values are now printed as bounds.
- **11 (local reward rate):** a variant without the current trial is run and agrees.
- **Section C checks, all now printed:**
  - `is_switch` marks the rule change in 300 of 300 sessions.
  - `start_time` is maze onset.
  - The RL optimiser converged.
  - The magnitude gap in the visually guided update is in the stored belief itself.
- **8 (LSTM held-out assumption):** remains an assumption the files cannot settle. It is properly flagged.

**Remaining that bears on a conclusion:**
- **fig3q:** the "partially reproduced" rests on PM above V1 by at most 0.027, on 12–14 PM decoders. That is within what an 18-session subsample can resolve no better than a tie. Fitting all decoders would take about 55 min on 4 cores (by the notebook's own timing) and would decide the outcome. Until then, the outcome should be read as "V1 versus PM undetermined", not as a failure of the gradient.
- **fig8cd:** the cue reading of the claims file (sessions with cue offset 0.76) was not attempted. The 6 sessions that match were left out of the random draw.
- **fig4h:** the well-fit reading is not run, so even the parts that hold are tested under one of the two readings.
- **The cost figures in the record** (GLM, shattering, decoders) must be brought into line with cells 55, 56 and 70, since they are the stated basis for the too_large outcomes and for the decoder subsample.
