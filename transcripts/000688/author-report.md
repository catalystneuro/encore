I tested 5 of the 28 claims and blocked the other 23, because the dandiset holds only the Baseline epoch of each session. The entry is `entries/000688-perich-2018/`, the record is `attempts/000688-perich-2018-01.yaml`, and the verifier's package is in `executed/000688-perich-2018/handover/`. `entry.py check` reports 0 errors, the notebook runs in 8.8 to 9 min from a clean environment, and nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-neuron-counts | partially reproduced (assumed) |
| fig3b-pmd-higher-dimensional | reproduced (assumed) |
| figs4d-dimensionality-robust-to-size | reproduced (assumed) |
| figs4c-null-potent-index-centered | reproduced (assumed) |
| fig6c-null-leads-potent | partially reproduced (assumed; Baseline part only) |
| the other 23 claims (behavior, covariance across epochs, all GLM claims, Washout, Mahalanobis distance, VR, cf-vr-dissociation) | blocked, `data_missing` |

## 2. Dataset, assumptions and questions

**What the dataset holds.** I pinned version 0.250122.1735: the paper cites no version and this is the only published one.
- **Baseline only.** The dual-array center-out sessions of Monkey C (2016-09/10, 14 sessions) and Monkey M (2014-02/03, 7 sessions) have unit counts that match the paper's ranges. Each holds only 155 to 286 reward trials, with steady reach errors and no perturbation block. A whole curl field session in the paper has at least 524 reward trials.
- **Missing labels.** No file has an epoch or perturbation column, and nothing says which sessions are the paper's 16.
- **Cursor and target metadata.** In seven Monkey C sessions the cursor ends reaches at about 4.2 cm while the targets are stored at 8 cm. In several sessions the cursor never enters the stored target square. Two sessions have thousands of repeated cursor timestamps.
- **Unit counts.** Units above 5 Hz are far fewer than the paper reports: at most 634 M1 and 1224 PMd, against 918 and 2221.
- **Empty field.** The session description is empty in all 111 files.

**Assumptions.**
- **Sessions.** I used all 21 candidate sessions, plus the 19 whose reward counts fall in the paper's Baseline range as a second set. For the neuron counts, the per-session ranges hold only if C 2016-09-29 (114 PMd units) is not one of the paper's sessions.
- **Target acquisition.** I took it as the trial's stop time minus the 0.5 s target hold from the Methods, because the cursor data cannot be used for it.
- **Noise scale in the dimensionality estimate.** I scaled the noise to that of a trial average. Taken as the text describes it, the noise exceeds every component and gives 0 dimensions.
- **Null/potent index.** I read "magnitude" as the sum of absolute values. With sums of squares, one reading of eight gives a mean of 0.100, just over the 0.1 bound.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How was the noise scaled in the dimensionality estimate?
- Is the 100 ms kernel width a standard deviation or a full width at half maximum? The Baseline lag is significantly negative under the first reading only.

I asked no reader any question.

## 3. Where the protocol was unclear or did not fit

1. **Session identity.** Step 1.2 has no rule for a dataset whose sessions cannot be matched to the paper's. I ran two session sets and, for the neuron counts, counted how many choices of 9 Monkey C sessions satisfy the claim. I marked those outcomes `assumed`.
2. **Partly testable claims.** The protocol does not say what to do when part of a claim's criterion cannot be tested (the end-of-Force lag in fig6c). I judged the Baseline part with the criterion's own partial rule and said in the notes that the Force part is untestable.
3. **Readings that are impossible.** Step 1.6 does not cover a reading the data show cannot be the paper's procedure (the raw noise scale gives 0 dimensions). I ruled those readings out on that basis, kept them in the notebook, and adopted the remaining one as an assumption.
4. **Many readings against the time limit.** "Run every reading" multiplies quickly with many open details. For Figure S4D I used 25 subsamples per size, 100 noise repetitions and only one kernel, and recorded these as deviations.
5. **Where to block for missing epochs.** The protocol does not say whether missing epochs belong at the dataset level or per claim. I blocked each claim with `data_missing` and also recorded one dataset-level finding.

## 4. Runtime and failures

The work took about 1 h 20 min (11:44 to 13:04 UTC); all steps up to the handover are done.
- A first full run took 19.5 min. I vectorised the noise repetitions and ran sessions in threads, which brought it to about 9 min.
- Detecting target acquisition from the cursor failed in many sessions, which is why I switched to the stop-time-minus-hold reading.
- Untracked files I did not create appeared in the repository root (.bashrc, .profile, .idea, .vscode, scripts and similar); I left them untouched, so make sure the workflow does not commit them.
