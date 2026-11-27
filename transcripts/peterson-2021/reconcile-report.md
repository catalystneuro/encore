I've written the reconciliation block in `attempts/peterson-2021-02.yaml` and added `entries/peterson-2021/earlier_findings.ipynb`. The entry check reports 0 errors, and both notebooks passed a clean run (the main one in 1790 s, the new one in 570 s). Nothing is committed.

The main result: the blind attempt has a bug in its own code. Its helper (`ajile.py`, `session_spectral`, line 357) assumes every ECoG recording starts at 0 s. In this version the dataset fixed the earlier attempt's finding 1: three files (sub-01 day 7, sub-04 day 3, sub-06 day 3) now set their ECoG `starting_time` to 29240.566–30682.414 s. As a result, peterson-2021-02 read those files' events about 8 h late.

**1. Blind:** yes (`blind: true`). The audit lines are only the generic pilot-notes link, the registry README, and the author writing its own record. None point at an earlier attempt's results.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | ECoG `starting_time` 0 in three late-starting files | fixed (checked in notebook) | – |
| 2 | 8088 events, false positives not marked | still_present | 1 |
| 3 | Reach angle convention not stated | still_present | 6 |
| 4 | Pose labelled meters, holds pixels | still_present | 5 |
| 5 | Bimanual overlap: 1708 values above 1 | still_present | 4 |
| 6 | `session_start_time` at 19:00 UTC-5 | fixed (checked) | – |
| 7 | NaN ECoG stretches | still_present | 3 |
| 8 | Sex and age missing | fixed (checked) | – |
| 9 | Seven subjects with depth groups, paper says five | still_present | 11 |
| 10 | `good` flags differ between a subject's files | still_present | 7 |
| 11 | S10/S11 group descriptions disagree with the data descriptor's Table 2 | still_present (checked), added as finding 18 with `found: on_prompt`, severity minor | 18 |
| 12 | Bad-segment rule unclear (question for authors) | still_present | 14 |
| 13 | "More widespread" measure unclear (question for authors) | still_present | 15 |

For finding 11, I compared the files against the descriptor's counts as quoted in the earlier statement, because the descriptor itself is not in the repository.

**3. New findings:** 2, 8, 9, 10, 12, 13, 16, 17. Finding 2 ("ECoG ends hours early, 237 events without neural data") comes from the bug: the ECoG actually starts late. I left the blind attempt's statements as they are.

**4. Outcomes that differ**
- **fig5-recording-day-effects** (earlier reproduced, now partially_reproduced): cause `error`, `error_in: this`, confidence medium.
  - The misread files produce the day effects the attempt reports for S01 LFB (p = 0.047), S01 HFB (0.023) and S06 HFB (6.7e-11), where the paper has none.
  - Read from `starting_time`, those become 0.777, 0.0546 and 0.847. Under each file's own electrode flags (the set the attempt's outcome rests on), 23 of 24 pairs then agree; S10 HFB (p = 0.0935) is the one left.
  - With the earlier attempt's electrode set (each subject's first file's flags), 24 of 24 agree. So which bad-electrode flags are used decides what remains. I left `supports` out.
- **fig4-precentral-subject-variability** (earlier reproduced, now partially_reproduced): cause `reading`, confidence medium.
  - Part 1 for S09 turns on which bad-electrode flags apply: 0.097 dB with the first file's flags, against -0.039 / -0.030 dB with the new attempt's sets.
  - Part 4 needs a tie-break under every set. The new attempt's pass of part 4 under each file's flags relied on the misread S04 day 3 file.

**5. What did not fit**
- `docs/pilot-notes.md` has nothing for pilot-15 to pilot-17. The `protocol` note covers pilot-14 (records filed by paper, no effect here) and the pilot-18 severity ratings, which I took from `docs/protocol.md` and the schema.
- `git log` for the earlier record points at HEAD because the checkout is shallow, so I used `earlier-entry/` for the earlier entry's files.
- The same bug affects every other ECoG claim of peterson-2021-02 (for example, Table 1's S06 values). Those outcomes match the earlier attempt's, so the protocol doesn't ask me to diagnose them, but they rest on misread data for three files.
- The last section of `earlier_findings.ipynb` reruns the whole spectral pass for the two outcome diagnoses. That goes beyond one section per finding; I added it so the numbers quoted in the reconciliation come from a committed notebook.
