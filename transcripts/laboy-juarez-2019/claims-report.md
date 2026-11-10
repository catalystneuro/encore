I wrote `claims/laboy-juarez-2019.yaml`, and `tools/claims_check.py` passes it: 50 claims, 0 problems. Nothing is committed.

**Text read.** I read the version of record (`paper/10.1038-s41593-019-0448-6.txt`). It has the main text, legends, Methods, the reporting summary and the supplement, which is the legends of Supplementary Figs 1 to 8. I did not need the PDF. The extraction garbles two formulas, the sparseness and the supralinearity z-score. I read them as the standard ones the legible parts and ref. 28 point to, and the opening comment says so. The paper links no code ("available upon request"), so none was read, and every method is cited from the Methods, the legends or the supplement.

**Claims.**
- **Quotes:** all 50 claims have one, so none needed an `inferred` note.
- **Statistics:** 26 claims carry 31 entries with 24 p-values; the other entries are one-sided bounds (`p_relation`).
- **Criteria:** every claim has one except `exp1-cw-tuned-fraction`, which is settled by its expected values.
- **Coverage:** experiment 1 (Fig. 1, Supp. Figs 1 and 2), experiment 2 (Figs 2 to 7, Supp. Figs 4, 6 and 8) and experiment 3 in awake mice (Fig. 8, including the behaviour claim).

**Details the paper leaves open, with the readings named:**
- **O1, sham window:** placed at the session's deflection time, or the whole sham trial scaled to 125 ms.
- **O2, directions in experiment 2:** the single-whisker responses used for responsiveness, CW or SW tuning and the linear prediction are either those in the stimulus's own directions or the mean over both directions.
- **O3, response at the best Δt:** the smoothed tuning value, or the raw mean within ±5 ms.
- **O4, FDR family:** all 451 units together, or correlated and anti-correlated apart.
- **O6, decoder:** "1,000 iterations" read as the optimiser's limit, with 1000 refits as a variant; a pseudo-population for test trials.
- **O7, "nearly all":** judged as at least 90% of units; the paper gives no threshold.
- **Per claim:**
  - slope fitted through the origin or with an intercept (Figs 1d, 8d);
  - the set z-scoring is done over (Fig. 1f);
  - the ANOVA's observations (Supp. 1d);
  - how responsiveness differs for correlated and anti-correlated stimuli;
  - Δt edge handling and held-out Δt without training trials;
  - the denominators of 35% and 46% (responsive sets or all 247 cells);
  - Supp. 6a, which names both all units and only the selective ones;
  - the two ways of computing R² without an intercept;
  - the reference distribution and denominator of the supralinearity test;
  - the Bonferroni family (Fig. 6b);
  - the definition of half-width (Fig. 7a);
  - which curve has the −10 ms minimum;
  - whether best Δt = 0 counts as outbound, since 121 + 56 = 177, not 187;
  - ensemble size and unit pool for Fig. 7g and Supp. 8;
  - which units "built as in Fig. 3e" means (Fig. 4c);
  - balancing in the binary decoder;
  - "peak response at each Δt" (Fig. 8j);
  - smoothing in experiment 3, read as not applied.

**Tolerances and tests that are not the paper's:**
- Per the protocol, the ± spreads are used as tolerances, including s.e.m. values as tight as 0.003.
- I set 2 ms for "~10 ms" and 0.3 for "approximately twofold", with the reasons given in the file.
- Where the paper names no test ("comparable", "significantly weaker", the PC2 and PC3 absence), the criterion says which test or threshold was chosen.

**Missing from the paper for a claim:** no analysis code. The data set's description lists no lick times or trial types, which Fig. 8b and the paper's lick exclusion need, and does not say whether experiment 3 has sham trials, which the spontaneous rates need. Whether the data hold these is left to the author.
