The reconciliation block is written in `attempts/churchland-2012-02.yaml`, along with one added on-prompt finding (number 9). The new notebook `entries/churchland-2012/earlier_findings.ipynb` is added to `entry.yaml`. The lock file came out unchanged. `tools/entry.py all` passed: the main notebook ran in 1222 s and `earlier_findings.ipynb` in 47 s. The final `check` gives 0 errors. Nothing is committed.

**1. Blind: recorded as `false`, narrowly.** The audit's five hits are harmless: links to the pilot notes and the site inside the protocol and README the author was given, and the author writing its own record. The author saw no earlier record, entry, question, transcript, outcome or number. But it did read the header of the claims file. The earlier attempt's author wrote that header, and the protocol lets the blind author keep it. It names two faults the earlier attempt found (the wrapped `spike_times_index` and the clock resets of the 2010 file), and it says ses-20090910 matches the N-9-10-2010 dataset. The author said so in its report and tested the clock itself. `blind_note` explains this. If you read "results" as outcomes only, this could be set to `true`.

**2. Earlier findings**

| # | Earlier finding | Status | now |
|---|---|---|---|
| 1 | Sorted isolations and other datasets missing | still_present | 1 (rest in 2) |
| 2 | `spike_times_index` first entry wrapped at 65536 | fixed | |
| 3 | Clock restarts and overlapping trials in Nitschke files | fixed | |
| 4 | Hand position stated in metres but stored in mm | fixed (conversion now 0.001) | |
| 5 | Hand-to-cursor offset not described | fixed (new `cursor_offset` column) | |
| 6 | Units table has only the default description | fixed | |
| 7 | Nothing says which sessions are the paper's datasets | still_present | 9, added `found: on_prompt`, minor |
| 8 | Session dates of the first conversion set to 2009 | fixed (Nitschke files now dated 2010) | |

**3. New findings:** 2, 3, 4, 5, 6, 7 and 8 of churchland-2012-02.

**4. Outcomes that changed (6 claims).** As a check, I ran the earlier attempt's code on the new version. Aligned on `move_begins_time`, it gives back the earlier numbers (J-array 19.98%, 1.033 Hz; N-array PMd 18.16%). So the files match where it matters, apart from the new `offline_move_onset_time` column.

| Claim | Earlier → now | Cause | Confidence |
|---|---|---|---|
| var-captured-jpc-plane | reproduced → not | dataset_changed: the new onset column (earlier code with it gives 16.67% in J-array) | high |
| pc23-variance | partial → not | dataset_changed: J-array ratio 0.925 vs 0.778 by onset column | high |
| rotation-frequency | partial → reproduced | dataset_changed: J-array 1.033 vs 1.447 Hz by onset column | high |
| suppfig3-shuffle-controls | not → partial | dataset_changed: J-array shuffle 3 at 0.745 of original vs 0.77–0.79 on `move_begins_time`; limit 0.75 | medium |
| suppfig5-areas-variance | partial → not | error in the earlier attempt (see below); supports not_reproduced | medium |
| fig6-velocity-model | not → partial | reading: when the simulated preparatory term ends | high |

- **suppfig5-areas-variance:** N-array PMd decides this claim against an 18% floor. The earlier attempt got 18.1% only because its normalisation range includes the window's first and last smoothed bins, which are artefacts of the filter's edge handling (`earlier-entry/reach.py`, `condition_rates` then `jpca`). Without them the earlier code gives 17.70%, and the blind attempt's four readings give 17.6–17.9%.
- **fig6-velocity-model:** the blind attempt changed its main reading after verification round 1. Its first reading matches the earlier one and gives not reproduced, as the earlier attempt did.

**5. Protocol issues**
- **No notes for most versions:** `docs/pilot-notes.md` has no section for pilot-11 or pilot-15 to pilot-18. I took the rules for pilot-15, 17 and 18 from `tools/entry.py`. Pilot-18's severity ratings are also described in `docs/protocol.md`.
- **Claims file:** it is still the one the earlier author wrote under pilot-7, with what that author found in the data check in its header. That header is how the blind author saw parts of earlier findings 2, 3 and 8.
- **Shallow clone:** the checkout holds one commit, so `git show $c:entries/...` returns the current entry. I used `earlier-entry/` as the earlier copy, and could not confirm from history that the claims criteria are unchanged. The earlier record's wording is consistent with them being the same.
- **Other changes:** the changes to `tools/build_osf_targets.py`, `tools/intake.py` and the untracked dotfiles at the repository root were there before this run. I did not touch them.
