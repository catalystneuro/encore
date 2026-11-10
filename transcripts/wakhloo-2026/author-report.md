I finished steps 1 to 6 of the Author section. The entry passes `python tools/entry.py all` (0 errors; the notebook ran in 1958 s from a clean environment), and the handover is built in `executed/wakhloo-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig7d-behavioral-error-learning | reproduced (error 0.668 at session 1, 0.157 at session 4, 0.180 at session 8) |
| fig7e-readout-error-learning | reproduced (both areas, both readings) |
| figs12c-behavior-readout-r2 | reproduced (R2 0.493 in CA1, 0.508 in PFC) |
| fig7f-theory-vs-empirical | not reproduced (r is 0.98 and 0.95, but the differences are 11.6% and 10.7% against the criterion's 10% bound; question asked) |
| fig7g-total-dimension-drops-early | reproduced |
| fig7h-task-dimension-increases | reproduced (reading a) |
| fig7hk-measures-increase-early | reproduced (PFC 4 of 4 measures, CA1 3 of 4) |
| fig7-late-reversal | reproduced |
| mixed-quadratic-dim-corr-snf | reproduced (all 12 P values below 1e-5) |
| mixed-quadratic-ssf-not-nonmonotonic | reproduced (P 0.366 and 0.313) |
| mixed-quadratic-task-dim | reproduced |
| mixed-linear-ssf-task-dim | partially reproduced (CA1 SSF P = 0.00106 against 1e-3; the code's 19 CA1 units give 0.00065) |
| late-trends-match-optimal | partially reproduced (PFC only; the CA1 task dimension falls after session 4) |
| glm-cross-validated-d2 | partially reproduced (3 of 4 values match; the PFC spread across rats is 0.060 against 0.022) |
| svc-hebbian-correlation | reproduced (PFC and CA1 part; r2 0.926 and 0.832) |
| 5 theory claims, 2 MLP claims | blocked, `other` (no recorded data) |
| 2 pose-network claims | blocked, `not_runnable` (needs a DeepLabCut network trained in Python 3.8) |
| 3 macaque claims | blocked, `other` (Brain-Score data are public; not attempted in this run's time) |

## 2. Dataset, assumptions, questions

- **What is there:** I pinned 0.240511.0307, the version the paper cites and also the latest; all three published versions have the same 9 assets and size. All 8 rats with 8 sessions each are there, with units, areas, trials and position. The fewest units kept in a session are exactly the Methods' 19 PFC and 24 CA1.
- **Clock check:** position decoded from CA1 spikes beats the 10 s and 60 s shifts in 64 of 64 sessions. 98.6% of trials end nearest their end well, against 51.7% with the end times moved 15 s earlier.
- **Duplicates:** no spike train or position trace is repeated across files.
- **Match with the paper's code:** the per-session measures agree with the paper's own results files to a median of 0.1% to 0.7%, and the behavioural errors are identical.
- **Findings recorded:**
  - The two ZT2 files both have `session_id` "01", and nothing says how they join.
  - Position is sampled at 27 to 33 fps, where the paper says 30.
  - JS15's timestamps span about 24 h.
  - The code uses 19 CA1 units where the Methods say 24.
  - The paper gives R2 0.48 in the Results and 0.49 in the legend.
  - The SVC comparison notebook reads a results file that is not in the repository.
- **Assumptions:** none (no outcome is marked `assumed`). Every open method detail came from the code, as the claims file cites it.
- **Question for the authors** (a `methods_unavailable` finding): how was the PFC D2 spread of 0.022 computed? Every reading gives 0.057 to 0.066.
- **Question for a reader** (`questions/wakhloo-2026.yaml`, fig7f): the 10% bound fails on the paper's own PFC results file too (11.55%). Does it misread the legend's "good agreement … small bias for low error values"?

## 3. Where the protocol was unclear

1. Blocked theory and simulation claims fit no `blocked_by` value. I used `other` and said why in the notes.
2. It does not say which reason to use for `elsewhere` claims left untested by choice, with time left (macaque). I used `other`, not `too_large`, and said so.
3. Paper results files as a comparison (not a link claim): I listed them under `inputs` as comparison only, and no outcome depends on them.
4. Editing conclusion markdown after the run: I filled in the conclusions after the clean run and copied those markdown cells into the executed copy (the code cells are identical). The handover strips them anyway.
5. Running a costly method in full: the SVC on all 500 subsets would take about 25 h, so I ran it on 4 subsets per session and recorded that as a deviation. I did not repeat the GLM basis grid search (108 settings at about 27 min each); I used the basis the code chose, as the claims file does.

## 4. Runtime and failures

- The notebook takes about 33 min on 4 cores and peaks at 0.59 GB of memory. The run ended at 07:43 UTC.
- About an hour was lost early, when a grep over the paper's one-line text hung until it timed out at 60 min.
- On the first full run the clock-check cell failed (a string bug); it is fixed, and the clean run had no errors.
- The checkout has stray untracked files I did not create (dotfiles at the root, `entries/wakhloo-2026/.claude/.cc-writes`, which look like sandbox artefacts), and I left them alone. Leave them out of the commit.
