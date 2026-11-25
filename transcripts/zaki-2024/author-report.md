I finished steps 1 to 6: the entry is at `entries/zaki-2024`, the record is `attempts/zaki-2024-02.yaml`, and there is a new question for a reader in `questions/zaki-2024.yaml`. `python tools/entry.py all` passes with 0 errors, and I built the verifier's package with `handover`. I did not verify my own work and committed nothing.

On blindness: the claims file's header already describes some of what an earlier author saw in the data. It gives the four ensemble sizes, version 0.260825.1902 and Ca_EEG3-4's Recall2 freezing of 15.1%. That is the only earlier-attempt information I came across. I looked at no other attempt, website, issue or pull request.

### 1. Outcomes

| Claim | Outcome | Basis |
|---|---|---|
| source-data-link | reproduced | Both mice and both shock groups match the paper's source data. All 4 freezing values are within tolerance under both readings; reading (b) equals the source data to two decimals for Ca_EEG3-4. |
| ed9b-aversive-freezing-high-vs-low | reproduced | 64.1% against 8.8% freezing; the high-shock mouse froze more in 10 of 10 30-s bins (Mann-Whitney p = 1.8e-4). One mouse per group. |
| offline-bursts-above-shuffle | not_reproduced | In all 3 recordings the true burst rate is below the surrogate mean (8.73 vs 10.94, 6.42 vs 8.81, 5.31 vs 8.48 per min). Same under all 5 seeds. |
| offline-skew-above-shuffle | reproduced | True skew is above all 1000 surrogates in all 3 recordings, under all 5 seeds. |
| burst-locomotion-pause | not_reproduced | No drop in movement before bursts under either time-zero reading (one-sided p 0.45 to 0.92). |
| fig5c-wake-overlap-neutral-coburst | partially_reproduced | Counting wake alone: overlap-neutral 33.3% against overlap-aversive 29.2%, McNemar p = 1.0. Counting wake plus quiet wake, the order reverses (25.9% against 35.3%). |
| 4 claims on this cohort | blocked, data_missing | fig5c sleep and low-shock claims, ed9c, ed9-ed10 |
| 16 claims on other experiments | blocked, data_missing | None of those mice are in the dataset. |

### 2. Dataset, assumptions, questions
- **Clock offset (major):** in Ca_EEG2-1, the behaviour sessions' timestamps run about 1 h ahead of the offline recordings and telemetry.
  - The telemetry drops out (mouse off its receiver) about an hour before each behaviour timestamp, and is normal during the FC timestamp itself.
  - The offline file's EEG equals the Week file's EEG exactly from the epoch start, so those two share one clock.
  - As timestamped, the first offline recording "after FC" starts 47 min before FC.
- **Undefined sleep state (major):** "quiet wake" has no definition and the paper has no such state. 61 of 87 bursts fall in it, and it flips the Fig. 5c comparison.
- **Missing data (major):** 2 of 9 mice are deposited, and 1 of 24 offline recordings for Ca_EEG2-1. Ca_EEG3-4 has no cell registration, and there are no NREM or REM epochs.
- **Minor:**
  - Telemetry is stored at 500 Hz, where the Methods say 100 Hz.
  - The shock amplitude in the FC descriptions has no unit.
  - The Week file's start time is local time labelled as UTC.
- **Checks that passed:** ensemble sizes are 97/80/166/282, no recording is deposited twice, and the 3 files changed since 0.260825.1902 hold the same values in every array used here.
- **Assumption:** circular-shift offsets are drawn uniformly over the whole recording, stated as a standard choice. No outcome is marked `assumed`.
- **Question for a reader and for the authors:** the criterion re-z-scores the shuffled trace before counting bursts, but the ED3l legend does not say this. The other reading, thresholding at the true trace's own z = 2 level, gives the opposite outcome; I show it as a variant. The paper's analysis code is still not public (404).

### 3. Protocol points
1. The claims header carries an earlier author's data-check facts into a blind attempt. I said so here.
2. The suggested clock check (decoding task variables around trial starts) does not fit offline imaging. I used lagged correlations and sleep labels shifted in time. The imaging and telemetry clocks were found consistent but could not be shown to match, and I said so on the locomotion claim.
3. The severity table puts "events on different clocks" under critical, but here the contradiction can be seen in the files and it is unclear which clock is right. I rated it major.
4. A method the criterion fixes but the paper does not state fits neither the "ask a reader" nor the "ask the authors" route cleanly. I did both.
5. The variant's random generator uses seed + 1, while the five-seed sensitivity runs use + 1000 to + 4000.

### 4. Runtime and failures
- The notebook runs in about 3 min with 0.87 GB peak memory; the whole session took about 35 min (03:35 to 04:10 UTC).
- Two bugs found during development were fixed before the final run: the 30-s bins came out as 9 instead of 10, and an array-length mismatch in the duplicate check. Nothing else failed.
