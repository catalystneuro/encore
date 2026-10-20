I pinned version 0.260728.1352 and ran the entry from a clean environment: it passes in 84 s. The new record is `attempts/001754-knierim-2000-03.yaml` and the handover package is built. `entry.py check` still reports 14 errors, all in the two earlier records, which I left unchanged as instructed (point 4). I did not verify the work, commit or push.

**Version.** 0.260728.1352 is the most recent published version, and the paper cites none. The two older published versions hold the same files. The draft has the conversion fixes but is unpublished, and it changed again after `-02` read it (last modified 2026-10-15 14:09, against 2026-10-14 21:55). So the pinned files are the ones `-01` read, which is why most findings below are "still present".

### 1. Outcomes per claim (earlier outcome from `-02`)

| Claim | Now | `-02` |
|---|---|---|
| flight-spatial-code | blocked: methods underspecified | not reproduced (by a shuffle test the paper doesn't use) |
| si-comparable-to-preflight | partially reproduced: no difference (p = 0.88 and 0.66), but the means are 1.377 and 1.32 against the paper's 1.13 and 1.12 | reproduced (later removed from the record) |
| si-rat1-fd9-vs-preflight | blocked: methods underspecified. p = 0.50 against the preflight ES epoch, 0.0055 against MC | new claim |
| si-rat3-fd4-vs-preflight | reproduced: p = 0.28 and 0.77, both means within tolerance; 11 cells against the paper's 7 | new claim |
| fd4-abnormal-selectivity | partially reproduced: lower than preflight for rat 2 under both readings, not for rat 1 | reproduced (later removed) |
| fig3-stability-across-sessions | blocked: methods underspecified. There are 16 active cells, not 7, so "4 of the 7" can be read as a count or a fraction, and the two give different outcomes | reproduced |
| direction-selectivity | blocked: data missing (no time spent per direction can be built from the position) | new claim |
| theta-normal, ripples-normal | blocked: data missing | blocked: data missing (later removed) |
| three-orthogonal-surfaces | blocked: methods underspecified (both claims it depends on are blocked) | blocked: metadata insufficient |

Five questions for a reader are in the new file `questions/001754.yaml`:
- **Reading M-b:** how to recompute maps when position exists only at spike times and not at all preflight.
- **Which preflight epoch:** each preflight file has one ES and one MC epoch, and the paper doesn't say which it compared.
- **Count or fraction:** how to read "4 of the 7" when there are 16 cells.
- **Pairing Rat3's maps:** how to pair session 2 and session 3 maps, since the file gives no link.
- **Direction-selectivity:** whether the claim can be tested at all with these data.

### 2. Findings of `-02` on the pinned version
- **Shared position trace, presented as each rat's position:** still present. It is partly fixed only in the draft. New here: the trace behaves as Rat2's position in Rat2's flight-day-9 ES window (12 of 28 units). It could not be attributed in Rat2's flight-day-4 window.
- **Position only at spike times, none preflight:** still present.
- **Preflight said to be on a flat rectangular track:** still present here. The draft's description has dropped the sentence.
- **Map smoothing not stated:** still present.
- **EEG reported but absent:** still present. No file name in the NASA record of the study (OSD-968) suggests EEG either.
- **Age, pixel scale and camera view missing:** still present.
- **Rat2's preflight and flight units share no tetrode:** still present.
- The `-01` findings that `-02` saw fixed in the draft are all present in this version and recorded again: `cell_number` does not link maps to units, -999 values and the lost-position bin are undocumented, identical map copies, and spike-time resolution and overlapping epochs.

### 3. New findings
- Every Rat3 flight-day-4 ES map has `cell_number` -1, so its session 2 and 3 maps cannot be paired by cell.
- The files' experiment description puts the rectangular track in the baseline sessions; the paper places baselines in the sleeping pouch.
- Position ends 41 s before the end of Rat3's flight-day-4 MC epoch and 7 s before the end of Rat2's flight-day-9 MC epoch.
- Active-cell counts don't match the paper's (for example 38 against 24 for Rat3 preflight), and the paper's selection is not recorded.

### 4. What did not fit a repeat attempt
- **Earlier records fail `entry.py check`.** It requires every claim in the current claims file to have an outcome in every record of the entry, deprecated ones included. `-01` and `-02` predate the rewritten claims, so `check` (and so `all`) fails on 14 errors there. I ran `run` separately; the tool would need to exempt deprecated records.
- **The repeat-attempt rule doesn't cover a rewritten claims file.** It assumes the claims file is kept and the dataset changed. Here the claims changed and the pinned version is older than the one `-02` read, so "fixed / still present" has to be judged against the draft's state.
- **`-02` no longer lists four of its outcomes.** Its record was later edited to drop four claims, so I compared those against its original outcomes from git history.
- **The pinned version is unclear for a repeat attempt.** The instruction to pin a published version conflicts with the repeat-attempt section's use of the draft, and the protocol doesn't say which takes precedence.
