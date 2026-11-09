I finished steps 1 to 6 by 04:33 UTC. The entry `entries/000231-rodgers-2022` passes `tools/entry.py check` and ran clean (`all`) in 4.7 min, and the handover package is built. Nothing is committed. I pinned version 0.220904.1554 because the paper cites it and it is the only published version; the reason is in the notebook header.

## 1. Outcomes (39 claims)

| Outcome | Claims |
|---|---|
| Reproduced (23) | neural-sessions, neural-hours (33.78 h in the raw Open Ephys files), task-rules, nothing-detection-only, one-task-per-mouse, servo-positions, outcome-consistency, forced-alternation-start, video-timebase, sync-gap-and-interpolation (gap 135 ms), bend-null-interpolated, neural-timestamps, unit-depth-layer, electrodes-order, recording-columns, units-obs-intervals, pose-structure, c0-rare-contacts (10 of 15 mice), contacts-structure, nwb-structure, file-layout, video-format, subjects-sex-age-strain |
| Not reproduced (6) | dataset-size (mice, sessions and frames match exactly; trials are 32,350 or 22,905 against 18,514), choice-time-first-lick (77.6% of trials), ignore-trial-definition (160 spoiled trials not ignored), trials-table-structure (5 of 32,235 pairs, all where trials are missing from the table), unit-quality-isi (the firing-rate part fails under both bin readings), session-labeling-quality (up to 7.7% of contacts have a missing frame) |
| Blocked, methods_underspecified (4) | reward-and-timeout (timeout readings 12.21 s and 8.34 s disagree), session-min-trials (one session has 84 or 101 trials depending on reading), prior-task-strategies, prior-orthogonal-subspaces |
| Blocked, data_missing (6) | response-window-timing, neural-video-alignment, behavior-clock-drift, tracking-mean-error, tracking-error-dataset1, tracking-error-challenge |

## 2. What I found about the dataset
- **Keywords are wrong:** all 30 detection sessions have the keyword "shape discrimination".
- **Right reward times are missing:** the right reward series is identical to the right lick series in every file.
- **Undocumented stimuli:** 1,533 trials are labelled "flatter convex" or "flatter concave", which Table 6 does not list.
- **Trials table differs from Table 6:**
  - `choice_time` is NaN on spoiled trials (Table 6 says 45 s after the window opens).
  - On 22% of other trials it falls 0 to 5 ms after the window opens, with a lick at that time on only 5.7% of them.
  - `ignore_trial` is not set on 160 spoiled trials.
- **Names and layout differ from the paper:** the files use one `behavior` module, not the group names in the Data Records. The neural recording has no timestamps array. 29 files have three contacts tables, not four.
- **Raw data not deposited:** the ADC and AUX channel files that carry the sync pulse are listed in each `.openephys` index but not in the dandiset. The Arduino logs and the curated tracking training sets are also absent.
- **Inclusion criteria not met:** 27 sessions break the paper's 2% limit on contacts with a missing frame, and one session has 84 usable trials.
- **No duplicate recordings.** The clock checks hold for every stream; for one session (KF134, 2018-02-09) the check on the neural stream is inconclusive.

**Assumptions:** none of the outcomes rests on one. I recorded three data-reading choices as deviations: frame counts come from the video duration headers, a whisker with no contacts table counts as zero contacts, and the flatter shapes are shown separately.

**Questions for the paper's authors** (filed as `methods_unavailable` findings): how the 9 s timeout is measured, and which trials count as "trials to analyze".

**Question for a reader** (`questions/000231.yaml`): should the three tracking claims and behavior-clock-drift use the paper's original Zenodo release (ref. 13)? Its README lists a `trainset/` folder and per-session behavioral logfiles. I read only that README, no data.

## 3. Where the protocol was unclear, wrong or incomplete
1. Step 1.6 lets the author adopt a reading as an assumption when readings disagree, but several criteria say to block in that case. I followed the claims file and blocked reward-and-timeout and session-min-trials.
2. In reward-and-timeout, the reward part fails on the right side, which the criterion's outcome rules don't cover. The disagreeing timeout readings already block the claim, so I blocked it and described the reward result in the notes.
3. Some criteria have no "partial" outcome for near-total agreement (trials-table-structure fails on 5 of 32,235 pairs). I applied them as written.
4. The protocol does not say whether an author may look at an outside archive only to locate data for a reader question. I read the Zenodo README for that purpose and used none of its data.
5. The video frame counts cannot be checked by decoding 2 TB of video. I used container headers and wrote that they are consistent with the paper, not shown.
6. `docs/archives.md` has two gaps. The version endpoint it names does not return `asset_count`; the `/info/` endpoint does. A HEAD request on DANDI's signed S3 URLs returns 403, so the S3 URL has to be taken from the redirect's Location header.
7. Step 1.2 does not say what to compare when checking for duplicate recordings. I compared trial times, whisker frame counts and video frame counts.

## 4. Runtime and failures
The notebook takes about 4.7 min; the whole run took about 66 min. During development, one network reset and one S3 403 failed a pass; I added retries to the helper and fixed how the S3 URL is resolved.
