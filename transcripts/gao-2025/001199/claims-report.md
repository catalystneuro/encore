I've written the claims file for DANDI:001199 at `claims/001199/10.1523-jneurosci.2218-24.2025.yaml`. The quote checker passes: 35 claims, 35 quotes, 84 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record, as served by PubMed Central (`paper/10.1523-jneurosci.2218-24.2025.txt`). It has the Methods, Results, all 11 figure legends and the Discussion. The paper has no supplement, and no PDF was supplied. It links no code (analysis was in MATLAB after sorting in Plexon Offline Sorter), so no repository was read.

**Claims.**
- 35 claims, all with quotes, none inferred.
- 25 record statistics: Kruskal–Wallis tests, then one-tailed Wilcoxon post hoc tests with Bonferroni correction, at 0.01 for firing rates and 0.05 for correlations.
- 14 have expected values. Mean ± SEM values use the paper's SEM as tolerance, unit counts use 10%, and rat counts are exact.
- All 35 have a criterion.
- The claims cover subjects, target determination (Fig. 2), unit counts, and Figs. 4 to 11. That includes the sham and cingulate-cortex control claims of no response, the auditory cortex claims, and the correlation claims. Fig. 3 (single example units) is not covered.

**The dataset does not match the paper's own data statement.** The Methods name dandiset **000946** as the repository of all the paper's data. 001199's description mentions things the paper does not report: 64-channel Cambridge electrodes, stimulation aimed at POm, and varied pressure levels. It also says nothing of the auditory cortex recordings. The opening comment says this and maps each figure's conditions to the PRF and pulse duration in the session names. The author must find which sessions match the paper.

**Details the paper leaves open, and the readings named:**
- **Unit typing:** whether waveform durations come from the mean waveform or are averaged over spikes, and whether k-means runs on all units pooled or per area. If the dataset holds the authors' RSU/FSU labels, they are used, with re-clustering as a variant.
- **Normalised rate:** trial-averaged rate over trial-averaged pre-stimulus rate, or a per-trial ratio then averaged.
- **Test against baseline:** the two samples are raw rates, or normalised values against 100%. The Bonferroni factor is either the number of comparisons with baseline or the number of all pairwise comparisons. The paper does not say whether its printed p-values are corrected.
- **Fig. 4 windows:** consecutive 67 ms windows inside the ranges the paper names.
- **Directional correlation (dSTTC):** the equation is lost from the text. It is rebuilt from the verbal definition plus the cited STTC formula (Cutts & Eglen 2014). Two choices remain open: which time windows are used, and whether normalisation is a difference from or a ratio to the pre-stimulus value.
- **Direction of an absence:** increase only, or either direction.
- **Fig. 9A:** the direction in which 30 Hz differs is not stated.
- **Fig. 11B:** which pulse duration the PRF series used; the reading is the 200 µs series.
- **Pair counts in Fig. 11C and 11D:** how the 1,421 and 1,714 pair totals relate to the 878 and 1,016 subsets.

**Wording the paper contradicts itself on:**
- POm RSU delayed responses: "PRFs higher than 1,500 Hz" yet highest at 1,500 Hz (Fig. 6C).
- Fig. 7C: "higher than 6%", but the list includes 6%, and one entry (n = 7) has no duty cycle; by order it is 30%.
- Fig. 8B: the Results report a delayed response at 90%, but the legend reports no difference across duty cycles after sonication.
- Fig. 11C: the Results give about 200 ms and synchronisation towards S1 FSUs; the legend gives about 150 ms and a decrease.
- Fig. 11D: "bidirectional" could mean both signs over time or both directions of the pair.

**Missing from the paper.** The dSTTC equation (lost when the text was extracted). Also any analysis code, and a statement of which dataset holds the S1–auditory cortex rats. No claim needed a supplement.
