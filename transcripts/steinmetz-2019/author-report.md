I've finished steps 1 to 5 and built the handover (step 6). The notebook ran from a clean environment in 12.7 min with 2.08 GB peak memory and passes `tools/entry.py check`. I did not commit, and I did not verify my own work.

**Dataset version.** I pinned 0.240329.1926, the only published version. The paper cites no DANDI version, and the draft has the same 39 files and size.

### 1. Outcomes (40 claims)

| Claim | Outcome |
|---|---|
| fig1c-easy, fig1c-low-contrast, fig1c-competing | reproduced (easy: 1.71% incorrect and 10.12% Misses on engaged trials) |
| fig1d-reaction-time-difficulty | reproduced (on the trials of definition T only) |
| ed1q-wheel-choice-decoding | reproduced (48.9% before onset, 94.8% after) |
| early-response-fraction | reproduced |
| passive-no-movement | not reproduced (84.6% against 94.1 ± 0.6) |
| recording-counts | reproduced (29,283 neurons; 9,538 trials, the paper's count exactly) |
| edtable1-region-counts | not reproduced (26 of 42 regions match; 38 of 42 without the 13-neurons-per-session rule) |
| supptable2-sessions | reproduced, resting on an assumption (region-label mapping) |
| task-modulated-fraction | reproduced (13,439 neurons, 60.3% active; 75% increase, 21% decrease) |
| suppfig2-rate-amplitude | partially reproduced |
| fig2de-activity-order | reproduced |
| fig2fg-miss-restricted | partially reproduced |
| fig5b-miss-more-than-passive | partially reproduced (36 sessions kept, not 34) |
| fig5c, ed6b, fig5d, ed7f (r = 0.515) | reproduced |
| fig5f (7.85 a.u., p = 1e-5), fig5e, ed9i, ed9cf, ed9k, suppfig3 | reproduced |
| ed7b-detect-probability-widespread | reproduced |
| fig4d-jpecc-vis-leads | partially reproduced (VIS leads Frontal; it does not lead Midbrain) |
| fig4d-jpecc-no-lag-frontal-midbrain | not reproduced (1 to 2 uncorrected significant points; none after Bonferroni) |
| 11 kernel-regression claims (fig3c, fig3d, fig3e, ed4f, ed5h, fig4b, fig4c, fig4f, fig4fg, ed5g, ed7c) | blocked, `too_large`: timed at 7.0 h on one core, 1.8 h on 4 |
| histology-alignment-error | blocked, `data_missing` |

### 2. Dataset, assumptions and questions

**Findings about the dataset:**
- The `rate` attribute of the wheel, lick and face-motion series holds the sampling interval (0.0004 s), not a rate.
- `peak_channel` is 1-based. This is undocumented, and each unit's region depends on it.
- `wheel_moves` has half as many data values as timestamps (format error).
- 2,262 units carry finer Allen labels (SCig, LSr, …) that have to be mapped to the paper's 42 regions.
- Genotypes are named differently from the paper's Supplementary Table 1.
- The dandiset does not say which 5 sessions had unusable pupil video.
- There is no histology.
- There are no duplicate recordings.
- The clock check (decoding the stimulus from spikes before and after onset) could not be established for one session, Tatum_2017-12-09.

**Assumptions:**
- Finer region labels are mapped to their parent region. Only supptable2's outcome rests on this.
- A z-score with zero baseline variance is run both counted as significant and left out (fig2fg, fig5b).

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How were neurons with no baseline spikes (infinite z) treated?
- Which "fewer than 10 trials" count gives 34 sessions?
- What counts as movement in the passive replay?

**Questions to a reader** (in `questions/steinmetz-2019.yaml`):
- Extended Data Table 1 seems to count every neuron of the 42 regions, not definition N. This would change edtable1 to reproduced.
- The jPECC criterion does the PCA per time bin, as the code does, but the Methods do it across time points and trials. I ran both; the outcomes are the same.

### 3. Protocol problems
1. `tools/entry.py lock` writes a `python:` field into `entry.yaml` that the entry schema rejects. I deleted the line by hand after locking.
2. For a claim of absence the protocol says to judge on the paper's test alone, but the jPECC baseline window is still open. I ran both baselines; both find a significant point, so I called it not reproduced.
3. The protocol does not say whether an expected value outside tolerance overrides a criterion that does not mention it (fig5f: 36 sessions against 34). I followed the criterion and recorded the difference.
4. Several criteria have no "partially reproduced" clause (fig2fg, suppfig2, fig4d-vis-leads). I used the protocol's own definition of partial.
5. The rule that a claim depending on a blocked claim is blocked forces ed7c out entirely, although its choice-probability part could be run.
6. A `too_large` block needs a timing from the notebook, so I put a timed fit of one neuron in the notebook. The estimate also relies on the claims file's figure of about 4,240 neurons entering the nested test.
7. The claims file follows the code where the Methods differ (jPECC PCA), against the reader rule that the Methods come first. I asked a reader.
8. The asymmetry-slice wording in the claims file is ambiguous. I took the Methods' diagonal slice and cited it.

### 4. Runtime and failures
- The run took about 1 h 40 min of the 5 h allowed, so no claim was blocked for time.
- The notebook ran twice in full: 739 s, then 773 s for the final run.
- Nothing failed apart from the lock/schema mismatch above.
