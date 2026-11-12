I made 12 corrections in `claims/brinke-2017.yaml` and recorded 4 problems I could not settle. The file is ready for an attempt, and its new `checks` entry says `ready: true`.

**Checker result:** `claims/brinke-2017.yaml: 55 claims, 55 quotes, 84 statistical values, 0 problems`. I got the same line before and after my edits, and the file still loads as YAML.

**Changes, by claim**
- **modulation-absolute-not-rate-dependent:** the paper never says how suppression is signed. Its two printed suppression correlations (r = −0.131 and r = −0.211) do not obviously fit one convention, so the sign is now open with two readings. The facilitation test is now marked as a claim of absence.
- **fig2a-facilitation-properties-ds1:** the tolerances on the duration and magnitude means were the cells' SDs (41 ms, 20.2 Hz), which would pass almost any value. They are now 10%, like every other mean in the file.
- **fig2-s1-correlation-matrix-offsets:** the rule "at least six of eight offsets" was made up. It now needs all eight within tolerance; matching only the signs counts as partial.
- **fig2e-facilitation-ds2:** added the selection the text states, "in the presence of conditioned behavior" (CRs in at least 20% of trials).
- **fig4s1-cs-peak-cells:** the paper says no second-dataset cell showed this response, so that count now has tolerance 0 instead of 1.
- **fig5cd-cs-pause-faster-facilitation-ds1:** the criterion said the Figure 5C legend measures from the baseline mean; it does not. The reference is now open with two readings.
- **fig6s1bc-purkinje-us-complex-spike-opening:** removed `data: with_inputs`. The test uses only the Purkinje cell data of ten Brinke et al. (2015) and no IpN data, so it stays on the default and is blocked unless the author finds those data public.
- **us-pause-declines-with-training:** the reference for the pause magnitude was taken from a legend that describes a different comparison. The baseline is added as a second reading.
- **fig7-second-us-peak-dynamics:** the criterion said 121 + 46 = 167 matches no count. 167 is the number of recordings without behavior, and the Figure 7E legend limits the velocity comparison to those recordings, so both comparisons now run on them.
- **fig7b-first-second-peak-correlated:** removed a required bootstrap test on the number of significant cells; the paper reports no such test.
- **us-only-trials-ds2:** the criterion fixed "all 25 cells, from baseline" without a source. Which cells and which reference are now open, with readings.
- **suppression-same-timing-as-facilitation:** now says plainly that the paper defines neither onset nor peak time, and that the reading comes from the duration threshold in the Methods.

**Still open** (recorded under `checks`)
- The mouse counts disagree: 19 in the Results, 25 in the Methods (split 22 and 6). The second dataset's CS-US interval is 200 ms in the paper and 212 ms in the dataset description. Both are named in the opening comment.
- Several printed numbers contradict each other, for example p = 0.0254 in the text against 0.0218 in the legend, 13 against 15 cells for Figure 6D, and 41 against 37 for Figure 6H. The claims keep them as printed.
- The paper links no analysis code, so the open methods (baseline correction, how the bootstrap's random datasets are made, trial-by-trial facilitation, spike rate velocity, cross-correlation lags) stay as readings.
- The dataset description mentions only paired trials. The US-only trials and the optogenetic sessions may not be in the deposit, so the claims on them may be blocked. That is for the author to check.

Nothing is committed. The untracked dotfiles and folders in the working tree were already there and I left them alone.
