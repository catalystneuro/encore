I checked the claims file for DANDI:000011 against the paper. After my edits the file is fit for an attempt, and I marked it `ready: true`.

**Checker result** (after edits): `claims/000011/10.1038-nature17643.yaml: 38 claims, 38 quotes, 11 statistical values, 0 problems`

**Changes, by claim**
- **Opening comment (convention T):** the paper doesn't say whether the recorded "late delay" condition in the unilateral experiment ends 0.3 s before the go cue (as the Methods name it) or 0 s before (as the Results name it). I noted this; the author reads the actual times from the trial metadata.
- **fig1d-earlier-photoinhibition-minimal:** added `n: 5 mice` to the statistics.
- **ed5-photoactivation-recovery:** the criterion said the timing was not given, but the Results give a 500 ms photostimulus. I added it; only where it falls in the trial stays open.
- **ed2e-no-rebound:** the criterion pooled lick left and lick right trials. The legend uses lick right trials only, with a two-tailed t-test at p < 0.01, so the criterion now follows the legend. It also now judges both windows after photoinhibition offset, not just the first 400 ms.
- **fig2b-unilateral-performance:** limited to photoinhibition at delay onset, which is what the statement and the Results describe.
- **fig2b-bilateral-performance:** added `n: 13 mice` to the three tests.
- **ed7-larger-photoinhibition:** the statement offered the 490 and 235 ms recovery times as evidence that recovery was "less robust". The Results cite Extended Data Fig. 7e (ROC values) for that, and 490 ms is actually faster than the one-spot 538 ms. I separated the two parts. The criterion now judges "less robust" by the four-spot ROC against the one-spot ROC; the earlier comparison is kept as a variant, and I extended `depends_on` to match.
- **cd-captures-selectivity:** the criterion pointed to a claim `fig3-modes` that doesn't exist. It now points to fig3d-persistent-mode and fig3e-ramping-mode.
- **fig5-callosotomy-no-recovery:** spike-rate recovery now accepts either reading (a) or (b) of fig2-recordings-recovery, as that claim does. Before, it used only (b).
- **fig6-modular-models-recover:** the paper says only the attractor model drifts randomly when both modules are silenced, and the statement now says the same. The 90% and 30% to 70% thresholds are now marked as readings, since the paper gives no numbers.

**Still open** (recorded under `checks`)
- **ed7e-roc-larger-photoinhibition:** the legend prints the bilateral s.e.m. as 0.8, which can't be right for an ROC value. The tolerance of 0.08 assumes a dropped zero, which the text can't confirm; the 10% default would be 0.054.
- **Corrigendum:** the published correction (doi:10.1038/nature18623) was not in the supplied text, so it's unknown whether it changes any value.
- **Photoactivation condition names:** Extended Data Fig. 5c says "late delay" and Fig. 5f says "middle delay". The paper doesn't say whether they are the same condition.

Each of the paper's main findings has a claim, and every claim comes from this paper. Nothing was committed or pushed.
