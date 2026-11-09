I finished steps 1 to 5 of the Author section and ran the handover at 20:09 UTC, well before the 22:59 cutoff. The entry is `entries/crcns-ofc-4-schuck-2016/` and the record is `attempts/crcns-ofc-4-schuck-2016-01.yaml`. `entry.py all` passes, and the notebook runs in about 5.5 min from a clean environment. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| behavior-error-rate | blocked: metadata_insufficient (the true error rate lies between 1.98% and 3.10%) |
| supp-errors-by-trial-class | not reproduced (Enter 4.79%; the other two classes together about 1.2%) |
| supp-errors-stable-over-blocks | reproduced |
| supp-errors-not-by-age-category | reproduced (assumed) |
| supp-training-errors-higher, supp-training-rt-unchanged | blocked: data_missing |
| supp-rt-stable-over-blocks, supp-rt-faces-faster, supp-rt-by-trial-class | reproduced |
| fig2a-16way-decoding | partially reproduced (8.93% against 12.2%, p = 0.002) |
| fig2-two-back-state-space | not reproduced |
| fig2b-hidden-components | partially reproduced (1 of 3 components) |
| fig2b-current-age-absent, fig2b-two-back-absent | reproduced |
| figs2c-8way-decoding | reproduced (assumed) |
| figs2a-permutation-control | partially reproduced |
| synthetic-data-control, fig5-synthetic-control | blocked: metadata_insufficient (no voxel coordinates) |
| fig2c-enter-cluster | reproduced |
| fig2d-enter-nonenter-decoding | not reproduced |
| fig3-searchlight-conjunction, other-rois-incomplete, supp-motor-action-not-in-ofc | blocked: data_missing |
| fig4a-decoding-error-correlation | partially reproduced (assumed; r = -0.27) |
| fig4b-error-trial-drop, fig4b-decline-before-errors | not reproduced |
| fig4b-error-vs-matched | reproduced (assumed) |
| fig5-similarity-predicts-errors | not reproduced |
| figs5-euclidean-distance | reproduced (assumed) |

Totals: 11 reproduced, 4 partially reproduced, 6 not reproduced, 8 blocked.

## 2. Dataset

**What it holds.** 24 of the paper's 27 participants and the OFC only, in native space with no voxel coordinates. There is no training session, no whole-brain data, no other regions, no cardiac regressors and no response side or response mapping. The zip's MD5 matches `checksums.md5`, and all 119 time series are distinct.

**Version.** CRCNS data sets are unversioned, so the record says `unversioned` with the DOI 10.6080/K0FN14CH. The bucket holds one copy under `live/` (data descriptor v0.6), and the notebook header records the zip's MD5 for change detection.

**Main finding.** Each `err` event is a block that covers the error trial, its repetitions and often the trials after it. The data descriptor does not say so. As a result:
- The number of errors cannot be recovered; one per block is a lower bound.
- Time-outs and the reaction time of error trials cannot be recovered either.
- An error trial's state can be reconstructed only for Enter errors: 39 under a strict rule, 98 under a span-based rule.
- Errors after an Exit trial make up 181 of 225 blocks. The paper reports 3.4%, 2.3% and 1.4% for Enter, Exit and Internal.

**Other findings.**
- The `err` column of the design matrices tracks a short event at each block onset (r 0.83 to 0.98), not the onset-to-button-press boxcar the descriptor describes.
- In Subj-01 run 4, two adjacent labelled trials break the task rules.
- Three runs have no `first` trial; the descriptor does not mention this.
- The paper contradicts itself on which trial is repeated after an error (Figure 1B legend against the Methods).
- The data's timing check is only consistent with events and scans sharing a clock, to within about two TRs.

**Assumptions.**
- Beta maps are z-scored per voxel across the state maps of each run. This is what the Princeton MVPA toolbox's `zscore_runs` does, and the paper names that toolbox. The per-map reading is shown throughout.
- Error-trial states use the span reading of the error blocks.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- In which direction were the beta maps z-scored, and with what smoothing kernel?
- How were errors counted, and how was each error trial's state labelled?

**Questions to a reader:** none.

## 3. Protocol gaps
1. When a criterion has no clause for partial reproduction, the protocol does not say whether "the effect holds only in part" may still be called partially reproduced. I followed the criterion strictly and recorded not reproduced (two-back state space, fig2d).
2. The data-check step assumes trial tables carry correct labels. Here the error events are merged blocks, and nothing in the protocol covers reconstructing labels. I made reconstruction a helper rule with two readings and marked the outcomes that rest on it as assumed.
3. Reading 2 of the clock check (decoding with labels shifted in time) is written for spike data. For fMRI I shifted the regressors and swept the volume lag. It can only show the clocks are consistent within about two TRs, and I reported it that way.
4. The protocol is silent when a mixed model does not converge or is singular. I fell back to a random-intercept model, marked it in the output, and left out one fit that was singular.
5. The archive notes give no way to check the version beyond the zip's MD5. To confirm it, I streamed the whole zip and computed the MD5.

## 4. Runtime and failures
- Session: 18:44 to 20:10 UTC. Notebook: about 5.5 min.
- Two runs failed on statsmodels mixed-model errors (a missing attribute, then a singular matrix). Both are fixed, and the final two runs gave identical outputs.
- Nothing else failed. The untracked files in the repository root (`.bashrc`, `scripts` and similar) are sandbox device mounts; I did not create them.
