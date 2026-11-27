All 27 outcomes are unchanged. The verifier agreed with every one, and the re-run (`python tools/entry.py all entries/wakhloo-2026`: 0 errors, notebook passes in 32 min, 0.84 GB peak memory) gives the same numbers. I committed nothing.

**What I added or corrected, by point in the report**
- **B3, the PFC spread for glm-cross-validated-d2:** I found the cause. The paper's own GLM fits are in its repository (`results/glm_results`, stored with Git LFS). A new cell reads them in memory and matches their rats to ours by unit counts, which agree in all 64 sessions of both areas.
  - Our session D2 equals the paper's to within 1.8e-09.
  - The paper's own fits give the same spread over rats: 0.0599 and 0.0640 in PFC, 0.1005 and 0.1075 in CA1. So the gap to the reported 0.022 comes from how the paper computed it, not from fitting.
  - The s.e.m. over rats is now printed for every reading: 0.0226 in PFC (close to 0.022) but 0.0380 in CA1 (against 0.1). No single reading gives all four reported values, so the outcome stays partially reproduced.
  - The task dimension from the paper's predictions also matches ours (r = 0.9996 in PFC, 0.9997 in CA1).
  - I changed the finding about the 0.022 from `methods_unavailable` to `code_mismatch`, stating that the paper's own results give 0.060.
- **B4, best-score selection:** `wtrack.glm_summary` now picks the best alpha with plain `np.argmax`, as the paper's code does, and the docstring is corrected. Only one unit has a nan score, so no number moves.
- **B5, unit count for CA1 task dimension:** I kept 19 units as the main reading, because the claims file's pipeline says so. The cells for fig7hk-measures-increase-early and late-trends-match-optimal now also print CA1 with 24-unit task-dimension subsets.
  - fig7hk is unchanged: 3 of 4 measures rise.
  - late-trends-match-optimal: under reading (a) the 24-unit value still falls (-0.026). Under reading (b) its slope is +0.013 with P = 0.86, which meets that reading in sign only. The outcome stays partially reproduced, judged on the 19 units, and this is written in the notes so round 2 sees it.
- **B6, the paper's mixed-model table:** a new cell prints the paper's `results/rat_stats.csv` next to the main reading and the 19-unit variant. In the 19-unit variant the signs agree in all 14 models.
- **Record:** I added the round under `verifications`, with all 27 claims, the verifier's reasons in its own words and my responses. I added the two new comparison files under `inputs` and updated the notes for the three claims above. The record validates against the schema, and the entry check passes.

**What I did not do, and why**
- **B1:** the SVC still runs on 4 of the 500 subsets per session. Running all 500 would take about 25 hours, and the verifier judged that it does not affect the conclusion.
- **The `blocked_by` reasons for the pose and macaque claims:** the verifier would mark them `data_missing`. I kept `not_runnable` and `other`, because the claims file marks those data as public elsewhere, and the protocol says such claims are never `data_missing`. The disagreement is recorded.
- **B7, the fig7f criterion change:** it is recorded for round 2. The change and the earlier outcome (not reproduced) were already stated in the notes.
- **Questions for a reader:** I added none, because the verifier reported no place where the claims file misreads the paper.
