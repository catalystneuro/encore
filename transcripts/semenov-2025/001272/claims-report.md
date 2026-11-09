I wrote `claims/001272/10.1016-j.xcrp.2025.102660.yaml`. The quote checker reports 19 claims, 19 quotes, 7 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main text, figure legends, STAR Methods, and the supplement PDF (Figures S1 to S4, Table S1). I did not read the version of record. There is no main-text PDF, so I could not look at the figures themselves; I read Figure S1 from its legend. The paper says it reports no original code, so I read none and no method detail is settled by code.

**This dataset.** I matched it to the paper from its archive title and description only: "The Use of Di8-ANEPPS to Evaluate Neuronal Sensitivity to Unmodulated Sine Waves". That is the Figure S1 control experiment: eight neurons stained with Di-8-ANEPPS, stimulated with 250-ms, 2-kHz sine waves.

**Claims (19).** Every claim has a quote and a criterion.
- **Tested on this dataset (5):** the count of eight neurons; action potentials appear as drops in emission; one or a few delayed spikes near threshold; stronger fields shorten the delay and give sustained firing; the strongest fields end in sustained depolarization.
- **Need the FluoVolt dandisets 001030 and 001032 to 001035 as well (2):** Di-8-ANEPPS traces are noisier than FluoVolt traces; the effects are the same with either dye.
- **Tested elsewhere (12):** the paper's other main findings, each assigned from the dandiset titles (Figures 1 to 3, S2, 4, 5 and 6, and the threshold depolarization estimate). The paper itself does not say which figure is in which dandiset. The Figure 4 and Figure 6 criteria refer to the existing claims files for 001273 and 001274.
- **Statistics:** 3 claims have them, 7 entries in all. All are from the threshold and Figure 4 findings; the paper reports no test for any Figure S1 finding.
- **Expected values:** 8 claims have them. The neuron count has tolerance 0, because 10% of 8 allows no other whole number.

**Details the paper leaves open, and the readings named.** A claim counts as decided only when every reading gives the same outcome.
- **Soma outline:** taken from the dataset if it holds one. Otherwise (a) an Otsu mask of the mean pre-stimulus frame, keeping the part nearest the image centre, or (b) that mask shrunk by 2 pixels.
- **Baseline interval for F0:** (a) all frames before the stimulus (about 50 ms), or (b) the last 20 ms before it.
- **Spike detection for Di-8-ANEPPS:** the paper gives no level for this dye. Readings: (a) a peak above 5% (the Methods' level for FluoVolt), or (b) a peak above 5 SD of the pre-stimulus trace. Both require a width of 2 to 20 ms, which is a standard choice.
- **"Near the threshold":** (a) sessions at the threshold field, or (b) sessions up to 10% above it.
- **"Delayed":** (a) the first spike at least 100 ms after onset, the lower end of the range the paper gives for FluoVolt, or (b) later than the same neuron's spikes at higher fields.
- **Sustained depolarization:** no spike in the last 100 ms of the stimulus while the signal stays above (a) 5 SD of baseline, or (b) half the neuron's median spike height.
- **Standard choices:** "a few" as 1 to 3 spikes; majority rules across neurons; a Spearman correlation for the delay falling with field.
- **"Noisier":** (a) signal to noise ratio, or (b) baseline SD.
- **Elsewhere claims:** whether "all thresholds" means one test per group or one pooled test, and whether the 60 to 90 Hz ceiling applies to the median neuron or to every neuron.

**Missing from the paper.**
- No test, measure or count for any Figure S1 finding, and no spike detection rule for Di-8-ANEPPS.
- No mapping from figures to dandisets.
- No statement of whether the Di-8-ANEPPS sessions were a threshold search. If they were not, the lowest firing field tested is only an upper bound on the threshold, so the comparison with the FluoVolt threshold of 57.7 ± 3.6 V/cm is limited; the criterion asks the notebook to report the gap to the next lower field.

The paper spells the dye "Di-8-ANEPSS" once in the Results and "Di-8-ANEPPS" elsewhere; it is the same dye.
