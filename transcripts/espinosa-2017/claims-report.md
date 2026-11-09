I wrote `claims/espinosa-2017.yaml`. The quote checker passes apart from two p-values it cannot parse ("4.10×10−5" in the Figure 1D legend and "4.94E-04" in Supplementary Table 2). I checked both by reading and noted them in the opening comment. Nothing is committed.

**Text read:** the version of record (Cereb Cortex 29:42–53) with its whole supplement: Supplementary Figures 1–14 and Tables 1–3. The full text, Methods and supplement were all present. Figures were read from their legends and the Results text; I didn't need the PDF. The supplementary movies were not supplied, and no claim depends on them alone.

**Code:** the paper links no analysis code of its own. The gamma-detection toolbox it names (LAN-toolbox, at a wikispaces.com address) did not respond. The Bitbucket copy named in the data descriptor asks for a login. The MATLAB scripts in the dataset were written for a later paper, and I didn't open them because they sit inside the dataset. So every method in the file comes from the Methods, Results, legends or supplement.

**Counts:** 27 claims, all with quotes and none marked as inferred. All 27 have criteria, 26 record statistics, and 21 have expected values with tolerances.

**Details the paper leaves open, with the readings named:**
- **Which units count as responsive:** the paper compares 100 shuffles "bin to bin" at P < 0.01. Readings: (r1) the mean rate over the light pulse is beyond all 100 shuffles; (r2) any bin during the pulse is beyond them; (r3) a rank-sum test at P < 0.01. The baseline rate used to normalize also has three readings: the 5 s before each pulse, the 15 s before it, or the rate over the recording outside pulses. The bin is 500 ms in the Methods and 250 ms in Figure 1C; 250 ms is a variant.
- **Time-constant fit (Fig. 1E):** fit from light onset to the first extremum, or over the whole 5-s pulse, each with either bin size.
- **Fig. 1D pairwise tests:** the legend gives three p-values without saying which pair each belongs to.
- **Basal firing rate:** the rate outside the pulses, or the rate in the 5 s before each pulse.
- **Coherence (Fig. 2E):** averaged across pulses before computing, or computed per pulse and then averaged.
- **Unit of the test:** per animal or per pulse for low gamma power and gamma episode density; per trial or per mouse for the Figure 5 t-tests.
- **Movement amplitude (Fig. 5):** the mean or the maximum of the movement measure from 20 to 60 s after train onset.
- **Slow oscillation "epoch":** one per pulse, or one per pulse and channel.
- **Cortical depth bins and "deeper layers":** not defined; equal-depth bins or probe rows, with the lower two or three bins counted as deep.
- **Unit sets:** which 64 units enter the drug test; the prefrontal/infralimbic counts (381 + 146) exceed the 387 excited units of Figure 2C; the cell-type counts give 2,895 units against 1,308.
- **Figure 2D:** the light-power levels are not listed, and the ANOVA is described both as repeated-measures and as plain two-way.
- **Figure 3B:** the time intervals are not listed.
- **Supplementary Table 1 and Figure 1 legend:** the table's EYFP/marker overlap percentages differ from the legend's 91% and 5%.

**Contradictions inside the paper, recorded in the claims they affect:**
- The Results say discharge is higher in infralimbic cortex; the Supplementary Figure 6 legend gives prelimbic as higher.
- Low gamma power has P = 0.0226 in the Results and P = 0.0018 in the Figure 4G legend.
- The interneuron comparison is an unpaired t-test in the Results and a signed-rank test in the legend.
- Phase modulation is significant over the first 3 s in Supplementary Figure 10B, but only over 3–5 s in the Results and 10C.
- The behavioral pulse train is 1 Hz in the Methods and 0.5 Hz in the legends.

**Missing data:** nothing a claim needed is missing from the paper. Going by its description, the dataset holds the ventral pallidum recordings: 4 animals and 330 units, which matches Figure 1 (56 + 29 + 245). It also holds open-field videos. It does not mention the prefrontal recordings behind Figures 2–4. Whether it holds them is for the author to establish.
