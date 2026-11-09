## Checks of claims file for DANDI:001767

**Checker result:** `claims/001767/10.1038-s41586-023-06492-9.yaml: 47 claims, 47 quotes, 29 statistical values, 0 problems`. Before my changes it read 46 claims and 0 problems. Only the claims file was changed, and nothing is committed.

**Changes, by claim**
- **ed1b-switch-after-block-transition:** the rule required the rise in every mouse. The panels show the mean ± s.e.m. over mice, so the rule now uses the mean.
- **fig1e-reward-outcome-post, fig1g-history-stay, fig1h-switch-da-approach:** these required a paired test across mice (T2) to reach p < 0.05. The paper reports no such test, and the file's own header says T2 is only reported. It no longer decides, and "more than half of the mice" is now marked as the reader's interpretation.
- **fig1e-reward-outcome-not-pre, fig1f-cue-omission:** the mouse counts are now marked as interpretations. fig1f now needs both window readings, where before it accepted either one.
- **ed3-not-lateralized:** it recorded p < 0.05 for a finding of no DA difference. It now records p > 0.05.
- **ed5f-leave-out, ed5-history-glm-r2, ed8f, ed11-cko-glm-r2, fig5a, fig5ef (both):** they used thresholds, tests and measures the paper does not give without saying so. Each is now named as a choice. ed11 also now tests "DA kernels comparable", which its statement says.
- **ed6c-da-bilateral:** dropped a zero-lag requirement that is not in the paper.
- **fig2d-anticorrelated-lag:** the statement said the controls show no anticorrelation. The paper states no result for the controls, so that part is removed. The criterion now marks the 0.3-s bound as the reader's choice and notes that the legend's "DA lags Ach" wording does not change the sign convention the Methods give.
- **fig3e-striatum-wide-telc:** the statement said ITI and decision time were "longer", but the paper gives no direction. The alpha test the statement mentions is now part of the criterion.
- **fig3f-vls-telc-da-unchanged:** the rule for combining the per-mouse tests is now marked as an interpretation.
- **ed8g-vls-telc-ach-suppressed:** the panel's traces are z-scored, which can hide a loss of signal size. Added a ∆F/F0 reading.
- **ed9jm-vls-telc-behaviour-normal:** added a third reading for the control group (sessions split by the hemisphere recorded). If the readings disagree, the claim is now blocked as underspecified; before, the author could pick one.
- **ed7e-cin-activation-evokes-da:** the legend does not say what the paired dots are, so two readings are now listed.
- **fig4bc-da-bidirectionally-controls-ach:** the Methods give two laser durations for this panel, 5 s and 1.5 s, and both are now readings. Dropped a requirement about DA under eticlopride that the paper does not state.
- **fig4g-cko-ach-suppression-lost:** noted that the legend prints "P > 0.05" for its significance circles. This is read as a misprint for P < 0.05.
- **New claim, fig3c-telc-blocks-cin-evoked-da-in-vitro:** Fig. 3c, the slice test showing TelC blocks DA release evoked by the cholinergic interneurons, is a main-figure finding and had no claim.

**Still open**
- Supplementary Data 1 is not under `paper/`. It holds the exact P-values for Fig. 1e and Extended Data Figs. 3e,f, 4c-e, 6d, 8i-k and 11d,e, so those claims record only the legends' P < 0.05.
- The paper describes many results with words like "robust", "consistent" or "abolished" and gives no rule for them. Many criteria therefore rest on thresholds the reader set; each one is now named as such in its criterion.

**Ready:** yes. The last entry under `checks` says `ready: true`.
