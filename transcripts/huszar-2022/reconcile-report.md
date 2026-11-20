The reconciliation block is written in `attempts/huszar-2022-02.yaml`. `python tools/entry.py check entries/huszar-2022` reports 0 errors. Both notebooks pass a clean run: the main one in 2179 s and the new `earlier_findings.ipynb` in 206 s. Nothing is committed.

**1. Blind: yes (`blind: true`).** The audit's only hit (`author.md:3720`) is the runner URL the author wrote into its own record. Nothing shows it saw `huszar-2022-01`.

**2. Earlier findings.** Each unmatched finding was checked on version 0.261113.1035 in `entries/huszar-2022/earlier_findings.ipynb`, which is now listed in `entry.yaml`.

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | No light-responsive labels or pulse times | fixed | |
| 2 | No cell types or waveforms | fixed | |
| 3 | Six mice without units (8,201 units) | fixed | |
| 4 | Only 9 of 16 novel explorations have position | fixed | |
| 5 | Sex differs between files of a mouse | fixed | |
| 6 | `is_familiar_maze` wrong | fixed | |
| 7 | Novel positions in 0 to 1 labelled cm | partly_fixed | 3 |
| 8 | Raw files start on 2011-08-18 | fixed | |
| 9 | LFP of e16_3m1_210201 labelled 30 kHz | fixed | |
| 10 | Units not linked to electrodes | fixed | |
| 11 | Embryonic day only in the subject id | fixed | |
| 12 | Two e13_1f1 sessions without sleep | still_present | 1 |
| 13 | Too few trials per arm; 19 trials without times | still_present | 6 |
| 14 | 92 against 96 sessions | still_present | 7 |
| 15 | e13_26m1 is in both the maze and novel cohorts | still_present | 13 (added, `found: on_prompt`) |

- **Finding 7:** the series are now labelled "n.a." with a "lab's units" description, but the scale is still missing.
- **Finding 11:** I called this fixed, which is a judgement call. The day is still only in the subject id, but the subject description now gives the mapping.

**3. New findings in `huszar-2022-02`:** 2, 4, 5, 8, 9, 10 and 11. Finding 12 is one too.

**4. Outcomes that changed (22 claims).**
- **sessions-durations** (partially reproduced earlier, not reproduced now): `claims_changed`, high confidence. Both attempts have the same numbers. The earlier criterion, written by that attempt's own author, gave the sleep condition no outcome. The reader's criterion makes it part of "reproduced".
- **unit-count** (not reproduced earlier, reproduced now): `dataset_changed`, supports reproduced, high confidence. The new version gives 9,472, 7,411 and 2,060.
- **novel-explorations** (partially reproduced earlier, reproduced now): `dataset_changed`, supports reproduced, high confidence. The open fields now have position, so all 16 explorations count.
- **18 claims blocked earlier for missing labels, cell types, LFP or electrode links** (ed2, fig1e–h, fig2b–g, fig5b–f, fig6e–f, fig7b, fig7ce): `dataset_changed`, high confidence. No `supports` is given; I did not judge the new attempt's analyses.
- **fig7fg-convergence-cofiring** (blocked as `methods_underspecified` earlier, not reproduced now): `dataset_changed`, medium confidence. Both connection detectors find far more connections than the paper's 31,932, so the outcome still turns on how the detector is read.

**5. What did not fit the protocol.**
- `docs/pilot-notes.md` has no section for pilot-11, pilot-15 or pilot-16, so the `protocol` note covers pilot-8 to pilot-14 only.
- The checkout has a single commit, so `git log` cannot recover the earlier claims file. I took the earlier criteria from the first version of that author's claims file in `transcripts/huszar-2022/attempt-01/author.md`; later edits to it may be missed.
- A finding the dataset owners answered with documentation only, like 11, sits between "fixed" and "still present". The status list has no option for that.
- The sandbox left placeholder device files in the repo root (`.bashrc`, `.gitconfig`, `scripts` and others). They show as untracked and should not be committed.
