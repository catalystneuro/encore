I've written `claims/000574/10.1126-sciadv.aav3687.yaml`, with 35 claims. The quote checker passes except for one flag, which I checked by reading and which needs no change (below). Nothing is committed.

**Text read.** I read the version of record from Europe PMC (PMC6436923), including the Methods and figure legends, and the supplement (figs. S1 to S6, tables S1 and S2). Table S1 came out garbled. I read it by column order and confirmed that reading by recomputing the medians the table prints (6.0 to 11.5 Hz and 7.8 to 10.0 Hz). The PDF page could not be opened as an image here because no PDF renderer is installed. I also read the data descriptor (Sci Data 2020) to describe the deposited data. Movie S1 was not read.

**Code.** The paper links no analysis code. The only code in the G-Node deposit (`USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM`, commit `0b27b34e`) is an example MATLAB script that loads the data. So code settles no method detail.

**Counts.**
- **Claims:** 35. 34 have quotes; one (the per-subject values of table S1) has an `inferred` note instead.
- **Statistics:** 26 entries over 22 claims.
- **Criteria:** all 35 claims have one.
- **Checker flag:** the checker reports `5e-05` as not found. The paper prints "P = 5.0 × 10 −5", which is the same value in a form the checker does not recognise.

**Details the paper leaves open, and the readings named:**
- **Permutation t test, paired or unpaired:** both.
- **Number of label-scrambled repetitions:** 499 (implied by P = 0.002) or 1000 (table S2).
- **Trials for the EEG, iEEG and PLV analyses:** correct trials only, or all artifact-free trials.
- **Behavior:**
  - Percentages are the mean over sessions or trials pooled.
  - Cowan's K is taken at set size 8, as the maximum over set sizes, from pooled rates times 8, or as the mean over set sizes.
  - The 48 ms per item comes from one of four slope definitions, using mean or median RT.
  - The ANOVA's F(2, 2007) fits no stated design, so it is run two ways and reported, not judged.
- **Neurons per session:** all 36 sessions, or only sessions with units (1526 / 36 is 42, not 51).
- **Firing-rate time base, and the noise SD in the SNR:** two readings each.
- **Chi-square:** with or without Yates correction.
- **Load-dependence test:** permutation t test, or a cluster-based test.
- **Probe window:** 0 to 1 s, probe to button press, or 0 to 0.5 s.
- **Window for the peak firing rate:** two readings.
- **Time range for the IN/OUT and workload tests on probe neurons:** two readings.
- **dPCA:**
  - The z-score scale and the regularization: two readings each.
  - The retrieval window: 0 to 1 s or 0 to 2 s.
  - Fig. S3d names both dPC2 and dPC3.
  - Loadings are absolute or signed.
- **Decoding:**
  - The smoothing kernel is a boxcar or a Gaussian.
  - Neuron firing rates are z-scored before the classifier, or not.
  - Class balance is equal trials per class, or all trials.
  - "Median accuracy" can be averaged over time steps two ways.
- **Frequency range searched for EEG, PLV and spike-field coherence:** 4 to 30 Hz or 1 to 40 Hz.
- **Trials for PLV maintenance against encoding:** set size 8 or all set sizes.
- **Position of a bipolar channel:** the deepest contact or the midpoint of the two contacts.
- **SOZ comparison:** which increase (workload, or maintenance against encoding) and which channels.
- **Spike-field coherence:** the window of the spike-triggered spectrum, run at 3 and 5 cycles.

**Missing from the paper:**
- **HFO claim:** the paper names no detector, test or comparison. It cites Fedele et al. 2017 (Sci Rep 7, 13836) for the detector, and that paper is not under `paper/`.
- **Channels for the other subjects' EEG power:** the fig. S5 legend cites a "table S7" that does not exist. I used each subject's maximal-PLV electrode instead.
- **Microwire field potentials:** the data descriptor does not list them among the deposited data. If the dataset lacks them, the spike-field coherence claim is blocked for the LFP part.
- **"Little difference" in decoding with maintenance neurons only:** the paper gives no threshold, so I used the protocol's default 10% tolerance.
