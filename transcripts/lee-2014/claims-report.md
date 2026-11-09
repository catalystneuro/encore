I wrote `claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml`, and the quote checker passes it with 0 problems.

**Text read.** The version of record with its Supplemental Information, from `paper/`. That covers the main text, Experimental Procedures, the legends for Figures 1–6 and S1–S5, Table S1 and the Supplemental Experimental Procedures. Values that appear only in figures (S1E–H and S3F) were read from rendered PDF pages, and the file marks them as read from a figure.

**Code read.** The model code the paper links, ModelDB 153280 ("superdeep", README dated May 15, 2014, zip sha256 recorded in the file). It holds only the network model. It has no analysis of the experimental cells, so it settles none of the intrinsic-property criteria. Two other links in the paper are dead: the lab page is a parked domain and the Open Source Brain page returns 404.

**What the dataset holds.** Current-step sweeps from 8 superficial and 9 deep pyramidal cells (PCs) and 6 PV+ basket cells (PVBCs). These match the n of Figure S1E–H and the step protocol in Supplemental Experimental Procedures 8A. Six claims concern these recordings: I-F curves, input resistance, resting potential, sag, rheobase, and PVBC firing (Figure S3F). The other claims cover the paper's main findings, whose data the dataset does not hold. The two model claims need runs of the ModelDB code, so they are marked `with_inputs`.

**Counts.**
- 34 claims.
- 32 have quotes. The other 2 have `inferred` notes: the Table S1 rheobase and the Figure S3F values.
- 25 have statistics, 29 have expected values, and 13 have criteria.

**Details the paper leaves open, with the readings named:**
- **Firing frequency:** spikes per 1 s step, or (n−1) over the time from first to last spike (the form the Figure S3E model legend implies). The I-F claim is a claim of absence judged on the paper's two-way ANOVA; a repeated-measures ANOVA is shown as a variant.
- **Input resistance:** slope of a linear V–I fit, or the mean of ΔV/I. The 0.8–1.0 s window and the ±100 pA steps come from the Methods.
- **Sag:** which step to use: −400, −300 or −200 pA. Steady state is taken at 0.8–1.0 s, borrowed from the input-resistance method.
- **Resting potential:** how it was measured is not stated. Table S1 says an unrecorded tonic current was applied during the sweeps. If the files show a holding current, the claim cannot be tested on them.
- **Rheobase group value:** median of per-cell values, mean rounded to the 50 pA step, or the first step where the group-mean I-F curve is above zero.
- **Figure S3F PVBC:** the cell is not named. Readings: any one of the dataset's 6 PVBCs, or their mean.
- **Tests:** the text never says which test each comparison used. Each claim records the Methods rule: two-tailed t test, switching to Mann-Whitney or Wilcoxon when Shapiro-Wilk fails.

**Gaps and inconsistencies in the paper:**
- Sag amplitude and the I-F values exist only in figures, as noted above.
- The release-probability comparison in Figure 3 prints "p < 0.05" in a sentence that reports no difference. The statistic is recorded as printed, and the criterion follows the sentence's words.
- The Figure 6G connection probabilities give no denominators.
- The simulation results are not deposited anywhere: the README offers them on request.

Nothing the claims need is missing from the text.
