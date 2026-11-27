# Round 3 verifier report: xia-2021-01

The attempt record has one claim with a `proposed` outcome: figs12-3v-propagation (line 465). No other claim carries one, so this round reviews that claim only.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs12-3v-propagation | blocked (data_missing) | **Yes** | — | See below. |

## Reason

**The criterion as written.** The claims file (`xia-2021.yaml`, figs12-3v-propagation) tests the 3 V recordings of three mice. It gives "reproduced" when each mouse shows the order and the amplitude at 3 V is below that at 8 V. It gives "partially reproduced" when two of three mice show the order. The paper does report three mice at 3 V, so the file reads it correctly. The Methods say one mouse was stimulated at 3 V and 8 V and two at 3 V only. The Results say "three independent experiments".

Cell 53 and the data check in cell 8 show that only one mouse is deposited: sub-2 (3 V) and sub-3 (8 V) are the same ganglion. With one mouse, neither the three-of-three nor the two-of-three threshold can be reached, so the criterion cannot be applied. That makes "blocked, data missing" the correct outcome, and the round-1 "partially reproduced" did not follow from the criterion. The attempt record already blocks other claims for missing recordings, such as fig5c-voltage-dose, so this is consistent.

**The one-mouse numbers come from the data.** Cell 54 prints every figure the proposal quotes:
- **Rostral region starts first:** 12 of 18 variants. All 12 are in bleaching fits a and c; fit b passes in none.
- **Earliest block in the rostral third:** 11 of 18.
- **Other frame orientations:** the rostral region starts first in 0 of 18 with the frame flipped top to bottom or turned 180 degrees.
- **Amplitude, 3 V below 8 V:** 6 of 6 readings. Tissue peak dF/F at 3 V is 27.1 to 29.0%, against 46.9 to 54.0% at 8 V.
- **Amplitude by region** (16 px blocks, 3 SD, fit a): 21.1 to 43.6% at 3 V, against 38.0 to 69.9% at 8 V.

The record's notes and the conclusion in cell 55 match these outputs.

**The choice was not made to reach a result.** The proposal moves the claim away from a positive label, to the outcome I asked for in round 2. The one-mouse results are kept in the notes, and nothing in the analysis was changed.

**Note on the claims file (reported, not corrected).** The criterion says to read rostral "from the electrode side … where the images do not mark it". The analysis does not do this. It takes the frame as oriented in Fig. 7A, an assumption it records as a deviation, and the direction depends wholly on that assumption (0 of 18 when flipped). This does not change the blocked outcome. But if the two missing mice are ever deposited, the orientation rule in the criterion would need to be applied as written.
