I wrote `claims/000620/10.64898-2026.01.27.702062.yaml`. The quote checker reports 26 claims, 26 quotes, 16 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the bioRxiv preprint, version 1, from its JATS XML: the main text, the Methods, and the legends of Extended Data Figs. 1 to 11. The paper has no separate supplement. There was no PDF for this paper, so I could not look at any figure panel, and the XML version leaves out the model equations (the models are still described in words). The `paper/` folder also holds a second paper, "A Relational Code for Objects…" (doi:10.64898/2026.10.17.759839). It is not the paper this run was asked to cover, so I did not use it.

**Code read.** I read `jazlab/multi_object_memory_2025` at commit 6e4b333: the behaviour and physiology processing, the model code and its settings, and the figure notebooks, several of which print their results.

**Claims.** There are 26, and every one has a quote and a criterion. Seven have statistics (16 entries); eight have expected values with tolerances. They cover:
- behaviour (Fig. 1b and 1c, and Extended Data Fig. 1);
- neuron and session counts for both datasets;
- activity in the stimulus and delay phases, and decoding (Extended Data Figs. 2 and 3);
- selectivity (AUC) and the signal versus noise correlation relationship (Figs. 2b, 2d and 5e);
- the model comparison (Figs. 4a and 5f), the brain-area controls, the general Slot model, the synthetic-data recovery test (Fig. 4b), and the choices of two slots and of temporal smoothing;
- whether the gains are spread across objects (Extended Data Fig. 7);
- gain against accuracy and reaction time (Figs. 4c, 4d, 5g and 5h), and the same for the Slot and Switching models (Extended Data Fig. 8).

For the correlation values I used the paper's own ± as the tolerance; the code shows it is the standard deviation of R over 1,000 bootstrap resamples.

**Details left open, with the readings named for each:**
- **What counts as correct:** within 2.4° of the target (Methods) or 4.8° (code). Both are run.
- **Trials in Fig. 1b:** Triangle trials only (code) or Triangle and Ring pooled (legend).
- **Which units are counted:** good and multi-units above 1 Hz (this is how the code reproduces 4,688); the same plus at least 500 stable trials (Methods); or single units only ("well-isolated").
- **Minimum stable trials per unit for modelling:** 500 (Methods) or 200 (code).
- **AUC p-value:** 1,000 label shuffles (Methods) or 5,000 bootstrap resamples (code). The legend calls the AUC values "cross-validated", but neither the Methods nor the code says how; I recorded this as a deviation.
- **Triangle noise correlations:** the Methods' 9 and 18 conditions, or the code's method built on triples of conditions.
- **Ring noise correlations:** a correlation over each trial's 10 nearest trials (Methods wording), or residuals from those neighbours (code).
- **Significance level in Fig. 4a:** p < 0.05 (legend) or p < 0.01 (where the code draws its brackets). The test itself is an independent t-test (code).
- **"At least 100 units":** ≥ 100 or > 100.
- **Order of steps in Fig. 4d:** average the gains over splits then normalise (legend), or normalise then average (code).
- **Ring sessions:** the 22 recorded or the 20 the code lists. Ring left/right trials are included (Methods) or excluded (code).
- **Synthetic-data test:** 2 new train/test splits (Methods) or 5 (code).
- **Descriptive words with no number or test** ("wide", "common", "similar", "typically", "broadly consistent", "distributed"): each criterion names two readings, or states the cut-off as my own reading of the word.

**Problems in the paper that bear on claims:**
- The statistics for Extended Data Fig. 8a are garbled; only "−4 … −10" survives, and the R values are missing.
- The Extended Data Fig. 8b legend says "not significant for either monkey" yet prints p = 0.034 for Monkey P.
- The Switching model's R for accuracy (0.65 and 0.34) is higher than the Gain model's, which contradicts "weaker" for accuracy. So that claim is judged on reaction time.
- The paper says Gain wins in 88% of sessions; the code's printed output gives 22 of 24 (92%). That is within the 10% tolerance.
- Some figure references in the paper point to the wrong panels (the Methods cite Fig. 5c and 5e–f for what are 5e and 5g–h; the Results cite Extended Data Fig. 8 for what is Fig. 9).
- Without the figures I could not check which significance brackets Fig. 4a actually shows.
