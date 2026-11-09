**Round-2 verification: Ito & Doya (2009) on DANDI:001641 (0.260922.0719)**

The claims file has 46 claims and the attempt record has 46 outcomes, in the same order. The record gives 23 reproduced, 7 partially reproduced, 8 not reproduced and 8 blocked (7 methods_underspecified, 1 metadata_insufficient). Cell numbers below are those of the re-executed notebook (155 cells), which differ from round 1's.

## 1. Outcomes and assumptions

**Agreement.** I agree with all 46 outcomes. They match my round-1 outcomes in 45 claims. The one change is fig9-action-value-information-low, now partially reproduced (cell 150) instead of reproduced. That change is correct: the O13 (b) estimate in `_pf_session` now takes the particle mean after the Q update with a(t) and r(t), and with it flatness fails in 48 of 96 readings (cell 149).

**Assumptions.** No outcome carries `assumed: true`. The O1, O3, O8 and O14 readings that the findings call "assumed" were all run, and claims whose readings disagree are blocked, so no outcome rests on them. Three things should still be stated:
- **Partial rule.** fig5-variable-models-best and fig9-action-value-information-low read the claims file's rule as "partial when the partial condition holds under every reading", although some readings give reproduced. The claims file's general rule says to block when readings disagree. The reading is reasonable and applied consistently (fig5-fq-dfq-beat-all-models is blocked because its partial condition fails in some readings). But it is an interpretation and should be marked as an assumption.
- **Initial value Qi(1) = 0.5.** It feeds the measured local-matching-law value of fig5-constant-models (0.5064). It also gives one of the 8 matching values in table2-ml-parameters, which would be 7 under Qi(1) = 0, as the claims file fixes it. Neither outcome changes.
- **tone-discrimination-errors.** The tone-A numerators bracket the paper's value: 0.27% from result codes, 0.56% from events with tones of at least 1 s (cell 19). Even the 1 s filter is only an upper bound, since cues run 1–2 s and a tone cut short after 1 s still passes. So the not_reproduced outcome rests on the tone-B part, which is 0.97–1.11% under every numerator against 0.73 ± 0.073. The record should say so. Its own metadata_insufficient finding, that the paper's rates "could not be recounted", sits awkwardly with not_reproduced.

## 2. Sentences the outputs do not support

- **Cell 20:** "The paper's 0.39% and 0.73% lie between these." This holds for 0.39% only. 0.73% lies below all three tone-B values (0.974–1.110%).
- **Cell 64, and the record notes for fig5-variable-models-best:** "in the 8 readings with the update O1 (b) and clipped drift O5 (b), DF-Q (variable) is highest." Twelve readings have O1 (b) and O5 (b). DF-Q leads only in the 8 on splits (a) and (b); on split (c), F-Q leads (cell 63).
- **Record notes for table2-ml-parameters:** "with Table 2's F-Q and DF-Q sigmas within 0.0005 of the best training score". This is true under O5 (a). Under O5 (b), F-Q is 0.0008 below (cell 74). Cell 75 correctly limits the statement to O5 (a).
- **Record finding (Q update):** "assumed here, as it reproduces Table 2 and Table 3". Table 2 is not reproduced under O1 (a): 6–8 of 16 values (cell 74).
- **Record finding (sigma search):**
  - "varies by under 0.003" leaves out the collapsed grid point, standard Q at (0.02, 0.10), which scores 0.398 (cell 54).
  - "the best sigma_alpha lies at the top of that grid" refers to a 0.0025–0.04 range, but the grid ran to 0.08, and F-Q under O5 (b) is best at 0.08.
- **Summary, cell 154, and the cue-tone finding:**
  - "The cue tone stops when the rat leaves the center hole early" is stated as fact. The notebook shows only short tones in 96 trials, and cell 20 itself says "probably".
  - "The trial table's tone offset then equals the exit" is not shown by any printed output.
  - "cue duration ... tells such trials apart" is only partly true, since cues of 1–2 s can be cut short after 1 s.
- **Minor:**
  - "6 to 7% of the peak" (cell 147 and the record) is 5.6–6.7% in cell 146.
  - The table2 response says the 5000-particle best sigmas "differ from the 1000-particle ones". They do in 5 of 6 cases; standard Q under O5 (a) is unchanged at (0.02, 0.07).

Every other Result sentence, the README table (its counts sum to 46 and match the record) and the other notes agree with the printed outputs.

**Round-1 reasons.** The attempt record states my round-1 reasons faithfully and with no distortion, including problems 1–3, 5–7 and 9–11 where they apply.

## 3. Round-1 points

**Resolved:**
- **1 (filter seeds):** six seeds were run on split (a) under every O1 and O5 reading (cells 53, 66, 68). Seed noise does not decide any outcome.
- **3 (local matching law):** the main table shows Qi(1) = 0 next to the labelled assumption.
- **4 (tone durations):** tone durations and a recount keeping tones of at least 1 s were added.
- **6 (QL/QR MI runs):** all four F-Q runs are now used.
- **7 (O13 b estimate):** fixed, and the outcome changed.
- **10 (one-sided column):** added.
- **11 (`mirror_avg` pairing):** fixed.
- **Section C:** every item was run, including the Table 1 and Table 2 likelihoods at the paper's values, the scores at the Table 2 sigmas, and the local-matching-law Wilcoxon tests under each initial value.

**Partly resolved:**
- **2 (sigma search):** the 5000-particle wider grid covers split (a) and O1 (a) only. Under O5 (b), F-Q's best σα is still at the grid edge (0.08). At those sigmas F-Q and DF-Q tie under O5 (a) (0.5372 each). Neither fig5-variable-models-best (partial either way) nor table2-ml-parameters (fails on the constant parameters) changes.

**Remaining, bearing on a conclusion:**
- **Problem 5, fig9-reward-information:** the criterion's "below threshold before entry" may misread the paper, as reported in round 1. This is with a reader.
- **Problem 9, table3-parameter-averages:** the criterion requires every O1 reading while the Table 1 and 2 criteria treat O1 as the parameterization. This inconsistency alone blocks the claim, and is with a reader.
- **tone-discrimination-errors:** the outcome rests on the tone-B part (section 1); the tone-A count is undetermined.
- **Partial rule:** the reading applied to fig5-variable-models-best and fig9-action-value-information-low should be recorded as an assumption.

Problem 8 (drift in the MI threshold) remains and follows the paper's method; it does not bear on an outcome.
