I've worked through every point in the round-2 report. All 34 outcomes stay as the verifier agreed, and no outcome change is proposed. I re-ran the entry twice with `python tools/entry.py all`: it passes the checks with 0 errors and the notebook runs in about 3.5 minutes.

**Outcomes:** unchanged. On model-na-ratio, the record now quotes the rule the verifier couldn't read: "A claim that depends on a blocked claim is blocked for the same reason" (Author, step 1.5).

**Analysis changes**
- **Bessel filter (point 3):** the variant ran the filter forward and backward with `sosfiltfilt`, which doubles its order. `nacurrent.lowpass` now runs it once forward with `sosfilt`, as an amplifier's filter acts (4-pole, -3 dB at the cut-off). The new numbers, now in the notebook, record and question file:
  - 13 of 24 baseline-subtracted variants are significant (was 17). They are every a2 reading at 2.9 kHz, every one with the 0 to 3 ms window, and a2b1c2 at 5 kHz.
  - 10 of 24 give a ratio within the model-na-ratio tolerance (was 13).
  - At most 3 of 35 cells are within 10% of the table (was 8).
- **Transients and sessions (point 1):** cell 14 now prints the transients by session, and the session contrast with the transient cells left out.
  - In session AS, 5 of 7 VENs and 4 of 10 PCs have a transient as their maximum. Without those cells only 2 VENs and 6 PCs are left (p = 0.86), too few to tell.
  - Session HS keeps its difference (p = 0.0019).
  - Three AS VEN transients are 3 to 5 times the table's value. The text now says the AS reversal is mostly the artefact, not a session effect.

**Text corrections**
- **The a1 readings:** the text now says two of the four find the effect (a1b2c1 p = 0.27, a1b2c2 p = 0.18).
- **Transient counts:** these are now stated as holding under a2b1c1, the only reading whose widths were computed.
- **Paper's values by session:** VENs are lower in both sessions (AS ratio 0.60); only the significance rests on HS.
- **Smoothing:** the claims that the table "matches" a smoothed peak are gone. The text now gives 19 of 35 cells within 10% at 0.5 ms and 26 at 0.75 ms. Both are below the 28 the criterion needs, and the 0.75 ms width was chosen to fit the table, so the smoothed peak only comes closest.
- **Streaming time:** the measured times are now 150 to 256 s per 0.33 GB across this attempt's runs. That puts DANDI:001746 at about 1.9 to 3.2 hours to stream, against the notebook's 60-minute limit. The earlier "over two hours" doesn't hold at the fastest rate measured, so I replaced it.
- **Capacitance:** the point that capacitive transients were removed is now said to be inferred from the Methods, and no estimate from the traces was tried.
- **Smaller fixes:** I removed the stray fragment in the na-cell-table-link notes and corrected the README row for the 24 other claims.
- **Questions file:** the existing question's numbers are updated to the new run, including "2.9 kHz" in place of "2.9 or 5 kHz".

**Recorded:** round 2 is under `verifications` with all 34 claims. Each gives the verifier's reason as written, its outcome, and a `response`.

**Not done:** I didn't compute transient widths under the other seven readings; the text now says which reading they come from. I didn't add a question for a reader, since the report found no new place where the claims file misreads the paper. I didn't commit anything; the workflow does that.
