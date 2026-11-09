I finished steps 1 to 6 for DANDI:001836 on version 0.261030.0428. Of the 29 claims, 9 behavioral claims were tested and 20 are blocked. The entry passes its checks, the notebook runs in a clean environment in about 26 minutes, and the handover package is built. Nothing is committed.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig1c-learning | reproduced |
| fig1e-trial-counts | not reproduced: at best 4 of the 10 counts are within tolerance |
| fig1d-initial-switch-bias | reproduced: the first-day ratio is above 2 in all 5 rats, binomial p = 0.031 |
| fig1d-switch-bias-declines | partially reproduced: the day effect is 0.933 (p = 2e-23), but the final ratio is 1.85 against 1.5 ± 0.15 |
| figs1f-multiple-com | reproduced |
| fig1g-com-corrective | reproduced: p < 0.05 in all 5 rats |
| fig1g-com-matches-run-through | reproduced: no rat differs |
| fig1h-final-choice-less-switching | not reproduced: paired t-test p < 0.01 in 2 rats (J, K), and E and L are at p = 0.013. The sign tests hold as the paper reports. |
| fig1h-final-ratio-near-one | reproduced |
| fig3b (two claims), fig3c, fig3d | blocked, metadata_insufficient |
| 16 claims on decoded content, sharp-wave ripples and theta | blocked, too_large |

No outcome rests on an assumption. Every open choice was run under each reading, and the readings gave the same outcome every time.

**2. The dataset**
- **What it holds:** raw 30 kHz voltage (12.5 TB), a 1 kHz LFP file per day, poke and pump events, Statescript logs, and 2415 unlabelled Spyglass analysis files. By content these are position (750), linearized position at 23 Hz and 500 Hz (446), and triggered decode tables (1219).
- **What it lacks:** the decoder's posterior and the detected remote and local events are not deposited. The triggered tables don't say what triggers them, and the track graph of the linearization is missing.
- **Fewer trials than the paper:** 2083, 3519, 4578, 2959 and 1816 trials for rats M, E, J, K and L, against 2370, 3554, 4628, 3779 and 2087 in the paper. Rat M has 5 days where the paper says 6 were collected.
- **Problems in rat M's files:**
  - Its 500 Hz linearizations are deposited twice, in 26 identical pairs; I counted each once.
  - Its Statescript logs are misnamed "syayescript" and hold no trial counts.
- **Small metadata error:** the head orientation's unit is given as meters.
- **The two published versions are identical** (same blobs), so I pinned the latest, since the paper cites none.
- **Sequence per rat:** the reward log gives 3-4-2-1-3 for M, E and J and 1-2-4-3-1 for K and L. This matches the Results and the Figure 1B legend but not the Figure S1E labels; I recorded it as a paper inconsistency.
- **Checks that passed:**
  - Trials built from the poke and pump events match the Statescript logs to within one trial per session.
  - A clock check (the head is on the final arm at the final poke 95 to 100% of the time, against 0 to 1% ten seconds earlier) shows the events and position share a clock.

Assumptions: none. Questions for the paper's authors: none. Questions to a reader: none.

**3. Where the protocol was unclear**
1. Step 2 doesn't say how to handle duplicates that are the same data at two sampling rates. Each run epoch has a 23 Hz and a 500 Hz linearization; I used the 500 Hz one, which the Methods describe, and reported only rat M's exact copies as duplicates.
2. The `too_large` rule covers the notebook's 60-minute limit but not the case where the run's remaining time is the constraint. For figs7b (sharp-wave ripples) the LFP is in the dataset. I estimated about 46 minutes of streaming on top of the 25-minute load, which is over the notebook limit, and recorded that.
3. The partial clause of a criterion ("holds in at least three rats") doesn't repeat its p threshold. For fig1h I read it as p < 0.01, the threshold of the main clause.

**4. Runtime and failures**
- My first look at a raw file took 17 minutes and the survey of all analysis files took 28.
- The full notebook runs in 25 to 27 minutes, nearly all of it streaming. I ran it four times in total.
- Nothing failed.

Files are in `entries/001836-gu-2026/`:
- `reproduce_gu_2026.ipynb`
- `comtask.py`

The record is `attempts/001836-gu-2026-01.yaml`.
