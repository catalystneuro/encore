I've revised the attempt for round 1 and re-run it: `python tools/entry.py all` passed in 27 minutes with 0 check errors. Its output matches the development run the conclusions were written from line for line, apart from timings. Nothing is committed.

The biggest change is the interneuron rule (point B2). The files hold no spike widths, so the Methods' rule (over 7 Hz and narrower than 0.3 ms) can't be applied. The main rule is now the paper code's own rate-only rule, over 9.5 Hz (F7/ParsePyrIN.m), recorded as an assumption. The 7 Hz threshold is run beside it for every claim that separates cell types.

**Outcomes now:** 19 reproduced, 6 partially reproduced, 12 not reproduced, 10 blocked (3 data missing, 7 methods underspecified).

**Changes of outcome:**

| Claim | Was | Now | Why |
|---|---|---|---|
| fig1d-turn-direction | partial | not reproduced | Accepted the verifier: the criterion has no partial band, and the opposite-turn counts fail. A precedent attempt (000013) used the same reading. |
| fig2s2d-phase-offsets | partial | not reproduced | Same reason as fig1d. |
| fig3-choice-selective-fraction | partial | not reproduced | Same reason as fig1d. |
| fig7b-odor-active-more-fields | partial | not reproduced | Same reason; CA1 is now also not significant under the 9.5 Hz rule. |
| fig5d-cross-region-beta | reproduced | partial | Accepted the verifier: the criterion compares the counts, and all four are outside tolerance. |
| fig5gh-phase-preference | partial | reproduced (assumed) | All 8 tests hold at 9.5 Hz; the PFC interneuron beta test is borderline (p = 0.054 and 0.051). At 7 Hz only 7 of 8 hold. |
| fig5-rr-more-than-beta | partial | reproduced (assumed) | The PFC depth comparison gives p = 0.037 at 9.5 Hz; at 7 Hz it gives p = 0.091 and would fail. |
| fig4d-ccg-lags | not reproduced | blocked (methods underspecified) | At 9.5 Hz the last-0.5 s window meets 2 of the 4 parts (partial) and the whole-period window meets 1 (not reproduced). The criterion blocks a claim when its readings differ. |

**Where I kept my outcome against the verifier:** fig6e-glm-with-interneurons stays blocked, and the disagreement is recorded. It depends on fig6e-glm-choice-prediction, which stays blocked, and the protocol blocks any claim that depends on a blocked claim. That parent is blocked because the two window alignments still disagree once random seeds are varied: with 4 other seeds, the onset-aligned reading puts PFC at 0.12 s (outside 0.3 ± 0.1) on 3 of the 4.

**What I added or corrected:**
- **Electrode mapping (B5):** unit counts per file under all three readings of the units' electrode value. Reading it as the electrode-group number puts 24 units in the olfactory bulb (which had no units) and matches no group for 333, so that reading is ruled out.
- **File inventory:** a list of every object in all 38 files. There is no waveform, width, thermocouple or respiration data anywhere. The electrode table's `referenced` column is described only as "my description"; this is now a finding.
- **Smaller requested outputs:**
  - per-epoch task performance (no epoch near chance, so no hidden air sessions);
  - the number of tetrodes averaged per region in the LFP measures;
  - a 7 Hz variant for the GLM, the ensemble (PCA) and all spatial claims.
- **Cross-correlograms (B3):** a global, max-over-bins jitter band, which keeps 5 to 32 pairs per type and finds no lag skew. The peak-z and lag distributions are printed.
- **Phase-locking selection bias (B4):** a split-half control for fig5e and fig5s2. Under the claims' own method both are still reproduced, but the control gives p < 0.05 in at most 1 of 5 splits per group, so selecting cells on the same spikes could produce the effect. The notes say so.
- **Correlations across selections (B11):** the selectivity-index correlations now run under every unit-selection reading.
- **Text fixes:**
  - fig1b: the files already exclude short-sampling trials, and the pass margin is 0.04 points (B7).
  - fig6d: the CA1-vs-PFC test cannot reach significance with 5 paired sessions (B6).
  - fig2s1e: the PFC peak sits at the band edge, and the tapers there are an assumption (B8).
  - the spectral smoothing of one LFP reading reaches into theta (B9), and the other reading's windows overlap the neighbouring periods (B10).
  - the even-odd control groups are half the size of the shuffle groups (B12).
- **Seed checks:** fig5f is fragile at 9.5 Hz: its PFC pyramidal p is 0.0502, and it falls under 0.05 in 4 of 10 other bootstrap seeds. It stays reproduced, with that stated in the notes.
- **Record:** the round is recorded under `verifications` with the verifier's reasons and my responses. New questions for the paper's authors cover the fig4d window and band, the tapers, and the 9.5 Hz rule.

**Not done:** I added nothing to `questions/001539.yaml`, because the verifier reported no place where the claims file misreads the paper. The GLM resampled control was not re-run under the 7 Hz rule, and still uses 10 resamples instead of 100.
