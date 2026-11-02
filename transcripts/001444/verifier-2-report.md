# Round 2 verifier report: 001444-doherty-2025-01

## 1. Outcomes

The claims file has 40 claims, and the attempt record has 40 outcomes, one per claim:

| Outcome | Count |
|---|---|
| reproduced | 18 |
| partially reproduced | 2 |
| not reproduced | 15 |
| blocked | 5 |

Eight outcomes are marked `assumed: true`.

**I agree with 39 of the 40 outcomes.** Compared with round 1:

- **fig4-control-unitary-events and fig7-pd-unitary-events: I now agree with not_reproduced.** In round 1 I asked for blocked. Four counts have now been run, each checked for chance level and against synthetic synchrony. No combination of count and reading meets the criterion (cell 81: "any combination meets the criterion: False" for both claims), so the outcome no longer depends on one saturated count.
- **rest-synchrony-increase: I now agree with reproduced, resting on the pair count.** The bin and spike counts are shown to be at their ceiling. Two or more cells fire in 99.1–100% of 1 ms bins, and 92–100% of control windows are at the maximum count. Under both pair nulls and every window reading, the parkinsonian file has the longer duration (cell 85, all 8 rows True).
- **activated-pt5b-rate-pd-vs-control: I accept partially_reproduced.** In round 1 I said not reproduced. All four tests find the increase at p ≤ 0.0052, and only Mann-Whitney misses the 0.001 bound (cell 109). That separates it from the IT2 claims, where some test finds no increase at all (p 0.69 and 0.60). The criterion does not make this distinction itself; the record states it as a judgment.
- **fig1-network-size: I still disagree with not_reproduced.**
  - The count of 4,480 measures what the files store, not the model's size. The gids support 10,073 (cell 7: input gids start at 10073; smallest blocks plus unseen gids sum to 10,073).
  - Cell 13 shows the files cannot hold the silent cells the criterion counts.
  - I recommend **blocked (data_missing)**: the quantity cannot be counted from these files. This revises my round-1 partially_reproduced. not_reproduced tells a reader the data contradict the paper, and they do not.

**Assumptions** (all eight are stated in the record):

- **R3 rate reading** (fig2c-control-it6, control-it5, control-it4, pd-it5, pd-it6, rest-it5a, activated-it6). Reasonable. R3 matches every IT value the paper prints, about 20 numbers, to the paper's digits (cells 34–112). R1 and R2 match none of these claims in full.
- **pd-it6-rate-unchanged pairing.** Pairing only cells kept in both files is reasonable. It keeps each paired rate inside the R3 group whose mean is tested. Both pairings are shown, and the union pairing would flip the outcome (cell 97: Wilcoxon 0.0025, paired t 0.0021).
- **rest-synchrony-increase pair count.** Stated, and defensible, with two caveats that the notes do not give:
  - Both pair nulls assume each cell's spikes are spread evenly across its 100 ms window (helper `unitary_events`). The excess therefore partly measures how strongly the population rhythm modulates firing within a window. The median observed/expected ratio is 1.38–1.41 at parkinsonian rest against 1.04–1.05 at control rest (cell 81), and the parkinsonian rest spike-histogram spectrum peaks about 30× higher (cell 25). The paper's own Poisson window null probably shares this property.
  - Under the count-preserving null the comparison is at the ceiling (4.0 against 3.98–3.99 s for slid windows). On independent cells that null's slid windows cover 0.64–0.75 s by chance alone (cell 80). The comparison therefore rests in effect on the rate null (3.8–3.98 s against 0.8–1.65 s), which is conservative.

## 2. Sentences the printed outputs do not support

- **Summary, cell 121:** "the nine IT outcomes that hold only under R3 rest on it as an assumption". The record marks seven IT outcomes as resting on R3, and the README says seven. The IT2 claims and rest-it4 are not reproduced under every reading. The record's findings repeat the error: "nine IT outcomes here rest on that reading".
- **Findings, coincidence question:**
  - "two or more cells fire in 95% to 100% of 1 ms bins". Cell 81 prints 0.991 to 1.0.
  - "the significant duration runs from 0 s (bins, spikes) to 0.8 to 4.0 s (pairs)". Under the pair counts, cell 81 gives 0.000 s (parkinsonian activated, rate null, (b)(i)) and 0.123 s, so the pair range is 0 to 4.0 s.
- **Cell 82 and the fig4 notes:** "rest clusters last up to 551 ms". Cell 81 prints a maximum of 552 ms for (a)(ii). This is trivial.
- **Cell 83 and the fig7 notes:** "in one or two clusters". Cell 81 prints 2 clusters in all four combinations. This is trivial.
- **Summary, cell 121:** "in W they come from a run that diverged from the stored spikes". This is stated as fact, but cell 10 says it "cannot be established from the files".
- **Record, rest-it4-rate-pd-vs-control:** `measured: [0.037, 0.037]` holds the R1 values, while the notes and outcome are argued under R3 (2.57, 14.13). Every other rate claim records the reading it argues from.
- **Record, fig5c-pd-it23-rate-activated, deviation:** "they give the same outcome here". Under the union pairing, every test finds the increase at p < 0.01 and only Mann-Whitney misses 0.001 (cell 91: 2.4e-04, 2.2e-04, 0.0018, 1.7e-04). The record grades that same pattern partially_reproduced for activated-pt5b. The two pairings give the same outcome only because the both-files pairing is adopted.

Everything else in the Result conclusions, the Summary, the README and the record's notes matches the printed outputs.

**My round-1 reasons:** the record's `verifications` block restates all 40 faithfully and in my own words. Problem 10 is answered in the pd-it6 response.

## 3. Round-1 points

**Resolved:**

- **Problem 1 (pairing).** The union pairing is now run everywhere (cells 31–112). It changes only pd-it6, which is now marked assumed.
- **Problem 2 (unitary-event counts).** Four counts were run, each with a chance level and synthetic checks (cells 80–81).
- **Problem 4 (S2 2 Hz test).** Rerun with 1 s and 2 s windows. fig3a fails under every reading either way.
- **Problem 5 (S2 burst span).** Fixed: rates are now per 2.3 s.
- **Problem 6 (which electrode).** "LFP 0" has no electrode metadata and the files have no electrode table (cell 13). This is settled as far as the data allow.
- **Problem 8 (potentials vs spikes).** Recorded as a finding.
- **Problem 9 (stored cells).** The units table has no rows for silent cells (cell 13).
- **Problem 10.** Answered in the pd-it6 response.
- **Time offsets.** Every LFP and potential series starts at 0 s at 40 kHz (cell 13).

**Remaining, bearing on a conclusion:**

- **fig1-network-size.** The outcome should be blocked (data_missing), not not_reproduced, as above.
- **rest-synchrony-increase.** The notes should say that the pair excess tracks the depth of the PT5B rhythm, and that the count-preserving comparison is at its ceiling.
- **Problems 3 and 7 (claims-file readings, reported, not corrected).**
  - The whole-population coincident-spike share cannot give 1–3%. The same all-PT5B reading underlies fig4 and fig7.
  - The half-height burst convention and the unsmoothed duty cycle are the claims-file reader's choices, not the paper's.

  These decide the six spike-synchrony outcomes (coincident spikes, fig4, fig7, rest-synchrony) and the six spectrogram and duty-cycle outcomes. The record asks a reader about them; they stay open until answered.
- **rest-beta-power-order-of-magnitude.** The criterion gives no outcome for a ratio above 31.6, so partially_reproduced is the author's choice. It is stated and reasonable, but the claims-file reader should close the gap.
