I've worked through every point in the round-2 report. The re-run passes (`python tools/entry.py all`, 467 s), and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes:** none changed. The verifier agreed with every outcome except fig1s1c-prereward-dwell-matched.
- **fig1s1c:** it stays `partially_reproduced`, with a `proposed` change to `not_reproduced` for a third round. The verifier is right that fig5b is judged by the rule "the criterion names no partial level", and that rule gives `not_reproduced` here. Bernard differs by 10.2%, or 16.1% with the other pre-reward start. The proposal uses existing outputs, and the conclusion cell now states it.

**Outputs added:**
- **Size estimate cell:** it now prints the one-epoch-per-rat estimate (0.8 h of reading in four processes), the 60 min notebook limit, and the 16.8 TB of 000629.
- **fig5s1:** the correlations are re-run without the 8 epochs whose first goal was carried over. r stays positive in all four rats under both readings (0.116 to 0.357).
- **fig3a-speed-below-immobility:** the largest neurofeedback-cohort median is now printed for every reading. It is 2.19 cm/s at most (2.17 under the adopted reading), still below 4 cm/s with the scale 80% larger.

**Corrections:**
- **Head-position range:** 000629 has a smaller median but a wider spread and larger maximum than 000115. Fixed in cells 14 and 43 and in finding 5, which no longer says the scale "gives the same maze size".
- **Streaming size:** the summary now says 1 to 17 TB, not 1 to 9.
- **Electrode groups:** the counts now match cell 9 (ca1 23, bad_ca1 4, empty 3, can1ref 1, lost 1). Fixed in finding 1, the fig2s1c notes, the header and the summary.
- **fig2e deviation:** it no longer points at fig2s1h for the leaving reading.
- **fig2s1h:** `assumed: true` is restored, with a deviation about the trial parser.
- **fig5b:** the notes now say gus's matched plateau is 5 days, below the Methods' 7 to 10. That reading is kept because it matches the paper's trial counts within 1%.
- **Unshown statement removed:** the claim that "a run of one session did not finish within 60 min" had no output behind it, so I removed it.
- **Summary tables:** the README and the notebook header and summary now list the 000115 claims (9, 5 tested) and the 000629 claims (26, 7 tested) under separate headings.

Round 2 is recorded under `verifications`. No finding is rated critical, and the verifier would raise none, so the round has no `findings` entries.

**Not done:**
- **fig2s1f and fig2b stay blocked.** One epoch per rat is now estimated at 0.8 h of reading. With the roughly 8 min the rest of the notebook takes, plus detection, that is at the 60 min limit. The read rate also varies between runs (97 s and 110 s for the same excerpt). The protocol leaves a change that needs a new analysis to a new attempt.
- **Nothing added to `questions/gillespie-2024.yaml`.** The verifier found no place where the claims file misreads the paper.
