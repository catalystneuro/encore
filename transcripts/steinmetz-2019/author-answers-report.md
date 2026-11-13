I re-ran the claims the two answers affected, and the entry passes `entry.py check` and `entry.py all` (notebook 985 s, peak memory 2.1 GB). The handover is built in `executed/steinmetz-2019/handover/`. Two outcomes changed from the first run: edtable1-region-counts and fig4d-jpecc-vis-leads are now reproduced. I did not verify my own work, commit or push.

## Question 1: edtable1-region-counts (also changes supptable2-sessions)

**What the answer changed.** The reader agreed the claims file had misread Extended Data Table 1. The table counts every neuron of the 42 regions (curated, trial rate at least 0.1 Hz), not definition N. Recordings now have two readings: (a) sessions with any neuron of the region, and (b) sessions with at least 13. Definition N, which the first run tested, is now a variant. supptable2-sessions now takes its area lists from the same neurons and readings.

| Claim | Earlier | Now |
|---|---|---|
| edtable1-region-counts | not reproduced (26 of 42 regions matched with neurons N) | reproduced |
| supptable2-sessions | reproduced, resting on an assumption | unchanged: reproduced, resting on an assumption |

- **edtable1-region-counts:** under reading a, recordings, mice and neuron counts all match in 38 of 42 regions, the number the criterion needs.
  - Recordings are exact in 41 regions, mice in 42, and neuron counts within 10% in 38.
  - The regions that differ are ACA, MOs, VPL and ZI. MOs has 18 recordings against 19, and 1,352 neurons against 1,534.
  - Totals are 22,434 neurons and 13,532 active, against 22,458 and 13,467 in the table.
  - Reading b and definition N each match in only 26 regions.
- **supptable2-sessions:** the area lists match in 38 of 39 sessions under reading a (Muller 2017-01-08 lacks MOs) and 24 under reading b. The first run had already used the reading a neurons as its main test, so I only added reading b. The match still depends on mapping the finer region labels to their parent regions.

## Question 2: fig4d-jpecc-vis-leads (also changes fig4d-jpecc-no-lag-frontal-midbrain)

**What the answer changed.** The criterion now uses one PCA per region group across time points and trials, as the Methods say. The per-time-bin PCA of the paper's code (jPECC.m), which the first run used, is now a variant. The first run had tried the Methods' PCA on only one reading. It is now run under every reading. I made it the helper's default, and each window and alignment gets its own PCA fit.

| Claim | Earlier | Now |
|---|---|---|
| fig4d-jpecc-vis-leads | partially reproduced | reproduced |
| fig4d-jpecc-no-lag-frontal-midbrain | not reproduced | unchanged: not reproduced |

- **fig4d-jpecc-vis-leads:** VIS leads Frontal in every reading (17 recordings):
  - Before movement (-0.2 to -0.05 s), 3 to 5 of 16 time points are positive at p < 0.05.
  - From 0.08 to 0.12 s after the stimulus, 3 points are.

  VIS leads Midbrain (11 recordings) only under the reading that uses Left and Right choice trials, at one point, 0.08 s. That point has p = 0.003 with the longer baseline window (-0.2 to 0 s) and p = 0.025 with the shorter one (-0.1 to 0 s). The criterion asks for one reading, so the claim is reproduced, but it rests on a single time point at the edge of the window. I added a check with five other random fold seeds: the point stays significant in 5 of 5 with the longer baseline and 3 of 5 with the shorter. With the per-bin PCA, still no VIS-Midbrain point is significant.
- **fig4d-jpecc-no-lag-frontal-midbrain:** the uncorrected test still finds 1 significant point of 26 under each baseline, at -0.12 s with Midbrain leading (p = 0.028 and 0.017, 9 recordings). No point survives Bonferroni correction.

## Other changes and a fix
- I updated the notebook's method text, conclusions and summary, the README outcome table, and the attempt record. Each affected claim's notes say what the answer changed.
- The notebook now takes 17 minutes, up from 13, because every jPECC reading is computed with both PCAs; `runtime_minutes` is updated.
- `entry.py lock` wrote a `python: "3.13"` field into `entry.yaml` that the entry schema rejects. That came from the uncommitted `tools/entry.py` already in the working tree. I deleted the line, since the tool falls back to the lock file's Python version, and `check` then passed.
