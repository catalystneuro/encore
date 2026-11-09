I checked the claims file for CRCNS:ssc-7 against the paper and corrected 11 claims and two of the shared method notes. I also added one claim, so the file now has 48. I marked it ready for an attempt.

**Checker result:** `claims/crcns-ssc-7/10.1038-nn.4412.yaml: 48 claims, 48 quotes, 20 statistical values, 0 problems`. Before my changes it read 47 claims, 47 quotes, 21 statistical values, 0 problems.

**Changes, by claim**
- **Shared method notes:**
  - The significance test note called 0.046 the smallest P value the paper lists. It is the largest; corrected.
  - The distance-to-threshold note gave only one reading (spikes removed). The Methods don't say, and the axes of Fig. 4h go below 0 mV, so I added "spikes kept" as a second reading.
- **behavior-performance:** added the open reading of counting touches before the first lick, since the Methods say mice touched "multiple times ... before reporting perceived object location with licking".
- **vpm-whisking-rate:** reading (b) took its window from a figure's plotted range, which the paper never defines as a measure. It is now only a variant, and reading (a) decides the claim.
- **l4e-example-e1:**
  - The rule "six of seven values in tolerance" wasn't from the paper. Now all seven must hold, with a partial result when one fails.
  - The 0.4 spikes/s can be read as the increase or as the whisking rate, so both readings are listed.
- **l4e-inhibition-window:**
  - The criterion contradicted the expected values and would have passed if every neuron's delay were 0.4 ms. The smallest and largest delays must now match the range bounds.
  - The tolerance on −0.8 ms is now 0.1 ms, one sample at 10 kHz, because 10% (0.08 ms) is below the sampling interval.
- **l4e-whisking-inhibition:** the criterion now says which windows come from Supplementary Fig. 4 and which are fixed here.
- **thalamus-inhibition-dose:** the statement also claimed dose dependence for VPM multiunit rates, which the paper does not state. I trimmed it; the multiunit test stays as a variant.
- **ion-cut-l4e-phase:** the Fig. 7e legend doesn't say the controls are the 15 matched neurons. I added the reading with all 37 control neurons, with its own tolerance.
- **enphr-auc-groups:** the rule "five of six rates" wasn't from the paper. Now all six must hold, with a partial result when one or two fail.
- **enphr-behavior:** I removed the chi-squared p < 0.05 entry. It is a threshold used to count mice, not a result.
- **New claim, fs-hf-fluctuations** (Supplementary Fig. 8): in fast-spiking interneurons, high-frequency fluctuations rise with whisking in some cells but not others. This Results finding had no claim.

**Still open** (recorded in the check entry)
- Two minor Results statements still have no claim:
  - phase modulation of excitatory-neuron Vm (Supplementary Fig. 3), partly covered by ion-cut-l4e-phase;
  - reduced fast-spiking Vm fluctuations under thalamic photoinhibition (Supplementary Fig. 9g,h), shown for one example neuron.
- Neither reader read the paper's code, which is the dataset's `example_analysis_code` folder. The author may use it to settle the details named as open.
- Eight criteria use tests, bands or margins the paper does not give. Each says so, and their outcomes will rest on those choices.

**Ready:** yes. Nothing was committed or pushed.
