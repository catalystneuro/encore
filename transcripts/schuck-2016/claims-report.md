I wrote `claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml`: 29 claims, every one with a quote, 22 with statistics (47 statistical values in all) and 28 with criteria. The quote checker passes except on two values. The confidence-interval bounds −0.8432 and −0.0169 are printed in the text with a garbled minus sign (line 340), and I confirmed them by reading.

**Text read:** the version of record with its full Supplemental Information (Figures S1 to S5, Table S1, Supplemental Results 1.1 to 1.5), from the PyMuPDF text. Nothing the claims need is missing. The paper links no analysis code (it names only SPM8, PhysIO, LIBSVM, the Princeton MVPA toolbox, R, neuRosim and AFNI), so I read none.

**The dataset, from its description:** 24 of the paper's 27 participants, the subset used in the trial-wise analysis. It holds OFC time series in native space, design matrices built with AFNI, drift and motion nuisance terms, and per-state event files. It has no whole-brain data, no other brain regions, no cardiac regressors and no training sessions. Claims that need those are kept, and their criteria say so: the whole-brain conjunction map, the other regions, and training against scanner performance.

**Details the paper leaves open, with the readings named:**
- **Beta-map smoothing kernel:** 3 mm FWHM (the kernel given for the trial-wise test data) or no smoothing. Smoothing needs voxel positions.
- **Z-scoring:** each voxel across the state maps of a run, or each map across voxels.
- **Trials after errors:** left out of the GLM as their own nuisance regressor, or merged with the error regressor.
- **Side of t-tests not stated:** one-sided or two-sided. For t24 = 2.3 with p = 0.01, I read it as one-sided.
- **Behavioral mixed models:** linear on per-participant cell rates, or logistic on single trials.
- **Error-rate denominator.**
- **Permutation test:** which distribution gives the 95th percentile, and which test gives p < 0.025.
- **Searchlight radius:** not given anywhere. I named 2 and 3 voxels as standard choices, not the paper's.
- **"2 TRs after onset":** the first volume at or after onset plus 4.8 s, or the volume nearest that time.
- **How the matched non-error time courses are chosen.**
- **Whether the diagonal is in the within-class similarity mean.**
- **Figure 5:** the eight transition types, or Figure 5B's ordinal positions. The text gives p = 0.02 and the legend p = 0.04, which may be these two readings.
- **Number of bootstrap iterations:** 10,000 in the Methods, 1,000 in the supplement.
- **How the true state of an error trial is reconstructed.**

**Inconsistencies in the paper, recorded in the claims:**
- The 8-way decoding is reported as 4.2% above chance with t26 = 3.3 in the main text, and as 8.5% above chance with t26 = 6.6 in the supplement. The arithmetic supports 4.2.
- Previous age in the 8-way analysis is "above baseline" in the main text but only marginal (p = .09) in the supplement.

**Missing details a claim needed:**
- The synthetic-data controls need each participant's decoding peak and the searchlight radius; the paper gives no radius.
- The motor-action claim needs the response side of each trial; whether the dataset has it is left to the author.
