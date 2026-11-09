I wrote `claims/crcns-ac-4/10.1038-ncomms13654.yaml`. It has 25 claims and all 25 have quotes. The quote checker passes every quote. It flags one problem: it can't find the behavioural t-test's P = 1e-5, because the extracted text prints it as "P 1⁄4 1e �5". I confirmed that value by reading and noted it in the file header. Nothing is committed.

**Text read:** the version of record, with Methods, figure legends and the Supplementary Information (Supplementary Figures 1 to 7 and Supplementary Methods). I read Figure 4 from the PDF page, because the text loses which P-value belongs to which window. The Supplementary Audio and Movies were not supplied, and no claim needs them. Nothing a claim needed was missing.

**Code read:** github.com/choldgraf/ecogtools at commit 7d1030e (2016-11-03), the last commit before publication. The STRF, audio and connectivity modules were removed on 2016-12-23. It is a helper library with no script that runs the paper's analyses: ridge encoding model, partial correlation, coherence-to-bits, Hilbert amplitude, NSL-style spectrogram, PAC and bootstrap regression.

**Contents:**
- **Statistics:** 27 values over 17 claims, two of them with confidence intervals.
- **Expected values:** 10 claims. The tolerance is the paper's stated spread where it gives one. For the 0.18 ± 0.001 partial-correlation result I used 10% instead, and said why: as an s.e. over 41 electrodes, 0.001 is implausibly small.
- **Criteria:** every claim has one, and 8 of them are claims of absence.

**Details the paper leaves open, with the readings named:**
1. Trials that define speech-responsive electrodes: (a) the unfiltered (MIDDLE) trials, which the Methods use; (b) all three conditions pooled, as the Results say.
2. Post-stimulus window for mean evoked HFB: (a) the length of each sound; (b) 0 to 2.5 s.
3. How the baseline z-score is formed: (a) per trial; (b) all baseline samples pooled; (c) the whole series by its non-event times, as the code does.
4. HFB band edges: 70 to 140 Hz in the Methods, 70 to 150 Hz in the Results. I used a standard choice, and the Methods' IIR filter over the code's FIR.
5. Number of bootstrap samples: 10,000, a standard choice.
6. Which electrodes are temporal or perisylvian: the paper gives no list, so the author labels them from the electrode images.
7. Samples used to fit each eSTRF: (a) sound onset to offset; (b) onset to 400 ms after offset. The ridge grid is a standard choice.
8. Lower bound for the well-modelled (STRF-R) test: (a) a bootstrap 99% interval on the mean R²; (b) the 1st percentile of per-split R²; (c) the 0.5th percentile of per-split R².
9. Meaning of ± on the eSTRF effects: (a) s.e.; (b) s.d.
10. Coherence: the taper settings and frequency range are standard choices. For the unexplained n = 78 electrodes: (a) speech-responsive perisylvian electrodes; (b) all perisylvian electrodes.
11. Cluster-forming threshold and number of permutations: MNE defaults.

Some readings apply to single claims only:
- **Behavioural samples:** df = 16 doesn't fit one group of 9.
- **Supplementary Figure 1A:** what the "t=9.74, df=28" test compares.
- **RMS analysis:** what gets standardized.
- **Prediction R²:** computed per trial or over all trials.
- **Partial correlation:** with or without an intercept.
- **Mean subtraction (Figure 4b):** one global mean or one per condition.
- **Pink-noise controls:** which electrodes.
- **PAC:** theta band 3 to 8 Hz, 2 to 12 Hz or 4 to 8 Hz.
- **Mixed model:** the random effects.

**Paper inconsistencies recorded:**
- **Figure 4:** the Results cite P = 0.006 for raw coherence, but Figure 4 prints 0.006 for the mean-subtracted late window (panel b). Panel a gives 0.000 and 0.001.
- **Figure 10b:** the Results correlate the similarity increase with evoked HFB amplitude; the legend and axis correlate it with model R². Both readings are listed.
- **Counts:** the paper uses electrode counts it doesn't explain (78, 72, 39 and 12), which the criteria read as subsets.

**Data:** the data set's description doesn't mention the behavioural control data. Five claims need it; they are marked "dataset", and whether the data set holds it is for the author to find. Its summary also says 40 to 50 sentences per subject, where the paper says 50 to 60 trials.
