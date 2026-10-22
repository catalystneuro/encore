I wrote the claims file for DANDI:000054: `claims/000054/10.1038-s41593-021-00816-6.yaml`. Every quote passes `claims_check.py`. The checker flags 4 values it cannot parse, the p = 6.0 × 10⁻⁵ entries in the Extended Data Fig. 9l legend; I confirmed those by reading the legend. Nothing is committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC8893323), not the version of record. It has the main text, Methods, the main and Extended Data figure legends, and the supplementary PDF (Supplementary Figs. 1 to 4, simulations of earlier morph studies). There was no main-text PDF, so I read no figures; claims shown only in figures rest on the legends and the Results.

**Code read.** github.com/GiocomoLab/PlittGiocomo_2021 at two commits:
- **dca5a57 (2020-10-28):** the last commit before publication. Its analysis is in `notebooks/`; its figure notebooks are empty.
- **9230b0a (2026-04-16, HEAD):** a refactor that reads the NWB files. Its README says it holds data not in the paper and recomputes place cells with an updated shuffle.

**Claims.** 28 in all: 27 with quotes, 1 with an `inferred` note (session and trial counts, read from three legends), 7 with statistics (16 entries), 10 with expected values, all 28 with criteria. Twelve shared method steps (M1 to M12) are set out in the opening comment.

**Details the paper leaves open, and the readings named:**
- **Speed exclusion for place cells:** (a) timepoints under 2 cm/s excluded, (b) none.
- **Denominator for place-cell percentages and overlap:** pooled over cells, or the mean of per-session fractions.
- **Cell overlap at the track ends and reward zone:** the paper gives only scatter plots. "End points" is read as the first and last bin, or the first and last 50 cm. The reference is either the share of track those regions cover, or the peak locations of all S̃ = 0 place cells.
- **Training fraction (<4% and 60% intermediate trials):** pooled over the group, or per mouse.
- **Which sessions the decision mice (FD1 to FD4) contribute:** all imaged sessions, or sessions 8 and later.
- **Which trials give the average MAP values:** both groups pooled, or each group's own sessions.
- **Pooled Q estimate:** the average of session Q estimates, or one Q from all of a mouse's trials pooled.
- **Ideal posteriors for session 3:** the group posteriors, or priors from the trials each mouse ran before session 3.
- **Decision-mice comparison:** the pooled Q estimate's ΔD_KL > 0, and/or each mouse's reconstructed prior ΔD_KL > 0.
- **UMAP "separable":** most of the 20 clusters significant, or at least one.
- **Simulated neural posterior (Extended Data Fig. 3):** one sample per trial with the session's cell count, or 45 samples with 100 neurons.
- **Visual-only claims** (NMF, single-session similarity, checkerboard sessions, SF along the track, licking): each criterion is my reading built from the paper's own measures, and says so.

**Where the Methods and the code disagree** (the Methods decide; the code's choice is run as a variant):
- **Likelihood width:** the Methods say variance 8.23. The code uses widths equal to 8.23 or 10.97 f_h, which is s.d. 5.82 or 7.76 rather than 2.87. This one could matter.
- **2020 group prior:** the code keeps only the last mouse's prior.
- **R6:** the Fig. 2 test in the code labels R6 as frequent.
- **z-scoring in Fig. 2h:** per cell in the Methods, jointly per session in the code.
- **Smoothing:** the 2020 code does not smooth for Figs. 2 and 3.
- **UMAP min_dist:** 0.1 in the Methods, 0.01 in the code.
- **Simulation parameters** for Extended Data Fig. 3.
- **Signal normalisation** in the 2026 code (95th or 99th percentile against the raw rate).

**Inconsistencies noted in the file:**
- Fig. 4e says 19 frequent sessions; elsewhere the paper says 21.
- The 2020 code ran the overlap t-test on 47 sessions; the paper says 45.
- The 2020 code printed p = 4.68e-3 for the uniform null, against 4.7e-4 in the legend.
- The Methods prior-reconstruction formula writes Q where R is meant; I read it as R, as the code computes it.

**Missing from the paper:**
- No code computes the ΔD_KL permutation tests or the 41/45 session count.
- The kernel widths for the prior and for Q come from the code alone.
- The priors need every trial from sessions 1 to 7, including non-imaged ones. The paper names only DANDI for its data; the 2026 code downloads extra VR data from figshare article 31974756, with no version given.
- One claim (the scene PCA, Extended Data Fig. 2) uses VR renders, not recorded data.
- One claim (the earlier-studies simulations) uses no data from this paper, so the dataset cannot test it.
