The file is fixed and fit for an attempt. I edited five of the 22 claims, recorded three open problems, and set the new check entry to `ready: true`.

**Checker result:** `claims/001683/10.1109-tnsre.2025.3644273.yaml: 22 claims, 21 quotes, 19 statistical values, 0 problems`. It reported 20 statistical values before my edits; one was removed (fig5cdj below).

**Changes, by claim**
- **fig2f-sham-percent-time-post3:** the criterion required post 3 to be lower. The paper only says "significantly different", so I dropped that condition; the direction is now reported but does not decide.
- **fig4-no-theta-alpha-gamma-power-change:** the criterion also required no sham-vs-tFUS difference. The Fig. 4 legend marks differences from baseline within a group separately from differences between groups, and the sentence is about "changes". So the absence now covers only within-group comparisons against baseline; group differences are reported but do not decide.
- **fig5b-tfus-evoked-potentials:** the criterion's per-time-point paired t-test readings were made up. Methods F says every comparison "between groups and time points" uses a two-way ANOVA with Bonferroni post hoc tests, so I put that in, as ordinary or repeated measures. I also named the pre-onset normalization as a standard baseline subtraction, and replaced "a run of significant time points" with "at least one significant time point".
- **fig5cdj-wild-type-gamma-pli-decrease:** I removed the p < 0.05 statistic for tFUS vs sham in Fig. 5J and its use in the criterion. No sentence in the paper states that significance, and the file's own header says the marks inside Figs. 2 to 6 were not read. That ANOVA is now reported but does not decide.
- **figs7-seizure-pli-s1-vs-non-s1:** the statement now matches the paper's hedged sentence ("may reflect distinct baseline network states", about wild-type vs seizure rats). The criterion now cites the Fig. S7A title "(seizure-baseline)" for the difference reading.

I checked the other claims, including the Fig. S4, S5 and S7 readings against the rendered supplement pages, and found them consistent with the paper.

**Still open**
- Results C says that "compared with the pre-4-AP baseline, CC tFUS improved interhemispheric balance (Fig. S5)". But Fig. S5 contains no tFUS data, so I could not set a test for that sentence and no claim covers it. The tFUS effect on the asymmetry index is covered by fig4ef-ai-increase.
- The quantity plotted in Fig. S7B is not defined anywhere. Its values go negative, so it is not raw PLI, and the "Baseline" bars cannot be interpreted.
- There is no PDF of the main paper, so the significance marks in Figs. 2 to 6 could not be read. Which blocks carry the AI, beta and Fig. 6 effects therefore stays open, covered by the criteria's alternative readings.

Nothing was committed or pushed.
