**Verifier report, round 2: DeWeese & Zador 2004 on CRCNS ac-2**

The claims file has 23 claims and the attempt record has 23 outcomes, one for each claim. The record gives 14 reproduced, 7 partially reproduced and 2 not reproduced, and 13 outcomes carry `assumed: true`. The outcome labels are the same in the record, the README and the notebook's summary.

### 1. Outcomes

I agree with all 23 outcomes. For each assumed outcome, this is whether its assumption is stated and reasonable, and whether the record names every choice the outcome rests on.

| Claim | Outcome | Agree | Assumption |
|---|---|---|---|
| fig2-stereotyped-shape | partially_reproduced | yes | none |
| fig3a-reliable-neuron | reproduced | yes | none |
| fig3b-total-variability-distribution | reproduced | yes | Spike rule. Stated and reasonable. |
| total-variability-population | reproduced | yes | Spike rule. Stated and reasonable. |
| lfp-culling-reduction | reproduced | yes | Stated as the spike rule only. Reading 1b gives 2.99 mV after culling, which is just below 3.0 (cell 28), so the outcome also rests on detail 1, and the record does not say so. |
| fig5b-residual-lfp-psp-correlation | reproduced | yes | none |
| fig7a-lfp-culling-estimation | partially_reproduced | yes | Spike rule and detail 5. Stated. |
| psp-culling-reduction | partially_reproduced | yes | Stated. |
| fig4c-psp-culling-can-increase | partially_reproduced | yes | Correctly not assumed: every reading gives 15, 16 or 20 (cell 40). |
| fig7b-private-best-estimate | reproduced | yes | Spike rule. Stated. |
| culling-controls | not_reproduced | yes | Two q values fail. The criterion's reading of the 10-trial rule is now a question for a reader. |
| fig7d-large-responses | reproduced | yes | Stated as the spike rule only. The LFP bound of 1.62 passes by 0.02. Readings 1b (1.57), variance over N (1.50) and 4b (1.61) all fall below 1.6 (cell 49), and the record does not mention this. |
| large-responses-controls | not_reproduced | yes | none |
| cv-large-responses | partially_reproduced | yes | The criterion defines no outcome for "one value out, test holds", and the record says so. Reasonable. |
| lfp-cv-not-different | reproduced | yes | none |
| anesthesia-comparison | reproduced | yes | Stated. The change from partially reproduced follows from the sequential culling, which the paper supports (Fig. 6 legend, "after first performing the PSP-based culling procedure"). The margins are 0.01 and 0.03 mV. Variance over N would also give partially reproduced (P 0.93, cell 61), and the record does not list it. |
| fig8-spontaneous-veto | reproduced | yes | Correctly not assumed. With the window ending 15 ms before onset, the matching reading (a,b) gives a whole-cell value of −0.172, which is out. (a,a) and (b,b) still hold (cell 64). |
| overfitting-correction-example | reproduced | yes | Details 2 and 4. Stated. |
| private-shared-ranges | partially_reproduced | yes | none |
| quantal-comparison | reproduced | yes | none |
| mepsp-size | partially_reproduced | yes | The detector is stated, but the result is fragile (see 3). |
| recording-properties | reproduced | yes | Access resistance subtracted. Stated and physically reasonable. |
| access-resistance-depth-no-effect | reproduced | yes | Spike rule. Stated. |

### 2. Statements the numbers do not support

- **Cell 29, and the lfp-culling notes:** "The readings of details 1, 2 and 5 keep both values within tolerance (2.99 to 3.12 mV after culling)." 2.99 is outside 3.1 ± 0.1.
- **Cell 44:** "every reading of details 1 to 5 gives 1.36 to 1.78 mV, all within tolerance". 1.36 is outside 1.6 ± 0.2. The record's own notes leave out "within tolerance" and are correct.
- **Cell 14:** "Other trials that only `spikethresh` removes (022301md01, 102500md02, 102900md02) carry narrow spikes that peak just below -20 mV after correction." The figure shows this for 022301md01 only. In 102500md02 and 102900md02 (and in 102900md04) the blue traces are spikes that peak at about −10 to 0 mV, above −20 mV. The claims-file variant misses them because their rise is below the 10 mV/ms the author chose. The summary (cell 86) and every spike-rule deviation in the record say the rule "misses slow regenerative events and spikes that peak below -20 mV". That leaves out this third group.
- **Record findings, mEPSP methods_unavailable:** "the mean size moves from 0.28 to 0.70 mV ... (CV 0.30 to 0.45)". Cell 78 has 0.726 with CV 0.296 (dir mapping, 10% bound), which the record's own notes cite, and 0.771 with CV 0.271 (dir, 5%). Cell 77 has CVs up to 0.53 with fixed thresholds.
- **Cells 35 and 50:** each says it rests on the spike rule (plus detail 5 in cell 35). Cell 50 should also name details 1 and 4 (see fig7d above). Cell 29 should name detail 1.

Everything else checks against the printed outputs: all other "Result:" paragraphs, the Summary, the README table and text, and the other notes. I checked the counts, the ranges, the p-values and the per-recording mEPSP rates and fractions individually.

The verification block states my round-1 reasons faithfully, in compressed form close to my wording, and attaches them to the right claims. For mepsp-size it records that I disagreed.

### 3. Round-1 points

**Resolved:**
- B1: the spike-rule table and figure were added, and the claims-file rule is now run as written.
- B2: sequential culling is now the main reading.
- B4: the identity for the overfitting correction is printed and the per-tone variant removed.
- B5: there is now one main reading for all claims, and every outcome lists which readings would move it.
- B7: reading 1b and the response onsets were added for fig2.
- B8: the reversed access-resistance ordering is stated.
- B9: both fig8 controls were added.
- C1, C2, C3 and C5: the outputs I asked for are now shown.
- B3 in part: mepsp-size is no longer labelled blocked, the collapsed noise SD is fixed, and there is now a false-positive estimate, event-triggered averages, a stimulus-locking check and three sweep mappings.

**Remaining, bearing on a conclusion:**
1. **mepsp-size.** The per-recording threshold gives event rates from 0.11 Hz (030401md02h, 15 events, 1.04 mV) to 19 Hz (050801md01c, 0.20 mV, sizes down to 0.01 mV). The five-recording mean is therefore driven by the threshold each recording happens to get. It is also driven by 030401md02h, whose offset and gain the record itself questions. Which of the two values holds changes between bounds and between mappings. The outcome is partial either way.
2. **Heights are not re-measured after culling.** This choice is stated but not run as a reading, although the Methods say q is "recalculated". It could move the outcomes that sit at their edges: anesthesia (0.01 and 0.03 mV), fig7d's LFP bound (0.02), lfp-culling (3.19 against 3.2) and fig7b.
3. **Spike rule.** The many "claims-file rule would give not reproduced" statements depend on the author's 10 mV/ms rise threshold, which the figure shows misses spikes that cross −20 mV. The 35-mV slow depolarizations that only `spikethresh` removes (102800md02, 100300md02) could be large PSPs as well as regenerative events. If they are PSPs, removing them lowers q by selecting on the response. The main argument for `spikethresh` is that it reproduces the paper's population values. That is reasonable, but it remains an assumption.
4. **culling-controls (B6).** Whether the paper applied the 10-trial criterion again after random culling is still unanswered. It is now a question for a reader. Without it the LFP-matched control gives 4.83 ± 0.22 mV; with it, 3.82.
5. **Figure panels.** The fig2, fig3a and fig4 panels have still not been compared with the paper by eye.
