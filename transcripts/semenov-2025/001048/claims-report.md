I wrote the claims file at `claims/001048/10.1016-j.xcrp.2025.102660.yaml`. The quote checker passes it: 19 claims, 19 quotes, 8 statistical values, 0 problems. But this dandiset does not hold this paper's data, so none of the claims can be tested on it.

**The dataset mismatch.** DANDI:001048 (version 0.250701.1624) is titled "Plasma membrane conductance changes in response to supraphysiological hyperpolarization". Its description covers membrane lesions in HEK cells, species human. The paper studies rat hippocampal neurons stimulated by sine waves and has no HEK cell or hyperpolarization experiment. Its Data and code availability section lists ten dandisets (001030–001035 and 001271–001274), and 001048 is not one of them. The two share authors and NIH grants, which may be why the dandiset names the paper. So every claim is marked `data: elsewhere`. Each one points to a dandiset and published version that I matched from DANDI titles only, because the paper doesn't say which figure is in which dandiset.

**Text read.** The NIH author manuscript (NIHMS2098259, PMC12320893) from Europe PMC: main text, figure legends and STAR Methods, plus the supplement (Figures S1–S4 and Table S1). I did not read the version of record, and there is no main-text PDF. The paper says it reports no original code, so no code was read.

**Claims.**
- **What they cover:** the AP selection, firing and the excitation block under unmodulated waves, the 20 kHz versus 2 kHz thresholds, the modulated versus unmodulated thresholds and firing patterns, low conductivity, heating, the 2-s ramp, Di-8-ANEPPS, TTX, the charging time constants, the sine-wave asymmetry, the sine versus pulse sensitivity, and the threshold depolarization estimate.
- **Statistics:** 4 claims carry 8 tests. These are two-tailed unpaired t tests (p < 0.0001, 0.0079, 0.0142, 0.0037), paired and unpaired t tests for Figure 4, and the regression p < 0.0001 (printed in the paper as "<0.01%").
- **Expected values and criteria:** 13 claims have expected values with tolerances, and all 19 have criteria.

**Details the paper leaves open, with the readings named:**
- **Soma region:** (a) Otsu threshold component nearest the centre, (b) that region eroded by 2 pixels.
- **Baseline interval:** (a) all frames before onset, (b) the last 20 ms.
- **AP detection:** (a) peaks above 5% dF, (b) above 5 SD of the baseline.
- **"Sustained depolarization":** (a) mean dF above 5 SD of baseline, (b) above half the median AP height.
- **Debris-ROI scaling:** (a) scaled, (b) unscaled.
- **LOESS span:** (a) 2 ms, (b) 4 ms.
- **AP measures:** (a) every AP or (b) the first per session; duration as (a) half-height width or (b) time back to the baseline.
- **Firing-rate ceiling:** (a) for the median neuron, (b) for at least 75% of neurons.
- **The single p for "all thresholds":** (a) one test per stimulus, (b) one pooled test.
- **Whether 57.7 V/cm is the 1-AP threshold:** read as the 1-AP threshold, with the 5-AP mean reported beside it.
- **Extrapolation to 2 mS/cm:** (a) proportional, (b) linear, (c) exponential.
- **Heating formula:** (a) peak or (b) RMS field, with water's heat capacity.
- **Discharging fit:** (a) free amplitude, (b) amplitude fixed at the end of the pulse.
- **Figure 4 tests:** (a) as in the Results or (b) as in the legend; the two give different p bounds.
- **Asymmetry measure:** (a) regression-based, (b) largest per-cycle difference.
- **Sine sensitivity regression:** (a) signed values, (b) per-cycle amplitudes.
- **Figure 2D:** the legend's unpaired test is followed, with a paired test as a variant, since the thresholds come from the same neurons.

**Missing from the paper.**
- No figure-to-dandiset map.
- No neuron counts for the TTX experiment, the block and Figure 2.
- No heat capacity or field definition for the temperatures: the paper's own numbers give neither 2.5 °C (peak about 3.9 °C, RMS about 1.95 °C), so that claim may end up blocked as `methods_underspecified`.
- No measure of the extrapolation to 2 mS/cm.

Nothing was committed.
