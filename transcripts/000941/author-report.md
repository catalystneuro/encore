I tested 1 of the 26 claims, and it was not reproduced. The other 25 are blocked because their data are not in the dandiset, which holds no kinematics at all. The entry passes `python tools/entry.py all` (0 errors, notebook runs in 32 s), and the handover package is built in `executed/000941-rouse-2015/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table2-trial-counts | blocked: data missing |
| table2-movement-time | not reproduced (monkey L only) |
| fig2-trial-count-coax-45 | blocked: data missing |
| The other 23 claims (fig2 shapes, fig4, all fig5–fig7, fig8a/b, fig8-hand-shape, fig9, fig10, elbow point) | blocked: data missing |

- **Trial counts:** the file of session L20120928 holds 412 successful trials (numbers 201 to 673, about 53 of 86 minutes) and no failed trials. The paper reports 768 trials and 717 successes, so the counts cannot be taken from a part of the session.
- **Movement time:** the median from the dataset's `move_onset_time` to `contact_time` is 200 ms (quartiles 160 and 240). The paper gives 255 ms (225, 295), so it is outside the tolerance of 229.5 to 280.5 ms, and it gives 41 samples where the paper has 52. The Kruskal-Wallis comparison across monkeys could not be run.
- **Coaxial cylinder at 45 degrees:** the file has 19 such trials against the paper's 28. That fits a file holding 57% of the session's successful trials.

## 2. What was found about the dataset

- **Version:** I pinned 0.241029.1405, the only published version; the paper cites none.
- **No kinematics:** no file holds marker positions or joint angles. The files hold trial tables, 16 EMG channels at 50 Hz and multiunit spikes from 64 channels.
- **Monkey L only:** the description points to dandiset 001209 for another monkey (X). It has no published version and the claims file does not name it, so I did not use it.
- **`tgt_obj` is not the object:** it runs in three long blocks (118, 159 and 135 trials) regardless of object or location.
  - `obj_id` is the object, but its codes have no names. I named them from the object order in the paper's Fig. 1 legend: 2 = perpendicular cylinder, 1 = coaxial, 4 = button, 3 = sphere. The names fit every constraint the legend states.
  - EMG decodes `obj_id` at 0.99 around contact, against 0.42 for `tgt_obj`.
  - I recorded the naming as a deviation and a finding, not as outside data.
- **Clock check:** EMG and spikes share the trial table's clock. The object decodes near chance a second or more before contact and near perfectly at contact; the next trial's object does not.
- **Trial numbers:** trial 255 or 256 is stored as 127 in all four calibration files. In session 20120927 a second trial is also numbered 127.
- **Event times:** they lie on a 20 ms grid and are not defined. `reward_time` falls a median of 0.10 s after contact, but the paper's task requires a 1 s hold before reward. `start_time` and `stop_time` are fixed 1 s windows around the cue and the reward.
- **Duplicates:** each minival file repeats the first two trials of the matching calibration file. Spikes and timestamps are identical, but the EMG is rescaled by a factor of 0.955 to 1.016.
- **Assumptions, questions for the paper's authors, questions to a reader:** none. No outcome rests on an open method choice, and I found no misreading in the claims file.

## 3. Where the protocol was unclear

1. **Claims that need three monkeys when only one is present.** The protocol does not say whether to block such a claim or judge the part that can be tested. I judged the movement time on L, since a failing L median makes the claim fail whatever X and Y show. I blocked the counts.
2. **Counts on a dataset holding only part of a session.** The protocol does not say whether that is `blocked` or `not_reproduced`. I chose `blocked: data_missing`, because the subset neither confirms nor contradicts the paper's counts.
3. **Naming dataset codes from the paper's own figure.** `with_labels` is defined for outside sources, and this source is the paper itself. I treated it as a method detail taken from the paper (step 1.6).
4. **Near-identical duplicates.** Step 1.2 speaks of identical recordings; here the copies match except for a rescaled EMG. I reported them as duplicates and noted the difference.
5. **Streams used by no claim.** Step 2's clock check is written for every data stream. I checked EMG and spikes anyway, even though only the trial table enters any claim.
6. **Blocked claims and notebook cells.** The protocol does not say whether blocked claims get notebook cells. I gave cells to the two count claims, since they show what the data hold.

## 4. Runtime and failures

- The run took about 13 minutes (18:51 to 19:04 UTC); the notebook itself runs in 32 s.
- One development error, an overflow on an unsigned trial-number column, was fixed before the final run.
- The sandbox refused to delete an empty `.claude/` directory the harness created inside the entry. Git ignores empty directories, so it will not be committed.
- The untracked dotfiles and `scripts` in the repository root are sandbox device files, not mine.
