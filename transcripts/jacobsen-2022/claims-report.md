I wrote `claims/jacobsen-2022.yaml` with 27 claims. All 24 quotes pass the checker. The checker still reports 2 problems: two p-values it cannot find in the text file. Both are in the Figure S2A legend, which exists only as an image in the PDF. I read them on PDF page 24 and noted this in the file header. Nothing is committed.

**Text read**
- Version of record (Cell Reports Methods 2, 100221), with STAR Methods and Supplementary Tables S1 and S2 from the `.txt` file.
- Figures S1 to S4 and their legends are images only, so I read them from PDF pages 23 to 26. I also read the values printed in Figures 3, 4 and 5C from the PDF.
- The paper says "This paper does not report original code", so there was no repository to read. The Methods send the electrophysiology analysis, including the head direction score and mean vector length, to Rowland et al. 2018 (eLife). The criteria point the author there for those definitions, and I did not read that paper.

**Claims**
- 27 claims: 24 with quotes, 3 marked `inferred`. Those three hold values read from figures: Fig 2A starter-count distribution, Fig 5C example cells, Fig S4 non-responsive cells.
- 4 claims carry statistics:
  - two Spearman correlations: R = 0.58, p = 0.0014; r = 0.54, p = 0.0036
  - two Wilcoxon rank-sum tests: p = 0.0159 and p = 0.0317
- 26 claims have criteria.
- Topics covered: success rates, the starter-count distribution, rabies spread over time and against controls, input cell composition for the single starter cells in Figs 3 and 4, specificity controls (S1), cytotoxicity, the optogenetic tagging results (Figs 5C, S3, S4), and the two imaging examples (Figs 6B, 7B).

**Details the paper leaves open, with the readings named**
- **Pulse time for latency and fidelity:** (a) TTL onset, (b) TTL offset.
- **What makes a cell "responsive":** (R-a) latency 2 to 4 ms and fidelity at least 11.64%, the lowest fidelity among the cells Figure 5C shows as responsive; (R-b) latency 2 to 4 ms and significantly more spikes in the 10 ms after pulses than in the 10 ms before.
- **Grid, head direction and border cell classification:** this paper gives no scores or thresholds of its own, so the criteria defer to Rowland et al. 2018, as its Methods do.
- **Units in the figures:** the cells are labelled by tetrode and cell ID (T1 C89 etc.). If the dandiset does not keep those labels, the fallback is a rate match on the same tetrode. Which of a day's two sessions is meant is also unstated, so each is tried.
- **Tracking one cell across sessions (Fig S3):** not described. The readings are the same cluster label in all sessions, or a waveform match, marked as an assumption.
- **MEC count against days (Fig S2B):** no test is reported. Readings: (a) Spearman p < 0.05, as for the parallel panels; (b) no MEC cells before 22 days.
- **"Detected from about 2 weeks":** the text does not say whether this means by recording or by histology. I read it as by recording.
- **Other:** the Hanning window length for dF/F is not given (a standard choice is allowed). Table S1's "EC" counts are taken to be the same as Figure S2B's "MEC" counts, which the paper does not state.

**Missing**
- Nothing a claim needs is missing from the paper.
- Data: the paper says it deposited only the electrophysiology on DANDI. The histology counts, starter-cell classification and imaging data are not said to be deposited anywhere. So the 18 histology and 2 imaging claims will likely not be testable on 000230; only the 7 electrophysiology claims are expected to be.
- The per-animal counts for the no-Cre controls (rabies cells and spread) are not tabulated anywhere. They appear only as points in Figures 2B and S2A.
