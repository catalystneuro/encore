The claims file for DANDI:000959 is ready for an attempt (`ready: true`). I found five errors and two muddled criteria, all fixed. Two points stay open.

**Checker:** `36 claims, 36 quotes, 132 statistical values, 0 problems`, both before and after my edits.

The paper's analysis code is public, so I cloned it to a temp folder to check the details the criteria take from it. It is at commit cc0bf99, the commit the file cites.

**Changes, by claim**
- **Header, hemifield split (an error):** the header said fixations are split left/right at the centre of the partner's face. The code splits at `center_roi_m2_face`: the face ROI from the partner's calibration, which is the stimulated monkey's own face, mapped into the stimulated monkey's coordinates. This affects fig2e-ofc-contralateral, fig2e-dmpfc-accg-no-hemifield-effect, fig2gh-nonsocial-no-hemifield-effect, the two Mouth claims and the epoch slope claims.
- **Header, which fixations enter the distance (an error):** the Methods say social gaze distance uses all of the stimulated monkey's fixations. The code uses only fixations labelled as that monkey's alone and drops those labelled mutual; the header didn't say so. The protocol says Methods come first when they and the code disagree, so the Methods reading is now the main one and the code's is a variant.
- **fig2c-ofc-social-gaze-distance:** the criterion now says the outcome is judged on the Methods reading, with the code's reading shown as a variant.
- **fig2gh-nonsocial-no-hemifield-effect (an error):** same hemifield-reference fix as the header.
- **figs1e-eyes-more-than-face (an error):** the FDR correction was described as covering two tests. The code corrects over 15 day-count tests. figs1e-eyes-vs-rdm-comparable refers to this criterion, so it follows.
- **methods-ofc-no-change-in-fixation-number:** one sentence said the code counts both kinds of fixation and also that it counts only the monkey's own. It counts only the monkey's own; fixed.
- **fig4c-dmpfc-slope-late-greater (an error):** the bound p < 0.1 was made up. It is now the reported p = 0.054 plus 10% (p ≤ 0.0594), the protocol's default tolerance.
- **fig4d-dmpfc-slope-permutation (an error):** the criterion said `S1_Gaze_Time_Epoch.m` builds the shuffled null. No script in the repository builds it. The construction is now credited to the Methods and figure legends, and the criterion says the code loads a precomputed shuffled file.

**What remains open** (both recorded under `checks`)
- **fig4d null:** the shuffled file's causal-strength field is named `causal_m1m2_eyes_null`. That may mean the code's null also uses causal strengths from a null decomposition, which the Methods don't describe. The Methods construction is used.
- **Hemifield reference:** my reading of what `rois.m2` holds rests on a code comment ("m1 roi is m2's eyes from m1's perspective") and on how the partner's distance is computed. It is an inference, not something the code states.

Everything else matches the paper: statements, sources, quotes, statistics and expected values. The other code details the criteria cite are as described: trial selection, the latency calculations, the stimulation-count tests, the five excluded epoch days, the slope fits, the heatmap normalisation, the Fig. 5G permutation p-value and the pupil analysis. Each main finding has a claim, and all claims come from this paper.

Only `claims/000959/` was changed; nothing is committed or pushed.
