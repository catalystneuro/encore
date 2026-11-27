I've written the `reconciliation` block in `attempts/mah-2023-02.yaml` and the new notebook `entries/mah-2023/earlier_findings.ipynb`. The full entry ran cleanly (all four notebooks pass, the new one in 874 s) and `python tools/entry.py check entries/mah-2023` reports 0 errors. Nothing is committed.

## 1. Blind

`blind: true`. The audit's hits are links to the pilot notes and README text, the attempt's own provenance, and tool code. The author also noted that the `pre-cue-session-link` criterion says "Written after a first look". That text is in the claims file, which the author is allowed to keep, and it contains no earlier results.

## 2. Earlier findings

| Earlier | Status | Now | Evidence |
|---|---|---|---|
| 1. Only sessions that pass the inclusion criterion are deposited, and nothing says so | still_present | 1 | Same problem |
| 2. Nothing marks the pre-cue sessions | still_present | 2 | Only the undocumented `center_port_cue` marks them. That field was already in the earlier version, so "nothing marks" was too strong |
| 3. L011 session deposited twice | fixed | | The `-x` copy is gone and no session is held twice |
| 4. No catch probability in the processed table | fixed | | All 23,033 files have `catch_percentage` |
| 5. Raw and processed `is_catch` differ, undocumented | fixed | | They still differ (176,006 trials), but both descriptions now explain the difference |
| 6. No subject age | still_present | 11 | 16 rats have only P6M/P24M. The other 275 have a date of birth, as they already did in the earlier version |
| 7. Catch probability 0.3 in 8 rats | still_present | 4 | Same 8 rats |
| 8. Model fitting code not public | still_present | 8 | Same questions |
| 9. Equation 6 gives H0, the code uses H0/2 | still_present | 12 | Code unchanged |
| 10. Figure5.m has 16 rats and 20 dates | still_present | 13 | Code unchanged. The cue flags fit the in-order pairing within a day for 9 of the 12 rats with earlier sessions, but not for E005, S042 or S050 |
| 12. Scaling in `myTauShuffleTest.m` | still_present | 14 | Code unchanged. The current-offer coefficient is 0.211, so 2.108 after the ×10 scaling, above the bound of 1 |

Findings 11 to 14 were added with `found: on_prompt`; finding 11 has severity minor.

## 3. New findings

3, 5, 6, 9 and 10.

## 4. Outcomes that changed

| Claim | Earlier → now | Cause | Supports |
|---|---|---|---|
| fig2k | reproduced → partial | error, earlier attempt (high) | partially_reproduced |
| fig2l | reproduced → partial | error, earlier attempt (high) | partially_reproduced |
| fig3j | blocked → reproduced | reading (medium) | reproduced |
| suppfig8 | blocked → reproduced | reading (medium) | not given; the result changes with the seed |
| fig4a, fig4c, fig4d | blocked → partial / reproduced / reproduced | error, earlier attempt (medium) | not given |
| fig5b | reproduced → partial | reading (high) | not given |

- **fig2k and fig2l:** for the Methods' reading, the earlier code kept each session's first trial, which is timed from session start, and gave it the previous day's last offer. Those long times flip the sign of the result; removing them gives this attempt's direction.
- **fig3j and suppfig8:** the earlier attempt kept the Methods' 100 random starts and blocked as too large (estimated 3.3 h). This attempt fitted from 2 starts in a separate notebook.
- **Figure 4:** the earlier attempt recorded `data_missing` without reading the paper's Zenodo `A_Structs_all`, which is public.
- **fig5b:** the difference is where the 99th-percentile cut is taken: over the pre-cue sessions (as `iti_by_reward.m` does) or over all of a rat's sessions. That choice alone creates the 5→10 uL rise.

## 5. Where the protocol did not fit

- **Pilot notes:** `docs/pilot-notes.md` has no section after pilot-14. I took the pilot-15, 17 and 18 changes from `docs/protocol.md` and `tools/entry.py`; I found nothing for pilot-16. None of these changes explains a differing outcome.
- **Earlier entry from git:** the history has a single commit, so `git show $c:entries/...` returns the new entry. I used `earlier-entry/` instead.
- **No cause for a different handling of the time limit:** fig3j and suppfig8 are recorded as `reading`, but the paper does fix 100 starts, so that label is approximate.
- **Lock not re-run:** `requirements.in` is unchanged and the check passes. Re-locking could have changed the package versions under the blind attempt's notebooks.

The working tree also has changes I didn't make: modified `tools/intake.py`, `tools/notify.py` and `tools/build_osf_targets.py`, and untracked dotfiles, `.idea`, `.vscode`, `.mcp.json` and `scripts`. These should be kept out of the workflow's commit.
