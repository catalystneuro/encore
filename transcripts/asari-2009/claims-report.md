I wrote `claims/asari-2009.yaml`, and the quote checker passes it: 21 claims, 19 quotes, 2 statistical values, 0 problems. Nothing is committed.

**Text read**
- **Version:** the version of record (J Neurophysiol 102:2638–2656), as a text extraction of the PDF, with its Methods and figure legends.
- **Garbled symbols:** the extraction breaks Greek letters, <, >, ~, = and ± into a replacement character. I read them from context and cut quotes around them. The PDF pages could not be rendered here because no rendering tool is installed, so I could not check them against the page images. Every value in the file is printed in the text or a legend.
- **Supplement:** Supplemental Figs. S1–S10 were not supplied and I did not read them. The main findings rest on main-text Figs. 2–9, so I went ahead. The one finding that comes from the supplement (`figs1-silence-probe`, effects after the silent gaps between sequences) is quoted from the Methods only.
- **Code:** the paper links none; it only says the analysis was done in MATLAB.

**Claims**
- **Quotes:** 19 claims have quotes. The other 2 are marked `inferred`: the fit values that appear only in the Fig. 3A and Fig. 8A legends.
- **Statistics:** 2 claims have them. They are the per-time-point Kruskal–Wallis tests (P < 0.01 for at least 5 ms) for the example cells of Figs. 2 and 7. The paper reports almost no tests as results. The 95% intervals of Fig. 8C exist only in the figure.
- **Criteria:** all 21 claims have one.

**Details the paper leaves open, with the readings named**
- **Silence as a context:** whether it counts among the contexts in Figs. 3 and 4. Readings are counted (the main one, since Fig. 2B uses it) and not counted.
- **Population average at time t:** whether it is over all probes or only those still running at t.
- **Exponential fits:** the fit range (0–4 s, 0–4.72 s or 0–6 s). Start values are a standard choice.
- **Trial correlation:** mean over all pairs of trials, or each trial against the mean of the others. Also whether the population mean is over cells or over probes.
- **Firing rates:**
  - Spike detection settings are not given, and the paper never says how A1 spikes were detected.
  - Spontaneous window: the gaps between sequences, or a pre-stimulus baseline.
  - Evoked window: all sound periods, or the probe periods.
- **Synaptic conductances:**
  - Which period counts as spontaneous (needed for the noise variance).
  - Any smoothing of the conductances.
- **MGB:** whether a 100-ms PSTH bin is timed at its start or its centre.
- **STRF models (Fig. 4):**
  - The spectrogram window: 10-ms or 20-ms Hann.
  - The response sampling: 4-ms bins or the raw trace.
  - How the cross-validation folds are formed: contiguous blocks or by stimulus.
  - "Did not improve significantly" names no test. I named a paired Wilcoxon test and a repeated-measures test across the nine windows.
- **Fig. 8C resampling:** what one of the "1,000 samples" is. Readings are probes, or trials within each probe and context.
- **Noise autocorrelation:** "decays within ~100 ms" is undefined. I used the lag where it falls below 1/e, with 0.1 as a variant.
- **Natural against synthetic probes:** the paper reports "no difference" without a test. I fixed Fisher's exact test with Bonferroni correction, and the outcome is marked as resting on that assumption.

**Missing from the paper or inconsistent**
- **Example cells:** the paper gives no identifiers for the example cells of Figs. 2, 5, 7 and 9. Those four claims say how to find a matching recording and are not testable if none matches.
- **Frequency percentage:** the paper prints 64.6% for frequency, but 73/110 is 66.4%. The count is what the claim tests.
- **Supplement:** without Fig. S1, the silence-gap claim has no numbers to match.
