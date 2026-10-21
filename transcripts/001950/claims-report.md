The claims file is written to `claims/001950/10.64898-2026.04.10.717727.yaml`; nothing is committed.

**Text read:** the bioRxiv preprint, version 1, full text from the JATS XML: Results, Discussion, Methods, and the legends of Figures 1 to 6 and Supplementary Figures S1 to S18. There is no separate supplement file; the supplementary figures exist in the text only as legends. The extraction lost every display equation in the Methods (the regression models, the Q-learning model, the drift measure, the Watson-Wheeler statistic) and the contents of Tables 1 to 3. Where those matter, the code fixes them and the claims cite it. The code's README cites a later Nature version of record, which I did not read.

**Code read:**
- `aind-beh-ephys-analysis` @ 971c1ca: all the physiology and behaviour analyses; it names DANDI:001950 as the home of the data.
- `aind_stan_fit_sim` @ 89371ee: the reinforcement-learning model.
- `aind-fip-dff` @ 03ca4d2: photometry preprocessing.
- `LC-ephys-tonguemovements` @ f6dd736: reaction-time analysis.
- `locus_coeruleus_norepinephrine_neurons` @ 43f7083: an index of the paper's 16 code capsules.

**Claims:**
- 44 claims, all 44 with a quote and a criterion; 22 have statistics and 23 have expected values.
- 38 use the paper's own data. 6 need outside inputs: MERFISH (Nardone et al. 2024), the MouseLight database, and the spatial axes from retrograde tracing and MERFISH.
- About 12 anatomy and gene-expression claims are included for coverage. This dandiset's description says nothing about holding those data.
- The quote check passes. It still flags three p-values printed with a trailing zero ("3.0 × 10 −4" twice, "3.40 × 10 −5"); I confirmed each by reading the text.

**Details the paper leaves open, and the readings named:**
- **Which neurons:** the Methods criteria are the main reading and the code's criteria a variant. The code skips the presence-ratio and amplitude-cutoff criteria but still gives the paper's 241 neurons from 19 mice.
- **Go-cue counts (fig4g):** whether a significant change must also be an increase (the code doesn't check the sign).
- **Fig. 4h baseline:** a 2 s baseline (the code) or 0.5 s.
- **46.5% (fig5b):** denominator of all 241 neurons, or only those with at least 2 ignored trials. The code's model adds a switch regressor.
- **Switch definition:** against the previous responded choice, or the code's version, where a trial after an ignored one counts as stay.
- **Outcome windows:** Methods (1 s, aligned to response time) or code (1.5 s, aligned to reward delivery, with fixed window centres).
- **76.8% "significant":** outcome coefficient p < 0.05 (which gives 185 of 241), outcome or chosen value, or the whole-model F-test.
- **Fig. 6a p = 3.0e-4:** linear-model or kNN test.
- **Fig. 6c rho:** two measures (Methods or code) crossed with Spearman over all trials or over 9 bin means.
- **Fig. 4c:** the Methods' reward and no-reward model or the code's reward and choice model, pooled or per mouse. R2 read as McFadden pseudo-R2 or as the R2 of the exponential fit.
- **Photometry:** with the isosbestic regressor (Methods) or without it (code); outcome window 2 s after outcome (Methods) or −0.3 to 1.7 s around the choice lick (code). For the Fig. 6j/6k Fisher test, which has no code, the table is the sign of the outcome t-statistic or membership of the RPE quadrant.
- **Others:** lick-bout gap (0.5 s in the Methods, 0.8 s in the code); pupil time constant per session or per neuron; sessions and trials counted for the session statistics; what "well-trained" means; the sign convention for "more symmetric" waveforms.

**Missing from the paper that some claims needed:**
- The code does not compute 76.8%, 46.5%, rho = 0.84, R2 = 0.60 or the 0.88 prediction rate.
- There is no code for the Fisher test of Fig. 6j/6k.
- Some of the paper's numbers have no stated test, so for those claims the criteria are readings of the figures: Fig. 5b direction, Fig. 6g, 6h, 6i, and the population pupil correlation.

**Where the paper or code disagree with themselves:**
- The calcium indicator is named differently in the Results and the Methods.
- The Fig. S15f legend gives the same r and p for two different panels.
- Fig. 6i says 9 mice, but the code's outcome regression prints 7 mice and 67 sessions.
- The code's Fig. 5b/5f scatter has its condition labels swapped and uses a 0.3 s window, not 0.5 s.
