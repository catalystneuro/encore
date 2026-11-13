Round 3 is applied and recorded. I re-ran the entry with `python tools/entry.py all entries/ghaderi-2026`: all three notebooks pass (8, 15 and 24 min) and `entry.py check` reports 0 errors.

**Outcome changed:** fig5c-cluster-removal goes from blocked (methods_underspecified) to **not_reproduced**, and its `proposed` field is removed. The verifier agreed because both decoder readings fail:
- **Methods' grid search:** cluster 25 is not significant (p_FDR 0.085), and cluster 11 is also significant in wS1.
- **Code's decoder:** it fails in 4 of its 5 runs. Only seed set 0 gives partial.

The verifier also judged that the dependency on fig4b-named-clusters does not apply, since this claim takes only the cluster labels, and those link fully. It added that if the protocol's rule is meant to be applied mechanically, the outcome would stay blocked. The record and cell 8 say this.

**Proposals still standing:** none. fig5c was the only proposal, and no other outcome changed.

**What else changed:**
- **Notebook, cell 6:** the code no longer builds a "mean of sets" row for the Methods reading, which had only one run, and it no longer calls seed set 0 the "main run". This was a minor fix the verifier asked for.
- **Notebook, cell 8:** it now points to the run time printed above it, not a fixed figure. The deviation in the record gives this run's printed time, about 40 min per run for the full Methods search over all 29 clusters.
- **Rounding:** two Methods values now match the printed table (ALM 4.73, and cluster 25 in ALM 1.92).
- **Text:** cell 8, the notebook summary, the README table and the outcome notes now give not reproduced.
- **Run times:** the README and `entry.yaml` now give 15 and 24 min for the two decoding notebooks, to match this run.
- **Record:** round 3 is under `verifications`, with one result for fig5c: agreed, not_reproduced, the verifier's reason and my response.

Nothing was committed.
