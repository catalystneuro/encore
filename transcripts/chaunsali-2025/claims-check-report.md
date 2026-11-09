The claims file is fit for an attempt. My check entry at the end of the file sets `ready: true`.

**Checker:** `claims/001702/10.1002-alz.70813.yaml: 51 claims, 51 quotes, 20 statistical values, 0 problems` (it was 50 claims before I added one).

Most claims hold. The statements, sources, quotes, recorded p bounds, n and DEG tolerances all match the main text and the figure legends. Nothing comes from outside this paper.

**Changes, by claim:**
- **All criteria with readings of an open method detail** (19 places): these criteria let a single reading decide the outcome, "under a reading" or "under one reading". The open details are threshold, intensity measure, ANOVA form, Tukey family, unit, DESeq2 model and GO background. I changed these to "under every reading" and added a READINGS rule to the shared definitions. The protocol takes the outcome that all readings give and blocks the claim as `methods_underspecified` when they disagree.
- **fig1gh-aging-reduction-smaller-than-5xfad:** the aging comparison was limited to controls at 9 or 12 M, with no reason from the paper. I widened it to any older control group (6, 9 or 12 M). The criterion now states that "significantly more pronounced" is tested as the genotype by age interaction of the two-way ANOVA the legend names.
- **fig1a-pv-pnns-intense-in-5xfad:** the 2 µm ring and mask-overlap measures were the other agent's own, and the paper says these PNNs could not be separated. The claim is now blocked unless the dataset holds a per-PV-neuron measure; the two measures stay as variants only.
- **figs9-partial-knockout:** the rule for counting partially knocked out neurons was the other agent's. The claim now needs the paper's own classification of those neurons, otherwise it is blocked; the old rule stays as a variant.
- **fig1b-loss-of-wfa-peaks:** I reworded it to say the 10% and 25% peak thresholds are not from the paper and decide the outcome only when they agree.
- **New claim, fig4a-7m-social-memory-deficit:** Results 3.4 and the Figure 4A legend state a confirmed social memory deficit in the 7 M RNA-seq mice, and no claim covered it.

**Still open:**
- **fig1b-loss-of-wfa-peaks:** any peak definition comes from outside the paper, and the figure shows one example neuron per group, so this claim will likely be blocked.
- **fig3b-acan-ko-eliminates-ca2-pnns:** "vast majority" is read as a mean below half the WT mean; the paper gives no number.
- **figs6-ca2-devoid-of-plaques:** "largely devoid" is read as CA2 having less plaque than the rest of the hippocampus in every section; the paper gives no measure or test.
- **Supplement and correction:** the Supporting Information (Figures S1 to S9, Tables S2 to S4) and the correction (e71098) were not in the text. The supplementary claims, the exact p-values and the RNA-seq sample sizes depend on them.

Nothing was committed or pushed. The only file I changed is `claims/001702/10.1002-alz.70813.yaml`.
