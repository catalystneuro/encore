## Report: DANDI:000115, Gillespie et al. 2021 (author steps 1 to 6)

I created the entry `entries/000115-gillespie-2021/`, the record `attempts/000115-gillespie-2021-01.yaml` and the questions file `questions/000115.yaml`, and built the handover. `entry.py check` reports 0 errors and the notebook runs clean. Nothing is committed.

### 1. Outcomes

| claim | outcome |
|---|---|
| fig1d-sessions-blocks | reproduced. Sessions are 25, 32, 24, 33 against 24, 32, 23, 33. Full blocks are 88 or 91, 85, 109, 167 or 166, against 89, 85, 105, 166. |
| fig1ef-reward-rate | reproduced. The rate on trial 1 is 0.068 to 0.133 and rises to 0.58 to 0.70 by trial 15. After the first reward, every lower bound is at least 0.234. |
| the other 31 claims (ripples, decoding, replay content, GLMs, controls) | blocked, `too_large` |

fig6b is blocked with fig6a because its criterion compares the visit decay with fig6a's replay curve. Every reading of both tested claims gives the same outcome.

### 2. The dataset

- **What it holds.** There are 57 files, about 9.1 TB. Each holds raw 30 kHz broadband (128 channels), port beam, light and pump events, position, and the StateScript task logs embedded as text.
- **What it lacks.** There are no spikes, LFP, ripple times, linearised position or decodes.
- **Streaming cost.** The raw data are stored one channel per chunk. Streaming them measured about 5 MB/s, so one 90-minute run epoch would take over 2 hours.
- **Trials rebuilt from the logs.**
  - Logged rewards equal the DIO pump onsets in 115 of 116 run epochs.
  - Rewards per block take only the programmed values.
  - Head position at each beam break identifies the arm (accuracy 1.0), against about 0.2 with a ±20 s shift.
- **Session counts.** All run epochs are the goal_delay task, and no log that states its parameters (111 of 116) sets forage assist. There are 27 and 24 run epochs for jaq and despereaux, where the paper used 26 and 23. The files don't mark which sessions the paper analysed.
- **Electrodes.** Every channel's location is "None", so the CA1 tetrodes and the reference tetrode can't be identified.
- **Position.** It is sampled at about 33 Hz, where the Methods say 30 Hz. 110 of 116 epochs end with NaN timestamps.
- **Two log anomalies.** In montague day 16 epoch 2 the log clock steps by about 3.4 s twice. In jaq day 6 epoch 4 the log stops before a final pump.
- **Version pinned.** I pinned 0.210914.1732, the only published version. In the draft, 55 of 57 files were rewritten in January 2022. In the file I compared, the draft's position timestamps are shifted by about -1.59e9 s off the DIO clock, while the DIO timestamps are unchanged.

**Questions asked (2):**
- Which jaq sessions are "sessions 1 and 3"? In recording order they are day 6 epochs 2 and 5. The session that fits the Methods' "not all arms visited" is day 6 epoch 4.
- Which trial closes a block when the rat doesn't go back to the old goal right after the switch?

I ran both readings of each, and none changes an outcome here.

### 3. Where the protocol was unclear or didn't fit

1. A variant that a criterion rules out: the criterion requires excluding two sessions, so excluding none is not a valid reading. I showed it labelled as a variant. It fails the jaq session count, and I recorded that in the notes.
2. Unused outside data: the paper's repository holds `ctrl_ripcontent.mat`, whose epoch lists may name the analysed sessions. The claims file doesn't list it as an input, so I looked at it only while preparing. It is mentioned in a finding without its numbers, and it decides nothing.
3. Step 1.6 says to ask even when every reading gives the same outcome. I asked anyway, and said in each question that the answer can't change this attempt's outcomes.
4. Step 1.3, choosing a version: the paper's code links the draft. The draft differs in content the analysis would use. I pinned the published version and showed the difference in the notebook.
5. Blocking when the input is the dataset itself: `not_runnable` covers outside inputs that are slow to fetch, but nothing covers a dataset too large to stream. I used `too_large` and put a measured throughput in the notebook to support it.
6. Judging "rises" in fig1ef: the criterion gives no test. I used trial 15 against trial 1 with non-overlapping bands, plus a Spearman correlation, printed both, and recorded this as a deviation.
7. A dependency that is only partly blocked: fig6b's visit curves can be computed from the logs. The protocol's rule (a claim depending on a blocked claim is blocked too) applies, so I blocked it and didn't compute them.

### 4. Runtime and failures

- **Runtime.** The notebook takes about 7.7 min, of which loading the 57 files is about 6.5 min.
- **Failures.** None in the final run. One bug was fixed during development: NaN position timestamps broke the position check.
- **Repo state.** Some dotfiles I didn't create (`.bashrc`, `.idea`, `scripts`, and others) show as untracked in the working tree. I left them alone.
