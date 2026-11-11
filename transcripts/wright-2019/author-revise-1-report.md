I've responded to all eleven of the verifier's round-1 points, and the re-run with `python tools/entry.py all entries/wright-2019` passes (150 s, 0 check errors). Nothing is committed.

**Outcomes.** None changed. The verifier gave the same outcome as the record for all 39 claims, and each is recorded under `verifications` with `agrees: true`.
- **fig6ef-beta-correlations:** the verifier read this as "close to not reproduced". I kept it partially reproduced because the criterion names this case as partial: Onset has more significant correlations than Ramping at both thresholds (3 vs 0, and 1 vs 0) while a count is off. The conclusion and notes now say the outcome is partial only through that branch, and that the reported counts are missed by about a factor of four under every reading.
- **fig1s1a-nose-poke-rates:** the outcome already rested on the 20 s window and was partially reproduced, as the verifier gives it. Nothing needed to change.

**Added or corrected:**
- **Spike-train gaps (problem 6).** The verifier was right. Each unit holds spikes only from 20 s before each cue onset to 31 to 34 s after it, with about 141 s gaps between trials (34 of 12,261,110 spikes fall outside). The data description doesn't say this, so I recorded it as a new `metadata_insufficient` finding. The "session" baseline for fig1e is now taken over the windows from 20 s before to 30 s after each onset. The clusters stay at 194 and 51, so that reading still misses the tolerance and the outcome is unchanged.
- **fig3 (problem 3).** The notebook now lists every unit with screen p between 0.017 and 0.05. Nine of them (p 0.025 to 0.046) would each add an Onset-Ramping pair if they passed, so the paper's fourth pair could be a borderline unit.
- **fig2s1 (problem 4).** The cell now prints the criterion's verdict: not met in full, because Ramping is above baseline at 6 of 10 safety positions.
- **fig4abc and fig4efg (problem 5).** I added a check with each neuron's trials shuffled. The Z-scoring alone gives median correlations of −0.49 to −0.70, and the observed −0.45 to −0.55 fall inside the shuffled ranges. The criterion only asks for p < 0.05, which holds, so the outcomes stand. The notes say this, and it is recorded as a new finding.
- **Waveform features (problem 9).** These are now printed per Onset neuron for comparison with Figure 1, figure supplement 4. I can't make that comparison because the paper gives the values only in a figure.
- **`mixed_anova` (problem 10).** A check on synthetic data with unequal groups now shows that all seven F values, including A×B and A×B×G, match sums of squares computed by model comparison.
- **Helper.** `pag.py` gained `screen_p` (per-cue screen statistics) and the `STORED_S` window.

**Not done:**
- No questions were added to `questions/wright-2019.yaml`: the verifier reported no place where the claims file misreads the paper.
- The verifier's suggestion to show the primary reading reproducing a second paper value. The only candidate is the 0.83 danger mean. Across readings the notebook gives 0.768 to 0.799, all within tolerance, with the primary reading closest, but none reaches 0.83. I found no other value that would test the windows on a second unit.
- Problems 7, 8 and 11 needed no change: the verifier judged the primary reading justified, the readings chosen are the ones the claims file allows, and the ITI mismatch is already a finding.
