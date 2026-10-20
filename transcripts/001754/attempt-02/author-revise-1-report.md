No outcome changed. The verifier agreed with all seven:

| Claim | Outcome |
|---|---|
| flight-spatial-code | not_reproduced |
| three-orthogonal-surfaces | blocked (metadata_insufficient) |
| si-comparable-to-preflight | reproduced |
| fd4-abnormal-selectivity | reproduced |
| fig3-stability-across-sessions | reproduced |
| theta-normal | blocked (data_missing) |
| ripples-normal | blocked (data_missing) |

The final run with `python tools/entry.py all entries/001754-knierim-2000` passed in 341 s with 0 check errors. The earlier numbers are unchanged, and the conclusions match the new outputs.

**Outputs added for each point:**
- **Whose position the trace is in Rat2's windows (point 1):** a data-check cell gives the trace's movement in every task window. The median step is 0.50 to 1.18 px and the path length is 20.5 to 91.6 px/s, so Rat2's windows hold a continuous track. The same cell tests each rat's units in its own and the other rat's MC windows. Only 0 to 2 units are significant anywhere, so neither check settles whose position it is, and the text says so.
- **Shuffle calibration at the real drop rates (point 4):** each unit's spikes were replaced by a Poisson train, and in a second version each spike was moved to its nearest position sample, which reproduces the real drop rates.
  - Over all flight ES epochs, 0.074 and 0.096 of units come out significant. One session reaches 0.21, so the criterion's 0.05 is lower than the real false-positive rate in some sessions.
  - Against each session's own rate, Rat1's 10 of 25 is still above chance (p 0.0035 and 0.0026) and Rat2's 2 of 28 is not, so flight-spatial-code stays not reproduced. This is now stated in the conclusion, summary, notes and README.
- **Whether rate-map information can fail (point 3):**
  - Rate-map spatial information split by the spike-based test: significant units have a median of 1.855 bits/spike against 1.076 for the rest (p 9e-7).
  - A bootstrap 95% interval for the FD9 minus preflight median difference: -0.425 to 0.312 bits/spike, about -29% to +22%.
  - The si-comparable conclusion now says the test has no equivalence margin, so a difference of about a quarter of the preflight level is not ruled out.
- **fd4-abnormal without Rat2 (points 1 and 2):** Rats 1 and 3 give p = 0.035, the same on the draft and the earlier version, because the three dropped maps are all Rat2's.
- **Rat3 ES1/ES2 difference (point 5):** I added each unit's shuffle 95th percentile in both epochs. For several stable units it rises more in ES2 than their information does. Poisson trains give 0 to 2 false positives in either epoch. The cause is still not explained, and the text says so.

**Records:** I added the round-1 `verifications` block to `attempts/001754-knierim-2000-02.yaml`, with the verifier's reasons and my responses. I also updated the notes of four claims and the first finding.

**Not done:**
- Point 6 (smoothing dependence) was already stated, so I left it as it was.
- Point 7 (occupancy at 38 to 57 counts/s against a stated 60 Hz) is already noted in the data check. It only matters if frames were dropped unevenly across space, and nothing in the files can test that.
- The Methods, chance level and Figure 3 sessions are still unavailable because the paper is not open access.
- I downloaded no paper text, so `paper/` is empty.
- I did not commit or push.
