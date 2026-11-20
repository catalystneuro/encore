I finished steps 1 to 6 and handed the entry over for verification. Both notebooks passed in a clean environment, `tools/entry.py check` reports 0 errors, and the handover is in `executed/van-der-molen-2025/handover/`. Of the 50 claims, 29 are reproduced, 11 partially reproduced, 5 not reproduced and 5 blocked. Nothing is committed.

## 1. Outcome per claim

| Claim | Outcome |
|---|---|
| methods-burst-count | reproduced (mean 35.7, but per recording it ranges from 0 to 156 bursts) |
| fig1c-example-burst-count, ed1c-lognormal-rates, fig1d-burst-duration, fig2-backbone-fraction, fig2e-b2b-correlation, fig2g-variance-latency, ed3f-burst-cluster-variability | reproduced |
| ed4b-gabazine-more-bursts, ed4b-nbqx-cpp-abolish-bursts, ed4c-gabazine-participation, ed5-shuffle-reduces-b2b | reproduced |
| fig3e-pairwise-correlation, fig4c-similarity-variance, fig4d-burst-similarity, supp13-top-correlated-units-similarity, fig6f-slice-b2b-correlation, fig6g-slice-pairwise-correlation | reproduced |
| fig7a-backbone-higher-rate, fig7b-primary-no-b2b-difference, fig7c-normalized-pairwise, fig7c-slices-primaries-no-pair-difference, supp24c-nonrigid-more-variable, ed2e-alam-el-din-b2b | reproduced |
| supp18-hmm-likelihood-real-above-shuffled, fig5d-backbone-more-states, fig7f-hmm-dimensionality, supp24d-backbone-non-poisson, supp26-state-traversal | reproduced |
| fig1e, supp2a, supp2c (human organoids only), fig3f, fig4e, fig4f, fig5f, fig7a-primary-higher-rate, fig7b-normalized-b2b, fig7d-lag-times, ed2f | partially reproduced |
| fig5c-states-converge-at-peak, fig7c-backbone-pairs-above-random, fig7d-murine-organoids-slices-same-lag, fig7e-pca-backbone-variance, ed2d-alam-el-din-rates | not reproduced |
| ed4d-gabazine-rank-order, supp10b-rank-order-by-model | blocked, methods_underspecified |
| supp8-backbone-stable-4h | blocked, metadata_insufficient |
| supp27-d2-near-critical | blocked, other (not run for time) |
| supp5-murine-organoid-forebrain-identity | blocked, methods_underspecified (data are in GEO, and the markers are not listed) |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.260923.0623, the only published version; the paper cites none.

**What the dandiset holds.** All 31 recordings are there as sorted files with 1 ms spike matrices. For HO1 to HO4, the burst counts and backbone units match the paper's processed tables exactly.

**Findings recorded:**
- **Murine organoid bursts.** With the burst detection as stated, MO2, MO4, MO5 and MO6 have no bursts. The paper does not give the parameters it used for murine organoids, so I recorded this as `methods_unavailable` with a question for the authors.
- **Missing data.** The MO12 baseline sorted file and all longitudinal murine organoid recordings are absent.
- **No unit identifiers.** Nothing links a unit across the 0 h and 4 h recordings or across drug conditions.
- **Duplicates.** The HO2 and HO3 longitudinal recordings are each deposited 2 or 3 times, with identical spike matrices.
- **Description errors.** The dandiset description says only sorted data are included for the sourced human organoids, but raw files exist for HO1 to HO4. The slice files say their sorting is "not specified".
- **The paper's n counts all sorted units.** The n it reports (507, 34,056, 959, 125,607) matches every sorted unit or pair, not the units its stated rules keep. Its Fig. 7A unit counts match neither count.
- **Species.** Pr1 to Pr4 are rat cultures (the files and the Methods say so), but the paper calls all primary cultures murine.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the murine organoid burst parameters, and which rank-order normalisation was used (z-score or (A−B)/(A+B)) and at which level. On ed4d and supp10b the two normalisations give opposite results.

**Method details taken from the code:** the lognormal fit form and the zero-lag handling for fig7d. The code's lag table has no zero lags, so I dropped them.

I asked readers no questions; I found no place where the claims file misreads the paper.

## 3. Problems with the protocol or tools

1. `entry.py lock` writes a `python:` field into `entry.yaml`, which `schemas/entry.schema.json` rejects. I removed the field; the lock file still records Python 3.13.
2. Editing the entry's README changes the entry hash, so `entry.py all` reruns every notebook (about 45 minutes). My last full run was cut off this way. The executed copies from the earlier passing run are still in place, but the reuse stamp was deleted.
3. Protocol step 1.6 says to adopt the best-supported reading as an assumption. The claims file says that readings which disagree make a claim methods_underspecified. I followed the claims file for ed4d and supp10b.
4. Running 100 shuffles per recording does not fit the 60-minute notebook limit, and the protocol says nothing about running fewer. I used 10 shuffles (3 for the pairwise correlations and shuffled similarity) and recorded this as a deviation.
5. The expected n values count all sorted units, while the criteria restrict which units enter the test. I recorded the count of all sorted units as `measured` and gave the tested counts in the notes.
6. The "Time" rule only names `too_large`, for a claim the computation stopped. It has no category for a claim never started for lack of time, so I used `other` for supp27.
7. The rule that every data stream shares the trial clock does not apply here: there are no trial tables. I said so in the notebook.
8. Seven claims (fig2e, fig3e, fig6f, fig6g, fig7a, fig7b, fig7c) used a mixed model fitted by REML with Wald z tests, which differs from the paper's lmerTest; that is recorded as a deviation. statsmodels' MixedLM did not converge on some models, so I wrote my own fit and checked it against MixedLM on a test case.

## 4. Runtime and failures

- **Runtime:** about 3 h 35 min (12:17 to 15:52 UTC). The main notebook takes 23 minutes and the HMM notebook 21 minutes.
- **HMM deviations:** SSM does not install in a locked environment, so I wrote my own Poisson HMM fitted by EM. I fitted K = 10, 12, ..., 30 instead of every K from 10 to 30. EM was capped at 300 iterations, and 34 of 341 models reached the cap.
- **Failure:** the final `entry.py all` was killed after 10 minutes because of problem 2. The earlier full run passed both notebooks, and its outputs match the reviewed numbers exactly.
- **Stray files:** dotfiles such as `.bashrc` and `.vscode` appeared untracked at the repository root. The sandbox mounts placeholder files at those paths; I did not create them.
