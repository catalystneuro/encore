I wrote `claims/hasnain-2025.yaml`. The quote checker passes it: 19 claims, 19 quotes, 9 statistical values, 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint, version 1 (PMC12632980), full text: Results, Discussion, Methods, and the legends of Figures 1 to 4 and Extended Data Figures 1 to 3. The paper has no separate supplement. No PDF was supplied, so I read no figures; every claim rests on the text.

**Code read.** github.com/economolab/subspaceID at commit d593949. It holds only the subspace optimization (`orthogonal_subspaces.m` with manopt, an example script and a Python port). The paper's other analysis code is "to be made available upon publication".

**Claims.**
- **Totals:** 19 claims, all with quotes. 9 have statistics and 8 have a criterion only. The other 11 have expected values and a criterion; none relies on expected values alone.
- **Testable on DANDI:000363 (8 claims):** the Figure 4 analyses of the reused MAP dataset. They cover session and unit selection, medulla selectivity, variance explained by each subspace in ALM and in the medulla, ALM-to-medulla and medulla-to-ALM decoding, dimensionality, and the UMAP embedding.
- **Not testable here (11 claims):** Figures 1 to 3 and Extended Data 2 and 3 use the paper's own recordings. The paper says these "will be made publicly available upon publication", so they are not public. These claims stay `data: dataset` and can be blocked as `data_missing`.

**Details the paper leaves open, with the readings named**
- **ALM and medulla session count:** 16 (Results and all Figure 4 statistics) or 11 sessions from 7 mice (Methods). The bilateral ALM unit count also disagrees: 1116 in the Results, 2016 in the Methods.
- **Units used:** only units labelled 'good', or all units in the regions of selected sessions. 'Good' is stated only as a session filter. The ALM hemisphere in ALM and medulla sessions is not stated; all ALM units are pooled.
- **Trial window for MAP:** -2.15 to +1.5 s or -1.8 to +1.5 s around the go cue. Normalization follows the Methods' baseline z-score; the code's whole-trace z-score is a variant.
- **Movement threshold:** set by hand per session. The reading is the trough between the two histogram modes, from the paper's own-data procedure. Above-threshold runs shorter than 100 ms count either as stationary or as moving.
- **Subspace dimensions:** a garbled Methods sentence about sessions with forty or fewer neurons. Readings: no cap beyond the neuron count, or a cap of 20 per subspace. The example script's fixed 15 is a variant.
- **Variance explained (Figure 4c):** the covariance and dimension used are open. Readings: full covariance normalized by its top-d eigenvalues, full covariance normalized by total variance (this makes 37 + 41 = 78 add up), or the stationary and moving covariances.
- **Selectivity (Figure 4b):** the five sub-epochs either combine into sample, delay and response, or are scored separately. The number of trials sampled is open.
- **Decoding (Figure 4d):**
  - Trials used: all trials or correct trials only.
  - How R² combines across target dimensions: pooled, or averaged per dimension.
  - Whether predictors are standardized before the ridge.
  - The ALM-to-ALM value: both directions averaged, or each direction alone.
  - Window: the Results say 40 ms, the Methods 45 ms; the Methods' 45 ms is used.
- **Dimensionality (Figure 4e):** the Methods' shuffle-based count, or the effective dimensionality (participation ratio) of the reference the Results cite.
- **UMAP (Figure 4f):** the paper gives no measure and judges by inspection, so the criterion rests on inspection.

**Missing from the paper.** Nothing a claim needed for the MAP analyses, beyond the open details above. Tolerances use the paper's s.d. for Figure 4c and its s.e.m. for Figure 4d.
