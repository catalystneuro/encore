I've done steps 1 to 6 for malfatti-2026 on DANDI:002056 version 0.261113.1541. That is the only published version, and the draft has the same 566 assets and size. Of the 34 claims, 8 were tested and 26 are blocked. `entry.py all` passes (0 errors, notebook 672 s, peak memory 3.4 GB), and the handover is built in `executed/malfatti-2026/handover/`. Nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1fh-no-genotype-effect-learning | Reproduced (genotype p 0.84, 0.84, 0.58; lowest under any reading 0.141) |
| fig1fh-session-effect | Reproduced (session F 9.57, 7.86, 6.30 against the paper's 9.525, 7.571, 5.536) |
| prehension-overlap | Partially reproduced (failed overlaps more than successful in every session, but at most 1 of 10 values is within tolerance) |
| fig4b-clz-improves-success | Reproduced (Cre+ CLZ against saline p = 0.011; controls p = 0.62) |
| fig4d-theta-genotype | Not reproduced (theta genotype p 0.17 to 0.48 across all 12 readings) |
| fig4e-high-theta-accuracy | Not reproduced (accuracy p 0.12 to 0.74) |
| fig4fh-gamma-session13 | Partially reproduced, `assumed: true` (rests on the realignment below) |
| supfig7-lfp-nonprehension | Not reproduced (interaction significant in at most 2 of 7 bands) |
| 21 calcium imaging claims | Blocked, `too_large` |
| supfig1-cfos-validation, fig5b, fig5d, fig5gh, fig5i | Blocked, `data_missing` |

The imaging claims need CNMF-E traces, and the dandiset holds only 89.4 GB of raw AVI video. Streaming that alone takes about 27 min at the measured 56 MB/s, before decoding, motion correction, CNMF-E and cell matching across sessions.

## 2. Dataset, assumptions and questions

What the dataset holds:
- **Critical: duplicate session.** In all 13 behaviour-only mice, the session 6 file holds the same tracking as session 5. The Methods put both halves of the fifth session in one recording, so I split session 5 at 300 s and dropped the copy. That leaves 10 distinct sessions where the paper has 11.
- **Critical: duplicate video.** Miniscope mouse 67111's two session 2 trials hold the same behaviour video, tracked twice, each with a different imaging recording.
- **Critical: LFP clock offset.** For four control mice (69107, 69109, 69110, 69204), the LFP potential locked to prehension onset sits about 8 s before the tracking onsets. Nothing in the files shows this. The other seven mice show it at lag 0.
- **Major: LFP scale.** Values labelled volts are microvolts or amplifier units. Mouse 67584 is on a scale 4 to 60 times the others.
- **Major: sex.** Every file says female. The Methods say the miniscope mice were male.
- **Major: data missing.** The dandiset has no extracted imaging data, no histology and no caspase-ablation group.
- **Minor:**
  - one file gives genotype "unknown";
  - the miniscope group has 7 mice where the paper analysed 6, and it isn't said which;
  - the LFP group has no session 7;
  - 67314's session 1 has only 20 s of tracking.

Assumptions:
- For the LFP claims I adopted the four offset mice realigned by their estimated lag, with 1 s windows and per-bin normalisation. Every result is also shown as deposited.
- Only fig4fh changes with that choice: as deposited it would be not reproduced.

Two questions for the paper's authors are recorded as `methods_unavailable` findings: the spectrogram window and the "cumulative mean" normalisation, and whether the LED alignment of the four offset mice matches the files. I asked no reader questions.

## 3. Protocol points

1. The protocol lets a critical or major finding name the notebook cell that shows it, but the attempt schema rejects `notebook` and `output` on findings. I removed them.
2. It doesn't say what to do when a data defect (the clock offset) can be corrected only by an estimate. I treated the correction as a step 1.6 reading and marked the one outcome that depends on it as assumed.
3. The Methods' "cumulative mean" can be read literally as a running mean, which the claims file didn't list. I added it as a reading, citing the passage.
4. R is not available, so nparLD can't be run. I implemented the ANOVA-type statistic in Python, checked my mixed ANOVA against pingouin, and recorded both as deviations.
5. fig4b's criterion names session 7, which isn't deposited. I used sessions 8 to 13 and recorded it as a deviation.
6. The dandiset holds one LFP channel per mouse, so the claims file's channel reading has only one answer.

## 4. Runtime and failures

The run took about 1 h 31 min (04:48 to 06:19 UTC). Two development runs failed because the column names `norm` and `align` clashed with pandas DataFrame methods; I fixed both. The final runs had no failures. The untracked dotfiles at the repository root (`.bashrc`, `.idea` and so on) are sandbox device mounts, not files I created.
