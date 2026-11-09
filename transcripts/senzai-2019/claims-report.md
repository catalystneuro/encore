I wrote `claims/000166/10.1016-j.neuron.2018.12.009.yaml` with 47 claims. All 47 quotes pass the checker. The checker still exits non-zero on two p-values, both confirmed by reading: 4.0e-4 and 2.0e-6 are printed in the text as "4.0 × 10 −4" and "2.0 × 10 −6", and it doesn't match the trailing zero. Nothing is committed.

**Text read:** the version of record (Neuron 101:500–513, 2019, from Europe PMC, PMC6367010), with full Results, figure legends and STAR Methods. Both supplements were there: mmc1 (legends for Figures S1–S8) and mmc2 (a PDF copy of the article). No PDF page could be opened because no renderer is installed, but every number used is in the text.

**Code read:** the paper links no analysis code of its own, only the lab's general toolbox buzcode, read at commit e615663 (the commit the paper used is not given). I used it for brain-state scoring, UP/DOWN state detection and the monosynaptic-connection functions. Its monosynaptic defaults differ from the STAR Methods (0.4 against 0.5 ms bins, the baseline kernel, the threshold, and the 0.8–4 against 1.5–4 ms window). The file follows the Methods and names the code as a variant.

**Counts:**
- 47 claims, all with quotes.
- 23 claims carry statistics (24 entries in all).
- 47 criteria.
- 18 claims have expected values.
- 46 claims use the dataset. One, the comparison with monkey alpha rhythm, uses data from elsewhere: a published figure from Bollimunta et al. 2008, with no deposit.

**Details the paper leaves open, and the readings named:**
- **Layer groups:** the eight clusters of Figure 5C map to layers 2/3, 4, 5 and 6. The Figure S8B legend settles that layer 5 is clusters 4–6. "Deep" can mean clusters 4–8 or 5–8, and "L4/5 interneurons" can mean clusters 3–6 or 3–8.
- **Clustering:** K-means can run on the coupling matrix or on its t-SNE embedding.
- **Transmission strength:** the Results use the CCG peak-to-baseline ratio, the Methods use the English et al. 2017 corrected probability. Also open: whether the Gaussian baseline kernel is hollowed (as buzcode does) or not.
- **Burst index:** the Results use 3–10 ms over the 200–300 ms bin, the Methods 1.5–13.5 ms over 200–300 ms.
- **Pair count (102,332):** ordered or unordered pairs, among all units or only E and I units.
- **Light pulse length:** 100 ms in the Results, 400 ms in the Methods. The CSD time window and how a sink's depth is read are also open.
- **Unnamed tests:** Figures 6B, 6D–6G and the slow-gamma p = 0.028. Readings are the Methods' defaults (Kruskal-Wallis, signed-rank or rank-sum) and, for phases, a circular test.
- **ICA:** which six of the ten components are the main ones, how they are matched across mice, how the volume-conducted fraction (0.34) is formed, and the denominator of relative power.
- **Gamma coherence clusters:** what the signed-rank "boundary consistency" test compares, and whether six clusters arise or are imposed.
- **Peri-event bins and windows** for the transient/steady index, DOWN-UP latency, the visual-offset rebound, and the light and optogenetic responses of DOWN-state neurons.
- **Other:** 3–6 Hz coupling in all waking or only waking immobility; slow-oscillation band 1–3 Hz (Figure 3D legend) or 0.5–3 Hz (Results); I-E dip as a mean or a median.

**Missing from the paper:**
- **DOWN-state active neurons:** there is no rule for selecting them. I named two readings: a higher rate in DOWN than in UP states, or a peri-event peak just before the DOWN-UP transition.
- **Two claims have no test or measure at all:** the lognormal spread of connection strengths and the similarity to monkey alpha. Both are recorded as `methods_underspecified`.
- **Inconsistent counts:** the paper gives 385 and also 392 E-I connections, and E-I plus E-E (475) falls short of the 525 excitatory connections. The opto-tagged PV cells are given as "15 (n = 11)", which is unexplained.
- **Mis-cited panels:** the text cites Figure S7C for reciprocal connections, but the panel is S8B; it cites S2I for the visual-offset rebound, but the panel is S2D.
