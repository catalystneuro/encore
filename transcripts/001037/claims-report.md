I wrote the claims file at `claims/001037/10.1038-s41586-024-07915-x.yaml`. The quote checker reports 0 problems, and every quote also matches the text exactly, spaces included. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC11499281, corrected publication 2025): main text, Methods, and the legends of Figs 1 to 5 and Extended Data Figs 1 to 12. The supplement is only a Reporting Summary, which no result rests on. No PDF was supplied, so I read no figure panels; findings shown only in a panel come from its legend or the Results.

**Code read.**
- The paper links only `lindermanlab/ssm` (commit eb6c8aa), the general rSLDS fitting library, with no analysis of this paper.
- The dataset's description links the authors' sample code, `neuralcomputation/hypothalamic-dynamics` (commit 28fee70). I read its code and not its example data files, and ranked it below the Methods. It settles four things:
  - the time-constant formula, |1/log|λ|| divided by the frame rate, in seconds;
  - how activity is projected onto x1 and x2, using stored rSLDS weights, smoothing and baseline windows;
  - the stimulation onset frames for the 20 s and 8 s gaps between pulses;
  - the rSLDS fitting settings, which the notebooks call "representative", so I used them as one reading next to the Methods' cross-validated number of states.

**Counts.** 54 claims:
- 53 have quotes; one is `inferred` (Fig. 1f, the line attractor score, which no sentence states).
- 40 claims record statistics, 75 statistical values in all.
- All 54 have criteria. 18 have expected values.
- The 2 network-model claims (Fig. 4) are simulations that use no recorded data.

**Details the paper leaves open, and the readings named:**
- **Gap windows** for "baseline or ISIs": from the end of the 2 s pulse to the next onset, or from onset to onset.
- **Which Dunn comparisons** the printed p-values belong to: each gap against baseline, or each gap against the one before.
- **State-space distance** (Fig. 2g,h,n,o): the starting point is either the mean baseline state or the last baseline frame. Each pulse is compared either with baseline-frame distances or with the first pulse.
- **Which neurons count as x1 and x2**: the top five by absolute weight (as in Fig. 1i), or whatever the dataset marks.
- **Which state's time constant** is x1's: the largest over states, or the state occupied after the intruder is removed.
- **Ramp-up rate** (Fig. 5f): the slope from BALB/c entry to the x1 peak, or the rise over the first 10 s.
- **Shared undefined measures:**
  - the AUC window, and the window for the influence scores;
  - the autocorrelation half-width, read as the first lag at or below 0.5;
  - the transient frequency unit, per baseline or per minute;
  - the decay-constant fit.
- **Decoders:** the train/test split, and for the follower decoder the regression form, the set sizes and the validation.
- **How a model or cross-validation is set up:**
  - how the pulse input enters the rSLDS model (Extended Data Fig. 8c);
  - what the finite and infinite attractor models are (Extended Data Fig. 9);
  - how the cross-validation folds are formed (contiguous blocks or random frames).
- **Thresholds the paper never gives a number for:** "small fraction" of variance explained by movement, "close to zero" at 15 µm, and a cut-off for the line attractor score. For the first two I chose a cut-off (under 10% of variance; under a tenth of the on-soma response) and labelled it as a reading. Under the protocol a threshold that could change the outcome should not be an agent's choice, so a second reader should check these two.
- **Tests:** I ran Mann-Whitney unpaired even where the Methods say "paired". The reported p-values at n = 4 and n = 5 are the smallest the unpaired test can give, and a paired test cannot reach them.

**Inconsistencies in the paper**, recorded in the criteria:
- **Pulse parameters:** the Results say 20 Hz and the Methods say 10 Hz.
- **Model fit:** the observation cvR² is 67.2%, below the Methods' own 70% minimum. Its printed spreads (±0.03% and ±0.02%) only make sense as fractions.
- **Fig. 3i:** the text says "not statistically significant", but the legend lists P = 0.0316.
- **Extended Data Fig. 12b:** the legend gives r² = 0.87 for x2 neurons, which conflicts with the Results.
- **Mouse counts:** Extended Data Fig. 8j–l uses n = 8 and Extended Data Fig. 7b,c uses n = 10, against 7 and 9 elsewhere.

**Missing from the paper.** Nothing a claim needed for the reader step; the full text and Methods are there. Some claims need data the dataset may not hold: face-video motion SVDs (Extended Data Fig. 5), the spatial-resolution calibration cells (Extended Data Fig. 6), and cell positions. Whether they are in the dataset is for the author to find.
