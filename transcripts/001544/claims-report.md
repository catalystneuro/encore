I wrote `claims/001544/10.1016-j.celrep.2024.114009.yaml`. The quote checker finds no problems: 30 claims, 30 quotes and 43 statistical values. Nothing is committed.

**Text read.** The NIH author manuscript from PMC (PMC11080946). It has the main text, the full STAR Methods and the legends of Figures 1 to 7. No PDF was supplied.
- **Missing:** the supplement (Figures S1 to S14 and their legends). I went ahead because the main findings rest on the main figures and the Methods. Eight claims cite a supplementary figure, and they rest only on the Results sentence that cites it. The supplement figure most relevant to this dataset is S12 (the other electrophysiological features).
- **Also missing:** group means and spreads. With no figure to read, none are known for any panel.

**Code read.**
- **Electrophysiology:** `nsdesai/patch_clamp_analysis` at tag v1.0.0 (commit 4ee1125), the version on Zenodo that the paper cites. I also read the current GitHub head (5d756c2, from April 2025, after the paper). The two differ in how spikes are detected and how input resistance is measured; I followed v1.0.0. The code extracts features from the current steps but holds no statistics.
- **Fiber photometry:** `rokim01/Fiber-Photometry-analysis` at commit 49dcfd4.

**The dataset.** The archive describes it as the paper's electrophysiology data, so 9 claims are on the patch-clamp and morphology data (the electrophysiology of Figure 6 and S12, and the reconstructions of Figure 6 and S13). The other 21 cover behaviour, cFos counts, fiber photometry, chemogenetics, reactivation labelling and the BLA projection, which the dataset probably does not hold.

**Counts.** All 30 claims have a quote and a criterion, so none needed an `inferred` note. 23 claims carry `statistics`, and 3 carry `expected` values: about 20% of cholinergic neurons cFos+, about 80% and 70% reactivated by a second odor of the same valence, and about 80% against under 20% of neurons reaching 100 µm.

**Details the paper leaves open, with the readings named:**
- **Membrane potential.** The Methods say it is measured with no current injected, but cells were held at −65 mV by a DC current. Readings: (a) the code's pre-step baseline; (b) a stretch with no injected current, if the data hold one.
- **AHP amplitude.** "Minimum potential 100 ms later" can mean (a) the minimum within 100 ms or (b) the voltage at 100 ms. The code's different definition is a variant.
- **Code against Methods.** Where they disagree I followed the Methods and recorded the code as a variant: spike threshold (Methods 20 mV/ms, code 10 mV/ms) and spike latency (Methods to threshold, code to peak).
- **Electrophysiology tests.** The reported degrees of freedom fit (a) a one-way ANOVA on cells with uncorrected unpaired t-tests. The Methods name (b) a nested ANOVA with mice. Both are to be run; if they disagree, the claim is blocked as `methods_underspecified`.
- **Measure of "less excitable".** Readings: (a) spike latency at rheobase; (b) rheobase.
- **Behaviour t-tests.** (a) Unpaired between groups or (b) paired within mice. The reported df(16) matches neither.
- **Unit for the cFos counts.** (a) Per-mouse means, as the Methods say, or (b) per-slice counts, which the reported df(64) fits.
- **Fiber photometry.** The length of the pre- and post-odor windows is open, and df(4, 34) matches no design for 7 mice.
- **Reactivated percentage (Fig S9).** Pooled over mice, or the mean of per-mouse percentages.
- **Thresholds I set for vague words.** "Virtually all" is taken as at least 90%, and "most" features as more than half. The file labels both as its own readings.

**Inconsistencies in the paper, noted in the file:**
- Several printed degrees of freedom do not match the sample sizes: Fig 4D F(3,17) with 18 mice, Fig 7D t(6) with 12 mice, and Fig 6K/L F(1,10) with 16 cells.
- The Sholl statistics are printed as negative F values.

**Needs the supplement.** One claim, other morphometric features not differing (Fig S13), cannot be specified without it, because the features are not named in the text.
