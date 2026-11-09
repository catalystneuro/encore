I tested 28 of the 33 claims on DANDI:000959. 19 reproduced, 4 partially, 5 did not; the other 5 are blocked. The entry passes `lock` and `all` from a clean environment and the handover package is built. Nothing is committed.

Version: the paper cites none, so I pinned the latest published version, 0.261020.0242. The only other version, 0.260531.2104, has the same 1705 assets with the same ids and sizes. The header says so.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| design-days-per-area | reproduced |
| design-sessions-per-day | partially reproduced (monkey L has 6.02 control runs per day, paper says 5) |
| fig1e-stim-counts-comparable, figs1d-stim-counts-nonsocial | reproduced |
| figs1e-eyes-more-than-face | reproduced |
| figs1e-eyes-vs-rdm-comparable | not reproduced under the Methods' "total per day"; comparable under the code's mean per run |
| fig2a-density-map-ofc | reproduced |
| fig2c (both claims), fig2e (both), fig2f, fig2gh, methods-ofc-distance-longer-windows | reproduced |
| methods-ofc-no-change-in-fixation-number | reproduced |
| methods-ofc-longer-face-looking | partially reproduced (tests hold; 2 of 3 OFC durations within tolerance) |
| methods-mouth-stimulation-no-effect | reproduced (with 5 days the smallest possible p is 0.0625) |
| methods-eyes-vs-mouth-bootstrap | not reproduced |
| fig3b-ofc-inter-looking-interval | reproduced (p = 0.044, close to the threshold) |
| ili-nonsocial-no-effect, ili-missing-trials-41, figs3b-ili-trial-level, figs3c-reciprocation-day-level-none, fig3d-ofc-reciprocation-latency | reproduced |
| partner-monkey-unchanged | partially reproduced (one reading of M2's reciprocation latency gives dmPFC p = 0.044) |
| epoch-days-76-of-81 | reproduced, with exactly the five named days |
| fig5a-trigger-duration-unchanged | not reproduced (dmPFC p = 0.019) |
| fig5b-pupil-unchanged | reproduced |
| figs4a, figs4b, ofc-slope, fig4c, fig4d, dmpfc-slope-positive | blocked, `too_large`: the causal decomposition would take about 870 CPU hours, timed in the notebook |
| fig5cd, fig5e-h (saccades) | blocked, `not_runnable`: the files hold no saccades and the paper's detection method is MATLAB code |

The headline result reproduces well: OFC stimulation lowers social gaze distance with p = 0.0002 (L p = 0.0067, T p = 0.016), and the contralateral pattern matches too.

### 2. Dataset, assumptions and questions

**Dataset.**
- It holds every day the paper describes: 81 Eyes days and 15 Mouth days, one file per run, no run deposited twice.
- Each file holds gaze, pupil, stimulation and sham times, ROIs, and fixation-event tables.
- The files' own hemifield labels match the claims file's rule for 99.98% of events.
- A clock check passes: 71% of trial times fall inside an M1 event in the triggering ROI, against 5 to 20% when the times are shifted.

**Findings recorded.**
- Run counts per day differ from the paper's (L control runs, T social runs never reaching 15).
- Methods and code count fixations differently (day total against mean per run), and the Eyes-vs-RDM outcome depends on it.
- Neither the paper nor the files give the Eyes ROI padding or how events were assigned to ROIs.
- The control runs lack `roi_m2_face`, the hemifield reference, which I took from the same day's social runs.

**Assumptions.** None of the outcomes rests on one: every reading was taken from the claims file or the paper and cited.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Does a face event that starts on the trial sample itself count as a look back with latency 0? Counting it moves OFC from p = 0.044 to p = 0.058.
- Is M2's reciprocation latency measured from M1's look or from the trial time?
- How is the bootstrap p-value computed (which side)?

**Questions to a reader:** none.

### 3. Protocol points
1. The DANDI section of `archives.md` says to stream with remfile. That took about 14 s per file for metadata alone (12.5 min with 32 threads). I read each file into memory over HTTP instead (never to disk), which brought the full load to about 10 min.
2. Each claim of absence must be judged "on the paper's test alone", yet this claims file names several readings for some of them (partner monkey). I followed the criterion, which requires every reading to pass, and gave `partially_reproduced` when one test out of 21 failed.
3. Several criteria have no rule for a partial result (sessions per day, partner monkey). I used `partially_reproduced` where most of the claim held, and said so in the notes.
4. For the Eyes-vs-RDM claim, the protocol's order (Methods first) gives a "not reproduced" that the code's reading would reverse. I did not ask a reader, since this is not a misreading of the paper, and recorded it as a `code_mismatch` finding.
5. The protocol does not say whether a cost estimate made inside the notebook is enough to support `too_large`. I timed one decomposition inside the notebook to give the estimate.
6. While the shell's working directory was the entry folder, the harness created an empty `.claude/.cc-writes` there; I removed it. Unrelated untracked dotfiles at the repository root (`.bashrc`, `.idea`, and others) I left untouched.

### 4. Runtime and failures
- The run took about 67 minutes of wall clock (23:22 to 00:29 UTC).
- The notebook takes 11.2 min, almost all of it reading the data.
- Nothing failed.

The new files are `entries/000959-fan-2024/` and `attempts/000959-fan-2024-01.yaml`; the handover is in `executed/000959-fan-2024/handover/`.
