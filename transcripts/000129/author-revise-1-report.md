No outcome changed in this revision. Both notebooks were re-run from a clean environment with `tools/entry.py all`: 0 check errors, and both passed (662 s and 1295 s). Every conclusion matches the new numbers. Nothing is committed.

**Outcomes**
- **Unchanged outcomes:** every one. The numbers on this machine are the same as in the first author run: two fits with the same seed gave identical results. The copy the verifier reviewed came from an earlier run, and its numbers differ in the second decimal (for example a KFobs ratio of 1.97 against 1.92 here).
- **Reasons for blocking:**
  - The 12 claims that need the paper's other sessions are now `data_missing` instead of `too_large`, as the verifier gave.
  - `fig4-task-similar` is now `other`. It is marked as using data from elsewhere, and `entry.py check` does not allow `data_missing` there; the real block is that monkey C's data have no archive identifier.
- **Kept against the verifier, with the disagreement recorded:**
  - `fig2-sagittal-better` stays partially reproduced. This run gives 23 of 24 pairs; the verifier's copy gave 24.
  - `fig4-vel-acc-every-session` stays reproduced. The claims file names its per-session part as the part one session can test.

**Fixes and added output**
- **EM stopping rule (problem 1):** the threshold was 1e-6 and is now the paper's 1e-4. Every EM run still reached the 100-epoch limit, with last-epoch gains of 4.3e-4 to 9.4e-4 (now printed), so no result changed.
- **Wiener filter (problem 7):** the first test bins now take their history from the last training bins instead of zeros. Its SNR moved by at most 0.01 dB.
- **Single-session values for the blocked claims:** each now has a tagged section printing its point values, including:
  - At 16 ms the Wiener filter beats the rEFH (+KF) for velocity and acceleration.
  - At f = 1/4 the rEFH (+KF) ties the Wiener filter for velocity.
  - The intro gains are outside tolerance under both readings.
- **Other output the verifier asked for:**
  - Two more seeds for the KFlatent EM initialization. `kflatent-modest` holds in all three runs, by 0.07 to 0.10 dB.
  - Training and test R2 of the static rEFH map. For x and y position it is 0.39 and 0.51 on training bins against 0.19 and 0.37 on test bins.
  - R2 tables for every configuration, and a list of all negative R2 values outside 64 ms.
- **Questions for a reader**, in the new `questions/000129.yaml`:
  - Should `fig2-gross-failures` cover every configuration the paper ran? Under that reading it would fail.
  - Should the claims that need the paper's sessions use its Zenodo deposit (doi:10.5281/zenodo.583331) instead of the dandiset?
- **Record and README:** the attempt record has a round-1 `verifications` block for all 31 claims, and its notes are updated. The README's blocked rows are updated.

**Not done**
- **Tapped decoders for `fig9-taps`:** not implemented. Every grade of its criterion needs the bootstrap across sessions, so the claim stays blocked whatever parts (i) and (iii) show. The tapped UKF would also be a second re-implementation of Li's UKF2, whose code is not in the paper's repository. The record says this.
- **Line references into the paper's code:** the verifier asked for these and I did not add them.

Untracked dotfiles at the repository root (`.bashrc`, `.gitconfig`, `.vscode` and others) and the changes under `tools/` were there before this run. I left them alone, and they should not be committed.
