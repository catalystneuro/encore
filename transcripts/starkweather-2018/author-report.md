All five author steps are done and the handover is built: 20 claims reproduced, 12 blocked because the data aren't in vta-1. The entry passed `tools/entry.py all` with 0 check errors, and the clean run finished in 159 s. Nothing is committed. I wrote `attempts/starkweather-2018-01.yaml`, the entry in `entries/starkweather-2018/`, and `executed/starkweather-2018/handover/`. I asked no reader questions.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig4a-task1-saline-post-decrease | reproduced (F=12.61, p=8.4e-16; paper 12.6, 9.1e-16) |
| fig4b-task2-saline-post-increase | reproduced (F=3.70, p=3.8e-4; same as the paper) |
| fig4b-odorc-below-latest-odora | reproduced |
| fig4ab-saline-pre-decrease | reproduced |
| fig4c-task1-salb-post-decrease | reproduced |
| fig4d-task2-salb-flat | reproduced (F=0.70, p=0.69) |
| fig4cd-salb-pre-decrease | reproduced |
| fig5f-task2-slope-signs | reproduced (29/12/24, the paper's counts exactly) |
| fig5e-task1-significant-slopes-unchanged | reproduced, rests on an assumption |
| fig5f-task2-significant-slopes-shift | reproduced, rests on an assumption (Fisher p=0.0405; paper 0.041) |
| fig4e, fig5e slope distributions; fig5f, fig5e slope variances | reproduced (4 claims) |
| fig6ab-odorc-above-odorb, fig6cd-omission-dips-intact, figs5d-omission-unchanged-by-salb | reproduced |
| fig7cd, fig7fgh, fig7ijk (the model) | reproduced, using a line-by-line Python port of the paper's code |
| fig2, figs1e, figs6ce (mPFC units) | blocked, data_missing |
| fig3g, figs3 ×2 (licks) | blocked, data_missing |
| figs4 (unidentified VTA neurons) | blocked, data_missing |
| figs5b, figs5c, anova-slopes, anova-time-task-drug (free water) | blocked, data_missing |
| figs6-salb-without-kord (no-KORD control neurons) | blocked, data_missing |

## 2. Dataset, assumptions, questions

- **Version:** CRCNS vta-1 is unversioned. It is pinned by the MD5 of `data.zip` (c5d2a9f8…, the same in `checksums.md5`, the S3 ETag and the bytes read), as recorded in the notebook header.
- **Contents:** 172 identified dopamine neurons (42/42/41/47, the paper's four groups) in 77 sessions. Sessions can be recovered from identical odor-onset arrays. No file names its mouse, so the per-mouse inset of Figure 5 can't be made.
- **Likely duplicates:** three pairs of task 1 SalB files share 65 to 99.7% of their spikes within 0.5 ms (chance at most 1.5%). Each pair is very likely one neuron deposited twice. The paper's statistics include all 42, and counting each once changes no outcome.
- **Unlabelled trials:** 21 file trials are rewarded but have a NaN trial type. They are left out.
- **40-minute window:** the files hold no recording onset, so I ran two readings (every trial in the file, or within 40 min of the session's first spike). Every outcome is the same under both.
- **Clock check:** spikes and events share a clock. Odor auROC is 0.50 before odor onset and 0.645 after it; rewarded against omission trials gives 0.87 at the reward time and 0.50 when shifted 2 s earlier.
- **Paper inconsistencies:**
  - The Figure 4A legend gives a 200 ms pre-reward window with F=15, but the printed statistics fit the Methods' 400 ms window (F=9.00, p=3.6e-11).
  - The Figure 5F counts as printed give Fisher p=0.037; the data give 8 (not 9) significant negative slopes and p=0.0405, the paper's 0.041.
- **Assumption, with a question for the paper's authors:** I assumed baseline is subtracted trial by trial. It recovers every printed slope count exactly. Under the other readings (neuron-mean baseline, or none), fig5f-task2-significant-slopes-shift fails (p=0.24). For fig5e-task1-significant-slopes-unchanged, one count falls outside tolerance, though the absence part still holds. The question is recorded as a `methods_unavailable` finding.

## 3. Protocol gaps

1. **Duplicates that aren't identical:** "Count each recording once" conflicts with claims whose expected counts (42) include the duplicates. I kept the paper's set as the main analysis and showed a count-once variant for every task 1 SalB claim.
2. **Paper code that can't be installed:** for MATLAB code that can't be installed, the protocol offers only `not_runnable`. The code was small, so I ported it to Python, recorded that as a deviation, and added 5 extra seeds plus the code's 10-simulation variant.
3. **Model claims marked as dataset claims:** the three model claims are marked `data: dataset` but use no data. I left them as written.
4. **Choosing among readings:** the protocol says a claim holds "under any reading" in one place (reader, step 3) and to adopt the best-supported choice when readings disagree in another (author, step 1.6). For the two Fisher claims, I applied 1.6 and set `assumed: true`.
5. **Version for an unversioned archive:** "pin the most recent published version" doesn't fit CRCNS, which has no versions. I followed archives.md (`unversioned` plus the MD5).

## 4. Runtime and failures

The notebook takes about 2.7 minutes, at 0.33 GB peak memory; the whole run took about 30 minutes (02:06 to 02:35 UTC).

- **Earlier bugs:** two errors in development code, fixed before the final runs. One was a typo in a lambda. The other was a pairwise spike comparison that would have exhausted memory; I replaced it before running it.
- **Blocked action:** an empty harness directory, `entries/starkweather-2018/.claude/.cc-writes`, could not be removed because the permission was denied. Git does not track empty directories, so it won't appear in the commit.
- **Stray files:** untracked dotfiles in the repo root (`.bashrc`, `.idea`, `scripts` and others) were not created by this run and were left alone.
