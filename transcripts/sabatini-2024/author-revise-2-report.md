I've worked through the round-2 report. No outcome changed and nothing is proposed for a third round: the verifier agreed with all 34, which stay at 13 reproduced, 11 partially reproduced and 10 not reproduced. The entry was re-run twice with `python tools/entry.py all entries/sabatini-2024`, both passing with 0 check errors (notebook 1 in about 40 min, notebook 2 in about 22). Nothing is committed.

**Why most of the quoted numbers did not match.** The verifier read a copy that had been run on a different machine. My two runs here printed identical outputs to each other, but they differ from that copy in the last digit of some fits. For example, the fig2c single-condition LDS gives 83.4% here and 83.2% there. My first run printed exactly the numbers the round-1 text already gave, so I put back the few I had "corrected" to the verifier's copy. Each notebook's summary now says the numbers depend on the machine and gives the other copy's values; no count against a criterion differs between the two. The round-2 responses explain this claim by claim.

**Real errors, now corrected in the notebooks and the record:**
- **fig3i:** the seed spread is at most 0.005, not 0.004.
- **fig4f:** the ranges are 0.816 to 0.952 and 0.824 to 0.947.
- **fig3a:** on the offline onset 3 of 10 frequencies are within 10%, not 2.
- **fig7f-ldr-decoding:** the null and seed ranges mixed the two kinematic bases; they are now given per basis.
- **fig6e:** the seed range is now given per basis.
- **suppfig8:** the p-value ranges are now given per basis.

**Added:**
- **Hand-position units:** notebook 1's data check now prints the hand position's unit and conversion factor, which the sanity finding relied on without showing.
- **Finding 2:** now names the notebook and the cell that shows it.
- **Online-onset assumption:** the 15 claims the offline-onset variant does not cover are now marked `assumed: true`, with a deviation saying so.
- **Round-1 reasons:** the verifier's round-1 problem 2 (which movement onset to align on) is added to the reasons of the eight claims it was raised for.
- **Round 2:** recorded under `verifications` for all 34 claims, with the verifier's reasons and my responses.

**Problem 10 (suppfig8 centring) is settled.** I cloned the paper's code at commit b65f28d. `removePotent.m` sets up `kinParams` as samples × 4, so `mean(kinParams,2)` is each sample's mean over the four variables. That is the notebook's main reading, not the alternative the verifier suspected; the notebook text and the record now cite it.

**Not done:**
- **suppfig3:** stays not reproduced on the claims file's reading. The verifier's misreading point is already in `questions/sabatini-2024.yaml` for a reader to answer.
- **Unsorted units:** the data contain only unsorted threshold crossings, which cannot be fixed. The notes already say this bears on the claims that count dimensions.
- **Round-2 `findings`:** left empty, because no finding is rated `critical`. The verifier found the `major` and `minor` ratings reasonable, which I noted under `reviewed`.
