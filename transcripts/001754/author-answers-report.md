I've re-run the claims the five answers bear on. One outcome now has a different blocking reason, one stays blocked for a different reason, and every other outcome and number is unchanged.

The notebook ran cleanly in 1.3 minutes and the handover is built in `executed/001754-knierim-2000/handover/`. The entry check does not pass: it fails with 14 errors, all in the earlier attempts `-01` and `-02`, which have no outcome for claims added to the claims file after they were written. The errors are the same with my changes removed. I left those two records alone, so `entry.py all` stops at the check, and I ran `entry.py run` on its own to execute the notebook. Nothing was verified by me, committed or pushed.

## Questions and what each answer changed

**Q1: how M-b is formed, and comparisons with preflight.** The answer says M-b may divide spike counts by the epoch's deposited occupancy map. A comparison must use the same map reading on both sides. Where M-b cannot be computed for preflight, the claim is judged on M-a, and the M-b flight against M-a preflight test is only a variant. That is what the attempt already did, so no number moved. The notebook, the helper's docstring and the record now cite the criterion instead of an open question.

**Q2: which preflight session.** Each preflight epoch (ES and MC) is a candidate under S-a. Under S-b each epoch of the day closest before launch is run on its own, and neither is preferred. Before, the attempt read S-b as the MC epoch alone; now S-b gives the same two readings as S-a. Rat 1's two readings still disagree (p = 0.50 against ES, p = 0.0055 against MC), so it stays blocked, now as the criterion itself says.

**Q3: what "most" means in the stability claim.** It is now more than half of the active cells of session 2, not a count of 4. Under M-b, 6 of 16 cells keep their field by reading (a) and 1 of 16 by reading (b), so both fail. Before, (a) passed as a count.

**Q4: pairing deposited maps to units for M-a.** The best-match pairing is now allowed when it is one to one. I added a check to the notebook, and the pairing passes: 11 maps are tied to 11 distinct units, with 11 distinct session 3 maps. M-a is therefore a judged reading, not a variant. By reading (a), 6 of 11 cells keep their field, which is more than half; by reading (b), 5 of 11, which is not. Without M-a the claim would be not reproduced; M-a's reading (a) is what keeps it blocked.

**Q5: direction-selectivity.** The paper allows no reading without time spent per bin in each direction, so the criterion now blocks the claim as methods_underspecified.

## Outcome per affected claim (earlier outcome in brackets)

| Claim | Now | Before |
|---|---|---|
| `si-comparable-to-preflight` | partially reproduced | partially reproduced |
| `si-rat1-fd9-vs-preflight` | blocked: methods underspecified | blocked: methods underspecified |
| `si-rat3-fd4-vs-preflight` | reproduced | reproduced |
| `fd4-abnormal-selectivity` | partially reproduced | partially reproduced |
| `fig3-stability-across-sessions` | blocked: methods underspecified (M-a reading (a) passes, the other three readings fail) | blocked: methods underspecified (a count of 4 and a fraction of 4/7 disagreed under M-b) |
| `direction-selectivity` | blocked: methods underspecified | blocked: data missing |
| `flight-spatial-code` (depends on the rat 1 claim) | blocked: methods underspecified | blocked: methods underspecified |
| `three-orthogonal-surfaces` (depends on two blocked claims) | blocked: methods underspecified | blocked: methods underspecified |

Each affected claim's notes in `attempts/001754-knierim-2000-03.yaml` now say what the answer changed. The notebook (header, method text, conclusions and summary), `neurolab.py` and the README are updated to match. The lock file was regenerated.
