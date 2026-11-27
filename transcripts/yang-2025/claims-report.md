I wrote `claims/yang-2025.yaml`, and the quote checker reports 19 claims, 17 quotes, 15 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record, with its one supplement (`supp1-3614867.docx`: Figures S1 to S3 and Table S1). I read Figures 2 to 6 from the PDF and Figures S2 and S3 from their images. The paper links no code and has no code or data availability statement. It names two outside MATLAB toolboxes: MVGC for the Granger causality network and the HFO App for high-frequency oscillation detection.

**Claims:**
- **Counts:** 19 claims. 17 have quotes and 2 are marked `inferred`: the target assignment read from Fig. S2, and the pairs of sites that differ within each rat, read from the bars of Fig. 3A.
- **Statistics:** 15 entries, from Table S1, Fig. 3, Fig. 4B, Fig. 5B and Fig. 6F.
- **Criteria:** all 19 claims have one. 7 are claims of absence, each judged on the paper's own test.
- **Coverage:** network stability (Table S1, Fig. 2), target selection (Fig. S2), seizure duration, duration proportion and frequency (Fig. 3), PSD ratio by band (Fig. 4), interictal spike rate (Fig. 5) and ripples and fast ripples (Fig. 6).

**Details the paper leaves open, and the readings named:**
- **Seizure onset and end:** no offline rule. (a) seizure times deposited with the data; (b) a stated amplitude or line-length rule, as an assumption.
- **Sign of the causal flow measure (cf_w):** the Methods define it as in-degree minus out-degree, but the text and Fig. 2 treat it as outflow. (a) out minus in; (b) in minus out, as worded.
- **Granger causality settings:**
  - Model order is not given; selection by AIC or BIC is used as a standard choice.
  - How the 9 windows are combined: (a) cf_w per window, then averaged; (b) matrices averaged, then cf_w.
  - The test behind a "significantly high" cf_w: (a) the node with the highest mean; (b) Kruskal-Wallis then pairwise tests, allowing ties.
- **Normalization formula:** (a) relative change; (b) difference from the baseline mean; (c) z-score.
- **Unit of analysis:** (a) seizures pooled across rats; (b) stimulation groups (8 target, 20 non-target).
- **Seizures counted per stimulation group:** all of them, or only those that received stimulation.
- **Channels:** all four, or the stimulated one only.
- **Fig. 3A and Fig. 3B:**
  - The post hoc test after Kruskal-Wallis is not named: Dunn's test, adjusted or unadjusted.
  - The test behind "significantly shortened" for the five non-target sites: Mann-Whitney against baseline, Wilcoxon against zero, or a t-test against zero.
  - Fig. 3B's test is not named; Mann-Whitney is used, with a t-test as a variant.
- **PSD:**
  - The change measure: relative change, log ratio or difference. The plotted gamma mean of about -1.3 cannot be a mean relative change.
  - Welch segment length is not given; standard choices are used.
  - The total frequency range: 0.5 to 120 Hz, or 0 to 500 Hz.
- **Interictal spikes:**
  - The rate's bin width: 1 s or 5 s.
  - The baseline for the 5 SD threshold: the 180 s before the seizure, or the interictal segments.
  - The test for Fig. 5B: Mann-Whitney per seizure and channel, or a paired test over time bins.
  - The unit of a point in Fig. 5D (per day or per group) and how it was z-scored.
- **HFOs:**
  - The "paired T-test" for independent groups: paired by rat, or unpaired.
  - Detector parameters are not given, so the HFO App defaults are used.
  - The manual review cannot be repeated, which is recorded as a deviation.
  - The ictal windows are not stated; those of the PSD Methods are used.

**Places where the paper is inconsistent or garbled:**
- **PSD bands:** the Results say alpha and beta rise, but Fig. 4B, the Abstract and the Discussion say theta and alpha. Both readings are named.
- **Duration proportion:** the text gives -0.06 against 0.36 and cites Fig. 3B, but that panel plots normalized seizure duration. No figure shows the proportion values, and their test is not named.
- **Table S1:** R7's significance mark is garbled ("0.71±0.41* **"); I recorded it as p < 0.01.
- **Table S1 tolerances:** I used the table's reported SDs, as the protocol says for a stated spread, which makes them loose.

Nothing a claim needed was missing from the paper beyond these unstated details.
