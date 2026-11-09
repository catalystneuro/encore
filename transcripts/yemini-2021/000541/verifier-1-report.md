**A. Outcomes**

The claims file has 29 claims: 27 from the paper and 2 links. The notebook tests 18 and blocks 11.

| Claim | Outcome | Reason |
|---|---|---|
| link-zenodo-traces | partially_reproduced | All 21 files match and all 21 stimulus orders agree, but only 81.7% of shared traces reach r ≥ 0.9, short of the 90% the criterion asks (cell 14). |
| link-connectome-names | reproduced | 190 of 193 names match Cook et al. The 3 that don't (AMSOL, AMSOR, HMC) are not neurons (cell 48). |
| fig6-sample-sizes | partially_reproduced | Heads = 21 and distinct names = 193 (190 neurons) are within tolerance. The median animals per name is 17 or 18 (within 16.2 to 19.8) only under near-duplicate readings "both" and "one"; under "none" it is 21 (cell 16). The tail counts can't be tested because there are no tails. |
| fig6-all-heads-responsive | not_reproduced | At most 19 of 21 heads pass (reading a, "none"); reading (b) passes 16 (cell 18). Cell 14 shows these are the paper's 21 kept heads, so the criterion requires all 21. |
| fig6d-ase-nacl | reproduced | ASER is excited: p = 0.0055 to 0.020, and q(b) ≤ 0.05 in every mode. q(a) is 0.0505 under "both" only. The ASEL against ASER asymmetry has p ≤ 1e-4 under both measures (cell 22). |
| fig6-nacl-unknown-interneurons | partially_reproduced | 4 of 6 classes (AIN, AVH, I2, MI) are significant under every FDR and duplicate reading. AVJ (p = 0.094) and AVF (mean response negative) fail (cell 24). |
| fig6c-odors-more-inhibitory | reproduced | Under reading (b), the fraction of classes with a negative mean is higher for both odors than NaCl in all modes (0.25 vs 0.27 and 0.44 under "both"). Reading (a) also holds except one tie ("none", q_stim). The butanone margin is thin (cell 26). |
| fig6d-awc-asymmetric | blocked (metadata_insufficient) | The files label only AWCL and AWCR, so the criterion blocks it. In the Zenodo-label variant, butanone gives p = 0.35 to 0.56 and pentanedione p = 0.038 to 0.096, so even that would be partial at best (cell 28). |
| fig6-asj-ric | partially_reproduced (fragile) | Under "both", 4 of 6 parts hold with q and 5 of 6 with p. Under "one" and "none" only 3 of 6 hold, which is not reproduced. ASJ inhibition by pentanedione fails everywhere (p = 0.21) (cell 30). |
| fig6-interneurons-downstream | reproduced | All 5 classes respond to at least one stimulus under every reading (cell 32). |
| fig6-tail-responses | blocked (data_missing) | Confirmed on the archive: the published versions and the draft all hold the same 21 head files, and no tail neurons are named (cell 34). |
| fig6f-pharyngeal | reproduced | At least 3 pharyngeal classes respond to NaCl and 4 to butanone under every reading (cell 36). |
| fig6-stimulus-sets-distinct | reproduced | Every pair of stimuli shares 9 to 14 classes and no two sets are identical, under all readings (cell 38). With sets of about 20 classes this is a weak test. |
| figs1h-avf-cyclic | not_reproduced | The median peak rate is 0.12 Hz at 1 SD and 0.19 to 0.20 Hz at 0.5 SD. The spectral-peak subset (n = 3) gives 0.17 to 0.18 Hz. All are outside 0.27 to 0.33 Hz (cell 40). |
| fig6gi-stimulus-specific-correlations | partially_reproduced | Under reading (a), NaCl against each odor gives p ≤ 0.008 in every mode, but butanone against pentanedione gives p = 0.18 to 0.34 (cell 42). Reading (b) passes all three pairs only under "both" (98/98/98), and the non-stimulus control window passes too (59/100/100, cell 44). That pass reflects the timing of the window, not the stimulus, so I don't count it as a full reproduction. |
| figs2a-pca-trajectories | not_reproduced | No reading separates all three pairs; at most one pair is distinguishable (cell 46). |
| fig6jk-connectome-correlation | partially_reproduced | Head only. No count-based reading puts electrical R2 in 2.52 to 3.08 (values 1.34, 3.53, 0.31, 0.83) or chemical R2 in 0.45 to 0.55 (all ≤ 0.29). All head values are below 5%. Tails can't be tested (cell 50). |
| fig6-connectome-variations | reproduced (heads only) | On the first-listed reading the largest R2 is 1.66%, under the 3.1% bound (cell 52). Off that reading, 3.64% is reached (electrical, pairs b, log), but against a baseline of 3.53%. |
| fig1-neuropal-color-map, fig1-neuropal-stable-variable-classes, figs1-integrant-health, fig2-positional-variability, fig4c-receptor-coverage, fig5ab-pag3-fate, fig5ef-eor1-rme, fig7bc-id-accuracy | blocked (data_missing) | The archive's 21 assets are all head GCaMP/NeuroPAL sessions of OH16230. None of the underlying imaging is there. |
| fig4bd-gaba-network, fig4e-extrasynaptic, fig7de-optimal-coloring | blocked (data_missing, the outside inputs are not available here) | These are `data: with_inputs` claims. They need the receptor expression tables, the connectome, or WormBase reporters plus the solver, not the dandiset. Saying "not in the dandiset" is not the reason they are blocked. |

**B. Problems**

1. [affects a conclusion] `near_duplicates` and the "both" main reading (cells 7, 8) remove far too many traces. "both" removes 669 traces and "one" removes 347. The paper's own deposit lacks only 101 of the dandiset's named neuron traces (cell 14), so the paper's removal was roughly 3 to 7 times smaller than either reading. The "both" reading is the only one under which these pass:
   - fig6-asj-ric reaches partial;
   - fig6gi reading (b) passes;
   - the head median falls in the 18 ± 1.8 band ("one" gives 18 too, "none" gives 21).
   
   A reading that removes exactly the traces missing from the deposit was available and was not run.
2. [affects a conclusion] The markdown in cell 12 misreports cell 11. AWC does not fall more at the odor times: for pentanedione it is −0.505 at the true window against −0.544 elsewhere (p = 0.96), and for butanone p = 0.45. This weakens the stimulus-clock check for the odors, and with it the AWC-based conclusions (fig6-all-heads-responsive).
3. [affects a conclusion] Cell 46 (PCA) runs on dF/F0 without normalization, with values from −41 to 89 because F0 is near zero for some traces. Under "one", PC1 explains 75% of the variance, which suggests a few outlier traces dominate. The dNMF class normalization the paper uses across animals is skipped (the module docstring says so). The not_reproduced outcome is therefore not robust; the z-scored variant also fails.
4. [does not affect a conclusion] `storey_pi0` follows the mafdr bootstrap faithfully, but on synthetic data it underestimates pi0: true 0.5 gives about 0.42, and a 95-test family with true pi0 0.42 gives 0.19. With pi0 = 0.30 for NaCl, q is often below p (cell 38, "none": 42 NaCl classes by q_stim against 28 by p), so reading (b) is more lenient than uncorrected p. No outcome depends on reading (b) alone.
5. [does not affect a conclusion] `class_tests` keeps the non-neurons AMSO (4 animals) and HMC (6) in the test family. This changes the counts in cells 26 and 38 slightly.
6. [does not affect a conclusion] `dff` drops a last frame, but the dandiset traces already have movie frames − 1. Deposit lengths differ by −1 to +1, so the alignment varies by file.
7. [does not affect a conclusion] Cell 28 searches for ON/OFF names only in `recs[:1]`, and searches only the label strings.
8. [does not affect a conclusion] fig6-sample-sizes: the paper's sentence gives the median of 18 for heads and tails together, and both the claims file and the notebook read it as head-only.

**C. Not checked**

- Whether the axis order of the `voxel_mask` x/y/z columns matches `grid_spacing`, which determines the 5 µm distances. A printout of nearest-neighbour distances per file, and of the pairs flagged per file, would have let me check.
- Whether the traces removed under each duplicate reading overlap the 101 traces missing from the deposit. A cross-tab would settle problem 1.
- The deposit's own median animals per name and per class, for fig6-sample-sizes.
- Whether the NWB files hold the AWC ON/OFF side anywhere other than the labels. The archive's asset metadata has nothing on it. The NeuroPALImageRaw volume could in principle show it, since srsx-3 colors AWC OFF, so that part may be testable. A listing of the NeuroPAL and subject metadata fields, and the AWCL/AWCR color values, would show it.
- The ASJ and RIC test rows under "one" and "none". Cell 30 shows only "both".
- The attempt record's reasons for the 11 blocked claims, which I was not given.
