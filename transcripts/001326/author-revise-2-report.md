I've finished the round-2 revision. No outcome changed and none is proposed: the verifier agreed with all 54, and nothing in the new run contradicts them. `python tools/entry.py all entries/001326-kauvar-2025` passes with 0 check errors (main notebook 349 s, behavior 195 s, iEEG 32 s). A second full run printed identical numbers.

**Cause of the run-dependent clustering.** The float32 PCA before Leiden rounds differently depending on how many threads the linear-algebra library (BLAS) uses. On the same data, 1, 2 and 4 threads gave three different partitions. The 4-thread one is exactly what the verifier saw (sizes 1019, 730, …), so the verifier's round-1 numbers were right. The record's earlier claim that they came from "a different partition" in the verifier's copy was wrong.
- **Fix:** the clustering cell now runs on one BLAS thread. That gives the same partition (963, 772, …, 173) whatever thread count the machine is set to.
- **Added check:** the stability section now also shows the partition with the PCA in float64 and with 4 threads. Each agrees with the main partition at an adjusted Rand index of 0.71, and the size condition fails in both.

**What I corrected**
- **Clustering and regional-timing conclusions** (fig4de, figs31b, fig4g, fig4i, fig4h, fig4h progression): rewritten from this run in the notebook and in the record's notes and measured values. All outcomes still hold:
  - fig4de: 6 of 12 sizes within tolerance and 2 persistent clusters where 3 are needed.
  - fig4g: rho is −0.273 and −0.409.
  - figs31b: on this partition it holds under the claims file's ranking at both FDR thresholds. I kept it as partially reproduced because the VPM part fails under the ranking of the paper's Fig. 4G and in 2 to 3 of 10 seeds. The new reasons are written down.
- **Round-1 statement:** the "different partition" claim is withdrawn in the round-1 `reviewed` field and in the fig4de and fig4g responses.
- **fig6h:** cell 42 and the record now say 853 s, not 610 s.
- **fig5e-rapid-unchanged (cell 54):** the code-window result is now said to be significant only with per-unit variance, and the pooled q values (0.059, 0.135, 0.220) are given.
- **fig5g:** the range now starts at 0.12, not 0.13.
- **Summary table:** now carries the assumption marks for figs33 and fig6j, and no longer says the default seed fixes the partition.
- **New output:** the data check now prints, per session, how many puff series have a tone or light onset in the 30 s before them, and which series. This backs the "14 of 30" sentence.
- **fig2g:** the notes add that held-out R² keeps rising slowly after six factors, to 0.507 at 22. The elbow assumption stays, since the verifier called it reasonable.
- **Round 2 recorded:** under `verifications`, all 54 claims, each with the verifier's reason in its own words and my response.

**What I did not change**
- **The five human iEEG claims stay blocked as `too_large`.** The protocol's Time rule says a claim stopped by time is recorded that way, and the notes now cite the rule. Testing them needs a raw-LFP analysis that has never been run, and the protocol says such a change waits for a new attempt.
- **The sub-5 assumption is unchanged.** The verifier found it reasonable, and the question stays open with the paper's authors.
- **`questions/001326.yaml` is unchanged.** The verifier reported no place where the claims file misreads the paper.
- **Files I didn't touch:** `tools/build_site.py` was already modified before this run, and the untracked dotfiles weren't created by me.

Nothing was committed, as instructed.
