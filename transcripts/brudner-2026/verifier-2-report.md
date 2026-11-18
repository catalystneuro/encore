**Verifier report, brudner-2026, round 2 (DANDI:001871 @ 0.260630.1657)**

I counted from the claims file and the attempt record. The claims file has 22 claims and the attempt record gives 22 outcomes:
- 1 reproduced (figs5c)
- 3 partially reproduced (fig5f, fig2c, fig2e)
- 2 not reproduced (fig5e, figs1fg)
- 16 blocked: 15 `other` and 1 `metadata_insufficient` (methods-intensity-right-bias)

Four outcomes carry `assumed: true`: fig5e, fig5f, figs5c and fig2c.

### 1. Outcomes

| Claim | Agree? | Assumption stated / reasonable |
|---|---|---|
| fig5e-cue-betas, not_reproduced | **Yes** | Stated. The outcome does not actually depend on it. With the SI onset, smoke-1a passes 0/24 readings and smoke-2a passes 16/24. With the event start, smoke-1a passes 8/24 and smoke-2a 0/24. Both sets together pass 0 (cell 14). No file set or onset gives the result in every reading, so the claim is not reproduced under any of them. The "resting on an assumption" label is over-cautious, not wrong. |
| fig5f-cue-dominance, partially_reproduced | **Yes, conditionally** | Stated, and reasonable: the dandiset description, the session descriptions and the match to the published tables (cell 12) all point to smoke-1a. Two other readings would make it reproduced: smoke-2a with the SI onset at 150–210 (0.937 / −0.717), and smoke-1a with the event start at 160–200 (0.879 / −0.701). The evidence that favours smoke-1a (the table match) comes from the event start, and under that onset this claim is reproduced. So the outcome depends on the onset question that was sent to the reader. With smoke-1a and the SI onset the signs hold in only 4 of 6 readings (cell 19), so "signs hold" is not true in every reading. |
| figs5c-turn-angles, reproduced | **Yes, only as conditional on the added reading** | Stated. Under both readings the claims file names, the medians are about ±21°, outside tolerance (cell 22). The outcome rests entirely on the author's bounds: the 20% crossings on the rising and falling edges. The paper's own turn detection (Fig. S5A) measures peak width at half height. Events 5–9 frames long that start a median of 4 frames after the 20% crossing are consistent with half-height bounds. If the deposited events are the paper's turn events, then the ±21° is the paper's own measure and the claim fails. A half-height reading was not tested. The assumption is plausible but chosen after the event bounds failed, so it is weak. |
| fig2c-complex-auc, partially_reproduced | **Yes** | Stated, and reasonable: a sum AUC of exactly 0.5 with SD 0 and a sum weight of 0 point to mirror balancing. Under the two samplings the claims file names, the sum AUC is 0.620–0.663, so the outcome would be not_reproduced (cell 40). The record says so. |
| fig2e-complex-weights, partially_reproduced | **Yes** | No assumption is needed. Every reading gives the ordering; the gradient weight (0.231–0.281) is out of tolerance under every reading. |
| figs1fg-resolution-robustness, not_reproduced | **Yes** | Across all six readings, the lowest motion r over delays 1–4 is 0.729–0.784, below 0.8 (cell 28). |
| methods-intensity-right-bias, blocked (metadata_insufficient) | **Yes** | Both conditional outcomes are now given (cell 17). |
| figs1-antisymmetry-index, figs1-temporal-statistics, blocked | **Yes** | The parts that can be computed are now computed (cells 33, 37). |
| The other 13 blocked claims | **Yes** | — |

**Places where the claims file may misread the paper (reported, not corrected):**
- **figs5c:** the claims file takes "the dataset's detected turn events" as the paper's turns. It does not consider that the deposited event bounds may differ from the paper's. It allows for this for the onset in fig5e but not for the turn bounds here.
- **fig5e:** the claims file says the code "selects smoke-2a" and that the criteria "follow the code". It does not mention the dandiset description, which says the smoke_1a_orig movie was the one analysed.
- **fig5e and fig5f use different rules:** fig5e takes "the outcome all readings give", while fig5f, whose readings are "as fig5e", takes "within tolerance under one reading". Under this mix the two can come out differently on the same turns.

### 2. Statements the printed outputs do not support

- **README:** "under these the complex motion cue does not reach significance." With smoke-1a and the SI onset, the motion p is 0.046 (below 0.05). With per-trajectory z-scoring it is 0.0046 and 0.013, so the 0.0046 case passes the criterion's 0.01 (cell 11). Those readings fail because the smooth motion term becomes significant (p 0.0079), not because the complex term does.
- **README and Summary (cell 44):** the published tables "are matched only by the smoke-1a files with the files' own turn start." smoke-1a with the SI onset at 160–200 is also within 0.45 SE (motion) and 0.09 SE (gradient), with max |ΔLL| 0.0036 (cell 12). "Closest" is supported; "only" is not.
- **Cell 15 and the record's fig5e notes:** "so the two sets do not differ by a flip convention." Cell 13 shows only that the projection-flip label does not reverse the sign within a set. In smoke-2a both the motion and the gradient coefficients have the opposite sign to smoke-1a (cell 11). That pattern is consistent with a sign or mirror convention that differs between the two sets as a whole, and nothing in the outputs rules that out.
- **Summary (cell 44), fig5f row:** "signs hold … with the SI onset." They hold in 4 of 6 readings; at 150–210, as stored or pooled, the complex value is +0.114 (cell 19).
- **Summary (cell 44), fig5e row:** "holds with the dataset's turn start, smoke-1a, at 160 to 200 degrees." It holds there only as stored or pooled; with per-trajectory z-scoring it fails (cell 14).
- **Summary (cell 44):** turn events "end before the turn does." No output shows where events end relative to the falling edge.
- **Summary (cell 44) and record inputs/findings:** the port "gives the code's numbers on the same files, checked in preparation." No output shows this. Cell 12 compares with the published tables only.
- **Cells 26 and 32:** the provenance strings "bgsub_gauss3_fullslice_p001_p99" and "bgsub_gauss3" are not printed anywhere in this notebook. Also in cell 32: "the same factor for the gradient and for motion." The slopes are 0.169–0.172 (gradient) and 0.196–0.221 (motion), and the motion fits have r of only 0.24–0.46 (cell 31). "Similar" would be supported; "the same" is not.
- **Cell 29 and the record's figs1fg notes:** the centered and correlator forms "give the same correlations to three decimals." They differ by 0.001 in several cells at 8 and 15 frames, e.g. 9 px at 8 frames is 0.534 against 0.533 (cell 28).
- **Record, fig5e notes:** "2846 turns, 1011 trajectories." Cell 11 prints 1010.
- **Record, findings:** events "last 5 to 9 frames." 8 events last 10–11 frames (cell 7). Also, the y values "768 to 814 mm": only the maximum (813.6) is printed (cell 5).
- **Record, findings, and cell 8:** the lag scan between `signal` and the movie "found no consistent peak." This was not run in the notebook.
- **Unchanged from round 1:** "Dryad answers 401" is not backed by any output.

All other numbers in the Result cells (15, 20, 23, 29, 38, 41), the Summary, the README and the record's notes match the outputs.

**The verifications block:**
- The round-1 reasons are stated accurately and fairly, mostly close to my wording. Folding problem 9 into the figs1fg reason, and problem 8 into the fig2c reason, is acceptable.
- The `reviewed:` field says the conclusions and summary were removed from the notebook I reviewed. That is inaccurate: in round 1 I reported that cell 26 still held the author's "Result" text (round-1 problem 12).

### 3. Round-1 points

**Resolved:**
- **Problem 1 (complex file set):** smoke-1a was adopted with evidence; fits per projection flip were added; every reading was compared with the published tables.
- **Problem 2 (onset bug):** the rule is now signed. The old rule's run reversed in 0.2% of turns, and no result changed.
- **Problem 3 (fig2c sampling):** the assumption is stated, and the record notes that the claims file's samplings would give not_reproduced.
- **Problem 4 (smoothing for motion):** smoothing was run for motion too; the motion part still fails.
- **Problem 5 (figs1 parts):** the freestream and complex parts were computed.
- **Problem 6 (right bias):** both left/right mappings are evaluated.
- **Problem 7 (centerline row):** the row-571 variant was run.
- **Problem 8 (train/test overlap):** location-split mirror sampling was added and gives the same AUCs.
- **Problem 9 (backward difference):** the centered form is now the main form.
- **Problem 10 (heading and position frames):** documented as the code's behaviour.

**Remaining, bearing on a conclusion:**
1. **fig5f depends on the onset question sent to a reader.** smoke-1a with the event start gives reproduced; smoke-1a with the SI onset gives partially reproduced; smoke-2a with the SI onset gives reproduced. The record states this, but the README's one-line outcome hides it.
2. **Why smoke-1a and smoke-2a differ in sign is still unexplained.** A set-wide sign or mirror convention has not been excluded (see the overstatement in §2). The test I would want is the sign of the gradient and motion signals against the known plume geometry in each set, e.g. the mean `spatial_gradient` as a function of y about the centerline. This decides whether smoke-2a is a mirrored copy, and so which set's outcome stands for the paper.
3. **figs5c rests on the author's turn bounds.** It is not reproduced under the claims file's readings, and the half-height alternative suggested by the paper's own Fig. S5A was not run.
4. **fig2c rests on the mirror-balancing assumption** (stated; the outcome is not_reproduced without it).
5. **The README's significance sentence needs correcting** (§2).
