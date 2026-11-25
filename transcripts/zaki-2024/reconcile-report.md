I've written the reconciliation block in `attempts/zaki-2024-02.yaml`. `python tools/entry.py all entries/zaki-2024` passed with 0 errors: `reproduce_zaki_2024.ipynb` ran in 247 s and the new `earlier_findings.ipynb` in 20 s. Nothing is committed.

## 1. Blind

`blind: true`. Every line `tools/blind.sh audit` printed is harmless: links in the protocol, the repository README naming the site, and the attempt writing its own record. The author never opened `zaki-2024-01`'s record, entry, transcripts or the repository history. The one thing it did see is the claims-file header, which describes the earlier author's data check (version 0.260825.1902, the four ensemble sizes, Ca_EEG3-4's Recall2 freezing of 15.1%). The author said so in its own report. The protocol lets the author keep the claims file, so this does not break blindness.

## 2. Earlier findings

| Earlier | What it reported | Status | Now |
|---|---|---|---|
| 1 | 2 of 9 mice, first offline recording only | still_present | 3 |
| 2 | No cell registration for Ca_EEG3-4; 19 registration tables with no imaging | still_present | 3 |
| 3 | Selection of mice and recordings not documented | still_present (checked in the notebook) | 11, `on_prompt` |
| 4 | Behaviour sessions about 1 h off the telemetry clock | still_present | 1 |
| 5 | OnePhotonSeries timestamps at 16.7 ms, covering half the recording | fixed (checked in the notebook) | |
| 6 | "quiet wake" state the paper does not use | still_present | 2 |
| 7 | Telemetry at 500 Hz, Methods say 100 Hz | still_present | 4 |
| 8 | Offline session descriptions describe the one-hour webcam experiment | still_present | 9 |
| 9 | Placeholder descriptions, shock amplitude without a unit, empty Week description | still_present | 5 |
| 10 | Analysis code not public | still_present | 8 |

Earlier finding 5 is fixed: the three re-converted files now have one timestamp per frame. The timestamps run over the whole recording, with a median step of 34.0 ms, and end 0.034 s after the last deconvolved sample.

## 3. New findings

Findings 6, 7 and 10 of `zaki-2024-02` are new; no earlier finding points at them. Findings 11 and 12 were added on prompt.

## 4. Outcomes that changed

- **offline-bursts-above-shuffle** (earlier blocked, now reproduced). Cause: `claims_changed`, confidence medium.
  - Both attempts got the same numbers under both ways of thresholding the shuffled traces.
  - A reader amended the criterion during `zaki-2024-02` so that the second reading also counts: shuffles held to the real trace's mean plus 2 SD. Under that reading the claim is reproduced.
  - The earlier attempt had blocked the claim because its shuffled burst rate was far from the paper's chance level. Neither reading comes near that level (3.38 to 4.39 per min), and `zaki-2024-02` never compared against it.
  - `supports: blocked`.
- **fig5c-wake-overlap-neutral-coburst** (earlier not_reproduced, now partially_reproduced). Cause: `label`, confidence high.
  - The numbers are essentially the same in both attempts. The only difference is 2 bursts that fall between sleep intervals, which the earlier code labels by stretching each interval by 0.1 s.
  - The earlier attempt judged the claim on wake with quiet wake alone. The criterion accepts any of its readings, and under wake alone it gives partially reproduced.
  - `supports: partially_reproduced`.

## 5. Protocol points that did not fit

- **No notes for most of the versions after pilot-7.** `docs/pilot-notes.md` has sections for pilot-8, 9, 10, 12, 13 and 14 only. What pilot-15, 17 and 18 changed I took from the version checks in `tools/entry.py`.
- **The "assumed reading" rule is in no note.** The current step 1.6, where an outcome rests on an assumed reading and is blocked only when no choice is defensible, is not described anywhere in the notes. Both changed outcomes in `zaki-2024-02` are marked as assumed under it.
- **A partly reported finding has nowhere clean to point.** Earlier finding 9 bundles three problems, and `zaki-2024-02` reported only one of them (its finding 5). Each earlier finding gets one item with one `now`. I pointed `now` at 5 and added the two missed parts as finding 12 (`on_prompt`), so finding 12 has no pointer to it.
- **Earlier finding 3 is half addressed.** The new release notes list the two mice and the first offline recordings as known gaps, but still give no reason. The statuses for findings not reported again do not include `partly_fixed`, so I recorded it as still present.
- **The chance-level rule was not applied in the new attempt.** The protocol says to compare against a chance level the paper states, but `zaki-2024-02` did not compare with the paper's source-data chance level for offline-bursts. This is noted in the outcome item; I changed no outcome.
