Round 2 is done: no outcome changed and nothing is under `proposed`. The verifier agreed with all 44 outcomes. The entry re-ran cleanly (`tools/entry.py all`: pass, 0 check errors, 356 s) and the conclusions match the new numbers. Nothing is committed.

**Outputs the verifier asked for**
- **The 13 in vivo files and cell 190326_e1:** the data check now lists and draws them, with each file's peak time, sign and first time above chance. The count of 13 of 110 is above chance (binomial p = 0.0034). Most of these are not responses, but two cells do respond:
  - 3 of the 13 files, from two cells (naive 190326_e1, both its EPSC files; experienced 190313_e2, one of its two files), carry an inward current during the call.
  - That current first exceeds chance 0.39 to 0.51 s after the call starts and peaks at 37 to 48 pA, in 13 of 15, 34 of 40 and 25 of 31 trials. The earlier test of the first 300 ms missed it because of this latency.
  - The other 10 files peak at scattered times, 9 of them in the wrong direction.
  - The one cell the inclusion rule keeps is 190326_e1, a naive cell. So the five in vivo claims stay blocked.
- **Imaging call order:** I folded one three-call movie from each of 38 subjects. In 31 of 38 the fold at 3 × 40 frames beats both 2× and 4×. So the trials appear to repeat in a fixed cycle of three, although the Methods say the order was pseudorandom. No file says which call sits at which position, and there are no ROIs, so the 20 imaging claims stay blocked as metadata insufficient.

**Wording corrected**
- "No current that follows the calls" now reads "almost never follows the calls", naming the two cells. This is fixed in the notebook header, data check, results and summary, the README, the record's notes, deviations and finding, and my round-1 response to ed6ef.
- The out-of-date sentence in all 20 imaging notes now says what folding finds. I withdrew "no clear cycle", including in the round-1 responses, marked as withdrawn.
- The call-rate finding is no longer `metadata_error`. 10.24 s is 0.098 Hz, the Methods' 0.1 Hz rounded, so it is now kind `other` and records the cycle of three.
- "p >= 0.35" is now "p >= 0.347" in the fig2i conclusion and notes.

**Other changes**
- A run failed once on a dropped figshare connection, so the helper's downloads now retry.
- The 38 movies are read on 4 threads, which brings the run back under 10 minutes (an unthreaded run took 655 s).
- Round 2 is recorded under `verifications` for all 44 claims, with the verifier's reasons in its own words and my responses.

**Not done**
- I added no reader questions, because the verifier found no misreading of the claims file.
- Which 13 of the 14 first-retrieval mice, and which 12 of the 23 naive excitatory mice, are the paper's cannot be determined from the files. I said so in the record.
- I did not re-measure the 8.2% of slice pulses that fall more than 1 ms off; the verifier says they do not affect the fig1g outcome.
- I left the existing change to `tools/runner/chain.sh` and the untracked dotfiles alone.
