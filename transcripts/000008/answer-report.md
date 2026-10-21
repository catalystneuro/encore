I answered the one open question, `fig5d-sst-pvalb-calb2-firing`, reading (b): **the paper does not give a test**.

- **What the paper and code show:** Fig. 5d is only a colour overlay with no measure. The Fig. 5d cell of the paper's code (`phenotype-tsne.ipynb`, mini-atlas at commit 3bf98a5) just colours the mapped cells by maximum number of APs. The 1,000 permutations came from the claims file, not the paper.
- **What I changed:** in the criterion, I fixed the count so no random seed decides the result. The p-value is exact over all subsets of that size when there are at most 1,000,000 of them. Otherwise it is estimated from 100,000 random subsets as (k+1)/(N+1). The threshold stays one-sided p < 0.05. Reading (b) holds only when the upper bound of the 95% Clopper-Pearson interval is also below 0.05.
- **Effect on this data:** with p ≈ 0.0505 from 100,000 subsets, (b) will most likely not hold. The two readings would then disagree, and the claim stays blocked as `methods_underspecified`. The claim's statement and readings are unchanged.

`answered: 2026-10-21` is set. `tools/claims_check.py` reports 0 problems, and both YAML files parse. Nothing is committed.
