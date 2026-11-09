I wrote `claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml`. The quote checker reports 26 claims, 24 quotes, 4 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PMC2525941, open access, from Europe PMC full-text XML): Methods, Results, Discussion, Figure 1 to 10 legends and Table 1. There is no supplement, and the paper links no code, so I read none. No PDF was supplied, so values shown only in figures (Figure 5, Figure 9B, the Figure 7 histograms) could not be read; those claims are judged on direction only. The data descriptor was used only to see which experiments the data set holds: it says Data1 (2003) is the one analysed in this paper.

**Claims.**
- **Quotes:** 24 of the 26 claims have quotes. The two without are Table 1 numbers, so each carries an `inferred` note instead.
- **Statistics:** 3 claims record statistics, 4 entries in all:
  - the one-way ANOVA on firing rate across conditions, p = 0.58;
  - the Fourier-domain two-way ANOVA comparing burst-triggered averages, with Bonferroni correction, p < 0.01;
  - the point-by-point t-test, p < 0.01;
  - the ANOVA comparing each burst-triggered average with summed single-spike averages, p < 0.01.
- **Criteria:** all 26 claims have one.
- **Coverage:** session selection and counts, firing rate, threshold, Table 1 (bursting sessions, isolated spikes, burst length), Figures 3, 5, 6, 7A–H, 8, 9 and 10, the comparison with the direct information method, the model, and the effect of firing rate on the ISI limit.

**Details the paper leaves open, and the readings named:**
- **Burst identification:**
  - Which first peak: the first local maximum after zero lag, or the largest value below 5 ms.
  - Which bounding minimum: the first significant local minimum, or the lowest value before 1.25/cutoff.
  - What σ and N mean in the error Δ = σ/√N: N as all product terms, or as the number of trials.
- **Which sessions count as bursting:** Table 1 implies 63, the Results say 59 cells (Fig 7B) and 58 sessions (Figs 8, 9). Readings: all sessions classified as bursting, or only those with enough bursts.
- **Session selection:** "about 100 Hz" has no bound; readings are the SD < 35 Hz condition alone, or that plus a recorded target rate of 100 Hz. The per-trial rate window is 200–1000 ms, with the full second as a variant.
- **Bin width for information and correlation measures:** 0.1 ms or 0.4 ms. Whether lag zero enters the Fig 6 average: with and without.
- **Slope significance:** within one standard error, or a t-test at p < 0.05. The Fig 7D slope of −2.6 only makes sense on a log scale: log2, ln or log10.
- **Jitter:** how bursts are matched across trials. Readings: peaks of the onset histogram, or windows of the peak domain.
- **Direct method:** rate at the 3.2 ms word length, or extrapolated. "All sessions" is read as the 86 kept sessions, or the bursting ones.
- **Model:** filter length 25 or 50 ms; filter scale as cross-correlation over variance, or matched to the session's mean rate.
- **Burst-triggered-average tests:** frequency bins (all, or up to the cutoff); what "central peaks significantly different" requires (one significant point, or most points); how the ANOVA against summed single-spike averages forms its observations.
- **Figure 10:** STA peak width (between minima, or at half height); the measure of segregation (peak position of P(n|h), or its weighted mean).
- **Latency decreasing "systematically" with n:** within most sessions, or in the population mean.

**Missing from the paper:**
- The Figure 3 example cell, said to be tested with all stimuli, is not identified, and the Methods say each cell had two.
- The firing-rate check behind "a 50 Hz increase shifts the limit by <0.4 ms" names no data or method.
- The model needs each cell's measured threshold, which the data may not hold.
- Two passages are garbled and are read as stated in their claims: "no <69%" is read as "at least 69%", and a ratio prints σ over σ, read as σ over σ_n.
- Figures 5 and 9B give values only in the figures.
