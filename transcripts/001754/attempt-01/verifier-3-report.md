## Round 3 report

The claims file lists 7 claims, and the attempt record gives an outcome for each of the 7. Only one outcome has a `proposed` change: flight-spatial-code. The re-executed notebook ran in order from execution count 1 to 27, with no errors, in 5.0 minutes (cell 50).

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| flight-spatial-code | not_reproduced | Yes | — | See below. |

### flight-spatial-code

**The numbers come from the data.**
- Cell 28 runs `epoch_units` on every in-flight ES and MC epoch with `N_SHUFFLES = 500`, which is the pre-specified run.
- Cell 29 prints the results:
  - Rat1 FD9: 12 of 25 units significant (0.480), binomial p 6.88e-10.
  - Rat2 FD9: 3 of 28 (0.107), binomial p 0.163.
- Cell 30 lists each unit's p. Rat1 has exactly 12 units at p ≤ 0.034, and the next unit is at 0.056. It also shows five repeats with 2000 shuffles: Rat1 gets 11 or 12 of 25 and Rat2 gets 2 or 3 of 28.
- Cell 23, a data-check run with 200 shuffles, gives Rat1 13 of 25.
- So there are seven runs, with Rat1 at 11 to 13 of 25. Every number in the proposed reason matches these outputs, and no numbers are hard-coded.

**The choice behind the change was not made to get this result.**
- The only change since the agreed outcome is the lookup in `neurolab.py`'s `PositionLookup`. A spike whose nearest sample is the lost position (0, 255) is now dropped. Before, it took the nearest valid sample.
- I raised this in round 1, problem 6. It brings the analysis into line with the claims file, which counts only units with ≥ 50 spikes "at a known position". A real spike's own sample is at its own time, so when that sample is the lost position, the spike has no known position.
- The synthetic assert in cell 9 checks the new behaviour, and it would fail with the old lookup.
- The fix moves the result against the claim (13 to 12 of 25). The other settings are unchanged from the claims file: shifts are uniform between 20 s and the duration minus 20 s, bins with fewer than 5 occupancy counts and bin [63, 0] are left out, and a unit is significant at p < 0.05 with p = mean(null ≥ observed).

**The criterion is applied as written.**
- Reproduced needs both FD9 sessions at ≥ 0.5. Rat1 has 0.48, so this fails.
- Partially reproduced needs both sessions above chance (binomial p < 0.01), or one session reproduced. Rat2 is not above chance (p 0.16), and neither session reaches 0.5, so this fails too.
- That leaves not_reproduced.
- The open question of whose position the shared trace holds in Rat2's epochs (cells 23–26) does not change the outcome. If Rat2 were excluded, Rat1 at 0.48 would still meet neither rule.

**Caveat.** The call sits on the 0.5 bound. Across the seven runs Rat1 has 11 to 13 of 25 significant, and 4 units lie within two Monte Carlo standard errors of 0.05 (cell 30). The proposed reason, cell 33 and the summary (cell 51) now say this openly. The deciding run is the pre-specified one with 500 shuffles. The five runs with 2000 shuffles are the most precise, and they agree with it (11 to 12). The single 13 comes from the least precise run, with 200 shuffles.
