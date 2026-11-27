I've written the `reconciliation` block in `attempts/amjad-2025-02.yaml` and added `entries/amjad-2025/earlier_findings.ipynb` to `entry.yaml`. The lock file was unchanged; `python tools/entry.py check entries/amjad-2025` reports 0 errors, and both notebooks pass `entry.py run` (75 s and 33 s). Nothing is committed.

**1. Blind: no (`blind: false`).** The audit printed only three harmless lines: two links to the pilot notes and the run's own URL. The author never saw the earlier record, entry or transcripts. But two texts left in its checkout carried the earlier results:
- The claims file's opening comment was written by the earlier author after its data check. It says events repeat about five times, the raw 09/26 ephys and Monkey P's spikes are off the trial clock, and the raw FSCV can't be matched to the trial-aligned traces. The author's report says it read this before its own analysis.
- The release notes of 0.261120.1306, printed in the author's data check, list the problems "found by a reproduction attempt" and how each was fixed.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Events stored about 5 times | fixed | |
| 2 | Trial conditions only in event codes; codes 35/36 not labelled as reward size | still_present (added, `found: on_prompt`, minor) | 12 |
| 3 | FSCV table covers 734 of 1468 trials; c8ds missing | still_present | 1 |
| 4 | FSCV columns have no units; reference point of da not stated | still_present | 7 |
| 5 | Raw FSCV labelled amperes, values in nA | fixed | |
| 6 | Raw FSCV scan times not on the trial clock | fixed | |
| 7 | LFP conversion factor makes values picovolts | fixed | |
| 8 | Raw 09/26 ephys offset by 9831.35 s | fixed | |
| 9 | Monkey P spikes offset by 6800.666 s | fixed | |
| 10 | Unit 0 merges unsorted and poor-quality spikes; spikes below 1 s, repeats, unsorted | fixed (the merge stays but is now described) | |
| 11 | Monkey P has no trials or events | partly_fixed (events added, codes still unnamed) | 2 |
| 12 | No implantation dates | still_present | 3 |
| 13 | Site cl3 vs c33; files cite the preprint; 8000 vs 7500 Hz | partly_fixed (the article is now cited) | 6 |
| 14 | FSCV waveform -0.347 to 1.340 V | still_present | 5 |

**3. New findings in amjad-2025-02:** 4, 8, 9, 10 and 11. Finding 4 (the 8000 Hz high cut) also covers part of earlier finding 13, which points at finding 6.

**4. Outcomes that changed:** only `fig3a-redox-peaks`, from blocked to not_reproduced.
- **Cause:** `dataset_changed`, high confidence. In the old version the raw FSCV scan times were a 0.1 s grid starting at the first trial, so the earlier attempt could not place the current in the trials. The new version puts each scan on the session clock, and my check confirms it: at shift 0 the raw current tracks the stored oxidation current in 96.3% of 734 rows, against 39.8% and 51.9% at ±50 scans.
- **Supports:** `not_reproduced`. On the fixed clock the voltammogram is flat within noise, and its falling-sweep minimum is at 0.897 V, outside the -0.35 to -0.05 V the criterion needs.
- `chronic-duration` is blocked in both attempts, under different reasons (`metadata_insufficient` before, `data_missing` now); since the outcome is the same, it has no item.

**5. What did not fit the protocol**
- **Blindness leaks.** The protocol lets the author keep the claims file, but this one's header repeats the earlier attempt's data-check results. The release notes, which the author is expected to read, also summarise the earlier findings. So a repeat attempt on a fixed dataset cannot be blind as defined.
- **No git history.** The repository has a single squashed commit, so `git show $c:…` returns the current entry, not the earlier one. I used the `earlier-entry/` copy instead, and couldn't diff the claims file between attempts. The block therefore says only that nothing in either record points to a changed criterion.
- **Pilot notes stop at pilot-14.** There is nothing on pilot-15 to pilot-18. The one later change I could name is from `protocol.md`: authors now rate each finding's severity from pilot-18, which the earlier attempt did not.
