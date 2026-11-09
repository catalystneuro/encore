# Verifier report, round 2: Tian et al. 2025 on DANDI:001559 v0.250902.2058

The claims file lists 21 claims, and the attempt record gives an outcome for each of them (6 from Figure 4, 15 blocked as data_missing). Cell numbers below refer to the re-executed notebook, which is numbered differently from the one I saw in round 1. This time I also looked at the figures embedded in cells 26, 29 and 40. The claims file reads the paper correctly for Figure 4: I checked its Results paragraph 1, the Figure 4 legend and the Methods, and found no misreading.

## 1. Outcomes and assumptions

| Claim | Record | Agree? | Note |
|---|---|---|---|
| fig4b-expression-healthy | reproduced | yes | Cell 26 shows many labelled somata. A few branching processes are visible from bright cells (for example, lower right). "Three months" is correctly reported as not shown. |
| fig4c-speckle-responsive-region | blocked, metadata_insufficient | yes | Cell 7 confirms no file has stimulus times. The time course is correctly labelled "a partial look, not a test". |
| fig4d-steady-baseline | partially_reproduced, assumed | yes | The assumption is stated and reasonable. It is not actually decisive: in cell 36, 14:50 fails and at least two recordings pass under all 12 combinations of pairing and window. |
| fig4d-evoked-increase | blocked, methods_underspecified | yes | Cell 39 shows the readings disagree, which is the case the criterion assigns to methods_underspecified. This outcome rests on one condition per session, but it is not flagged `assumed: true` (see below). |
| fig4d-4ma-single-trials | blocked, methods_underspecified | yes, changed from round 1 | In round 1 I gave reproduced (conditional). The claims file lists the claim as depending on fig4d-evoked-increase, and the record applies the protocol's rule that such a claim is blocked with its parent. The protocol isn't in my materials, so I take the rule as the record quotes it. The notes report the test as it ran. |
| fig4d-electrode-timing | blocked, methods_underspecified | yes, changed from round 1 | Same reasoning as the claim above (in round 1 I gave partially_reproduced). |
| The 15 claims for Figures 1–3, 5, S2, S3 and Table S1 | blocked, data_missing | yes | No such data are in the 35 files (cells 3 and 7). |

**The unflagged assumption.** The fig4d-evoked-increase outcome depends on each session being one condition. That is stated only as a deviation, not flagged `assumed: true`. It matters because of session 15:04. Cell 34 itself notes that 15:04 splits into five trials at −2.0 to −0.3 and five at 2.9 to 7.5, "which a mix of two electrodes or failures of response could both give". If 15:04 were a mix of two conditions, the per-condition tests would change, and the outcome could change with them. This outcome should be marked `assumed: true`.

## 2. Statements the printed numbers do not support

- **README line 30:** "It takes about nine minutes". Cell 51 prints "notebook ran in 11.3 min".
- **Cell 12:** "at irregular intervals of 12.3 to 56.5 s". Cell 11 prints a shortest interval of 12.20 s and a longest of 56.58 s.
- **Cell 37:** "at most 6.64 against 14.13 or more, in both channels and both windows". The channel 3 window b reference in cell 36 is 13.60. The outcome is unaffected.
- **Cell 45 and the record's notes for fig4d-4ma-single-trials:** "The single-pulse variant does not show responses to individual pulses". This holds for channel 4 only. In channel 3, cell 44 gives per-trial p = 0.023 for 145933 (an assumed 4 mA session) and p = 0.039 for 145053. The variant does not decide the claim.
- **Cell 30:** "three times in 12:49 (0.9% to 2.6%, at about 27.5, 41.6 and 99.6 s, the same times in phases 2 and 3)". The 0.9% comes from phase 1, whose episodes are at 27.5, 60.3 and 99.6 s, not those times.
- **Record notes for fig4c-speckle-responsive-region:** "the spectrum between 2 and 33 s peaks at 30 s". 30 s is the longest-period bin in that band, so this describes a red spectrum, not a 30 s rhythm. Cell 30 says "its longest period"; the record drops that qualifier.
- **Cell 0:** "The draft has the same 35 assets and the same size … last modified at publication time" and "the only published version". **Cell 4:** "The archive's summary says one subject". No printed output shows any of these.

Every other number in the five "**Result:**" cells (27, 30, 37, 41, 45, 49), the Summary (cell 52), the README and the record's notes and findings matches the outputs. I checked them against cells 11, 13, 26, 29, 33, 36, 39, 40 and 43–48.

**My round-1 reasons in the record:** they are stated in my words. The record also adds relevant points from my problem list to the reasons for fig4c, steady-baseline, evoked-increase and electrode-timing, and represents each of them correctly.

## 3. Round-1 points

**Resolved:**
- **Point 1 (rise time of 150418):** cell 48 prints the traces around onset and two other ways of measuring the rise. 15:04's early "rise" is a step at onset. The 2 mA result is the same under all three measures in both channels.
- **Point 2 (steady baseline):** cell 36 adds straight-line trends, and the day-long rise is now stated.
- **Point 4 (speckle):** cell 29 reads every frame (1079 to 1465 per exposure phase, matching the frame counts in cell 3).
- **Point 5 (baseline s.d.):** cell 43 adds a variant without the last 0.5 s; every 4 mA fraction stays 1.0.
- **Point 6 (channel 3 count):** now in the record.
- **Point 7 (processes):** the processes are visible in cell 26.
- **Point 8 (pixel size):** now a finding.
- **What I could not check in round 1:** the images, the 150418 trace around onset, the per-trial order and the speckle time course are now all available. Cell 7 lists the groups of all 35 files.

**Partly resolved:**
- **Point 3 (one condition per session):** cell 33 now prints the trials in order. No alternation or blocks appear (Mann-Whitney p 0.31 to 0.89). That is consistent with one condition per session but does not show it.

**What remains that bears on a conclusion:**
1. **The session-to-condition assumption** is still unverifiable, and 15:04 is bimodal. This bears on fig4d-evoked-increase, which should be flagged `assumed: true`, and through it on both claims that depend on it.
2. **The 15:04 "earlier rise" starts before onset.** Its smoothed trace crosses half its peak at −0.23 s, and the unsmoothed average is already 0.77 above baseline in the second before onset (cell 48). If fig4d-evoked-increase were ever unblocked, the 2 mA timing result would rest on a session whose early rise is partly not stimulus-locked. The record says this; it does not change the current outcome.
