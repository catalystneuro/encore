The claims file for espinosa-2017 is fit for an attempt: I corrected what was wrong and marked the last check `ready: true`. Nothing is committed.

**Checker:** `claims/espinosa-2017.yaml: 27 claims, 27 quotes, 49 statistical values, 2 problems`. The two problems are p-values printed in forms the checker cannot match: 4.10×10−5 in the Figure 1D legend and 4.94E-04 in Supplementary Table 2. I found both in the text by reading.

**Changes, by claim:**
- **Opening comment, how responsive units are found:** the file listed three ways to normalize firing to a "basal rate", all made up. The Methods define it: spikes in a bin divided by all spikes in the 30-s window around each pulse. I put that in and named the one open choice, normalizing pulse by pulse (n1) or after summing over pulses (n2). I also added the bin alignment the Methods give, and moved the definition of percent change here, citing the Supp. Fig. 5A axis. Separately, I recorded that the Supp. Fig. 4 legends give 15 to 25 mW where the Methods give 4 to 6 mW for that probe.
- **supp1:** the file said the legend's 91% and 5% fit no denominator in Supp. Table 1. They are the share of EYFP+ cells that carry each marker (87 of 96, 3 of 63, 0 of 22), and the criterion now tests that.
- **supp2:** the Results say light also cuts current-evoked firing in SOM+ cells only (Supp. Fig. 2J, 2K, p < 0.05), and the claim left this out. I added it, using the paired t-test the Methods name, since the legend names no test.
- **supp3:** I split the one entry covering three evoked-firing tests into three, and added the 50 and 150 pA values. The membrane-potential test was recorded but missing from the statement, so I added it there.
- **fig1-bf-response-classes, fig2c:** the criteria now use n1/n2. For fig2c I noted that pairing each unit with its shuffles is a reading, and that it fits the reported W.
- **fig2d:** the statement said "only about 10%" of units respond in NpHR− animals. The legend says "a minimum of ~10%", so I corrected it.
- **fig2e:** the Methods compute coherence "for each 5 s epoch" and then average, so that is now the main reading and the pooled Chronux average is the variant.
- **supp9-layers:** no combination of the legend's depth bins gives 79.8% (closest is the middle two, 80.6%). I said so and added that combination as a reading.
- **supp9-interneurons:** the criterion now says the paper gives no test for "similar proportions", so the chi-square test is a choice. The legend's counts show the excited units come from the 2,895-unit set, not the 1,308 units of Figure 2C.
- **supp10:** the paper does not say which phase is binned. The two readings are the phase at light onset and the phase of each spike.
- **suppt2:** the statement covers high gamma events, but their three t-tests from Supp. Table 2 were missing, so I added them.
- **fig5c (and fig5d, supp14, which use its method):** the Figure 5B legend says the 2 z threshold is used for amplitude. I cited it and added a reading built on it.

**Still open:**
- The Figure 1D legend does not say which pairs of classes its three rank-sum tests compare.
- fig2e says the drop is significant "only below 10 Hz", but the band above 10 Hz is not defined. The test there is reported but does not decide the claim.
- Some discrepancies inside the paper cannot be settled from it; the criteria test each version:
  - which of prelimbic or infralimbic cortex responds more;
  - the low gamma test, P = 0.0226 in the Results against 0.0018 in the legend;
  - a t-test in the Results against a signed-rank test in the Supp. Fig. 9D legend;
  - the window of the phase-modulation result in Supp. Fig. 10B;
  - the behavioral pulse train, 1 Hz in the Methods against 0.5 Hz in the legends.
- The paper links no analysis code. Its toolbox site no longer exists, the Bitbucket copy asked for a login, and the scripts held inside the dataset were not read because readers may not open the data.
