The claims file is fit for an attempt. I made 11 corrections and recorded 4 problems I could not settle, all in a new `checks` entry with `ready: true`.

**Checker:** `47 claims, 47 quotes, 24 statistical values, 2 problems`. Both problems are about how the paper prints numbers. The checker could not find 4.0e-4 (fig3c-slow-oscillation-nrem-deep) or 2.0e-6 (fig3c-3-6hz-layer4) because the text prints them as "4.0 × 10 −4" and "2.0 × 10 −6"; both values are there. All quotes match word for word, and the file loads as valid YAML.

**Changes, by claim**
- **fig2b-clusters-same-across-states:** The paper names "ANOVA", and its Methods give "Kruskal-Wallis one-way analysis of variance" as the default test. The named ANOVA stays the test for this claim of absence; Kruskal-Wallis is now shown as a variant.
- **fig2c-six-gamma-ics:** The brain state the ICA runs on is not in the Methods. It is now named as open, with whole session and waking as the readings.
- **fig2d-superficial-ic-power:** I removed the reading that divides by the variance of the six ICs. The Methods define relative power as "variance they explain in the original data". The six reported shares then sum to 0.66, which matches the 0.34 volume-conducted fraction.
- **fig3d-slow-oscillation-gamma-coupling:** Added the 5 to 200 Hz amplitude axis of Figure 3D, read from the article PDF's text. The number of phase bins is now flagged as not given in the Methods, and the criterion says where the superficial and deep values are read.
- **slow-gamma-superficial-wake:** Superficial sites changed from coherence clusters 1-3 to 1-2. Figures S3B and S3D label the six LFP layers L2, L3, L4, L5a, L5b, L6, so cluster 3 is layer 4.
- **figs2c-3-6hz-theta-anticorrelation:** The 1 s window reading came from no source. It is replaced by the wavelet power time series of the Methods.
- **fig4de-optotagging:** Whether the tagging histogram pools the three light intensities is now named as open, with both readings.
- **fig5b-eight-clusters:** What the K-means input holds per unit is now named as open: the full 6 ICs × 20 scales profile, or one value per IC.
- **fig7-within-layer-fractions:** I removed the four-layer reading. The paper says layers here "refer to IC-based clusters", and Figure S8B numbers those clusters 1 to 8.
- **figs8b-reciprocal-connections:** The 1.5 ratio for "almost twice" was not from the paper. It is now 1.8, which is 2 less the protocol's default 10%. I also added a reading with layer 5 pooled, since the text does not say whether "60-70%" spans the separate clusters or the whole layer.
- **figs7-strongest-3-6hz-coupling:** Added a second reading by mean modulation strength per frequency (Figures S7C and S7D).

**Still open**
- **figs8b-reciprocal-connections:** I could not match the per-cluster percentages in Figure S8B to their clusters, because no PDF renderer was available. The text extraction places 38.5% where cluster 6 might be, which would fail the per-cluster reading; the pooled reading would still apply.
- **fig8-down-active-neurons:** The paper gives no rule for picking DOWN state-active cells. Both readings in the criterion are the claims file's own.
- **fig8cd-down-active-suppressed and fig8eh-down-active-inverse-correlation:** The time windows come from neither the text nor the extracted figure text, and they could change the outcome.
- **figs2d-visual-offset-rebound:** The windows for the blocking and the rebound are not given.

Every main finding has a claim, and no claim draws on anything but this paper. Nothing was committed.
