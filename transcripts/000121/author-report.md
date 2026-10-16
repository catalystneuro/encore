I've done steps 1 to 6 for dandiset 000121: the claims file, the entry, the attempt record and the handover (`python tools/entry.py handover`). Nothing is committed. The paper is open access and I used its full text (PLOS JATS XML, saved under `paper/`). I pinned version 0.220124.2156: the paper cites no DANDI version, and this is the newest published one. It holds the same 12 files (same blobs) as 0.210815.0703; the draft holds no files.

## 1. Outcome per claim

| Claim | Outcome |
|---|---|
| session-configurations | partially reproduced |
| r-trial-counts | partially reproduced |
| j-sessions-complete | blocked (data_missing) |
| delays-and-times | partially reproduced |
| channels-task-correlated | reproduced (J 72, R 80 against 74 and 80) |
| pca-variance | partially reproduced |
| spatial-plane-variance | not reproduced |
| plane-timecourse | reproduced |
| onoff-predicts-kinematics | reproduced |
| speed-axis-within-distance | partially reproduced (R 11 of 12, J 6 of 12) |
| distance-after-speed | reproduced |
| speed-distance-projection | not reproduced |
| single-trial-variance | not reproduced |
| ellipse-orientation | reproduced |
| on-greater-than-off | partially reproduced (5 of 6 tasks) |
| relative-deviation-decreases | reproduced |
| svm-ring-and-distance | not reproduced (all four accuracies below the paper's) |
| svm-3rings-by-ring | partially reproduced |
| arc-error-distance-independent | not reproduced |
| distance-error-and-plane-projection | reproduced, but R's full error is inside its bound by only 0.001 cm |

Totals: 7 reproduced, 7 partially reproduced, 5 not reproduced, 1 blocked. All claims use the dandiset alone; there are no outside inputs.

## 2. What was found about the dandiset

- **PMd and M1 labels are swapped on the units.** Units 0 to 95 are labelled PMd but point to M1 electrode rows; in R that array has 29 silent channels and almost no target signal. The data identify units 96 to 191 as PMd, so I used those and showed the file's label as a variant.
- **Spike times broken in every J file.** The boundary between units 0 and 1 is misplaced: unit 1's spike times run to the end of the session and restart near 0.
- **Positions are mislabelled.** They are in mm but stated in meters, with `conversion` NaN.
- **Configuration not recorded.** `task_id` is 2 in every trial, so the target configuration has to be inferred from target positions.
- **Smaller metadata errors.** The `is_successful` description is wrong; the description says sorted spikes, but the units are threshold crossings; the archive summary gives 15 files and 187.5 GB for a version of 12 files and 39.5 GB.
- **Monkey J is incomplete.** Only 5 of J's 16 sessions are deposited, and none of its horizontal sessions. The paper's data link returns HTTP 403, and no analysis code is published.
- **Session dates and trials differ from the Methods.** R's horizontal and vertical dates are the reverse of the Methods; trial counts fit better when grouped by the files' geometry. R's delays run to 1000 ms (the paper says 900), and R has almost no no-delay trials (the paper says 10%). R's 3-rings session holds 1340 trials where the paper used 912.
- **Cursor glitch.** In R's 2017-01-19 session the cursor differs from the hand by more than 1 m in over 1% of samples.

## 3. Where the protocol was unclear, wrong or missing something

1. **A criterion can fail to cover a result.** For pca-variance my criterion named no outcome for "one R value just outside, all J values inside". The protocol only covers ties. I judged it partially reproduced and recorded this as a deviation.
2. **"Use the paper's uncertainty" does not fit SEM over CV folds.** That SEM does not describe a repeat with other trials or other hyperparameters, so I used 10% and gave the reason in the claims file.
3. **No guidance when data contradict a label that every claim depends on.** I settled which array is PMd from the data during the data check, before writing criteria, and showed the file's label as a variant.
4. **No rule for one subject's data being partial.** I tested J's claims on the 5 sessions present, recorded deviations, and blocked one claim for the missing sessions.
5. **p-values with no stated null.** The rule on chance levels covers selections only. For the plane's p < 1e-4 I added a shuffle null and reported it in the notes, outside the criterion.
6. **No finding kind fits "the paper's Methods disagree with the data"** (the swapped R dates). `paper_inconsistency` is defined as the paper disagreeing with itself, so I used `other`.
7. **Step 5 assumes analysis code exists.** None is published, so I read the conversion code (catalystneuro/shenoy-lab-to-nwb at 319acb4); it explains the data but settles no analysis choice.
8. **The suggested clock check needed adapting.** With variable delays I decoded the target before and after target onset, and with the previous trial's labels. The latter comes out slightly above chance (at most 0.023), so I report it as near chance.
9. **Results per session are not possible everywhere.** I gave them for the channel, on/off and variance claims; PCA and SVM need pooled sessions.
10. **An empty draft is not mentioned.** The draft holds no files; it had no effect on the attempt.

## 4. Runtime and failures

- The notebook runs in 466 to 472 s from a clean environment; about 197 s of that is streaming. Peak memory is about 3.5 GB.
- Two clean runs gave identical outputs, and `check` reports no errors.
- Earlier development runs failed on differing LFP series names, unsorted J spike times, and NaN onsets; all three are fixed.
- The repository root holds untracked dotfiles (`.bashrc`, `.mcp.json` and others) and `scripts`. These are character devices mounted by the sandbox, not files I created, so I left them.
