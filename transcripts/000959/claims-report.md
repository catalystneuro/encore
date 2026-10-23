I wrote `claims/000959/10.1016-j.neuron.2024.05.004.yaml`. The quote checker reports 36 claims, 36 quotes, 132 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the PubMed Central author manuscript (PMC11309918): main text, figure legends and STAR Methods, plus its one supplement, which holds Table S1 and the legends of Figures S1 to S4. I did not read the version of record. The Results refer to "Supplementary Results" for the Mouth-stimulation control and the post-gaze window. The supplement has no such section, but those results appear in the manuscript's STAR Methods, so nothing a claim needed was missing.

**Code read.** I read the analysis code at github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994. It is MATLAB that starts from intermediate files made by a pipeline not in the repository, and it calls outside packages (bfw, shared_utils, dsp3). Where the code settles something the Methods leave open, I followed it and said so in the file:
- which trials are kept (the first trial of each run and trials in the last 5 s of a run are dropped);
- the post-gaze window is [0, 1.5) s by fixation start time;
- how ipsilateral and contralateral are defined for each monkey;
- how the two latencies are measured;
- the 10 ms bins and the regression used for the slope analysis;
- the FDR families.

Where the code and the Methods disagree, the Methods give the main result and the code's choice is shown as a variant. This applies to the heatmap (the Methods z-score it, the code divides by total count) and to the per-day fixation count (a day total in the Methods, a mean per session in the code).

**Counts.**
- 36 claims, all with quotes, none marked `inferred`.
- 34 claims carry statistics (132 values recorded); 6 carry expected values.
- All 36 have criteria, and all use the dataset as their data.
- Many claims are of absence (no effect for dmPFC, ACCg, the non-social condition, the partner monkey, and the pupil and saccade controls). Each is judged on the paper's own test.

**Details the paper leaves open, and the readings named for each:**
- **Heatmap "more clustered":** the summed stimulation-minus-sham difference inside the Face ROI or inside the Eyes ROI, each under both normalisations.
- **Per-day fixation count:** day total, or mean per session.
- **"diff" in the face-looking durations:** the median over days of the day differences, or their mean.
- **41% and 86% of trials:** averaged over all 81 days, or over the 27 OFC days.
- **Mouth bootstrap p-value:** one-sided or two-sided (no code for it).
- **Slope permutation p-value:** one-sided in the observed direction, as the code does for Fig. 5G, or two-sided.
- **Causal decomposition:** the paper doesn't give the gap-filling smoothing or the decomposition settings. Reading (a) uses settings guessed from the output folder name (noise 0.2, 1,000 ensembles, 150 bins); reading (b) uses the defaults of the original authors' code. Linear interpolation over gaps is a standard choice I named, not one the paper makes.
- **Fig. S4B comparisons:** the four single-factor pairs, or all six pairs.
- **"76 of 81 days with at least 90 stimulations":** counted among analysed trials, or among all delivered.
- **Partner reciprocation latency:** timed from the start of M1's look, or from the trial time.
- **Trigger-fixation duration and fixation counts:** M1-only events, or M1-only plus mutual.
- **"Positive slope on average":** mean or median, and combined hemifields or each hemifield.

**Gaps in the paper itself:**
- The Eyes ROI padding value is missing from the text ("adding a padding of to the center of each eye").
- The repository has no code for the Mouth-stimulation analysis, the partner-monkey latencies, the contralateral-versus-ipsilateral test, or the causal decomposition run.
- The Methods put the middle monitor at 36 cm, but the code converts pixels to degrees with 50 cm. This changes no rank test.
- The Fig. S4F legend shows a "* p < 0.05" key, while the Results give p = 0.455; I used the Results value.
