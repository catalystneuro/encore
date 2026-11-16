I've worked through every point in the round-2 report. No outcome changed. One change is proposed for round 3: spectral-features-weak from blocked to not_reproduced. I re-ran the entry with `python tools/entry.py all entries/danish-2017`: it passed in 40 minutes, and the checks report 0 errors.

**Outcomes**
- **spectral-features-weak:** it stays blocked, the outcome round 2 reviewed, with not_reproduced written under `proposed`. The analysis ran: 9 of 18 bird-feature pairs are significant in single birds under reading (a) and 15 of 18 under (b), and pooled gravity center is 0.291 or 0.082 against 0.17 ± 0.017. The schema doesn't allow `assumed: true` on a blocked outcome, so the proposal's reason and a deviation say it rests on the approximate SAP features.
- **fig3-antidromic:** stays blocked, but I dropped the unsupported "no antidromic response" finding. Subtracting each file's median trace removed exactly the response the cell was looking for, as the verifier said, so the spike count is gone. The cell now only describes the artefacts: they recover after a median 2.3 ms, and 36 of 779 stimuli recover before 1.5 ms. The blocked reason is now the claims file's: no stimulus times and no identified units. The notebook, summary, README and record all say this.
- **lesion-undirected-rate-similar:** added `assumed: true`, a deviation for counting only the authors' selected segments, and the all-segment p-values (0.078, 0.109 and 0.078) to the notes.

**Corrected or added**
- **Record numbers, now matching the executed notebook:**
  - fig4b: 36 and 38 ms, mean 37.0
  - fig6-dip: 40.7 ms
  - fig7b: 9.28 Hz, 6.10 to 6.23 Hz over bouts, and the length-normalized MUA peaks of 12.6 and 11.6 Hz
  - fig2e-residual: 1000 null draws (the wrong "200" deviation is removed), local-maximum test 7 of 7, prominence test 4 of 7 or 5 of 7
  - fig9: the coherence part holds
- **fig6-peak:** the notes now say that on b871's channel 7 the mean peak would be 18.7 ms, inside the tolerance.
- **fig9:** I added the criterion's across-bird coherence average. It exceeds its null (0.141) from 2.0 to 59.6 Hz without a break, the same as the average over long types.
- **Notebook text:** corrected cell 43 (Wiener entropy is not significant under the z-scored variant, p = 0.06), cell 83 (local maxima 1.29 to 3.34), the header table and the summary.
- **Round-1 text:** removed the false statements that the revised notebook was never executed, and every "(not executed in this run)" in the responses.
- **Round 2:** recorded under `verifications`, with the verifier's reasons in its own words and my responses.
- **README:** the table now matches the record, including the "(assumption)" tags, and the runtime is updated.
- **Helper speed-up:** the first re-run took 63 minutes, over the 60-minute limit, although the same code had run in 43 minutes before; the rhythm null cell alone took 31 minutes. In `uva.py` I replaced `signal.detrend` and `oaconvolve` in the rhythm null with direct equivalents. On synthetic input the results agree to within 2e-15, and the re-run printed the same numbers.

**Not done**
- I added nothing to `questions/danish-2017.yaml`, because the report found no place where the claims file misreads the paper.
- The channel assumption, which decides whether fig6-peak is partial or reproduced, and the maturity-index form, chosen after the fact, stay as stated assumptions. The verifier found both reasonable, and both are asked of the authors.
- fig8 (GTE) is still not attempted.
- The 5-draw rhythm null mean and the 30 Hz bound are unchanged; the verifier said neither bears on a conclusion.
- Nothing is committed. The changes in `tools/` and the untracked dotfiles are not mine and I left them alone.
