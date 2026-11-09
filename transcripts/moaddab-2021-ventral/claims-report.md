I wrote the claims file at `claims/crcns-bf-3/10.1038-s42003-020-01554-4.yaml`. The quote checker passes every quote. It flags three p-values as not found (1.20 × 10⁻⁷, 1.50 × 10⁻⁷, 8.20 × 10⁻⁴); the paper prints them with trailing zeros, and I confirmed each by reading.

**Text read.** The version of record (PMC7794503, Europe PMC full-text XML): Results, figure legends and Methods. There was no PDF.
- **Supplement:** the Supplementary Information (Supplementary Figs. 1 to 10) was not supplied. The main findings rest on Figs. 1 to 6 and the Methods, so I went ahead. Four claims come from Results sentences that only point to a supplementary figure (Supplementary Figs. 5, 6, 8, 9); their sources say "(not read)". The High firing neuron analyses (Supplementary Figs. 4 to 7) have no claim.
- **Code:** the only code link the paper gives, http://mcdannaldlab.org/resources, returns 404, and the lab site has no resources page. No code was read.

**Counts.**
- 45 claims, all with quotes and all with criteria.
- 22 claims have expected values. Where the paper gives a bootstrap interval, the tolerance is the larger distance from the mean to a bound of that interval; otherwise it is 10%.
- 36 claims carry statistics, 102 entries in all (ANOVA and ANCOVA F tests, bootstrap 95% intervals, Pearson R², Fisher r-to-z).
- 10 claims are claims of absence, judged on the paper's own test.

**Details the paper leaves open, with the readings named for each:**
- **O1, Z-score pool:** the three cue types (uncertainty pooled) or the four trial types.
- **O2, per-trial firing for the regression:** the Methods define normalization on trial averages but regress single trials. Readings:
  - (a) each trial minus its own baseline, scaled by the neuron's normalization;
  - (b) the trial-type mean baseline;
  - (c) Z-scored across all trials and bins.
- **O3, suppression ratios:**
  - trials with no pokes at all (0/0): dropped, or set to 0;
  - per-rat means: each session counted once, or once per cue-responsive neuron in it.
- **O4, reward events and normalization:**
  - events: deliveries outside the cue and 2 s delay, or outside the whole trial window;
  - Z-scoring: over the 16 reward bins, or with the cue normalization's SD.
- **O5, "peak" and "trough" values in the correlations (Fig. 5d to i, Fig. 6g):** the bin after delivery minus the bin before, or the maximum of the two bins minus the bin before.
- **O6, sample sizes:** several reported degrees of freedom imply fewer neurons than the stated groups (72 of 74 Low firing, 130 of 131 cue-excited). The author uses all neurons and reports the n used.
- **O7, k-means:** raw features with Matlab defaults, or Z-scored features. Seed and replicates are a standard choice.
- **Cue-excited/inhibited split:** baseline-subtracted Hz or Z-scored firing, and the two window means averaged or the 6 s pooled.
- **Two regressors for 0.25 and 0.50:** one joint model, a joint model with fear output, or the separate single-assignment models.
- **Fisher r-to-z formula:** the reported Z values fit the independent-samples form with n = 74 (they give about 0.79 and 2.98), so that is the main reading. A test for dependent correlations is shown as a variant.
- **Nose-poke pause definition:** it is in the unread Supplementary Fig. 6. Readings are a gap of at least 10 s or at least 5 s.

**Missing material a claim needed.**
- The supplement: it holds the pause definition and the panels behind the cue-cue correlation claims, which I could only judge as stated in the Results.
- The linked behavior-analysis code, now offline.
