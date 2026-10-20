I rewrote `claims/000005/10.1038-nn.4412.yaml` from the full text. The quote checker reports 0 problems: 31 claims, 31 quotes, 20 statistical values. Nothing is committed.

**Text read:** the version of record, with its Online Methods and its one supplement (Supplementary Figures 1–14 and Tables 1–2). The extracted text garbled a few things, so I rendered PDF pages for four of them: Supplementary Table 2, the FS waveform boundary in Supp. Fig. 6, the number of phase bins in Supp. Fig. 2d (12), and the P values printed in Fig. 8d (0.55 and 0.02).

**Code:** the paper's data and code link is CRCNS ssc-7 (doi:10.6080/K0T43R01). Its public pages list NWB data files and a data-description document. No analysis code is listed, and downloading needs an account, so I read no code. Every method in the criteria comes from the Methods, the figure legends or the supplement.

**Claims:**
- 31 claims, all with quotes and criteria; 20 have expected values; 13 have statistics (20 entries).
- The eight earlier ids are kept, each with a new criterion. The new criteria for exc-mainly-touch and fs-enhance-touch-selectivity use the paper's own tests: P = 0.20, and P = 0.02 against 0.55. The proxy cell types and the touch-selectivity index from the deprecated file are gone.
- 23 claims are new: VPM phase coupling, excitatory-neuron Vm, distance to threshold, effective reversal, inhibition timing, FS touch, FS Vm, FS whisking rate and FS phase, VPM photoinhibition, excitatory Vm under thalamic photoinhibition, rabies tracing, five nerve-cut claims, PV suppression, touch spikes under eNpHR, two AUC claims, and two behavior claims.
- The opening comment says what changed and why. It also notes that I read the deprecated file's comment, which reports some outcomes of the earlier attempt; no criterion was set from them.

**Details the paper leaves open, and the readings named for each:**
- **O1, band-pass filter direction:** zero-phase, or a single forward pass.
- **O2, samples for the per-cell rank-sum test:** rates per epoch, or per trial.
- **O3, spike threshold:** dV/dt more than 3 s.d. above its mean, or above 3 s.d.
- **O4, resting Vm:** mean or median of nonwhisking Vm.
- **O5, light comparison window:** control trials over the same span of trial time, or all control-trial time.
- **O6, "% of control":** ratio of population means, or median of per-cell ratios.
- **O7, laser powers:** all powers pooled, or the highest power only.
- **O8, latency derivative:** read as the unsmoothed 1-ms PSTH, since the text names no smoothing.
- **Claim-specific:**
  - Effective reversal: one fit per neuron, or one pooled fit.
  - Nerve-cut controls "with matched resting potential": controls within the nerve-cut cells' Vm range, or the 15 nearest in Vm.
  - Latency of the light effects: the dV/dt rule, or a 3 s.d. drop of the average.
  - "Strongly inhibited" PV cells: rate below the control 95% interval.
  - AUC windows on no-touch trials: random windows in the sample epoch, or windows at the median touch time.
  - Pooling for the per-mouse chi-squared test: per mouse, or per session.
- **Other gaps:**
  - The paper states no significance level. I used 0.05, since it calls P = 0.046 significant and P = 0.09 and 0.20 not.
  - Several P values are printed without a test named; I used the Wilcoxon test the Methods give for that design.
  - Which cells make up some counts is not stated: 40 of the 43 excitatory cells in PV-Cre mice, and 13 to 15 FS cells in the thalamic experiment.

**Missing or inconsistent in the paper:**
- The FS count is 26 in the Results and Methods but 25 in Supp. Fig. 7 and Table 2; both sets are to be reported.
- The FS waveform boundary is only drawn in Supp. Fig. 6, near 0.27 ms and a peak-to-trough ratio of 2.8; that is an approximate reading.
- No sentence gives the number of VPM cells with phase coupling. I read about 23 to 26 above r² = 0.25 from the Supp. Fig. 2e histogram.
- Whether the dandiset holds the rabies histology (rabies-vpm-input) is for the author to find.
