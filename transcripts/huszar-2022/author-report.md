The attempt is complete: the entry is at `entries/huszar-2022`, the record is `attempts/huszar-2022-02.yaml`, and the handover package is built. `check` passes with 0 errors, and the last clean `run` passed in 35.8 min with 1.05 GB peak memory. Of the 44 claims, 18 are reproduced, 9 partially reproduced, 6 not reproduced and 11 blocked.

**Earlier attempt seen by accident.** The release notes of dandiset version 0.261113.1035, which I read to choose the version, say the conversion "fixes problems found by a reproduction attempt (issue #83)". They list the fixes: left and right arms were swapped, ripple maps were shifted by a row, the `light_responsive` column was added, and others. I did not look up the issue or anything else.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cohort-birthdates, st1-animal-sessions, unit-count, ed2-light-responsive-count, spwr-duration | reproduced (counts exact: 17 mice, 96/104 sessions, 7,411 pyramidal cells, 664 light-responsive) |
| sessions-durations | not reproduced: two sessions have no sleep states; median 309.9 min and range 113.7–475.6 min hold |
| fig1e, fig1g, fig2b, fig2f, fig2g | reproduced |
| fig1h (burst index) | partially reproduced: shape and test hold, medians about 25% low |
| fig2c, fig2d, fig6c-theta-rate, fig6d-rate | reproduced, resting on an assumed theta channel |
| fig1f (REM shift) | not reproduced (slope −2.05 %/day, p = 0.16), assumed theta channel |
| maze-cohort, novel-explorations, fig5f, fig6f | reproduced |
| maze-task | not reproduced (30 of 57 sessions have ≥10 trials of each type) |
| fig5b, fig5c, fig5d, fig5e | partially reproduced |
| fig6d-info, fig6e | partially reproduced (open fields left out) |
| fig6c-novel-ratemap | not reproduced (p = 0.75; open fields left out) |
| fig7b, fig7ce | partially reproduced, assumed connection detector |
| fig7d, fig7fg | not reproduced, assumed connection detector |
| ed1, fig1c (histology), ed2-waveform, ed10 (via its dependency), ed5 (no L-ratio) | blocked: data_missing |
| fig3c, fig3e, ed6, ed7, fig4d | blocked: too_large (1 ms ICA matrix about 9 GB for a median session; not attempted in chunks) |
| ed3-depth-control | blocked: other (not reached in the time) |

## 2. Dataset, assumptions and questions

**Pinned version.** I pinned 0.261113.1035, the latest published version. The paper cites none, and the earlier version lacks the light-responsive labels, the pulses and LFP for most sessions.

**What matches the paper.** The files give the paper's counts exactly:
- mice, sex and birthdate;
- every row of Supplementary Table 1;
- 7,411 / 1,556 / 504 cell types and 664 light-responsive cells;
- the per-session labelled fractions;
- all pair counts (3,751 / 50,461 and 2,609 / 39,965) and 184,230 possible pyramidal-interneuron pairs.

**Problems found in the files:**
- Sessions e13_1f1_200305 and e13_1f1_200307 have wake only in their sleep states.
- In e16_3m2_211211, the position series named for the `linear_manu` subsession lies inside the `openField_thomas` subsession.
- Open-field positions have no spatial scale.
- The units table has no L-ratio.
- Two mice the paper says had one light-responsive cell per session have 1 and 2 same-birthdate pairs.
- 27 of 57 familiar-maze sessions have fewer than ten trials of one arm.
- The paper's "92 sessions" disagrees with its own 96 (recorded as a finding about the paper).

**Assumptions**, each recorded with a question for the paper's authors:
- **Theta channel.** I used the channel with a positive sharp wave and the most ripple power. None qualified in 62 of 104 sessions, so the pyramidal-layer channel was used there.
- **Connection detector.** The tested lags, hollow fraction and Bonferroni count are my choices. It finds 50,618 connections against the paper's 31,932.
- **Burst index.** The ACG the paper used is not fully given, which may explain the 25% gap.

No questions were put to a reader.

## 3. Protocol points

1. In the claims file, the per-mouse numbers of `st1-animal-sessions` are in the table's row order, while the mice are named in birthdate order. I read the row order from the table image and recorded it as a deviation.
2. The criterion of `sessions-durations` has no partial outcome for "all holds but the sleep condition". I applied it literally (not reproduced) and explained in the notes.
3. Claims skipped for time but not stopped by computation (ed3) have no fitting `blocked_by`. I used `other`.
4. The rule "a claim depending on a blocked claim is blocked for the same reason" made ed10 `data_missing`, although part of it could be computed from the stored waveforms. I said so in the notes.
5. There was no rule for a monosynaptic count far from the paper's. The chance-level rule covers only false-positive rates, so I tested the claims under a stated assumption.
6. Each edit to the entry forces a full 35-minute re-run, even for text-only edits. I ran it three times; the outputs were identical each time.

## 4. Runtime and failures

The run took about 4 h 10 min, 04:31 to 08:39 UTC; the notebook alone takes about 36 min. Nothing failed.
