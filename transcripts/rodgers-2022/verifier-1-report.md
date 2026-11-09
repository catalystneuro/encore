**Verifier report, round 1: Rodgers 2022 (Sci Data 9, 620), DANDI:000231 v0.220904.1554**

The claims file lists 39 claims (`grep -c "^- id:"`).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| dataset-size | not_reproduced | Mice 15, sessions 115 and video frames 63,979,800 (88.86 h) match exactly. Trials are 32,350 (a) or 22,905 (b), +74.7% and +23.7%, both outside the 10% partial band (cell 11). |
| neural-sessions | reproduced | 44 files are named ecephys and 44 hold the ElectricalSeries and units (cell 13). |
| neural-hours | reproduced | Reading (b) gives 33.782 h, inside 33.8 ± 0.05; reading (a) gives 33.656 h. 64 channel files per session (cell 15). Caveat: problem 2. |
| task-rules | reproduced | 21,752 of 21,752 trials to analyse, in 115 of 115 sessions, follow the rule. The rule-based task agrees with experiment_description in 30 + 85 sessions (cell 17). |
| nothing-detection-only | reproduced | 0 of 85 discrimination sessions (by experiment_description) contain "nothing" (cell 19). Caveat: problem 5. |
| one-task-per-mouse | reproduced | Every mouse has a single task: 5 detection mice, 10 discrimination mice (cell 21). |
| servo-positions | reproduced | Trials with a shape use exactly {close, medium, far}, and all 115 sessions have all three (cell 23). |
| response-window-timing | blocked (data_missing) | No motor-time column or series exists. The asset list shows only NWB, mkv, Open Ephys and Kilosort/Phy files, so no part can be tested. Window opening minus start_time has median 3.023 s (cell 25). |
| choice-time-first-lick | not_reproduced | On non-spoiled trials the first lick matches choice_time in only 0.776 of trials; every session is below 0.99. On all 265 spoiled trials choice_time is NaN, not 45 s (cell 27). |
| outcome-consistency | reproduced | 32,350 of 32,350 trials are consistent, direct-delivery trials included (cell 29). |
| reward-and-timeout | blocked (methods_underspecified) | Timeout reading (a) is 12.21 s (fails); reading (b) is 8.34 s (holds), so the readings disagree. The reward part also fails as computed (8.5% of error trials "rewarded"), but rewards/right is identical to licks/right in all 115 files, so the right side cannot be tested. The left side holds: 1.0 of correct trials rewarded, 0.0 of error trials (cells 3, 31). |
| forced-alternation-start | reproduced | In 110 of 110 sessions that include trials 0–44, none is random, and the first random trial is 45. The other 5 tables start at trial 61–124 and pass only vacuously (cell 33). |
| ignore-trial-definition | not_reproduced | 160 spoiled random trials in 50 sessions have ignore_trial False. ignore_trial equals (not random or optogenetic) on every trial (cell 35). |
| trials-table-structure | not_reproduced | 5 row pairs in 4 sessions break stop_time = next start_time (7–68 s apart), all where a trial number is skipped. id equals trial on every row (cell 37). Caveat: problem 6. |
| video-timebase | reproduced | Processed, pose and contact times lie on the 5 ms grid within 9e-13 s, with no step shorter than one frame (cell 39). |
| sync-gap-and-interpolation | reproduced | The longest interpolated run is 4 frames. The trial-start gap has median 0.135 s, and the lowest session-wise fraction within 10% is ≥0.984 for each of C1, C2 and C3 (cell 41). |
| bend-null-interpolated | reproduced | 0 of 368,927 interpolated frames have a bend value (cell 43). |
| neural-timestamps | reproduced | Stored rates are 29,999.9354–30,000.0199 Hz and none is exactly 30 kHz. Spacing is constant because the file stores a rate, not a timestamps array (cell 45). |
| neural-video-alignment | blocked (data_missing) | ADC and AUX files are listed in the .openephys index but not deposited, and all_channels.events holds only its header (cell 47). I checked the archive: each exp.dat is 2 bytes × 64.0 channels × samples, so it holds neural channels only. The neural side cannot be tested. |
| behavior-clock-drift | blocked (data_missing) | The archive holds no Arduino times or logs. File kinds (cell 49 and my asset query) are NWB, mkv, Open Ephys, settings.xml and Kilosort/Phy files only. |
| unit-quality-isi | not_reproduced | The ISI part holds (max 4.93%). The firing-rate part fails under both readings: 6 units with 60 s bins (max 23.3%) and 78 units with trial bins (cell 51). |
| unit-depth-layer | reproduced | Depth equals the y of the neuron_channel electrode for 999 of 999 units, and the layer depth ranges do not overlap and run in order (cell 53). Caveat: problem 4. |
| electrodes-order | reproduced | In 44 of 44 sessions y increases in steps that are multiples of 20 µm, rows (56–64) equal the data columns, and every location string parses into its 5 items (cell 55). |
| recording-columns | reproduced | Each of the 44 sessions names a column; C1/C2/C3 account for 33 (cell 57). |
| units-obs-intervals | reproduced | Each unit has one interval holding all its spikes. The interval starts at the first sample and stops exactly one sample after the last, within the criterion's one sample (cell 59). |
| pose-structure | reproduced | 115 of 115 sessions have 4 × 8 series of shape (N, 2) and one conversion value; the conversion varies across sessions (cell 61). |
| c0-rare-contacts | reproduced | C0 makes fewer contacts than each of C1–C3 in 10 of 15 mice (cell 63). |
| session-min-trials | blocked (methods_underspecified) | Reading (a) gives a minimum of 84 (228CR, 2019-07-15) and reading (b) a minimum of 90, so the readings disagree (cell 65). |
| session-labeling-quality | not_reproduced, provisional | The contact-missing maximum is 0.077 under all four readings (cell 67), but problem 1 could move a reading under 2%, which would make this blocked. |
| contacts-structure | reproduced | 431 tables, all with tip_x/tip_y and angle and no start > stop. The missing tables are 21 for C0 and 8 for C3 (cell 69). |
| nwb-structure | reproduced | Every section is present under the "behavior" module naming, and video paths resolve in 115 of 115 files (cell 71). |
| file-layout | reproduced | 115 files are named and placed correctly, 115 have exactly one video, and 44 sourcedata folders hold Open Ephys and Phy files (cell 73). |
| video-format | reproduced | All files are matroska/h264 at a nominal 30 fps, and 111 of 115 are 640 × 550 (cell 75). |
| subjects-sex-age-strain | reproduced | All are C57BL6/J. Sex is 10 F / 5 M (binomial p = 0.302, minority exactly 1/3). First sessions are at 197–436 days (cell 77). |
| tracking-mean-error | blocked (data_missing) | No curated labels or predictions exist in the asset list, which I confirmed against the archive. |
| tracking-error-dataset1 | blocked (data_missing) | Same reason. |
| tracking-error-challenge | blocked (data_missing) | Same reason. |
| prior-task-strategies | blocked (methods_underspecified) | The claims file gives no method. |
| prior-orthogonal-subspaces | blocked (methods_underspecified) | The claims file gives no method. |

Totals: 24 reproduced, 0 partially reproduced, 7 not reproduced, 8 blocked.

### B. Problems

1. **[affects a conclusion]** `rodgers._whisker`, `contact_missing`, used in cell 67 for session-labeling-quality:
   - The code counts the stop_time frame as part of each contact. The notebook never checks this against `frame_stop` and `duration_frames`. If stop is exclusive, every contact gets one extra frame, which inflates the missing fractions.
   - The fraction is taken per whisker. The paper's "contact events" of a session could also be pooled over whiskers, a reading the paper allows that was not run.
   - Either change could pull one reading under 2%, which would turn the outcome into blocked.
2. **[affects a conclusion, unlikely]** Cell 15, neural-hours reading (b):
   - The criterion leaves out the Open Ephys "test recordings". The notebook counts whole files and never reads the per-record recording number.
   - Leaving them out can only lower 33.782 h. The margin to 33.75 h is about 115 s.
3. **[does not affect a conclusion]** Cell 31, reward-and-timeout:
   - rewards/right duplicates licks/right in every file, so the right-side reward test measures licks. This deposit defect should be reported as such.
   - The verdict line returns "blocked" without stating that the reward part also fails.
4. **[does not affect a conclusion]** Cell 53, unit-depth-layer: the unit's layer equals the layer in its electrode's location string for only 553 of 999 units. Two layer labels for the same depth disagree, and the notebook neither explains nor reports this.
5. **[does not affect a conclusion]** Cells 3 and 19, nothing-detection-only:
   - general/keywords say "shape discrimination" in all 115 files, including the 30 detection sessions. The criterion allows "description or keywords".
   - Using the description alone is reasonable because the keyword is identical in every file, but the choice should be stated as a reading.
   - The same constant keyword makes `R.task_from_metadata` return None for detection sessions, so the metadata branch of `task_by_rule` never fires.
6. **[affects a conclusion; claims-file reading]** trials-table-structure: the criterion compares consecutive rows. All 5 failures are where a trial is absent from the table (paper: trials before the video began are dropped; munged trials). The paper's "next trial" may mean the next trial run, so not_reproduced may be due to the claims file's reading rather than the data.
7. **[does not affect a conclusion]** Cell 1: `V["frames"]` overwrites the container's frame count `v.frames` with duration × 30, and the overwritten value is never shown. The exact match to 63,979,800 supports the method.
8. **[does not affect a conclusion]** Cell 51: the amplitude criteria were not reported, although `amplitudes.npy` is in sourcedata and the criterion asks for them "where sourcedata allows".
9. **[does not affect a conclusion]** Cell 8: the clock check fails for KF134 2018-02-09 (ratio 1.01). That session's units still enter unit-quality-isi and the other unit claims.
10. **[does not affect a conclusion]** Cell 71: Table 4 electrode columns are checked only by row count.

Helper tests on synthetic inputs all gave the expected values: `max_true_run`, `isi_fraction`, `low_rate_fraction_bins`, `low_rate_fraction_trials`, `assign_trials`, `openephys_samples` and `grid_offset`.

### C. Not checked

- **Whether contact stop_time is inclusive (problem 1).** Needed output: `frame_stop - frame_start` against `duration_frames` for one session, plus cell 67 rerun with exclusive stops and with contacts pooled per session.
- **Test recordings in the Open Ephys files (problem 2).** Needed output: the distinct recording numbers in the record headers of one channel file per session.
- **Why the two layer labels disagree (problem 4).** Needed output: a crosstab of `UD.layer` against `UD.el_layer`, with sample location strings.
- **The container frame counts (problem 7).** Needed output: `v.frames` per video.
- **The three earlier-paper and tracking claims.** Nothing could be done beyond confirming in the archive's file list that the data are absent; the Zenodo release was not consulted, as instructed.
