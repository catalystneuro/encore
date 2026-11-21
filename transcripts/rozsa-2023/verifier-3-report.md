# Verifier report, round 3: Rozsa et al. 2023 on DANDI:000341 0.241220.1312

The attempt record has four proposed changes of outcome, which I counted from the `proposed:` entries in `rozsa-2023-01.yaml`. All four propose `blocked (methods_underspecified)` for the rat active-slice claims that rest on the reading (b) mixture classes. They share one analysis, the class share check in sl[32] and sl[33]. Cell references: sl[n] is the slices notebook and ind[n] the induction notebook.

## What I checked

**The numbers come from the data.**
- sl[31] fits the mixture: 14161 RA-APs of 18779 APs. The RA component has the lower threshold and the lower slope (-50.81 against -44.07 mV, 1.12 against 2.79 mV/ms), so it passes the slope check.
- sl[32] gives the RA share as 0.754 over all gap-free APs and 0.749 in the carbachol + SCH23390 recordings. The median share per recording is 0.868, and the RA class is more than half of the APs in 28 of 32 recordings.
- The paper's share is 76 of 610 (0.125). This matches the Figure 3M legend in `paper/`: "n = 22 cells, n = 76 RA-APs, and n = 534 AIS-APs".
- The median class thresholds in sl[32] are -51.0 and -43.0 mV.
- The protocol-defined rat classes in ind[17] have sporadic-cell medians of -61.58 against -41.19 mV. The record's figures of -61.6 against -41.2 are correct.

**The comparison is not unfair to the attempt.**
- Figure 3M counts APs after the delta-power selection. The attempt's own selection in sl[46] gives 8896 RA-APs and 3867 AIS-APs, an RA share of 0.70. On the population closest to the paper's, the share is still more than five times the paper's.
- Figure 3L (13 of 40 cells with RA-APs) points the same way: the mixture labels RA-APs in 29 cells (record notes, sl[39]).
- The record does not cite this delta-selected figure, but it strengthens the argument.

**The choice was not made to reach a result.**
- I asked for the share check in round 2. It is applied in one cell to all four claims.
- It moves two favourable outcomes (fig3k reproduced, fig3m-ais partially reproduced) and two unfavourable ones (fig3l and fig3m-ra, both not reproduced) to blocked. It does not favour any direction.
- There is no other route to the classes. The dandiset has no AP labels for reading (a), and reading (c) applies only to induction recordings.

**The criterion as written.**
- The claims file's reading (b) has no component or share check, so this block is a judgement, as it was for the human and in vivo claims.
- It is now applied consistently. A mixture whose classes cannot be the paper's (here an inverted share, about 75% RA against 12.5%) does not test claims about those classes.
- This is a gap in the claims file, already reported in round 2. It is not a misreading of the paper.

## Two wording points (no change of outcome)

1. The proposed reason calls share and separation "the standard under which the human and in vivo claims were blocked". Those claims were blocked on an inverted slope (sl[26]; record, fig4b). Share was only reported "for the record" in vivo. What the two cases have in common is "the mixture's classes are not the paper's"; the evidence differs.
2. The 20 mV comparator comes from induction-protocol classes, where AIS-APs are evoked by current pulses. At 100 kHz the rat order even reverses (-41.69 against -42.48 mV, ind[17]). It is weaker evidence than the share, which carries the argument.

## Table

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3l-rat-spontaneous-ra-proportion | blocked (methods_underspecified) | Yes | — | The count of cells with RA-APs depends entirely on the mixture classes. In sl[32] the RA class holds 0.754 of APs against 0.125 in the paper (0.70 after delta selection, sl[46]), and is more than half of the APs in 28 of 32 recordings. The classes are not the paper's, and no reading of the claims file can give the classes in these files. |
| fig3k-rat-pre-ap-fluctuation | blocked (methods_underspecified) | Yes | — | The AIS-AP vs RA-AP SD comparison (sl[42]) uses the same classes, which fail the share check in sl[32]. The reproduced result loses its basis on the same grounds as the claims that went the other way, so the change is not driven by the result. |
| fig3m-rat-ais-phase-coupling | blocked (methods_underspecified) | Yes | — | The population assumption is separate, but the AIS-APs are still the mixture's minority class (3867 of 12763 after delta selection, sl[46], against 534 of 610 in the paper). The coupling of those APs does not test the paper's AIS-APs (sl[32]). |
| fig3m-rat-ra-no-phase | blocked (methods_underspecified) | Yes | — | The strong RA-AP phase coupling (sl[46], sl[48]) is measured on 8896 mixture-labelled RA-APs against the paper's 76. A class that holds most APs, including many coupled to the oscillation, cannot test an absence claim about the paper's RA-APs (sl[32]). |
