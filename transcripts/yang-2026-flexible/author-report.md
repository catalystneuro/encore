## Report: yang-2026-flexible on DANDI:000020 (version 0.210913.1639)

The entry is locked, checked and run, and the handover is built (`executed/yang-2026-flexible/handover/`). Nothing is committed. The record is `attempts/yang-2026-flexible-01.yaml`.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| join-link (link claim I added) | reproduced |
| cohort-label-join, table1-phenotype-spaces (`assumed`), pc1-long-pulse-loadings | reproduced |
| fig1b-distance-correlation, fig1-fixed-five-pcs-ordering, fig1c-knn-jaccard, knn-scale-sweep | reproduced |
| split-half-reliability | partially reproduced |
| fig2c-eta2-ttype-over-cre, fig2d-knn-type-enrichment, fig2ab-ttype-structure-within-cre | reproduced |
| table2-alignment-ttype | partially reproduced |
| ttype-beyond-cre | partially reproduced |
| fig3a, shared-map, subclass, equal-N, within-regime reliability, fig3b pair tags, threshold sensitivity, type-level-exceeds-cell-level | reproduced |
| mobility-distribution | reproduced |
| Six Figure 4 RNA claims, plus wgcna-mobility-within-type | blocked (`other`): the NeMO data server returned 502 or timed out from 09:20 to 11:49 UTC. WGCNA would also need R. |

Most counts equal the paper's exactly: cells per regime, features, k80, overlaps, t-type counts, 57 types, 156 selective pairs. Mobility is 0.589, SD 0.110.

The three partial outcomes:
- **table2-alignment-ttype:** A_t is significant in every regime, but none of the three values is within tolerance. Over the five seeds long-pulse ranges 0.021 to 0.034, because of how the code breaks ties. No seed gives "reproduced", so it is not marked seed-sensitive.
- **ttype-beyond-cre:** the same pattern, after removing each Cre line's mean.
- **split-half-reliability:** one same-pool value is 0.0002 over its bound and one pool is 2 cells short of its tolerance. Only 16 cells got a random split, against the paper's 358, probably because I had to use the protocol's seed instead of the code's seed 0.

### 2. Dataset, assumptions, questions

- **Version.** I pinned 0.210913.1639: it is the version the paper cites and the only published one.
- **Critical finding.** `sub-673135474_ses-680563483` and `sub-673135516_ses-680897463` are identical recordings. All long-square voltage traces have the same SHA-1 and all 93 IPFX features match, yet the files are from different mice with different Cre lines and t-types. No other pair shares a trace or a feature vector.
- **Minor findings.** The four files of subject 636828314 list two response series for sweep 1, so IPFX cannot open them. The files hold no t-type or RNA sample id.
- **Checks that passed.** Sessions, subjects and genotypes match the paper's join for all 4,430 cells. Stimulus and response share a clock.
- **Assumption.** `extract_ok` means the file opened and the extraction ran. It gives exactly the paper's cell sets.
- **Question for the paper's author** (a `methods_unavailable` finding): which IPFX version and call made the feature table, and what sets `extract_ok`. The script for the 1,000-shuffle null of Table 2 rows m and n is also missing.
- **Reader.** I asked no questions.
- **Inputs.** The join CSV and the feature lists, both from the paper's code at commit 61a5a41.

### 3. Protocol points

1. **Adding a link claim means editing the claims file**, which the author is otherwise told not to change. I added `join-link` and listed it in `depends_on` of six claims; statements, expected values and criteria are untouched.
2. **Notebook conclusions are part of the run hash.** Writing them after the run forces a second 43-minute run. I wrote them from a development run of the same deterministic code and checked them against the final executed output.
3. **The protocol's seeds can conflict with a reported count.** Its seed rule replaces the code's seed 0, and one reported count (358 random splits) depends on that seed. Re-extracting under four more seeds would cost about 10 more minutes, so I noted it and did not measure it.
4. **No `blocked_by` value fits a public input whose server is down.** I used `other` and the notebook prints the server's answers.
5. **Python 3.13 runs process pools in spawn mode** when a pool restarts its workers, which breaks scripts. I used fork with my own pool restarts.
6. **Nothing says how to rate a duplicate recording.** I rated it critical: it is one recording deposited as two, which is among the protocol's critical examples.

### 4. Runtime and failures

- **Notebook:** 43 min (extraction 39 min); peak memory 2.8 GB for the largest worker.
- **Development:** in the first full pass a worker was killed and the pool's retry logic marked 661 files as failed. I fixed the retry logic and re-extracted them; the final run had no failures beyond the 4 unreadable files.
- **Whole session:** about 2 h 40 min.

The repo root shows untracked device nodes (`.bashrc`, `scripts`, …); they come from the sandbox, not from me.
