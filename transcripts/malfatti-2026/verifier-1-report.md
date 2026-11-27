**A. Outcomes**

The claims file has 34 claims. The notebook tests 8 of them and treats 26 as blocked.

| Claim | Outcome | Reason |
|---|---|---|
| pc-selection-counts, supfig2i-baseline-lower, fig1j-session-effect-controls, fig1j-session2-success-lower, fig1j-genotype-session6, trial-adjacency, supfig3-baseline-epochs, supfig2j-phase-amplitudes, supfig2j-control-training-decrease, supfig2j-creplus-naive-failed, supfig4-ratio-interaction, supfig4-ratio-reconfiguration, fig2d-latency-accuracy, fig2d-control-temporal-separation, fig2d-genotype-latency, fig2i-peak-width, supfig6-width-training, assemblies-counts, fig3g-salience, fig3k-assembly-area, fig3l-resilience (21) | blocked (data_missing; the notebook says too_large) | I checked the archive. It has 566 assets: 224 NWB and 342 AVI. The miniscope NWBs have an empty `OnePhotonSeries` and only a `behavior` processing module, and `variableMeasured` lists no ROI or fluorescence data. No part of these claims can be tested without re-deriving CNMF-E traces from 89.4 GB of raw video. |
| supfig1-cfos-validation, fig5b-ablation-efficiency | blocked (data_missing) | The archive has no histology. The only groups are BehaviourL5GqMC, L5PCMSMCGq and LFPM1GqMC. |
| fig5d-pasta-drops, fig5gh-hanging-wire, fig5i-ablation-prehension | blocked (data_missing) | The archive has no caspase group, pasta handling or hanging wire data. |
| fig1fh-no-genotype-effect-learning | reproduced | Cell 22: the genotype p is above 0.05 under every reading and variant (smallest 0.141). The main table's raw-count total gives F(1,11) = 0.048, p = 0.831, against the paper's 0.048 and 0.83. The success ratio gives 0.327, p = 0.579, against 0.336 and 0.574. |
| fig1fh-session-effect | reproduced | Cell 24: the session effect has p ≤ 5.25e-07 for all three measures under the auto test (ATS ≤ 0.002). Means over mice rise from session 1 to 2 (for example 48.1 to 90.0 for total, raw) and fall in sessions 5 and 6, in every table. The degrees of freedom are 9,99 rather than 10,110 because only 10 distinct sessions are deposited. |
| prehension-overlap | partially_reproduced | Cell 26: failed exceeds successful in every session under all 24 readings and variants. At most 1 of the 10 values is within tolerance; for example, successful in session 1 is 13.9 to 30.6% against 3.17%. |
| fig4b-clz-improves-success | reproduced | Cell 28: in Cre+ mice CLZ beats saline in 5 of 5 mice (reading a, F(1,4) = 19.7, p = 0.011; reading b, p = 0.0085). Controls show no effect (p = 0.62 and 0.63). The same holds with the four-body-part variant. |
| fig4d-theta-genotype | not_reproduced | Cell 32: under the criterion's test (mixed ANOVA, since Shapiro does not reject) the genotype p is 0.167 to 0.480 for theta and 0.143 to 0.447 for low theta. That is 0 of 12 readings, although Cre+ is higher in all 12. The accuracy effect also has p > 0.17. |
| fig4e-high-theta-accuracy | not_reproduced | Cell 34: the accuracy p is 0.117 to 0.745, so 0 of 12 readings pass, although successful is higher in all 12. |
| fig4fh-gamma-session13 | not_reproduced | Cell 36: no reading gives both genotype effects, and no reading gives an accuracy effect (0 of 12). One band holds only in 4 of 12 readings, all realigned, 3 of them through the ATS. No deposited reading gives even the partial outcome. |
| supfig7-lfp-nonprehension | not_reproduced | Cell 38: the genotype × session interaction reaches p < 0.05 in only 0 to 2 of the 7 bands. Partial needs at least 3. |

The paper states no chance level for any selection, so there was nothing to compare.

**B. Problems**

1. **[affects a conclusion]** Cells 19–20 and 30–38, `locked_lag`/`SHIFT`: the "realigned" reading is the notebook's own.
   - It moves the onsets of four mice by a lag chosen to maximise the prehension-locked LFP, and then tests prehension-locked power on the same data, which is circular. It also adds about 8 s of shift to WT mice only, so the shift is confounded with genotype.
   - The partial genotype result in fig4fh exists only under this reading, and it raises supfig7 from 0 to 2 bands. Neither changes the outcomes above, but the fig4fh pattern depends on it.
   - The "dated December 2021" description rests on `session_start_time` values like 2021-12-31T23:59:59.84 (69107), which looks like a placeholder, not a recording date.
2. **[affects a conclusion]** Cell 26: the miniscope DLC gives very few prehensions. Six of 28 files have none: for example, 67111 has none in sessions 1–2, and 67110 has 4, 11, 0 and 6. Mouse 67109 alone supplies 322 of the 841 prehensions.
   - This is hard to square with the paper analysing PCs for 3 control and 3 Cre+ mice in all four sessions. The notebook never checks tracking quality per file, nor which 6 mice the paper used.
   - So the overlap magnitudes that fail (the "partial" part) may reflect detection that does not match the paper's in this group.
3. **[does not affect a conclusion]** `learning_table`: it keeps deposited sessions 7–10 under their own numbers. The module docstring (lines 32–33) and BehavOnly.py line 330 both renumber sessions after 5 by +1. Only the unjudged "stable after session 7" description is affected.
4. **[does not affect a conclusion]** `learning_table`: session 5 is split at a fixed 300 s, while the code uses per-mouse thresholds from `Session5Split.dict`, which is not in the repository. The Methods' "after five minutes" supports 300 s, and I checked that the DLC start time is 0 in all 13 session-5 files.
5. **[does not affect a conclusion]** `learning_table(keep_copy=True)`: this variant counts a duplicated recording as an eleventh session. It only serves to match the paper's degrees of freedom and has no meaning of its own, but the genotype outcome is the same.
6. **[does not affect a conclusion]** `lfp_tests`: the auto test almost always picks the mixed ANOVA (Shapiro with Holm over 24 cells of 4–6 mice each). The ATS would give a theta genotype p < 0.05 in 7 of 12 readings. The criterion and the paper's F(1,8) both point to the ANOVA, so the outcome stands, but it rests on that choice.
7. **[does not affect a conclusion]** `window_means`: with 1 s spectrogram windows, a "before" bin centred just before onset reaches up to 0.5 s past it, so the before and during phases blur. The 0.5 s variant reduces this. No judged contrast is a phase contrast.
8. **[does not affect a conclusion]** Cells 15–17: the reason given is too_large, but the deciding fact is that no extracted traces or ROIs are deposited. Re-deriving them also needs CNMF-E and cell-matching parameters, not only compute time.

On the helpers themselves: I diffed `reach_classify` against Core.ReachClassify at commit 86efdf1 and it is the same line for line. On synthetic data, `mixed_anova` matched pingouin (unbalanced 6 vs 7 mice, 1 within factor) and statsmodels AnovaRM (2 within factors). `holm` matched statsmodels, and `overlap_flags` behaved correctly. The 13.8% limit of the onset threshold is correct.

**C. What I could not check**

- **`ats` against R nparLD:** R is not available here. Adding one ATS table computed in nparLD would settle it.
- **Miniscope detection:** whether it matches the authors'. A per-file table would show it: the fraction of frames with LPaw and LFinger1 likelihood above 0.7, each subject's genotype, and prehensions per genotype and session.
- **The 8 s LFP offset:** whether it is real. The deposited files have no LED or sync trace. The LFP tests rerun with the four mice left out, rather than realigned, would show how much rests on the shift.
- **The deposited LFP channel:** its description is "All accepted MOp5 channels", but whether it is a mean or the code's SingleCh is unknown. Reading (b) of the claims file has only one answer for that reason.
- **The per-mouse session-5 split times:** not available.
