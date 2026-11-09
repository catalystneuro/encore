## Round 3 verifier report: crcns-ia-1-eyherabide-2008-01

The attempt record has one proposed change of outcome (`grep -c "proposed:"` returns 1). It is for table1-bursting-sessions. No other claim is under review this round.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| table1-bursting-sessions | not_reproduced (currently partially_reproduced, assumed) | Yes | — | See below. |

**Reason (cells 7, 8, 21, 22).**

- **The numbers come from the data.** Cell 8 computes the burst limit for every session and every reading combination with `ia1.burst_limit` on the trial spike times. Cell 21 counts the sessions with any burst of n > 1 per protocol using `ia1.burst_counts`. It then checks each count against the claims-file values (40, 0, 7, 6, 7, 3, 0) with tolerance 0.1 × value, which is 0 where the value is 0. The proposed reason says "at most 2 of 7" under selections (a) and (b). I recomputed it by hand for the main reading over selection (a): 52/60, 2/9, 8/8, 9/10, 10/11, 3/8 and 0/9. Only protocols 6 and 7 are within tolerance, so 2 of 7. Across all 18 burst-reading combinations, selections (a) and (b) score 1 or 2, never more (cell 21).
- **The criterion is applied as written.** The claims file says the claim is reproduced when all seven counts are within tolerance under one combination of burst readings, and partially reproduced when five or six are. The counts depend on table1-sessions-per-protocol, which counts over the kept sessions of data-sessions-and-trials under that claim's readings (a) and (b). Selection (c) is not one of those readings. Cell 7 says it was taken "because, with it, the kept sessions per protocol and the bursting sessions per protocol come close to Table 1". It drops the off-line sorted sessions, and no passage of the paper supports that. So (c) was fitted partly to this claim's own expected values and cannot decide it. That is the problem I raised in round 2. Under the selections the criterion supports, no combination reaches five of seven, so the outcome is not_reproduced. This also matches how the record treats table1-sessions-per-protocol, whose outcome is not_reproduced.
- **The choice does not drive the result.** The proposed outcome holds under every burst reading and under both supported selections, so it does not depend on the main burst reading (peak b, minimum a, N a).
- **Selection (c) is reported accurately.** Cell 22 still shows it, as a variant: six of seven counts equal the paper's (40/47, 1/6, 7/7, 6/7, 7/8, 3/7, 0/7). The `assumed: true` flag is no longer needed because the proposed outcome holds under every reading shown. That flag is metadata, though, and the outcome does not depend on it.

**Note on the claims file (reported, not corrected).** The criterion compares absolute counts. Under selection (a), 115 sessions are kept against the paper's 86, so a count test partly measures the session selection. The fractions are closer: for example, 52/60 = 87% of reference sessions burst, against 40/43 = 93%. This is a limit of the criterion, not a misreading of the paper, and it does not change the outcome as the criterion is written.
