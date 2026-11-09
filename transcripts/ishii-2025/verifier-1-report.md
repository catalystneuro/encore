**A. Outcomes** (27 claims in the claims file. 20 were tested in the notebook. 7 are Figure 2 claims, which the notebook blocks.)

| Claim | Outcome | Reason |
|---|---|---|
| fig2-density-link | blocked (too_large) | I checked the DANDI API myself. It lists only 14 raw NWB volumes, 1.38 TB in total, with empty `processing` and `analysis` groups. There are no atlas labels, cell counts or classifier. Cell 3 measured 35.5 MB/s, so streaming the TRAP channel once takes 5.4 h. The ilastik classifier would also have to be retrained from manual labels. |
| fig2c-brain-wide-increase | blocked (too_large) | Same as above. |
| fig2ei-social-regions-higher | blocked (too_large) | Same. |
| fig2-mpn-higher | blocked (too_large) | Same. |
| fig2f-mpn-fourth-largest | blocked (too_large) | Same. |
| fig2gh-consummatory-tendency | blocked (too_large) | Same. |
| fig2s-dorsal-raphe | blocked (too_large) | Same. |
| fig1gh-transitions-isolation | reproduced | Cell 9 gives F(2,16)=10.888, p=0.00104 and F=14.344, p=0.00027. The Tukey p-values are 0.0142 and 0.0015 for transitions, and 0.0057 and 0.0004 for isolation time. All match the legend, and all are in the stated direction. |
| fig1i-latency-return | reproduced | Cell 11: F=11.870, p=0.000691. Ejaculation against sniff gives p=0.0016 and against mount p=0.0077, with ejaculation longest. |
| fig1jm-behaviors-after-ejaculation | reproduced | Cell 13: sniff p=0.652 (not significant). Mount and intromission p=0.0039, all 9 mice lower. Grooming p=0.0234 (exact) or 0.0251 (approximate), higher in 7 of 9. |
| fig1nt-natural-estrus | reproduced | Cell 15: the three RM ANOVAs give p=0.0101, 0.00082 and 2.0e-5. Sniff, mount and intromission give p=0.031 (all 6 mice lower). Grooming gives p=0.35 (approximate) or 0.44 (exact). |
| fig1s1-experience | reproduced | Cell 17: virgin females spend more time in the isolation zone, p=0.026 (code's column) or 0.041 (legend's measure). Entries differ at p=0.041; virgin females make fewer. |
| fig1s2-novel-male | reproduced | Cell 19: entries fall in 6 of 7 mice (p=0.027/0.031) and average time rises in 6 of 7 (p=0.028/0.031). |
| fig3d-mpn-fos | reproduced | Cell 25: MPN t=−4.2709, Bonferroni p=0.0136. MPA p=0.514. BST, LPO and VLPO give p=1. The MPN is the only significant region. |
| fig3i-vgat-vglut2-fos | reproduced | Cell 27: Vgat p=0.0153 and Vglut2 p=0.0190, as in the legend. The post-ejaculatory Fos+ share is 0.235 in Vgat against 0.160 in Vglut2. |
| fig3jm-cell-types | reproduced | Cell 29: Vgat+Calcr 0.0318, Gal 0.0174, Prlr 0.0212. In Vglut2 cells only Calcr is significant (0.0146). Clusters: Vglut2 0.0189, Vgat 0.0022, Gal 0.0265; Nts 0.377 (not significant). |
| fig4h-response-magnitude | reproduced | Cell 33: ejaculation t=3.998, p=4.2e-4. Sniff t=6.46 and anogenital sniffing t=6.64, both significant with Vgat higher. Mount and intromission give p=1. This tests the deposited magnitudes; see problem 4. |
| fig4i-ejaculation-responders | reproduced | Cell 35: 184/522 against 35/271 (p=1.5e-10) and 29 against 1 (p=0.0017). The counts are exact. |
| fig5-ejaculation-specific | reproduced | Cell 37: 178 ejaculation, 48 mount and 12 sniff cells. These are the legend's counts and lie within tolerance of the Results' 177 and 46. Specific share: Vgat 0.810, Vglut2 0.829. Readings (a) and (b) agree for all 793 cells. |
| fig5c-class-selectivity | reproduced | Cell 39: all five F values match the legend. In the Tukey tests every required pairwise contrast holds. Mount cells do not exceed sniff cells for sniff, and do not exceed ejaculation cells for ejaculation. |
| fig6c-decay-length | reproduced (fragile) | Cell 41, reading (c): t=3.037, p=0.00268, against the paper's t(217)=3.0397, p=0.00266. Reading (a) is not significant, and reading (b) is significant in the opposite direction. The result rests on giving 120 s to traces that never return below 0 (problem 3). |
| fig6k-late-cluster-vgat | reproduced | Cell 43: the late cluster holds 37 Vgat and 0 Vglut2 cells (Bonferroni p=0.018). The fast cluster holds 26/184 Vgat against 16/35 Vglut2 (p=6.8e-5). All of these match the legend. The fit's labels are identical to the deposited labels (adjusted Rand 1.0), and every seed gives the same result. |
| fig7fg-activation-suppresses | partially_reproduced | Cell 47: post-ejaculatory-hM3Dq is significant in both measures under both tests. Under the claims file's main reading (rank-sum), the consummatory-hM3Dq group also drops in transitions (Bonferroni p=0.0157), so "only post-ejaculatory" fails. Under the signed-rank variant it holds, with p=0.0625; see problem 1. |
| fig7kl-activation-intromission | reproduced | Cell 49: intromission p=0.0026 and receptive score p=0.0033 (rank-sum); both 0.03125 (signed-rank). Grooming and mount give 0.0625 under signed-rank, as the legend says. |
| fig7s1-mpn-proportion | reproduced | Cell 51: cell count F(2,24)=0.3072, p=0.7383. MPN proportion F=4.3335, p=0.0247, Tukey p=0.0471. Vgat exceeds Vglut2 in both groups. The proportions are 0.743/0.124 (pooled) and 0.786/0.138 (post-ejaculatory only), both within tolerance. |
| fig7s2-home-cage-activation | reproduced | Cell 53: sniff p=0.0072, intromission p=0.0165, mount p=0.41. Only post-ejaculatory-hM3Dq is significant. No place-preference comparison is significant (smallest p=0.062). |
| fig7s3-inhibition | reproduced | Cell 55: home cage intromission p=0.0045 and receptive score p=0.020; sniff p=0.70, mount p=0.40. In the self-paced assay the smallest corrected p is 0.117 (rank-sum) and 0.100 (signed-rank). |

**B. Problems**

1. **[affects a conclusion]** Claims file, fig7fg/fig7kl/fig7s3 (cells 47, 49, 55). The claims file makes the Wilcoxon rank-sum test the main reading. That looks like a misreading of the paper. Every p-value in the Figure 7 legend is reproduced exactly by the paired signed-rank test in the `p_signedrank_exact_bonf`/`p_signedrank_bonf` columns: 0.03125, 0.0625 and 0.125 for the consummatory group, 0.875 for the appetitive group, and 0.4594 and 0.11197 for sniff. The design is also paired (saline and CNO in the same mice). With the unpaired test, fig7fg drops to partial.
2. **[does not affect a conclusion]** Claims file, fig7s1 (cell 51). The claims file makes the unpaired t-test the main reading for the Vgat against Vglut2 comparison. The paper's t(10)=6.6154 and t(12)=13.9477 equal the paired t values (6.615 and 13.95). Its p-values equal twice the paired p (0.0024 and 1.69e-5). Both readings are significant.
3. **[does not affect a conclusion, but weakens it]** fig6c, `decay_length(unreturned="window")`, cell 41. 43 of the 184 Vgat cells never return below 0; 31 of them come from one mouse, Vgat_2. These cells get 120 s, which is more than a peak-to-return time can be (120 s minus the peak time). The convention does match the deposited table (r=1.000) and the paper's t, so as a reproduction of the authors' computation it is reasonable. But Vgat is no longer significantly longer if those cells take the time from peak to end of window (p=0.11), are left out (p=0.30), or animals are the unit (p=0.149).
4. **[does not affect a conclusion]** fig4h, fig4i and fig5 (cells 31, 33). For the five non-ejaculation behaviors, the magnitudes come from the deposited table, not from the traces. The array means correlate with the table at r=0.70 to 0.89 only. The tests therefore check the authors' table, not the Methods' computation. The array variant gives the same outcomes (mount p=0.106).
5. **[does not affect a conclusion]** fig6k, cell 43. "Fast" is defined as the largest 0 to 5 s mean, which is the notebook's own choice; cluster 4 actually peaks earlier (1.9 s against 5.8 s). The best fit is 30 neighbours with silhouette 0.474, not the paper's 55 and 0.405. At 55 neighbours the late cluster holds 33 Vgat cells, outside the 37±3.7 tolerance.
6. **[does not affect a conclusion]** `mpoa.elbow_pcs` returns a 0-based index. On synthetic data with the elbow at the 3rd component it returns 2. The value is not used, because 4 components are hard-coded from the Methods.
7. **[does not affect a conclusion]** Figures 4 to 6 (cells 33 to 43) treat cells as independent units, as the paper does. Per-animal results are shown only for fig6c.
8. **[does not affect a conclusion]** Figure 2 (cells 3, 56). The Figshare file "Figure 2 and S3, S4.zip" is listed in `FIGSHARE_FILES` but never opened. The 4/5/5 group structure, which is part of fig2-density-link, is shown but never matched to the table's Stim labels. The undeposited classifier would also justify methods_underspecified as a second reason. For any later attempt:
   - The volumes are stored contiguous and uncompressed (chunks None), so a subvolume around the medial preoptic area could be read by range requests.
   - The Mount brains were imaged in 2024, and their mid-plane TRAP intensities are 20 to 35 against 47 to 143 for the other brains. That is a possible batch effect.

**C. What I could not check**

- **The "60 minute notebook limit"** that underlies too_large. It is not in my materials.
- **The contents of the Figure 2 Figshare zip.** A cell listing its members and the Stim labels of `tdTomato_summary.csv` would have shown how much of fig2-density-link could be checked.
- **The place-preference measure of fig7s2.** I could not check whether "post-test minus pre-test in the CNO-paired zone" matches Figure S10.ipynb. Printing the legend's place-preference p-values next to the notebook's would settle it.
- **Where fig6c's 12 differences come from.** Reading (c) and the table differ for 12 of the 219 responders. A table of those 12 cells, giving the peak time, return time and table value, would show which convention the authors used.
- **The cost of the alternatives for Figure 2.** I could not judge whether region-restricted reading would make the analysis feasible. A timing of one registration on a heavily downsampled brain, and of reading one medial preoptic subvolume, would have shown it.
