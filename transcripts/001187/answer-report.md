There was one question, on fig3a-area-interactions, and it also covered eight other GLM claims. I changed the claims file in part.

**Answer:** The Methods outlier rule does apply to the GLMs. The sentence "Before each test, we removed neurons ..." comes right after "or mixed-effects GLMs (fitglme.m in MATLAB)", so it is not limited to the t-tests as the question argued. But the Methods don't say what value to compare when a GLM has a continuous term. The claims file's O-M rule (one value per neuron and condition) was the claims file's own reading, not the paper's.

The paper's code for the Fig. 3a GLM (`NWB_computeGLM.m`, commit 6d07204, which I read) settles that: one value per neuron, its mean normalised rate over all its rows. Where the code then departs from the Methods, I kept the Methods, as protocol step 2 says. The code's cut-off is 3 SD with no centring and on the upper side only, while the Methods say "±3 SD from the mean".

**What changed in the claims file:**
- **Header rule O:** it now defines a new rule, O-G: the code's per-neuron means, with neurons removed when they fall outside mean ± 3 SD of those means. O-G is the main reading for the GLMs of Figures 2 and 3. The code's rule (O-C) is a variant, and O-M is no longer a reading for those GLMs.
- **fig3a-area-interactions and fig3b-hippocampus-predicts-ltm:** their criteria now name O-G.
- **The other seven claims** (fig2b, fig2c, fig2e, fig2f, fig3b-amygdala-no-prediction, fig3g, fig3h) pick up O-G through the header rule.
- **Unchanged:** expected values and grading rules. O-M still applies to the permutation t-tests and to the Figure 4 GLMs, which the question did not cover.

O-G is a third rule that this attempt has not computed, so the author will need to run it. It should be very close to O-C, but that is my expectation, not a result.

`questions/001187.yaml` now has the answer and `answered: 2026-11-01`. `python tools/claims_check.py` reports 0 problems. Nothing is committed or pushed.
