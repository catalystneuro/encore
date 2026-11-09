**Verifier report, round 2: Dembrow, Sawchuk et al. 2024 on DANDI:001065 (0.241028.1559)**

The claims file has 42 claims, and the attempt record has 42 outcomes with the same IDs: 22 reproduced, 7 partially reproduced, 6 not reproduced, 7 blocked. Six outcomes are marked `assumed: true`: fig5e-morph-classifier, fig7-oscillation-frequency-vm, fig7k-oscillation-power-vm, figs7-oscillations-with-blockers, fig7l-firing-tracks-oscillation and figs7g-modal-rates-long-isis.

### 1. Outcomes

I agree with all 42 stated outcomes. Comments on the ones that changed or that need a remark:

- **species-no-effect → reproduced. Agree.** I tested `anova_estimable` on synthetic data:
  - On a full-rank four-way design it equals statsmodels' type II table exactly.
  - On a null design with an empty species × preparation × area cell, 4.3% of 300 runs give p < 0.05. Statsmodels' table gives 86%, so the round-1 counts were artefacts.
  - Power against a 0.5 SD species shift is 0.79 at n ≈ 300.
  - Cell 52: both readings give BH species p ≥ 0.62, and the additive model agrees. The criterion's rule (no feature at corrected p < 0.05 under either reading, with the readings agreeing) is met.
- **fig3e-classifier-accuracy → partially reproduced. Agree.** After the sweep check, the 50% score is 78.3, 77.5, 78.2 or 77.6 across readings and split rules, all below 79.11 (cell 24). The criterion has no partial rule; four of five values holding makes partial a fair call, though not_reproduced would also be defensible.
- **fig5c-basal-apical-features → reproduced. Agree** (my round-1 point).
- **fig4a-top-subthreshold, not reproduced. Agree.** Fr ranks 1st, MaxRn 4th and cutoff 11th. On the table's values cutoff ranks 10th, which also fails the partial rule (it needs the third feature in the top five).
- **figs7-cv-isi-higher-mcx, partially reproduced. Agree under the interaction model.** The additive variant gives p = 0.18 with bins of 25 (cell 105). The partial outcome therefore depends on the model that drops sweeps. That choice is not marked as assumed, though it is stated.
- **fig7-oscillation-frequency-vm, partially reproduced. Agree.** The criterion has no partial rule, and three of the four correlations hold. The MCx FFT result that passes is fragile: the spline maximum sits at the 3 Hz band edge in 52% of sweeps, and the interior-maximum variant gives r = −0.04 (cells 103 and 109). The notes say so.

The six assumptions are all stated, and all are reasonable:

- **Oscillation claims (fig7, fig7k, blockers, fig7l):** the smoothing spline chosen by GCV matches the criterion's "R smooth.spline defaults". Using Hann-windowed amplitude as strength, and resampling to 1 kHz, are the author's own choices, and they are disclosed.
- **figs7g:** the 1–200 spike limit is supported by the STAR Methods ("restricted to sweeps with no more than 200 spikes"), and the Results tie 650 ms to that analysis. The outcome rests entirely on this limit and on 1 Hz bins; with 2 Hz bins TCx is 9.0 Hz, above the 8.8 Hz bound.
- **fig5e:** the stratified-split assumption is reasonable. Unstratified splits would leave only 1 of 3 values within tolerance.
- **figs7-oscillations-with-blockers:** blocker status comes from the table, not from recording metadata as the criterion says. This deviation is stated.

### 2. Sentences the printed numbers do not support

- **Cell 22 and the fig3a-cs-with-l5et notes:** "the nearest labelled non-CS neighbour of 38 of 52 CS neurons is L5 ET" and "32 of 46 cultured". Cell 21 prints **42 of 52** and **36 of 46**. The author's round-1 response says the count was "corrected to the executed numbers", but this execution does not show 38. The UMAP count apparently changes between runs. The outcome is unaffected, since reading (a) needs 52 of 52.
- **Cell 53 and the species-no-effect notes:** statsmodels' table "gives … 1 under reading (b)". Cell 52 prints "BH species p < 0.05 for **2** features | smallest p 4.26e-05 (AP_amp)". The sentence also calls these "the round 1 result", but round 1 had 11 and 1 (my report), not 13 and 2.
- **Every outcome's `deviations` block in the record** says the link check finds "median Spearman 0.952". Cell 9 prints **0.957**, which is the value the link-cells notes use.
- **Cell 73 and the figs6b-mcx-higher-rheobase notes:** "so the shortfall comes from the cells in the dataset, not from the extraction." This is overstated. The uncorrected p is 0.08 here and 0.048 on the table's values (cell 72), so the extraction also moves the result, although both fail after BH correction. Cell 73 also points to the donor-means cell as "above"; it is cell 81, below.
- **figs7-oscillations-with-blockers notes, cell 116, and the metadata_insufficient finding:** "none mentions a blocker". Cell 115 prints "files mentioning a drug word anywhere: 1 | words found: ['wash']". 'wash' is not a blocker name, but that hit is neither shown nor explained.
- **Summary, oscillation bullet:** "the observations are cell by 5 mV bins". That holds for fig7 and fig7k only. fig7l, figs7g and the blockers claim use sweeps (cells 115, 118 and 121).
- **Entry README:** the table has no row covering tcx-et-types-no-difference or figs6b-avg-gain-no-difference. Both are reproduced in the record.

Everything else in the conclusions, the Summary, the README and the notes matches the printed outputs.

The attempt record's round-1 reasons are faithful to my report and use my own wording. Several reasons merge in the problem from section B that goes with the claim (species, fig4a, figs6b-lower-rin, fig6j, fig7, blockers, figs6c, fig6h, figs7-cv, fig5-tap-root), which is fair. Two small omissions: the fig7l reason leaves out that its r² shortfall rested on the missing spline (problem 4), and the blocked_by data_missing that I gave is recorded correctly.

### 3. Round-1 points

**Resolved:**

- **1 (species-no-effect):** crosstab, design rank and valid type II tests were added. My test above confirms them.
- **2 (fig4a):** the outliers are fixed, and the table-values and ranks variants show the failure does not come from extraction.
- **3 (implausible SSRn and sag values):** cell 7 now shows 0 cells with SSRn ≤ 0, MaxRn ≤ 0, negative sag ratio or Fr > 30 Hz. Three cells still have sag ratio < 1.
- **4 (no spline in the oscillation claims):** the spline is implemented, under two readings.
- **5 (fig6j width definition):** two width definitions were added as variants, and the per-step agreement with the pickle is shown.
- **7 (dropped bins):** the additive variant is added.
- **8 (blocker labels):** the drug counts and the file search are added.
- **12 (commands above 4 nA):** the five cells are listed and recorded as a finding.
- **Section C:** the RawFeatureWide columns are printed and have no per-layer length, so fig5b stays blocked correctly.
- **6, 9, 10 and 11:** these did not affect a conclusion and are stated in the record.

**Still bearing on a conclusion:**

- **fig3a:** the CS neighbour count is not stable from one execution to the next (42 printed, 38 written). The text and the output must agree, and the run-to-run variation should be reported.
- **fig7-oscillation-frequency-vm:** the MCx FFT component that passes probably reflects low-frequency power at the band edge (interior maximum r = −0.04). That makes the partial outcome weaker than it reads.
- **figs7-cv-isi-higher-mcx:** the partial outcome holds under the interaction model but not under the additive model with 25-spike bins (p = 0.18).
- **figs7g-modal-rates-long-isis:** the outcome depends on both the 200-spike limit and 1 Hz bins.
- **cohort-animals:** the M. mulatta count still rests on the unresolved species of subject Q19.01.001 (8 by the table, outside tolerance).
- **figs7-oscillations-with-blockers:** the single 'wash' hit in the files has not been looked at.
