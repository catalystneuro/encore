I've written the claims file, `claims/002020/10.1101-2025.01.14.630383.yaml`. The quote checker reports 20 claims, 20 quotes and 0 problems.

**Text read.** The bioRxiv preprint, version 1, flattened from its JATS XML. It has the main text, figure legends, Discussion and Methods. There is no PDF and no supplement. The dandiset's metadata points at version 2 of the preprint, which I did not read. The paper links no code and has no code or data availability statement, so I read no repository.

**Claims.** 20, all with quotes and none inferred.
- **Statistics:** none. The paper reports no tests, p-values or intervals for any finding.
- **Expected values:** 8 claims have them: 7 dishes; activity onset at 2 to 3 DIV; the example dish's shift at about 10 DIV with exponent 1.30; transition at about 15 DIV; exponent about 1.2; avalanche shift at about 15 DIV with exponent about 1.5; the paper's group threshold b = 0.1; the model's exponent 1.56.
- **Criteria:** all 20 claims have one.
- **Model claims:** 2 are simulation claims, recorded so the findings are covered. They cannot be specified from the text: the network size, how the weight distributions scale with g, the run length, the initial state and how model activity is binned for PCA are all missing.

**Details the paper leaves open, with the readings named**
- **The 0.03 Hz rule:** applied per electrode, or per recording.
- **The fitted function:** its formula is lost from the text. I read it as a·x^(−c)·exp(−b·x). The squared error is taken either on log values or on raw values. The ranks fitted for the variance spectrum aren't stated, so the reading is all ranks with a positive eigenvalue.
- **Local Moran's I:** its formula is also lost. Readings are Anselin's normalised form, or the form without the variance normalisation. Whether an electrode counts as its own neighbour is open; the usual reading (it does not) is the default, the other a variant.
- **Locality slope:** "semi-logarithmic" could mean locality against log PC index, or log locality against PC index.
- **Avalanches:** spikes from all electrodes pooled into one train for the mean inter-spike interval. Cascade size is either the number of spikes or the number of distinct electrodes.
- **When the transition happens:** the DIV at which b stays below 0.1, taken either on the 3-day moving average pooled over dishes or per dish then the median.
- **Figure 1E:** which dish is the example, and which spectra the exponent-1.30 line fits (three readings).
- **No measure given:** the shift from asynchronous firing to bursting (two synchrony measures named) and the absent temporal structure of PCs (two timescale measures named).
- **No test given:** for "did not alter", "significantly disrupted", "clear positive correlation", "became steeper" and "nearly independent", the criteria use Spearman/Pearson, Wilcoxon or Mann-Whitney tests at p < 0.05, or 10% bands. These are readings I chose because the paper gives no test, and each criterion says so.
- **Avalanche threshold:** the 0.1 boundary on b is carried over from the PCA groups, because the paper gives none for avalanches.

**Missing from the paper**
- **Supplementary Figures S1 and S2:** their legends are not in the text. So for classifying recordings by avalanches (S1) the threshold is unknown, and for shuffling breaking the co-occurrence (S2) the shuffle and the measure are unknown. Both claims rest only on the Results sentence that cites the figure, and stay open until the supplement is supplied.
- **The Methods equations:** these are garbled in the flattened text, as listed above.
- **The model's parameters:** too incomplete to simulate, as noted under the claims.
