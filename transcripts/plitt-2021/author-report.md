I finished steps 1 to 5 of the Author section and ran the handover; the verifier's package is in `executed/000054-plitt-2021/handover/`. I pinned version 0.260415.1712, the latest published one. The paper cites only the draft, and the 2021 versions hold 10 of the 16 mice. Overall: 8 claims reproduced, 9 partially reproduced, 8 not reproduced and 3 blocked. The final `python tools/entry.py all` passed check and run, and nothing was committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| cells-per-session | reproduced |
| session-and-trial-counts | partially reproduced (decision-mouse trials out of tolerance) |
| training-intermediate-fraction | blocked: data missing |
| place-cell-fractions | not reproduced (60–69% rare, 48–57% frequent vs 43%, 30%) |
| edf4a-fewer-place-cells-frequent | reproduced |
| edf4a-overlap-above-chance | partially reproduced (the test holds, the four values don't) |
| edf4bc-overlap-cells-at-ends-and-reward | not reproduced |
| fig2eh-place-cell-similarity-differs | partially reproduced (raw part holds, z-scored part fails) |
| edf6-nmf-confirms-remapping | not reproduced |
| edf5-umap-rare-frequent-separable | reproduced |
| edf1-licking-before-reward | reproduced |
| fig3ab-block-versus-gradual-similarity | not reproduced |
| edf7-checkerboard-sessions | partially reproduced (5 of 6 sessions) |
| fig3f-zscored-difference-at-025 | reproduced |
| fig4-sf-stable-along-track | reproduced |
| fig6a-dkl-sign | partially reproduced |
| fig6bc-pooled-dkl | not reproduced |
| fig6d-prior-reconstruction | partially reproduced |
| map-estimate-values | reproduced |
| edf9-early-sessions | reproduced |
| edf9k-null-models-rare | reproduced |
| edf9l-null-models-frequent | partially reproduced (3 of 5 tests) |
| edf10-decision-mice-like-frequent | partially reproduced |
| fig7-model-reproduces-remapping | not reproduced |
| fig7g-model-prior-reconstruction | not reproduced |
| edf3-simulated-posterior-population | not reproduced |
| edf2-fh-best-predictor | blocked: data missing |
| supp-earlier-morph-studies | blocked: other |

**2. What was found about the dataset**
- **Only imaged trials.** Each file holds only the imaged trials of its session, and sessions 2, 4 and 6 are absent. The priors behind every posterior therefore come from the imaged trials before session 8. For rare-morph mice these include session 3, which is half intermediate: 13.8% of their trials here are intermediate, against fewer than 4% in the paper. R6 has no trials before session 8.
- **Full VR behaviour on figshare.** The authors later deposited the full VR behaviour on figshare (doi:10.6084/m9.figshare.31974756.v1). The dandiset does not reference it.
- **Sessions the paper doesn't describe.** The files include imaging sessions 5 and 7, where F6 has 4,103 cells. There are 26 rare sessions where the paper counts 24. FD3 has no session after 7, and FD1's sessions 1 and 3 hold continuous morph values.
- **Wrong recording dates.** `session_start_time` in every file is the 2026 conversion date, not the recording date.
- **Place cells stored in the files.** Each file's JSON annotation holds place cells from the authors' 2026 code. They agree with this attempt for about 96% of cell and morph pairs, and both are far above the paper's fractions.
- **Hebbian model.** With the parameters the claims file gives, the weights decay to zero during training, so the network learns nothing. The paper's code uses a rescaled stimulus unit instead.
- **Checks that passed.** No recording is deposited twice, and activity and trial labels share one clock in every session (to within about 0.5 s).

**Questions asked** (in `questions/000054.yaml`):
- Should the training-fraction claim and all the posterior-based claims take the figshare deposit as `with_inputs`?
- What input width and scale does the Hebbian model use, and is it tested with or without noise? I cite the code's `d_def` parameters.
- In edf4bc, how do a cell's two peaks enter the share?
- In edf3, what range do the simulated neurons' centres tile?

**3. Where the protocol was unclear or did not fit**
1. The full VR data are public, but neither the paper nor the claims file names them as an input, and an author cannot set a claim's `data` field. Neither `data_missing` ("not public anywhere") nor `elsewhere` fits. I blocked the training-fraction claim as `data_missing` and asked.
2. The protocol does not say whether to test or block claims that rest on partial data (the priors). I tested them, recorded the partial priors as a deviation in each, and asked.
3. The suggested clock checks (decoding around trial start, or shifted labels for continuous sessions) fit continuous VR poorly. I used the odd-even trial map correlation as a function of lag, plus trial labels shifted by one trial. I report the result as consistent with a shared clock, to within about 0.5 s.
4. The 30-minute limit per notebook forced two notebooks. The summary is only in the last one.
5. After the final run I made markdown-only edits (removing bold). I copied them into the executed copies, after checking that the code cells were identical, instead of re-running for 29 minutes.
6. edf9k/edf9l and fig7/fig7g each share one section with both claim tags, against "one section per tested claim".
7. Several criteria have no rule for a partial result. I used `partially_reproduced` when a criterion holds only in part.
8. The dataset holds imaging sessions the paper does not describe. I took the paper's imaging sessions (1, 3, 8 to N) as the main reading for cells-per-session and showed the count over every file.
9. The protocol does not say whether an author may read the paper's code. I read it only to implement what the claims file says to take from the code, and to frame the questions.

**4. Runtime and failures**
- **Runtime.** The final run took 29 minutes: 15.2 for notebook 1 and 13.6 for notebook 2.
- **Fixed during development.** Two bugs:
  - The place-cell maps were smoothed along the wrong axis.
  - The posterior simulation took 27 minutes until I limited each worker process to one thread.
- **Fixed after the final run.** A regex I used to strip bold text broke two code lines in my source script. I restored them before writing the final notebooks, and the run itself was unaffected.
- **Files I did not create.** There are untracked dotfiles (`.bashrc`, `.mcp.json` and others) at the repository root. I left them alone; check them before the workflow commits.
