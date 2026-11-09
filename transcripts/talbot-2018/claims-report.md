I wrote `claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml`: 32 claims, all from the Neuron paper, and nothing committed. The quote checker passes every quote. It still reports 6 problems, all p-values printed as powers of ten that it cannot find (1e-8, 1e-6, 1e-7, 1e-10, 1e-7, 1e-6). I confirmed each by reading the text.

**Text read.** The version of record with its supplement (Figures S1 to S6, Tables S1 and S2), from the PyMuPDF text: Results, Discussion, figure legends and STAR Methods. The PDF pages could not be rendered here, so no figure was read from the image. The second paper under `paper/` (Dvorak et al., PLoS Biol) and the data description were read only to know what the dataset holds.

**Code read.** All three repositories the paper links:
- **SpikeField 4dfbc35:** Morlet wavelets on 2 to 250 Hz, where the Methods say 2 to 100 Hz.
- **CorrelateBPFSpikeTrainEpisodes 150c2df:** Kendall tau-b, a bin-gating rule (only bins where the mouse is in pixels at or above the cell's mean rate) and 300 s episodes. It has no speed filter and does not compute PCo.
- **PositionalInfo 9f186c5:** Ipos in natural log, with the sign kept unless an option is set.

**Counts.**
- 32 claims; 31 have quotes and 1 is `inferred` (the Table S1 difference in non-spatial pyramidal cells' active pixels).
- 29 claims carry statistics, 104 recorded values in all.
- 30 have criteria; 2 rest on expected values and statistics alone.

**Details the paper leaves open, and the readings named:**
- **Which bins enter Kendall tau:** every bin, since the Results call it location-independent; or the code's gated bins.
- **Which period gives a pair's tau:** the whole session, or the first 5-min interval (Figure 4D legend).
- **Recurrence intervals:** the two halves of the recording (Results), or the first two 5-min intervals (legend and code).
- **Place-cell percentage denominator:** all 226 and 334 cells, which matches the printed percentages; or the principal cells the sentence names.
- **Ensemble correlation in Figure 5C:** ΔIpos (Methods) or |ΔIpos| (Results and legend).
- **Place field and in-field rate (Figure 2E, 2F):** not defined anywhere. Readings: contiguous pixels above the cell's mean rate, or above 20% of its peak.
- **"The box" in Figure 2:** the large box, the small box, or both.
- **Square-versus-cylinder pairs (Figure S4):** read as a box and the stationary arena on the same day.
- **Minimum passes per cell for overdispersion:** 2, 10 or 30 (80 and 98 cells against 108 and 141 place cells).
- **"Errors during training" (Figure 6):** Train 1-3, or all shock-on sessions.
- **How quiet and sleep periods are identified:** the data's own labels, or speed below 2 cm/s.
- **Other open items:**
  - classification session
  - placement of the 5 s pass intervals
  - interspike interval measure
  - number of phase bins for the MSE
  - log transform in Figure S6
  - one- or two-tailed test in Figure 6
  - whether locomotion is analysed per mouse or per recording

**Inconsistencies in the paper, recorded in the criteria:**
- The printed z values for the interneuron and place-cell proportions (9.4 and 2.04) cannot be recovered from the printed counts. A pooled two-proportion test gives about 4.7 and 1.3.
- The extracted Table S2 lists 11 WT mice; the text says 12.
- The Figure 4D legend gives p = 0.09 for Fmr1-null at 125 ms, against "all significantly different" in the Results.
- The phase spreads (±50 to 76°) cannot be SEMs, so the angle tolerance is set to 36°, 10% of a cycle.

**Missing from the paper.** No claim was blocked. The dataset's description lists only spike times and positions: no LFP, no waveforms, no slice recordings and no avoidance sessions. The claims that need those (Figures 1, 3, S1, S3 width, S5A and 6, and the waveform-based cell classification) are kept as the paper's findings, for the author to judge.
