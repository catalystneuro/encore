**Round 3 verifier report: crcns-hc-13-yu-2017-01 (Yu et al. 2017, eLife 6:e27621)**

The claims file has 32 claims and the attempt record has 32 outcomes. Only one outcome carries a `proposed` change: fig2s1cd-theta-autocorrelation, from partially_reproduced to reproduced. The record now stands at 11 reproduced, 7 partially reproduced, 11 not reproduced and 3 blocked. If the proposal is accepted, that becomes 12 / 6 / 11 / 3.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig2s1cd-theta-autocorrelation | reproduced | Yes | — | See below. |

**Reason (cells 58, 64, 65)**

1. **The numbers come from the data.**
   - Cell 58 builds the entry and exit windows from every immobility period. Each window is ±1.5 s around the start (entry) or end (exit) of a period, merged where they overlap.
   - Cell 64 computes the autocorrelation as the criterion sets it: ±0.5 s (1 s in all) in 10 ms bins.
     - Spikes are split by speed, interpolated at each spike: > 4 cm/s and < 1 cm/s.
     - A cell is kept when it has more than 100 lag pairs; each cell's histogram is normalised, then averaged over cells.
     - The peak is the highest local maximum among bins 0.105–0.155 s, which is inside the criterion's 0.1–0.16 s.
     - Depth is that peak's height above the minimum of the positive lags below it, which is "the minimum between 0 and that lag".
   - Cell 64 prints the following for the claims file's reading:

     | Cells | Window | Peak lag, moving | Depth, moving | Depth, still |
     |---|---|---|---|---|
     | MAP (n = 150) | entry | 0.115 s | 0.00653 | 0.00140 |
     | MAP (n = 151) | exit | 0.115 s | 0.00636 | 0.00193 |
     | IAP (n = 14) | entry | 0.115 s | 0.00104 | 0.00043 |
     | IAP (n = 14) | exit | 0.125 s | 0.00135 | 0.00053 |

   - In all four cases, moving cells have a local maximum in the band and a greater depth than still cells. The numbers in the record's notes match these outputs.

2. **The reading was not chosen to reach the result.**
   - O1 (b), every immobility period, is the claims file's reading as written. It is the reading the attempt used in round 1, where the claim also came out reproduced.
   - The partial outcome came from the well-visit variant. That variant was added later and is not a reading in the claims file. It fails one of four cases (IAP at entry), by a near tie: 0.00089 against 0.00093, with 13 IAPs.
   - Taking the outcome from the claims file's reading undoes a deviation. It is not a choice made to get the result.

3. **The criterion is applied as written.**
   - "Reproduced" needs the moving peak and the greater depth for both cell types, at entry and at exit, and all four hold.
   - The criterion has no partial clause, so there was never a basis for partially_reproduced under the claims file's reading.
   - Like the other `with_inputs` claims, this is a foraging-only test. Here that means 14 IAPs from T1 and S2, and IAP depths that are small.

**Caveats**

- **Wording in cell 65:** it says the O1 (b) maxima lie "between 0.105 and 0.125 s". Cell 64 gives 0.115–0.125 s for O1 (b); 0.105 s appears only in the visit variant, for MAPs. The record's notes have it right. This does not change the outcome.
- **Weak test of transitions:** under O1 (b) the entry and exit windows cover 32 to 62% of task time (median 53%; cell 58). So the test only weakly isolates the periods around transitions.
- **Possible misreading in the claims file (reported, not corrected):** O1 (b) counts every pause as a well entry. The paper's entries look like visits to a well ("periods at wells", Figure 1, supplement 1B–C). The attempt has passed this to `questions/crcns-hc-13.yaml`. If the claims file is revised, this outcome should be re-tested under the new reading.
