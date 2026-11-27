I've written the `reconciliation` block into `attempts/grosmark-2016-02.yaml` and added `entries/grosmark-2016/earlier_findings.ipynb` to `entry.yaml`. `python tools/entry.py all` passed: both notebooks ran (the main one in 2824 s, the new one in 32 s) and `check` reports 0 errors. Nothing is committed.

**1. Blind.** Yes, `blind: true`. The audit printed four lines. Three are the protocol's own link to the pilot notes, which the author read as part of `docs/protocol.md`. The fourth matched only this attempt's own runner URL inside its record. The transcripts never name `grosmark-2016-01`, `entries/grosmark-2016-000044` or the earlier dataset version.

**2. Earlier findings**

| # | Earlier finding | Status | now | Evidence on 0.261106.0236 |
|---|---|---|---|---|
| 1 | Position rate stored as the sampling period | fixed | | Rates are 39.0625 to 39.0628 Hz, and the samples span the MAZE epoch exactly in all 8 files. |
| 2 | Gatsby_08022013 POST epoch ends at 30413.6 s | still_present | 2 | The new attempt reports the same session and values. |
| 3 | No EMG or accelerometer data | fixed | | `neck_emg` and `accelerometer` are now in every file at 1250 Hz. |
| 4 | Derived data not deposited | still_present | 14 (added, `found: on_prompt`, major) | No events, place cells, scores, PCC values or rigid and plastic labels anywhere. |
| 5 | No analysis code; supplement unavailable | partly_fixed | 15 (added, `found: on_prompt`) | The supplement was read for the new claims file; still no analysis code is linked. |
| 6 | Electrode locations "unknown"; age "/" | fixed | | Electrodes are in CA1 and the shank groups name the pyramidal layer. The 8 "unknown" sites are documented extra sites above CA1. Age is still "/", but the subject description now says the lab did not record it. |
| 7 | Circular-track running direction undocumented | fixed | | The descriptions now say the rats ran toward decreasing position; the samples confirm it (0.522, 0.636 and 0.594 moving lower). |

**3. New findings:** 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 and 13.

**4. Outcomes that changed.** All 11 have `cause: claims_changed`. The earlier attempt used a claims file written without the supplement, so its author chose the place-cell, event, best-of-two-template scoring and PCC methods. Its PCC test flagged 56.1% of cells with every rate map shifted, so that attempt blocked `fig2b-strong-contributors` and the seven claims that depend on it. The new claims file takes its methods from the supplement and lists readings for each open choice.

| Claim | Earlier → now | supports | Confidence |
|---|---|---|---|
| fig1c-post-gt-pre | not_reproduced → reproduced | reproduced | high |
| fig2b-strong-contributors | blocked → not_reproduced | not stated | high |
| fig2-pre-post-overlap | blocked → reproduced | not stated | high |
| fig2d-shuffle-high-dpcc | partially_reproduced → reproduced | not stated | medium |
| fig2e-remove-plastic | blocked → reproduced | reproduced | high |
| figs2-track-distribution | blocked → reproduced | reproduced | high |
| fig3a-plastic-specificity | blocked → partially_reproduced | partially_reproduced | high |
| fig3b-plastic-improve | blocked → not_reproduced | not stated | medium |
| fig4a-rigid-faster | blocked → not_reproduced | not_reproduced | high |
| rate-split-medians | partially_reproduced → reproduced | reproduced | medium |
| fig4d-slow-sequences | not_reproduced → reproduced | not stated | medium |

Where no outcome is stated, the new result turns on an open reading (direction or kernel width), or the two attempts' numbers point opposite ways.

**5. What did not fit the protocol**
- `docs/pilot-notes.md` has no sections for pilot-11 or pilot-15 to pilot-19. For pilot-18 and pilot-19 I relied on `docs/protocol.md`, and the `protocol` note says so.
- For a finding the new attempt did not report, the prompt allows only fixed, still_present or not_checked. Earlier finding 5 was half fixed, so I used `partly_fixed` and added an `on_prompt` finding for the part that remains.
- Finding 5 is about the paper, so it doesn't depend on the dataset version. I checked the code-link part on the dandiset's metadata; the supplement's availability rests on the new claims file's header.
- All the outcome differences come from the claims file being rewritten, which tells you little about how well results repeat between attempts.
- I copied the earlier entry into `earlier-entry/` to read it and emptied it again afterwards.
- `git status` shows untracked dotfiles (`.bashrc`, `.gitconfig` and others), `.idea`, `.vscode` and `scripts/` at the repository root, and the modified `tools/runner/chain.sh`. I did not create or touch any of them, so the workflow may pick them up when it commits.
