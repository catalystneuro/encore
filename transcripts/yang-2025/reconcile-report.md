I wrote the `reconciliation` block in `attempts/yang-2025-02.yaml` and `python tools/entry.py check entries/yang-2025` gives 0 errors. Both notebooks ran cleanly: `reproduce_yang_2025.ipynb` in 561 s and the new `earlier_findings.ipynb` in 127 s. Nothing is committed.

**1. Blind: no (`blind: false`).** In its author-revise-1 run, the author read the first 3000 characters of the earlier attempt's `author-revise-1-report.md`, which was still in `transcripts/yang-2025/`. That text gave some earlier results:
- no outcome changed in its first verification round;
- figs2 matched 21 of 28 groups, with counts of 8 and 20;
- fig5b depends on R7;
- the HFO App repository and commit 1ccff19.

The author said so in that run's report. The transcript then shows a GitHub search for the HFO App. Every outcome had already been set in the author run, and none changed afterwards. The audit's hits in `author-answers*.md` are the earlier attempt's own transcripts (run 42729502254, 10 November), not this attempt's.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Only 600 s clips; no seizure or stimulation times, interictal recordings or durations | still_present | 1 |
| 2 | Baseline clips carry stimulation trains | still_present | 6 |
| 3 | 16 clip names in two groups with different contents; dates out of order | still_present (checked in the notebook) | 8, on_prompt |
| 4 | R5 and R6 stimulation order differs from Figure S2 | still_present | 3 |
| 5 | Clip selection, `-small`/`-large` names, groups under 6 seizures | still_present | 2 |
| 6 | ANT depth DV -5.6 mm against -6.0 mm in the paper; age and weight the same in every session | still_present (checked in the notebook) | 9, on_prompt |
| 7 | Questions for the paper's authors | still_present | 7 |

For finding 3, none of the 16 repeated names holds the same data in its two groups. I gave both added findings `severity: minor`.

**3. New findings:** 4 and 5.

**4. Outcomes that changed** (no outcome was changed):
- **fig2-r1-target-shifts** (earlier partially_reproduced, now reproduced). Cause is `reading`, confidence high: the paper gives no rule for marking seizure onset, and the two attempts chose different ones. I ran a check on R1's 35 baseline seizures:
  - The earlier attempt's onsets fall a median 1.00 s later.
  - With this attempt's onsets, both attempts' GC code give 4 of 4 named nodes.
  - With the earlier onsets they give 2 or 3 of 4.
- **fig3a-some-nontarget-shorten** (earlier partially_reproduced, now not_reproduced). Cause is `reading` (the onset and end rule), confidence high. Both attempts find the same 3 named groups significantly shorter. The difference is R7, over the same 4 seizures:
  - Earlier: R7 CA3 -0.1899 against the R7 ANT target's -0.2561, so less effective (3 of 5).
  - Now: R7 CA3 -0.2258 against -0.1995, so more effective (2 of 5).

  I left `supports` out of both items, because each outcome turns on that unstated rule.

**5. What did not fit**
- **Blindness gap:** `tools/blind.sh hide` moves earlier transcripts only for the author role. The revise runs could see them, and this attempt's same-named transcripts have overwritten the earlier ones in the folder (they remain in git history).
- **Missing earlier entry:** `earlier-entry/` was empty and the clone was shallow. I fetched more history, took the earlier entry from commit e7ed8b71c8e, and re-ran its notebook in a scratch folder (it passed). I emptied `earlier-entry/` again afterwards.
- **Severity:** the protocol asks for `severity` on findings added on prompt, but this record is pilot-14 and its other findings have none.
- **Other changes and files:** `entry.py lock` added `python: "3.13"` to `entry.yaml`. Untracked files I did not create (`.bashrc`, `.idea`, `scripts/` and other dotfiles) are at the repository root; the workflow should not commit them.
