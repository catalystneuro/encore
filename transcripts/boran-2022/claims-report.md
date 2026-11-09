I wrote `claims/000575/10.1016-j.neuroimage.2022.119123.yaml`. The quote checker passes: 17 claims, 16 quotes, 18 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record, extracted from the publisher PDF, including the Methods, Results, figure legends and Table 1. The paper has no supplement and cites none. I opened the PDF only for Figures 2c, 2d, 3b and 4d, to read per-region counts and the amygdala decoding level that the text doesn't give.

**Code:** the only link the paper gives is the G-Node GIN repository USZ_NCH/Human_MTL_units_visual_WM. GIN timed out, so I read its listing from an Internet Archive snapshot of 2026-10-15 (head commit 5ccc2377802e…). It holds the 16 session data files, a README and a LICENSE. The README mentions a MATLAB data-loading example folder, but that folder isn't on master. There is no analysis code, so code settles no method detail.

**Counts:**
- 17 claims; 16 have quotes, and 1 is `inferred` (the Table 1 values per participant).
- 11 claims carry `statistics`, 18 values in all.
- All 17 have a criterion and `expected` values.
- All use the dataset's own data; no outside data is needed.

**Details the paper leaves open, with the readings named:**
- **Permutation t-test (statcond):** (a) paired or (b) unpaired. The number of permutations isn't given; 1000 is used as a standard choice, with 5000 as a check.
- **Repetitions behind "permutation test against scrambled labels":** inferred from the printed minimum p, about 499 for p = .002 and 4999 for p = .0002. What gets scrambled is also unstated; the reading is that the labels the selection compares are shuffled.
- **Behaviour:**
  - Accuracy: trials pooled over sessions, or the mean of session percentages.
  - Median capacity: over 13 participants or 16 sessions.
  - Cowan's K: maximum over set sizes, or the value at set size 6.
  - Response time per session: mean or median.
  - 118 ms/item slope: fit per session, fit over pooled trials, or fit to the four set-size means.
- **Firing rates:** correct or all trials, and two possible extents for "the whole trial". The noise used for the waveform signal-to-noise ratio is either the spread of single-spike waveforms or a noise level stored by the spike sorter.
- **Workload-modulated neurons:** the per-neuron test is either the permutation t-test or the cluster-based test used for the Figure 2a example.
- **Correct vs incorrect maintenance neurons:** all trials as they are, or correct trials subsampled to the number of incorrect trials.
- **Test neurons:** the Methods compare test with maintenance; the Results compare test with encoding and maintenance (separately or joined). The Methods reading is the main one.
- **dPCA:**
  - Gaussian kernel SD: 200 ms or 167 ms.
  - Regularization: none, or cross-validated.
  - The 20% subsampling: of neurons or of trials.
  - Speed and distance: defined as Euclidean measures in the 15-dPC space.
- **Decoding:**
  - Which window counts as "maintenance": the window centred on the period, or the median over windows inside it.
  - Trials per label: equal across sessions, or each session's own count.
  - Features: z-scored or raw.
  - Kernel: linear, the toolbox default.
  - Balancing correct against incorrect trials for performance decoding: the smallest incorrect-trial count of any session.

**Missing from the paper:**
- **No analysis code is published**, which is why so many details above stay open.
- **Two cited methods papers weren't read.** The Methods defer to Boran et al. 2019 ("identical" non-task-specific analyses) and to Kaminski et al. 2017 (dPCA). Neither is under `paper/`, so anything they would fix is named as open.
- **Amygdala decoding accuracy:** read only from the figure (about 62%), with no p-value printed.
