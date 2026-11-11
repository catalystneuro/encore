I wrote `claims/dijk-2018.yaml`: 44 claims, all with quotes. The checker passes except for three p-values it cannot parse, which I confirmed by reading the text.

**Text read:** the version of record (Neuron 98, 832–845), with its STAR Methods and the supplement (Figures S1 and S2, Tables S1 and S2). I read no figure from the PDF. I read the CRCNS data descriptor only to see which experiments the dataset holds.

**Code:** the GitHub repository the paper links (FentonLab/Mcode_DG-MemoryDiscrimination-NeuronMS, commit 3542a85, its only commit) has no code. It holds a one-line README and a macOS alias file, so the code settles no method detail.

**Claims:**
- **Counts:** 44 findings, all quoted, with 89 statistical values. Every claim has a criterion, and 10 also have expected numbers.
- **Coverage:** the environment-remapping experiment (Figure 1, Table S1), the optogenetic behaviour (Figure 2), stability and rate remapping in the avoidance task (Figure 3, Table S2), Ipos and ΔIpos frame preference (Figure 4), overdispersion and network consistency, place cell to interneuron correlations and their changes (Figure 5, Figure S2), and avoidances against errors (Figure 6).
- **Checker:** the three values it flags (Figure 2D 1e-07, Figure 5D4 1e-06, Figure 5E4 1e-05) are printed "10�7", "10�6" and "10�5" in the text (lines 374, 898 and 908). Two quotes were cut with "..." where the text has garbled glyphs.

**Details the paper leaves open, with the readings named:**
- **Cell classes (M1):** the features are listed but no cut-offs. The paper's own class lists are to be used; without them, the claims that need classes are methods_underspecified.
- **Rate maps (M2):** (a) unsmoothed, every visited pixel; (b) pixels with less than 0.67 s of occupancy left out.
- **Place field definition (M5):** not given at all. I named two standard choices, which the paper does not make: (a) at least 9 contiguous pixels above 20% of peak; (b) the same above 1 AP/s. Claims on field counts or field masks rest on this assumption.
- **Rate remapping (M4):** absolute value is the main reading; the signed ratio is a variant.
- **Ipos location bin (M6):** (a) 1.5-cm pixels; (b) 3-cm blocks.
- **Local minima of distance to the shock zone (M8):** (a) raw 30-Hz series; (b) a 1-s moving average.
- **Episodes for standardized rates (M10):** (a) consecutive 5-s windows; (b) windows centred on field entries.
- **Session pairs for each manipulation (M11):** (a) the adjacent sessions; (b) all pairs, averaged per cell.
- **Random term of the mixed ANOVAs (M12):** (a) mouse; (b) cell or pair nested in mouse; (c) an ordinary ANOVA. The printed df pick the reading.
- **Per claim:**
  - Which pairs count as positive, negative or independent: (a) Kendall test at p < 0.05; (b) a time-shift null. Also which pretraining session: 1, 2, or both.
  - Normalizer for Ipos near the zone: (a) room Ipos; (b) room plus arena Ipos.
  - What "increased" co-firing means: (a) change above 0; (b) above 1 SD.
  - Meaning of "overlapping" fields for network consistency.
  - Window for running speed.
  - Which sessions enter the Figure 2D ANOVA.
  - Which mice enter the Figure 3B ANOVA (its df are 2 and 4).
  - The SD used for zone-vicinity correlation changes.

**Missing from or inconsistent in the paper:**
- There is no analysis code.
- No place field definition and no cut-offs for cell classes.
- Field-count SEMs differ between the Results and Table S1 (I used the Results).
- Mouse counts for Figure 1 differ: 5 + 3 mice in the Results, seven in the Methods.
- The Figure 1B interaction is printed without its F value.
- The overdispersion F-test p-values (0.17 and 0.63) look inconsistent with their df. I recorded them as printed.
- Figure 6C reports no statistics for the correlations, so I judged it on the same ANOVA as Figure 6B.
- The data descriptor mentions wild-type mice only, so the optogenetic data (Figure 2) and the shock-on behaviour (Figure 3B, top) may not be in hc-17. That is for the author to establish.

Nothing has been committed. The other untracked files in the working tree are not mine.
