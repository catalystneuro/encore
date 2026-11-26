The reconciliation is written and `python tools/entry.py check entries/pasquereau-2013` reports 0 errors. I changed nothing the blind attempt recorded and committed nothing. Both notebooks in the entry ran from a clean environment and passed (851 s and 193 s).

**1. Blindness.** `blind: true`. The audit found four lines, all in `author.md`: two links to the README and pilot notes, the README text itself, and the attempt's own runner URL inside its record-writing script. None of them points at an earlier attempt's results. The author's report says it came across no earlier attempt. It did see a header in the claims file mentioning an earlier data check and "repeated files". The protocol allows the author to keep the claims file, so I did not count that against blindness.

**2. Earlier findings (pasquereau-2013-02)**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Leu files have no perturbations | still_present | 1 |
| 2 | Three torque command pulse sizes, split by MPTP state | still_present | 3 |
| 3 | Leu analog stored at 100 Hz (paper says 200 Hz); EMG in arbitrary units | still_present (checked in `earlier_findings.ipynb`) | 8 |
| 4 | Torque onset a fixed delay after the centre target appears | still_present | 7 |
| 5 | Response detection gives a false-positive rate of 0.23; no code published | still_present | 5 |
| 6 | Resting rates differ between text and Table 1; Table 1's CSN chi-square gives p = 0.54 | still_present (checked) | 9 |
| 7 | v1401, v1402 and v1501: 51 labelled perturbations, no pulse in the command | still_present (checked) | 10 |
| 8 | Conversion code not on main of turner-lab-to-nwb | fixed (checked) | – |

- **Finding 8:** https://github.com/catalystneuro/turner-lab-to-nwb/pull/33 was merged at 15:55 UTC on 2026-11-24. The version was published at 19:06 UTC the same day, and main now contains the merge commit.
- **Findings 3, 6 and 7:** these were added to the record as findings 8, 9 and 10, with `found: on_prompt`. Each has a tagged cell in the new notebook `entries/pasquereau-2013/earlier_findings.ipynb`, which is now listed in `entry.yaml`. The lock file did not change.

**3. New findings.** 2, 4 and 6. Finding 4 is the attempt's list of checks that passed (severity none).

**4. Outcomes that changed.** None. All 28 claims have the same outcome in both attempts, so there is no `outcomes` list. The measured values differ slightly in a few places, for example kinematics 28.11/14.56 against 28.1/14.8, and EMG duration 24.6/49.4 against 22.2/51.5.

**5. What did not fit the protocol**
- **Missing pilot notes:** `docs/pilot-notes.md` has no sections for pilot-15 to pilot-19; the last one is pilot-14. For pilot-18 (findings rated by severity) and pilot-19 (a critical or major finding names the cell that shows it), I worked the changes out from `docs/protocol.md` and `tools/entry.py`. The `protocol` note says this, and that no outcome moved.
- **Only one `now` per finding:** earlier finding 5 covers two problems, the false-positive rate and the undefined single-trial latency. This attempt splits them into its findings 5 and 6, but `now` takes one number. I pointed it at 5 and named 6 in the note.
- **Finding 8 needs live GitHub data:** its notebook cell queries the GitHub API each time it runs, so its output reflects the repository as it is at that moment.
