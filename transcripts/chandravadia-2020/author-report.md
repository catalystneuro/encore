I've finished steps 1 to 6 for `chandravadia-2020` on DANDI:000004 version 0.220126.1852. The entry is in `entries/chandravadia-2020/` and the record is `attempts/chandravadia-2020-02.yaml`. `lock`, `check` and `all` passed with 0 errors, the notebook ran clean in 144 s, and `handover` wrote `executed/chandravadia-2020/handover/`. Nothing was committed.

On blindness: `transcripts/chandravadia-2020/` was still in the checkout. I listed it and it was empty, so I saw nothing from the earlier attempts.

**1. Outcomes (25 claims)**

| Claim | Outcome |
|---|---|
| counts-neurons-subjects | reproduced (1864 units, 59 subjects) |
| counts-sessions | reproduced (the 87 sessions are exactly those of Online-only Table 1) |
| table1-demographics | partially (56 of 59 subjects match) |
| task-structure | partially (8 sessions have 50 or 97 encoding trials) |
| new-old-label-coding | not reproduced (labels reversed in the files) |
| ttl-codes | partially (78 of 87 files) |
| experiment-ids | partially (83 of 87 files) |
| session-dates | partially (86 of 87 on the 1st) |
| units-table | partially (many SNR/IsolationDist values not finite) |
| electrodes-table | not reproduced (impedance empty everywhere) |
| isi-criterion | partially (99.68% of units pass) |
| fig5a-mtl-locations | reproduced |
| fig5c-auc-all | reproduced (0.753 ± 0.094) |
| fig5c-auc-sites | reproduced |
| fig5b-roc-asymmetric | reproduced (z-ROC slope 0.78, p = 4e-9) |
| fig5d-confidence-accuracy | reproduced |
| vs-cells-proportion | reproduced (332, 17.8%) |
| ms-cells-proportion | not reproduced (112 cells; the code's choices give 151) |
| dual-cells-proportion | not reproduced (12 cells; the code's choices give exactly 26) |
| fig5f-site-proportions | partially (3 of 6 values within tolerance; the code's choices give 6 of 6) |
| twh-sessions | reproduced |
| previous-release-link | partially (64 of 65 sessions found) |
| previous-release-additions | partially (23 sessions and 17 subjects match; the new sessions hold 325 neurons, not 288) |
| fig4-example-vs-neuron | reproduced |
| fig3-example-vs-neuron | blocked, data_missing (session 144 is in neither the dandiset nor the paper's OSF deposit) |

**2. What I found**

About the data (11 findings in the record):
- `new_old_labels_recog` is 1 for old and 0 for new, the reverse of both the paper and the column's own description.
- Impedance is empty for every electrode; MNI coordinates are empty in 8 sessions.
- Quality metrics are often unusable (SNR not finite for 86 units, IsolationDist missing for 493), and the paper's `IsolDist` column is named `IsolationDist`.
- Three subjects' age or sex differ from both papers' patient tables.
- 8 sessions have fewer than 100 encoding trials.
- Four files use experiment ids outside Table 2, and nine hold event codes outside Table 1.
- **Privacy:** in 38 files the trial and event times are Unix timestamps. They reveal the exact day of each recording, which the paper says `session_start_time` was set to hide. Separately, session 48 is dated the 13th and session 68 is dated 2000.
- `stop_time` is the end of the trial, not the stimulus offset the paper describes.
- Identical spike trains appear in two files for sessions 38/39, 43/44 and 54/55: the same neurons recorded across two sessions of one recording.
- Two units in session 58 store every spike twice, and 13 units have spike times out of order.
- Session 144 (the Figure 3 neuron) and session 98 of the earlier release are missing.

About the paper:
- The paper's MS and dual counts follow its code (0.2 to 1.7 s window, correct trials only), not its text (1 s window, all trials). The code's choices reproduce 343 VS, 151 MS and 26 dual cells, and all six per-site percentages.
- The Methods say 89 sessions; the table and files hold 87.
- The stated 288 new neurons is the difference of the two releases' totals; the new sessions themselves hold 325.
- The Python and MATLAB versions of the dynamic confidence split differ.

I made no assumptions (no `assumed` outcomes), so there are no questions for the paper's authors. I asked no reader questions.

**3. Points where the protocol was unclear**
1. Shared-clock check: the suggested decoding test didn't fit this data. I compared onset responses at the true onsets against onsets shifted ±3 s. This holds in 68 of 87 sessions; the other 19, mostly with few units, could not be established and are named in the notebook.
2. Duplicated recordings: the protocol says to count each once, but the claims file's main reading counts per file. I followed the claims file and showed both counts.
3. No outcome fits "the criterion's method fails, but the paper's own code reproduces the number exactly". I recorded not_reproduced, kept the code's result as a variant, and added a `code_mismatch` finding.
4. Nulls for a selection that conditions on correct trials: shuffling the labels alone is not a null (it gave about 144 units). I permuted label, response and category together per session (about 105).
5. Whether the paper's own Online-only Table 1 counts as an outside input is not said. I read it at run time from Europe PMC, to avoid embedding numbers, and listed it under `inputs`.
6. There is no finding kind for exposed patient information; I used `metadata_error`.
7. The OSF deposit's NativeData.zip was listed while preparing, outside the notebook. The notes say so; the block rests on the NWBData.zip listing, which the notebook prints.

**4. Runtime and failures**
The work took about 30 minutes (07:21 to 07:52 UTC). The notebook runs in 144 s (71 s of that is loading), with about 0.3 GB peak memory in development. Nothing failed in the final run. Two earlier dev runs failed: one on a string-formatting error, which I fixed, and one gave a label-only null that was invalid, which I replaced.
