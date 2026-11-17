I checked the file for DANDI:000054 against the paper and made seven changes. It is ready for an attempt, though several criteria rest on interpretations the paper does not give.

**Checker:** `28 claims, 27 quotes, 16 statistical values, 4 problems`. All four are p = 6e-05 in `edf9l-null-models-frequent`. The legend prints it as "6.0 × 10 −5" and the checker doesn't match that form, so the values are correct and nothing changed. Every quote matched word for word.

**Changes, by claim:**
- **cells-per-session:** the criterion counted the four decision-task mice (FD1 to FD4) without the paper saying to. Extended Data Fig. 1a,b plot only the rare and frequent morph mice. Both versions, with and without the FD mice, are now named.
- **fig3ab-block-versus-gradual-similarity:** the old criterion could not tell two blocks from a gradual change, because its rare-mouse and frequent-mouse conditions both hold under gradual remapping. I replaced it with a "step share": the largest drop in similarity between neighbouring morph values, divided by the whole drop from one extreme to the other. It is compared between groups with the paper's mouse permutation test and marked as an interpretation the paper does not give.
- **edf6-nmf-confirms-remapping:** same fault ("high", "low" and "step" were undefined). It now uses the same step share on the NMF factors.
- **edf5-umap-rare-frequent-separable:**
  - The Methods say 100 shuffles for the classifier test, the Extended Data Fig. 5c legend says 1,000; both are now run.
  - The UMAP Methods name no sessions, so sessions 8 to N are now cited to the Results.
  - The morph bin edges are named as open, with a standard choice.
  - The paper's 18,230 cells kept is added for comparison.
- **fig7-model-reproduces-remapping:** the Methods list a weight-noise term (sigma_w, 0.05 N(0,1)) that the criterion left out. It appears in no equation, so versions with and without it are both run.
- **edf1-licking-before-reward:** the statement includes running, which no figure shows and the criterion did not test. The criterion now says running is not judged.

**Still open:**
- **Judged by eye:** seven claims rest on interpretations because the paper judges them by eye (edf4bc, fig3ab, edf6, edf7, fig4, edf9-early-sessions, edf10). Each is marked as such.
- **Likelihood width:** the Methods' "variance of 8.23" matches the code's width parameter, so the Methods may mean a width. The Methods version stays the main one and the code's widths are variants, as the protocol requires.
- **No recorded data:** the Unity scene renders (Extended Data Fig. 2), the network model (Fig. 7) and the simulations (Extended Data Fig. 3 and the supplementary figures) use no recorded data. The protocol has no data kind for them, so they stay under the default, the dataset.
- **No claim for Extended Data Fig. 5d:** a secondary finding, judged by eye, that frequent-morph UMAP clusters change position gradually and have wider spatial preferences.

All main findings have a claim, and every claim comes from this paper. The check entry is at the end of the file under `checks`, with `ready: true`. I did not commit.
