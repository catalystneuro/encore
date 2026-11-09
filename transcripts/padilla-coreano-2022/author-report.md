I've finished steps 1 to 6 for DANDI:001749: 6 of the 46 claims could be tested and all 6 reproduced; the other 40 are blocked. The entry passes `lock`, `check` and `run` (the notebook takes 550 s), and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| ed5b: rank 1 mice win the most competitions | reproduced: rank 1 won 10 of 11 (90.9%). Competitions per rank are 12, 11, 15, 15 against the paper's 12, 12, 15, 14. |
| ed5c: dominants and subordinates get similar rewards | reproduced for the rewards part (p = 0.505 over 34 files, 0.498 over 20 sessions). The body-weight correlation cannot be tested: there are no weights in the dataset. |
| ed5d: subordinates are slower to the reward in win trials | reproduced from port entries (median 1.47 against 1.01 s, rank-sum p = 0.0196). From the hand-scored labels the direction is the same but not significant (p = 0.206). |
| ed5e: port occupancy does not differ by rank | reproduced (p = 0.327 over files, 0.284 over sessions) |
| ed5f: dominants are better at displacing | reproduced over 13 sessions (91.7% against 60.2% of pushes, p = 0.0051; during the tone p = 0.0013) |
| ed5g: time displaced does not differ by rank | reproduced over 14 sessions (p = 0.359) |
| 26 claims needing neural data: the 21 single-unit claims, ED Fig. 7b, ED Fig. 8f-h, and the 3 HMM-GLM claims | blocked, metadata insufficient |
| 14 claims on data not deposited (unimplanted cohort, AlphaTracker evaluation frames, alone sessions, ex vivo, phototagging, optogenetics) | blocked, data missing |

## 2. What was found about the dataset

- **Spike times are on the wrong scale.** They are two thirds of their true time in the raw recording (divided by 30 kHz where the logger samples at 20 kHz). Multiplied by 1.5 they line up with the raw signal in 50 of 53 files.
- **The neural and behaviour clocks are offset, and the offset is missing.** In 18 of the 21 mPFC-LH files and one ephys file, the rescaled spikes match the raw recording only after an offset of 5 to 28 s. The offset between the neural recording and the tone, port-entry and label times is in no file, though the dataset description says a `video_gap` variable holds it. Estimated from the data it is 4 to 45 s, different in each session, and it cannot be estimated for 12 of the 38 files with port entries, or for the 10 ephys files, which have none.
- **The paper's cells cannot be identified.** All 5,879 Klusta clusters are labelled "unsorted", against the paper's 998 curated cells, and no rule on firing rate comes near 998. This is the main reason the single-unit claims are blocked.
- **One recording is deposited twice.** sub-20191025-chrimson2-3-1v3 and sub-20191029-chrimson2-3-1v3 have the same raw signal, with different units. Neither file is labelled, so no behavioural test uses them.
- **Behaviour data are incomplete.**
  - The 10 ephys files have no port entries, labels or poses.
  - In all 22 BLA files every pose value is missing.
  - Pose files never say which tracked mouse is the subject.
  - There is no port location.
- **Tone and reward times are a program schedule.** Tone times are the same in all files of a cohort. Reward delivery is 0.49 s after tone onset in every file, where the paper's Methods say 2 s.
- **Metadata errors:**
  - `pair_in_dataset` says "not included" in all 53 files, but 20 sessions have both mice's files.
  - One file has a wrong session date.
  - One subject description swaps the animal numbers.
- **The labelled data match the paper's HMM-GLM set:** 965 trials from 14 mice (paper: 965 trials, 13 mice).

Assumptions and questions:
- No outcome rests on an assumption (`assumed` is not set on any of them). The trial-winner rule from the Methods was run under two readings of a "switch" and both delivery times (2 s and 0.49 s); all gave the same outcomes.
- No questions for the paper's authors and none for a reader.

## 3. Where the protocol was unclear

1. **What counts as a session.** The paper's counts (31 and 32 sessions, 965 trials) fit one file per mouse better than unique competitions. I ran both readings where the measure allows.
2. **A claim that is half untestable.** ED Fig. 5c has a testable rewards part and a weight part with no data. The protocol has no rule for this, so I gave the outcome of the testable part and said so in the deviations.
3. **Choosing the main block reason for the HMM-GLM claims.** Two reasons apply: the missing clock offset (metadata insufficient) and the paper's MATLAB-only code (not runnable). I chose metadata insufficient and noted the code in the notes; I did not port the model.
4. **Estimating a missing clock offset from the data.** The protocol does not say whether an alignment estimated from neural responses may be used. I used it only to show the offset exists, not for any test.

## 4. Runtime and failures

The run took 12:00 to 13:52 UTC; the notebook takes about 9 minutes, most of it streaming parts of the raw recordings. Two errors in my own code were fixed before the final run: a column-name clash, and misreading the tone schedule and delivery times in the data check. Nothing failed in the final run.

Files are in `entries/001749-padilla-coreano-2022/`:
- `reproduce_padilla_coreano_2022.ipynb`
- `competition.py`
- `entry.yaml`
- `README.md`
- `requirements.in` and `requirements.lock.txt`

The record is `attempts/001749-padilla-coreano-2022-01.yaml`.
