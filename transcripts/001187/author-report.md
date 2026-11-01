I finished steps 1 to 5 of the Author section and ran the handover (step 6) at 08:21 UTC. `python tools/entry.py all` passes: 0 errors, and the notebook runs in 6.9 min. I did not verify my own work, and nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| sessions-and-neurons | reproduced (46 sessions, 950 units; 351 and 532 after the rate filter) |
| table-s1-counts | partially reproduced (unit counts match in 42 of 46 sessions) |
| behaviour-overall-accuracy, fig1c, fig1e, ltm-rt-confidence, fig1f, fig1g | reproduced |
| fig1d-wm-rt-load | partially reproduced (t = -4.28 against the paper's -4.29, but p = 0.0003, not below 0.0001) |
| category-neuron-counts | reproduced (102 hippocampus, 222 amygdala) |
| fig2b, fig2e, fig2f | partially reproduced |
| fig2c-hippocampus-correct-load | not reproduced (rests on an assumption) |
| fig3a-area-interactions | partially reproduced (rests on an assumption) |
| fig3b-hippocampus-predicts-ltm | partially reproduced |
| fig3b-amygdala, fig3d, fig3f | reproduced |
| fig3c-hippocampus-high-confidence | not reproduced |
| fig3e-early-delay-cluster | partially reproduced (the significant cluster is at 0.875 to 1.05 s, not 0 to 650 ms) |
| fig3g-nonpreferred-no-effect | reproduced (rests on an assumption) |
| fig3h-encoding-no-effect | not reproduced (rests on an assumption) |
| ms-neuron-counts, fig4b, fig4c | reproduced |
| fig4d-category-no-memory-signal | blocked, metadata_insufficient |
| fig4e-fs-strong-maintenance | not reproduced (the effect goes the other way, not significant) |
| fig4f-ns-no-effect | reproduced (rests on an assumption) |

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.240904.2347. It is the version the paper cites and the only published one.

**Dataset findings.**
- Table S1 lists 973 units against 950 in the dandiset; four sessions differ.
- Every file names Cedars-Sinai as the institution, though 20 sessions are from Toronto Western or Johns Hopkins.
- New LTM pictures (IDs 1001 to 1200) have no category. Neural responses suggest blocks of 40 IDs per category, but that is an inference, so fig4d stays blocked.
- The confidence coding is undocumented, though it agrees with the accuracy column in every trial. One trial has confidence 7.
- Five units have spike times out of order. I sorted them before analysis.
- Eight sessions have fewer than 400 LTM trials, and one has 139 WM trials.
- The paper's code removes outliers differently from the Methods and keeps the session whose ratings are all "sure".

**Assumptions.**
- For the GLMs, the Methods outlier rule's "tested conditions" are the levels of the categorical factors (confidence is continuous).
- Fig. 2c uses baseline B1, the mean over all WM trials, with the main-effects model.
- Fig. 4f uses all trials of the old pictures, keeps self-pairs, and uses spikes per second.

**Questions for the paper's authors.** Two are recorded as `methods_unavailable` findings: how the outlier rule applies to the GLMs (and which baseline Fig. 2 used), and the variable names lost from the Fig. 4e/4f GLM sentence.

**Question to a reader** (`questions/001187.yaml`). Should the code's outlier rule be the main reading for the GLMs? With it, Fig. 3a gives 56.61, 16.60 and -27.83, and with the all-sure session kept 59.96, 17.84 and -29.16; Fig. 3b hippocampus gives 21.25, 67.37 and -30.69. All are within tolerance of the paper, which the Methods rule does not achieve.

## 3. Where the protocol was unclear

1. The claims file header says to block a claim when its readings disagree; protocol step 1.6 and the prompt allow adopting the best-supported reading as an assumption. I followed the protocol and marked those outcomes `assumed: true`.
2. Neither the protocol nor the claims file says how a per-condition outlier rule applies to a GLM. I treated it as an open method detail, ran two readings, and asked a reader as well.
3. The protocol does not say how to handle reference numbers needed only for comparison, such as Table S1. I put them in the helper as a labelled text table taken from the paper.
4. The protocol does not say whether an inference from the neural data, like the picture-category blocks, may be used. I showed it as a variant only and kept the claim blocked.
5. A presigned DANDI download URL refuses HEAD requests, which `docs/archives.md` does not mention. I read the redirect `Location` header instead.

## 4. Runtime and failures

- The run took 1 h 04 min of wall time (07:17 to 08:21 UTC), and the notebook takes 6.9 min.
- The default statsmodels optimizer stopped at a poorer fit once. I now run three optimizers and keep the best fit.
- Nothing is left failing.
- Untracked dotfiles (`.bashrc` and others) and a `scripts` directory sit in the repo root. I didn't create them and left them alone.
