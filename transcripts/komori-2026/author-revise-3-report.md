The verifier agreed with the one change I proposed, so one outcome changed and no proposals are left open. `entry.py all` passes (0 check errors, both notebooks run), and nothing is committed.

**Outcome changed**
- `rest-ic-count-and-window`: partially_reproduced → not_reproduced. `proposed` is removed, and the notes, both notebooks' conclusions and summaries, and the README now say not reproduced.
- Round 3 is recorded under `verifications` with this claim's result: agreed, not_reproduced, the verifier's reason and caveats in its own words, and my response.
- `questions/komori-2026.yaml` now notes that the round-3 verifier raised the epoch-selection (R5) point again.

**Proposals still standing:** none.

**Two things came up during the run that you should know about:**
- **Crash on this runner, and a helper change.** The first run died: numpy's OpenBLAS, pinned to Haswell kernels, segfaults on this runner's AMD Zen 5 processor. I added a fixed `OPENBLAS_L2_SIZE` to the kernel pins in `pupilwf.py`. Any size I tried (0.5, 1 and 2 MiB) gives the same bits. The verifier has not seen this helper change.
- **Some numbers moved.** The decomposition and every number the verifier quoted for the IC count are unchanged, but some GRU fits differ from the round-2 run. No outcome changes, and I updated the texts and record to this run:
  - **This claim:** under R5 (a), 10 s now has the highest window median (0.6403), not 0.5 s. 1.5 s is still never highest. Your verifier's reason, recorded as given, still says 0.5 s; my response notes the change.
  - **rest-needs-0-1-hz:** at 0.1 Hz under R5 (a), 0.661 against 0.629, p = 0.085 (was 0.660 against 0.642, p = 0.425). I also changed its `measured` value from 0.66 to 0.661.
  - **rest-decoding-above-null:** its seed and one-at-a-time p ranges, and the highest mean AUC (now 0.722).
  - **rest-loss-accuracy-vs-null:** its seed p ranges.
  - **SHAP:** an extra MOs window now differs from null, with the model lower.
  - **Third ICA restart:** no longer below null (p = 0.144).
  - The sentence saying the run gives the same numbers on any machine is corrected in both notebook summaries, the README and the record.

A second full run on this machine gave identical outputs, and the workflow's re-run on another processor may give other fits again. I left the untracked dotfiles at the repo root and the existing `tools/` changes alone.
