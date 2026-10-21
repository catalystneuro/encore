I wrote no claims for DANDI:001349. The supplement this paper's results depend on is missing from `paper/`, and the protocol says to stop in that case (Reader, step 1). Nothing was created under `claims/001349/`.

**Text read:** `paper/10.1016-j.isci.2025.112104.txt` is the version of record, served by Europe PMC (PMC11930745). It holds the main text, the five main figure legends, the STAR Methods and the references. There is no PDF.

**What is missing:** Document S1, the supplement with Figures S1 to S9 and their legends. The text only points to it ("Supplemental information can be found online at https://doi.org/10.1016/j.isci.2025.112104"). These findings and methods rest on it:
- **Pairwise correlations:** the Pearson correlation and mutual information results, P11 against P21 and across all ages (Figs. S2F, S2G, S4A, S4B).
- **Subnetwork checks:** within-subnetwork tCC higher than between-subnetwork tCC, and the Spearman correlations of subnetwork number with neuron count (ρ = −0.063) and with time interval (ρ = 0.233) (Figs. S3C to S3E).
- **Spatial development:** neuron distances and centroid distances over development (Figs. S4B to S4D; the text cites "S4F to S4H" for configuration).
- **CNO experiment:** effects on correlation, MI, subnetwork number, tCC (the increase in females) and spatial distribution (Figs. S6A to S6G).
- **Robustness and cell identity:** clustering with the cosine and Jaccard metrics, Louvain and DBSCAN (Figs. S7, S8), the glutamatergic and GABAergic identity of imaged cells (Fig. S5), and GABAergic synapse density by layer and sex (Fig. S9).
- **Methods:** the Methods cite the supplement for event detection (the noise level and the 4× threshold, Fig. S1D), quiescence selection (Figs. S1E, S2E) and preprocessing (Figs. S2A to S2D). Without its legends, the per-panel sample sizes and the definitions behind those panels cannot be checked.

The main text gives almost no statistics: one p = 0.051 and the two Spearman ρ values. It says the "detailed statistical comparisons for all figures" are at https://github.com/EdnaHuang/SubnetworkAssembley2024. I did not read that repository, since the run stopped at step 1. Once the supplement is supplied, the repository (folder `Statistical_Script_Data`) would also be the source of the LME and bootstrap results that the claims' `statistics` and `expected` values need.

**To proceed:** put Document S1 (Figures S1 to S9 with legends, as text or PDF) under `paper/` and re-run the claims role.
