I wrote `claims/000689/10.1038-s41586-022-04964-y.yaml`. The quote checker passes it with 0 problems (38 quotes, 185 statistical values found in the text). Nothing is committed.

**Text read:** the accepted author manuscript in PubMed Central (PMC9583860), as served by ncbi_pmc. It has the main text, the full Methods (including the per-panel "Additional statistical information"), and the legends of Figures 1–5 and Extended Data Figures 1–10. I did not read the version of record. The supplementary files the manuscript lists (source data per figure, Reporting Summary) are not in `paper/`, and no claim needs them. There was no PDF, so I could not look at any figure.

**Code:** none. The paper links no code and says it is "available upon request", so every method detail comes from the Methods and the legends.

**Claims:** 38. All 38 have quotes, 30 record statistics and 26 have criteria. They cover:
- anatomy, glutamate co-release and CRISPR validation (Extended Data 1–5);
- the global and PVT-BLA Nt knockouts and the photostimulation behavior (Figures 1 and 2);
- terminal calcium and NT-sensor photometry (Figure 3, Extended Data 6);
- the electrophysiology: recording count, photoidentification, basal firing, responsive proportions, the 7 clusters, cluster and projector responses (Figure 4, Extended Data 8);
- trajectories, SVM decoding and behavior clustering with active/passive strategies (Figure 5);
- the ex vivo and Ntsr1 pharmacology and knockout results (Extended Data 9–10).

The non-recording claims are included even though the dataset may not hold them.

**Details the paper leaves open, with the readings named:**
- **Analysis windows shown only as figure shading:** Fig 1g (0–10 s or 0–25 s), Fig 2c (0–20 s, 0–2 s or 0–25 s), Fig 4e/f/g (0–1 s or 0–0.5 s), and the z-scored window in Extended Data 8e (0–10 s or 0–25 s).
- **Session for Fig 2c:** the last tone-sucrose day, or the sucrose trials of the discrimination task.
- **Photometry early/late trials:** the first 16 trials, or all trials, of the first and last sessions. The measure can be area under the curve or mean z-score.
- **Responsive-neuron threshold (z ±1.98):** applied to the mean over 0–1 s, or to any 20 ms bin.
- **Basal firing rate:** the 1 s pre-CS baseline, or the whole session.
- **Photoidentification pulses:** all light onsets, or the 1 Hz pulses only. The authors' own labels are used if the dataset has them.
- **Ward clustering on correlation distance:** Ward on the correlation matrix, or Euclidean Ward on normalized rows.
- **Single PCA across two groups of neurons (Fig 5a):** the groups stacked along time with shared neuron slots, or all neurons as variables with the other group zeroed. The random subsample and neuron pairing are run over 20 subsamples.
- **SVM pseudo-trials:** trial-index matching, or random draws per neuron. Features come from activity averaged over 0–1 s, or from AUC per time bin.
- **Active/passive split of behavior clusters:** by the median of cluster means, or by the overall mean. "Darting" is undefined, and freezing is read by the Methods' 0.3 cm/s velocity rule.
- **Unit of the Extended Data 8o/s ANOVA:** neurons, or trials.
- **Whether the 685 neurons are counted before or after the 0.3 Hz exclusion:** both counts are shown.

**Missing or inconsistent, needed by claims:**
- Freezing in Fig 2d/h was scored by hand, so an automated rule stands in for it and that is recorded as a deviation.
- The behavior-cluster claims need the paper's pose estimates or its trained DeepLabCut network. If the dataset holds neither, they are blocked. t-SNE perplexity, kernel bandwidth and seed are not given.
- The text itself disagrees in places:
  - Fig 5a reports t(11) for groups of 12 and 14 leave-one-out iterations, and t = 1.224 with P = 0.0002 for the neutral CS.
  - Fig 5b's P-value is 0.2122 in the legend and 0.1309 in the Methods.
  - The Fig 2h statistics are printed under "2f".
  - Mouse counts differ across panels that come from the same cohort.
- Extended Data 9f–g does not say which Wilcoxon result belongs to BLA-NAc and which to BLA-CeM; I recorded them by n and W.
- Cluster numbering can't be recovered from the text, so the Fig 4e clusters are judged as a set.
