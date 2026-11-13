No outcome changed. The entry re-ran cleanly with `python tools/entry.py all entries/peron-2015` (0 check errors, notebook runs in 26 s), and I rebuilt the handover package. Nothing is committed.

**Outcomes:** 1 reproduced, 1 not reproduced, 41 blocked, as before. The verifier agreed on 42 of the 43 claims.

- **results-whisking-amplitude:** I kept not reproduced and recorded the verifier's disagreement (it would give partially reproduced). I ran what it asked for:
  - **Tracking errors:** dropping only the error samples barely moves reading (a): 72.4 without samples above 85°, 71.9 without short spikes, 71.7 to 74.1 with other thresholds. Unwrapping whisks that pass 90° raises it to 77.0. Only cutting every sample above 70°, which also cuts real whisks, brings it inside the tolerance (67.4). Most of the range is real whisking: an229717's median is 87.2.
  - **Edge effects:** on a pure sine of amplitude 20 the peak reads 22.0, and 20.1 once 0.2 s is left out at each end. On the data, trimming the ends moves reading (c) only from 26.9 to 26.6.
  - **Why the outcome stays:** every reading the criterion lists stays outside 42.2 to 68.8, and the criterion decides the outcome. The notes record that some unlisted measures fall inside, and that the untested part of the statement (larger than about 20°) holds. Two of those measures:
    - the mean of the per-mouse medians of reading (a), 68.6, just inside the upper bound;
    - twice the Hilbert peak, 53.2 after the fixes.
- **results-trials-per-session:** still reproduced. A new data-check cell shows trial ids run from 1 with no gaps in every session and the imaged trials are a subset. So the tables look like whole behavioural sessions, though trials after the last one can't be ruled out. The conclusion now says the five deposited sessions may not be representative, so the match is weak evidence.

**Added or corrected:**
- **Label fields:** a data-check cell prints what every dF/F series' identifier and description fields hold. None carries a layer, cell-class or column label: `idStrs` just repeats the ROI id, `idStrsDetailed` is empty, and the ROI ids only number planes. This supports the 18 blocks that rest on the missing labels.
- **figs3d-neuropil-correction:** the notes and header now mention the route through the registered imaging files. The claim stays blocked because it needs L2/3 labels. The verifier's 165 GB is the whole data set; the imaging files are 146 GB, which is what the record says.
- **Helper (`ssc1.py`):** new functions for the error masks, unwrapping, the trimmed Hilbert peak and the sine check, each documented as a standard choice, not from the paper. The sample-epoch passages are now cited.
- **New finding:** the whisker angle contains undocumented tracking errors (single samples at ±90°, short jumps, and wraps past 90°), with examples printed.
- **Question for the paper's authors:** the existing whisking-amplitude question now also asks how tracking errors were handled.
- **Question for a reader:** I created `questions/peron-2015.yaml` for the verifier's sample-epoch point. The claims file's opening comment says 1 s, while the Figure 1C legend says 1 to 2 s. It cannot change any outcome here, because the attempt uses the pole-in-reach times stored in the data. The claims file is unchanged.
- **Record:** the round is in `attempts/peron-2015-01.yaml` under `verifications`, with all 43 claims, the verifier's reasons and my responses. The README now gives the corrected whisking numbers.

**Not done:**
- **methods-event-detection:** the verifier would block it as data missing. I kept "methods underspecified", because the protocol never blocks a claim whose data are deposited elsewhere as data missing.
- **an197522, 2013-03-10:** I could not show that its imaging and trial clocks agree. No tested claim uses that imaging, so it remains noted and recorded as a finding.
