I worked through every point in the round-1 report. No outcome changed. The final `python tools/entry.py all entries/001950-su-2026` passed with 0 errors, and the notebook ran in 1921 s (about 32 minutes). Before writing the record I checked the executed notebook's numbers against the conclusions. Nothing is committed or pushed.

**Outcomes:** 13 reproduced, 10 partially reproduced, 5 not reproduced, 11 blocked. The verifier agreed on 37 of the 39 claims. I kept two of my outcomes against its view, and recorded both disagreements:
- **fig4c-choice-history** stays reproduced. The criterion tests only the R², the fraction of choices predicted, and the sign and decay of the rewarded coefficients. It does not test the 3.95 coefficient. The measured value is now the decay constant (1.391 trials), which does not match. The fit's amplitude (4.33) does match, and I asked a reader which of the two the legend means.
- **figs15t-crosscorrelogram-outcome-axis** stays partially reproduced, now marked as resting on an assumption. The outcome-axis part holds. The "no effect" part holds only when the shuffle keeps pairs within their session and pairs are placed by the difference of their positions (outcome p = 0.030, the other axes p = 0.13 to 0.36). With the ordinary shuffle it fails in most variants.

For the 11 blocked claims, the verifier gave different block reasons from mine. I kept mine. The ten anatomy claims are marked as data held elsewhere, and the protocol does not allow `data_missing` for those. For the cortex-projecting claim, the stimulation tables that the paper's code needs are not in the dandiset, so it stays `data_missing`.

**What I added to the notebook and helper:**
- **Q-learning model:**
  - A parameter-recovery check: on 40 simulated sessions the per-trial RPE and chosen value are recovered at median r 0.995 and 0.991, although the parameters themselves are recovered less well (r 0.56 to 0.96).
  - A refit that pools sessions within each mouse, approximating the paper's hierarchical fit. It leaves no session at the aF = 0 bound (107 were there before).
  - Every Q-dependent claim keeps its outcome with these variables.
- **Population sensitivity:** a new section reruns the single-neuron results on three other populations: 207 units passing the model-based session criteria under the per-session fit, 229 under the pooled fit, and 226 units the unpublished draft labels as the paper's. All outcomes hold, with two exceptions now in the notes:
  - fig5d reproduces on the 207-unit population only (r = 0.231 and 0.235). It is now marked as resting on the population choice.
  - fig5b gives 51.3% on the draft units, just outside the tolerance.
- **Drift stand-in:** the trial-index regressor is now also in the fig5g switch regressions and the outcome regressions. fig5g's best reading is now R² 0.055 (p = 0.068), and fig5h's best is r = 0.229 and 0.220; both still miss.
- **figs15q:** now follows the paper's own code (lick cleaning, 0 to 1.5 s in-trial window, smoothed rates, baseline, peak window): r = 0.580 to 0.618, still above tolerance.
- **figs14:** added 50 to 8,000 Hz filtered waveforms and a check that amplitudes are in µV.
- **figs16:** added the code's fit, linear detrending and a breakdown by mouse. The spike–pupil correlations stay mostly negative.
- **iti-mean:** printed the `ITI_duration` column. It is 0.5 s in every photometry trial, so it does not hold the paper's intervals.

**Record:** round 1 is under `verifications`, with the verifier's reasons in its own words. The notes, deviations and measured values for the affected claims are updated. I added two findings: the code's lick gap and pupil averaging differ from the Methods, and the stimulation tables and pupil confidence values are missing from the dataset. The questions for the paper's authors now cover the figs15t shuffle method, the 3.95 coefficient and the lick gap.

**Questions for a reader:** I added two to `questions/001950.yaml`:
- iti-mean: the Methods measure the interval between consecutive cue onsets. Under that definition the mean is 7.48 s, which would fail.
- fig4c: whether 3.95 is the fit's amplitude or its decay constant.

**Not done:**
- The paper's full hierarchical Stan fit was not run; cmdstan is not in the locked environment, so the pooled refit stands in for it.
- The kNN tests still use 1,000 permutations. The verifier found no conclusion at 0.05 depends on this.
- Cortex-projecting neurons still cannot be tested from the published version.
- My check that the published files hold no antidromic stimulation events was done outside the notebook. The record only mentions it and takes no number from it.
