## Report: author-answers run on 001187-daume-2024-01

There was one question, asked on `fig3a-area-interactions`, and its answer applies to all nine GLM claims of Figures 2 and 3. I re-ran all nine. Six outcomes changed: four moved towards the paper and two dropped their assumption. Three outcomes are unchanged. The entry is locked and checked with 0 errors. It ran from a clean environment in 648 s, and the handover package is in `executed/001187-daume-2024/handover/`. Nothing is committed.

**What the answer changed.** The reader decided that the Methods' outlier sentence does cover the GLMs. The values it compares come from the paper's code (`NWB_computeGLM.m`): each neuron's mean normalized rate over all its rows. Where the code departs from the Methods on the threshold, the Methods win. Claims header O now makes this rule, O-G, the main reading for these GLMs: a neuron is removed when its mean lies outside the mean ± 3 SD of the neuron means. The code's own rule (O-C) is a variant, and the Methods' per-condition rule (O-M) is no longer a reading for them. Expected values and grades are unchanged.

**What I changed:**
- `sbcat.py`: added `og_remove`.
- Notebook: the Fig. 2 and Fig. 3 GLMs now run O-G (main), O-C and no removal. Both rules work on the full table before trial selection, as the code does. For Fig. 3b reading (a), "outliers over both areas", the outliers are now found on the table of both areas.
- I rewrote the conclusions, the summary and the README.
- `entry.yaml`: runtime raised from 7 to 11 minutes.
- Attempt record: each claim's notes say what the answer changed.
- I reworded the `code_mismatch` and `methods_unavailable` findings to match.

| Claim | Earlier (O-M) | Now (O-G) | Numbers now |
|---|---|---|---|
| fig2b-hippocampus-persistent | partially reproduced | partially reproduced | 20.22 and 14.11, both above tolerance under one row per trial with B1; a beta is outside tolerance in every reading |
| fig2c-hippocampus-correct-load | not reproduced (assumed) | partially reproduced (assumed) | accuracy 18.48 (p = 0.0499), load 18.64 (p = 0.0003), both above tolerance; B2 gives the same grade |
| fig2e-amygdala-persistent | partially reproduced | reproduced (assumed) | 10.50 and 6.88, both within tolerance |
| fig2f-amygdala-load-not-accuracy | partially reproduced | reproduced (assumed) | load 11.55, within tolerance; accuracy p is at least 0.19 everywhere |
| fig3a-area-interactions | partially reproduced (assumed) | partially reproduced | 19.12, 70.57, -32.52: significant with the paper's signs, all outside tolerance; no longer assumed |
| fig3b-hippocampus-predicts-ltm | partially reproduced | reproduced | 21.25, 67.37, -30.69, all within tolerance under both readings |
| fig3b-amygdala-no-prediction | reproduced | reproduced | smallest p 0.43 |
| fig3g-nonpreferred-no-effect | reproduced (assumed) | reproduced | smallest p 0.089 and 0.11; no longer assumed |
| fig3h-encoding-no-effect | not reproduced (assumed) | reproduced | smallest p 0.30 and 0.078 |

**Outcomes still resting on an assumption:**
- **fig2c:** I assumed the main-effects model. With the interaction term it would be not reproduced. The accuracy p of 0.0499 is close to the threshold.
- **fig2e:** I assumed one row per trial. With the code's rows it would be partially reproduced.
- **fig2f:** I assumed main effects and baseline B1. Baseline B2 or the interaction term would give partially reproduced.

**Fig. 3a under the code's rule:** the code's own rule (O-C) gives 16.60, 56.61 and -27.83, all within tolerance. O-G does not.

The untracked dotfiles, `.idea`, `.vscode` and `scripts/` in the working tree were not created by this run.
