# Round 3 verifier report

The attempt record has one proposed change of outcome, on claim `fig1e-oxtr-avpr1a-coexpression`. No other claim has a `proposed` entry.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig1e-oxtr-avpr1a-coexpression | partially_reproduced (current verified outcome: blocked, other) | Yes | — | See below. |

## Reason for fig1e (notebook `reproduce_mountoufaris_2024.ipynb`, cells 54–56)

**The numbers come from the data.**
- Cell 55 calls `vmh.load_atlas`. It reads the SMART-seq counts per million (CPM) and the cell metadata of the Kim et al. 2019 deposit (Mendeley Data, doi:10.17632/ypx3sw2f7c.1), and checks each file against the archive's SHA-256 before reading it (`vmh.py:572-605`).
- The cell has an execution count and printed outputs.
- The cell counts printed by cluster and sex add up:
  - Male cells: 103+93+99+147+143+104+14+10 = 713.
  - Female cells: 137.
  - Together: 850, the n used.
- The proposed values come straight from the printed table, row "CPM above 0, all cells of the Esr1 clusters":
  - Oxtr: 73.9%. That is within 78 ± 7.8, so inside.
  - Avpr1a among the Oxtr+ cells: 49.4%. That is more than 6.1 below 61, so outside.
- The tolerance checks in the code are written as |x − 78| ≤ 7.8 and |x − 61| ≤ 6.1, which matches the claims file.

**The choice of reading was not made to reach the result.**
- The adopted reading is all cells of the eight Esr1 clusters, at CPM above 0. It does not give the best outcome: male cells only at CPM above 0 put both values inside (70.4% and 56.2%), which would be "reproduced".
- So the author took the less favourable of the two most inclusive readings. The reason given in cell 56 is that the paper says "Esr1+ cells in VMHvl" and names no sex.
- The Figure 1E legend ("Venn diagram of Esr1, Avpr1a, and Oxtr mRNA-expressing VMHvl neurons") suggests Esr1+ is decided cell by cell. That is the "Esr1 detected" reading, and it gives the same split: 73.9% inside, 48.6% outside.
- So the outcome holds under both readings that follow the paper's wording.
- The Avpr1a fraction is outside under every threshold for both of those cell sets (43.0 to 49.4%). The Oxtr fraction is inside only at thresholds of 0 and 1 CPM.

**The criterion is applied as written.**
- The criterion says "Reproduced when both fractions are within tolerance". Here one of the two fractions is inside, so "reproduced" does not apply.
- The claims file does not define "partially reproduced" for this claim. Calling one of two quantities inside "partial" is consistent with how other claims in the file define it.

**Caveats that do not change my agreement:**
1. The outcome rests on the threshold. At 5 CPM or more, every cell set puts both values outside, which would be "not reproduced". The paper gives no threshold: the STAR Methods say only "analyzed as described previously". The record says this and asks the authors (findings, question 7).
2. CPM above 0 does not reproduce the paper's "most clusters (5/8) containing cells that co-expressed Avpr1a". In the per-cluster table in cell 55, all eight clusters contain co-expressing cells; the lowest is Tsix_Esr1_1 at 3%. This suggests the paper used a criterion other than detection above 0, at least at cluster level. The notebook treats "5/8" as matching the eight clusters, but it matches only their number, not the co-expression count. This weakens the case for the threshold somewhat. It does not point to a reading that would put both values inside, since higher thresholds lower both fractions.

**Claims file:** the claim calls the atlas "a single-cell RNA-seq atlas of VMHvl". Kim et al. 2019 is an atlas of the whole VMH, and the paper's own legend says "VMH single cell transcriptomic clusters". This is a small imprecision; I report it and have not corrected it. It does not affect the test, which restricts the cells to the Esr1 clusters.
