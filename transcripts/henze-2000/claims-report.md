I wrote `claims/crcns-hc-1/10.1152-jn.2000.84.1.390.yaml`, and the quote checker passes it: 21 claims, 21 quotes, 4 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the version of record from `paper/` (Methods, Results, Discussion, legends of Figs. 1 to 8). The paper has no supplement and links no code, so no code was read. The text extraction turns =, <, >, ± and ≈ into a replacement character. I read those signs from the font encodings in the PDF's content streams and listed them in the opening comment. The PDF could not be rendered here, so numbers printed only inside figures were not read.

**Claims.**
- **Quotes:** all 21 claims have one. None is from the abstract.
- **Expected values:** 10 claims have them. The tolerance is the paper's SD where it gives one, otherwise 10%.
- **Statistics:** 3 claims carry 4 values in total:
  - duration correlation, R = 0.66, P < 0.03;
  - Fig. 4D, R = 0.40, P < 0.0001;
  - Fig. 5 theta against non-theta, paired t-test, P < 0.001 for pyramidal cells and P < 0.003 for interneurons.
- **Criteria:** all 21 claims have one.
- **Expected untestable:** 5 claims rest on recordings from sleeping rats that this paper re-examined from an earlier study (Csicsvari et al. 1999a). Fig. 5, the firing-rate claim and Fig. 8 use those recordings; the "silent cells" claim rests on unit counts from other studies. The paper names no archive for them, and the data set's description holds only the anesthetized recordings. The propagation-velocity claim may also depend on them.

**Details left open, with the readings named.**
- **O1:** the spike-detection threshold. A standard choice is used, since it should barely change the averages.
- **O2:** which spikes are averaged: (a) all of them, or (b) spontaneous only, leaving out current steps.
- **O3:** which tetrode channel: (a) the one with the largest spike, or (b) all four, reported.
- **O4:** how the start of each waveform is found. Intracellular: (a) dV/dt above 10 V/s, or (b) maximum of the second derivative. Extracellular: (a) leaving 2 SD of the baseline noise, or (b) maximum of the second derivative. The threshold that defines the intracellular end follows from the same reading.
- **O5:** the 3 kHz low-pass filter, a standard zero-phase choice.
- **O6:** action potential amplitude: (a) from threshold, or (b) from the pre-spike baseline.
- **O7:** extracellular amplitude: (a) negative to positive peak, or (b) the negative peak alone.
- **Per-claim choices:**
  - **Derivative mismatch:** (a) phase correlations, or (b) peak-to-peak timing.
  - **Notch and AHP landmarks:** agreement within (a) 0.1 ms or (b) 0.2 ms.
  - **Interneuron width:** (a) shorter than every pyramidal cell, or (b) more than 2 SD below the pyramidal mean.
  - **Latency against amplitude (Fig. 3B):** (a) Pearson or (b) Spearman.
  - **Back-propagation velocity:** two reference amplitudes and three ways to fit the velocity.
  - **Burst "decrease":** (a) 5th spike below the 1st, or (b) falling from spike to spike from the 2nd on.
  - **Amplitude against distance (Fig. 6):** (a) Spearman or (b) Pearson.
  - **Propagation velocity:** which recordings (anesthetized probe or behaving rats) and how site pairs are formed.
- **Rules the paper never states:** the noise rule for "spike present" and the "majority of cells" thresholds are standard choices, flagged as such in the file.

**Inconsistencies inside the paper.**
- The back-propagation velocity is 1.61 m/s in the Results and Discussion but 1.68 m/s in the abstract. 1.68 falls within the claim's tolerance.
- The Fig. 3B legend says 20 pyramidal cells; the text says 21.
- The Fig. 5 legend gives P < 0.001 for pyramidal cells; the Results text gives P < 0.003 for both groups.

**Missing for some claims.**
- **Fig. 6 and the cell-count estimate:** they need each cell's distance from the tetrode, which came from histology.
- **Figs. 1 to 3:** they need each cell's impalement site (somatic or dendritic) and cell type.
- **Fig. 3A example pair and Fig. 4D:** the paper does not identify these cells, so the criteria name how to find candidates.

Whether the data set holds the distances, sites and cell types is left to the author. The paper itself supplies everything else the claims need.
