I've written the reconciliation into `attempts/markowitz-2023-02.yaml`, and `python tools/entry.py check entries/markowitz-2023` passes with 0 errors. The new notebook `entries/markowitz-2023/earlier_findings.ipynb` is listed in `entry.yaml`. The lock file did not change, and the full run passed: photometry.ipynb took 2794 s, optoda.ipynb 649 s and earlier_findings.ipynb 109 s. Nothing is committed.

**1. Blind.** Yes, `blind: true`. The audit's four hits are the GitHub Actions runner URL, which contains "catalystneuro/encore", and the repository README's link to encorescience.org. No author transcript mentions `markowitz-2023-01`, `attempt-01` or `earlier-entry`. The author did read the dataset's own release notes, which say the catch trials and the dLight-only mouse labels were fixed. Those are the dataset's public text, not the earlier attempt.

**2. Earlier findings**

| # | Earlier finding | Status | now |
|---|---|---|---|
| 1 | Catch trials not marked | fixed (601 of 604 stimulation files now have catch detections, 21740 of 77405) | |
| 2 | Genotype and opsin not stated | fixed (one snc-eyfp mouse, 3155, says its genotype is not in the source) | |
| 3 | Session type and number not stored | fixed (a TargetSessions table now stores them) | |
| 4 | 635-nm stimulator listed for the Ai32 mice | fixed (470 nm) | |
| 5 | dLight-only mice described as Ai32 | fixed (now C57BL/6J) | |
| 6 | Syllable timestamps not ascending | fixed | |
| 7 | Mouse 3155 files store every frame twice | fixed | |
| 8 | 14 empty syllable series | fixed | |
| 9 | dLight+ChrimsonR sessions missing, fewer DLS experiments | still_present | 1 |
| 10 | Food-reward sessions missing | still_present | 1 |
| 11 | Unflagged behaviour-only and failed sessions | still_present | 2 |
| 12 | z-scored dLight trace not stored | still_present, added as `found: on_prompt`, severity minor | 15 |

**3. New findings.** Findings 3 to 14 of `markowitz-2023-02` are new; no earlier finding points at them. Finding 15 is the one I added for earlier finding 12.

**4. Outcomes that changed (12 claims)**
- **Criteria changed (`claims_changed`, 9 claims).** The claims file was rewritten by a separate reader, so the criterion differs:
  - fig1l: the forest now has to be the paper's 1,000 trees with 100 shuffles, so it is blocked as too large.
  - fig2e: the paper's segments and a z-scored null.
  - ed7-dms-no-usage-prediction: now depends on an encoding model that was not run.
  - fig3e and fig3f: the baseline day is now the day before stimulation, where it was a Monday.
  - fig3h: the controls must now not be significant, and in both attempts they are, so the evidence supports `partially_reproduced`.
  - fig1f, fig2k and ed10d: the earlier claims file gave them no criterion and that attempt did not run them, for time.
- **Dataset changed (`dataset_changed`, 3 claims).** fig3i, fig3l and fig3m became testable once catch trials were marked. The evidence supports `reproduced` for fig3l and `not_reproduced` for fig3m.
- **A bug in the blind attempt's Monday variant.** The fig3e/fig3f Monday variant in `optoda.ipynb` cell 4 (`target_table`) searches only the target's own baseline rows, so it does not test the code's rule. A diagnosis agent re-ran the earlier selection on the new files: the Monday rule gives U = 198 and the day before gives U = 151. This bug is in a variant only, not in the outcome.

**5. What did not fit the protocol**
- **No pilot notes for this span.** `docs/pilot-notes.md` has no entries for pilot-11, pilot-15 or pilot-16, so the `protocol` text covers only pilot-8 to pilot-14.
- **The earlier claims file is not in the history.** The history is squashed to one commit, so I took the earlier criteria from the Write call in `transcripts/markowitz-2023/attempt-01/author.md`.
- **No cause fits "not attempted, for time".** I used `claims_changed` for fig1f, fig2k and ed10d.
- **Rule for a direct check that is only partly fixed.** The step-2 rule for a directly checked finding has no way to mark it partly fixed without a matching finding in the new attempt. So I marked 2 and 3 as fixed and put the leftovers in the notes.
- **Possible problem not recorded as a finding.** While checking finding 3 I found 23 files with no light pulses whose TargetSessions gives a stimulation session number (1 or 2). It is a different problem, so it is only in the note.
- **Severity.** The blind attempt's findings have no `severity`, because it ran under pilot-16. Only the finding I added has one.
