I finished steps 1 to 6 for `entries/henry-2022/`. The run took about 3 h 20 min and both notebooks pass `tools/entry.py all`. The attempt record is `attempts/henry-2022-01.yaml` and the handover package is in `executed/henry-2022/handover/`. Nothing is committed.

**1. Outcomes (32 claims)**

| Claim | Outcome |
|---|---|
| data-populations | partially reproduced (rests on an assumption) |
| fig1b-v4-rf-larger, figs4-rf-alignment, fig6-well-isolated | blocked: data_missing |
| fig2a, fig2b, fig2c-farthest-spacing-slopes, fig2c-v4-worse-all-spacings | reproduced (e.g. V1 0.580, V4 0.206) |
| fig2de-population-decoding-example | reproduced (the V1 part holds only when all 84 cases are used) |
| fig2f-v1-threshold-elevation | not reproduced (1.69 and 1.67 against 1.31 and 1.15) |
| fig2f-v4-threshold-elevation | partially reproduced (significant and above V1, but 7.30 against 2.52) |
| figs3-pseudo-populations | reproduced (7 of 8 pairs within 2 SEM) |
| fig3ab correlations, fig3c shuffled, fig3d and fig3e Fano factors | reproduced |
| fig4a-v1-modulation-indices | partially reproduced (closest spacing holds, far spacing does not) |
| fig4b-v4-modulation-indices | reproduced (V4 above V1 only when the t test is on log indices) |
| fig4c, all three claims | reproduced |
| figs5-additive-vs-multiplicative, fig5-terms-covary, fig5de-simulated-discriminability | reproduced |
| fig5bc-tuning-model-terms | partially reproduced (directions hold; V1 m is 0.41 against 0.59) |
| fit-quality | not reproduced |
| fig5-negative-multiplicative | partially reproduced (23% of V1 cases, not rare) |
| fig6c, fig6d | partially reproduced (the tests hold, the values do not) |
| fig6e-tuning-correlation-configuration, figs6-common-neuron-pool | reproduced |
| fig7cd-fixed-decoder-generalization | partially reproduced (the tests hold, d' is much lower than the paper's) |

Totals: 19 reproduced, 8 partially reproduced, 2 not reproduced, 3 blocked.

**2. What I found about the dataset**
- **Blank epochs are not blank in six sessions.** In sessions 1, 2 and 8 to 11 (12 of 22 populations per area), the epochs labelled blank and distractor-only give the same counts as the target epochs. The labels do line up with the counts, because orientation tuning shows up only with the true labels. So the spontaneous rate cannot be measured in those sessions.
- **V4 epochs are in a different order.** V1 and V4 entries of the same population hold the same epochs in different orders. The V1 order looks like recording order and the V4 order does not. As a result, epochs cannot be matched across areas, and the even/odd reliability split gives 244 V4 units against the paper's 198. V1 gives exactly the paper's 146.
- **Units are already selected.** The deposit holds exactly 396 and 691 units, but the Methods' selection rule keeps only 115 to 147 of them.
- **Missing labels.** The two epochs of a trial are not marked. The orientation experiment does not store its spacing, and the description never mentions the blank or distractor-only epochs.
- **Missing data.** The receptive-field maps, the per-session coarse mapping and the waveform SNR are not deposited, which blocks three claims.

I made one assumption: blank epochs are the spontaneous condition (data-populations, `assumed: true`). The questions for the paper's authors are recorded as a `methods_unavailable` finding: how spontaneous activity was measured for the selection, the decoder and threshold-fit details, and how the tuning model's means were averaged. I asked no reader questions.

**3. Where the protocol was unclear**
1. **Clock check.** The suggested check (decoding around trial start) does not fit data that are only counts per epoch. I contrasted target and blank epochs, and orientation tuning, with true labels and with labels shifted by one epoch.
2. **Run time.** The decoding claims need about 80 minutes. I split the work into two notebooks (46 and 35 minutes) and cut the pseudo-population draws from 20 to 10, recorded as a deviation.
3. **Editing conclusions after the final run.** I fixed liblinear's random seed just before the final run, so the decoding numbers moved slightly from my development run. I then corrected five Result paragraphs identically in the source notebooks and the executed copies, which changed text only. The protocol does not say whether this is allowed; re-running would have cost another 80 minutes.
4. **Partial outcomes.** Several criteria name no partial case. Where the direction and the test held but the values did not (fig2f-v4, fig5bc, fig6c, fig6d), I recorded partially reproduced.
5. **Pre-selected units.** The protocol does not cover a deposit that already holds the selected units when the stated rule cannot regenerate them. I used all deposited units and judged data-populations as partial.
6. **Comparisons with this attempt's own estimates.** fig3c and figs3 compare against this attempt's threshold elevations, which themselves differ from the paper's. The protocol is silent on this; I said so in the notes.
7. **Combining readings.** "Under one reading" is ambiguous when two independent open details combine, for example the fig4b values on indices with the test on log indices. I allowed combinations of readings the criterion lists.

**4. Runtime and failures**
- The two notebooks ran in 2781 s and 2076 s; peak memory was below 0.5 GB.
- Nothing failed in the final run.
- During development the scikit-learn 1.9 `penalty` argument quietly conflicted with `l1_ratio` and would have given L2 fits. I caught it and call liblinear directly with an L1 penalty.
- The repository root has untracked dotfiles and a `scripts` device node that the environment created at 00:06, before this run started; I left them alone.
