The new attempt is written and the entry runs from a clean environment (375 s). I ran `entry.py lock`, `run` and `handover`; the handover is in `executed/000582-sargolini-2006/handover/`. `entry.py check` still fails with 18 errors, all about the unchanged `-01` record (see point 4). The new record, the entry and the notebook pass every check. I did not verify my own work, and nothing is committed.

**Version.** 0.251111.2151 is the only published version, and the draft has the same 118 assets, so the pin, the helper constant and the `dandi:` relation stay as they were. The notebook header says why.

## 1. Outcome per claim (earlier outcome in brackets)

"Every reading" means every combination of the readings the claims file names for details the paper leaves open (trials pooled or first trial only, map bin size, how the gridness circle and central peak are cut, significance level).

| Claim | This attempt | Earlier (`-01`) |
|---|---|---|
| layer2-grid | partially reproduced | partially reproduced |
| grid-all-layers | reproduced | not tested |
| gridness-range-similar | blocked, methods underspecified | not tested |
| grid-stable | blocked, methods underspecified | not tested |
| spacing-dorsoventral | blocked, data missing | not tested |
| fieldsize-dorsoventral | blocked, data missing | not tested |
| grid-phase-orientation | blocked, methods underspecified | not tested |
| hd-layers | not reproduced | not tested |
| hd-with-grid-colocalized | blocked, methods underspecified | not tested |
| hd-tuning-breadth-layers | blocked, methods underspecified | not tested |
| hd-full-range | reproduced | not tested |
| hd-colocalized-distributed | reproduced | not tested |
| hd-stable-trials | reproduced | not tested |
| hd-rates | not reproduced | not tested |
| deep-hd-conjunctive | not reproduced | reproduced |
| gridness-hd-continuous | reproduced | not tested |
| conj-tuning-similar | blocked, methods underspecified | not tested |
| cue-rotation-coherent | blocked, data missing | not tested |
| speed | blocked, methods underspecified | reproduced |
| speed-slope-steeper | blocked, methods underspecified (depends on speed) | not tested |
| speed-intercept | blocked, methods underspecified (depends on speed) | not tested |

Where the three earlier claims changed:

- **layer2-grid:** same outcome, different reason. With the paper's criterion (gridness above 0), 62% to 72% of layer II cells are grid cells, above every deeper layer under every reading. But layers III, V and VI come out far above the paper's fractions (for example layer III 0.54 to 0.60 against 0.35). The earlier attempt fell short on layer II itself, using a stricter threshold of its own.
- **deep-hd-conjunctive:** layer II now has 1 to 8 conjunctive cells under every reading, all from rat 11265, and the claim requires none.
- **speed:** counted at P < 0.001 per cell, every reading fails. Counted by positive slope, the readings split between reproduced (54) and partially reproduced (200), and the criterion calls that split methods underspecified.

I added five questions to `questions/000582.yaml`:
- what "a peak's centre" and "a peak's radius" mean; I ran both centres;
- which angular standard deviation the paper used;
- how to read the speed criterion's two conflicting rules;
- whether conjunctive cells count as head-direction cells in hd-with-grid-colocalized;
- which rats' pairs the orientation test compares against.

## 2. Earlier findings

The data are unchanged, so:
- **Enclosure size stated as 1 x 1 m:** still present (22 files span 150 or 200 cm).
- **Description says two LEDs:** still present (47 of 118 files have one; rat 11084 has files of both kinds).
- **No identifier links a cell across files:** still present (99 apparent cells recur in 2 to 7 files).
- **Undocumented selection:** still present, now measured against the paper's table S1: 620 cell-sessions against 627 cells, 15 rats against 17, 71 layer II cells against 108.
- **Methods unavailable:** partly fixed. The supplement was supplied for this attempt, but the dandiset gives no analysis parameters and no code is public.

## 3. New findings

- **Positions are rescaled without saying so.** Every file spans exactly 100, 150 or 200 cm. The 19 circular files at 200 cm are likely the paper's 180 cm circle, about 11% too large.
- **Two trials are joined in the 20-minute files.** Those 23 files hold two trials joined near 600 s, and there is no trial table.
- **Distance from the postrhinal border is missing.** The `depth` column is the depth the electrodes were lowered to.
- **No labels for enclosure, condition or cue-card position**, so the cue-rotation trials cannot be found.
- **Missing cell metadata:** 6 cells have no layer, 36 no depth and 230 no hemisphere.
- **Descriptions contradict the files.** They say "grid cells", or "conjunctive and head-direction cells of layers III and V"; the files hold all cell types from layers II, III, V and VI.
- **The red LED is not identified.** The SOM tracks position from the red LED, and nothing says which LED that is.

Spikes and positions share a clock: both test measures peak at zero time shift for 29 and 28 of 30 cells.

## 4. Where the protocol did not fit a repeat attempt

- **`entry.py check` fails on the kept record.** It requires every record naming the entry to have an outcome for every claim. It does not skip deprecated records, so the unchanged `-01`, which has only 3 of the 21 claims, fails the check. Either the tool should skip deprecated records or the protocol should say how a kept record meets this.
- **Re-checking earlier findings is awkward.** The finding schema has no field for whether an earlier finding is fixed, so I put the status at the start of each statement. And with no new version to test, a repeat attempt can only re-confirm the earlier findings.
- **The dependency rule hides results that ran.** It blocks speed-slope-steeper and speed-intercept because speed is blocked, although their analyses ran and give the same outcome under every reading (partially and not reproduced). The block on speed comes from its counting rule, not from the regressions they use.
- **Several claims will block on wide reading combinations.** Many criteria give 32 to 64 combinations of readings and require all to agree. Eight claims are blocked as methods underspecified for that reason, so the questions decide much of this attempt.

One unrelated thing: untracked entries such as `.bashrc`, `.idea` and `scripts` now appear at the repository root. They are sandbox device files, not files I wrote, and should not be committed.
