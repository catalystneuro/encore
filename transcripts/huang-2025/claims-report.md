I've written `claims/huang-2025.yaml`. The quote checker passes with 0 problems: 44 claims, 44 quotes, 1 statistical value checked. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC11930745): Results, Discussion, figure legends and STAR Methods, plus the supplement (Document S1, Figures S1 to S9). There is no PDF of the main article, so I read no main-figure images, and I did not read Videos S1 to S3. Nothing a claim needed was missing.

**Code read.** github.com/EdnaHuang/SubnetworkAssembley2024 at commit 28e1b6d. It holds the MATLAB preprocessing, event detection and synchrony code, the k-means, Louvain and DBSCAN clustering, the tCC and distance code, and the R statistics (mixed models with bootstrap) with their knitted outputs. It also has per-dataset summary tables: 455 developmental rows and 96 DREADD rows.

**Claims.**
- **Quotes:** all 44 claims have one.
- **Statistics:** the text prints almost no tests, so only one entry is recorded (L4 tCC, p = 0.051). The contrast estimates and p-values from the repository outputs, which the Methods name as the detailed statistics, are cited inside the criteria.
- **Expected values:** 5 claims have them: the Spearman ρ values −0.063 and 0.233 (tolerance ±0.08, one sampling standard error at n = 162, with the reason given), about 25%, 1% and 30% of events clustered, DBSCAN about 10%, about 4 k-means subnetworks, and about 90% / 10% glutamatergic / GABAergic neurons.
- **Criteria:** every claim has one. Two shared tests are defined in the opening comment, T1 (development) and T2 (CNO), taken from the R scripts.
- **Data:** the 2 histology claims for Figure S9 are `data: elsewhere`, pointing to the repository's spreadsheet.

**Details left open, with the readings named:**
- **O1, quiescent window:** no movement threshold is given. Either use the repository's per-dataset start and end times, or detect it from the behavioral video with a stated threshold.
- **O2, synchrony threshold:** the Methods use the 95th percentile of each shuffle's peak; the code uses the 95th percentile of all shuffled frames, after circular shifts. The Methods are the main reading, the code the variant.
- **O3, k-means runs per cluster number:** 100 in the Methods, 10 in the code. Methods main.
- **O4, participation threshold:** the 95th percentile in the Methods; the code uses 5,000 shuffles and the 1 − 0.05/(number of clusters) quantile. Methods main.
- **O5, denominator of the neuron percentages:** all ROIs, or only ROIs with at least one event.
- **O6, dataset event frequency:** averaged over neurons with at least one event (the code sets silent ones to NaN), or over all ROIs.
- **Smaller readings:** "younger ages" is read as P11 (Figure S2G shows only P11 and P21), "maximum mean difference" as the contrast from P11, and "similar" event percentages as within 5 points. The S3C paired test is a standard choice because the paper names none.

**Conflicts found.** These are tested as the paper states them, and each criterion notes the conflict.
- **Figure S4B vs S2G (`figs4b-mi-sex-p21`):** the S4B text says females have higher MI at P21. The S2G text and the paper's own output say males are higher (p = 0.015).
- **CNO and Pearson correlation (`figs6ab-cno-correlation-unchanged`):** the text says CNO did not change it. The paper's test gives p = 0.040.
- **Subnetwork number across methods (`figs7-subnetwork-number-stable`):** the text says every clustering method shows a stable number. The output gives p < 0.05 for four of the six methods.
- **VGAT by layer (`figs9-layer-differences`):** the text says L4 does not differ from L2/3 in VGAT density. The output shows L4 higher, p < 0.001.
- **Supplement panel letters:** the text's letters for Figures S4 and S6 are off by one from the legends; the sources say so.
- **Neuron count and interval length:** the paper calls their effect on subnetwork count "minimal", but its test of ρ = 0.233 has p = 0.0028.

**Possibly not in the dataset.** The archive description mentions only the P11 to P21 developmental imaging, so the DREADD/CNO sessions (Figure 5, S6) and the histology (S5, S9) may not be there.
