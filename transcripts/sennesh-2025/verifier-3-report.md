# Verifier report, round 3: Sennesh et al. 2025 on DANDI:000253 (0.240923.1441)

The claims file has 37 claims. The attempt record has 37 outcomes: 16 reproduced, 10 partially reproduced and 11 not reproduced. Two outcomes carry a `proposed` change, fig3h-go-alphabeta-csd-feedback and fig3i-go-theta-csd. Both would go from reproduced to not reproduced. I reviewed only these two.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3h-go-alphabeta-csd-feedback | not reproduced | Yes | — | v1 cell 85 (rule in cell 49). In reading a (the Methods' band), L1's mean CSD has one sink sample near −32 ms, and no row shows a displayed sink there. L1's first lasting, displayed sink starts at +28.0 ms. L4 is a sink from the window start (−37.6 ms) and L2/3 from −28.8 ms, so L1 is clearly not first. In reading b, L1 (−12.0 ms) comes after L2/3 (−20.0 ms) and L4 (−27.2 ms). At the window start L1, L4 and L5/6 are all sinks, so L1 does not come first by eye either. The rule fails at 1/8 and 1/16 of a cycle in both readings. S7's own rule fails in both readings. The criterion needs the L1 sink before the L2/3 and L4 sinks, and neither reading meets it. The numbers match the printed sign and display strings. Window counts are 279 and 275 against 300, which is within 10%. |
| fig3i-go-theta-csd | not reproduced | Yes | — | v1 cell 88. In reading a (the Methods' band), L2/3 and L4 are sinks across nearly the whole window. L2/3's only source gap is shorter than the 27-sample minimum, so both onsets are at the window start (−124.8 ms). The two tie, and the criterion's "L2/3 sink comes after it" fails. This matches what you see by eye and what S7's own rule gives. Reading b gives L4 at −124.8 and L2/3 at −58.4 ms, so the rule holds there. Note that L2/3 is also a sink for about 35 ms at the window start in reading b, so even this pass rests on the onset definition ignoring a sink that is already present when the window starts. Taking the Methods' band where the readings split is the same choice the record makes for fig2h (cell 55) and fig4h (cell 104), both graded not reproduced. Window counts are 685 and 575 against 335, about double; the criterion reports this but does not require it. |

## Was the revised rule chosen to reach these results?

The revised tie-break is the change I asked for in round 2: count only a sink that is displayed and lasts at least 1/8 of a band-centre cycle (cells 48 and 49). It is applied the same way to every CSD claim, and the 1/16 and 1/4 variants are printed next to it.

- No other CSD outcome changes under it:
  - fig2g, fig3g and fig4g stay reproduced (cells 51, 83, 101).
  - fig2h, fig2i, fig4h and fig4i stay not reproduced (cells 54, 57, 103, 106).
- Under the new rule, reading b of fig4h now holds. The record states this and grades fig4h by reading a.

## Sensitivity to the minimum duration

For fig3i, the outcome depends on the minimum duration:

- At 1/16 of a cycle, reading a holds, because the L2/3 source gap is no longer merged.
- At 1/8 of a cycle (adopted) and at 1/4, reading a fails.

I accept the outcome for two reasons. The 1/8 value was set for all CSD claims together, and both S7's own rule and a reading by eye give a tie in reading a.

## Claims file against the paper

For both claims, the claims file matches the paper's legend (paper line 91). It does not misread the paper on either claim.
