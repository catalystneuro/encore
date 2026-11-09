I wrote `claims/crcns-ssc-7/10.1038-nn.4412.yaml`, and the quote checker passes on it (47 claims, 47 quotes, 0 problems). Nothing is committed.

**Text read.** The version of record: main text, figure legends and Online Methods, plus the supplement PDF with the legends of Supplementary Figs. 1 to 14 and Supplementary Tables 1 and 2. The supplementary videos aren't text and weren't used. No PDF renderer is installed here, so I read no figure as an image; I only claimed numbers that appear in the text.

**Code.** I read none. The paper says its code is at the CRCNS DOI, which is this dataset, and the data descriptor names the folder `example_analysis_code`. That folder is one of the dataset's files, so I didn't open it. Every method comes from the paper alone, and the author may read that code to settle the open details below.

**Claims.**
- **Count:** 47, all of them findings and all with quotes, none inferred. Every claim uses the paper's own recordings (`data: dataset`).
- **Statistics:** 34 claims have a `statistics` block or `expected` values (31 with `expected`). The checker found 21 of the recorded p-values in the text.
- **Criteria:** all 47 have one. They cover VPM, L4 excitatory and L4 FS activity during touch and whisking, thalamic photoinhibition, rabies tracing, nerve transection (ION cut), PV suppression with eNpHR (including AUC and behaviour), and task performance.

**Tolerances.** For a mean ± s.d. I used s.d./√n, or 10% of the value if that is larger, because the s.d. is the spread of neurons, not the precision of the mean. A mean ± s.e.m. takes the s.e.m. Medians, single-neuron values and percentages take 10%. Counts take 10%, with a minimum of 1. The two latencies in `enphr-pv-latency` take one 1 ms bin, because 10% is smaller than the bin.

**Unnamed tests.** Many P values come without a named test. The Methods list only the rank-sum test (unpaired), the signed-rank test (paired) and Kruskal-Wallis, so I read paired comparisons as signed-rank and unpaired ones as rank-sum. Where the paper reports no test at all, the criterion fixes one from that list and says so.

**Details the paper leaves open, with the readings named.** These are defined once in the file's opening comment (labels M-…) and referred to by the criteria.
- **Whisking epochs:** the margin around touches and licks for nonwhisking epochs is either the whisking one or none. The 2° rise at whisking onset is measured over 250 ms or over 100 ms.
- **Epoch rates:** total spikes over total epoch time, or the mean of per-epoch rates. In laser experiments, control trials only.
- **Per-neuron whisking test:** rank-sum on per-epoch rates or on per-trial rates.
- **Vm measures:** resting Vm is the nonwhisking mean or the median outside touch. The touch-response peak is sought within 0–50 ms or 0–25 ms. Whisking depolarization is the 100–300 ms after onset minus the 0–200 ms before, or whisking-epoch Vm minus nonwhisking-epoch Vm.
- **Duration of the VPM touch response:** the width at 25% of the rise from baseline to peak.
- **Phase coupling:** 8 or 16 phase bins.
- **Spectra:** band 10–100 Hz or 10–500 Hz.
- **ROC for touch detection:** in no-touch trials, the reference time is either drawn at random within the sample epoch 5,000 times, or set at the median first-touch time with 5,000 trial bootstraps.
- **Photostimulation:** epochs within the laser-on period or whole trials; all laser powers or the highest only; "to x% of control" as a ratio of population means or a median of per-neuron ratios.
- **ION-cut controls "with matched resting potential":** controls within the ION-cut neurons' range, or the 15 nearest to the ION-cut mean.
- **Kruskal-Wallis groups for eNpHR:** four groups (nonwhisking and whisking, control and eNpHR) or two (control and eNpHR).
- **Fig. 8h touch-evoked rate:** raw or baseline-subtracted.
- **Two thalamic-photoinhibition latencies** that the paper doesn't define: the Methods' touch-latency rule, adapted to laser onset.
- **Fig. 8d:** the extracted text shows P = 0.55 beside P = 0.02. I read it as the control-trial comparison, which the text can't confirm, so it is only a variant.

**Missing or inconsistent in the paper.**
- L4 FS neurons are 26 in the Results and Methods, but 25 in the Supplementary Fig. 7 legend and in the sum of Supplementary Table 2.
- ION-cut L4 excitatory neurons are 8, 9 or 10 depending on the passage.
- The rabies tracing and the L5 FS ION-cut recordings ("data not shown") may not be in the dataset; whether they are is for the author to find.
- The example session of Supplementary Fig. 1e names no unit.

Nothing the claims needed was missing.
