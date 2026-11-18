The verifier agreed with the one proposed change, so one outcome changed and no proposals stand.

**Changed:** `fig8a-proportion-by-property` went from partially reproduced to **not reproduced**, and its `proposed` block is removed. The claims file says the populations follow the columns of Table 1. Counted that way, the results are:

| Property | Here | Paper |
|---|---|---|
| Amplitude | 58/95 | 77/95 |
| Frequency | 62/110 | 73/110 |
| AM | 41/96 | 62/96 |
| FM | 29/82 | 47/82 |
| Higher-order | 64/131 | 59/137 |

Only the higher-order count is within tolerance. The required order AM > FM > higher-order fails, because AM (0.427) and FM (0.354) both fall below higher-order (0.489).

**Also updated to match:**
- **Measured values:** now 58, 62, 41, 29, 64, as the verifier asked. They were the counts from the other reading (one count per probe).
- **Notes:** these now cover two points the verifier raised:
  - The outcome depends on counting higher-order by probes. Counted per probe and ensemble instead, it would be 109/336 (0.324) and the order would hold.
  - How the counts split across Table 1's MHT row is still unresolved, and the question for the authors stays.
- **Notebook:** the result cell and the summary row say "not reproduced". I also tagged the cell that prints the Table 1 counts as an output of this claim.
- **README:** its row says "Not reproduced (assumption)".
- **Round 3 record:** added under `verifications`, with the verifier's reason, its outcome and my response.

**Unchanged:** all other outcomes. While editing I briefly changed a deviation paragraph that the other four Figure 8 claims share; I put their copies back as they were.

**Re-run:** `python tools/entry.py all entries/asari-2009` passed with 0 errors. `reproduce_asari_2009.ipynb` took 1578 s and `strf_wehr.ipynb` 2426 s. The re-run notebook prints the same numbers as the record. Nothing is committed.
