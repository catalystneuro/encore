I checked the claims file for DANDI:001960 against the paper, the supplement legends and the paper's code (commit 181ad475). It is ready for an attempt: `ready: true`.

**Checker result** (before and after my edits): `56 claims, 56 quotes, 31 statistical values, 0 problems`.

**Changes, by claim** (each is recorded with its reason under `checks`):
- **Header:** the Figure 6 code loader takes the QC cells (258 for M-YQ0201-29), not the stored correlation index. I fixed the citation.
- **gap-junction-connection-counts:** the code gives 3,553 and 2,199 for pairs 60 to 400 um apart. That settles the band the file called open, so 60 to 400 um is now the main reading.
- **fig5g-gap-junction-synchrony:** the file read n = 5,752 as including pairs under 60 um. It is 3,553 + 2,199, the in-band counts, and the Results exclude pairs under 60 um, so the selection is now 60 to 400 um.
- **synaptic-connection-counts:** added the 60 to 400 um band as a reading. The code gives 800 connections in that band (814 without it) and 667.
- **npy-ipsp-amplitude:** stated the 60 to 400 um band (1,467 = 800 + 667).
- **ipsp-median-amplitude:** the paper gives no method for the "~20%" correlated fluctuations, and no code computes it. The measure used is now labelled a reading chosen by the reader.
- **fig2gk-bin-profiles:** the paper does not say which firing rate it means. Added two readings: the maximum rate and the cluster-average rate.
- **fig3jk-presynaptic-sets-amplitude** (and fig3mn, which refers to it): the file misdescribed the code's time-constant filter. Corrected it.
- **fig4hi-self-sta-diverges:** fixed the citation; only code panel H uses the 60 to 200 um band.
- **fig5b-adaptation-dvdt:** added the code's effective voltage window (0.25 to 0.75 spike heights) to the code variant.
- **fig5e-inhibition-in-spontaneous-voltage:** the expected values included the control pairs' +1% change, but the statement and quote did not. Added it to both.
- **npy-umap-groups:** added two code steps the criterion left out: an svds projection before UMAP, and box binning.
- **npy-oscillation-peak-rates:** the code fixes the filter, which the file called a standard choice. The ±50 and ±100 ms windows came from neither the paper nor the code. They are replaced by the code's Figure 6I window (±381 ms) and the value at the peak.
- **npy-state-dependent-excitability:** the window is 635 ms, not 636.
- **fig3lo-variance-components:** stated that the code chooses the distance term by AIC from ML fits.

**What remains open** (logged under `checks`, not settled):
- **npy-gap-junction-no-difference:** this is a claim of absence, but Supplementary Figure 25D and E mark several pairwise subtype differences as significant on the paper's own test. The "consistent direction" rule in the criterion is the claims writer's reading of "did not differ systematically"; the paper does not state it.
- **Qualitative claims with no number in the paper:** these are judged on thresholds or tests the claims writer chose, each labelled as such. They are amplitudes-log-normal, gap-junction-no-identity-effect, voltage-to-spike-sigmoid, fig4g, fig4hi, fig5a, npy-fraction-and-similarity, npy-umap-groups (Fisher test), inhibition-gap-balance, and the degree-distribution part of connection-distance-structure. interaction-kernel has no method in the paper at all.
- **Significance marks:** the supplement PDF could not be rendered here. I checked the marks of Supplementary Figures 10H, 24E and 26 against the order of the extracted text, and they agree with the claims. I could not tell which comparison each mark in 25D and E belongs to.

Every main finding of the paper has a claim, and no claim comes from outside this paper. Nothing was committed or pushed.
