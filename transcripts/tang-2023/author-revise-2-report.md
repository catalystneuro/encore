No outcome changed and none is proposed. The verifier's main finding, that the UMAP-based text didn't match the outputs, turned out to come from the embedding differing between machines, not from stale numbers. I fixed that cause, re-ran, and rewrote every UMAP-based conclusion from the new run. The entry check passes with 0 errors, and the notebook now runs in 25 minutes; it ran in 31 minutes on the first run of this round, over the 30-minute limit. Nothing is committed.

**Why the UMAP numbers didn't match**
- UMAP's numba code is compiled for whatever CPU it runs on, and its optimisation magnifies tiny rounding differences. So each machine gave a different embedding. My text came from my run, the verifier's copy was re-run by the workflow on another runner, and my first run here gave a third set of numbers.
- On one machine it repeats exactly. In the locked environment, separate processes gave the same input and embedding, a second seed-0 fit inside the notebook is identical, and two full runs matched in every code cell.
- The header cell now compiles numba for a generic x86-64 CPU and also pins the BLAS kernel and numpy's CPU dispatch. Pinning numba alone was enough to change the embedding here, which confirms it was the source. I can't test another machine type from here, so cross-machine repeatability is expected, not confirmed. The notebook, summary, deviations and README now state this.

**Re-run and new numbers**
- The verifier's two specific points mostly reverse on the new run:
  - **fig3h:** now holds at every seed with the main alignment (weakest is PFC at seed 2, p = 0.042). I recorded the verifier's seed-1 failure (p = 0.096) in the notes and kept the outcome, since seed 0 passed in every run.
  - **fig3j:** without gap filling at 2 cm, PFC now fails (0.8% farther than the shuffle, p = 0.029), so I kept `assumed: true`. The text says this variant changes with the embedding (4.9% closer in the verifier's copy).
- **fig4d-pfc (blocked):** 9 of 16 decoders pass at 8 cm. Above every one of 100 shuffles, 14 of 16 pass at 4 cm and 15 of 16 at 2 cm, so in this run no width gives all 16. I kept the block because 2 cm gave 16 of 16 in the verifier's copy, so it sits right at the edge of the criterion. The finding is reworded to match.
- fig3i, fig4d-ca1, figs7b and figs7d have new numbers in the notebook and the record.
- Everything not based on UMAP is unchanged: I checked each number in those conclusions against the new outputs.

**Other points from the report**
- **Dependency blocking (fig4d-ca1, figs7b, figs7d):** kept. The claims file lists `depends_on: fig4d-pfc-ccgp` for all three, and docs/protocol.md (Author, step 1.5) says a claim that depends on a blocked claim is blocked for the same reason. The conclusions now cite both. Each one's own result would be not_reproduced.
- **fig2f:** added that calling it partial at every width is a judgement call, and that at 2 cm CA1 rises under neither reading.
- **figs5f:** added the 4 cm and 2 cm results. At 2 cm both SI readings find a correlation, so the outcome changes with the width and stays blocked.
- **Cell 23:** now says 100 draws.
- **Round 2 record:** added under `verifications`, with the verifier's reasons for all 32 claims and my responses. No question went to `questions/000447.yaml`: the report names no place where the claims file misreads the paper.

**What I didn't do**
- To get under the time limit I cut shuffle counts, only in variant and blocked analyses: the variant CCGP from 200 to 100, the same-segment variant from 200 to 100, and figs7d from 100 to 50. The record and notebook say so, and figs7d's p-value is still fine enough to decide p < 0.05. Two other speed-ups left the numbers unchanged.
- The figs7b and figs7d tests were still not run at the 4 cm and 2 cm widths, for the time limit.
- I left the round-1 responses in the record as they were written; the round-2 responses give the current numbers.
