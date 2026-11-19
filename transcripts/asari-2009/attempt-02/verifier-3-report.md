# Round 3 verifier report: Asari & Zador (2009), CRCNS ac-1

The attempt record (`asari-2009-02.yaml`) has one proposed change of outcome, for `fig8a-proportion-by-property`. No other claim has a `proposed` entry, so this report covers only that one.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig8a-proportion-by-property | not_reproduced | Yes | — | See below. |

**Reason (cells 42, 43, 44):**

- **The numbers come from the data.** Cell 42 gives the eligible probe x ensemble table: 738 of 756 entries, with 18 higher-order entries dropped at 3 trials per context. It gives both the probe count and the entry count for each property. Cell 44 takes the Table 1 reading from those counts: 58/95 (0.611), 62/110 (0.564), 41/96 (0.427), 29/82 (0.354) and 64/131 (0.489). I checked the fractions and they are correct. Against the paper's 77, 73, 62, 47 and 59, only higher-order is within tolerance (64 against 59 ± 5.9).
- **The criterion is applied as written.**
  - Not all counts are within tolerance, so the claim is not reproduced in full.
  - The partial rule needs amplitude > frequency and AM > FM > higher-order. Amplitude > frequency holds (0.611 > 0.564). AM > FM > higher-order fails, because both AM (0.427) and FM (0.354) fall below higher-order (0.489).
  - So the rule does not hold, and the outcome is not reproduced.
- **The choice of reading was not made to reach the result.**
  - The claims file says "which probes form each property follows the columns of Table 1". The reading is chosen by which counting unit reproduces the Table 1 totals, and those totals do not depend on significance. Probes give 95 and 110, and entries give 96 and 82 (cell 42, `reading_matching_n`). Entries also give the MHT sub-rows 71 and 57 (cell 43).
  - The outcome does depend on one choice: counting higher-order by probes. Counted by entries, higher-order is 109/336 (0.324), and the order AM > FM > higher-order would hold (0.427 > 0.354 > 0.324). Neither unit matches 137, but probes are far closer (131 against 336). Counting by probes also matches the Table 1 legend ("each row represents the probe stimulus type") and is the only reading that puts the count within tolerance. That choice is defensible and not tuned to the result.
  - The uniform readings that give a partial outcome reproduce the AM and FM totals (probes: 39 and 25) or the amplitude, frequency and higher-order totals (entries: 104, 120, 336) far worse than this reading.
- **A caveat remains, as in round 2.** Getting 71 and 57 for the MHT row means counting the further ensembles of natural probes in that row. That conflicts with the legend's "each row represents the probe stimulus type", and cell 43 shows only 14 MHT probes with AM ensembles (2 cells) against the paper's 25, 25, 71 and 57. The Table 1 reading is the best match to the claims file, but it rests on this unresolved split. The record keeps the question for the authors, which is appropriate.
- **The record's `measured` values need updating if the change is accepted.** They are still the probe-reading counts (58, 62, 25, 16, 64). Under the Table 1 reading the AM and FM values are 41 and 29, so they should become 58, 62, 41, 29, 64. The result paragraph in cell 45 and the README row would then also need to say "not reproduced".
- **Claims file against the paper.** The claims file's Table 1 sums (95, 110, 96, 82, 137) match Table 1 in `paper/10.1152-jn.00577.2009.txt` (lines 174–210) and the Results totals. I found no misreading of the paper for this claim.
