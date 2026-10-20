I've written `claims/crcns-ret-1/10.1242-dev.027912.yaml`. The quote checker passes: 26 claims, 26 quotes, 6 statistical values, 0 problems. Nothing is committed.

**Text read.** The NIH author manuscript from PubMed Central (PMC2644426): Methods, Results, Discussion and the legends of Figures 1 to 9, with the published abstract appended. There was no PDF. The paper links no code, so none was read.

**Supplement.** Supplementary Figures 1 to 3 are missing. I went ahead because they hold only figures, and the electrophysiology methods (Eqns 1 to 3) and Figure 9 are complete in the main text. Four claims cite them: Chx10-Cre recombination (S1), synapse density in Bax mutants (S2, whose test is therefore unnamed), and receptive field surrounds (S3, whose criterion therefore names its own readings for what counts as a surround). They are quoted from the main text and take no number from the supplement. The manuscript also cites S2 both for synapse density and for example spike-triggered averages. Supplying the supplement would settle the synapse-density test and the surround criterion.

**Claims.**
- **Quotes:** all 26 have one; none needed `inferred`.
- **Statistics:** 9 claims carry them, all histology (ANOVA with Tukey, Student's t-test, Mann-Whitney; p < 0.01, 0.0001, 0.001, 0.05).
- **Expected values:** 8 claims, including the Figure 9 cell counts of 115 mutant and 143 control.
- **Criteria:** all 26 have one.
- **Testable on this data set:** 16 claims are histology or immunostaining, which the data set does not hold. The 10 Figure 9 claims are the ones it can test.

**Details the paper leaves open, with the readings named:**
- **95% bands on the Figure 9 cumulative histograms.** These are the paper's only comparison, and it doesn't say how they were built. Readings: a pointwise binomial interval, the Dvoretzky-Kiefer-Wolfowitz band, or a bootstrap over cells.
- **Splitting the spike-triggered average into b(x) and a(t).** Readings: the leading singular vectors, or slices through the largest absolute value.
- **Time to peak of a(t).** Readings: at the 16.6 ms frame resolution, or with parabolic interpolation.
- **Fitting the Linear-Nonlinear model.** Readings: least squares on the rate binned per frame, or on the mean rate in bins of the model input. The printed nonlinearity `B + G·y` is discontinuous at the threshold, so the continuous `B + G·(y − θ)` is named as a second reading.
- **Response classes (Figure 9A).** The paper defines no cut-offs for ON/OFF/ON-OFF or for transient against sustained. Two sets of cut-offs are named.
- **Direction selectivity (Figure 9B).** No index or threshold is given. Readings: a vector-sum index above 0.3, or preferred against opposite above 0.5, each with a shuffle test.
- **Surrounds (S3).** A lobe of opposite sign beyond 10% or 20% of the centre peak.
- **Standard choices that shouldn't change outcomes:** a 0.5 s spike-triggered average window and linear interpolation for the receptive field width.
- **Cell selection.** Read as all cells in each group, since the legend gives one count for every panel.

**Inconsistencies and gaps in the paper:**
- The Results name the mutant allele fcon3, while the Figure 9 legend says f-del.
- Mouse age, number of retinas and flash intensities for the recordings are not given.
- In Figure 5, the Results and the legend disagree on which layers show more apoptosis at P0 and P7, and the panel letters don't match. Both versions are named.
- The Figure 6F significance marks aren't assigned to bars.
