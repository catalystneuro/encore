There was one question, on **fig3a-eq3a-fit** (it also covers every claim that uses CLW, and nlw-capacitance). I changed the claims file to answer it.

**What the questioner was right about:** the paper does not take CNLW as a fixed 4.82 pF for every cell. It works CNLW out for each cell as CSB + root (Eq. 8c) and then gets CLW with Eq. 8a. The Fig. S1 legend shows this: CL is 24.45 pF and CLW is 18.56 pF, so CNLW is 5.89 pF for that cell, not 4.82 pF.

**What changed:**
- **Shared method** (the opening comment of the claims file): CLW is now CL − CNLW, with CNLW = CSB + root for each cell. The comment notes that the paper takes its rule for CSB from Corbitt et al. (2012) and does not give it. It lists three readings:
  - **(L-a)** CLW, CNLW or CSB as stored for each cell, if the data set stores them.
  - **(L-b)** the root plus a CSB rule the author states as an assumption. The rule only counts if it gives the Fig. S1 cell a CLW within 1.856 pF of 18.56 pF.
  - **(L-c)** a fixed 4.82 pF, shown for comparison only.

  Claims that use CLW, dVmin_exp or C_Leq are judged under (L-a), or under (L-b) where (L-a) doesn't exist. Each outcome is marked as resting on whichever CSB reading was used.
- **nlw-capacitance:** the expected 4.82 pF stays, because that is the value the paper gives for the non-lateral-wall capacitance. Its criterion now reads 4.82 pF as either the mean CNLW across cells or the root alone, and both are shown.
- No claim's statement, expected value or tolerance changed.

**What I left open:** which CSB rule to use is a method detail, so I didn't pick one. Under Author, step 1.6 the author chooses it and states it.

**Answer recorded:** the claims file misread the paper by treating CNLW as a constant. The paper's own Eq. 8a/8c method and its Fig. S1 cell (CNLW 5.89 pF) show it is worked out for each cell, and the shared method and the nlw-capacitance criterion now say so.

`answered: 2026-11-06` is set. `python tools/claims_check.py` reports 0 problems, and both YAML files parse. Nothing is committed.
