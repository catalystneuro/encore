I've finished the round-1 revision. No outcome changed, and the verifier agreed with all 19 outcomes in round 1. The clean run of `python tools/entry.py all entries/yang-2025` passes in 287 s with 0 errors. Its outputs match the run I wrote the conclusions from, apart from timing. Nothing is committed.

**Fixes, by report point**
1. **Group order (R3-07 dated before R3-06):** I added a variant that takes the preceding baseline by the epoch dates; it changes only R3-07, now normalized to R3-04. fig3a-per-rat-site-differences gives the same counts under it as under the main order.
2. **Groups with few trains:** checking this found a real fault in the train detector, which missed trains. It chose each epoch's pulse rate by the 99th percentile of the comb score, and short 125 Hz bursts (fs / 8) won that choice.
   - It now picks the rate with the most train time and leaves 125 Hz out.
   - Trains are now found in all 8 R3-07 seizures and in every seizure of 24 of the 28 groups.
   - R7's ANT, CA1 and CA3 groups still show trains in only 3 of 13, 2 of 7 and 0 of 4 seizures, and their spectrograms show no stimulation comb.
   - All the false 125 Hz baseline trains are gone. 7 baseline epochs keep trains at their own rat's pulse rate, which is now a finding.
   - Example spectrograms, per-rat traces with onset, end and trains marked, and comb-score diagnostics per group are added, plus a variant that keeps only groups with trains in most seizures.
3. **Post window overlapping the next train:** this happens in 48 of 228 stimulation seizures. The main post window now ends where the next train starts. The window as worded, the same without those 48 seizures, and a 5 s pre window are variants.
4. **Circular clock check:** it now uses the seizure found from the LFP without the trains. 98.9% of trains fall inside it, against about 47% with a 30 s shift.
5. **Pre-window lengths:** now printed (median 13.1 s, none under 1 s).
6. **Table S1 self-pairs:** the outcome stays reproduced, as the criterion names reading (d) and asks for one reading. The text now says the outcome rests on it. Without self-pairs, 5 of 7 rats hold, which would be partial.
7. **fig5b pseudo-replication:** the outcome stays reproduced under the criterion's reading (b). The notebook now prints the bins' lag-1 autocorrelation (0.40) and a test with the rat as the unit (p = 0.23); reading (a) alone would be partial.
8. **Figure S2 order:** the text now says all 28 labels cannot agree under any reading, and that the Figure S2 order variant contradicts the dates.
9. **HFO parameters:** the detector is now the HFO App's own short line length detector at its dialog defaults. I read these from its source (zelanolab/hfoapp, commit 1ccff19, listed under `inputs`):
   - a 5 ms line-length window and a threshold at the 97.5th percentile over the epoch;
   - a 12 ms minimum event length and a two-pass FIR band-pass.

   fig6e is still reproduced, but weakly: p = 0.061, and 5 of 12 readings are significant with target lower. The record says it rests on the all-channels reading. fig6f stays not reproduced.

**Other additions**
- VAR model checks: the fits are stable in all but 2 of 266 seizures, but the residuals are not white at the BIC order. This is stated as a limitation of the GC results.
- A round-1 `verifications` block in `attempts/yang-2025-02.yaml`, with the verifier's reasons and my response for each claim. The notes, measured values, deviations and findings are updated to the new numbers, and the README marks the two weak reproduced outcomes.

**Not done**
- No question was added to `questions/yang-2025.yaml`. The verifier reported no misreading of the claims file, and said the Figure S2 order conflict is between the data and the paper.

**Blindness:** while listing files at the start, I read the first part of `transcripts/yang-2025/author-revise-1-report.md`. It belongs to an earlier attempt (it names `attempts/yang-2025-01.yaml`) and should not have been visible. It mentioned the same HFO App repository and commit. I found the repository again on my own, from the paper's ref. 50 and a GitHub search. Still, the reconcile step should be told this was not fully blind.
