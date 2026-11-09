I wrote `claims/kim-2020.yaml`. The checker reports 45 claims, 41 quotes, 97 statistical values and 0 problems.

**Text read:** the version of record (PMC7046699, Europe PMC JATS text), with its Results, figure legends, Tables 1 and 2, Methods and the Supplementary Information (Supplementary Figs. 1 to 3 and their legends). I did not need the PDF. The paper links no code repository, only the CRCNS dataset. The dataset's description says it holds a "codes" folder of Matlab scripts, but those are dataset files, so I did not open them and no method comes from them.

**Claims:**
- **Quotes:** 41 of the 45 have one. Four are marked `inferred`: three are read from Table 1 or Table 2 alone (total bandwidth, latency and duration, E/I latency and duration). The fourth is the Table 1 event-rate claim, whose note gives only the p-values.
- **Statistics:** 29 claims carry them, 97 values in all, including every Table 1 and Table 2 p-value that a claim rests on.
- **Criteria:** 44 claims have one; the counts claim for voltage clamp is settled by its expected values alone.
- **Expected values:** 38 claims have them. Means given as mean ± s.d. use the s.d. as tolerance; other values use 10%. Recorded cohort counts use 0, and counts that come out of an analysis use 10%.
- **Claims of absence:** eight claims (no difference or no correlation) are judged on the paper's own test only.

**Details the paper leaves open** (numbered D1 to D17 in the file's opening comment, each with its readings):
- **D1, spikes vs PSPs:** how spikes are told from PSPs among detected peaks. (a) a cut at the gap in each neuron's peak-amplitude histogram; (b) an action-potential criterion on the trace.
- **D2, amplitude reference:** (a) peak voltage minus resting potential; (b) the peak detector's height above the neighbouring minimum.
- **D3, baseline for the 4× and 3× s.d. cuts:** (a) stretches without stimulus; (b) quiet stretches during the DMR.
- **D4, bimodality test:** none is named. (a) two maxima with a trough between them; (b) Hartigan's dip test.
- **D5 and D6, STRF window and shuffle count:** neither is stated; I used standard choices.
- **D7, "significant subfield":** (a) any significant positive pixel; (b) a contiguous significant region.
- **D8, STRF bandwidth:** not defined. (a) the spectral extent of the significant region, with total bandwidth spanning the gap between peaks, which the Fig. 3 examples support; (b) the width at half maximum. It is also unclear how 31 single bands come from 30 neurons.
- **D9, double-peaked STRF:** (a) two separate significant subfields; (b) two maxima with a dip between them.
- **D10, latency and duration:** neither is defined. Latency: (a) delay of the STRF peak; (b) onset of the significant region. Duration: (a) extent of the significant region; (b) width at half maximum.
- **D11, modulation transfer functions:** (a) computed from the significant STRF or (b) from the full STRF; also how bandpass is told from lowpass.
- **D12, nonlinearity fit:** whether projections use the significant or the full STRF. The fitted power-law function itself is only cited (refs. 19, 28, 29), not printed.
- **D13, feature selectivity index:** the details beyond ref. 19 are standard choices, using the same STRF as D12.
- **D14, resting potential:** (a) median over the recording; (b) mean of the pre-tone baselines.
- **D15, tonal receptive field:** the response region, how bandwidth at 30 dB above threshold is measured, and whether Q uses bandwidth in kHz or octaves.
- **D16, "maximum PSP amplitude":** (a) the largest PSP per neuron; (b) the mean over responsive tones.
- **D17, "power fit" correlations:** (a) Pearson r on raw values; (b) on log values.
- **Single claims:** some claims name their own readings:
  - the frequency scale for best-frequency statistics (kHz or log)
  - the test for "PSP STRFs more reliable than spike STRFs" (paired t-test or signed-rank)
  - two readings for "closely matched" excitatory and inhibitory best frequencies
  - two readings for the Fig. 5c counts, which do not add up (20 − 13 = 7, but the text says 9)

**Missing from the paper:**
- **Nonlinearity fit:** the equation for the threshold (θ) and transition (σ) fit is not given; it is only in the cited refs. 19, 28 and 29, which were not supplied. The four claims resting on it say that they are blocked as methods underspecified if no paper source supplies the equation.
- **Definitions:** the paper never defines STRF bandwidth, latency, duration or double-peakedness, nor how spikes are separated from PSPs.
- **Supplementary data:** the dataset description says only one example neuron is held for Supplementary Figs. 2 and 3. Those claims say what to report if the data are short.
