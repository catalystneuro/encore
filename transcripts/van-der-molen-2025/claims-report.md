I've written `claims/001603/10.1038-s41593-025-02111-0.yaml`. `tools/claims_check.py` finds no problems: 48 claims, 48 quotes, 71 statistical values. Nothing is committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC12912721.1), not the typeset version of record. It has the main text, Methods, figure legends and Extended Data legends. I also read the Supplementary Information PDF, which has Supplementary Figs. 1 to 27 and the Supplementary Methods. Nothing the claims rest on is missing: the HMM, d2, rank-order and burst-clustering methods are all in the Supplementary Methods.

**Code read.** github.com/braingeneers/Protosequences at commit e9a79c4 (2025-05-19). It holds the MATLAB scripts for bursts, backbone units, correlations, burst similarity and PCA; the Python spike shuffling; the HMM code with `lmem.R`; the burst clustering; and per-figure processed tables. The R models for Figs. 2, 3, 6 and 7 are not in it.

**Claims.**
- 48 claims, all with quotes and criteria.
- 31 have statistics.
- 12 have expected values.
- One claim (murine organoid scRNA-seq, Supp. Fig. 5) is `data: elsewhere`, at GEO GSE290330. The dandiset holds only electrophysiology, and that claim is recorded but not tested because the paper does not list its markers.
- The rest use the dataset.
- Seven are claims of absence: two in Fig. 7B and 7C, plus Fig. 7D, Fig. 7E's slices and primaries, Fig. 7F, Supp. Fig. 26 and Extended Data Fig. 2D.

**Where the Methods and the code disagree** (the Methods are followed, the code is run as a variant):
- **Minimum gap between bursts:** 700 ms in the Methods, 800 ms in the code.
- **Units kept for burst-to-burst correlation:** at least 2 spikes in at least 30% of bursts (Methods), against at least 70% (code).
- **HMM cross-validation:** an 80/20 split (Supplementary Methods), against holding out 10% of time-bin by unit entries (code).
- **Lognormal fit:** the code's density divides by (2σ)² where the standard form has 2σ².

**Details the paper leaves open, with the readings named:**
- **Recording length:** the code's 180 s or 600 s, or the first segment holding about 40 bursts.
- **Backbone threshold for slices:** 90% (Methods, Supp. Fig. 1) or 70% (Fig. 6B legend). The random effect for slices is per slice or per animal, since the legend says n = 6 mice.
- **R² of the lognormal fit:** a lognormal fitted to the rate histogram, or a normal fitted to the log-rate histogram. Either over all units or over units with at least 30 spikes.
- **Backbone fraction denominator:** all sorted units, or units with at least 30 spikes.
- **"Close proximity" (Fig. 1E):** within 50 ms or within 100 ms of the burst peak, on per-unit medians or on pooled peak times.
- **Relative position (Fig. 2G):** rank scaled to 0 to 1, or median peak time rescaled over the backbone period.
- **Burst-clustering k:** the knee of the SSE curve, or the largest silhouette coefficient.
- **Rank-order normalization:** z-score or (A−B)/(A+B).
- **Second factor of the Supp. Fig. 2 two-way ANOVA:** unit type or organoid.
- **Sidedness and form of "significantly reduced" after shuffling:** a model of real against shuffled values, or a one-sided test of the normalized value above 0.
- **"Tail" (Fig. 3F):** the backbone-pair mean above the 75th or the 90th percentile of all pairs.
- **Entropy minimum (Fig. 5C):** within 90 ms of the peak, or within the backbone window.
- **"Pool of states" (Fig. 5D):** states with consistency above 0.5, or mean consistency over states.
- **Fig. 5F test:** a paired t-test over the 8 organoids, or per-organoid one-sample t-tests as in the code.
- **Zero lags in Fig. 7D:** dropped, or set to 1 ms.
- **CV2:** raw or z-scored to shuffles.
- **The d2 exclusion rule:** "more than one order of magnitude" is not specified further.

**Gaps that limit testing:**
- The example organoid of Figs. 1, 2 and 4 is not named. It is to be found by its 46 bursts in three minutes.
- No way to match units across recordings is given, which Supp. Fig. 8 (4 h stability) and the gabazine participation analysis need. These are tested only if the dataset links units.
- The text and legends print different p-values for Figs. 7B, 7D and 7F, and both are recorded.
- The paper gives 1048 units for both human organoids and primary cultures, so one of those counts may be a copying error.
- The Fig. 7D legend contradicts itself on murine organoids against primary cultures. I read its second contrast as slices against primary cultures.
