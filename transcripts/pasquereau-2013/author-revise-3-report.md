No outcomes changed. The round-3 verifier disagreed with all four proposals, so all four stay open in the record with the verifier's view added to each reason.

| Claim | Outcome (kept) | Proposed (still stands) |
|---|---|---|
| kinematic-latency-unchanged | not_reproduced | reproduced |
| emg-duration-longer | partially_reproduced | not_reproduced |
| emg-onset-unchanged | not_reproduced | reproduced |
| emg-m1-weak | partially_reproduced | reproduced |

The verifier's reasons, in short:
- **Wrong comparison:** each criterion compares all sessions or channel-sessions. Restricting to equal pulses is a choice made after the all-perturbation results were known.
- **Too few sessions:** the equal-pulse subsets are small (5 pre-MPTP channel-sessions near 180 units, 14 post-MPTP near 90 units). That is too little to show that an effect is absent.
- **Filter dependence:** for the movement latency, the causal filter gives p = 0.0027 at 85 to 95 units, which by the criterion is not reproduced.
- **Small-pulse sessions:** for emg-m1-weak, these are most pre-MPTP sessions (105 of 151), and the claims file includes them.

The verifier agreed the pulse-size difference is real. It belongs in finding 3 (already rated major), not in the outcomes.

What I updated:
- **Attempt record:** the four proposal reasons now carry the verifier's view. The emg-m1-weak notes now say most pre-MPTP sessions have small pulses. Round 3 is recorded under `verifications` with one `agrees: false` result per claim, the verifier's reasons in its own words, and my response.
- **Notebook:** the four conclusion cells and the summary now say the proposals were reviewed and not accepted.
- **README:** says the same. It also notes that the "unchanged latency" at equal pulses holds only for the claims file's onset measure.

`python tools/entry.py all entries/pasquereau-2013` gave 0 errors, and the notebook passed in 570 s. Nothing is committed.
