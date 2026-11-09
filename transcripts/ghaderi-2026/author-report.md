I finished steps 1 to 5 and ran the handover. All three notebooks pass `python tools/entry.py all` (0 check errors) and the verifier's package is in `executed/001530-ghaderi-2026/handover/`. Nothing is committed.

**1. Outcome per claim** (dataset version 0.260605.0601, the only published version)

| Claim | Outcome |
|---|---|
| fig1c-lick-probabilities | reproduced |
| fig1f-movement-latencies | partially reproduced (lick latency 330 ms matches; movement latencies too short) |
| quiet-trials-half | partially reproduced (55.06% rejected; tolerance is 45 to 55%) |
| fig2-auditory-window, fig2-delay-window, fig2-whisker-window | reproduced (every value and every significance) |
| fig2-wm2-vs-alm-auditory | reproduced |
| fig2-other-trial-types | not reproduced (18 of 72 changes significant; allowed 7) |
| units-recorded | reproduced (exactly 10,294 units and the per-area counts) |
| fig3a-activity-maps, fig6b, fig6c, fig7b, fig7c, fig5b-decoding-time-course | reproduced |
| fig3b, fig3c, fig3d, fig5a, fig6a, fig8a, fig5b-context-decoding-delay | partially reproduced |
| cluster-label-link (link claim I added) | reproduced (10,294 of 10,294 neurons match) |
| fig4-29-clusters | not reproduced (lowest BIC at k = 44; only 5 GMM initialisations per k) |
| fig4b-named-clusters, fig5c-cluster-removal, fig7d-context-decoding-after-whisker | blocked, methods underspecified (the two readings give different outcomes) |
| fig5d-null-space-decoding | blocked, not runnable (needs a MATLAB toolbox) |
| fig8b-lick-coding-direction, figs18-later-lick-coding | blocked, other (not tested within the run's time) |

**2. What was found about the dataset**
- **Quiet-trial rule:** the Methods say the quiet-trial rule uses the median absolute deviation; the paper's code uses the mean absolute deviation. With the code's rule, Fig. 3c, 3d, 5a and 6a come out at the paper's values; with the Methods' rule, which the claims file requires, they are lower. That gap is why those claims are only partially reproduced. Recorded as `code_mismatch`.
- **Areas need an outside file:** units can only be assigned to the five areas with `Area_list.mat` from the Zenodo record. With it the unit counts match exactly; without it there are 12,066 units.
- **Metadata errors:**
  - 12 optogenetic sessions (mice PG021, PG061) list genotype C57BL/6JRj but are inactivated like the VGAT-ChR2 sessions.
  - `spike_width` is described in ms but holds seconds.
  - Several trial-table column descriptions do not match their contents.
- **Trial and session oddities:** 11 trials have `trial_type` 0; one session has no No-tone trials; 272 trials in two sessions have no video; one session keeps no unit after the CCF filter.
- **Paper inconsistencies:** the Fig. 2 legend says SD and 1,000 iterations, but the spreads are SEM and the p-values need 10,000 iterations. The Methods say 34 sessions where the paper elsewhere says 35, and 8 mice for ALM inactivation where the dataset has 7.
- **Assumptions:** none adopted. Where the claims file gave two readings and they disagreed, I followed its own rule and blocked the claim.
- **Questions for the paper's authors** (recorded as `methods_unavailable`):
  - What does "mostly" mean for cluster 1? It is 30.5% A1: the largest share, but not more than half.
  - Which SVM and which C grid were used? The Methods describe a grid search with no grid; the code uses nu-SVC with no search.
- **Question to a reader** (`questions/001530.yaml`): for fig1f, the criterion takes the maximum over 1.0 to 1.2 s, which cannot produce the reported 231 ms tongue latency.

**3. Where the protocol was unclear, wrong or missing something**
1. The Methods-first rule makes some claims partial even when the code's rule reproduces the paper's numbers, and nothing lets the author adopt that rule. I kept the claims file's rule and recorded a finding.
2. The fig3d criterion's partial case does not fit the result (the test holds but one value is low). I recorded it as partial and said why.
3. Some claims files say "block when readings differ", while protocol step 1.6 allows adopting the best-supported reading. I followed the claims file.
4. Running both SVM readings at full size would take about 37 min for the code's decoder (main delay claim alone) and about 30 h for the grid search. The protocol has no rule for running fewer repetitions. I ran fewer and recorded each as a deviation with the full-run estimate.
5. The protocol has no clear block reason for a claim left untested because the run's time ran out rather than because the computation was too large (fig8b needs an 18-minute download). I used `other` and explained it.
6. Adding a link claim meant adding it to the `depends_on` of fig4b and fig5c. The protocol does not say whether the author may edit that field; I did.
7. `Area_list.mat` is a label mapping used by every unit claim, but those claims are marked `data: dataset` and I cannot change that field. I listed it under `inputs` and as a finding.
8. `archives.md` could note that a HEAD request on DANDI's download redirect returns 403 in this environment; I used the asset metadata's `contentUrl` instead.

**4. Runtime and failures**
- The work took about 2 h 35 min (23:44 to about 02:19 UTC).
- Notebook run times: 5.5 min, 14.5 min and 21.5 min.
- The first full run failed in the two decoding notebooks because one session has no analysed units. I fixed that and both later runs passed with identical numbers.
